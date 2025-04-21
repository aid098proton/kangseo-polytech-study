const express = require('express');
const http = require('http');
var app = express();
const port = 80;
const server = http.createServer(app).listen(port);

app.get('/test', function(req, res){
    res.send("hello world");
});