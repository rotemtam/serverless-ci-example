'use strict';

const Repository = require('../../../model/Repository')
  , LambdaRunner = require('co-lambda-runner');

function *main(e) {
  let query = e.queryParams.q
    , res = yield Repository.search(query);
  return {items: res.items};
}

module.exports = {
  default: LambdaRunner(main)
}
