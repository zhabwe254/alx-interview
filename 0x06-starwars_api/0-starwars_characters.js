#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(url, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  const film = JSON.parse(body);
  const characterUrls = film.characters;

  const getCharacterName = (characterUrl) => {
    return new Promise((resolve, reject) => {
      request(characterUrl, (error, response, body) => {
        if (error) {
          reject(error);
        } else {
          const character = JSON.parse(body);
          resolve(character.name);
        }
      });
    });
  };

  Promise.all(characterUrls.map(getCharacterName))
    .then((names) => {
      names.forEach((name) => console.log(name));
    })
    .catch((error) => {
      console.error('Error:', error);
    });
});
