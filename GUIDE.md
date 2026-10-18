# Five small tool examples you can reproduce

Pick a problem, run a small fixture, and inspect the result before adding another dependency to a project. These examples cover structural code search, form validation, a model file, vector lookup and experiment metrics.

Tested on 18 October 2026 with synthetic inputs, in disposable Linux x86-64 containers. The checks were automated with AI assistance. The catalogue's existing review labels stay unchanged. Installation needs internet; the final checks ran with external networking disconnected.

```sh
git clone --branch practical-examples-2026-10-18-r2 --depth 1 https://github.com/JuanTorchia/awesome-curated.git
cd awesome-curated/examples/practical
```

[Install the pinned dependencies](examples/practical/README.md) before running the commands below. That file separates the Node.js and Python environments. [Versions and artifact checksums](examples/practical/versions.json) and [asserted results](examples/practical/expected.json) accompany the source. Python top-level versions are fixed; transitive Python dependencies are not fully locked.

## <a id="ast-grep"></a>Find a real call with ast-grep

A text search also finds `console.log` inside comments and strings. The [fixture](examples/practical/ast-grep.mjs) asks the JavaScript parser for a call expression and rewrites only that match.

```sh
npm ci
node ast-grep.mjs
```

With ast-grep **0.51.0**, the fixture finds **one** call and produces `logger.info("hello")`. The comment and string remain unchanged. `logger` is an illustrative target; this checks the syntax transformation, not whether replacing a logger preserves application behavior.

Use it when the pattern is about code structure. A repository-wide migration still needs tests for the behavior of the replacement. [Official ast-grep documentation](https://ast-grep.github.io/guide/quick-start.html).

## <a id="vest"></a>See which form fields fail with Vest

The [fixture](examples/practical/vest.mjs) runs two length rules against invalid input, then valid input.

```sh
node vest.mjs
```

With Vest **6.3.4**, the invalid fields are `["password", "username"]`; the valid run returns `hasErrors: false`. The example uses `suite.run`, the API documented for this version.

This is a validation-suite check, before connecting a form UI. It does not exercise asynchronous rules or define a production password policy. Server validation still needs its own implementation. [Vest documentation](https://vestjs.dev/docs/get_started).

## <a id="netron"></a>Open a model file with Netron

The [fixture](examples/practical/netron-example.py) creates an ONNX file with one `Relu` node and shape `[1, 3]`, starts Netron on loopback port 18080, and retrieves the page and model bytes.

```sh
/tmp/awesome-chroma-env/bin/python netron-example.py
```

Netron **9.3.2** and ONNX **1.23.2** served the **104-byte** model with HTTP **200** and identical bytes. Its SHA-256 is `b8f44a12ed8dff00d68bfb2fe6bee423dd7b100422c4ad6cf087b25af23a9c4e`.

This establishes that this small file can be served. No browser rendering or model inference was checked; the `Relu` node is verified in the generated ONNX file, not by a visual assertion. Port 18080 must be available. [Netron source and usage](https://github.com/lutzroeder/netron).

## <a id="chroma"></a>Query vectors without downloading an embedding model

The [fixture](examples/practical/chroma.py) inserts three explicit one-hot vectors and queries with a vector equal to the first.

```sh
/tmp/awesome-chroma-env/bin/python chroma.py
```

With Chroma **1.5.9**, the collection contains **3** records, returns `logs` as nearest and reports distance **0.0**.

Explicit vectors make the storage/query step easy to inspect separately from embedding generation. The exact-match toy query does not measure semantic search quality, persistence or scale. Data is ephemeral. [Chroma query documentation](https://docs.trychroma.com/docs/querying-collections/query-and-get).

## <a id="aim"></a>Read experiment metrics back with Aim

The [fixture](examples/practical/aim-example.py) records synthetic loss values, closes the run, reopens the repository and checks the stored sequence.

```sh
/tmp/awesome-aim-env/bin/python aim-example.py
```

With Aim **3.29.1**, the recorded result was **1** run, steps `[0, 1, 2]` and loss `[1.0, 0.5, 0.25]`. System tracking and terminal capture are disabled. The data is temporary; no model is trained and no tracker comparison is implied. [Aim tracking documentation](https://aimstack.readthedocs.io/en/latest/quick_start/setup.html).

## Where these examples fit

Choose the fixture that matches a task you already have. The [current catalogue](TOOLS.md) keeps review labels, limits and source traces; these dated examples are a separate reproduction package, not five new endorsements. The [18 October evidence snapshot](https://github.com/JuanTorchia/awesome-curated/blob/4d851df75e1aeeb861b2046ce4784d5706e7d548/data/latest.json) records the source coverage used for this selection.

[Español](GUIDE.es.md) · [Catalogue](TOOLS.md) · [Methodology](METHODOLOGY.md)
