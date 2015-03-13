#!/bin/sh
':' //; exec "$(command -v node)" "$0" "$@"

var MAX_COCURRENCY = 200;

var fs = require('fs');
var path = require('path');
var util = require('util');
var open = require('open');
var request = require('request');
var queue = require('block-queue');

var filepath = path.join(__dirname, 'ips.json');
var content = fs.readFileSync(filepath);
var ips = JSON.parse(content);

var q = queue(MAX_COCURRENCY, function(ip, done) {
  var uri = util.format('http://%s', ip);
  request({uri: uri, method: 'HEAD'}, function(err, res, _) {
    return !err && res.statusCode === 200 && open(uri) && process.exit();
  });
  done();
});

for (var i = 0; i < ips.length; i++) {
  q.push(ips[i]);
}
