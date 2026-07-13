'use strict';

const ACCENT = { mate: 'var(--mate)', ciencias: 'var(--ciencias)', economia: 'var(--economia)', otro: 'var(--otro)', zapialab: 'var(--otro)' };
const KIND_LABEL = { guia: 'Guía profe', taller: 'Taller', beamer: 'Beamer', material: 'Material', imagen: 'Imagen', icono: 'Icono', libreria: 'TikZ', tema: 'Tema' };
const LICLASS = (l) => !l ? 'lic-none' : /dominio|cc0/i.test(l) ? 'lic-pd' : /by-sa/i.test(l) ? 'lic-sa' : /mit|cc by/i.test(l) ? 'lic-permissive' : 'lic-none';
const REPO = (p) => '/repo/' + p.split('/').map(encodeURIComponent).join('/');
const el = (t, c) => { const e = document.createElement(t); if (c) e.className = c; return e; };

let DATA = [];
const state = { q: '', f: { grupo: new Set(), tipo: new Set(), grado: new Set(), asig: new Set() } };

const DIMS = [
  { key: 'grupo', label: 'Sección', get: (r) => r.grupo },
  { key: 'asig', label: 'Asignatura', get: (r) => r.asignatura?.key, labelOf: (r) => r.asignatura?.label, accent: (r) => r.asignatura?.key },
  { key: 'grado', label: 'Grado', get: (r) => r.grado, labelOf: (r) => r.grado },
  { key: 'tipo', label: 'Tipo', get: (r) => r.tipo },
];

init();
async function init() {
  syncTheme();
  let payload;
  try { payload = await (await fetch('resources.json', { cache: 'no-store' })).json(); }
  catch (e) {
    document.getElementById('lede').textContent = 'No pude cargar resources.json. Corre `npm run index` en viewer/ y recarga.';
    return;
  }
  DATA = payload.resources;
  const m = payload.meta;
  document.getElementById('lede').textContent =
    `${m.total} recursos · ${m.conteos.conThumb} con vista previa. Filtra por sección, asignatura, grado o tipo; clic en una tarjeta para abrirla.`;
  document.getElementById('foot').innerHTML =
    `Índice generado el ${new Date(m.generado).toLocaleString('es-CO')} · el material vive en <code>material/</code> y <code>pdfs/</code> (fuera de git). ` +
    `Regenera con <code>npm run index</code>.`;
  buildFilters();
  document.getElementById('q').addEventListener('input', (e) => { state.q = e.target.value.toLowerCase().trim(); render(); });
  document.getElementById('clear2').addEventListener('click', clearAll);
  wireModal();
  render();
}

function buildFilters() {
  const host = document.getElementById('filters');
  host.innerHTML = '';
  for (const dim of DIMS) {
    const counts = {};
    const labels = {};
    const accents = {};
    for (const r of DATA) {
      const v = dim.get(r); if (v == null) continue;
      counts[v] = (counts[v] || 0) + 1;
      labels[v] = dim.labelOf ? dim.labelOf(r) : v;
      if (dim.accent) accents[v] = ACCENT[dim.accent(r)] || null;
    }
    const keys = Object.keys(counts).sort((a, b) => counts[b] - counts[a]);
    if (!keys.length) continue;
    const set = el('div', 'fset');
    const lab = el('span', 'flabel'); lab.textContent = dim.label; set.appendChild(lab);
    for (const k of keys) {
      const chip = el('button', 'chip');
      chip.type = 'button';
      chip.setAttribute('aria-pressed', 'false');
      if (accents[k]) { chip.style.setProperty('--c', accents[k]); const d = el('span', 'dot'); chip.appendChild(d); }
      chip.appendChild(document.createTextNode(labels[k]));
      const n = el('span', 'n'); n.textContent = counts[k]; chip.appendChild(n);
      chip.addEventListener('click', () => {
        const s = state.f[dim.key];
        if (s.has(k)) s.delete(k); else s.add(k);
        chip.setAttribute('aria-pressed', s.has(k) ? 'true' : 'false');
        render();
      });
      set.appendChild(chip);
    }
    host.appendChild(set);
  }
}

function matches(r) {
  for (const dim of DIMS) {
    const s = state.f[dim.key];
    if (s.size && !s.has(dim.get(r))) return false;
  }
  if (state.q) {
    const hay = [r.titulo, r.serie, r.tipo, r.grupo, r.ruta, r.asignatura?.label, r.licencia].join(' ').toLowerCase();
    if (!hay.includes(state.q)) return false;
  }
  return true;
}

