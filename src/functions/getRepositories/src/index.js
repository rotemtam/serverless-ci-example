'use strict';

const Repository = require('../../../model/Repository')
  , LambdaRunner = require('../../../lib/lambda-co-runner');

function *main(e) {
  let query = e.queryParams.q
    , res = yield Repository.search(query);
  return {items: res.items};
}

module.exports = {
  default: LambdaRunner(main)
}
