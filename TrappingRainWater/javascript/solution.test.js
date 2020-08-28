var assert = require("assert");
var { trap } = require("./solution.js");

describe('Trapping rain water works for', () => {
    it('empty', () => { assert.equal(trap([]), 0); });
    it('hill', () => { assert.equal(trap([0, 1, 2, 1, 0]), 0); });
    it('bowl', () => { assert.equal(trap([2, 1, 0, 1, 2]), 4); });
    it('normal', () => { assert.equal(trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]), 6); });
});
