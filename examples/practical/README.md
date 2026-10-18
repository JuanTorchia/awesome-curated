# Three small Awesome Curated examples — revision 3

These synthetic examples check one concrete behavior per tool. They are not
benchmarks, production deployments, security assessments, or evidence that Juan
personally used a tool. Existing catalogue verdicts are unchanged.

Revision 3 removes the Chroma and Aim examples. Their latest stable releases
have unresolved security advisories, so this package no longer installs or
recommends running them. The immutable older tags remain historical evidence,
not supported installation targets.

Use an isolated directory with Node.js 22, npm and Python 3.11 on Linux x86-64.
Installations need internet access. The examples themselves run without internet;
Netron uses a temporary loopback HTTP server, without opening a browser.
Dependencies are installed only in this directory or its virtual environment.

## ast-grep and Vest

```sh
npm ci
node ast-grep.mjs
node vest.mjs
```

ast-grep finds and rewrites one real call. The same text in a comment and string
stays unchanged. `logger` is an illustrative migration target, not an installed
logging library. The fixture tests a syntax rewrite, not behavioral equivalence.
Vest checks two length rules, with invalid and valid inputs. No UI, asynchronous
rules, password policy, or server trust boundary is evaluated.

## Netron

```sh
python3.11 -m venv /tmp/awesome-netron-env
/tmp/awesome-netron-env/bin/pip install --only-binary=:all: -r requirements.txt
/tmp/awesome-netron-env/bin/python netron-example.py
```

Netron serves a generated 104-byte ONNX model containing one `Relu` node. The
example checks HTTP 200, the page title and identical model bytes. It does not
check browser rendering, visual node labels or inference. Port 18080 must be free.

## Reproduction scope

Each script compares its full observed result with `expected.json` and exits
with an error on any difference. `check-result.mjs` and `check_result.py` load
that contract relative to their own file, independently of the working directory.
Netron extracts shape and node types from the served ONNX model.

See `expected.json` for the asserted observations and `versions.json` for tested
versions, base image digests and first-party package artifact checksums. The npm
lock pins the JavaScript dependency graph and integrity. Python top-level
versions are fixed; transitive Python dependencies are not fully locked, so
future installation resolution can differ. Results were checked on 2026-10-18
in disposable containers, as UID 10001 with external networking disconnected
before final execution. This is not an installation-security audit.
