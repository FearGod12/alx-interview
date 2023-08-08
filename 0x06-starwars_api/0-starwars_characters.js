#!/usr/bin/node

import request from "request";

let result = [];
let arg = process.argv[2];

request("https://swapi-api.alx-tools.com/api/films/" + arg, (error, response, body) => {
    if (error) {
        console.log(error);
    }

    console.log(response.statusCode);
    console.log(body);
});