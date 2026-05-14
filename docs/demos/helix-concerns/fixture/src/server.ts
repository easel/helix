// DRIFT: imports node `http` instead of using Bun.serve().
// The typescript-bun concern requires Bun.serve(); align should flag this.
import http from "http";

const PORT = process.env.PORT ? parseInt(process.env.PORT, 10) : 3000;
const startTime = Date.now();

const server = http.createServer((req, res) => {
  if (req.url === "/health" && req.method === "GET") {
    const uptime = Math.floor((Date.now() - startTime) / 1000);
    res.writeHead(200, { "Content-Type": "application/json" });
    res.end(JSON.stringify({ status: "ok", uptime }));
    return;
  }
  res.writeHead(404);
  res.end("Not Found");
});

server.listen(PORT, () => {
  console.log(`server on :${PORT}`);
});
