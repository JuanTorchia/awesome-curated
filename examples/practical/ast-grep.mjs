import { execFileSync } from 'node:child_process';
import { mkdtempSync, writeFileSync, readFileSync, rmSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join } from 'node:path';
import assert from 'node:assert/strict';
const dir = mkdtempSync(join(tmpdir(), 'awesome-ast-'));
try {
  const path = join(dir, 'example.js');
  writeFileSync(path, '// console.log("comment")\nconst text = "console.log(123)";\nconsole.log("hello");\n');
  const cli = './node_modules/.bin/ast-grep';
  const matches = JSON.parse(execFileSync(cli, ['run', '--pattern', 'console.log($$$ARGS)', '--json=compact', path], { encoding: 'utf8' }));
  assert.equal(matches.length, 1);
  execFileSync(cli, ['run', '--pattern', 'console.log($$$ARGS)', '--rewrite', 'logger.info($$$ARGS)', '--update-all', path]);
  const after = readFileSync(path, 'utf8');
  assert.ok(after.includes('logger.info("hello")'));
  assert.ok(after.includes('// console.log("comment")'));
  assert.ok(after.includes('"console.log(123)"'));
  console.log(JSON.stringify({ matches: matches.length, rewritten: 'logger.info("hello")', commentAndStringUnchanged: true }));
} finally { rmSync(dir, { recursive: true, force: true }); }
