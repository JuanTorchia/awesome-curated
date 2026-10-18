import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';

export function checkResult(name, observed) {
  const expected = JSON.parse(readFileSync(new URL('./expected.json', import.meta.url), 'utf8'))[name];
  assert.deepEqual(observed, expected, `${name}: observed result differs from expected.json`);
  console.log(JSON.stringify(observed));
}
