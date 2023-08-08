#!/usr/bin/node

const request = require('request');
const util = require('util');

const promisified = util.promisify(request);
const names = [];
const arg = process.argv[2];

const url = 'https://swapi-api.alx-tools.com/api/films/' + arg;

async function main () {
  let response = await promisified(url);
  let body = JSON.parse(response.body);

  for (const nam of body.characters) {
    response = await promisified(nam);
    body = JSON.parse(response.body);
    names.push(body.name);
  }

  for (const each of names) {
    console.log(each);
  }
}

main();
