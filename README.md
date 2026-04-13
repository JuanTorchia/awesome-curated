# Awesome Curated

> Lista **auto-curada** de herramientas de desarrollo.
> Harvest semanal de 20 awesome-* repos activos en GitHub, deduplicado cross-fuente,
> clasificado por IA + veredicto humano.

**Actualizado:** 2026-04-13 · Última sync automática

---

## 📊 Métricas

| Qué | Cuánto |
|---|---|
| Fuentes activas (ROSTER + BENCH) | **20** |
| Items totales scrapeados | **28,417** |
| Tools con señal cross-awesome (x≥2) | **1,479** |
| ⭐ GEMs (estándar de la industria) | **62** |
| 👍 Worth trying | **70** |

---

## 🎯 Cómo se curó

1. **Discovery**: Motor de búsqueda en GitHub API (GraphQL batched) detecta repos `awesome-*` con stars ≥ 500 (ROSTER) / 250 (BENCH) y commits recientes.
2. **Scoring** 0–100 en 5 dimensiones: freshness 35% + activity 20% + popularity 15% + depth 20% + community health 10%.
3. **Dedupe cross-source**: items que aparecen en 2+ awesomes se agrupan en un `CuratedTool` único. `appearsInCount` = señal cruzada de consenso.
4. **Clasificación IA**: Claude (Anthropic) asigna `GEM | WORTH_TRYING | MEH | HYPE | DEAD` con razonamiento por item.
5. **Verdict humano**: Juan confirma/overridea las sugerencias IA. Los tools marcados con 👤 tienen verdict humano.

