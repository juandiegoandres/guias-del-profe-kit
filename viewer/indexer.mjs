#!/usr/bin/env node
// indexer.mjs — Recorre el kit y genera public/resources.json + miniaturas.
// Uso: node indexer.mjs   (desde viewer/).  Sin dependencias externas.
//
// Genera para cada recurso: ruta, tipo, asignatura, grado, serie, título,
// licencia (si aplica) y una miniatura (thumbs/<slug>.jpg|png).
// Herramientas del sistema usadas si están: pdftoppm (PDF→jpg), sips (raster),
// rsvg-convert (svg→png). Si falta alguna, el recurso queda sin miniatura.

import { execFileSync } from 'node:child_process';
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const HERE = path.dirname(fileURLToPath(import.meta.url));
const ROOT = path.resolve(HERE, '..');           // raíz del repo
const PUBLIC = path.join(HERE, 'public');
const THUMBS = path.join(PUBLIC, 'thumbs');

fs.mkdirSync(THUMBS, { recursive: true });

// ── utilidades ────────────────────────────────────────────────────────
const has = (bin) => { try { execFileSync('/bin/bash', ['-c', `command -v ${bin}`], { stdio: 'ignore' }); return true; } catch { return false; } };
const TOOLS = { pdftoppm: has('pdftoppm'), sips: has('sips'), rsvg: has('rsvg-convert') };
const rel = (p) => path.relative(ROOT, p).split(path.sep).join('/');
const slug = (p) => rel(p).replace(/[\/ .]/g, '_');

function walk(dir, out = []) {
  let entries = [];
  try { entries = fs.readdirSync(dir, { withFileTypes: true }); } catch { return out; }
  for (const e of entries) {
    if (e.name.startsWith('.')) continue;
    const full = path.join(dir, e.name);
    if (e.isDirectory()) walk(full, out); else out.push(full);
  }
  return out;
}

// ── taxonomía ─────────────────────────────────────────────────────────
const GRADES = { '8': '8.º', '9': '9.º', '10-11': '10-11.º', 'zapialab': 'ZapiaLab' };
function gradeOf(r) {
  const m = r.match(/(?:^|\/)(10-11|8|9|zapialab)(?:\/|$)/);
  return m ? m[1] : null;
}
function subjectOf(r) {
  if (/economia/.test(r)) return { key: 'economia', label: 'Economía' };
  if (/matematicas|factorizacion|estadistica/.test(r)) return { key: 'mate', label: 'Matemáticas' };
  if (/fisica|ciencias|genetica|tabla-periodica|quimica|termo|reproduccion/.test(r)) return { key: 'ciencias', label: 'Ciencias' };
  if (/zapialab/.test(r)) return { key: 'zapialab', label: 'ZapiaLab' };
  return { key: 'otro', label: 'Otro' };
}
function seriesOf(r) {
  // La "serie" es la carpeta temática dentro de material/ o pdfs/.
  const parts = r.split('/');
  const i = parts.findIndex((p) => p === 'material' || p === 'pdfs');
  if (i < 0) return null;
  const rest = parts.slice(i + 1, -1); // sin el archivo
  // quita grado y 'ciencias'/'matematicas' genéricos, deja el tema
  const skip = new Set(['8', '9', '10-11', 'zapialab', 'ciencias', 'matematicas']);
  const topic = rest.filter((p) => !skip.has(p));
  return topic.length ? topic.join(' · ') : (rest[rest.length - 1] || null);
}
const DOCTYPES = [
  [/guia_profe/i, 'Guía del profe', 'guia'],
  [/(^|_)taller|worksheet/i, 'Taller', 'taller'],
  [/beamer/i, 'Beamer', 'beamer'],
  [/(^|_)guia(_|\.|$)|guia_eje/i, 'Guía', 'guia'],
  [/tablero/i, 'Tablero', 'taller'],
];
function docTypeOf(name) {
  for (const [re, label, kind] of DOCTYPES) if (re.test(name)) return { label, kind };
  return { label: 'Material', kind: 'material' };
}

const TITLECASE = (s) => s.replace(/[-_]/g, ' ').replace(/\b\w/g, (c) => c.toUpperCase());

