'use strict';

const co = require('co');

module.exports = function(lambda) {
    return function(e, ctx, cb) {
        co(
            function* () {
                let result = yield lambda(e, ctx);

                if (cb) {
                    cb(null, result)
                }

                ctx.succeed(result);
            }
        )
        .catch(
            function(err){
                console.error(err);
                ctx.fail('Error: ' + err.message);
                if(cb) {
                    cb(err)
                }
            }
        );
    }
};