Más detalle técnico → [Blog series en juanchi.dev](https://juanchi.dev/blog/series/awesome-curated)

---

## ⭐ GEMs — estándares de la industria
Herramientas que la comunidad considera default. Si no las conocés, valen la pena.

### AI Framework
- **[Vercel AI](https://github.com/vercel/ai)** — - Vercel AI is a TypeScript toolkit designed to help you build AI-powered applications using popular frameworks like Next.js, React, Svelte, Vue and runtimes like Node.js. — appears in 3 lists · `typescript` `nextjs` `react` `llm-integration`

### API Code Generation
- **[OpenAPI Generator](https://github.com/openapitools/openapi-generator)** — OpenAPI Generator allows generation of API client libraries (e.g. C#, TypeScript, etc), server stubs (ASP.NET Core, NancyFx, etc), documentation and configuration automatically given an OpenAPI… · `openapi` `codegen` `api` `documentation`

### C++
- **[TensorFlow](https://github.com/tensorflow/tensorflow)** — - TensorFlow is a leading library designed for developing and deploying state-of-the-art machine learning applications. — 🔥 appears in **6** lists · `machine-learning` `deep-learning` `python` `c++`
- **[LightGBM](https://github.com/microsoft/lightgbm)** — Microsoft's fast, distributed, high performance gradient boosting (GBDT, GBRT, GBM or MART) framework based on decision tree algorithms, used for ranking, classification and many other machine… — appears in 3 lists · `machine-learning` `gradient-boosting` `distributed` `python`

### CI/CD Pipeline
- **[GitLab CI](https://about.gitlab.com/solutions/continuous-integration)** — Gitlab's built-in, full-featured CI/CD solution. · `cicd` `gitlab` `devops` `pipelines`

### CI/CD Platform
- **[Concourse](https://concourse-ci.org)** — Concourse is a CI tool that treats pipelines as first class objects and containerizes every step along the way. ) · `ci-cd` `go` `self-hosted` `open-source`

### Container Monitoring
- **[cadvisor](https://github.com/google/cadvisor)** — Analyzes resource usage and performance characteristics of running containers. · `containers` `monitoring` `go` `kubernetes`

### Data Visualization
- **[matplotlib](https://github.com/matplotlib/matplotlib)** — - A Python 2D plotting library which produces publication-quality figures in a variety of hardcopy formats and interactive environments across platforms. — appears in 3 lists · `feature-engineering` `python` `sklearn` `ml`
- **[Streamlit](https://github.com/streamlit/streamlit)** — - Streamlit lets you create apps for your machine learning projects with deceptively simple Python scripts. It supports hot-reloading, so your app updates live as you edit and save your file. — appears in 3 lists · `python` `web-framework` `ml-apps` `rapid-prototyping`
- **[Apache ECharts](https://github.com/apache/echarts)** — - Apache ECharts is a powerful, interactive charting and data visualization library for browser. · `dataviz` `javascript` `interactive` `charts`

### Deep Learning
- **[Stable Baselines](https://github.com/dlr-rm/stable-baselines3)** — - A fork of OpenAI Baselines, implementations of reinforcement learning algorithms. — appears in 3 lists · `reinforcement-learning` `python` `pytorch` `tensorflow`

### Deep Learning Library
- **[oneDNN](https://github.com/oneapi-src/onednn)** — An open-source cross-platform performance library for deep learning applications. [Apache] [website](https://01.org/onednn) · `deep-learning` `cpp` `cpu-optimization` `gpu`

### Developer Tools
- **[Docker](https://docker.com)** — Powerful, performs operating-system-level virtualization. [![Open-Source Software][OSS Icon]](https://github.com/docker) ![Freeware][Freeware Icon] [![Awesome List][awesome-list… — appears in 4 lists · `containers` `devops` `virtualization`
- **[mitmproxy](https://mitmproxy.org)** — A Python tool used for intercepting, viewing and modifying network traffic. Invaluable in troubleshooting certain problems. — appears in 3 lists · `python` `proxy` `debugging` `security`
- **[Wireshark](https://wireshark.org)** — The world’s foremost and widely-used network protocol analyzer. [![Open-Source Software][OSS Icon]](https://github.com/wireshark/wireshark) ![Freeware][Freeware Icon] — appears in 3 lists · `network` `pcap` `wireshark` `cli-gui`

### Development Tools
- **[Visual Studio Code](https://code.visualstudio.com)** — Microsoft's free & open-source editor, TypeScript friendly, [VSCode Plugins](editor-plugin.md#vscode-plugin). [![Open-Source Software][OSS Icon]](https://github.com/Microsoft/vscode)… — appears in 4 lists · `editor` `typescript` `vscode-plugins`

### Distributed Computing
- **[RLlib](https://github.com/ray-project/ray)** — RLlib is an industry level, highly scalable RL library for tf and torch, based on Ray. It's used by companies like Amazon and Microsoft to solve real-world decision making problems at scale. — appears in 3 lists · `reinforcement-learning` `ray` `python` `distributed`

### Distributed Data Processing
- **[Dask](https://github.com/dask/dask)** — - Distributed parallel processing framework for Pandas and NumPy computations. · `python` `distributed-computing` `pandas` `numpy`

### Distributed Systems
- **[ZooKeeper](https://zookeeper.apache.org)** — ZooKeeper is a centralized service for maintaining configuration information, naming, providing distributed synchronization, and providing group services. — appears in 3 lists · `java` `distributed-coordination` `apache` `consensus`

### Docker SDK
- **[Docker.DotNet](https://github.com/microsoft/docker.dotnet)** — C#/.NET HTTP client for the Docker remote API. · `csharp` `dotnet` `docker-api` `client-library`

### Go
- **[Kubernetes](https://github.com/kubernetes/kubernetes)** — _(label: good first issue)_ <br> Production-Grade Container Scheduling and Management System — appears in 3 lists · `kubernetes` `container-orchestration` `go` `distributed-systems`
- **[Moby](https://github.com/moby/moby)** — Collaborative project for the container ecosystem to assemble container-based systems. — appears in 3 lists · `go` `containers` `docker` `open-source`

### Identity Management
- **[KeyCloak](https://keycloak.org)** — Open Source Identity and Access Management. · `iam` `oauth2` `java` `self-hosted`

### Java Build Tool
- **[Apache Maven](https://maven.apache.org)** — Build automation tool mainly for Java. A software project management and comprehension tool. Based on the concept of a project object model (POM), Maven can manage a project's build, reporting and… · `java` `build-automation` `dependency-management` `xml`
- **[Gradle](https://gradle.org)** — Incremental builds programmed via Groovy instead of declaring XML. Works well with Maven's dependency management. · `java` `build-automation` `groovy` `incremental`

### JavaScript
- **[Jest](https://github.com/facebook/jest)** — _(label: good first issue)_ <br> A complete and easy to set up JavaScript testing solution. — 🔥 appears in **5** lists · `testing` `javascript` `typescript` `mocking`
- **[Next.js](https://github.com/vercel/next.js)** — _(label: good first issue)_ <br> A minimalistic framework for universal server-rendered React applications — 🔥 appears in **5** lists · `react` `ssr` `typescript` `full-stack`
- **[Netron](https://github.com/lutzroeder/netron)** — - Netron is a viewer for neural network, deep learning and machine learning models. — appears in 4 lists · `neural-networks` `visualization` `ml-models`
- **[Vite](https://github.com/vitejs/vite)** — _(label: good first issue)_ <br> Next generation frontend tooling. It's fast! Alternative to Create React App — appears in 4 lists · `build-tool` `frontend` `javascript` `typescript`
- **[Babel](https://github.com/babel/babel)** — _(label: good first issue)_ <br> A compiler for writing next generation JavaScript. — appears in 3 lists · `javascript` `transpiler` `babel` `ast`
- **[D3js](https://d3js.org)** — is a powerful data visualization javascript library. — appears in 3 lists · `javascript` `visualization` `svg` `data-driven`
- **[ESLint](https://github.com/eslint/eslint)** — _(label: good first issue)_ <br> A fully pluggable tool for identifying and reporting on patterns in JavaScript. — appears in 3 lists · `javascript` `linting` `eslint` `typescript`
- **[React Native](https://github.com/facebook/react-native)** — _(label: Good-first-issue)_ <br> A framework for building native apps with React. — appears in 3 lists · `javascript` `react` `mobile` `cross-platform`
- **[Vue.js](https://github.com/vuejs/vue)** — _(label: good first issue)_ <br> The Progressive JavaScript Framework. — appears in 3 lists · `javascript` `vue` `spa` `frontend`

### JavaScript Runtime
- **[Node.js](https://github.com/sindresorhus/awesome-nodejs)** — Async non-blocking event-driven JavaScript runtime built on Chrome's V8 JavaScript engine. — appears in 4 lists · `nodejs` `javascript` `runtime`

### Knowledge Management
- **[Obsidian](https://obsidian.md)** — Obsidian is a powerful knowledge base on top of a local folder of plain text Markdown files. — appears in 4 lists · `markdown` `local-first` `knowledge-base` `self-hosted`

### ML Research
- **[Dlib](https://github.com/davisking/dlib)** — zap: - A toolkit for making real world machine learning and data analysis applications in C++. [Boost] [website](http://dlib.net/) · `python` `automatic-differentiation` `jit-compiler` `numpy-compatible`

### Machine Learning
- **[BayesWitnesses/m2cgen](https://github.com/bayeswitnesses/m2cgen)** — A CLI tool to transpile trained classic machine learning models into a native Rust code with zero dependencies. [](https://github.com/BayesWitnesses/m2cgen/actions) — 🔥 appears in **7** lists · `machine-learning` `code-generation` `model-export` `open-source`
- **[XGBoost](https://github.com/dmlc/xgboost)** — - XGBoost is an optimized distributed gradient boosting library designed to be highly efficient, flexible and portable. — 🔥 appears in **5** lists · `machine-learning` `gradient-boosting` `python` `distributed`
- **[Apache Spark](https://github.com/apache/spark)** — - Micro-batch processing for streams using the apache spark framework as a backend supporting stateful exactly-once semantics. — appears in 3 lists · `ai-agents` `memory` `python` `storage`

### Message Broker
- **[ActiveMQ](https://activemq.apache.org)** — Java message broker. · `java` `message-broker` `messaging` `apache`

### Monitoring TSDB
- **[Prometheus](https://prometheus.io)** — Service monitoring system and time series database. · `monitoring` `tsdb` `go` `open-source`

### Natural Language Processing
- **[SpaCy](https://github.com/explosion/spacy)** — - spaCy is a library for advanced Natural Language Processing in Python and Cython. — appears in 3 lists · `nlp` `python` `spacy` `nlp-pipeline`

### Node Process Mgr
- **[pm2](https://github.com/unitech/pm2)** — Production Process Manager for Node.js. · `node.js` `process-manager` `production` `clustering`

### P2P Sync
- **[Syncthing](https://syncthing.net)** — Syncthing is an open source peer-to-peer file synchronisation tool. · `sync` `p2p` `self-hosted` `go`

### Python
- **[Pytorch](https://github.com/pytorch/pytorch)** — _(label: good first issue)_ <br> PyTorch is an open source machine learning library based on the Torch library, used for applications such as computer vision and natural language processing. — 🔥 appears in **6** lists · `deep-learning` `machine-learning` `python` `gpu`
- **[Jupyter Notebooks](https://github.com/jupyter/notebook)** — - Web interface python sandbox environments for reproducible development — appears in 3 lists · `python` `jupyter` `notebook` `interactive`
- **[PyG](https://github.com/pyg-team/pytorch_geometric)** — - PyG (PyTorch Geometric) is a library built upon PyTorch to easily write and train Graph Neural Networks (GNNs) for a wide range of applications related to structured data. — appears in 3 lists · `gnn` `pytorch` `python` `ml`
- **[scikit-learn](https://github.com/scikit-learn/scikit-learn)** — - Scikit-learn is a powerful machine learning library that provides a wide variety of modules for data access, data preparation and statistical model building. — appears in 3 lists · `python` `machine-learning` `sklearn` `supervised`
- **[SymPy](https://github.com/sympy/sympy)** — _(label: Easy-to-Fix)_ <br> A Python library for symbolic mathematics. — appears in 3 lists · `python` `mathematics` `symbolic-computation` `open-source`
- **[Transformers](https://github.com/huggingface/transformers)** — - Huggingface's library of state-of-the-art pretrained models for Natural Language Processing (NLP). — appears in 3 lists · `python` `nlp` `transformers` `pytorch`

### Reinforcement Learning
- **[TF-Agents](https://github.com/tensorflow/agents)** — - A reliable, scalable and easy to use TensorFlow library for contextual bandits and reinforcement learning. · `reinforcement-learning` `tensorflow` `python` `contextual-bandits`

### Reverse Proxy
- **[Træfɪk](https://github.com/containous/traefik)** — Automated reverse proxy and load-balancer for Docker, Mesos, Consul, Etcd... By [EmileVauge](https://github.com/emilevauge). · `reverse-proxy` `load-balancer` `docker` `kubernetes`

### Rust Node Bridge
- **[Neon](https://github.com/neon-bindings/neon)** — Rust bindings for writing safe and fast native Node.js modules. · `rust` `node.js` `native-bindings` `ffi`

### Security Audit
- **[Lynis](https://cisofy.com/lynis)** — Auditing tool for UNIX-based systems. · `security` `audit` `unix` `cli`

### Statistical Modeling
- **[statsmodels](https://github.com/statsmodels/statsmodels)** — Statistical modelling and econometrics in Python. · `python` `statistics` `econometrics` `timeseries`

### Testing E2E
- **[Playwright](https://github.com/microsoft/playwright)** — Node.js library to automate Chromium, Firefox and WebKit with a single API. — appears in 4 lists · `testing` `e2e` `automation` `browser`

### Text Editor
- **[Vim](https://vim.org)** — An old terminal-based editor. For common plugins, check [Vim Common Plugins](editor-plugin-zh.md#vim-plugin). [![Open-Source Software][OSS Icon]](https://github.com/vim/vim) ![Freeware][Freeware… · `editor` `terminal` `modal` `unix`

### Tools
- **[DVC](https://github.com/iterative/dvc)** — Data Science Version Control is an open-source version control system for machine learning projects with pipelines support. It makes ML projects reproducible and shareable. — appears in 3 lists · `data-science` `version-control` `ml-pipelines`

### TypeScript
- **[Visual Studio Code](https://github.com/microsoft/vscode)** — New type of tool that combines the simplicity of a code editor with what developers need for their core edit-build-debug cycle. Code provides comprehensive editing and debugging support, an… — appears in 4 lists · `editor` `typescript` `open-source` `debugging`

### Utilities
- **[Bitwarden](https://bitwarden.com)** — Open source password management tool for Mac OS, iOS and browsers. [![Open-Source Software][OSS Icon]](https://github.com/bitwarden) ![Freeware][Freeware Icon] — appears in 3 lists · `password-manager` `security` `open-source` `self-hosted`

### Web Servers
- **[grpc](https://github.com/grpc/grpc)** — Remote Procedure Calls (RPCs) provide a useful abstraction for building distributed applications and services. The libraries in this repository provide a concrete implementation of the gRPC… — appears in 3 lists · `rpc` `http2` `distributed-systems` `protobuf`

---

## 👍 Worth trying — buenas en su nicho
Menos hype que las GEMs, pero sólidas si caés en su caso de uso.

### AI Memory Layer
- **[Mem0](https://github.com/mem0ai/mem0)** — - Mem0 enhances AI assistants and agents with an intelligent memory layer, enabling personalized AI interactions. — appears in 3 lists · `ai-memory` `python` `agents` `llm`

### AI Skills Kit
- **[Superpowers](https://github.com/obra/superpowers)** — by [Jesse Vincent](https://github.com/obra) - A strong bundle of core competencies for software engineering, with good coverage of a large portion of the SDLC - from planning, reviewing, testing,… · `prompt-engineering` `sdlc` `best-practices` `claude`

### Applications
- **[Sniffnet](https://github.com/gyulyvgc/sniffnet)** — Cross-platform application to monitor your network traffic with ease [](https://github.com/GyulyVGC/sniffnet/blob/main/.github/workflows/rust.yml) [](https://crates.io/crates/sniffnet) — appears in 4 lists · `rust` `networking` `open-source` `packet-sniffer`

### Browser Extension
- **[OctoLinker](https://github.com/octolinker/octolinker)** — ice_cube: - A browser extension for GitHub that makes the image name in a `Dockerfile` clickable and redirect you to the related Docker Hub page. · `browser-extension` `docker` `github` `productivity`

### Browsers
- **[Vivaldi](https://vivaldi.com)** — The browser that puts you in control. ![Freeware][Freeware Icon] — appears in 3 lists · `browser` `chromium` `customization`

### C#
- **[Cake](https://github.com/cake-build/cake)** — _(label: Good-first-issue)_ <br> Cake (C# Make) is a free and open source cross-platform build automation system with a C# DSL for tasks such as compiling code, copying files and folders, running… — appears in 3 lists · `csharp` `build-automation` `dsl` `ci-cd`

### C++
- **[Polyaxon](https://github.com/polyaxon/polyaxon)** — - A platform for reproducible and scalable machine learning and deep learning on kubernetes - [(Video)](https://www.youtube.com/watch?v=Iexwrka_hys). — appears in 3 lists · `kubernetes` `ml-ops` `reproducibility` `python`

### C++ ML Toolkit
- **[JAX](https://github.com/google/jax)** — JAX is Autograd and XLA, brought together for high-performance machine learning research. · `cpp` `machine-learning` `computer-vision` `lightweight`

### CI/CD Service
- **[CircleCI](https://circleci.com)** — :yen: Push or pull Docker images from your build environment, or build and run containers right on CircleCI. · `ci-cd` `saas` `docker` `cloud`
- **[Semaphore CI](https://semaphore.io)** — yen: — A high-performance cloud solution that makes it easy to build, test and ship your containers to production. · `ci-cd` `saas` `docker` `cloud`

### CLI Tools
- **[yt-dlp](https://github.com/yt-dlp/yt-dlp)** — Downloads videos from almost any online platform, along with information, thumbnails, subtitles, descriptions, and comments (comments only on a select few sites like Youtube and a few small… — appears in 3 lists · `cli` `video-download` `python` `metadata-extraction`

### Classical ML Library
- **[SHOGUN](https://github.com/shogun-toolbox/shogun)** — The Shogun Machine Learning Toolbox. [GPLv3] · `machine-learning` `cpp` `scikit-learn-alternative`

### Claude Tips
- **[Claude Code Tips](https://github.com/ykdojo/claude-code-tips)** — by [ykdojo](https://github.com/ykdojo) - A nice variety of 35+ brief but information-dense Claude Code tips covering voice input, system prompt patching, container workflows for risky tasks,… · `claude-code` `tips-tricks` `workflow` `voice`

### Container CLI
- **[lazydocker](https://github.com/jesseduffield/lazydocker)** — The lazier way to manage everything docker. A simple terminal UI for both docker and docker-compose, written in Go with the gocui library. By [jesseduffield](https://github.com/jesseduffield). · `cli` `go` `docker` `tui`

### Continuous Integration
- **[Bencher](https://bencher.dev)** — Suite of continuous benchmarking tools designed to catch performance regressions in CI. — appears in 4 lists · `benchmarking` `ci-cd` `rust`

### Data Visualization
- **[gradio](https://github.com/gradio-app/gradio)** — - Quickly create and share demos of models - by only writing Python. Debug models interactively in your browser, get feedback from collaborators, and generate public links without deploying anything. — appears in 3 lists · `python` `web-ui` `demos` `visualization`
- **[vizzu](https://github.com/vizzuhq/vizzu-lib)** — Library for animated data visualizations and data stories. · `dataviz` `animation` `javascript`

### Desktop Framework
- **[tauri-apps/tauri](https://github.com/tauri-apps/tauri)** — Build smaller, faster, and more secure desktop applications with a web frontend, powered by [WRY](https://github.com/tauri-apps/wry).… · `rust` `desktop` `web-frontend` `cross-platform`

### Developer Tools
- **[Rider](https://jetbrains.com/rider)** — A cross-platform C# IDE based on the IntelliJ platform and ReSharper — appears in 3 lists · `csharp` `ide` `dotnet` `jetbrains`

### Developer Utilities
- **[intelli-shell](https://github.com/lasantosr/intelli-shell)** — Bookmark commands with placeholders and search or autocomplete at any time [](https://crates.io/crates/intelli-shell) [](https://github.com/lasantosr/intelli-shell/actions/workflows/release.yml) — appears in 3 lists · `rust` `cli` `productivity` `shell`

### Distributed Systems
- **[Dragonfly](https://github.com/dragonflyoss/dragonfly2)** — Provide efficient, stable and secure file distribution and image acceleration based on p2p technology to be the best practice and standard solution in cloud native architectures. — appears in 3 lists · `p2p` `oci-images` `container-registry` `distributed-systems`

### Doc Browser
- **[Dash](https://kapeli.com/dash)** — Offline API documentation browser for macOS with instant search access to Vue.js docs and 200+ other frameworks. · `macos` `documentation` `offline` `developer-tools`

### Docker Management
- **[dockly](https://github.com/lirantal/dockly)** — An interactive shell UI for managing Docker containers. · `docker` `cli` `tui` `containers`

### Editor Plugins
- **[Cline](https://marketplace.visualstudio.com/items)** — Autonomous coding agent for VS Code that can create/edit files, execute commands, and use the browser with user permission. Supports multiple AI providers including OpenRouter, Anthropic, OpenAI,… — 🔥 appears in **7** lists · `vscode-extension` `ai-agent` `autonomous-coding` `multi-provider`

### Enterprise Search
- **[Apache Solr](https://lucene.apache.org/solr)** — Enterprise search platform featuring full-text search, hit highlighting, faceted search, real-time indexing, dynamic clustering, and rich document (e.g., Word, PDF) handling. · `search` `java` `lucene` `docker`

### GPU ML Frameworks
- **[CuML](https://github.com/rapidsai/cuml)** — - cuML is a suite of libraries that implement machine learning algorithms and mathematical primitives functions that share compatible APIs with other RAPIDS projects. · `gpu` `cuda` `machine-learning` `python`

### Go Tools
- **[OctoLinker](https://github.com/octolinker/browser-extension)** — Navigate through `projects.json` files efficiently with the OctoLinker browser extension for GitHub. — appears in 3 lists · `github` `browser-extension` `typescript` `navigation`

### Graph Visualization
- **[Gephi](https://gephi.org)** — is an open-source graph and network visualization software. · `graph-visualization` `network-analysis` `java` `desktop-app`

### Image Processing
- **[Scikit-Image](https://github.com/scikit-image/scikit-image)** — A collection of algorithms for image processing in Python. — appears in 3 lists · `python` `image-processing` `computer-vision` `scipy`

### JavaScript
- **[Gatsby.js](https://github.com/gatsbyjs/gatsby)** — _(label: good first issue)_ <br> Build blazing fast, modern apps and websites with React. — appears in 4 lists · `react` `static-site-generator` `graphql`
- **[Ghost](https://github.com/tryghost/ghost)** — _(label: good first issue)_ <br> Just a blogging platform — appears in 3 lists · `javascript` `node.js` `cms` `self-hosted`
- **[Vest](https://github.com/ealush/vest)** — _(label: good first issue)_ <br> Validations framework inspired by unit testing frameworks. — appears in 3 lists · `javascript` `validation` `forms` `typescript`
- **[webdriver.io](https://github.com/webdriverio/webdriverio)** — _(label: first-timers-only)_ <br> Next-gen browser and mobile automation test framework for Node.js — appears in 3 lists · `javascript` `e2e-testing` `webdriver` `automation`

### Learning Resource
- **[CTFs](https://github.com/apsdehal/awesome-ctf)** — Capture The Flag frameworks, libraries, etc. — appears in 3 lists · `ctf` `security` `awesome-list`

### Low Code ML
- **[Ludwig](https://github.com/ludwig-ai/ludwig)** — - Ludwig is a low-code framework for building custom AI models like LLMs and other deep neural networks. · `low-code` `llm` `deep-learning` `python`

### ML Research Library
- **[Flashlight](https://github.com/flashlight/flashlight)** — - A fast, flexible machine learning library written entirely in C++ from the Facebook AI Research and the creators of Torch, TensorFlow, Eigen and Deep Speech. · `machine-learning` `cpp` `facebook-ai` `research`

### Machine Learning
- **[CatBoost](https://github.com/catboost/catboost)** — General purpose gradient boosting on decision trees library with categorical features support out of the box. It is easy to install, contains fast inference implementation and supports CPU and GPU… — appears in 4 lists · `gradient-boosting` `machine-learning` `categorical-features` `gpu`
- **[Feature Engine](https://github.com/feature-engine/feature_engine)** — - Feature-engine is a Python library that contains several transformers to engineer features for use in machine learning models. — appears in 3 lists · `spark` `streaming` `scala` `java`
- **[H2O-3](https://github.com/h2oai/h2o-3)** — - Fast scalable Machine Learning platform for smarter applications: Deep Learning, Gradient Boosting & XGBoost, Random Forest, Generalized Linear Modeling (Logistic Regression, Elastic Net),… — appears in 3 lists · `machine-learning` `automl` `java` `distributed`

### Mapping Library
- **[OpenLayers3](https://openlayers.org)** — A high-performance, feature-packed library for all your mapping needs. · `maps` `gis` `javascript` `geospatial`

### Misc
- **[awesome](https://github.com/sindresorhus/awesome)** — zap: - A curated list of awesome lists. — appears in 4 lists · `curated-list` `discovery` `meta-index`

### Monitoring System
- **[HertzBeat](https://github.com/dromara/hertzbeat)** — An open-source real-time monitoring system with custom-monitor and agentless. · `monitoring` `observability` `agentless` `open-source`

### Online IDE
- **[OneCompiler](https://onecompiler.com)** — A free AI Powered online compiler supporting over 70 languages, including Java, Python, MySQL, C++, and HTML, for writing, running, and sharing code. · `online-ide` `web-compiler` `multi-language` `prototyping`

### Package Management
- **[RepoFlow](https://repoflow.io)** — A simple and easy-to-use package management platform with Docker support alongside other formats like PyPI, Maven, npm, and Helm. Includes smart search, built-in Docker image scanning, and a great… · `package-registry` `docker` `self-hosted` `saas`

### Performance Testing
- **[bencher](https://github.com/bencherdev/bencher)** — A suite of continuous benchmarking tools designed to catch performance regressions in CI. — appears in 3 lists · `benchmarking` `ci-cd` `performance` `monitoring`

### Prompt Optimization
- **[Context Engineering Kit](https://github.com/neolabhq/context-engineering-kit)** — by [Vlad Goncharov](https://github.com/LeoVS09) - Hand-crafted collection of advanced context engineering techniques and patterns with minimal token footprint focused on improving agent result… · `prompt-engineering` `token-optimization` `context` `agents`

### PyTorch Training
- **[Ignite](https://github.com/pytorch/ignite)** — - Ignite is a high-level library to help with training and evaluating neural networks in PyTorch flexibly and transparently. · `pytorch` `deep-learning` `training-loops` `python`

### Python
- **[Bokeh](https://github.com/bokeh/bokeh)** — - Bokeh is an interactive visualization library for Python that enables beautiful and meaningful visual presentation of data in modern web browsers. — appears in 4 lists · `python` `data-visualization` `interactive-charts` `open-source`
- **[Colossal-AI](https://github.com/hpcaitech/colossalai)** — - A unified deep learning system for big model era, which helps users to efficiently and quickly deploy large AI model training and inference. — appears in 3 lists · `python` `llm` `distributed-training` `gpu`
- **[Deepchecks](https://github.com/deepchecks/deepchecks)** — - Deepchecks is a holistic open-source solution for all of your AI & ML validation needs, enabling you to test your data and models from research to production thoroughly. — appears in 3 lists · `python` `ml-validation` `testing` `data-quality`
- **[PyMC](https://github.com/pymc-devs/pymc)** — _(label: beginner friendly)_ <br> A Python library for Bayesian statistical modeling and probabilistic machine learning. Beginner-friendly with 'good first issue' labels. — appears in 3 lists · `bayesian` `probabilistic-ml` `statistics` `open-source`

### Resources
- **[Docker for novices](https://youtube.com/watch)** — An introduction to Docker for developers and testers who have never used it. (Video 1h40, recorded linux.conf.au 2019 — Christchurch, New Zealand) by Alex Clews. — 🔥 appears in **16** lists · `docker` `containers` `beginners` `video`

### Reverse Proxy
- **[Pomerium](https://pomerium.io)** — Identity-aware reverse proxy, successor to now obsolete oauth_proxy. It inserts an OAuth step before proxying your request to the backend, so that you can safely expose your self-hosted websites… · `reverse-proxy` `oauth` `identity` `go`

### Rust
- **[Readest](https://github.com/readest/readest)** — _(label: good first issue)_ <br> A modern, feature-rich ebook reader designed for avid readers offering seamless cross-platform access, powerful tools, and an intuitive interface. — appears in 3 lists · `rust` `desktop-app` `ebook-reader` `cross-platform`

### Rust ML Kit
- **[linfa](https://github.com/rust-ml/linfa)** — a comprehensive toolkit to build Machine Learning applications with Rust · `rust` `machine-learning` `supervised` `unsupervised`

### Security
- **[themis](https://github.com/cossacklabs/themis)** — High level crypto library for storing data (AES), secure messaging (ECC + ECDSA / RSA + PSS + PKCS#7) and session-oriented, forward secrecy data exchange (ECDH key agreement, ECC & AES… — 🔥 appears in **7** lists · `cryptography` `security` `multi-platform` `open-source`
- **[mariocandela/beelzebub](https://github.com/mariocandela/beelzebub)** — ☁️ - Beelzebub is a honeypot framework that lets you build honeypot tools using MCP. Its purpose is to detect prompt injection or malicious agent behavior. The underlying idea is to provide the… · `honeypot` `security` `ai-safety` `prompt-injection`

### Security Defense
- **[Honeypots](https://github.com/paralax/awesome-honeypots)** — Deception trap, designed to entice an attacker into attempting to compromise the information systems in an organization. — appears in 3 lists · `security` `honeypots` `threat-detection` `curated-list`

### Server Implementations
- **[juspay/neurolink](https://github.com/juspay/neurolink)** — 📇 ☁️ 🏠 🍎 🪟 🐧 - Making enterprise AI infrastructure universally accessible. Edge-first platform unifying 12 providers and 100+ models with multi-agent orchestration, HITL workflows, guardrails… — appears in 3 lists · `edge-computing` `multi-agent` `enterprise` `orchestration`
- **[pydantic-ai](https://github.com/pydantic/pydantic-ai)** — A Python agent framework for building generative AI applications with structured schemas. · `python` `ai-agents` `llm` `pydantic`
- **[txn2/kubefwd](https://github.com/txn2/kubefwd)** — 🏎️ 🏠 - Kubernetes bulk port forwarding with service discovery, /etc/hosts management, traffic monitoring, and pod log streaming · `kubernetes` `port-forwarding` `cli` `go`

### Software Packages
- **[lstags](https://github.com/ivanilves/lstags)** — Tool and API to sync Docker images across different registries. — appears in 3 lists · `docker` `registry` `devops` `golang`

### Swift
- **[Awesome Core ML Models](https://github.com/likedan/awesome-coreml-models)** — A curated list of machine learning models in CoreML format. — appears in 3 lists · `swift` `coreml` `ios` `curated-list`

### System Monitoring
- **[glances](https://nicolargo.github.io/glances)** — Open-source, cross-platform real-time monitoring tool with CLI and web dashboard interfaces and many exporting options. · `monitoring` `cli` `python` `cross-platform`

### Terminal Apps
- **[Wave](https://github.com/wavetermdev/waveterm)** — Open-source terminal with built-in file previews, web browsing, and AI tools. [![Open-Source Software][OSS Icon]](https://github.com/wavetermdev/waveterm) ![Freeware][Freeware Icon] — appears in 3 lists · `terminal` `rust` `ai-integration` `open-source`

### Test Framework
- **[Mocha](https://github.com/mochajs/mocha)** — _(label: good first issue)_ <br> Javascript test framework for Node.js and the browser. — appears in 3 lists · `javascript` `testing` `nodejs` `browser`

### Text Editor
- **[GNU Emacs](https://gnu.org/software/emacs)** — An extensible, customizable text editor-and more. `GPL-3.0` `C` · `editor` `lisp` `cli` `text-editor`

### TypeScript
- **[Amplication](https://github.com/amplication/amplication)** — _(label: good first issue)_ <br> Amplication is an open-source development tool. It helps you develop quality Node.js applications without spending time on repetitive coding tasks. — appears in 3 lists · `code-generation` `nodejs` `backend` `low-code`
- **[Vitest](https://github.com/vitest-dev/vitest)** — _(label: good first issue)_ <br> A blazing fast unit test framework powered by Vite. — appears in 3 lists · `typescript` `testing` `vite` `jest-alternative`

### Videos
- **[Functional Programming with TypeScript](https://youtube.com/playlist)** — Discover functional programming with Typescript and create a library like fp-ts alongside Sahand Javid in this beginner-friendly YouTube playlist. — 🔥 appears in **11** lists · `typescript` `functional-programming` `fp-ts` `video-tutorial`

---

## 🤖 Por qué confiar en esta lista

- **Transparente**: todos los scores y metodología están en público en [juanchi.dev/awesome/sources](https://juanchi.dev/awesome/sources) (próximamente)
- **Auto-regulada**: si un awesome-* deja de mantenerse, cae al BENCH y eventualmente sale del roster
- **Human-in-the-loop**: no es IA sola. Tools con ⭐ GEM pasan primero por Claude, después por veredicto humano de [Juan Torchia](https://juanchi.dev)
- **Reproducible**: este README se regenera semanalmente. El código del sistema está documentado en [juanchi.dev/blog/series/awesome-curated](https://juanchi.dev/blog/series/awesome-curated)

## 🤝 Contribuir

- 🐛 ¿Tool mal clasificada? → [abrí un issue](https://github.com/JuanTorchia/awesome-curated/issues/new)
- ➕ ¿Falta una tool importante? → issue con el link + justificación
- 📝 ¿Querés agregar una fuente? → proponé un repo `awesome-*` que no estemos scrapeando

## 📬 Newsletter

Si querés recibir el digest mensual con las tools nuevas que entran al roster →
[juanchi.dev/newsletter](https://juanchi.dev)

---

<sub>📄 Generado automáticamente desde [juanchi.dev](https://juanchi.dev) · [código fuente del sistema](https://juanchi.dev/blog/series/awesome-curated) · MIT licensed</sub>
