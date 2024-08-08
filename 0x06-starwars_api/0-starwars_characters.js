#!/usr/bin/node

const request = require('request');

if (process.argv.length < 3) {
  console.error('Usage: ./0-starwars_characters.js <movie_id>');
  process.exit(1);
}

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error(`Error: ${response.statusCode}`);
    return;
  }

  const data = JSON.parse(body);
  data.characters.forEach(character => {
    request(character, (err, res, charBody) => {
      if (err) {
        console.error(err);
        return;
      }

      if (res.statusCode !== 200) {
        console.error(`Error: ${res.statusCode}`);
        return;
      }

      console.log(JSON.parse(charBody).name);
    });
  });
});
