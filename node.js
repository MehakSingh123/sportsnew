const http = require('http');

const hostname = fs.readFileSync("/index.html", "utf-8");
const port = 3000; // You can change this to any available port you prefer

const server = http.createServer((req, res) => {
  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/plain');
  res.end('Hello, World!\n');
});

server.listen(port, hostname, () => {
  console.log(`Server running at http://${hostname}:${port}/`);
});
