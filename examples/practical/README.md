# Five small Awesome Curated examples — revision 2

These synthetic examples check one concrete behavior per tool. They are not
benchmarks, production deployments, security assessments, or evidence that Juan
personally used a tool. Existing catalogue verdicts are unchanged.

Use an isolated directory with Node.js 22, npm and Python 3.11 on Linux x86-64.
Installations need internet access. The examples themselves run without internet;
Netron uses a temporary loopback HTTP server, without opening a browser.
Dependencies are installed only in this directory/its virtual environments.

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

## Chroma and Netron

```sh
python3.11 -m venv /tmp/awesome-chroma-env
/tmp/awesome-chroma-env/bin/pip install --only-binary=:all: -r requirements.txt
/tmp/awesome-chroma-env/bin/python chroma.py
/tmp/awesome-chroma-env/bin/python netron-example.py
```

Chroma uses three explicit one-hot vectors and a query equal to the first. No
embedding model or model download is used; it checks storage/query plumbing,
not semantic retrieval quality, persistence, or scale. It uses ephemeral data.
Netron serves a generated 104-byte ONNX model containing one `Relu` node. The
example checks HTTP 200, the page title and identical model bytes. It does not
check browser rendering, visual node labels or inference. Port 18080 must be free.

## Aim

Use a separate environment. Aim's UI dependency is distributed as a source
archive; packaging that archive is allowed below, while native dependencies use
wheels. This environment is larger than the two JavaScript examples.

```sh
python3.11 -m venv /tmp/awesome-aim-env
/tmp/awesome-aim-env/bin/pip install --only-binary=:all: --no-binary=aim-ui aim==3.29.1 numpy==1.26.4
/tmp/awesome-aim-env/bin/python aim-example.py
```

Aim records synthetic values `[1.0, 0.5, 0.25]`, closes the run, then reads the
stored steps/values back in a second process. The reader reopens the disposable
run in normal mode; it is not a read-only audit. It uses the version-specific
`aim.storage.context.Context` API and `sequence.data.items_list()` to retrieve
original steps (raw array indices are not training steps). There is no trained
model or comparison of trackers.
System tracking and terminal capture are disabled. All temporary data is removed.

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
before the final execution. This is not an installation-security audit.
