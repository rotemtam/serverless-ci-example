'use strict';

const chai = require('chai').use(require('sinon-chai'))
  , expect = chai.expect
  , sinon = require('sinon')
  , Repository = require('../../../model/Repository')
  , MockContext = require('../../../lib/mock-lambda-context')
  , getRepositories = require('../src/index').default;

require('co-mocha');
require('sinon-as-promised');

describe('getRepositories', function() {
  this.timeout(20000)
  let res, ctx;
  before(function() {
    sinon.stub(Repository, 'search').resolves({ items: [{}, {}, {}]});
  });

  before(function (done) {
    ctx = new MockContext();
    getRepositories({queryParams: {q: 'golang'}}, ctx, done);
  });

  it('should get repositories from github', function() {
    expect(ctx.succeed).calledWith({items: [{}, {}, {}]});
  });

  after(function() {
    Repository.search.restore();
  })


})
