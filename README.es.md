# Awesome Curated

<p align="center"><sub>Leer en otros idiomas: [🇬🇧 English](README.md) · **🇪🇸 Español** · [🇧🇷 Português (BR)](README.pt-BR.md) · [🇨🇳 中文](README.zh-CN.md) · [🇯🇵 日本語](README.ja.md)</sub></p>

> Lista **auto-curada** de herramientas de desarrollo. Harvest semanal de repos `awesome-*` activos en GitHub, deduplicado cross-fuente, clasificado por IA + veredicto humano.

**Última sincronización automática:** 2026-04-13

---

## 📊 Métricas

| Qué | Cuánto |
|---|---|
| Fuentes activas (ROSTER + BENCH) | **20** |
| Items totales scrapeados | **28,417** |
| Tools con señal cross-awesome (x≥2) | **1,479** |
| ⭐ GEMs (estándares de la industria) | **200** |
| 👍 Vale probar | **335** |

---

## 🎯 Cómo se curó

1. **Discovery**: GitHub API (GraphQL batched) detecta repos `awesome-*` mantenidos activamente.
2. **Scoring multidimensional**: freshness, actividad, popularidad, profundidad y salud de la comunidad ponderados en un único score.
3. **Dedupe cross-source**: items que aparecen en 2+ awesomes se agrupan en un `CuratedTool` único. `appearsInCount` es la señal de consenso.
4. **Clasificación IA**: Claude (Anthropic) asigna `GEM | WORTH_TRYING | MEH | HYPE | DEAD` con razonamiento por item.
5. **Veredicto humano**: un curador humano confirma o overridea las sugerencias IA. Tools con 👤 tienen veredicto humano.

