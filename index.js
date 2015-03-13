#!/bin/sh
':' //; exec "$(command -v node)" "$0" "$@"

var fs = require('fs');
var path = require('path');
var util = require('util');
var open = require('open');
var request = require('request');

var filepath = path.join(__dirname, 'ips.json');
var content = fs.readFileSync(filepath);

JSON.parse(content).forEach(function(ip) {
  var uri = util.format('http://%s', ip);
  request({uri: uri, method: 'HEAD'}, function(err, res, _) {
    return !err && res.statusCode === 200 && open(uri) && process.exit();
  });
});
