'use strict';

const sinon = require('sinon');
require('sinon-as-promised');

module.exports = function mock() {
    this.succeed = sinon.stub();
    this.fail = sinon.stub();
};
