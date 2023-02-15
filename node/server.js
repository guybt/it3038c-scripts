const http = require("http");
const fs = require("fs");
const os = require("os");
const ip = require("ip");


http.createServer((req, res) => {
  if (req.url === "/") {
      fs.readFile("index.html", "UTF-8", (err, body) => {
      res.writeHead(200, {"Content-Type": "text/html"});
      res.end(body);
    });
  } else if(req.url.match("/sysinfo")) {
    systemHostName = os.hostname();
    systemIP = ip.address();
    systemUptime = os.uptime();
    days = Math.floor(systemUptime / 86400);
    hours = Math.floor((systemUptime % 86400) / 3600);
    minutes = Math.floor(((systemUptime % 86400) % 3600) / 60);
    seconds = Math.floor(((systemUptime % 86400) % 3600) % 60);
    totalMemory = parseFloat((os.totalmem()/(1024 * 1024)).toFixed(2));    
    freeMemory = parseFloat((os.freemem()/(1024 * 1024)).toFixed(2));
    totalCPUs = os.cpus().length

    html=`
    <!DOCTYPE html>
    <html>
      <head>
        <title>Node JS Response</title>
      </head>
      <body>
        <p>Hostname: ${systemHostName}</p>
        <p>IP: ${systemIP}</p>
        <p>Server Uptime: ${days} days, ${hours} hours, ${minutes} minutes, ${seconds} seconds</p>
        <p>Total Memory: ${totalMemory} MB</p>
        <p>Free Memory: ${freeMemory} MB</p>
        <p>Number of CPUs: ${totalCPUs}</p>
      </body>
    </html>`
    res.writeHead(200, {"Content-Type": "text/html"});
    res.end(html);
  } else {
    res.writeHead(404, {"Content-Type": "text/plain"});
    res.end(`404 File Not Found at ${req.url}`);
  }
}).listen(3000);

console.log("Server listening on port 3000");