Más detalle técnico → [Blog series en juanchi.dev](https://juanchi.dev/blog/series/awesome-curated)

---

## ⭐ GEMs — estándares de la industria
Herramientas que la comunidad considera default. Si no las conocés, valen la pena.

### AI Framework
- **[Vercel AI](https://github.com/vercel/ai)** — - Vercel AI is a TypeScript toolkit designed to help you build AI-powered applications using popular frameworks like Next.js, React, Svelte, Vue and runtimes like Node.js. — aparece en 3 listas · `typescript` `nextjs` `react` `llm-integration`

### API Code Generation
- **[OpenAPI Generator](https://github.com/openapitools/openapi-generator)** — OpenAPI Generator allows generation of API client libraries (e.g. C#, TypeScript, etc), server stubs (ASP.NET Core, NancyFx, etc), documentation and configuration automatically given an OpenAPI… · `openapi` `codegen` `api` `documentation`

### API Testing
- **[Postman](https://getpostman.com)** — GUI platform for API development. ![Freeware][Freeware Icon] · `api` `testing` `rest` `http`

### Advanced ML System
- **[Vowpal Wabbit](https://github.com/vowpalwabbit/vowpal_wabbit)** — Vowpal Wabbit is a machine learning system which pushes the frontier of machine learning with techniques such as online, hashing, allreduce, reductions, learning2search, active, and interactive… · `online-learning` `streaming` `c++` `ml-research`

### Algorithmic Trading
- **[Lean](https://github.com/quantconnect/lean)** — Lean Engine is an open-source fully managed C# algorithmic trading engine built for desktop and cloud usage. https://www.quantconnect.com/lean/ · `csharp` `trading` `backtesting` `quantitative`
- **[nautilus_trader](https://github.com/nautechsystems/nautilus_trader)** — `Python` `Rust` - A high-performance algorithmic trading platform and event-driven backtester. · `python` `rust` `trading` `backtesting`

### Anomaly Detection
- **[PyOD](https://github.com/yzhao062/pyod)** — > Python Outlier Detection, comprehensive and scalable Python toolkit for detecting outlying objects in multivariate data. Featured for Advanced models, including Neural Networks/Deep Learning and… · `python` `anomaly-detection` `machine-learning` `scikit-compatible`

### Anonymity Network
- **[Tor](https://torproject.org)** — Free software and onion routed overlay network that helps you defend against traffic analysis. · `anonymity` `overlay-network` `privacy` `c`

### Anonymity OS
- **[Tails](https://tails.boum.org)** — Live operating system aiming to preserve your privacy and anonymity. · `anonymity` `live-os` `privacy` `linux`

### Array Computing
- **[numpy](https://numpy.org)** — `Python` - NumPy is the fundamental package for scientific computing with Python. [GitHub](https://github.com/numpy/numpy) · `python` `arrays` `scientific-computing` `vectorization`

### Asset Discovery
- **[Shodan](https://shodan.io)** — Shodan is a search engine for the IOT(Internet of Things) that allows you to search variety of servers that are connected to the internet using various searching filters. · `iot-search` `vulnerability-scanning` `asset-discovery` `threat-intel`

### Backend Platform
- **[TrailBase](https://trailbase.io)** — Open, sub-millisecond, single-executable FireBase alternative with type-safe REST & realtime APIs, built-in JS/TS runtime, auth & admin UI. ) · `firebase-alternative` `rust` `self-hosted` `realtime`

### Backup & Recovery
- **[BorgBackup](https://github.com/borgbackup/borg)** — _(label: easy)_ <br> Deduplicating backup program with compression and authenticated encryption. · `backup` `deduplication` `encryption` `python`

### C++
- **[TensorFlow](https://github.com/tensorflow/tensorflow)** — - TensorFlow is a leading library designed for developing and deploying state-of-the-art machine learning applications. — 🔥 aparece en 6 listas · `machine-learning` `deep-learning` `python` `c++`
- **[LightGBM](https://github.com/microsoft/lightgbm)** — Microsoft's fast, distributed, high performance gradient boosting (GBDT, GBRT, GBM or MART) framework based on decision tree algorithms, used for ranking, classification and many other machine… — aparece en 3 listas · `machine-learning` `gradient-boosting` `distributed` `python`

### CI/CD Pipeline
- **[GitLab CI](https://about.gitlab.com/solutions/continuous-integration)** — Gitlab's built-in, full-featured CI/CD solution. · `cicd` `gitlab` `devops` `pipelines`

### CI/CD Platform
- **[Concourse](https://concourse-ci.org)** — Concourse is a CI tool that treats pipelines as first class objects and containerizes every step along the way. ) · `ci-cd` `go` `self-hosted` `open-source`

### Cloud Encryption
- **[Cryptomator](https://cryptomator.org)** — Multi-platform transparent client-side encryption of your files in the cloud. [![Open-Source Software][OSS Icon] ![Freeware][Freeware Icon]](https://github.com/cryptomator/cryptomator/) · `encryption` `client-side` `java` `cross-platform`

### Code Editor
- **[VSCodium](https://vscodium.com)** — An open source cross-platform extensible code editor based on [VS Code by Microsoft](https://code.visualstudio.com/) removing their non-free additions. · `code-editor` `open-source` `vscode` `typescript`
- **[Zed](https://zed.dev)** — A high-performance, multiplayer code editor from the creators of Atom and Tree-sitter. [![Open-Source Software][OSS Icon]](https://github.com/zed-industries/zed) ![Freeware][Freeware Icon] · `rust` `editor` `multiplayer` `performance`

### Code Quality
- **[astral-sh/ruff](https://github.com/astral-sh/ruff)** — An extremely fast Python linter and code formatter [](https://github.com/astral-sh/ruff/actions) · `linter` `formatter` `rust` `python`

### Command Line Tools
- **[fzf](https://github.com/junegunn/fzf)** — A general purpose command-line fuzzy finder, can be used with any list: files/directories, command history, processes, hostnames, bookmarks, git commits, etc. · `cli` `fuzzy-finder` `go` `unix-philosophy`

### Compiler Cache
- **[Sccache](https://github.com/mozilla/sccache)** — A fast compiler cache for C/C++, with cross-platform support and cloud backed storage options. · `compiler-cache` `c` `cpp` `build`

### Component Development
- **[Storybook JS](https://github.com/storybookjs/storybook)** — _(label: good first issue)_ <br> Storybook is a frontend workshop for building UI components and pages in isolation. · `ui-components` `documentation` `testing` `react-vue-angular`

### Computer Vision
- **[GoCV](https://github.com/hybridgroup/gocv)** — Package for computer vision using OpenCV 4 and beyond. · `go` `opencv` `computer-vision` `binding`

### Config Management
- **[SaltStack](https://github.com/saltstack/salt)** — _(label: good first issue)_ <br> Software to automate the management and configuration of any infrastructure or application at scale. · `orchestration` `configuration-management` `python` `devops`

### Container Monitoring
- **[cadvisor](https://github.com/google/cadvisor)** — Analyzes resource usage and performance characteristics of running containers. · `containers` `monitoring` `go` `kubernetes`

### Container Security
- **[Syft](https://github.com/anchore/syft)** — CLI tool and library for generating a Software Bill of Materials (SBOM) from container images and filesystems. By [Anchore](https://github.com/anchore). · `sbom` `container-security` `cli` `go`

### Cross Platform Mobile
- **[TiDB](https://github.com/pingcap/tidb)** — _(label: good first issue)_ <br> A distributed scalable Hybrid Transactional and Analytical Processing (HTAP) database · `dart` `flutter` `mobile` `cross-platform`

### Crypto Standard
- **[OpenSSL](https://github.com/openssl/openssl)** — A robust, commercial-grade, full-featured, and Open Source cryptography library. [Apache] [website](http://www.openssl.org/) · `openssl` `cryptography` `tls` `c`

### Cryptography Libraries
- **[s2n](https://github.com/awslabs/s2n)** — An implementation of the TLS/SSL protocols. [Apache] · `tls` `ssl` `cryptography` `c`

### Cryptography Library
- **[Bouncy Castle](https://bouncycastle.org/java.html)** — All-purpose cryptographic library and JCA provider offering a wide range of functions, from basic helpers to PGP/SMIME operations. · `java` `cryptography` `jca-provider` `pgp`
- **[Crypto++](https://github.com/weidai11/cryptopp)** — A free C++ class library of cryptographic schemes. [Boost] [website](http://www.cryptopp.com/) · `cpp` `cryptography` `production-ready`
- **[hashes](https://github.com/rustcrypto/hashes)** — Collection of cryptographic hash functions written in pure Rust. · `rust` `cryptography` `hashing` `library`
- **[libsodium](https://github.com/jedisct1/libsodium)** — P(ortable|ackageable) NaCl-based crypto library, opinionated and easy to use. [ISC] · `cryptography` `nacl` `security` `c`
- **[pynacl](https://github.com/pyca/pynacl)** — Python binding to the Networking and Cryptography (NaCl) library. · `cryptography` `python` `nacl` `bindings`
- **[Tink](https://github.com/google/tink)** — A multi-language, cross-platform library that provides cryptographic APIs that are secure, easy to use correctly, and hard(er) to misuse. [Apache-2.0] · `cryptography` `multi-language` `secure-by-default`

### DL Framework
- **[PyTorch Lightning](https://github.com/lightning-ai/pytorch-lightning)** — - PyTorch Lightning pretrains, finetunes and deploys AI models on multiple GPUs, TPUs with zero code changes. · `pytorch` `deep-learning` `distributed-training` `python`

### Data Analysis
- **[pandas](https://pandas.pydata.org)** — `Python` - pandas is an open source, BSD-licensed library providing high-performance, easy-to-use data structures and data analysis tools for the Python programming language.… · `dataframe` `data-analysis` `python` `performance`

### Data Interchange Format
- **[protobuf](https://github.com/protocolbuffers/protobuf)** — Protocol Buffers - Google's data interchange format. [BSD] · `serialization` `rpc` `schema` `multi-language`

### Data Libraries
- **[pandas](https://github.com/pandas-dev/pandas)** — _(label: good first issue)_ <br> Flexible and powerful data analysis / manipulation library for Python, providing labeled data structures similar to R data.frame objects, statistical functions,… · `python` `data-science` `pandas` `dataframe`

### Data Orchestration
- **[Apache Airflow](https://github.com/apache/airflow)** — - Data Pipeline framework built in Python, including scheduler, DAG definition and a UI for visualisation. · `python` `dag` `scheduler` `etl`

### Data Processing
- **[DataFrames](https://github.com/juliadata/dataframes.jl)** — library for working with tabular data in Julia. · `julia` `dataframes` `data-science` `tabular`
- **[pola-rs/polars](https://github.com/pola-rs/polars)** — Fast feature complete DataFrame library [](https://github.com/pola-rs/polars/actions) · `rust` `dataframe` `performance` `data-science`

### Data Quality
- **[cleanlab](https://github.com/cleanlab/cleanlab)** — - Python library for data-centric AI. Can automatically: find mislabeled data, detect outliers, estimate consensus + annotator-quality for multi-annotator datasets, suggest which data is best to… · `python` `data-quality` `ml-monitoring` `label-errors`

### Data Transformation Tool
- **[dbt-labs/dbt-core](https://github.com/dbt-labs/dbt-core)** — Project banner, super clear description (friendly to people brand new to the product), screenshot of the docs the tool generates, and concise links to other comprehensive pages explaining Getting… · `data-engineering` `sql` `python` `analytics`

### Data Visualization
- **[matplotlib](https://github.com/matplotlib/matplotlib)** — - A Python 2D plotting library which produces publication-quality figures in a variety of hardcopy formats and interactive environments across platforms. — aparece en 3 listas · `feature-engineering` `python` `sklearn` `ml`
- **[Streamlit](https://github.com/streamlit/streamlit)** — - Streamlit lets you create apps for your machine learning projects with deceptively simple Python scripts. It supports hot-reloading, so your app updates live as you edit and save your file. — aparece en 3 listas · `python` `web-framework` `ml-apps` `rapid-prototyping`
- **[Apache ECharts](https://github.com/apache/echarts)** — - Apache ECharts is a powerful, interactive charting and data visualization library for browser. · `dataviz` `javascript` `interactive` `charts`
- **[Chart.js](https://chartjs.org)** — a javascript library that allows you to create charts easly · `javascript` `charts` `visualization` `canvas`
- **[Plotly](https://github.com/plotly/plotly.py)** — - An interactive, open source, and browser-based graphing library for Python. · `data-visualization` `python` `interactive` `web-based`
- **[seaborn](https://github.com/mwaskom/seaborn)** — - Seaborn is a Python visualization library based on matplotlib. It provides a high-level interface for drawing attractive statistical graphics. · `visualization` `matplotlib` `statistical-graphics` `python`
- **[Seaborn](https://seaborn.pydata.org)** — A python visualization library based on matplotlib. · `visualization` `matplotlib` `statistical-graphics` `pandas`

### Database CLI
- **[pgcli](https://github.com/dbcli/pgcli)** — Postgres client with autocompletion and syntax highlighting. · `cli` `postgres` `python` `repl`

### Deep Learning
- **[Stable Baselines](https://github.com/dlr-rm/stable-baselines3)** — - A fork of OpenAI Baselines, implementations of reinforcement learning algorithms. — aparece en 3 listas · `reinforcement-learning` `python` `pytorch` `tensorflow`

### Deep Learning Library
- **[oneDNN](https://github.com/oneapi-src/onednn)** — An open-source cross-platform performance library for deep learning applications. [Apache] [website](https://01.org/onednn) · `deep-learning` `cpp` `cpu-optimization` `gpu`

### Dependency Security
- **[safedep/vet](https://github.com/safedep/vet)** — 🎖️ 🏎️ ☁️ 🍎 🪟 🐧 - vet-mcp checks open source packages—like those suggested by AI coding tools—for vulnerabilities and malicious code. It supports npm and PyPI, and runs locally via Docker or… · `mcp` `dependency-check` `security` `npm`

### Desktop GUI Toolkit
- **[GTK+](https://gtk.org)** — A multi-platform toolkit for creating graphical user interfaces. [LGPL] · `gui` `gtk` `cross-platform` `linux`

### Developer Tools
- **[Docker](https://docker.com)** — Powerful, performs operating-system-level virtualization. [![Open-Source Software][OSS Icon]](https://github.com/docker) ![Freeware][Freeware Icon] [![Awesome List][awesome-list… — aparece en 4 listas · `containers` `devops` `virtualization`
- **[mitmproxy](https://mitmproxy.org)** — A Python tool used for intercepting, viewing and modifying network traffic. Invaluable in troubleshooting certain problems. — aparece en 3 listas · `python` `proxy` `debugging` `security`
- **[Wireshark](https://wireshark.org)** — The world’s foremost and widely-used network protocol analyzer. [![Open-Source Software][OSS Icon]](https://github.com/wireshark/wireshark) ![Freeware][Freeware Icon] — aparece en 3 listas · `network` `pcap` `wireshark` `cli-gui`

### Development Tools
- **[Visual Studio Code](https://code.visualstudio.com)** — Microsoft's free & open-source editor, TypeScript friendly, [VSCode Plugins](editor-plugin.md#vscode-plugin). [![Open-Source Software][OSS Icon]](https://github.com/Microsoft/vscode)… — aparece en 4 listas · `editor` `typescript` `vscode-plugins`

### Disk Analysis
- **[dust](https://github.com/bootandy/dust)** — A more intuitive version of `du` in Rust. · `rust` `cli` `disk-analysis` `unix-tool`

### Distributed Computing
- **[RLlib](https://github.com/ray-project/ray)** — RLlib is an industry level, highly scalable RL library for tf and torch, based on Ray. It's used by companies like Amazon and Microsoft to solve real-world decision making problems at scale. — aparece en 3 listas · `reinforcement-learning` `ray` `python` `distributed`

### Distributed Data Processing
- **[Dask](https://github.com/dask/dask)** — - Distributed parallel processing framework for Pandas and NumPy computations. · `python` `distributed-computing` `pandas` `numpy`

### Distributed Database
- **[TiKV](https://github.com/tikv/tikv)** — _(label: difficulty/easy)_ <br> A distributed transactional key-value database · `rust` `distributed-db` `kvstore` `transactional`

### Distributed Processing
- **[Flink](https://flink.apache.org)** — Open source platform for distributed stream and batch data processing. · `java` `distributed-computing` `stream-processing` `apache`

### Distributed Storage
- **[Kubo](https://github.com/ipfs/kubo)** — Implementation of IPFS, a global, versioned, peer-to-peer filesystem that seeks to connect all computing devices with the same system of files. · `ipfs` `p2p` `go` `distributed`

### Distributed Store
- **[etcd](https://github.com/etcd-io/etcd)** — Distributed reliable key-value store for the most critical data of a distributed system by [etcd-io](https://github.com/etcd-io) (former part of CoreOS). · `distributed` `key-value` `go` `consensus`

### Distributed Systems
- **[ZooKeeper](https://zookeeper.apache.org)** — ZooKeeper is a centralized service for maintaining configuration information, naming, providing distributed synchronization, and providing group services. — aparece en 3 listas · `java` `distributed-coordination` `apache` `consensus`

### Docker SDK
- **[Docker.DotNet](https://github.com/microsoft/docker.dotnet)** — C#/.NET HTTP client for the Docker remote API. · `csharp` `dotnet` `docker-api` `client-library`

### EBook Manager
- **[Calibre](https://calibre-ebook.com)** — E-book library manager that can view, convert, and catalog e-books in most of the major e-book formats and provides a built-in Web server for remote clients. ) · `ebook` `conversion` `python` `pyqt`

### Embedded Python
- **[MicroPython](https://github.com/micropython/micropython)** — Aims to put an implementation of Python 3.x on a microcontroller. [MIT] · `python` `microcontroller` `embedded` `iot`

### Encryption CLI
- **[gpg](https://gnupg.org)** — Complete and free implementation of the OpenPGP standard. It allows to encrypt and sign your data and communication, features a versatile key management system. GnuPG is a command line tool with… · `gpg` `encryption` `cli` `openpgp`

### Experiment Tracking
- **[Sacred](https://github.com/idsia/sacred)** — Python tool to help you configure, organize, log and reproduce experiments. Like a notebook lab in the context of Chemistry/Biology. The community has built multiple add-ons leveraging the… · `python` `reproducibility` `ml-experiment` `logging`

### Fast Hashing
- **[xxHash](https://github.com/cyan4973/xxhash)** — Extremely fast non-cryptographic hash algorithm. [BSD-2-Clause] [website](https://xxhash.com/) · `hashing` `performance` `non-crypto` `c`

### File Search
- **[sharkdp/fd](https://github.com/sharkdp/fd)** — A simple, fast and user-friendly alternative to find. [](https://github.com/sharkdp/fd/actions/workflows/CICD.yml) · `cli` `rust` `files` `search`

### File Sharing
- **[Samba](https://samba.org)** — Samba is the standard Windows interoperability suite of programs for Linux and Unix. It provides secure, stable and fast file and print services for all clients using the SMB/CIFS protocol.… · `c` `file-sharing` `smb-cifs` `production`

### File Utilities
- **[sharkdp/bat](https://github.com/sharkdp/bat)** — A cat(1) clone with wings. [](https://github.com/sharkdp/bat/actions/workflows/CICD.yml) · `cli` `rust` `files` `syntax-highlighting`

### Finance Data
- **[edgartools](https://github.com/dgunning/edgartools)** — `Python` - AI-native SEC EDGAR library with XBRL financials, clean text extraction, 17+ typed forms, and pandas DataFrames. · `python` `sec` `xbrl` `fintech`

### Frontend Framework
- **[svelte](https://github.com/sveltejs/svelte)** — Svelte is a new way to build web applications. It's a compiler that takes your declarative components and converts them into efficient JavaScript that surgically updates the DOM. · `javascript` `compiler` `reactive` `ui`

### Game Engine
- **[Godot Engine](https://github.com/godotengine/godot)** — _(label: good first issue)_ <br> 2D and 3D cross-platform game engine. Also has C# and Python code. · `cpp` `gamedev` `csharp` `cross-platform`

### Geospatial Data
- **[OpenStreetMap](https://openstreetmap.org)** — Collaborative project to create a free editable map of the world. ) · `geospatial` `osm` `collaborative` `maps`

### Go
- **[Kubernetes](https://github.com/kubernetes/kubernetes)** — _(label: good first issue)_ <br> Production-Grade Container Scheduling and Management System — aparece en 3 listas · `kubernetes` `container-orchestration` `go` `distributed-systems`
- **[Moby](https://github.com/moby/moby)** — Collaborative project for the container ecosystem to assemble container-based systems. — aparece en 3 listas · `go` `containers` `docker` `open-source`

### GraphQL Engine
- **[Hasura GraphQL Engine](https://github.com/hasura/graphql-engine)** — _(label: good first issue)_ <br> Blazing fast, instant realtime GraphQL APIs on Postgres with fine grained access control, also trigger webhooks on database events. · `haskell` `graphql` `postgres` `realtime`

### HTTP Debugging
- **[mitmproxy](https://github.com/mitmproxy/mitmproxy)** — _(label: help-wanted)_ <br> An interactive TLS-capable intercepting HTTP proxy for penetration testers and software developers · `proxy` `http` `https` `security`

### HTTP Library
- **[hyperium/hyper](https://github.com/hyperium/hyper)** — an HTTP implementation [](https://github.com/hyperium/hyper/actions?query=workflow%3ACI) · `rust` `http` `async` `networking`

### High Performance Networking
- **[uWebSockets](https://github.com/unetworking/uwebsockets)** — µWS is one of the most lightweight, efficient & scalable WebSocket & HTTP server implementations available. [Zlib] · `networking` `websocket` `http` `cpp`

### Hyperparameter Tuning
- **[Optuna](https://github.com/optuna/optuna)** — - Optuna is an automatic hyperparameter optimisation software framework, particularly designed for machine learning. · `hyperparameter-optimization` `bayesian-search` `ml-pipeline`

### IDE Apple
- **[Xcode](https://developer.apple.com/xcode)** — Essential IDE for iOS/macOS development. [![App Store][app-store Icon]](https://apps.apple.com/app/id497799835?platform=mac) · `ide` `swift` `ios` `macos`

### Identity Management
- **[KeyCloak](https://keycloak.org)** — Open Source Identity and Access Management. · `iam` `oauth2` `java` `self-hosted`

### Immediate Mode GUI
- **[imgui](https://github.com/ocornut/imgui)** — Immediate Mode Graphical User Interface with minimal dependencies. [MIT] · `cpp` `immediate-mode-gui` `graphics`

### In Memory Database
- **[Redis](https://github.com/redis/redis)** — Redis is an open-source, in-memory data store that supports vector similarity search, making it suitable for AI/ML applications such as semantic search and recommendation systems. · `database` `in-memory` `cache` `vector-search`

### Infrastructure Automation
- **[Ansible](https://github.com/ansible/ansible)** — _(label: easyfix)_ <br> A simple IT automation platform · `infrastructure-as-code` `automation` `ssh` `python`

### Interactive Computing
- **[Jupyter](https://github.com/markusschanta/awesome-jupyter)** — Create and share documents that contain code, equations, visualizations and narrative text. · `notebook` `interactive` `python` `research`

### JVM IDE
- **[IntelliJ IDEA](https://jetbrains.com/idea)** — Powerful IDE for JVM languages. (**Free** for Students) · `ide` `java` `kotlin` `jvm`

### Java Build Tool
- **[Apache Maven](https://maven.apache.org)** — Build automation tool mainly for Java. A software project management and comprehension tool. Based on the concept of a project object model (POM), Maven can manage a project's build, reporting and… · `java` `build-automation` `dependency-management` `xml`
- **[Gradle](https://gradle.org)** — Incremental builds programmed via Groovy instead of declaring XML. Works well with Maven's dependency management. · `java` `build-automation` `groovy` `incremental`

### JavaScript
- **[Jest](https://github.com/facebook/jest)** — _(label: good first issue)_ <br> A complete and easy to set up JavaScript testing solution. — 🔥 aparece en 5 listas · `testing` `javascript` `typescript` `mocking`
- **[Next.js](https://github.com/vercel/next.js)** — _(label: good first issue)_ <br> A minimalistic framework for universal server-rendered React applications — 🔥 aparece en 5 listas · `react` `ssr` `typescript` `full-stack`
- **[Netron](https://github.com/lutzroeder/netron)** — - Netron is a viewer for neural network, deep learning and machine learning models. — aparece en 4 listas · `neural-networks` `visualization` `ml-models`
- **[Vite](https://github.com/vitejs/vite)** — _(label: good first issue)_ <br> Next generation frontend tooling. It's fast! Alternative to Create React App — aparece en 4 listas · `build-tool` `frontend` `javascript` `typescript`
- **[Babel](https://github.com/babel/babel)** — _(label: good first issue)_ <br> A compiler for writing next generation JavaScript. — aparece en 3 listas · `javascript` `transpiler` `babel` `ast`
- **[D3js](https://d3js.org)** — is a powerful data visualization javascript library. — aparece en 3 listas · `javascript` `visualization` `svg` `data-driven`
- **[ESLint](https://github.com/eslint/eslint)** — _(label: good first issue)_ <br> A fully pluggable tool for identifying and reporting on patterns in JavaScript. — aparece en 3 listas · `javascript` `linting` `eslint` `typescript`
- **[React Native](https://github.com/facebook/react-native)** — _(label: Good-first-issue)_ <br> A framework for building native apps with React. — aparece en 3 listas · `javascript` `react` `mobile` `cross-platform`
- **[Vue.js](https://github.com/vuejs/vue)** — _(label: good first issue)_ <br> The Progressive JavaScript Framework. — aparece en 3 listas · `javascript` `vue` `spa` `frontend`

### JavaScript Runtime
- **[Node.js](https://github.com/sindresorhus/awesome-nodejs)** — Async non-blocking event-driven JavaScript runtime built on Chrome's V8 JavaScript engine. — aparece en 4 listas · `nodejs` `javascript` `runtime`
- **[Node.js core](https://github.com/nodejs/node)** — _(label: good first issue)_ <br> JavaScript runtime built on Chrome's V8 JavaScript engine · `javascript` `runtime` `backend` `v8`

### JavaScript UI Library
- **[React](https://github.com/facebook/react)** — _(label: good first issue)_ <br> A declarative, efficient, and flexible JavaScript library for building user interfaces. · `javascript` `ui-library` `component-based` `jsx`

### Knowledge Management
- **[Obsidian](https://obsidian.md)** — Obsidian is a powerful knowledge base on top of a local folder of plain text Markdown files. — aparece en 4 listas · `markdown` `local-first` `knowledge-base` `self-hosted`

### Kubernetes Management
- **[k9s](https://github.com/derailed/k9s)** — Kubernetes CLI to manage your clusters in style. · `kubernetes` `cli` `golang` `devops`

### LLM Fine Tuning
- **[PEFT](https://github.com/huggingface/peft)** — - Parameter-Efficient Fine-Tuning (PEFT) methods enable efficient adaptation of pre-trained language models (PLMs) to various downstream applications without fine-tuning all the model's parameters. · `fine-tuning` `lora` `transformers` `python`

### LLM Serving Engine
- **[vLLM](https://github.com/vllm-project/vllm)** — - vLLM is a high-throughput and memory-efficient inference and serving engine for LLMs. · `llm-inference` `serving` `cuda` `python`

### Local LLM Runtime
- **[Ollama](https://github.com/ollama/ollama)** — - Get up and running with large language models, locally. · `llm` `local-inference` `docker` `go`

### ML CI/CD
- **[CML](https://github.com/iterative/cml)** — A library for doing continuous integration with ML projects. Use GitHub Actions & GitLab CI to train and evaluate models in production like environments and automatically generate visual reports… · `ci-cd` `mlops` `github-actions` `gitops`

### ML Library
- **[scikit-learn](https://scikit-learn.org)** — A Python module for machine learning built on top of SciPy. · `python` `machine-learning` `scikit-learn` `scipy`

### ML Monitoring
- **[Evidently](https://github.com/evidentlyai/evidently)** — - Evidently is an open-source framework to evaluate, test and monitor ML and LLM-powered systems. · `python` `mlops` `monitoring` `data-drift`

### ML Research
- **[Dlib](https://github.com/davisking/dlib)** — zap: - A toolkit for making real world machine learning and data analysis applications in C++. [Boost] [website](http://dlib.net/) · `python` `automatic-differentiation` `jit-compiler` `numpy-compatible`

### ML/Explainability
- **[InterpretML](https://github.com/interpretml/interpret)** — InterpretML implements the Explainable Boosting Machine (EBM), a modern, fully interpretable machine learning model based on Generalized Additive Models (GAMs). This open-source package also… · `interpretable-ml` `python` `glass-box` `visualization`

### Machine Learning
- **[BayesWitnesses/m2cgen](https://github.com/bayeswitnesses/m2cgen)** — A CLI tool to transpile trained classic machine learning models into a native Rust code with zero dependencies. [](https://github.com/BayesWitnesses/m2cgen/actions) — 🔥 aparece en 7 listas · `machine-learning` `code-generation` `model-export` `open-source`
- **[XGBoost](https://github.com/dmlc/xgboost)** — - XGBoost is an optimized distributed gradient boosting library designed to be highly efficient, flexible and portable. — 🔥 aparece en 5 listas · `machine-learning` `gradient-boosting` `python` `distributed`
- **[Apache Spark](https://github.com/apache/spark)** — - Micro-batch processing for streams using the apache spark framework as a backend supporting stateful exactly-once semantics. — aparece en 3 listas · `ai-agents` `memory` `python` `storage`
- **[Jax](https://github.com/jax-ml/jax)** — - Composable transformations of Python+NumPy programs: differentiate, vectorize, JIT to GPU/TPU, and more. · `python` `ml` `jit` `gpu`

### Media Center
- **[Kodi](https://kodi.tv)** — Multimedia/Entertainment center, formerly known as XBMC. Runs on Android, BSD, Linux, macOS, iOS and Windows. · `multimedia` `open-source` `cross-platform` `htpc`

### Media Player
- **[mpv](https://mpv.io)** — Free, open-source, and cross-platform media player. [![Open-Source Software][OSS Icon]](https://github.com/mpv-player/mpv) ![Freeware][Freeware Icon] · `media-player` `open-source` `cli-friendly` `cross-platform`

### Message Broker
- **[ActiveMQ](https://activemq.apache.org)** — Java message broker. · `java` `message-broker` `messaging` `apache`

### Metadata Analysis
- **[ExifTool](https://sno.phy.queensu.ca/~phil/exiftool)** — Platform-independent Perl library plus a command-line application for reading, writing and editing meta information in a wide variety of files. · `metadata` `cli` `perl` `forensics`

### Monitoring TSDB
- **[Prometheus](https://prometheus.io)** — Service monitoring system and time series database. · `monitoring` `tsdb` `go` `open-source`

### Music Library Manager
- **[beets](https://github.com/beetbox/beets)** — A music library manager and [MusicBrainz](https://musicbrainz.org/) tagger. · `audio` `metadata` `python` `cli`

### NLP Tokenization
- **[huggingface/tokenizers](https://github.com/huggingface/tokenizers)** — Hugging Face's tokenizers for modern NLP pipelines (original implementation) with bindings for Python. [](https://github.com/huggingface/tokenizers/actions) · `nlp` `tokenization` `rust` `huggingface`

### Natural Language Processing
- **[SpaCy](https://github.com/explosion/spacy)** — - spaCy is a library for advanced Natural Language Processing in Python and Cython. — aparece en 3 listas · `nlp` `python` `spacy` `nlp-pipeline`

### Network Tools
- **[scapy](https://github.com/secdev/scapy)** — Python-based interactive packet manipulation program and library. · `python` `networking` `packets` `security`

### Node Process Mgr
- **[pm2](https://github.com/unitech/pm2)** — Production Process Manager for Node.js. · `node.js` `process-manager` `production` `clustering`

### OSINT Automatizado
- **[SpiderFoot](https://spiderfoot.net)** — SpiderFoot is an open source intelligence (OSINT) automation platform with over 200 modules for threat intelligence, attack surface monitoring, security assessments and asset discovery. · `osint` `automation` `threat-intel` `asset-discovery`

### OSINT Basico
- **[Google Hacking Database (GHDB)](https://exploit-db.com/google-hacking-database)** — The GHDB is an index of search queries (we call them dorks) used to find publicly available information, intended for pentesters and security researchers. · `osint` `google-dorking` `recon` `pentesting`

### Object Detection
- **[YOLOv8](https://github.com/ultralytics/ultralytics)** — Ultralytics' YOLOv8 implementation with C++ support for real-time object detection and tracking, optimized for edge devices. · `yolo` `object-detection` `python` `cpp`

### P2P Sync
- **[Syncthing](https://syncthing.net)** — Syncthing is an open source peer-to-peer file synchronisation tool. · `sync` `p2p` `self-hosted` `go`

### Package Manager
- **[Homebrew](https://brew.sh)** — The missing package manager for macOS. ![Freeware][Freeware Icon] [![Open-Source Software][OSS Icon]](https://github.com/Homebrew/brew/) · `package-manager` `macos` `cli` `open-source`

### Password Manager
- **[vaultwarden](https://github.com/dani-garcia/vaultwarden)** — ](https://github.com/dani-garcia/vaultwarden/actions/workflows/build.yml) - Alternative implementation of the Bitwarden server API written in Rust · `password-manager` `rust` `self-hosted` `security`

### Penetration Testing
- **[Social Engineer Toolkit (SET)](https://github.com/trustedsec/social-engineer-toolkit)** — Open source pentesting framework designed for social engineering featuring a number of custom attack vectors to make believable attacks quickly. · `pentesting` `social-engineering` `framework` `python`
- **[SQLMap](https://github.com/sqlmapproject/sqlmap)** — An automatic SQL injection and database takeover tool. · `penetration-testing` `sql-injection` `python` `automation`

### Pentesting Recursos
- **[SecLists](https://github.com/danielmiessler/seclists)** — Collection of multiple types of lists used during security assessments. · `wordlist` `payload` `pentesting` `curado`

### Performance
- **[Numba](https://github.com/numba/numba)** — - A compiler for Python array and numerical functions. · `jit-compiler` `numpy` `performance` `scientific-computing`

### Privacy ML
- **[PySyft](https://github.com/openmined/pysyft)** — - A Python library for secure, private Deep Learning. PySyft decouples private data from model training, using Multi-Party (MPC) within PyTorch. · `privacy-preserving` `federated-learning` `python` `pytorch`

### Project Scaffolding
- **[cookiecutter](https://github.com/cookiecutter/cookiecutter)** — _(label: good first issue)_ <br> A command-line utility that creates projects from cookiecutters (project templates). E.g. Python package projects, jQuery plugin projects. · `cli` `scaffolding` `templating` `python`

### Python
- **[Pytorch](https://github.com/pytorch/pytorch)** — _(label: good first issue)_ <br> PyTorch is an open source machine learning library based on the Torch library, used for applications such as computer vision and natural language processing. — 🔥 aparece en 6 listas · `deep-learning` `machine-learning` `python` `gpu`
- **[Jupyter Notebooks](https://github.com/jupyter/notebook)** — - Web interface python sandbox environments for reproducible development — aparece en 3 listas · `python` `jupyter` `notebook` `interactive`
- **[PyG](https://github.com/pyg-team/pytorch_geometric)** — - PyG (PyTorch Geometric) is a library built upon PyTorch to easily write and train Graph Neural Networks (GNNs) for a wide range of applications related to structured data. — aparece en 3 listas · `gnn` `pytorch` `python` `ml`
- **[scikit-learn](https://github.com/scikit-learn/scikit-learn)** — - Scikit-learn is a powerful machine learning library that provides a wide variety of modules for data access, data preparation and statistical model building. — aparece en 3 listas · `python` `machine-learning` `sklearn` `supervised`
- **[SymPy](https://github.com/sympy/sympy)** — _(label: Easy-to-Fix)_ <br> A Python library for symbolic mathematics. — aparece en 3 listas · `python` `mathematics` `symbolic-computation` `open-source`
- **[Transformers](https://github.com/huggingface/transformers)** — - Huggingface's library of state-of-the-art pretrained models for Natural Language Processing (NLP). — aparece en 3 listas · `python` `nlp` `transformers` `pytorch`

### Python CV
- **[Detectron2](https://github.com/facebookresearch/detectron2)** — - Detectron2 is Facebook AI Research's next generation library that provides state-of-the-art detection and segmentation algorithms. · `python` `computer-vision` `detection` `segmentation`

### Python Optimization
- **[Cython](https://github.com/cython/cython)** — Cython is an optimising static compiler for both the Python programming language and the extended Cython programming language (based on Pyrex). It makes writing C extensions for Python as easy as… · `python` `c-extension` `compiler` `optimization`

### Python Testing
- **[Pytest](https://github.com/pytest-dev/pytest)** — _(label: status:-easy)_ <br> The pytest framework makes it easy to write small tests, yet scales to support complex functional testing. · `testing` `python` `fixtures` `assertions`

### Python Typing
- **[mypy](https://github.com/python/mypy)** — _(label: good first issue)_ <br> Optional static typing for Python. · `static-typing` `python` `linter`

### Quantitative Finance
- **[QuantLib](https://github.com/lballabio/quantlib)** — The QuantLib project is aimed at providing a comprehensive software framework for quantitative finance. · `quantitative-finance` `cpp` `pricing` `risk`

### R Visualization
- **[ggplot2](https://ggplot2.tidyverse.org)** — A data visualization package based on the grammar of graphics. · `r` `visualization` `grammar-of-graphics` `data-science`

### RAG Framework
- **[LlamaIndex](https://github.com/run-llama/llama_index)** — - LlamaIndex (GPT Index) is a data framework for your LLM application. · `rag` `retrieval` `llm-framework` `python`

### RL Framework
- **[Gymnasium](https://github.com/farama-foundation/gymnasium)** — - Gymnasium is an open source Python library for developing and comparing reinforcement learning algorithms by providing a standard API to communicate between learning algorithms and environments,… · `reinforcement-learning` `python` `api-standard` `simulation`

### Real Time OLAP DB
- **[Druid](https://druid.apache.org)** — Distributed, column-oriented, real-time analytics data store. · `olap` `timeseries` `column-store` `java`

### Reinforcement Learning
- **[TF-Agents](https://github.com/tensorflow/agents)** — - A reliable, scalable and easy to use TensorFlow library for contextual bandits and reinforcement learning. · `reinforcement-learning` `tensorflow` `python` `contextual-bandits`

### Remote Desktop
- **[RustDesk](https://github.com/rustdesk/rustdesk)** — [99332⭐] - Open source virtual / remote desktop. TeamViewer alternative. Built with Rust by [RustDesk team](https://www.rustdesk.com/). · `remote-desktop` `rust` `open-source` `self-hosted`

### Reverse Proxy
- **[Træfɪk](https://github.com/containous/traefik)** — Automated reverse proxy and load-balancer for Docker, Mesos, Consul, Etcd... By [EmileVauge](https://github.com/emilevauge). · `reverse-proxy` `load-balancer` `docker` `kubernetes`

### Rust Cryptography
- **[briansmith/ring](https://github.com/briansmith/ring)** — Safe, fast, small crypto using Rust and BoringSSL's cryptography primitives. · `rust` `crypto` `boringssl` `tls`

### Rust Node Bridge
- **[Neon](https://github.com/neon-bindings/neon)** — Rust bindings for writing safe and fast native Node.js modules. · `rust` `node.js` `native-bindings` `ffi`

### SQL IDE
- **[DataGrip](https://jetbrains.com/datagrip)** — DataGrip is a cross-platform IDE that is aimed at DBAs and developers working with SQL databases. It has built-in drivers that support DB2, Derby, H2, HSQLDB, MySQL, Oracle, PostgreSQL, SQL… · `sql` `ide` `dba` `jetbrains`

### Scientific Computing
- **[ROOT](https://root.cern.ch)** — A modular scientific software framework. It provides all the functionalities needed to deal with big data processing, statistical analysis, visualization and storage. · `cpp` `scientific-computing` `big-data` `statistics`
- **[scipy](https://scipy.org)** — `Python` - SciPy (pronounced “Sigh Pie”) is a Python-based ecosystem of open-source software for mathematics, science, and engineering. [GitHub](https://github.com/scipy/scipy) · `python` `scientific-computing` `numpy-dependent`

### Security Analysis
- **[Virus Total](https://virustotal.com)** — Free service that analyzes suspicious files and URLs and facilitates the quick detection of viruses, worms, trojans, and all kinds of malware. · `malware` `osint` `antivirus` `saas`

### Security Audit
- **[Lynis](https://cisofy.com/lynis)** — Auditing tool for UNIX-based systems. · `security` `audit` `unix` `cli`

### Self Hosted Cloud
- **[Nextcloud](https://nextcloud.com)** — Access and share your files, calendars, contacts, mail and [more](https://apps.nextcloud.com/) from any device, on your terms. ) · `cloud-storage` `self-hosted` `php` `docker`

### Service Mesh
- **[Consul](https://consul.io)** — Consul is a tool for service discovery, monitoring and configuration. · `service-discovery` `go` `distributed` `configuration`

### Shell Navigation
- **[ajeetdsouza/zoxide](https://github.com/ajeetdsouza/zoxide)** — A fast alternative to `cd` that learns your habits [](https://github.com/ajeetdsouza/zoxide/actions) · `rust` `cli` `shell` `productivity`

### Speech Processing
- **[EspNet](https://github.com/espnet/espnet)** — ESPnet is an end-to-end speech processing toolkit for tasks like speech recognition, translation, and enhancement, using PyTorch and Kaldi-style data processing. · `speech-processing` `pytorch` `asr` `end-to-end`
- **[Wav2Letter++](https://github.com/facebookresearch/wav2letter)** — Public domain, a fast open source speech processing toolkit written entirely in C++ and uses the ArrayFire tensor library and the flashlight machine learning library for maximum efficiency. [BSD] · `c++` `lua` `speech-processing` `audio`

### Speech Recognition
- **[Kaldi](https://github.com/kaldi-asr/kaldi)** — Kaldi is a toolkit for speech recognition written in C++ and licensed under the Apache License v2.0. Kaldi is intended for use by speech recognition researchers. · `speech-recognition` `asr` `c++` `toolkit`

### Statistical Modeling
- **[statsmodels](https://github.com/statsmodels/statsmodels)** — Statistical modelling and econometrics in Python. · `python` `statistics` `econometrics` `timeseries`

### TLS Certificate Validation
- **[webpki](https://github.com/briansmith/webpki)** — Web PKI TLS X.509 certificate validation in Rust. · `rust` `tls` `x509` `pkix`

### Task Management CLI
- **[Taskwarrior](https://taskwarrior.org)** — Taskwarrior is Free and Open Source Software that manages your TODO list from your command line. It is flexible, fast, efficient, and unobtrusive. It does its job then gets out of your way. · `cli` `productivity` `task-management` `c++`

### Test Automation
- **[Selenium](https://github.com/christian-bromann/awesome-selenium)** — Open-source browser automation framework and ecosystem. · `browser-automation` `testing` `webdriver` `cross-browser`

### Testing
- **[cypress](https://github.com/cypress-io/cypress)** — _(label: good first issue)_ <br> Fast, easy and reliable testing for anything that runs in a browser. · `javascript` `testing` `e2e` `browser-automation`

### Testing E2E
- **[Playwright](https://github.com/microsoft/playwright)** — Node.js library to automate Chromium, Firefox and WebKit with a single API. — aparece en 4 listas · `testing` `e2e` `automation` `browser`

### Text Editor
- **[Vim](https://vim.org)** — An old terminal-based editor. For common plugins, check [Vim Common Plugins](editor-plugin-zh.md#vim-plugin). [![Open-Source Software][OSS Icon]](https://github.com/vim/vim) ![Freeware][Freeware… · `editor` `terminal` `modal` `unix`

### Time Series Analysis
- **[tsfresh](https://github.com/blue-yonder/tsfresh)** — - Automatic extraction of relevant features from time series. · `python` `timeseries` `feature-engineering` `ml`

### Tools
- **[DVC](https://github.com/iterative/dvc)** — Data Science Version Control is an open-source version control system for machine learning projects with pipelines support. It makes ML projects reproducible and shareable. — aparece en 3 listas · `data-science` `version-control` `ml-pipelines`

### Torrent Client
- **[qBittorrent](https://qbittorrent.org)** — A project aims to provide an open-source software alternative to µTorrent. [![Open-Source Software][OSS Icon]](https://github.com/qbittorrent/qBittorrent) ![Freeware][Freeware Icon] · `torrent` `open-source` `cross-platform` `bittorrent`

### TypeScript
- **[Visual Studio Code](https://github.com/microsoft/vscode)** — New type of tool that combines the simplicity of a code editor with what developers need for their core edit-build-debug cycle. Code provides comprehensive editing and debugging support, an… — aparece en 4 listas · `editor` `typescript` `open-source` `debugging`

### Utilities
- **[Bitwarden](https://bitwarden.com)** — Open source password management tool for Mac OS, iOS and browsers. [![Open-Source Software][OSS Icon]](https://github.com/bitwarden) ![Freeware][Freeware Icon] — aparece en 3 listas · `password-manager` `security` `open-source` `self-hosted`

### Vector Computing
- **[ashvardanian/NumKong](https://github.com/ashvardanian/numkong)** — SIMD-accelerated vector distances and similarity functions for x86 AVX2 & AVX-512, and Arm NEON [](https://crates.io/crates/simsimd) · `rust` `simd` `vector-search` `avx512`

### Vector Database
- **[Milvus](https://github.com/milvus-io/milvus)** — Milvus is a cloud-native, open-source vector database built to manage embedding vectors generated by machine learning models and neural networks. · `vector-database` `embeddings` `cloud-native` `python`
- **[Qdrant](https://github.com/qdrant/qdrant)** — An open source vector similarity search engine with extended filtering support [](https://github.com/qdrant/qdrant/actions) · `vector-db` `rust` `similarity-search` `filtering`

### Vector Similarity Search
- **[Faiss](https://github.com/facebookresearch/faiss)** — - Faiss is a library for efficient similarity search and clustering of dense vectors. · `machine-learning` `similarity-search` `vector-db` `gpu`

### Web Browser
- **[Safari](https://apple.com/safari)** — Native browser for Macs. ![Freeware][Freeware Icon] [![Awesome List][awesome-list Icon]](https://github.com/learn-anything/safari-extensions#readme) · `browser` `webkit` `macos` `native`

### Web Log Analyzer
- **[GoAccess](https://goaccess.io)** — Real-time web log analyzer and interactive viewer that runs in a terminal or through the browser. `MIT` `C` · `web-analytics` `log-parser` `cli` `c`

### Web Mapping Library
- **[Leaflet](https://github.com/leaflet/leaflet)** — _(label: good first issue)_ <br> JavaScript library for mobile-friendly interactive maps. · `mapping` `geospatial` `javascript` `lightweight`

### Web Scraping
- **[scrapy](https://github.com/scrapy/scrapy)** — _(label: good first issue)_ <br> A fast high-level web crawling & scraping framework for Python. · `python` `scraping` `web-crawling` `framework`

### Web Servers
- **[grpc](https://github.com/grpc/grpc)** — Remote Procedure Calls (RPCs) provide a useful abstraction for building distributed applications and services. The libraries in this repository provide a concrete implementation of the gRPC… — aparece en 3 listas · `rpc` `http2` `distributed-systems` `protobuf`

### Workspace Platform
- **[Notion](https://notion.so)** — All-in-one workspace for your notes, tasks, wikis, and databases. · `saas` `workspace` `collaborative` `closed-source`

---

## 👍 Vale probar — sólidas en su nicho
Menos hype que las GEMs, pero confiables si caés en su caso de uso.

### .NET Optimization
- **[GeneticSharp](https://github.com/giacomelli/geneticsharp)** — Multi-platform genetic algorithm library for.NET Core and.NET Framework. The library has several implementations of GA operators, like: selection, crossover, mutation, reinsertion and termination. · `dotnet` `genetic-algorithm` `optimization` `csharp`

### AI Agent CLI
- **[agent-of-empires](https://github.com/njbrake/agent-of-empires)** — A TUI/CLI for managing multiple AI coding agent sessions with tmux, git worktrees, and Docker sandboxing [](https://github.com/njbrake/agent-of-empires/actions) · `cli` `tui` `ai-agents` `rust`

### AI Agent Environment
- **[Nimbalyst](https://nimbalyst.com)** — An agent management environment for Claude Code and Codex. Interactive visual editing of markdown, mockups, excalidraw, code. Parallel session management. · `ai-agents` `claude` `visual-editing` `markdown`

### AI Assistant Unifier
- **[askbudi/roundtable](https://github.com/askbudi/roundtable)** — 📇 ☁️ 🏠 🍎 🪟 🐧 - Meta-MCP server that unifies multiple AI coding assistants (Codex, Claude Code, Cursor, Gemini) through intelligent auto-discovery and standardized MCP interface, providing… · `mcp` `ai-assistants` `claude` `cursor`

### AI Code Editor
- **[Cursor](https://cursor.com)** — An IDE with chat, edit, generate and debug features. Forked from VSCodium, so the interface is similar to VS Code. Uses OpenAI. · `ai-ide` `vscode-fork` `chat` `code-generation`
- **[Windsurf](https://windsurf.com)** — An IDE with chat, edit, generate and debug features. Forked from VSCodium, so the interface is similar to VS Code. Formerly known as Codeium. · `ide` `ai-coding` `electron` `vscode-fork`

### AI Dev Tools
- **[kagan-sh/kagan](https://github.com/kagan-sh/kagan)** — ](https://glama.ai/mcp/servers/kagan-sh/kagan) 🐍 🏠 🍎 🪟 🐧 - AI-powered Kanban TUI and MCP server for autonomous development workflows. Orchestrates 14 coding agents across task tracking,… · `mcp` `tui` `kanban` `ai-agents`

### AI Infrastructure
- **[MCP Memory Service](https://github.com/doobidoo/mcp-memory-service)** — Universal memory service with semantic search, autonomous consolidation, and multi-client support for AI applications. · `mcp` `memory` `semantic-search` `ai-agents`

### AI Memory Layer
- **[Mem0](https://github.com/mem0ai/mem0)** — - Mem0 enhances AI assistants and agents with an intelligent memory layer, enabling personalized AI interactions. — aparece en 3 listas · `ai-memory` `python` `agents` `llm`

### AI Skills Kit
- **[Superpowers](https://github.com/obra/superpowers)** — by [Jesse Vincent](https://github.com/obra) - A strong bundle of core competencies for software engineering, with good coverage of a large portion of the SDLC - from planning, reviewing, testing,… · `prompt-engineering` `sdlc` `best-practices` `claude`

### API Testing
- **[ATAC](https://github.com/julien-cpsn/atac)** — A feature-full TUI API client made in Rust. ATAC is free, open-source, offline and account-less. · `api-client` `tui` `rust` `rest`

### AWS CLI Tools
- **[s5cmd](https://github.com/peak/s5cmd)** — Blazing fast S3 and local filesystem execution tool. · `cli` `s3` `go` `parallel`

### Agent Infrastructure
- **[dagger/container-use](https://github.com/dagger/container-use)** — 🏎️ 🏠 🐧 🍎 🪟 - Containerized environments for coding agents. Multiple agents can work independently, isolated in fresh containers and git branches. No conflicts, many experiments. Full… · `containers` `agents` `ci-cd` `dagger`

### Algorithmic Trading
- **[StockSharp](https://github.com/stocksharp/stocksharp)** — `CSharp` - Algorithmic trading and quantitative trading open source platform to develop trading robots (stock markets, forex, crypto, bitcoins, and options). · `csharp` `trading` `forex` `crypto`

### Anonymity
- **[I2P](https://geti2p.net)** — The Invisible Internet Project. · `anonymity` `p2p` `overlay-network` `privacy`

### Applications
- **[Sniffnet](https://github.com/gyulyvgc/sniffnet)** — Cross-platform application to monitor your network traffic with ease [](https://github.com/GyulyVGC/sniffnet/blob/main/.github/workflows/rust.yml) [](https://crates.io/crates/sniffnet) — aparece en 4 listas · `rust` `networking` `open-source` `packet-sniffer`

### AutoML
- **[TPOT](https://github.com/epistasislab/tpot)** — Tool that automatically creates and optimizes machine learning pipelines using genetic programming. Consider it your personal data science assistant, automating a tedious part of machine learning. · `automl` `genetic-programming` `python` `pipeline-optimization`

### Barcode Processing
- **[ZXing](https://github.com/zxing/zxing)** — An open-source, multi-format 1D/2D barcode image processing library implemented in Java, with ports to other languages. [Apache] · `barcode` `qr-code` `image-processing` `java`

### Bayesian ML
- **[Infer.NET](https://dotnet.github.io/infer)** — Infer.NET is a framework for running Bayesian inference in graphical models. One can use Infer.NET to solve many different kinds of machine learning problems, from standard problems like… · `dotnet` `bayesian-inference` `probabilistic` `graphical-models`

### Binary Format Parser
- **[Kaitai Struct](https://kaitai.io)** — File formats and network protocols dissection language and web IDE, generating parsers in C++, C#, Java, JavaScript, Perl, PHP, Python, Ruby. · `serialization` `parsing` `dsl` `code-generation`

### Binary Serialization
- **[FlatBuffers](https://github.com/google/flatbuffers)** — Memory-efficient serialization library that can access serialized data without unpacking and parsing it. · `serialization` `low-latency` `zero-copy` `binary`

### Browser Extension
- **[OctoLinker](https://github.com/octolinker/octolinker)** — ice_cube: - A browser extension for GitHub that makes the image name in a `Dockerfile` clickable and redirect you to the related Docker Hub page. · `browser-extension` `docker` `github` `productivity`

### Browsers
- **[Vivaldi](https://vivaldi.com)** — The browser that puts you in control. ![Freeware][Freeware Icon] — aparece en 3 listas · `browser` `chromium` `customization`

### Build Automation
- **[just](https://github.com/casey/just)** — A handy command runner for project-specific tasks · `task-runner` `cli` `rust`

### Build System
- **[Bazel](https://bazel.build)** — A multi-language, fast and scalable build system from Google. [Apache] · `build-system` `java` `c++` `monorepo`
- **[Buck2](https://github.com/facebook/buck2)** — Encourages the creation of small, reusable modules consisting of code and resources. · `build-system` `rust` `monorepo` `facebook`

### Business Intelligence
- **[Metabase](https://metabase.com)** — Easy way for everyone in your company to ask questions and learn from data. · `bi` `dashboard` `agpl` `java`
- **[Redash](https://redash.io)** — Connect and query your data sources, build dashboards to visualize data and share them with your company. · `bi` `dashboard` `bsd` `sql-first`

### C#
- **[Cake](https://github.com/cake-build/cake)** — _(label: Good-first-issue)_ <br> Cake (C# Make) is a free and open source cross-platform build automation system with a C# DSL for tasks such as compiling code, copying files and folders, running… — aparece en 3 listas · `csharp` `build-automation` `dsl` `ci-cd`

### C++
- **[Polyaxon](https://github.com/polyaxon/polyaxon)** — - A platform for reproducible and scalable machine learning and deep learning on kubernetes - [(Video)](https://www.youtube.com/watch?v=Iexwrka_hys). — aparece en 3 listas · `kubernetes` `ml-ops` `reproducibility` `python`

### C++ IDE
- **[CLion](https://jetbrains.com/clion)** — Powerful C and C++ IDE. (**Free** for Students) · `ide` `cpp` `c` `jetbrains`
- **[KDevelop](https://kdevelop.org)** — IDE by the people behind KDE. · `ide` `cpp` `kde` `qt`

### C++ ML Toolkit
- **[JAX](https://github.com/google/jax)** — JAX is Autograd and XLA, brought together for high-performance machine learning research. · `cpp` `machine-learning` `computer-vision` `lightweight`

### CI/CD Server
- **[Drone](https://github.com/drone/drone)** — Continuous integration server built on Docker and configured using YAML files. · `ci-cd` `docker` `yaml` `go`

### CI/CD Service
- **[CircleCI](https://circleci.com)** — :yen: Push or pull Docker images from your build environment, or build and run containers right on CircleCI. · `ci-cd` `saas` `docker` `cloud`
- **[Semaphore CI](https://semaphore.io)** — yen: — A high-performance cloud solution that makes it easy to build, test and ship your containers to production. · `ci-cd` `saas` `docker` `cloud`

### CLI Timetracker
- **[Bartib](https://github.com/nikolassv/bartib)** — ] - A simple timetracker for the command line [](https://github.com/nikolassv/bartib/actions/workflows/test.yml) · `cli` `rust` `time-tracking` `self-hosted`

### CLI Tool
- **[television](https://github.com/alexpasmantier/television)** — A blazing fast general purpose fuzzy finder TUI · `rust` `cli` `tui` `fuzzy-search`

### CLI Tools
- **[yt-dlp](https://github.com/yt-dlp/yt-dlp)** — Downloads videos from almost any online platform, along with information, thumbnails, subtitles, descriptions, and comments (comments only on a select few sites like Youtube and a few small… — aparece en 3 listas · `cli` `video-download` `python` `metadata-extraction`
- **[broot](https://github.com/canop/broot)** — A new way to see and navigate directory trees (get an overview of a directory, even a big one; find a directory then `cd` to it; never lose track of file hierarchy while you search; manipulate… · `rust` `cli` `tui` `file-navigation`

### Charting Library
- **[C3.js](https://c3js.org)** — customizable library based on D3.js for easy chart drawing. · `javascript` `d3` `charts` `visualization`

### Classic NLP Toolkit
- **[CoreNLP](https://nlp.stanford.edu/software/corenlp.shtml)** — Stanford CoreNLP provides a set of natural language analysis tools which can take raw English language text input and give the base forms of words. · `nlp` `java` `stanford` `pos-tagging`

### Classical ML Library
- **[SHOGUN](https://github.com/shogun-toolbox/shogun)** — The Shogun Machine Learning Toolbox. [GPLv3] · `machine-learning` `cpp` `scikit-learn-alternative`

### Claude Tips
- **[Claude Code Tips](https://github.com/ykdojo/claude-code-tips)** — by [ykdojo](https://github.com/ykdojo) - A nice variety of 35+ brief but information-dense Claude Code tips covering voice input, system prompt patching, container workflows for risky tasks,… · `claude-code` `tips-tricks` `workflow` `voice`

### Client Side Database
- **[pouchdb](https://github.com/pouchdb/pouchdb)** — Javascript db inspired by Apache CouchDB to run well within the browser. · `database` `offline-first` `sync` `browser`

### Code Analysis
- **[ast-grep](https://github.com/ast-grep/ast-grep)** — A CLI tool for code structural search, lint and rewriting. · `ast` `cli` `linting` `refactoring`

### Code Generation
- **[Agentify](https://github.com/koriyoshi2041/agentify)** — CLI tool that transforms any OpenAPI spec into 9 agent interface formats (MCP server, AGENTS.md, CLAUDE.md,.cursorrules, Skills, llms.txt, GEMINI.md, A2A Card, CLI) with a single command. Tiered… · `ai` `openapi` `code-generation` `cli`

### Code Metrics
- **[scc](https://github.com/boyter/scc)** — Sloc Cloc and Code, a very fast accurate code counter with complexity calculations and COCOMO estimates. · `code-metrics` `golang` `cli` `sloc`

### Code Verification
- **[Infer](https://github.com/facebook/infer)** — Modern static analysis tool for verifying the correctness of code. · `static-analysis` `verification` `java` `c`

### Code Visualization
- **[carbon-now-cli](https://github.com/mixn/carbon-now-cli)** — Beautiful images of your code — from right inside your terminal. · `cli` `code-screenshot` `images` `javascript`

### Computer Vision C
- **[CCV](https://github.com/liuliu/ccv)** — C-based/Cached/Core Computer Vision Library, A Modern Computer Vision Library. [BSD] · `c` `computer-vision` `library` `bsd`

### Configuration Validation
- **[config-file-validator](https://github.com/boeing/config-file-validator)** — Cross Platform tool to validate configuration files. · `config-validation` `cli` `golang` `ci-cd`

### Container CLI
- **[lazydocker](https://github.com/jesseduffield/lazydocker)** — The lazier way to manage everything docker. A simple terminal UI for both docker and docker-compose, written in Go with the gocui library. By [jesseduffield](https://github.com/jesseduffield). · `cli` `go` `docker` `tui`

### Container Monitoring
- **[ctop](https://github.com/bcicen/ctop)** — interface (e.g. htop) for container metrics. · `cli` `monitoring` `docker` `containers`

### Container Tools
- **[lazyjournal](https://github.com/lifailon/lazyjournal)** — A interface for reading and filtering the logs output of Docker and Podman containers like [Dozzle](dozzle) but for the terminal with support for fuzzy find, regex and output coloring. · `docker` `podman` `logging` `tui`

### Continuous Integration
- **[Bencher](https://bencher.dev)** — Suite of continuous benchmarking tools designed to catch performance regressions in CI. — aparece en 4 listas · `benchmarking` `ci-cd` `rust`

### Crypto Library
- **[orion-rs/orion](https://github.com/orion-rs/orion)** — This library aims to provide easy and usable crypto. 'Usable' meaning exposing high-level API's that are easy to use and hard to misuse.… · `rust` `cryptography` `security` `high-level-api`

### Crypto Library C++
- **[Botan](https://botan.randombit.net)** — Cryptography library written in `C++20`. · `cpp20` `cryptography` `library` `algorithms`

### Data Cleaning
- **[OpenRefine](https://openrefine.org)** — Tool for working with messy data: cleaning, transforming, extending it with web services and linking it to databases. · `data-cleaning` `etl` `jython` `gui`

### Data Exploration
- **[Bread Dataset Viewer](https://github.com/bread-technologies/mle_vscode_extension)** — A VS Code extension for viewing and exploring large machine learning datasets (CSV, JSON, Parquet, etc.) directly within the editor without VS Code crashing in a clean UI. · `vscode-extension` `data-exploration` `ml-tooling`

### Data Orchestration
- **[Dagster](https://github.com/dagster-io/dagster)** — - A data orchestrator for machine learning, analytics, and ETL. · `python` `orchestration` `assets` `ml`

### Data Pipelines
- **[pathwaycom/pathway](https://github.com/pathwaycom/pathway)** — Performant open-source Python ETL framework with Rust runtime, supporting 300+ data sources. · `python` `etl` `rust` `data-pipelines`

### Data Processing
- **[csvkit](https://github.com/wireservice/csvkit)** — Utilities for converting to and working with CSV. · `python` `csv` `cli` `data-wrangling`
- **[Vaex](https://github.com/vaexio/vaex)** — Vaex is a high performance Python library for lazy Out-of-Core DataFrames (similar to Pandas), to visualize and explore big tabular datasets. Vaex uses memory mapping, zero memory copy policy and… · `python` `dataframe` `big-data` `out-of-core`

### Data Query Tool
- **[dasel](https://github.com/tomwright/dasel)** — Query and update data structures using selectors from the command line. Comparable to jq/yq but supports JSON, YAML, TOML and XML with zero runtime dependencies. · `cli` `json` `yaml` `toml`

### Data Research
- **[AI Job Displacement Tracker](https://github.com/noahaust2/ai-displacement-tracker)** — - Structured, source-backed dataset tracking 96 AI-attributed workforce reductions (457K workers affected, 13 countries, 13 sectors). Every entry includes source URLs, attribution tier, and job… · `dataset` `csv` `labor-economics` `open-data`

### Data Science Notebooks
- **[Deepnote](https://github.com/deepnote/deepnote)** — - Deepnote is a drop-in replacement for Jupyter with an AI-first design, sleek UI, new blocks, and native data integrations. Use Python, R, and SQL locally in your favorite IDE, then scale to… · `jupyter` `python` `r` `sql`

### Data Validation
- **[DataComPy](https://github.com/capitalone/datacompy)** — A library to compare Pandas, Polars, and Spark data frames. It provides stats and lets users adjust for match accuracy. · `python` `dataframes` `testing` `etl`

### Data Visualization
- **[gradio](https://github.com/gradio-app/gradio)** — - Quickly create and share demos of models - by only writing Python. Debug models interactively in your browser, get feedback from collaborators, and generate public links without deploying anything. — aparece en 3 listas · `python` `web-ui` `demos` `visualization`
- **[Perspective](https://github.com/finos/perspective)** — Streaming pivot visualization via WebAssembly. · `webassembly` `data-visualization` `streaming` `pivot`
- **[Rerun](https://github.com/rerun-io/rerun)** — - Rerun is an open-source SDK for logging, storing, querying, and visualizing multimodal data, designed for robotics, computer vision, and spatial AI. · `visualization` `robotics` `spatial-ai` `rust`
- **[vizzu](https://github.com/vizzuhq/vizzu-lib)** — Library for animated data visualizations and data stories. · `dataviz` `animation` `javascript`

### Database CLI
- **[iredis](https://github.com/laixintao/iredis)** — Redis client with autocompletion and syntax highlighting. · `cli` `redis` `python` `repl`
- **[mycli](https://github.com/dbcli/mycli)** — MySQL client with autocompletion and syntax highlighting. · `cli` `mysql` `python` `repl`

### Database GUI
- **[Mingo](https://mingo.io)** — Easy to use MongoDB GUI with mind-blowing features. · `mongodb` `gui` `database` `nosql`

### Dataflow Orchestration
- **[Hamilton](https://github.com/dagworks-inc/hamilton)** — - Hamilton is a micro-orchestration framework for defining dataflows. Runs anywhere python runs (e.g. jupyter, fastAPI, spark, ray, dask). Brings software engineering best practices without you… · `dataflow` `feature-engineering` `orchestration` `lightweight`

### Deep Learning Go
- **[gorgonia](https://github.com/gorgonia/gorgonia)** — graph-based computational library like Theano for Go that provides primitives for building various machine learning and neural network algorithms. · `go` `neural-networks` `graph-based` `autodiff`

### Deployment Tools
- **[Deployer](https://github.com/deployphp/deployer)** — _(label: good-for-beginner)_ <br> A deployment tool written in PHP with support for popular frameworks out of the box. · `php` `deployment` `cli`

### Desktop Framework
- **[tauri-apps/tauri](https://github.com/tauri-apps/tauri)** — Build smaller, faster, and more secure desktop applications with a web frontend, powered by [WRY](https://github.com/tauri-apps/wry).… · `rust` `desktop` `web-frontend` `cross-platform`

### Developer Knowledge Base
- **[AgentsKB](https://agentskb.com)** — Knowledge base with 39K+ researched technical Q&As accessible via MCP server, REST API, or web search. Integrates with Claude Code, Cursor, and Cline. · `knowledge-base` `mcp-server` `rest-api` `ai-assist`

### Developer Tools
- **[Rider](https://jetbrains.com/rider)** — A cross-platform C# IDE based on the IntelliJ platform and ReSharper — aparece en 3 listas · `csharp` `ide` `dotnet` `jetbrains`

### Developer Utilities
- **[intelli-shell](https://github.com/lasantosr/intelli-shell)** — Bookmark commands with placeholders and search or autocomplete at any time [](https://crates.io/crates/intelli-shell) [](https://github.com/lasantosr/intelli-shell/actions/workflows/release.yml) — aparece en 3 listas · `rust` `cli` `productivity` `shell`

### Differentiable Vision
- **[Kornia](https://github.com/kornia/kornia)** — - Kornia is a differentiable computer vision library built on PyTorch that provides a rich set of differentiable image processing and geometric vision algorithms. · `computer-vision` `pytorch` `differentiable` `geometry`

### Disk Analysis
- **[diskonaut](https://github.com/imsnif/diskonaut)** — Terminal visual disk space navigator · `rust` `tui` `cli` `disk-analysis`

### Distributed Database
- **[Apache Ignite](https://github.com/apache/ignite)** — - A memory-centric distributed database, caching, and processing platform for transactional, analytical, and streaming workloads delivering in-memory speeds at petabyte scale -… · `database` `distributed` `in-memory` `streaming`

### Distributed Security
- **[Ockam](https://github.com/ockam-network/ockam)** — _(label: good first issue)_ <br> End-to-end encryption and mutual authentication for distributed applications. · `rust` `cryptography` `distributed` `security`

### Distributed Systems
- **[Dragonfly](https://github.com/dragonflyoss/dragonfly2)** — Provide efficient, stable and secure file distribution and image acceleration based on p2p technology to be the best practice and standard solution in cloud native architectures. — aparece en 3 listas · `p2p` `oci-images` `container-registry` `distributed-systems`

### Doc Browser
- **[Dash](https://kapeli.com/dash)** — Offline API documentation browser for macOS with instant search access to Vue.js docs and 200+ other frameworks. · `macos` `documentation` `offline` `developer-tools`

### Doc Extraction
- **[kreuzberg](https://github.com/kreuzberg-dev/kreuzberg)** — High-performance document extraction library with a Rust core, supporting 62+ formats including PDF, Office, images with OCR, HTML, email, and archives. · `rust` `document-parsing` `ocr` `pdf`

### Docker Backup
- **[docker-volume-backup](https://github.com/offen/docker-volume-backup)** — Backup Docker volumes locally or to any S3, WebDAV, Azure Blob Storage, Dropbox or SSH compatible storage. · `docker` `backup` `s3` `devops`

### Docker CLI Tool
- **[oxker](https://github.com/mrjackwills/oxker)** — A simple tui to view & control docker containers. Written in [Rust](https://rust-lang.org/), making heavy use of [ratatui](https://github.com/tui-rs-revival/ratatui) &… · `rust` `tui` `docker` `terminal`

### Docker Management
- **[dockly](https://github.com/lirantal/dockly)** — An interactive shell UI for managing Docker containers. · `docker` `cli` `tui` `containers`

### Docker Tool
- **[dive](https://github.com/wagoodman/dive)** — A tool for exploring each layer in a docker image. By [wagoodman](https://github.com/wagoodman). · `docker` `go` `debugging` `cli`

### Document Conversion
- **[microsoft/markitdown](https://github.com/microsoft/markitdown)** — 🎖️ 🐍 🏠 - MCP tool access to MarkItDown -- a library that converts many file formats (local or remote) to Markdown for LLM consumption. · `python` `mcp` `markdown-conversion` `llm-tools`

### Document Search
- **[Aleph](https://aleph.occrp.org)** — Tool for indexing large amounts of both documents (PDF, Word, HTML) and structured (CSV, XLS, SQL) data for easy browsing and search. It is built with investigative reporting as a primary use case. ) · `search` `indexing` `documents` `docker`

### Documentation
- **[Sphinx](https://github.com/sphinx-doc/sphinx)** — Sphinx makes it easy to create intelligent and beautiful documentation. [BSD-2-Clause] [website](https://www.sphinx-doc.org) · `documentation` `rst` `static-site` `python`

### Documentation Generator
- **[readme-md-generator](https://github.com/kefranabg/readme-md-generator)** — A CLI that generates beautiful README.md files · `cli` `documentation` `nodejs`

### Editor Plugins
- **[Cline](https://marketplace.visualstudio.com/items)** — Autonomous coding agent for VS Code that can create/edit files, execute commands, and use the browser with user permission. Supports multiple AI providers including OpenRouter, Anthropic, OpenAI,… — 🔥 aparece en 7 listas · `vscode-extension` `ai-agent` `autonomous-coding` `multi-provider`

### Educación Seguridad
- **[Security Talks](https://github.com/paulsec/awesome-sec-talks)** — Curated list of security conferences. · `educacion` `conferencias` `osint` `recursos`

### Educational Crypto
- **[crypto-algorithms](https://github.com/b-con/crypto-algorithms)** — Basic implementations of standard cryptography algorithms (AES, SHA, etc.) in C. [PublicDomain] · `cryptography` `c` `educational` `aes`

### Educational Resource
- **[awesome-talks](https://github.com/janvanryswyck/awesome-talks)** — A lot of screencasts, recordings of user group gatherings and conference talks. · `curated-content` `learning` `talks` `community`

### Elasticsearch UI Library
- **[ReactiveSearch](https://github.com/appbaseio/reactivesearch)** — _(label: good first issue-:wave:)_ <br> A UI components library for Elasticsearch: Available for React, Vue and React Native. · `react` `vue` `elasticsearch` `ui-components`

### Email Client
- **[Mailspring](https://getmailspring.com)** — A beautiful, fast, and fully open source mail client. [![Open-Source Software][OSS Icon]](https://github.com/Foundry376/Mailspring) ![Freeware][Freeware Icon] · `email` `open-source` `cross-platform` `electron`

### Email Marketing
- **[phpList](https://phplist.org)** — Newsletter and email marketing with advanced management of subscribers, bounces, and plugins. · `php` `self-hosted` `email-marketing` `agpl`

### Email Server
- **[chasquid](https://blitiri.com.ar/p/chasquid)** — SMTP (email) server with a focus on simplicity, security, and ease of operation. · `go` `smtp` `email-server` `self-hosted`

### Email Testing
- **[Mailpit](https://github.com/axllent/mailpit)** — An email and SMTP testing tool for developers. · `smtp` `testing` `go` `email`

### Enterprise Search
- **[Apache Solr](https://lucene.apache.org/solr)** — Enterprise search platform featuring full-text search, hit highlighting, faceted search, real-time indexing, dynamic clustering, and rich document (e.g., Word, PDF) handling. · `search` `java` `lucene` `docker`

### Environment Linting
- **[dotenv-linter](https://github.com/dotenv-linter/dotenv-linter)** — Linter for `.env` files [](https://github.com/dotenv-linter/dotenv-linter/actions?query=workflow%3ACI+branch%3Amaster) · `rust` `linter` `cli` `dotenv`

### Evolutionary Algorithms
- **[DEAP](https://github.com/deap/deap)** — - A novel evolutionary computation framework for rapid prototyping and testing of ideas. It seeks to make algorithms explicit and data structures transparent. It works in perfect harmony with… · `evolutionary-computation` `python` `genetic-algorithms` `parallelizable`

### Experiment Tracking
- **[Aim](https://github.com/aimhubio/aim)** — - A super-easy way to record, search and compare AI experiments. · `experiment-tracking` `mlops` `self-hosted` `dashboard`

### File Encryption
- **[rage](https://github.com/str4d/rage)** — is a simple, modern, and secure file encryption tool, using the age format. · `encryption` `rust` `file-encryption` `age-format`

### File Sharing
- **[Gokapi](https://github.com/forceu/gokapi)** — Lightweight server to share files, which expire after a set amount of downloads or days. Similar to the discontinued Firefox Send, with the difference that only the admin is allowed to upload files. · `file-sharing` `self-hosted` `go` `docker`

### File Transfer
- **[croc](https://github.com/schollz/croc)** — Easily and securely send files or folders from one computer to another. · `file-transfer` `p2p` `golang` `encryption`

### Financial Data
- **[yfinance](https://github.com/ranaroussi/yfinance)** — `Python` - Yahoo! Finance market data downloader (+faster Pandas Datareader). · `finance` `data-fetching` `python` `stock-market`

### Frontend Toolchain
- **[biome](https://github.com/biomejs/biome)** — A toolchain for web projects, aimed to provide functionalities to maintain them. Biome offers formatter and linter, usable via CLI and LSP · `rust` `javascript` `formatter` `linter`

### Functional Utilities
- **[IterTools TS](https://github.com/smoren/itertools-ts)** — _(label: good first issue)_ <br> Extended itertools port for TypeScript and JavaScript. Provides a huge set of functions for working with iterable collections (including async ones). · `typescript` `javascript` `itertools` `functional`

### GPU ML Frameworks
- **[CuML](https://github.com/rapidsai/cuml)** — - cuML is a suite of libraries that implement machine learning algorithms and mathematical primitives functions that share compatible APIs with other RAPIDS projects. · `gpu` `cuda` `machine-learning` `python`

### Geolocation OSINT
- **[WiGLE](https://wigle.net)** — Wi-fi "wardriving" database. Contains a global map containing crowdsourced information on the location, name, and other properties of wi-fi networks. Software available to download to contribute… · `wifi-mapping` `geolocation` `wardriving` `crowdsourced`

### Git Automation
- **[AI Git Narrator](https://github.com/pmusolino/ai-git-narrator)** — CLI tool that uses AI to automatically generate high-quality Git commit messages and pull request descriptions. · `ai` `git` `llm` `cli`

### Git Enhanced
- **[ggc](https://github.com/bmf-san/ggc)** — A Git CLI tool with both traditional command-line and interactive incremental-search UI, workflow support, and configurable keybindings. · `git` `cli` `vcs` `interactive`

### Git GUI
- **[GitKraken](https://gitkraken.com)** — The most popular Git GUI for Windows, Mac and Linux. · `git-gui` `version-control` `freemium` `cross-platform`

### Git UI
- **[GitButler](https://gitbutler.com)** — Change management with parallel and stacked branches, unlimited undo, agent integrations. [![Open-Source Software][OSS Icon]](https://github.com/gitbutlerapp/gitbutler) ![Freeware][Freeware Icon] · `git` `vcs` `ui` `ai-agent`

### Go Debugging
- **[Gebug](https://github.com/moshebe/gebug)** — A tool that makes debugging of Dockerized Go applications super easy by enabling Debugger and Hot-Reload features, seamlessly. · `debugging` `docker` `go` `development`

### Go NLP Library
- **[spaGO](https://github.com/nlpodyssey/spago)** — Self-contained Machine Learning and Natural Language Processing library in Go. · `nlp` `go` `machine-learning` `self-contained`

### Go Recommender
- **[gorse](https://github.com/zhenghaoz/gorse)** — An offline recommender system backend based on collaborative filtering written in Go. · `go` `recommender-system` `collaborative-filtering` `ml`

### Go Scaffolding
- **[create-go-app/cli](https://github.com/create-go-app/cli)** — Clean project logo. Useful badges (version, code style, test cover, docs). Clear readme with quickstart, understandable installation and usage manual, video screencast, ToC with well-documented… · `cli` `go` `scaffolder` `boilerplate`

### Go Tools
- **[OctoLinker](https://github.com/octolinker/browser-extension)** — Navigate through `projects.json` files efficiently with the OctoLinker browser extension for GitHub. — aparece en 3 listas · `github` `browser-extension` `typescript` `navigation`

### Go Utilities
- **[script](https://github.com/bitfield/script)** — _(label: good first issue)_ <br> A Go library for doing the kind of tasks that shell scripts are good at: reading files, executing subprocesses, counting lines, matching strings, and so on.… · `go` `scripting` `shell` `io`

### Graph Visualization
- **[Gephi](https://gephi.org)** — is an open-source graph and network visualization software. · `graph-visualization` `network-analysis` `java` `desktop-app`

### Graphics Library
- **[SVGo](https://github.com/ajstarks/svgo)** — The Go Language library for SVG generation. · `go` `svg` `graphics` `library`

### HPC Package Manager
- **[Spack](https://spack.io)** — A flexible package manager that supports multiple versions, configurations, platforms, and compilers. · `package-manager` `hpc` `python` `multi-version`

### HTTP Client
- **[httpie/httpie](https://github.com/httpie/httpie)** — Description of what the project does. Demo screenshots. Project logo. TOC for easy navigation. Build badges. Quick and simple installation and usage sections. Includes an examples section. · `cli` `http` `api-testing` `python`

### HTTP Server
- **[svenstaro/miniserve](https://github.com/svenstaro/miniserve)** — A small, self-contained cross-platform CLI tool that allows you to just grab the binary and serve some file(s) via HTTP [](https://github.com/svenstaro/miniserve/actions) · `rust` `cli` `http-server` `self-contained`

### Hardened Firefox
- **[LibreWolf](https://librewolf.net)** — A fork of Firefox, focused on privacy, security and freedom. [![Open-Source Software][OSS Icon]](https://gitlab.com/librewolf-community) ![Freeware][Freeware Icon] · `firefox` `privacy` `hardened` `open-source`

### Hyperparameter Tuning
- **[keras-tuner](https://github.com/keras-team/keras-tuner)** — - Keras Tuner is an easy-to-use, distributable hyperparameter optimisation framework that solves the pain points of performing a hyperparameter search. Keras Tuner makes it easy to define a search… · `keras` `tensorflow` `hyperparameter-tuning` `beginner-friendly`

### IaC Automation
- **[nwiizo/tfmcp](https://github.com/nwiizo/tfmcp)** — 🦀 🏠 - A Terraform MCP server allowing AI assistants to manage and operate Terraform environments, enabling reading configurations, analyzing plans, applying configurations, and managing… · `terraform` `mcp` `ai` `infrastructure`

### Image Processing
- **[Scikit-Image](https://github.com/scikit-image/scikit-image)** — A collection of algorithms for image processing in Python. — aparece en 3 listas · `python` `image-processing` `computer-vision` `scipy`

### Immediate Mode GUI
- **[nuklear](https://github.com/immediate-mode-ui/nuklear)** — A single-header ANSI C gui library. [PublicDomain] · `gui` `c` `single-header` `immediate-mode`

### Interactive Programming
- **[.NET Interactive](https://github.com/dotnet/interactive)** — -.NET Interactive takes the power of.NET and embeds it into your interactive experiences. · `dotnet` `repl` `interactive` `jupyter`

### Interactive Visualization
- **[Vega-Altair](https://github.com/vega/altair)** — - Vega-Altair is a declarative statistical visualization library for Python. · `visualization` `declarative` `interactive` `vega`

### Internationalization
- **[Python Babel](https://github.com/python-babel/babel)** — _(label: difficulty/low)_ <br> The Python Internationalization Library. · `i18n` `localization` `python`

### JSON Viewer
- **[fx](https://github.com/antonmedv/fx)** — Terminal JSON viewer & processor. · `cli` `json` `terminal` `visualization`

### Java C++ Bridge
- **[JavaCpp](https://github.com/bytedeco/javacpp)** — The missing bridge between Java and native C++. [Apache2] · `jni` `java` `c++` `performance`

### Java Security
- **[Apache Shiro](https://shiro.apache.org)** — Performs authentication, authorization, cryptography and session management. · `java` `authentication` `authorization` `security`

### JavaScript
- **[Gatsby.js](https://github.com/gatsbyjs/gatsby)** — _(label: good first issue)_ <br> Build blazing fast, modern apps and websites with React. — aparece en 4 listas · `react` `static-site-generator` `graphql`
- **[Ghost](https://github.com/tryghost/ghost)** — _(label: good first issue)_ <br> Just a blogging platform — aparece en 3 listas · `javascript` `node.js` `cms` `self-hosted`
- **[Vest](https://github.com/ealush/vest)** — _(label: good first issue)_ <br> Validations framework inspired by unit testing frameworks. — aparece en 3 listas · `javascript` `validation` `forms` `typescript`
- **[webdriver.io](https://github.com/webdriverio/webdriverio)** — _(label: first-timers-only)_ <br> Next-gen browser and mobile automation test framework for Node.js — aparece en 3 listas · `javascript` `e2e-testing` `webdriver` `automation`

### Jira Client
- **[fjira](https://github.com/mk-5/fjira)** — A fuzzy-search based terminal UI application for Attlasian Jira · `jira` `cli` `rust` `tui`

### Knowledge Base
- **[AFFiNE Community Edition](https://affine.pro)** — Next-gen knowledge base that brings planning, sorting and creating all together. Privacy first, customizable and ready to use (alternative to Notion and Miro). ) · `self-hosted` `knowledge-base` `open-source` `docker`
- **[tldr-pages](https://github.com/tldr-pages/tldr)** — _(label: help-wanted)_ <br> Collaborative cheatsheets for console commands. · `documentation` `cli` `community` `cheatsheet`

### LLM Framework
- **[dspy](https://github.com/stanfordnlp/dspy)** — - A framework for programming with foundation models. · `llm-framework` `prompt-engineering` `python` `stanford`

### LLM Inference
- **[SGLang](https://github.com/sgl-project/sglang)** — - SGLang is a fast serving framework for large language models and vision language models. · `llm-serving` `inference-optimization` `python` `cuda`

### LLM Monitoring
- **[Opik](https://github.com/comet-ml/opik)** — - Opik is an open-source platform for evaluating, testing and monitoring LLM applications. · `python` `llm-monitoring` `evaluation` `open-source`

### LLM Observability
- **[Opik](https://comet.com/site/products/opik)** — Open source engineering platform to debug, evaluate, and monitor your LLM applications, RAG systems, and agentic workflows with comprehensive tracing, automated evaluations, and production-ready… · `llm` `observability` `tracing` `evals`
- **[TensorZero](https://github.com/tensorzero/tensorzero)** — data & learning flywheel for LLMs that unifies inference, observability, optimization, and experimentation · `llm` `inference` `observability` `python`

### LLM Orchestration Framework
- **[LangChain](https://github.com/langchain-ai/langchain)** — - LangChain assists in building applications with LLMs through composability. · `llm` `python` `framework` `agent-orchestration`

### LLM Security Testing
- **[Promptfoo](https://github.com/promptfoo/promptfoo)** — - LLM red teaming and evaluation framework for testing jailbreaks, prompt injection, and other vulnerabilities with CI/CD integration. · `llm-security` `red-teaming` `prompt-injection` `ci-cd`

### LLM Training
- **[unsloth](https://github.com/unslothai/unsloth)** — - Fine-tuning & Reinforcement Learning for LLMs. Train OpenAI gpt-oss, DeepSeek-R1, Qwen3, Gemma 3, TTS 2x faster with 70% less VRAM. · `llm` `fine-tuning` `qlora` `python`

### Learning Material
- **[data-science-ipython-notebooks](https://github.com/donnemartin/data-science-ipython-notebooks)** — Continually updated Data Science Python Notebooks: Spark, Hadoop MapReduce, HDFS, AWS, Kaggle, scikit-learn, matplotlib, pandas, NumPy, SciPy, and various command lines. · `jupyter` `python` `data-science` `tutorials`

### Learning Resource
- **[CTFs](https://github.com/apsdehal/awesome-ctf)** — Capture The Flag frameworks, libraries, etc. — aparece en 3 listas · `ctf` `security` `awesome-list`

### Local LLM
- **[LocalAI](https://github.com/mudler/localai)** — - LocalAI is a drop-in replacement REST API that's compatible with OpenAI API specifications for local inferencing. · `ai` `llm` `self-hosted` `openai-compatible`

### Low Code ML
- **[Ludwig](https://github.com/ludwig-ai/ludwig)** — - Ludwig is a low-code framework for building custom AI models like LLMs and other deep neural networks. · `low-code` `llm` `deep-learning` `python`

### MCP Server
- **[spfunctions/simplefunctions-cli](https://github.com/spfunctions/simplefunctions-cli)** — ](https://glama.ai/mcp/servers/spfunctions/simplefunctions-cli) 📇 ☁️ - Calibrated world model for AI agents from 9,700+ prediction markets. 16 MCP tools covering real-time world state, market… · `mcp` `prediction-markets` `forecasting` `api`

### ML Explainability
- **[SHAPash](https://github.com/maif/shapash)** — - Shapash is a Python library that provides several types of visualization that display explicit labels that everyone can understand. · `python` `explainability` `shap` `visualization`

### ML Framework
- **[MLX](https://github.com/ml-explore/mlx)** — - MLX is an array framework for machine learning on Apple silicon. · `numpy-alternative` `apple-silicon` `machine-learning` `array-framework`
- **[modAL](https://github.com/modal-python/modal)** — A modular active learning framework for Python, built on top of scikit-learn. · `python` `machine-learning` `active-learning` `scikit-learn`
- **[PyCaret](https://github.com/pycaret/pycaret)** — ) - low-code library for training and deploying models (scikit-learn, XGBoost, LightGBM, spaCy) · `python` `ml` `low-code` `automl`

### ML Libraries
- **[CloudForest](https://github.com/ryanbressler/cloudforest)** — Fast, flexible, multi-threaded ensembles of decision trees for machine learning in pure Go. · `go` `machine-learning` `decision-trees` `performance`

### ML Monitoring
- **[Bread WandB Viewer](https://github.com/bread-technologies/bread_wandb_viewer_extension)** — A VS Code extension to view Weights & Biases experiments, logs, and artifacts within the IDE, eliminating the need to switch to the web UI & preserving data privacy by being 100% offline. · `vscode-extension` `weights-and-biases` `ml-monitoring`

### ML Pipeline Framework
- **[ZenML](https://github.com/zenml-io/zenml)** — - ZenML is an extensible, open-source MLOps framework to create reproducible ML pipelines with a focus on automated metadata tracking, caching, and many integrations to other tools. · `mlops` `ml-pipelines` `metadata-tracking` `python`

### ML Research Library
- **[Flashlight](https://github.com/flashlight/flashlight)** — - A fast, flexible machine learning library written entirely in C++ from the Facebook AI Research and the creators of Torch, TensorFlow, Eigen and Deep Speech. · `machine-learning` `cpp` `facebook-ai` `research`

### ML Serving
- **[DeepDetect](https://github.com/jolibrain/deepdetect)** — - Machine Learning production server for TensorFlow, XGBoost and Cafe models written in C++ and maintained by Jolibrain. · `cpp` `ml-serving` `tensorflow` `xgboost`

### ML Sparse Data
- **[xLearn](https://github.com/aksnzhy/xlearn)** — A high performance, easy-to-use, and scalable machine learning package, which can be used to solve large-scale machine learning problems. xLearn is especially useful for solving machine learning… · `machine-learning` `sparse-data` `c++` `scalable`

### ML Utilities
- **[mlxtend](https://github.com/rasbt/mlxtend)** — A library consisting of useful tools for data science and machine learning tasks. · `python` `machine-learning` `data-science` `scikit-learn`

### MLOps Platform
- **[ClearML](https://github.com/clearml/clearml)** — Auto-Magical CI/CD to streamline your AI workload. Experiment Management, Data Management, Pipeline, Orchestration, Scheduling & Serving in one MLOps/LLMOps solution. · `python` `mlops` `orchestration` `experiment-tracking`
- **[Determined](https://github.com/determined-ai/determined)** — - Deep learning training platform with integrated support for distributed training, hyperparameter tuning, and model management (supports Tensorflow and Pytorch). · `mlops` `distributed-training` `hyperparameter-tuning` `python`
- **[Hopsworks](https://github.com/logicalclocks/hopsworks)** — A data-intensive platform for AI with the industry's first open-source feature store. The Hopsworks Feature Store provides both a feature warehouse for training and batch based on Apache Hive and… · `feature-store` `ml-ops` `apache-hive` `mysql-cluster`

### MacOS Developer Tools
- **[quick-look-plugins](https://github.com/sindresorhus/quick-look-plugins)** — List of useful [Quick Look](https://en.wikipedia.org/wiki/Quick_Look) plugins for developers · `quicklook` `macos` `plugins` `curated-list`

### Machine Learning
- **[CatBoost](https://github.com/catboost/catboost)** — General purpose gradient boosting on decision trees library with categorical features support out of the box. It is easy to install, contains fast inference implementation and supports CPU and GPU… — aparece en 4 listas · `gradient-boosting` `machine-learning` `categorical-features` `gpu`
- **[Feature Engine](https://github.com/feature-engine/feature_engine)** — - Feature-engine is a Python library that contains several transformers to engineer features for use in machine learning models. — aparece en 3 listas · `spark` `streaming` `scala` `java`
- **[H2O-3](https://github.com/h2oai/h2o-3)** — - Fast scalable Machine Learning platform for smarter applications: Deep Learning, Gradient Boosting & XGBoost, Random Forest, Generalized Linear Modeling (Logistic Regression, Elastic Net),… — aparece en 3 listas · `machine-learning` `automl` `java` `distributed`
- **[GoLearn](https://github.com/sjwhitworth/golearn)** — General Machine Learning library for Go. · `machine-learning` `go` `classification-regression`

### Mapping Library
- **[OpenLayers3](https://openlayers.org)** — A high-performance, feature-packed library for all your mapping needs. · `maps` `gis` `javascript` `geospatial`

### Markdown Editor
- **[MarkText](https://github.com/marktext/marktext)** — Next generation markdown editor, running on platforms of MacOS Windows and Linux. [![Open-Source Software][OSS Icon]](https://github.com/marktext/marktext) ![Freeware][Freeware Icon] · `markdown` `wysiwyg` `electron` `cross-platform`

### Message Queues
- **[NSQ](https://nsq.io)** — A realtime distributed messaging platform. · `go` `messaging` `distributed` `realtime`

### Metaheuristic Optimization
- **[Scikit-Opt](https://github.com/guofei9987/scikit-opt)** — Swarm Intelligence in Python (Genetic Algorithm, Particle Swarm Optimization, Simulated Annealing, Ant Colony Algorithm, Immune Algorithm, Artificial Fish Swarm Algorithm in Python) · `optimization` `swarm-intelligence` `genetic-algorithm` `python`

### Misc
- **[awesome](https://github.com/sindresorhus/awesome)** — zap: - A curated list of awesome lists. — aparece en 4 listas · `curated-list` `discovery` `meta-index`

### Mobile AI SDK
- **[RunAnywhere](https://github.com/runanywhereai/runanywhere-sdks)** — - RunAnywhere is a production-ready SDK for running AI models (LLMs, speech-to-text, text-to-speech) on-device for iOS, Android, React Native, and Flutter - enabling private, offline, and fast… · `mobile` `on-device` `llm` `offline`

### Mobile Framework
- **[NativeScript](https://github.com/nativescript/nativescript)** — _(label: good first issue)_ <br> NativeScript is an open source framework for building truly native mobile apps with JavaScript. Use web skills, like Angular and Vue.js, FlexBox and CSS, and get… · `javascript` `mobile` `cross-platform` `angular`

### Mock API
- **[Mockoon](https://mockoon.com)** — Create mock APIs in seconds. [![Open-Source Software][OSS Icon]](https://github.com/mockoon/mockoon) · `mock-api` `testing` `http-server` `oss`

### Model Serving
- **[BentoML](https://github.com/bentoml/bentoml)** — - BentoML is an open source framework for high performance ML model serving. · `python` `mlops` `model-serving` `containerization`

### Model Visualization
- **[Netron](https://netron.app)** — Visualizer for neural network and machine learning models. · `visualization` `neural-network` `onnx` `model-inspection`

### Modern GUI Toolkit
- **[slint-ui/slint](https://github.com/slint-ui/slint)** — [Slint](https://slint.dev/) is a toolkit to efficiently develop fluid graphical user interfaces for embedded devices and desktop applications.… · `gui` `rust` `embedded` `cross-platform`

### Monitoring
- **[netdata/netdata#Netdata](https://github.com/netdata/netdata)** — 🎖️ 🏠 ☁️ 📟 🍎 🪟 🐧 - Discovery, exploration, reporting and root cause analysis using all observability data, including metrics, logs, systems, containers, processes, and network connections · `observability` `metrics` `self-hosted` `c`

### Monitoring System
- **[HertzBeat](https://github.com/dromara/hertzbeat)** — An open-source real-time monitoring system with custom-monitor and agentless. · `monitoring` `observability` `agentless` `open-source`

### Music Server
- **[Polaris](https://github.com/agersant/polaris)** — Music browsing and streaming application optimized for large music collections, ease of use and high performance. · `rust` `self-hosted` `music-streaming` `docker`

### NLP RAG Framework
- **[Haystack](https://github.com/deepset-ai/haystack)** — - Haystack is an open source NLP framework to interact with your data using Transformer models and LLMs (GPT-3 and alike). Haystack offers production-ready tools to quickly build ChatGPT-like… · `nlp` `llm` `rag` `transformers`

### Native Interop
- **[CppSharp](https://github.com/mono/cppsharp)** — Tools and libraries to glue C/C++ APIs to high-level languages. [MIT] · `interop` `csharp` `c++binding` `code-generation`

### Network Analysis
- **[kpcyrd/sniffglue](https://github.com/kpcyrd/sniffglue)** — A secure multithreaded packet sniffer · `rust` `network` `sniffer` `cli`

### Network Monitor
- **[domcyrus/rustnet](https://github.com/domcyrus/rustnet)** — Cross-platform network monitoring TUI with process identification via eBPF/PKTAP and deep packet inspection [](https://github.com/domcyrus/rustnet/actions/workflows/rust.yml)… · `network` `tui` `rust` `ebpf`

### Network Monitoring
- **[bandwhich](https://github.com/imsnif/bandwhich)** — Track bandwidth utilization by process. · `network` `monitoring` `rust` `cli`

### Network Reconnaissance
- **[DNSDumpster](https://dnsdumpster.com)** — is a website that will help you discover hosts related to a specific domain. · `dns` `recon` `subdomain-enumeration` `web-tool`

### Network Security
- **[rshijack](https://github.com/kpcyrd/rshijack)** — TCP connection hijacker, Rust rewrite of `shijack`. · `rust` `pentest` `network` `tcp`

### Network Tool
- **[sshuttle](https://github.com/sshuttle/sshuttle)** — Transparent proxy server that works as a poor man's VPN. · `vpn` `proxy` `ssh` `cli`

### Network Tools
- **[MyIP](https://github.com/jason5ng32/myip)** — All in one IP Toolbox. Easy to check all your IPs, IP geolocation, check for DNS leaks, examine WebRTC connections, speed test, ping test, MTR test, check website availability, whois search and… · `vue` `network-tools` `ip-tools` `frontend`

### Networking
- **[localtunnel](https://github.com/localtunnel/localtunnel)** — Expose your localhost to the world. · `tunneling` `networking` `demo` `node`

### Node.js Framework
- **[Fastify](https://github.com/fastify/fastify)** — _(label: good first issue)_ <br> Fast and low overhead web framework, for Node.js. · `nodejs` `web-framework` `rest` `low-overhead`

### Note Manager
- **[Linus-Mussmaecher/rucola](https://github.com/linus-mussmaecher/rucola)** — Terminal-based markdown note manager. [](https://crates.io/crates/rucola-notes) [](https://github.com/Linus-Mussmaecher/rucola/actions/workflows/continuous-testing.yml) · `notes` `markdown` `rust` `tui`

### Note Taking
- **[Joplin](https://joplinapp.org)** — Note taking application with markdown editor and encryption support for mobile and desktop platforms. Runs client-side and syncs through a self hosted Nextcloud instance or similar (alternative to… · `note-taking` `markdown` `encryption` `self-hosted`

### Notion Alternative
- **[AppFlowy](https://appflowy.io)** — Build detailed lists of to-do’s for different projects while tracking the status of each one. Open Source Notion Alternative. · `rust` `dart` `open-source` `agpl-3.0`

### OSINT Avanzado
- **[Maltego](https://maltego.com)** — Maltego is an open source intelligence (OSINT) and graphical link analysis tool for gathering and connecting information for investigative tasks. · `osint` `graph-analysis` `link-analysis` `investigacion`

### OSINT Email
- **[Hunter.io](https://hunter.io)** — Data broker providing a Web search interface for discovering the email addresses and other organizational details of a company. · `osint` `email-discovery` `brute-force` `paid`

### OSINT Tool
- **[sherlock](https://github.com/sherlock-project/sherlock)** — Hunt down social media accounts by username across social networks. · `osint` `social-media` `python` `cli`

### Online Compiler
- **[Ideone](https://ideone.com)** — An online compiler and debugging tool which allows you to compile source code and execute it online in more than 60 programming languages. · `online-compiler` `pastebin` `coding-interview`

### Online IDE
- **[OneCompiler](https://onecompiler.com)** — A free AI Powered online compiler supporting over 70 languages, including Java, Python, MySQL, C++, and HTML, for writing, running, and sharing code. · `online-ide` `web-compiler` `multi-language` `prototyping`

### PHP NLP
- **[Jieba-PHP](https://github.com/fukuball/jieba-php)** — A PHP port of Python's jieba. Chinese text segmentation for natural language processing. · `php` `nlp` `chinese` `text-processing`

### Package Management
- **[RepoFlow](https://repoflow.io)** — A simple and easy-to-use package management platform with Docker support alongside other formats like PyPI, Maven, npm, and Helm. Includes smart search, built-in Docker image scanning, and a great… · `package-registry` `docker` `self-hosted` `saas`

### Passive Reconnaissance
- **[The Harvester](https://github.com/laramies/theharvester)** — Gather emails, subdomains, hosts, employee names, open ports and banners from different public sources like search engines, PGP key servers and SHODAN computer database. · `osint` `reconnaissance` `python` `email-scraping`

### Performance Testing
- **[bencher](https://github.com/bencherdev/bencher)** — A suite of continuous benchmarking tools designed to catch performance regressions in CI. — aparece en 3 listas · `benchmarking` `ci-cd` `performance` `monitoring`
- **[loadtest](https://github.com/alexfernandez/loadtest)** — Run load tests for your web application, with an API for automation. · `load-testing` `nodejs` `performance` `api`

### Privacy Browser
- **[Brave](https://brave.com)** — Web browser with an emphasis on privacy and speed. [![Open-Source Software][OSS Icon]](https://github.com/brave/brave-browser/) ![Freeware][Freeware Icon] · `chromium` `privacy` `browser` `open-source`

### Privacy Frontend
- **[Redlib](https://github.com/redlib-org/redlib)** — An alternative private front-end to Reddit, with its origins in [Libreddit](https://github.com/libreddit/libreddit) · `rust` `frontend` `privacy` `reddit`

### Privacy Utility
- **[paaster](https://paaster.io)** — Paaster is a secure and user-friendly pastebin application that prioritizes privacy and simplicity. With end-to-end encryption and paste history, Paaster ensures that your pasted code remains… · `pastebin` `encryption` `privacy` `self-hosted`

### Probabilistic Modeling
- **[pgmpy](https://github.com/pgmpy/pgmpy)** — A Python library for probabilistic graphical models and Bayesian networks. · `probabilistic-graphical-models` `bayesian` `python` `inference`

### Process Utilities
- **[fkill](https://github.com/sindresorhus/fkill-cli)** — Fabulously kill processes. Cross-platform. · `process-management` `cli` `node`

### Project Management
- **[Focalboard](https://focalboard.com)** — Define, organize, track and manage work across individuals and teams (alternative to Trello, Notion and Asana). ) `MIT/AGPL-3.0/Apache-2.0` · `project-management` `self-hosted` `nodejs` `go`

### Project Scaffolding
- **[boilr](https://github.com/tmrts/boilr)** — Blazingly fast CLI tool for creating projects from boilerplate templates. · `cli` `golang` `scaffolding` `boilerplate`

### Prompt Optimization
- **[Context Engineering Kit](https://github.com/neolabhq/context-engineering-kit)** — by [Vlad Goncharov](https://github.com/LeoVS09) - Hand-crafted collection of advanced context engineering techniques and patterns with minimal token footprint focused on improving agent result… · `prompt-engineering` `token-optimization` `context` `agents`

### Publishing Platform
- **[Superdesk](https://superdesk.org)** — `⚠` - End-to-end news creation, production, curation, distribution, and publishing platform. `AGPL-3.0` `Docker/Python/PHP` · `cms` `news-management` `docker` `python`

### PyTorch Framework
- **[Catalyst](https://github.com/catalyst-team/catalyst)** — High-level utils for PyTorch DL & RL research. It was developed with a focus on reproducibility, fast experimentation and code/ideas reusing. Being able to research/develop something new, rather… · `pytorch` `training-framework` `python` `reproducibility`

### PyTorch Sklearn
- **[skorch](https://github.com/skorch-dev/skorch)** — A scikit-learn compatible neural network library that wraps PyTorch. · `python` `pytorch` `scikit-learn` `wrapper`

### PyTorch Training
- **[Ignite](https://github.com/pytorch/ignite)** — - Ignite is a high-level library to help with training and evaluating neural networks in PyTorch flexibly and transparently. · `pytorch` `deep-learning` `training-loops` `python`

### Python
- **[Bokeh](https://github.com/bokeh/bokeh)** — - Bokeh is an interactive visualization library for Python that enables beautiful and meaningful visual presentation of data in modern web browsers. — aparece en 4 listas · `python` `data-visualization` `interactive-charts` `open-source`
- **[Colossal-AI](https://github.com/hpcaitech/colossalai)** — - A unified deep learning system for big model era, which helps users to efficiently and quickly deploy large AI model training and inference. — aparece en 3 listas · `python` `llm` `distributed-training` `gpu`
- **[Deepchecks](https://github.com/deepchecks/deepchecks)** — - Deepchecks is a holistic open-source solution for all of your AI & ML validation needs, enabling you to test your data and models from research to production thoroughly. — aparece en 3 listas · `python` `ml-validation` `testing` `data-quality`
- **[PyMC](https://github.com/pymc-devs/pymc)** — _(label: beginner friendly)_ <br> A Python library for Bayesian statistical modeling and probabilistic machine learning. Beginner-friendly with 'good first issue' labels. — aparece en 3 listas · `bayesian` `probabilistic-ml` `statistics` `open-source`

### Python Library
- **[einops](https://github.com/arogozhnikov/einops)** — - Flexible and powerful tensor operations for readable and reliable code. · `python` `tensor-ops` `numpy` `readable-code`

### Python Notebook
- **[Marimo](https://github.com/marimo-team/marimo)** — - Reactive Python notebook — run reproducible experiments, execute as a script, deploy as an app, and version with git. · `notebook` `python` `reactive` `git-friendly`

### Python Optimization
- **[CodeFlash.AI](https://codeflash.ai)** — CodeFlash.AI – Ship Blazing-Fast Python Code, Every Time. · `python` `optimization` `saas` `ai-assisted`

### Python Trading
- **[PyBroker](https://github.com/edtechre/pybroker)** — `Python` - Algorithmic Trading with Machine Learning. · `python` `trading` `machine-learning` `backtesting`

### QUIC Protocol
- **[tencent/tquic](https://github.com/tencent/tquic)** — A high-performance, lightweight, and cross-platform QUIC library [](https://github.com/Tencent/tquic/actions/workflows/rust.yml) · `quic` `rust` `networking` `http3`

### RAG Pipeline
- **[skill-seekers/Skill_Seekers](https://github.com/yusufkaraaslan/skill_seekers)** — ](https://glama.ai/mcp/servers/yusufkaraaslan/Skill_Seekers) 🐍 🏠 🍎 🪟 🐧 - Transform 17 source types (docs, GitHub repos, PDFs, videos, Jupyter, Confluence, Notion, Slack/Discord) into AI-ready… · `mcp` `rag` `knowledge-extraction` `multi-source`

### RAG Reference
- **[Awesome RAG Production](https://github.com/yigtwxx/awesome-rag-production)** — A curated collection of battle-tested tools, frameworks, and best practices for building, scaling, and monitoring production-grade Retrieval-Augmented Generation (RAG) systems. Covers frameworks,… · `rag` `llm` `production` `curated-list`

### REPL .NET
- **[LINQPad](https://linqpad.net)** — a C#/VB/F# scratchpad that instantly executes any expression, statement block or program with rich output formatting and a wealth of features. Also lets you interactively query databases in LINQ. [$] · `csharp` `repl` `linq` `dotnet`

### RSS Reader
- **[NewsBlur](https://newsblur.com)** — Personal news reader that brings people together to talk about the world. A new sound of an old instrument. · `python` `rss-reader` `social` `self-hosted`
- **[Reeder 5](https://reederapp.com)** — News reader for Feedbin, Feedly, Feed Wrangler and so on. [![App Store][app-store Icon]](https://apps.apple.com/pl/app/reeder-5/id1529448980?platform=mac) · `rss` `news-reader` `macos` `ios`

### React Component Library
- **[material-ui](https://github.com/mui/material-ui)** — _(label: good first issue)_ <br> React components for faster and easier web development. Build your own design system, or start with Material Design. · `react` `ui-components` `material-design` `component-library`

### Real Time Encoding
- **[SimpleBinaryEncoding](https://github.com/real-logic/simple-binary-encoding)** — encoding and decoding application messages in binary format for low-latency applications. [Apache2] · `binary-codec` `low-latency` `fixed-schema` `java`

### Real Time ML Framework
- **[Oryx 2](https://github.com/oryxproject/oryx)** — Framework for building real-time, large-scale machine learning applications. Includes end-to-end applications for collaborative filtering, classification, regression, and clustering. · `java` `machine-learning` `realtime` `spark`

### Redis Client
- **[Another Redis Desktop Manager](https://github.com/qishibo/anotherredisdesktopmanager)** — A faster, better and more stable redis desktop manager [GUI client], compatible with Linux, Windows, Mac. What's more, it won't crash when loading massive keys. · `redis` `gui` `database-tools` `electron`

### Regex Generator
- **[grex](https://github.com/pemistahl/grex)** — A command-line tool and library for generating regular expressions from user-provided test cases · `regex` `rust` `cli` `code-generation`

### Remote Access VPN
- **[Firezone](https://firezone.dev)** — Secure remote access gateway that supports the WireGuard protocol. It offers a Web GUI, 1-line install script, multi-factor auth (MFA), and SSO. · `wireguard` `vpn` `self-hosted` `mfa-sso`

### Remote Management
- **[MeshCentral](https://meshcentral.com)** — Run your own web server to remotely manage and control computers on a local network or anywhere on the internet. · `nodejs` `remote-management` `web-ui` `self-hosted`

### Resources
- **[Docker for novices](https://youtube.com/watch)** — An introduction to Docker for developers and testers who have never used it. (Video 1h40, recorded linux.conf.au 2019 — Christchurch, New Zealand) by Alex Clews. — 🔥 aparece en 16 listas · `docker` `containers` `beginners` `video`

### Reverse Engineering
- **[x64dbg](https://x64dbg.com)** — An open-source x64/x32 debugger for windows. · `debugger` `reverse-engineering` `x64` `windows`

### Reverse Proxy
- **[Pomerium](https://pomerium.io)** — Identity-aware reverse proxy, successor to now obsolete oauth_proxy. It inserts an OAuth step before proxying your request to the backend, so that you can safely expose your self-hosted websites… · `reverse-proxy` `oauth` `identity` `go`

### Rust
- **[Readest](https://github.com/readest/readest)** — _(label: good first issue)_ <br> A modern, feature-rich ebook reader designed for avid readers offering seamless cross-platform access, powerful tools, and an intuitive interface. — aparece en 3 listas · `rust` `desktop-app` `ebook-reader` `cross-platform`

### Rust Deep Learning
- **[burn](https://github.com/tracel-ai/burn)** — Burn is a new comprehensive dynamic Deep Learning Framework built using Rust with extreme flexibility, compute efficiency and portability as its primary goals · `rust` `deep-learning` `gpu` `dynamic-computation`
- **[candle](https://github.com/huggingface/candle)** — Candle is a minimalist ML framework for Rust with a focus on performance (including GPU support) and ease of use. · `rust` `deep-learning` `gpu` `minimalist`

### Rust IDE
- **[RustRover](https://jetbrains.com/rust)** — A powerful Rust IDE by JetBrains, free for individual non-commercial use · `ide` `rust` `jetbrains` `debugger`

### Rust ML Bindings
- **[tch-rs](https://github.com/laurentmazare/tch-rs)** — Rust bindings for the C++ API of PyTorch · `rust` `pytorch` `bindings` `deep-learning`

### Rust ML Kit
- **[linfa](https://github.com/rust-ml/linfa)** — a comprehensive toolkit to build Machine Learning applications with Rust · `rust` `machine-learning` `supervised` `unsupervised`

### Rust NLP Inference
- **[rust-bert](https://github.com/guillaume-be/rust-bert)** — Rust native ready-to-use NLP pipelines and transformer-based models (BERT, DistilBERT, GPT2,...) · `rust` `nlp` `transformers` `inference`

### Rust String Library
- **[ashvardanian/stringzilla](https://github.com/ashvardanian/stringzilla)** — SIMD-accelerated string search, sort, edit distances, alignments, and generators for x86 AVX2 & AVX-512, and Arm NEON [](https://crates.io/crates/stringzilla) · `simd` `rust` `strings` `performance`

### SQL Database
- **[Dolt](https://github.com/dolthub/dolt)** — - Dolt is a SQL database that you can fork, clone, branch, merge, push and pull just like a git repository. · `database` `sql` `version-control` `go`

### SQL Tooling
- **[ajitpratap0/GoSQLX](https://github.com/ajitpratap0/gosqlx)** — ](https://glama.ai/mcp/servers/ajitpratap0/GoSQLX) 🏎️ ☁️ 🏠 - 7 SQL tools (validate, format, parse, lint, security scan, metadata extraction, full analysis) over Streamable HTTP. Public remote… · `go` `sql` `http-api` `linting`

### SSH Client
- **[Termius](https://termius.com)** — A beautiful SSH and SFTP client for Mac. It is also available for mobile. ![Freeware][Freeware Icon] [![App Store][app-store… · `ssh` `sftp` `terminal` `mac`

### Scientific Visualization
- **[vispy](https://github.com/vispy/vispy)** — GPU-based high-performance interactive OpenGL 2D/3D data visualization library. · `python` `gpu` `visualization` `opengl`

### Scientific Viz
- **[pyqtgraph](https://github.com/pyqtgraph/pyqtgraph)** — Interactive and realtime 2D/3D/Image plotting and science/engineering widgets. · `python` `visualization` `qt` `plotting`

### Secrets Management
- **[ssh-vault](https://github.com/ssh-vault/ssh-vault)** — A simple tool to manage secrets using ssh keys for encryption and decryption. · `secrets-management` `ssh` `encryption` `cli`

### Secure Chat
- **[Element](https://element.io)** — Create, share communicate. Chat and call securely. [![Open-Source Software][OSS Icon] ![Freeware][Freeware Icon]](https://github.com/vector-im) · `matrix` `chat` `encrypted` `federation`

### Secure Communication
- **[Keybase](https://keybase.io)** — Secure groups, files, and chat for everyone! [![Open-Source Software][OSS Icon]](https://github.com/keybase) ![Freeware][Freeware Icon] · `crypto` `e2e` `chat` `security`

### Security
- **[themis](https://github.com/cossacklabs/themis)** — High level crypto library for storing data (AES), secure messaging (ECC + ECDSA / RSA + PSS + PKCS#7) and session-oriented, forward secrecy data exchange (ECDH key agreement, ECC & AES… — 🔥 aparece en 7 listas · `cryptography` `security` `multi-platform` `open-source`
- **[mariocandela/beelzebub](https://github.com/mariocandela/beelzebub)** — ☁️ - Beelzebub is a honeypot framework that lets you build honeypot tools using MCP. Its purpose is to detect prompt injection or malicious agent behavior. The underlying idea is to provide the… · `honeypot` `security` `ai-safety` `prompt-injection`

### Security Auditing
- **[Trail of Bits Security Skills](https://github.com/trailofbits/skills)** — by [Trail of Bits](https://github.com/trailofbits) - A very professional collection of over a dozen security-focused skills for code auditing and vulnerability detection. Includes skills for… · `security` `code-audit` `codeql` `semgrep`

### Security Defense
- **[Honeypots](https://github.com/paralax/awesome-honeypots)** — Deception trap, designed to entice an attacker into attempting to compromise the information systems in an organization. — aparece en 3 listas · `security` `honeypots` `threat-detection` `curated-list`

### Security Sandbox
- **[mavdol/capsule/mcp-server](https://github.com/mavdol/capsule)** — ](https://glama.ai/mcp/servers/mavdol/capsule-mcp-server) 🦀 🏠 🍎 🪟 🐧 - Run untrusted Python/JavaScript code in WebAssembly sandboxes. · `mcp` `wasm` `sandbox` `rust`

### Security Testing
- **[kpcyrd/authoscope](https://github.com/kpcyrd/authoscope)** — A scriptable network authentication cracker · `rust` `pentest` `network` `security`

### Security Tooling
- **[Agentic Radar](https://github.com/splx-ai/agentic-radar)** — Open-source CLI security scanner for agentic workflows. Scans your workflow’s source code, detects vulnerabilities, and generates an interactive visualization along with a detailed security… · `security` `cli` `agentic-workflows` `langraph`

### Self Hosted Apps
- **[orhun/rustypaste](https://github.com/orhun/rustypaste)** — A minimal file upload/pastebin service · `rust` `self-hosted` `file-upload` `minimal`
- **[ryot](https://github.com/ignisda/ryot)** — Track various facets of your life - media, fitness, etc. · `self-hosted` `docker` `tracking` `privacy-first`
- **[SinTan1729/Chhoto URL](https://github.com/sintan1729/chhoto-url)** — A simple, blazingly fast, selfhosted URL shortener with no unnecessary features.[](https://github.com/SinTan1729/chhoto-url/actions/workflows/docker-release.yml) · `rust` `self-hosted` `url-shortener` `cli`

### Self Hosted Proxy
- **[Outline Server](https://getoutline.org)** — A proxy server that runs a Shadowsocks instance for each access key and a REST API to manage the access keys. · `proxy` `shadowsocks` `docker` `nodejs`

### Server Implementations
- **[juspay/neurolink](https://github.com/juspay/neurolink)** — 📇 ☁️ 🏠 🍎 🪟 🐧 - Making enterprise AI infrastructure universally accessible. Edge-first platform unifying 12 providers and 100+ models with multi-agent orchestration, HITL workflows, guardrails… — aparece en 3 listas · `edge-computing` `multi-agent` `enterprise` `orchestration`
- **[pydantic-ai](https://github.com/pydantic/pydantic-ai)** — A Python agent framework for building generative AI applications with structured schemas. · `python` `ai-agents` `llm` `pydantic`
- **[txn2/kubefwd](https://github.com/txn2/kubefwd)** — 🏎️ 🏠 - Kubernetes bulk port forwarding with service discovery, /etc/hosts management, traffic monitoring, and pod log streaming · `kubernetes` `port-forwarding` `cli` `go`

### Shell Replacement
- **[nushell](https://github.com/nushell/nushell)** — _(label: good first issue)_ <br> A modern shell for the GitHub era written in Rust. · `rust` `shell` `cli` `unix`

### Shell Resources
- **[awesome-zsh-plugins](https://github.com/unixorn/awesome-zsh-plugins)** — ZSH frameworks, plugins, tutorials & themes. · `zsh` `curated-list` `shells` `reference`

### Software Packages
- **[lstags](https://github.com/ivanilves/lstags)** — Tool and API to sync Docker images across different registries. — aparece en 3 listas · `docker` `registry` `devops` `golang`

### Spotify CLI
- **[LargeModGames/spotatui](https://github.com/largemodgames/spotatui)** — ] - A Spotify terminal client with native streaming, synced lyrics, and real-time audio visualization [](https://github.com/LargeModGames/spotatui/actions/workflows/cd.yml) · `rust` `cli` `spotify` `audio`

### Static Analysis
- **[Cppcheck](https://cppcheck.sourceforge.net)** — A tool for static C/C++ code analysis. - [source](https://github.com/danmar/cppcheck) · `static-analysis` `cpp` `c` `linter`

### Stream Database
- **[RisingWave](https://github.com/risingwavelabs/risingwave)** — - A distributed SQL streaming database that unifies stream processing and low-latency serving, ideal for building and serving features for online machine learning. · `rust` `streaming` `sql` `feature-store`

### Swift
- **[Awesome Core ML Models](https://github.com/likedan/awesome-coreml-models)** — A curated list of machine learning models in CoreML format. — aparece en 3 listas · `swift` `coreml` `ios` `curated-list`

### Swift Crypto Lib
- **[CryptoSwift](https://github.com/krzyzanowskim/cryptoswift)** — Crypto related functions and helpers for Swift implemented in Swift programming language. · `swift` `cryptography` `ios` `aes`

### Swift NaCl Library
- **[Swift-Sodium](https://github.com/jedisct1/swift-sodium)** — Swift interface to the Sodium library for common crypto operations for iOS and macOS. · `swift` `libsodium` `nacl` `cryptography`

### Synthetic Data Generation
- **[TabGAN](https://github.com/diyago/tabular-data-generation)** — - Synthetic tabular data generation using GANs (CTGAN), Diffusion Models, and LLMs with adversarial filtering, privacy metrics, and sklearn integration. · `synthetic-data` `gan` `tabular` `privacy`

### System Monitoring
- **[glances](https://nicolargo.github.io/glances)** — Open-source, cross-platform real-time monitoring tool with CLI and web dashboard interfaces and many exporting options. · `monitoring` `cli` `python` `cross-platform`

### Tabular AutoML
- **[mljar-supervised](https://github.com/mljar/mljar-supervised)** — - A Python package for AutoML on tabular data with feature engineering, hyper-parameters tuning, explanations and automatic documentation. · `automl` `tabular-data` `python` `feature-engineering`

### Task Management
- **[Super Productivity](https://super-productivity.com)** — Task manager with timeboxing and time tracking. [![Open-Source Software][OSS Icon]](https://github.com/johannesjo/super-productivity) ![Freeware][Freeware Icon] [![App Store][app-store… · `task-management` `time-tracking` `productivity` `open-source`

### Terminal Apps
- **[Wave](https://github.com/wavetermdev/waveterm)** — Open-source terminal with built-in file previews, web browsing, and AI tools. [![Open-Source Software][OSS Icon]](https://github.com/wavetermdev/waveterm) ![Freeware][Freeware Icon] — aparece en 3 listas · `terminal` `rust` `ai-integration` `open-source`

### Terminal Emulator
- **[Warp](https://warp.dev)** — Warp is a blazingly fast, rust-based terminal reimagined from the ground up to work like a modern app. · `terminal` `rust` `cli` `cross-platform`

### Terminal File Manager
- **[xplr](https://github.com/sayanarijit/xplr)** — A hackable, minimal, fast TUI file explorer. · `rust` `tui` `file-manager` `hackable`
- **[yazi](https://github.com/sxyazi/yazi)** — Blazing fast terminal file manager, based on async I/O. · `rust` `tui` `async` `file-manager`

### Test Framework
- **[Mocha](https://github.com/mochajs/mocha)** — _(label: good first issue)_ <br> Javascript test framework for Node.js and the browser. — aparece en 3 listas · `javascript` `testing` `nodejs` `browser`

### Text Editor
- **[GNU Emacs](https://gnu.org/software/emacs)** — An extensible, customizable text editor-and more. `GPL-3.0` `C` · `editor` `lisp` `cli` `text-editor`
- **[helix](https://github.com/helix-editor/helix)** — A post-modern modal text editor inspired by Neovim/Kakoune. [](https://github.com/helix-editor/helix/actions) · `editor` `rust` `modal` `cli`
- **[micro](https://micro-editor.github.io)** — Modern and intuitive terminal-based text editor. [![Open-Source Software][OSS Icon]](https://github.com/ory/editor) ![Freeware][Freeware Icon] · `terminal-editor` `golang` `cli` `lightweight`

### Text Processing
- **[Retext](https://github.com/retextjs/retext)** — Extensible system for analyzing and manipulating natural language. · `javascript` `nodejs` `nlp` `text-processing`

### Time Series Database
- **[QuestDB](https://github.com/questdb/questdb)** — High-performance SQL database for time series. Supports InfluxDB line protocol, PostgreSQL wire protocol, and REST. · `timeseries` `sql` `java` `high-performance`

### Time Tracking
- **[ActivityWatch](https://activitywatch.net)** — Cross-platform, extensible, and privacy-focused time-tracker. [![Open-Source Software][OSS Icon]](https://github.com/ActivityWatch/activitywatch) ![Freeware][Freeware Icon] · `self-hosted` `privacy` `time-tracking` `cross-platform`

### Torrent Client
- **[Deluge](https://deluge-torrent.org)** — Deluge is a lightweight, Free Software, cross-platform BitTorrent client. [![Open-Source Software][OSS Icon]](https://dev.deluge-torrent.org/wiki/Development) ![Freeware][Freeware Icon] · `bittorrent` `python` `cross-platform` `lightweight`

### Trading Analysis
- **[ticker](https://github.com/achannarasappa/ticker)** — Terminal stock watcher and stock position tracker. · `go` `technical-analysis` `indicators` `backtesting`

### TypeScript
- **[Amplication](https://github.com/amplication/amplication)** — _(label: good first issue)_ <br> Amplication is an open-source development tool. It helps you develop quality Node.js applications without spending time on repetitive coding tasks. — aparece en 3 listas · `code-generation` `nodejs` `backend` `low-code`
- **[Vitest](https://github.com/vitest-dev/vitest)** — _(label: good first issue)_ <br> A blazing fast unit test framework powered by Vite. — aparece en 3 listas · `typescript` `testing` `vite` `jest-alternative`

### UI Framework
- **[grommet](https://github.com/grommet/grommet)** — _(label: good first issue)_ <br> a react-based framework that provides accessibility, modularity, responsiveness, and theming in a tidy package · `react` `component-library` `accessible` `theming`

### UK Company Tools
- **[uk-company-number](https://github.com/borschai/uk-company-number)** — `Python` - Validate, format, and identify UK Companies House company numbers. Supports all 27 prefixes. [PyPI](https://pypi.org/project/uk-company-number/) · `python` `uk-companies` `validation` `pypi`
- **[uk-sic-codes](https://github.com/borschai/uk-sic-codes)** — `Python` - UK SIC 2007 industry classification code lookup, search, and validation. 731 codes, 21 sections. [PyPI](https://pypi.org/project/uk-sic-codes/) · `python` `sic-codes` `uk-industry` `classification`

### Vector Database
- **[Chroma](https://github.com/chroma-core/chroma)** — - Chroma is an open-source embedding database. · `vector-db` `embeddings` `rag` `python`
- **[Infinity](https://github.com/infiniflow/infinity)** — The AI-native database built for LLM applications, providing incredibly fast vector and full-text search. Developed using C++20 · `vector-db` `c++` `self-hosted` `llm`

### Vector Databases
- **[USearch](https://github.com/unum-cloud/usearch)** — Similarity Search Engine for Vectors and Strings [](https://crates.io/crates/usearch) · `vector-search` `similarity-search` `rust` `c++`

### Vector Graphics Editor
- **[Vectr](https://vectr.com)** — Vectr is a free graphics software used to create vector graphics easily and intuitively. It's a simple yet powerful web and desktop cross-platform tool to bring your designs into reality. · `vector-graphics` `design` `free` `web-desktop`

### Video Automation
- **[editly](https://github.com/mifi/editly)** — Declarative video editing API. · `video` `editing` `declarative` `javascript`

### Video Trimming
- **[LosslessCut](https://github.com/mifi/lossless-cut)** — Cross platform tool for quick and lossless video and audio trimming using ffmpeg. [![Open-Source Software][OSS Icon] ![Freeware][Freeware Icon]](https://github.com/mifi/lossless-cut) · `ffmpeg` `video-editing` `cross-platform` `cli-gui`

### Videos
- **[Functional Programming with TypeScript](https://youtube.com/playlist)** — Discover functional programming with Typescript and create a library like fp-ts alongside Sahand Javid in this beginner-friendly YouTube playlist. — 🔥 aparece en 11 listas · `typescript` `functional-programming` `fp-ts` `video-tutorial`

### Virtualization
- **[QEMU](https://qemu.org)** — A free and open-source emulator and virtualizer that can perform hardware virtualization. [![Open-Source Software][OSS Icon]](https://github.com/qemu/qemu) ![Freeware][Freeware Icon] · `virtualization` `vm` `gui` `freeware`

### Vision Pretraining
- **[LightlyTrain](https://github.com/lightly-ai/lightly-train)** — - Pretrain computer vision models on unlabeled data for industrial applications. · `computer-vision` `self-supervised` `pytorch` `python`

### Web Archiving
- **[Certificate Ripper](https://github.com/hakky54/certificate-ripper)** — CLI tool and library for extracting and exporting server certificates from HTTPS endpoints. · `go` `web-archiving` `self-hosted` `ipfs`

### Web Framework Go
- **[gofiber/fiber](https://github.com/gofiber/fiber)** — Clean project logo. Useful badges and links (languages switcher, code style, test cover, docs, Discord channel). Clear description of what the project does with quickstart, benchmark charts,… · `web-framework` `go` `http` `performance`

### Web Monitoring
- **[changedetection.io](https://changedetection.io)** — Stay up-to-date with web-site content changes. · `web-monitoring` `change-detection` `python` `self-hosted`

### Windows Utilities
- **[Water-Run/treepp](https://github.com/water-run/treepp)** — A Rust-based native Windows `tree` replacement with diff-level input/output compatibility on successful runs, many more features including essential exclusions and `.gitignore` support, and… · `rust` `windows` `cli` `file-tree`

### Workflow Engine
- **[Prefect Core](https://github.com/prefecthq/prefect)** — - Workflow management system that makes it easy to take your data pipelines and add semantics like retries, logging, dynamic mapping, caching, failure notifications, and more. · `python` `workflow-orchestration` `dag` `job-scheduler`

### Workflow Orchestration
- **[Luigi](https://github.com/spotify/luigi)** — - Luigi is a Python module that helps you build complex pipelines of batch jobs, handling dependency resolution, workflow management, visualisation, etc.. · `python` `workflow` `batch` `dag`

### Writing Editor
- **[Typora](https://typora.io)** — Truly minimal Markdown editor featuring seamless live preview. · `markdown` `editor` `minimal` `wysiwyg`

### Índice Referencia
- **[Forensics](https://github.com/cugu/awesome-forensics)** — Free (mostly open source) forensic analysis tools and resources. · `forense` `osint` `recursos` `curado`

---

## 🤖 Por qué confiar en esta lista

- **Transparente**: toda la metodología y scores están públicos en [juanchi.dev/awesome/sources](https://juanchi.dev/awesome/sources) (próximamente)
- **Auto-regulada**: si un `awesome-*` deja de mantenerse, cae al BENCH y eventualmente sale
- **Human-in-the-loop**: no es IA sola. Tools con ⭐ GEM pasan primero por Claude, después por veredicto humano de [Juan Torchia](https://juanchi.dev)
- **Reproducible**: este README se regenera semanalmente. El sistema documentado en [juanchi.dev/blog/series/awesome-curated](https://juanchi.dev/blog/series/awesome-curated)

## 🤝 Contribuir

- 🐛 ¿Tool mal clasificada? → [Abrí un issue](https://github.com/JuanTorchia/awesome-curated/issues/new)
- ➕ ¿Falta una tool importante? → Issue con el link + justificación
- 📝 ¿Querés proponer una fuente? → Mandá un repo `awesome-*` que debamos scrapear

## 📬 Newsletter

Recibí el digest mensual con las tools nuevas que entran al roster → [juanchi.dev/newsletter](https://juanchi.dev)

---

<sub>📄 Generado automáticamente desde [juanchi.dev](https://juanchi.dev) · [código del sistema](https://juanchi.dev/blog/series/awesome-curated) · MIT licensed</sub>
