#!/usr/bin/env node
// serve.mjs — Servidor estático mínimo (sin dependencias) para el visor.
// Sirve viewer/public/ y, además, expone la raíz del repo en /repo/ para
// poder abrir los PDFs/imágenes reales (que viven fuera de public/).
// Uso: node serve.mjs   →   http://localhost:4173

import http from 'node:http';
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const HERE = path.dirname(fileURLToPath(import.meta.url));
const PUBLIC = path.join(HERE, 'public');
const ROOT = path.resolve(HERE, '..');
const PORT = process.env.PORT || 4173;

const MIME = {
  '.html': 'text/html; charset=utf-8', '.js': 'text/javascript; charset=utf-8',
  '.css': 'text/css; charset=utf-8', '.json': 'application/json; charset=utf-8',
  '.pdf': 'application/pdf', '.jpg': 'image/jpeg', '.jpeg': 'image/jpeg',
  '.png': 'image/png', '.svg': 'image/svg+xml', '.tex': 'text/plain; charset=utf-8',
  '.md': 'text/plain; charset=utf-8',
};

function safeJoin(base, target) {
  const p = path.normalize(path.join(base, target));
  if (!p.startsWith(base)) return null; // fuera del sandbox
  return p;
}

http.createServer((req, res) => {
  let url = decodeURIComponent(req.url.split('?')[0]);
  let file;
  if (url.startsWith('/repo/')) {
    file = safeJoin(ROOT, url.slice('/repo/'.length));
  } else {
    if (url === '/') url = '/index.html';
    file = safeJoin(PUBLIC, url);
  }
  if (!file) { res.writeHead(403); return res.end('403'); }
  fs.stat(file, (err, st) => {
    if (err || !st.isFile()) { res.writeHead(404); return res.end('404 · ' + url); }
    res.writeHead(200, { 'Content-Type': MIME[path.extname(file).toLowerCase()] || 'application/octet-stream' });
    fs.createReadStream(file).pipe(res);
  });
}).listen(PORT, () => {
  console.log(`▸ Visor del kit en  http://localhost:${PORT}`);
  console.log('  (Ctrl-C para salir · recuerda correr `npm run index` primero)');
});
