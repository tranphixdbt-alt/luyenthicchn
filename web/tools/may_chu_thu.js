// Máy chủ thử trên máy: phục vụ dist/ và chạy các hàm api/*.js giống Vercel (cần REDIS_URL trỏ tới redis-server).
// Chạy: REDIS_URL=redis://127.0.0.1:6379 ADMIN_KEY=... node web/tools/may_chu_thu.js [cổng]
const http = require('http'), fs = require('fs'), path = require('path');
const DIST = path.join(__dirname, '../dist'), API = path.join(__dirname, '../api'), PORT = +process.argv[2] || 8777;
const TYPES = { '.html': 'text/html; charset=utf-8', '.js': 'text/javascript', '.json': 'application/json', '.png': 'image/png', '.webmanifest': 'application/manifest+json' };
http.createServer((req, res) => {
  const url = new URL(req.url, 'http://x');
  if (url.pathname.startsWith('/api/')) {
    const name = url.pathname.slice(5).replace(/[^a-z-]/g, '');
    if (!fs.existsSync(path.join(API, name + '.js'))) { res.statusCode = 404; return res.end(); }
    req.headers['x-forwarded-for'] ||= req.socket.remoteAddress;   // như Vercel: IP người truy cập
    let raw = ''; req.on('data', c => (raw += c)); req.on('end', () => {
      try { req.body = raw && /json/.test(req.headers['content-type'] || '') ? JSON.parse(raw) : raw; } catch { req.body = raw; }
      res.status = c => { res.statusCode = c; return res; };
      res.json = o => { res.setHeader('content-type', 'application/json'); res.end(JSON.stringify(o)); };
      require(path.join(API, name + '.js'))(req, res);
    });
    return;
  }
  const f = path.join(DIST, url.pathname === '/' ? 'index.html' : path.normalize(url.pathname));
  if (!f.startsWith(DIST) || !fs.existsSync(f) || fs.statSync(f).isDirectory()) { res.statusCode = 404; return res.end(); }
  res.setHeader('content-type', TYPES[path.extname(f)] || 'application/octet-stream'); fs.createReadStream(f).pipe(res);
}).listen(PORT, () => console.log('http://localhost:' + PORT));
