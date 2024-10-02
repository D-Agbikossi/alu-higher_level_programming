#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];

if (movieId) {
  const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;
  request(url, (err, response, body) => {
    if (err) {
      console.log(err);
    } else {
      const movie = JSON.parse(body);
      if (response.statusCode === 200) {
        console.log(movie.title);
      }
    }
  });
}
