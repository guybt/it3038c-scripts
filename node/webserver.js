const http = require("http");

const server = http.createServer((req, res) => {
  res.writeHead(200, {"Content-Type": "text/html"});

  res.end(`
  <!DOCTYPE html>
  <html>
    <head>
      <title>Node JS Response</title>
    </head>
    <body>
      <p>My name is Braiden</p>
    </body>
  </html>
  `)
})

server.listen(3000)

console.log("Server listening on port 3000")