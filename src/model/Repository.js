'use strict';

const request = require('axios');

function *search(query) {
  let options = {
    params: {
        q: query,
        sort: 'stars',
        order: 'desc'
    },
    headers: {
        'User-Agent': 'rotemtam'
    },
    responseType: 'json'
  };
  let res = yield request.get('https://api.github.com/search/repositories', options);
  return {items: res.data.items};
}

module.exports = {
  search: search
};
