#!/usr/bin/node
const request = require('request');

const apiUrl = process.argv[2];
const characterId = '18';

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  const films = JSON.parse(body).results;
  const moviesWithWedge = films.filter(film =>
    film.characters.some(character => character.includes(characterId))
  );

  console.log(moviesWithWedge.length);
});