// ── licencias desde los CREDITOS.md ───────────────────────────────────
// Devuelve un mapa "carpeta relativa" -> { archivo -> {licencia,autor} }
function parseCreditos() {
  const map = {};
  for (const f of walk(path.join(ROOT, 'assets', 'imgs'))) {
    if (!/CREDITOS.*\.md$/i.test(f)) continue;
    const dir = rel(path.dirname(f));
    map[dir] = map[dir] || {};
    const text = fs.readFileSync(f, 'utf8');
    for (const line of text.split('\n')) {
      if (!line.includes('|')) continue;
      const cells = line.split('|').map((c) => c.trim());
      // primer backtick = nombre de archivo
      const fileM = line.match(/`([^`]+\.(?:pdf|jpg|jpeg|png|svg))`/i);
      if (!fileM) continue;
      const fname = fileM[1];
      const licM = line.match(/(Dominio p[úu]blico|Public domain|CC0|CC BY[\- ]SA[\d. ]*|CC BY[\d. ]*|MIT)/i);
      const lic = licM ? licM[1].replace(/\s+/g, ' ').trim() : null;
      // autor = celda que no es el archivo, la licencia, ni vacía (heurístico)
      let autor = null;
      for (const c of cells) {
        if (!c || c.includes('`') || /Dominio|Public|CC0|CC BY|MIT|Licencia|Archivo|Autor|Contenido|---/i.test(c)) continue;
        if (c.length > 2 && c.length < 60) { autor = c; break; }
      }
      map[dir][fname] = { licencia: normLic(lic), autor };
    }
  }
  return map;
}
function normLic(l) {
  if (!l) return null;
  if (/dominio p|public domain/i.test(l)) return 'Dominio público';
  if (/cc0/i.test(l)) return 'CC0';
  if (/by[\- ]sa/i.test(l)) return 'CC BY-SA';
  if (/cc by/i.test(l)) return 'CC BY';
  if (/mit/i.test(l)) return 'MIT';
  return l;
}
const LICENSE_CLASS = (l) => {
  if (!l) return 'lic-none';
  if (/dominio|cc0/i.test(l)) return 'lic-pd';
  if (/by-sa/i.test(l)) return 'lic-sa';
  if (/mit|cc by/i.test(l)) return 'lic-permissive';
  return 'lic-none';
};

// ── miniaturas ────────────────────────────────────────────────────────
function thumbFor(abs) {
  const ext = path.extname(abs).toLowerCase();
  const base = slug(abs);
  try {
    if (ext === '.pdf' && TOOLS.pdftoppm) {
      const out = path.join(THUMBS, base); // pdftoppm añade -1.jpg
      execFileSync('pdftoppm', ['-jpeg', '-jpegopt', 'quality=70', '-f', '1', '-l', '1',
        '-scale-to-x', '360', '-scale-to-y', '-1', abs, out], { stdio: 'ignore' });
      // localizar el archivo generado (-1.jpg / -01.jpg)
      const dirents = fs.readdirSync(THUMBS).filter((n) => n.startsWith(path.basename(base) + '-') && n.endsWith('.jpg'));
      if (dirents.length) {
        const final = base + '.jpg';
        fs.renameSync(path.join(THUMBS, dirents[0]), path.join(THUMBS, final));
        return 'thumbs/' + final;
      }
    } else if ((ext === '.jpg' || ext === '.jpeg' || ext === '.png') && TOOLS.sips) {
      const final = base + ext;
      fs.copyFileSync(abs, path.join(THUMBS, final));
      execFileSync('sips', ['-Z', '400', path.join(THUMBS, final)], { stdio: 'ignore' });
      return 'thumbs/' + final;
    } else if (ext === '.svg' && TOOLS.rsvg) {
      const final = base + '.png';
      execFileSync('rsvg-convert', ['-w', '360', '-o', path.join(THUMBS, final), abs], { stdio: 'ignore' });
      return 'thumbs/' + final;
    }
  } catch { /* miniatura opcional */ }
  return null;
}

// ── recolección de recursos ───────────────────────────────────────────
const resources = [];
const creditos = parseCreditos();

// 1) PDFs compilados (el "producto" imprimible)
for (const abs of walk(path.join(ROOT, 'pdfs'))) {
  if (!abs.endsWith('.pdf')) continue;
  const r = rel(abs);
  const name = path.basename(abs, '.pdf');
  const dt = docTypeOf(path.basename(abs));
  resources.push({
    id: slug(abs), grupo: 'Paquetes de clase', tipo: dt.label, kind: dt.kind,
    grado: gradeOf(r), asignatura: subjectOf(r), serie: seriesOf(r),
    titulo: `${TITLECASE(name)}`, ruta: r, abrir: r, thumb: thumbFor(abs),
    licencia: null,
  });
}