function render() {
  const grid = document.getElementById('grid');
  const shown = DATA.filter(matches);
  document.getElementById('count').textContent =
    `${shown.length} de ${DATA.length} recursos` + (activeCount() ? ' · filtros activos' : '');
  document.getElementById('empty').hidden = shown.length > 0;
  grid.innerHTML = '';
  const frag = document.createDocumentFragment();
  for (const r of shown) frag.appendChild(card(r));
  grid.appendChild(frag);
}
const activeCount = () => Object.values(state.f).reduce((a, s) => a + s.size, 0) + (state.q ? 1 : 0);

function card(r) {
  const accent = ACCENT[r.asignatura?.key] || 'var(--muted)';
  const c = el('button', 'card'); c.type = 'button'; c.style.setProperty('--c', accent);
  const th = el('div', 'thumb' + (r.kind === 'icono' ? ' icon' : ''));
  const stripe = el('div', 'tstripe'); th.appendChild(stripe);
  if (r.thumb) {
    const img = el('img'); img.loading = 'lazy'; img.src = r.thumb; img.alt = r.titulo; th.appendChild(img);
  } else {
    const ph = el('div', 'ph');
    ph.innerHTML = `<span class="big">${r.kind === 'tema' ? '🎨' : r.kind === 'libreria' ? '△' : '📄'}</span>${r.tipo}`;
    th.appendChild(ph);
  }
  const meta = el('div', 'meta');
  const t = el('div', 'ctitle'); t.textContent = r.titulo; meta.appendChild(t);
  const tags = el('div', 'tags');
  const kind = el('span', 'tag kind'); kind.textContent = KIND_LABEL[r.kind] || r.tipo; tags.appendChild(kind);
  if (r.grado) { const g = el('span', 'tag'); g.textContent = r.grado; tags.appendChild(g); }
  if (r.serie) { const s = el('span', 'tag serie'); s.textContent = r.serie; s.title = r.serie; tags.appendChild(s); }
  if (r.licencia) { const l = el('span', 'lic ' + LICLASS(r.licencia)); l.textContent = r.licencia; tags.appendChild(l); }
  meta.appendChild(tags);
  c.appendChild(th); c.appendChild(meta);
  c.addEventListener('click', () => openModal(r));
  return c;
}

// ── modal ─────────────────────────────────────────────────────────────
let modal;
function wireModal() {
  modal = document.getElementById('modal');
  modal.querySelectorAll('[data-close]').forEach((x) => x.addEventListener('click', closeModal));
  document.addEventListener('keydown', (e) => { if (e.key === 'Escape') closeModal(); });
}
function openModal(r) {
  document.getElementById('m-title').textContent = r.titulo;
  document.getElementById('m-sub').textContent =
    [r.asignatura?.label, r.grado, r.serie, r.tipo].filter(Boolean).join(' · ');
  const openLink = document.getElementById('m-open');
  openLink.href = REPO(r.abrir);
  const body = document.getElementById('m-body');
  body.innerHTML = '';
  const ext = r.abrir.split('.').pop().toLowerCase();
  if (ext === 'pdf') {
    const f = el('iframe'); f.src = REPO(r.abrir); f.title = r.titulo; body.appendChild(f);
  } else if (['jpg', 'jpeg', 'png', 'svg'].includes(ext)) {
    const img = el('img'); img.src = REPO(r.abrir); img.alt = r.titulo; body.appendChild(img);
  } else {
    const box = el('div'); box.style.cssText = 'color:#e8e2d5;padding:40px;text-align:center';
    box.innerHTML = `<p style="font-size:2rem;margin:0 0 10px">📄</p><p>Fuente <b>${ext.toUpperCase()}</b> — ábrela en pestaña para ver el código.</p>`;
    body.appendChild(box);
  }
  // pie con licencia/crédito si aplica
  const old = modal.querySelector('.credit'); if (old) old.remove();
  if (r.licencia || r.autor) {
    const cr = el('div', 'credit');
    cr.innerHTML = `Licencia: <b>${r.licencia || '—'}</b>` + (r.autor ? ` · Autor/origen: ${r.autor}` : '') +
      ` · <span style="opacity:.7">${r.ruta}</span>`;
    modal.querySelector('.modal-card').appendChild(cr);
  }
  modal.hidden = false;
  document.body.style.overflow = 'hidden';
}
function closeModal() {
  modal.hidden = true;
  document.getElementById('m-body').innerHTML = '';
  document.body.style.overflow = '';
}

function clearAll() {
  state.q = ''; document.getElementById('q').value = '';
  for (const s of Object.values(state.f)) s.clear();
  document.querySelectorAll('.chip[aria-pressed="true"]').forEach((c) => c.setAttribute('aria-pressed', 'false'));
  render();
}

function syncTheme() {
  // respeta el toggle del host si estampara data-theme; si no, sigue el SO.
  const mq = window.matchMedia('(prefers-color-scheme: dark)');
  const apply = () => { if (!document.documentElement.dataset.theme) {/* deja el media query */} };
  mq.addEventListener?.('change', apply); apply();
}
