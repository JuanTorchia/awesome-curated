import assert from 'node:assert/strict';
import { create, test, enforce } from 'vest';
const validate = create((data) => {
  test('username', 'Use at least 3 characters', () => enforce(data.username).longerThanOrEquals(3));
  test('password', 'Use at least 8 characters', () => enforce(data.password).longerThanOrEquals(8));
});
const invalid = validate.run({ username: 'ab', password: '123' });
assert.equal(invalid.hasErrors('username'), true);
assert.equal(invalid.hasErrors('password'), true);
const valid = validate.run({ username: 'ana', password: 'fixture-only-password' });
assert.equal(valid.hasErrors(), false);
console.log(JSON.stringify({ invalidFields: Object.keys(invalid.getErrors()).sort(), validHasErrors: valid.hasErrors() }));