// 2) Fuentes .tex del material (sin PDF equivalente: p. ej. subtemas)
for (const abs of walk(path.join(ROOT, 'material'))) {
  if (!abs.endsWith('.tex')) continue;
  const r = rel(abs);
  const name = path.basename(abs, '.tex');
  // ¿ya hay un PDF con el mismo nombre en pdfs/? entonces lo omitimos (evita duplicar)
  const dt = docTypeOf(path.basename(abs));
  resources.push({
    id: slug(abs), grupo: 'Fuentes LaTeX', tipo: dt.label, kind: dt.kind,
    grado: gradeOf(r), asignatura: subjectOf(r), serie: seriesOf(r),
    titulo: `${TITLECASE(name)} (fuente)`, ruta: r, abrir: r, thumb: null,
    licencia: null,
  });
}

// 3) Assets de imagen / iconos (con licencia)
for (const abs of walk(path.join(ROOT, 'assets', 'imgs'))) {
  const ext = path.extname(abs).toLowerCase();
  if (!['.pdf', '.jpg', '.jpeg', '.png'].includes(ext)) continue;
  const r = rel(abs);
  const dir = rel(path.dirname(abs));
  const fname = path.basename(abs);
  const cred = (creditos[dir] || {})[fname];
  const esImagen = ['.jpg', '.jpeg', '.png'].includes(ext) || (cred && /dominio|cc0|cc by/i.test(cred.licencia || ''));
  resources.push({
    id: slug(abs), grupo: esImagen ? 'Imágenes libres' : 'Iconos y vectores',
    tipo: esImagen ? 'Imagen libre' : 'Icono', kind: esImagen ? 'imagen' : 'icono',
    grado: gradeOf(r), asignatura: subjectOf(r), serie: path.basename(dir),
    titulo: TITLECASE(path.basename(fname, ext)), ruta: r, abrir: r,
    thumb: thumbFor(abs), licencia: cred ? cred.licencia : (esImagen ? null : 'MIT/CC BY'),
    autor: cred ? cred.autor : null,
  });
}

// 4) Librerías TikZ (+ preview si existe)
for (const abs of walk(path.join(ROOT, 'tikzlib'))) {
  if (!abs.endsWith('.tex')) continue;
  const r = rel(abs);
  const name = path.basename(abs, '.tex');
  const previewPng = path.join(ROOT, 'tikzlib', 'previews', name + '.png');
  const thumb = fs.existsSync(previewPng) ? thumbFor(previewPng) : null;
  resources.push({
    id: slug(abs), grupo: 'Librerías TikZ', tipo: 'Librería', kind: 'libreria',
    grado: null, asignatura: subjectOf(r), serie: path.basename(path.dirname(r)),
    titulo: TITLECASE(name), ruta: r, abrir: r, thumb, licencia: null,
  });
}

// 5) Temas de diseño
for (const abs of walk(path.join(ROOT, 'design'))) {
  if (!/tema-.*\.tex$/.test(abs)) continue;
  const r = rel(abs);
  resources.push({
    id: slug(abs), grupo: 'Temas de diseño', tipo: 'Tema', kind: 'tema',
    grado: null, asignatura: { key: 'otro', label: 'Sistema' }, serie: 'design',
    titulo: TITLECASE(path.basename(abs, '.tex')), ruta: r, abrir: r, thumb: null, licencia: null,
  });
}

// ── métricas + salida ─────────────────────────────────────────────────
const meta = {
  generado: new Date().toISOString(),
  total: resources.length,
  herramientas: TOOLS,
  conteos: {
    grupos: tally(resources.map((x) => x.grupo)),
    tipos: tally(resources.map((x) => x.tipo)),
    grados: tally(resources.map((x) => x.grado).filter(Boolean)),
    asignaturas: tally(resources.map((x) => x.asignatura?.label).filter(Boolean)),
    conThumb: resources.filter((x) => x.thumb).length,
  },
};
function tally(arr) { const m = {}; for (const a of arr) m[a] = (m[a] || 0) + 1; return m; }

fs.writeFileSync(path.join(PUBLIC, 'resources.json'), JSON.stringify({ meta, resources }, null, 1));
console.log(`✓ ${resources.length} recursos indexados · ${meta.conteos.conThumb} con miniatura`);
console.log('  grupos:', meta.conteos.grupos);
console.log('  herramientas:', TOOLS);
console.log('  → public/resources.json');
