# 🧰 Ferramentas Dev — Awesome Curated

<p><sub>← [Voltar ao main](../README.pt-BR.md)</sub></p>

**52 GEMs · 96 Vale a pena testar**

---

## ⭐ GEMs — padrões da indústria

Ferramentas que a comunidade considera default. Se você não conhece, vale explorar.

### [Pytorch](https://github.com/pytorch/pytorch)

![](https://img.shields.io/github/stars/pytorch/pytorch?style=flat-square&label=⭐) · 🔥 **aparece em 6 listas**

_(label: good first issue)_ <br> PyTorch is an open source machine learning library based on the Torch library, used for applications such as computer vision and natural language processing.

> **Análise IA:** No hay mucho que analizar acá: PyTorch es el estándar de facto para investigación en deep learning y cada vez más para producción. Si trabajás con ML/AI en Python, lo vas a usar o ya lo usás. No es hype, es infraestructura. El ecosistema es masivo, la documentación es sólida y tiene el respaldo de Meta. ¿Para quién? Desde estudiantes aprendiendo redes neuronales hasta equipos construyendo LLMs. La curva existe, pero es la más razonable del área.

**Pontos fortes:** _API pythónica e imperativa (define-by-run) que facilita debugging y experimentación frente a enfoques de grafo estático_ · _Ecosistema gigante: torchvision, torchaudio, HuggingFace, Lightning y miles de papers con implementaciones oficiales en PyTorch_ · _Soporte nativo de GPU vía CUDA con autograd automático, reduciendo la complejidad de implementar backpropagation custom_

**Tags:** `deep-learning` `machine-learning` `python` `gpu` `open-source`

---

### [TensorFlow](https://github.com/tensorflow/tensorflow)

![](https://img.shields.io/github/stars/tensorflow/tensorflow?style=flat-square&label=⭐) · 🔥 **aparece em 6 listas**

- TensorFlow is a leading library designed for developing and deploying state-of-the-art machine learning applications.

> **Análise IA:** TensorFlow es el framework de ML más battle-tested de la industria, respaldado por Google y con años de producción real. No es hype: es infraestructura seria para modelos a escala. El dev promedio hoy en día probablemente prefiere PyTorch por ergonomía, pero TF sigue siendo la opción cuando necesitás deployment en móvil (TFLite), edge, o integración con ecosistema Google Cloud. Si estás aprendiendo ML desde cero, PyTorch te va a hacer menos daño de cabeza. Si tenés un sistema productivo que lo usa, no hay razón para migrar.

**Pontos fortes:** _Ecosistema maduro con TFLite para deployment en dispositivos móviles y edge computing_ · _TensorFlow Serving y soporte nativo para producción a gran escala con Google Cloud_ · _Graph execution permite optimizaciones de rendimiento que eager mode no siempre logra_

**Tags:** `machine-learning` `deep-learning` `python` `c++` `open-source`

---

### [Docker](https://docker.com)

aparece em 4 listas

Powerful, performs operating-system-level virtualization. [![Open-Source Software][OSS Icon]](https://github.com/docker) ![Freeware][Freeware Icon] [![Awesome List][awesome-list Icon]](https://github.com/veggiemonk/awesome-docker#readme)

> **Análise IA:** Containerización OS-level con ecosis maduro. Resuelve deployment y reproducibilidad en equipos; costo en curva de aprendizaje y overhead de recursos.

**Pontos fortes:** _Reproducibilidad garantizada entre ambientes_ · _Orquestación nativa con Docker Compose y Swarm_

**Tags:** `containers` `devops` `virtualization`

---

### [Node.js](https://github.com/sindresorhus/awesome-nodejs)

![](https://img.shields.io/github/stars/sindresorhus/awesome-nodejs?style=flat-square&label=⭐) · aparece em 4 listas

Async non-blocking event-driven JavaScript runtime built on Chrome's V8 JavaScript engine.

> **Análise IA:** Info insuficiente: la desc es generic sobre Node.js runtime, pero id/URL apuntan a awesome-nodejs (curated list). Clarificar si es sobre Node o el índice.

**Pontos fortes:** _Event loop no-bloqueante nativo_ · _npm ecosystem con millones de packages_

**Tags:** `nodejs` `javascript` `runtime`

---

### [Obsidian](https://obsidian.md)

aparece em 4 listas

Obsidian is a powerful knowledge base on top of a local folder of plain text Markdown files.

> **Análise IA:** PKM basado en Markdown local. Para investigadores, escritores, developers que necesitan conectar ideas sin vendor lock-in. Resuelve el problema de organización flexible sin cloud obligatorio.

**Pontos fortes:** _Graph de notas sin fricción, completamente local_ · _Plugin ecosystem robusto para extender funcionalidad_

**Tags:** `markdown` `local-first` `knowledge-base` `self-hosted`

---

### [Playwright](https://github.com/microsoft/playwright)

![](https://img.shields.io/github/stars/microsoft/playwright?style=flat-square&label=⭐) · aparece em 4 listas

Node.js library to automate Chromium, Firefox and WebKit with a single API.

> **Análise IA:** Playwright es la herramienta de testing E2E más sólida del ecosistema web hoy. Microsoft la mantiene activamente y superó a Cypress en varios aspectos clave: soporte multi-browser real (no solo Chromium), ejecución en paralelo nativa, y una API más potente para casos complejos. Si hacés testing de frontends modernos, esto es oro. No es hype: resuelve problemas reales que Selenium hacía sufrir. El dev que ya usa Cypress debería evaluarla seriamente antes de seguir invirtiendo ahí.

**Pontos fortes:** _Soporte nativo para Chromium, Firefox y WebKit con una sola API coherente, sin parches ni wrappers_ · _Ejecución de tests en paralelo out-of-the-box con aislamiento por contexto de browser, sin configuración compleja_ · _Auto-wait integrado que elimina la mayoría de los flaky tests por timing sin agregar sleeps manuales_

**Tags:** `testing` `e2e` `automation` `browser` `node`

---

### [Visual Studio Code](https://code.visualstudio.com)

aparece em 4 listas

Microsoft's free & open-source editor, TypeScript friendly, [VSCode Plugins](editor-plugin.md#vscode-plugin). [![Open-Source Software][OSS Icon]](https://github.com/Microsoft/vscode) ![Freeware][Freeware Icon] [![Awesome List][awesome-list Icon]](https://github.com/viatsko/awesome-vscode#readme)

> **Análise IA:** Editor gratuito open-source con soporte TypeScript nativo y ecosistema masivo de plugins. Standard de facto para desarrollo moderno, resuelve el 80% de casos sin fricción.

**Pontos fortes:** _Debugging integrado robusto_ · _Marketplace de extensiones maduro con miles de plugins probados_

**Tags:** `editor` `typescript` `vscode-plugins`

---

### [Bitwarden](https://bitwarden.com)

aparece em 3 listas

Open source password management tool for Mac OS, iOS and browsers. [![Open-Source Software][OSS Icon]](https://github.com/bitwarden) ![Freeware][Freeware Icon]

> **Análise IA:** Password manager open-source, self-hosteable o cloud. Resuelve problema real: almacenar credenciales sin depender de propietario. Soporte multiplataforma (desktop, mobile, browser).

**Pontos fortes:** _Código abierto auditado, E2E encryption_ · _Self-hosting option + cloud oficial_

**Tags:** `password-manager` `security` `open-source` `self-hosted`

---

### [DVC](https://github.com/iterative/dvc)

![](https://img.shields.io/github/stars/iterative/dvc?style=flat-square&label=⭐) · aparece em 3 listas

Data Science Version Control is an open-source version control system for machine learning projects with pipelines support. It makes ML projects reproducible and shareable.

> **Análise IA:** Control de versiones para pipelines ML con reproducibilidad garantizada. Resuelve problema real: trackear datos+code+modelos juntos. Pero setup inicial tedioso.

**Pontos fortes:** _Versionado de datasets y modelos sin duplicar en git_ · _Pipelines reproducibles con dag tracking_

**Tags:** `data-science` `version-control` `ml-pipelines`

---

### [Jupyter Notebooks](https://github.com/jupyter/notebook)

![](https://img.shields.io/github/stars/jupyter/notebook?style=flat-square&label=⭐) · aparece em 3 listas

- Web interface python sandbox environments for reproducible development

> **Análise IA:** Entorno web interactivo para Python que mezcla código, visualización y documentación. Estándar para data science y research reproducible. Resuelve bien el problema de experimentación exploratoria, menos para producción.

**Pontos fortes:** _Excelente para documentación viva y sharing de análisis_ · _Integración nativa con librerías científicas (numpy, pandas, matplotlib)_

**Tags:** `python` `jupyter` `notebook` `interactive` `data-science`

---

### [Kubernetes](https://github.com/kubernetes/kubernetes)

![](https://img.shields.io/github/stars/kubernetes/kubernetes?style=flat-square&label=⭐) · aparece em 3 listas

_(label: good first issue)_ <br> Production-Grade Container Scheduling and Management System

> **Análise IA:** Orquestador de contenedores nivel producción: scheduling, networking, storage en clusters. Para infraestructura en serio. Resuelve el problema masivo de ejecutar aplicaciones distribuidas sin entrar en detalles manuales.

**Pontos fortes:** _Standard de facto: madurez y ecosystem inmensamente mayor a alternativas_ · _Abstracción poderosa: declarativa, multi-cloud, self-healing integrado_

**Tags:** `kubernetes` `container-orchestration` `go` `distributed-systems` `infrastructure`

---

### [LightGBM](https://github.com/microsoft/lightgbm)

![](https://img.shields.io/github/stars/microsoft/lightgbm?style=flat-square&label=⭐) · aparece em 3 listas

Microsoft's fast, distributed, high performance gradient boosting (GBDT, GBRT, GBM or MART) framework based on decision tree algorithms, used for ranking, classification and many other machine learning tasks.

> **Análise IA:** Framework de gradient boosting distribuido y veloz de Microsoft. Para data scientists que necesitan modelos predictivos rápidos en ranking, clasificación y regresión. Resuelve el problema real de entrenar GBDT sin esperar horas.

**Pontos fortes:** _Velocidad de entrenamiento significativamente superior a XGBoost en datasets grandes_ · _Manejo eficiente de features categóricas sin necesidad de one-hot encoding previo_

**Tags:** `machine-learning` `gradient-boosting` `distributed` `python` `gpu`

---

### [mitmproxy](https://mitmproxy.org)

aparece em 3 listas

A Python tool used for intercepting, viewing and modifying network traffic. Invaluable in troubleshooting certain problems.

> **Análise IA:** Proxy MITM escrito en Python para interceptar y modificar tráfico HTTP/HTTPS. Imprescindible para debugging de APIs, testing de seguridad y análisis de aplicaciones cliente-servidor. Resuelve real: ver qué hace una app cuando habla con el servidor.

**Pontos fortes:** _Interfaz web moderna y CLI potente_ · _Scripting en Python para automatizar modificaciones de requests/responses_

**Tags:** `python` `proxy` `debugging` `security` `networking`

---

### [Moby](https://github.com/moby/moby)

![](https://img.shields.io/github/stars/moby/moby?style=flat-square&label=⭐) · aparece em 3 listas

Collaborative project for the container ecosystem to assemble container-based systems.

> **Análise IA:** Proyecto open-source para ecosistema de contenedores (base de Docker). Core de containerización. Para devops/infra que necesitan abstracción de contenedores a nivel producción.

**Pontos fortes:** _Standard de facto en containerización moderna_ · _Comunidad masiva y mantenimiento activo de Docker Inc_

**Tags:** `go` `containers` `docker` `open-source` `infrastructure`

---

### [PyG](https://github.com/pyg-team/pytorch_geometric)

![](https://img.shields.io/github/stars/pyg-team/pytorch_geometric?style=flat-square&label=⭐) · aparece em 3 listas

- PyG (PyTorch Geometric) is a library built upon PyTorch to easily write and train Graph Neural Networks (GNNs) for a wide range of applications related to structured data.

> **Análise IA:** Biblioteca PyTorch para GNNs: abstracción sobre grafos con ops optimizadas. Para ML engineers que laburen con datos estructurados no-euclidianos. Problema real: training de GNNs sin reinventar la rueda.

**Pontos fortes:** _Abstracciones de alto nivel para message passing_ · _Buncha datasets y benchmarks precocinados_

**Tags:** `gnn` `pytorch` `python` `ml` `graphs`

---

### [scikit-learn](https://github.com/scikit-learn/scikit-learn)

![](https://img.shields.io/github/stars/scikit-learn/scikit-learn?style=flat-square&label=⭐) · aparece em 3 listas

- Scikit-learn is a powerful machine learning library that provides a wide variety of modules for data access, data preparation and statistical model building.

> **Análise IA:** Librería ML clásica con algoritmos supervisados/no supervisados bien documentados. Para quien necesita baseline rápido en tabular data. Maduro, predecible, sin sorpresas.

**Pontos fortes:** _API consistente y previsible entre estimadores_ · _Documentación y comunidad excepcionales_

**Tags:** `python` `machine-learning` `sklearn` `supervised` `unsupervised`

---

### [SymPy](https://github.com/sympy/sympy)

![](https://img.shields.io/github/stars/sympy/sympy?style=flat-square&label=⭐) · aparece em 3 listas

_(label: Easy-to-Fix)_ <br> A Python library for symbolic mathematics.

> **Análise IA:** SymPy es una librería de matemática simbólica en Python puro, sin dependencias externas pesadas. Resuelve un problema muy real: hacer álgebra, cálculo, ecuaciones diferenciales y geometría de forma simbólica (no numérica) desde Python. Para científicos, ingenieros o devs que trabajan con modelos matemáticos es oro puro. No es hype, lleva décadas activa y es usada en producción. No es para el dev web promedio, pero si necesás manipular expresiones matemáticas formales, no hay mejor opción en el ecosistema Python.

**Pontos fortes:** _Matemática simbólica completa sin depender de software externo como Mathematica o Maple_ · _Integración nativa con el ecosistema científico Python (NumPy, SciPy, Jupyter)_ · _Capacidad de simplificar, derivar, integrar y resolver ecuaciones de forma exacta, no aproximada_

**Tags:** `python` `mathematics` `symbolic-computation` `open-source` `scientific-computing`

---

### [Transformers](https://github.com/huggingface/transformers)

![](https://img.shields.io/github/stars/huggingface/transformers?style=flat-square&label=⭐) · aparece em 3 listas

- Huggingface's library of state-of-the-art pretrained models for Natural Language Processing (NLP).

> **Análise IA:** Librería PyTorch/TensorFlow que domina NLP. Estado del arte en transformer models, fine-tuning y deployment. Estándar de facto para cualquier proyecto serio en lenguaje natural.

**Pontos fortes:** _Modelos preentrenados para 100+ tareas_ · _Documentación y comunidad sólida_

**Tags:** `python` `nlp` `transformers` `pytorch` `tensorflow`

---

### [Wireshark](https://wireshark.org)

aparece em 3 listas

The world’s foremost and widely-used network protocol analyzer. [![Open-Source Software][OSS Icon]](https://github.com/wireshark/wireshark) ![Freeware][Freeware Icon]

> **Análise IA:** Network protocol analyzer: captures, disecciona, filtra tráfico en tiempo real. Para SREs/security teams debugueando conectividad. Resuelve: visibilidad low-level de packets.

**Pontos fortes:** _Parser de protocols exhaustivo (2000+)_ · _Filters potentes, hstore de pcaps_

**Tags:** `network` `pcap` `wireshark` `cli-gui` `security`

---

### [ajeetdsouza/zoxide](https://github.com/ajeetdsouza/zoxide)

![](https://img.shields.io/github/stars/ajeetdsouza/zoxide?style=flat-square&label=⭐) · aparece em 2 listas

A fast alternative to `cd` that learns your habits [](https://github.com/ajeetdsouza/zoxide/actions)

> **Análise IA:** Reemplazo moderno de `cd` que aprende patrones de navegación. Escrito en Rust, más rápido y útil que `z`. Resuelve fricción real en la terminal.

**Pontos fortes:** _Significativamente más rápido que alternativas tipo `z`_ · _Aprende automáticamente frecuencia y recencia de directorios_

**Tags:** `rust` `cli` `shell` `productivity` `self-hosted`

---

### [Apache Maven](https://maven.apache.org)

aparece em 2 listas

Build automation tool mainly for Java. A software project management and comprehension tool. Based on the concept of a project object model (POM), Maven can manage a project's build, reporting and documentation from a central piece of information.

> **Análise IA:** Build automation estándar para Java desde 2002. Project Object Model (POM) centraliza configuración. Imprescindible en ecosistema Java enterprise.

**Pontos fortes:** _Estándar de facto en Java, integración IDE perfecta_ · _Dependency management centralizado y reproducible_

**Tags:** `java` `build-automation` `dependency-management` `xml`

---

### [astral-sh/ruff](https://github.com/astral-sh/ruff)

![](https://img.shields.io/github/stars/astral-sh/ruff?style=flat-square&label=⭐) · aparece em 2 listas

An extremely fast Python linter and code formatter [](https://github.com/astral-sh/ruff/actions)

> **Análise IA:** Linter + formateador Python ultra-rápido (Rust). Reemplaza flake8 + black + isort. Estándar emergente, compatibilidad casi total con black.

**Pontos fortes:** _Velocidad 10-100x respecto a flake8/black_ · _Drop-in replacement con casi cero config_

**Tags:** `linter` `formatter` `rust` `python` `cli`

---

### [Calibre](https://calibre-ebook.com)

aparece em 2 listas

E-book library manager that can view, convert, and catalog e-books in most of the major e-book formats and provides a built-in Web server for remote clients. )

> **Análise IA:** Gestor ebooks robusto: conversión formatos (EPUB, MOBI, PDF), catalogación, servidor web integrado. Python+PyQt. Estándar para colecciones e-books, muy pulido.

**Pontos fortes:** _Conversión EPUB↔MOBI↔PDF sólida, servidor web para acceso remoto_ · _Metadatos automáticos, busca potente_

**Tags:** `ebook` `conversion` `python` `pyqt` `catalog`

---

### [cookiecutter](https://github.com/cookiecutter/cookiecutter)

![](https://img.shields.io/github/stars/cookiecutter/cookiecutter?style=flat-square&label=⭐) · aparece em 2 listas

_(label: good first issue)_ <br> A command-line utility that creates projects from cookiecutters (project templates). E.g. Python package projects, jQuery plugin projects.

> **Análise IA:** CLI para generar proyectos desde templates. Estándar en Python para scaffolding. Resuelve problema real de boilerplate, muy usado en comunidad.

**Pontos fortes:** _Estándar de facto en Python para templates_ · _Extremadamente simple y flexible_

**Tags:** `cli` `scaffolding` `templating` `python`

---

### [cypress](https://github.com/cypress-io/cypress)

![](https://img.shields.io/github/stars/cypress-io/cypress?style=flat-square&label=⭐) · aparece em 2 listas

_(label: good first issue)_ <br> Fast, easy and reliable testing for anything that runs in a browser.

> **Análise IA:** Framework de testing end-to-end para navegadores moderno. Mejor UX que Selenium, dominante en testing de SPA/web apps.

**Pontos fortes:** _Experiencia de desarrollo superior a Selenium_ · _Excellent debugging tools y error messages_

**Tags:** `javascript` `testing` `e2e` `browser-automation`

---

### [dust](https://github.com/bootandy/dust)

![](https://img.shields.io/github/stars/bootandy/dust?style=flat-square&label=⭐) · aparece em 2 listas

A more intuitive version of `du` in Rust.

> **Análise IA:** Reimplementación de `du` en Rust. Más intuitivo, agrupa por tamaño descendente. Reemplazo directo para auditorías de espacio disco.

**Pontos fortes:** _Output ordenado por tamaño por defecto, ahorra pipe a `sort`_ · _10-100x más rápido que `du` en directorios masivos_

**Tags:** `rust` `cli` `disk-analysis` `unix-tool`

---

### [fzf](https://github.com/junegunn/fzf)

![](https://img.shields.io/github/stars/junegunn/fzf?style=flat-square&label=⭐) · aparece em 2 listas

A general purpose command-line fuzzy finder, can be used with any list: files/directories, command history, processes, hostnames, bookmarks, git commits, etc.

> **Análise IA:** Fuzzy finder CLI universal. Estándar para shell scripts, searching en archivos/historia/procesos. Indispensable en workflow moderno Unix. Activo, Go, miles de integraciones comunitarias.

**Pontos fortes:** _Prácticamente obligatorio para devs Unix, integración con toda herramienta imaginable_ · _Activo, confiable, overhead mínimo_

**Tags:** `cli` `fuzzy-finder` `go` `unix-philosophy`

---

### [Gradle](https://gradle.org)

aparece em 2 listas

Incremental builds programmed via Groovy instead of declaring XML. Works well with Maven's dependency management.

> **Análise IA:** Build tool para Java con sintaxis Groovy programática vs XML declarativo. Builds incrementales, buena integración con Maven repos. Alternativa moderna a Maven.

**Pontos fortes:** _Sintaxis Groovy más flexible y menos verbosa que Maven XML_ · _Builds incrementales más rápidos_

**Tags:** `java` `build-automation` `groovy` `incremental`

---

### [GTK+](https://gtk.org)

aparece em 2 listas

A multi-platform toolkit for creating graphical user interfaces. [LGPL]

> **Análise IA:** Toolkit GUI multi-plataforma estándar en Linux desktop. Maduro, usado en GNOME y miles de apps. Curva aprendizaje pronunciada, pero production-ready.

**Pontos fortes:** _Ecosistema maduro con librerías integradas y binding en múltiples lenguajes_ · _Nativo en Linux, buena integración con escritorios GNOME/KDE_

**Tags:** `gui` `gtk` `cross-platform` `linux` `desktop`

---

### [Homebrew](https://brew.sh)

aparece em 2 listas

The missing package manager for macOS. ![Freeware][Freeware Icon] [![Open-Source Software][OSS Icon]](https://github.com/Homebrew/brew/)

> **Análise IA:** Package manager de facto en macOS. Estándar industria para devs Mac. Resuelve distribución de software sin dolor. Open-source, activo, integrado en workflow de miles de desarrolladores.

**Pontos fortes:** _Estándar absoluto en macOS, ahorra horas en setup_ · _Activo, confiable, con ecosistema masivo de fórmulas_

**Tags:** `package-manager` `macos` `cli` `open-source`

---

### [imgui](https://github.com/ocornut/imgui)

![](https://img.shields.io/github/stars/ocornut/imgui?style=flat-square&label=⭐) · aparece em 2 listas

Immediate Mode Graphical User Interface with minimal dependencies. [MIT]

> **Análise IA:** GUI inmediata minimalista en C++. Excelente para tools internas, debugging, prototipado. Renderiza GPU-friendly. Estándar en graphics/gamedev. No para UI empresarial.

**Pontos fortes:** _Minimalismo radical + performance_ · _Curva aprendizaje baja para use case específico_

**Tags:** `cpp` `immediate-mode-gui` `graphics`

---

### [IntelliJ IDEA](https://jetbrains.com/idea)

aparece em 2 listas

Powerful IDE for JVM languages. (**Free** for Students)

> **Análise IA:** IDE JetBrains flagship para JVM (Java, Kotlin, etc). Gold standard en desarrollo backend/Android. Poderoso pero costoso. Alternativas libres cierran brecha.

**Pontos fortes:** _Refactoring y análisis estático superior_ · _Plugin ecosystem masivo, integración perfecta JVM_

**Tags:** `ide` `java` `kotlin` `jvm`

---

### [Jupyter](https://github.com/markusschanta/awesome-jupyter)

![](https://img.shields.io/github/stars/markusschanta/awesome-jupyter?style=flat-square&label=⭐) · aparece em 2 listas

Create and share documents that contain code, equations, visualizations and narrative text.

> **Análise IA:** Entorno interactivo para notebooks (code + markdown + output). De facto para research, educación, data science. Ecosistema maduro, estándar indiscutido.

**Pontos fortes:** _Flexibilidad narrativa + código vivo_ · _Integración con 100+ librerías de viz/compute_

**Tags:** `notebook` `interactive` `python` `research` `visualization`

---

### [MicroPython](https://github.com/micropython/micropython)

![](https://img.shields.io/github/stars/micropython/micropython?style=flat-square&label=⭐) · aparece em 2 listas

Aims to put an implementation of Python 3.x on a microcontroller. [MIT]

> **Análise IA:** Python 3.x en microcontroladores (STM32, ESP32, etc). Estándar de facto para IoT educativo y hobbyista. Resuelve problema: programar embebidos sin C/C++.

**Pontos fortes:** _Python real en hardware con recursos limitados, curva de aprendizaje mínima_ · _Comunidad masiva, soporte multi-chip, ecosystem grande_

**Tags:** `python` `microcontroller` `embedded` `iot` `esp32`

---

### [mitmproxy](https://github.com/mitmproxy/mitmproxy)

![](https://img.shields.io/github/stars/mitmproxy/mitmproxy?style=flat-square&label=⭐) · aparece em 2 listas

_(label: help-wanted)_ <br> An interactive TLS-capable intercepting HTTP proxy for penetration testers and software developers

> **Análise IA:** Proxy HTTP/HTTPS interactivo para testing y pentesting. Herramienta de facto en seguridad. Resuelve debugging de requests HTTPS e inspection de tráfico.

**Pontos fortes:** _TLS termination interactivo_ · _API programática + web UI_

**Tags:** `proxy` `http` `https` `security` `penetration-testing`

---

### [mypy](https://github.com/python/mypy)

![](https://img.shields.io/github/stars/python/mypy?style=flat-square&label=⭐) · aparece em 2 listas

_(label: good first issue)_ <br> Optional static typing for Python.

> **Análise IA:** Type checker estático para Python. Estándar de la industria para tipado opcional. Resuelve problema crítico: mantener calidad sin overhead de lenguaje tipado.

**Pontos fortes:** _Estándar de facto para type checking en Python_ · _Mantiene retrocompatibilidad con código no tipado_

**Tags:** `static-typing` `python` `linter`

---

### [Neon](https://github.com/neon-bindings/neon)

![](https://img.shields.io/github/stars/neon-bindings/neon?style=flat-square&label=⭐) · aparece em 2 listas

Rust bindings for writing safe and fast native Node.js modules.

> **Análise IA:** Bindings seguros Rust ↔ Node.js natives. Performance critica (crypto, image processing). Activo, bien diseñado. Resuelve problema real: escribir C++ modules sin dolor.

**Pontos fortes:** _Memory-safety sin GC overhead_ · _Ejemplos production-ready_

**Tags:** `rust` `node.js` `native-bindings` `ffi`

---

### [Node.js core](https://github.com/nodejs/node)

![](https://img.shields.io/github/stars/nodejs/node?style=flat-square&label=⭐) · aparece em 2 listas

_(label: good first issue)_ <br> JavaScript runtime built on Chrome's V8 JavaScript engine

> **Análise IA:** Runtime JavaScript de facto. Estándar industrial para backend, CLI, edge. Core del ecosistema JS/TS moderno.

**Pontos fortes:** _Estándar absoluto, mantenimiento empresarial activo_ · _Ecosistema npm más grande que existe_

**Tags:** `javascript` `runtime` `backend` `v8`

---

### [Notion](https://notion.so)

aparece em 2 listas

All-in-one workspace for your notes, tasks, wikis, and databases.

> **Análise IA:** Workspace all-in-one dominante: notas, bases de datos, tareas, wikis. Estándar de facto en equipos modernos. Sincrono, colaborativo, con API robusta pero vendor-locked.

**Pontos fortes:** _Interfaz polida, adopción masiva_ · _Flexibilidad del data model (databases, relations)_

**Tags:** `saas` `workspace` `collaborative` `closed-source`

---

### [OpenAPI Generator](https://github.com/openapitools/openapi-generator)

![](https://img.shields.io/github/stars/openapitools/openapi-generator?style=flat-square&label=⭐) · aparece em 2 listas

OpenAPI Generator allows generation of API client libraries (e.g. C#, TypeScript, etc), server stubs (ASP.NET Core, NancyFx, etc), documentation and configuration automatically given an OpenAPI Spec (v2, v3).

> **Análise IA:** Generador de código a partir de specs OpenAPI. Crea clientes, servidores y docs automáticamente. Estándar en equipos que usan OpenAPI/Swagger. Ahorra horas de boilerplate.

**Pontos fortes:** _Cubre 50+ lenguajes y frameworks en un solo generador_ · _Genera código production-ready, no templates rotos_

**Tags:** `openapi` `codegen` `api` `documentation` `multi-language`

---

### [Postman](https://getpostman.com)

aparece em 2 listas

GUI platform for API development. ![Freeware][Freeware Icon]

> **Análise IA:** GUI para API testing, collections y docs. Estándar de facto en industria. Gratuito con plan Pro. Excelente UX, integraciones y automation.

**Pontos fortes:** _Collections y workspace sharing maduros_ · _Built-in mocking, testing, y documentación_

**Tags:** `api` `testing` `rest` `http`

---

### [Pytest](https://github.com/pytest-dev/pytest)

![](https://img.shields.io/github/stars/pytest-dev/pytest?style=flat-square&label=⭐) · aparece em 2 listas

_(label: status:-easy)_ <br> The pytest framework makes it easy to write small tests, yet scales to support complex functional testing.

> **Análise IA:** Framework testing Python estándar industrial. Sintaxis simple, fixtures poderosas, escalable a tests complejos. Reemplazó unittest.

**Pontos fortes:** _Sintaxis más limpia y menos boilerplate que unittest_ · _Sistema de fixtures maduro para dependency injection en tests_

**Tags:** `testing` `python` `fixtures` `assertions`

---

### [RustDesk](https://github.com/rustdesk/rustdesk)

![](https://img.shields.io/github/stars/rustdesk/rustdesk?style=flat-square&label=⭐) · aparece em 2 listas

[99332⭐] - Open source virtual / remote desktop. TeamViewer alternative. Built with Rust by [RustDesk team](https://www.rustdesk.com/).

> **Análise IA:** Escritorio remoto open-source en Rust, alternativa a TeamViewer/Chrome Remote. 99k estrellas, activo, self-hosted posible. Resuelve RDP de forma ligera sin vendor lock-in.

**Pontos fortes:** _Extremadamente ligero, bajo latency, código auditable_ · _Funciona sin servidores centrales, control total_

**Tags:** `remote-desktop` `rust` `open-source` `self-hosted` `cross-platform`

---

### [Sccache](https://github.com/mozilla/sccache)

![](https://img.shields.io/github/stars/mozilla/sccache?style=flat-square&label=⭐) · aparece em 2 listas

A fast compiler cache for C/C++, with cross-platform support and cloud backed storage options.

> **Análise IA:** Cache de compilador rápido para C/C++ con almacenamiento cloud. Para build pipelines que repiten compilaciones iguales en CI/local.

**Pontos fortes:** _Ganancia real en builds repetitivos (8-20x faster)_ · _Cloud storage backend flexible (S3, Redis, etc)_

**Tags:** `compiler-cache` `c` `cpp` `build` `mozilla`

---

### [Selenium](https://github.com/christian-bromann/awesome-selenium)

![](https://img.shields.io/github/stars/christian-bromann/awesome-selenium?style=flat-square&label=⭐) · aparece em 2 listas

Open-source browser automation framework and ecosystem.

> **Análise IA:** Framework de browser automation open-source. Resuelve testing y scraping de navegadores. Estándar de industria con amplio soporte lingüístico.

**Pontos fortes:** _Soporte oficial WebDriver, múltiples lenguajes_ · _Estándar de facto para testing en web_

**Tags:** `browser-automation` `testing` `webdriver` `cross-browser`

---

### [sharkdp/bat](https://github.com/sharkdp/bat)

![](https://img.shields.io/github/stars/sharkdp/bat?style=flat-square&label=⭐) · aparece em 2 listas

A cat(1) clone with wings. [](https://github.com/sharkdp/bat/actions/workflows/CICD.yml)

> **Análise IA:** Reemplazo de `cat` con syntax highlighting, git integration y line numbers. Mejora UX en lectura de archivos desde CLI. Estándar en toolchains modernos.

**Pontos fortes:** _Highlighting automático sin configuración_ · _Integración seamless con git (muestra cambios)_

**Tags:** `cli` `rust` `files` `syntax-highlighting`

---

### [sharkdp/fd](https://github.com/sharkdp/fd)

![](https://img.shields.io/github/stars/sharkdp/fd?style=flat-square&label=⭐) · aparece em 2 listas

A simple, fast and user-friendly alternative to find. [](https://github.com/sharkdp/fd/actions/workflows/CICD.yml)

> **Análise IA:** Reemplazo de `find` más rápido, intuitivo y amigable. Sintaxis simplificada, respeta .gitignore por defecto. Estándar en toolchains modernos.

**Pontos fortes:** _UX drasticamente mejorada vs find (sintaxis natural)_ · _Respeta .gitignore automáticamente_

**Tags:** `cli` `rust` `files` `search`

---

### [Taskwarrior](https://taskwarrior.org)

aparece em 2 listas

Taskwarrior is Free and Open Source Software that manages your TODO list from your command line. It is flexible, fast, efficient, and unobtrusive. It does its job then gets out of your way.

> **Análise IA:** TODO list CLI minimalista, rápido y eficiente. Filosofía Unix: hace una cosa bien. Flexible con sintaxis potente para power users.

**Pontos fortes:** _Extremadamente liviano y rápido_ · _Sintaxis flexible y scripting avanzado para automatización_

**Tags:** `cli` `productivity` `task-management` `c++` `unix`

---

### [Vim](https://vim.org)

aparece em 2 listas

An old terminal-based editor. For common plugins, check [Vim Common Plugins](editor-plugin-zh.md#vim-plugin). [![Open-Source Software][OSS Icon]](https://github.com/vim/vim) ![Freeware][Freeware Icon] [![Awesome List][awesome-list Icon]](https://github.com/mhinz/vim-galore#readme)

> **Análise IA:** Editor modal terminal, estándar unix desde 1991. Ubiquo en servers. Shallow learning, high ceiling. Hoy compite con Neovim (fork activo).

**Pontos fortes:** _Omnipresente en cualquier unix_ · _Modal editing paradigm superior para texto bulk_

**Tags:** `editor` `terminal` `modal` `unix`

---

### [VSCodium](https://vscodium.com)

aparece em 2 listas

An open source cross-platform extensible code editor based on [VS Code by Microsoft](https://code.visualstudio.com/) removing their non-free additions.

> **Análise IA:** VS Code open-source puro, sin telemetría Microsoft. Fork mantenido, extensiones compatibles. Alternativa ética a VS Code proprietary, mismo poder.

**Pontos fortes:** _Feature parity VS Code sin tracking_ · _Comunidad activa, builds para todas plataformas_

**Tags:** `code-editor` `open-source` `vscode` `typescript` `cross-platform`

---

### [Xcode](https://developer.apple.com/xcode)

aparece em 2 listas

Essential IDE for iOS/macOS development. [![App Store][app-store Icon]](https://apps.apple.com/app/id497799835?platform=mac)

> **Análise IA:** IDE estándar de Apple para iOS/macOS. Imprescindible si trabajás en ecosistema Apple. Integración nativa, debugger potente, excelente performance.

**Pontos fortes:** _Integración perfecta con Xcode Server y Apple frameworks_ · _Debugger y profiler nativos sin rival en el ecosistema_

**Tags:** `ide` `swift` `ios` `macos`

---

### [Zed](https://zed.dev)

aparece em 2 listas

A high-performance, multiplayer code editor from the creators of Atom and Tree-sitter. [![Open-Source Software][OSS Icon]](https://github.com/zed-industries/zed) ![Freeware][Freeware Icon]

> **Análise IA:** Editor Rust ultra-rápido, multiplayer, modern UX. Si programás en Rust o quiero algo que no lagguee en archivos grandes, es la mejor opción actual.

**Pontos fortes:** _Performance genuinamente superior a VS Code en archivos enormes_ · _Colaboración en tiempo real nativa, UX pulida_

**Tags:** `rust` `editor` `multiplayer` `performance`

---


---

## 👍 Vale testar — sólidas no seu nicho

Menos hype que as GEMs, mas confiáveis se você cair no caso de uso.

### [Cline](https://marketplace.visualstudio.com/items)

🔥 **aparece em 7 listas**

Autonomous coding agent for VS Code that can create/edit files, execute commands, and use the browser with user permission. Supports multiple AI providers including OpenRouter, Anthropic, OpenAI, Google Gemini, AWS Bedrock, Azure, and GCP Vertex.

> **Análise IA:** De los agentes de código en VS Code, Cline es probablemente el más serio del mercado. No es un autocomplete glorificado: ejecuta comandos, toca el filesystem y navega el browser con tu permiso explícito. El modelo de 'human-in-the-loop' es lo que lo salva del caos. Soporta prácticamente todos los providers relevantes, lo que te evita el lock-in. Ideal para devs que quieren automatizar tareas repetitivas sin ceder el control total. No es magia, pero tampoco es humo.

**Pontos fortes:** _Soporte real de múltiples providers (Anthropic, OpenAI, Gemini, Bedrock, etc.) sin vendor lock-in_ · _Modelo de permisos explícitos por acción: no ejecuta nada sin tu aprobación, lo que lo hace usable en producción real_ · _Capacidad de agente completo: edita archivos, corre comandos y usa el browser en un solo flujo_

**Tags:** `vscode-extension` `ai-agent` `autonomous-coding` `multi-provider` `open-source`

---

### [Bokeh](https://github.com/bokeh/bokeh)

![](https://img.shields.io/github/stars/bokeh/bokeh?style=flat-square&label=⭐) · aparece em 4 listas

- Bokeh is an interactive visualization library for Python that enables beautiful and meaningful visual presentation of data in modern web browsers.

> **Análise IA:** Bokeh es una biblioteca de visualización Python madura y legítima, no hype. Resuelve un problema real: crear gráficos interactivos para el browser sin escribir JavaScript. El diferencial es que genera HTML/JS autónomo o se integra con servidores como Tornado/Flask para dashboards con datos en vivo. Ideal para data scientists y devs Python que necesitan más que matplotlib pero no quieren meterse en D3.js. Compite con Plotly; Bokeh gana en personalización y control del rendering, pero tiene una curva de aprendizaje más pronunciada.

**Pontos fortes:** _Genera visualizaciones interactivas autocontenidas en HTML/JS sin requerir conocimiento de JavaScript por parte del desarrollador_ · _Soporta streaming de datos en tiempo real via Bokeh Server, útil para dashboards de monitoreo con actualizaciones dinámicas_ · _Altamente personalizable a bajo nivel: control fino sobre widgets, layouts y callbacks del lado servidor o cliente_

**Tags:** `python` `data-visualization` `interactive-charts` `open-source` `javascript-output`

---

### [Sniffnet](https://github.com/gyulyvgc/sniffnet)

![](https://img.shields.io/github/stars/gyulyvgc/sniffnet?style=flat-square&label=⭐) · aparece em 4 listas

Cross-platform application to monitor your network traffic with ease [](https://github.com/GyulyVGC/sniffnet/blob/main/.github/workflows/rust.yml) [](https://crates.io/crates/sniffnet)

> **Análise IA:** Herramienta legítima y útil para monitorear tráfico de red con una UI cómoda, construida en Rust. No es un Wireshark killer, pero tampoco pretende serlo: apunta a devs y sysadmins que necesitan visibilidad rápida de qué está pasando en su red sin volverse locos con tcpdump. El diferencial es la experiencia de uso: gráficos en tiempo real, filtros simples, multiplataforma. Para debugging de conectividad o auditorías básicas, es genuinamente bueno. Open source y gratuito suman mucho.

**Pontos fortes:** _UI accesible que hace que el monitoreo de tráfico sea consumible sin ser experto en redes_ · _Escrito en Rust: performance nativa y binario standalone sin dependencias pesadas_ · _Open source con desarrollo activo en GitHub, bien mantenido_

**Tags:** `rust` `networking` `open-source` `packet-sniffer` `cross-platform`

---

### [Cake](https://github.com/cake-build/cake)

![](https://img.shields.io/github/stars/cake-build/cake?style=flat-square&label=⭐) · aparece em 3 listas

_(label: Good-first-issue)_ <br> Cake (C# Make) is a free and open source cross-platform build automation system with a C# DSL for tasks such as compiling code, copying files and folders, running unit tests, compressing files and building NuGet packages.

> **Análise IA:** Build system en C# con DSL para compile, testing, packaging. Para .NET teams que quieren scripting de build portable sin PowerShell crudo. Resuelve fricciones de cross-platform build automation.

**Pontos fortes:** _DSL en C# permite reutilizar logica de compilación sin shell script, más type-safe_ · _Integración nativa con NuGet y ecosystem .NET sin plugins externos_

**Tags:** `csharp` `build-automation` `dsl` `ci-cd` `dotnet`

---

### [Colossal-AI](https://github.com/hpcaitech/colossalai)

![](https://img.shields.io/github/stars/hpcaitech/colossalai?style=flat-square&label=⭐) · aparece em 3 listas

- A unified deep learning system for big model era, which helps users to efficiently and quickly deploy large AI model training and inference.

> **Análise IA:** Framework distribuido para entrenamiento/inferencia de LLMs grandes. Optimizaciones para multi-GPU, tensor parallelism. Para MLOps que entrenan modelos propios.

**Pontos fortes:** _Optimizaciones specific para big models (tensor/pipeline parallelism)_ · _Integration con HF transformers_

**Tags:** `python` `llm` `distributed-training` `gpu` `deep-learning`

---

### [Deepchecks](https://github.com/deepchecks/deepchecks)

![](https://img.shields.io/github/stars/deepchecks/deepchecks?style=flat-square&label=⭐) · aparece em 3 listas

- Deepchecks is a holistic open-source solution for all of your AI & ML validation needs, enabling you to test your data and models from research to production thoroughly.

> **Análise IA:** Framework Python para validación exhaustiva de datos y modelos ML en toda la pipeline. Resuelve el problema real de detectar data drift, model degradation y issues de calidad antes de producción. Para data scientists y ML engineers serios.

**Pontos fortes:** _Cobertura integral: data checks, model validation, drift detection en un solo lugar_ · _Integración práctica con workflows reales (notebooks, CI/CD, production monitoring)_

**Tags:** `python` `ml-validation` `testing` `data-quality` `open-source`

---

### [intelli-shell](https://github.com/lasantosr/intelli-shell)

![](https://img.shields.io/github/stars/lasantosr/intelli-shell?style=flat-square&label=⭐) · aparece em 3 listas

Bookmark commands with placeholders and search or autocomplete at any time [](https://crates.io/crates/intelli-shell) [](https://github.com/lasantosr/intelli-shell/actions/workflows/release.yml)

> **Análise IA:** CLI en Rust para guardar comandos frecuentes con placeholders y recuperarlos por búsqueda/autocompletado. Para devops y sysadmins que repiten comandos complejos. Resuelve el tedio de escribir lo mismo diariamente.

**Pontos fortes:** _Escrito en Rust: binario rápido y sin dependencias runtime_ · _Búsqueda fuzzy y placeholders parametrizables hacen reutilización flexible_

**Tags:** `rust` `cli` `productivity` `shell` `bookmarks`

---

### [lstags](https://github.com/ivanilves/lstags)

![](https://img.shields.io/github/stars/ivanilves/lstags?style=flat-square&label=⭐) · aparece em 3 listas

Tool and API to sync Docker images across different registries.

> **Análise IA:** CLI + API para sincronizar imágenes Docker entre registries (Docker Hub, ECR, GCR, etc). Para DevOps/SREs que necesitan replicar imágenes. Resuelve: evitar vendor lock-in de registries.

**Pontos fortes:** _Simple, hace una cosa bien_ · _Paralelización de pulls/pushes_

**Tags:** `docker` `registry` `devops` `golang`

---

### [Mocha](https://github.com/mochajs/mocha)

![](https://img.shields.io/github/stars/mochajs/mocha?style=flat-square&label=⭐) · aparece em 3 listas

_(label: good first issue)_ <br> Javascript test framework for Node.js and the browser.

> **Análise IA:** Test runner JS/Node maduro. Para testing en Node.js y browsers. Estándar de facto, compite con Jest/Vitest pero sigue siendo sólido.

**Pontos fortes:** _Sintaxis clara, fácil de leer para no-especialistas_ · _Integración directa con CI/CD sin configuración compleja_

**Tags:** `javascript` `testing` `nodejs` `browser`

---

### [OctoLinker](https://github.com/octolinker/browser-extension)

![](https://img.shields.io/github/stars/octolinker/browser-extension?style=flat-square&label=⭐) · aparece em 3 listas

Navigate through `projects.json` files efficiently with the OctoLinker browser extension for GitHub.

> **Análise IA:** Browser extension GitHub: navegación inteligente en monorepos via package.json. Para devs browsing código en GH. Resuelve: saltar imports sin clonar repo.

**Pontos fortes:** _Zero-config, activa automáticamente en GH_ · _Soporta monorepos y path mappings_

**Tags:** `github` `browser-extension` `typescript` `navigation` `dev-tools`

---

### [Polyaxon](https://github.com/polyaxon/polyaxon)

![](https://img.shields.io/github/stars/polyaxon/polyaxon?style=flat-square&label=⭐) · aparece em 3 listas

- A platform for reproducible and scalable machine learning and deep learning on kubernetes - [(Video)](https://www.youtube.com/watch?v=Iexwrka_hys).

> **Análise IA:** Plataforma ML completa para entrenar y desplegar en Kubernetes. Orientada a reproducibilidad y escalabilidad. Para equipos que necesitan workflow ML estructurado en infraestructura cloud.

**Pontos fortes:** _Integración nativa con Kubernetes sin overhead_ · _Tracking de experimentos y versionado de modelos_

**Tags:** `kubernetes` `ml-ops` `reproducibility` `python`

---

### [PyMC](https://github.com/pymc-devs/pymc)

![](https://img.shields.io/github/stars/pymc-devs/pymc?style=flat-square&label=⭐) · aparece em 3 listas

_(label: beginner friendly)_ <br> A Python library for Bayesian statistical modeling and probabilistic machine learning. Beginner-friendly with 'good first issue' labels.

> **Análise IA:** PyMC es la librería de referencia para modelado bayesiano en Python, y el label 'beginner friendly' no es humo: tiene documentación seria y ejemplos didácticos. Si trabajás en estadística, ciencia de datos o ML probabilístico, esto es herramienta real. No es para el dev promedio que quiere hacer un CRUD, pero si necesitás cuantificar incertidumbre o ajustar modelos estadísticos complejos, PyMC es producción-ready con comunidad activa detrás.

**Pontos fortes:** _API de alto nivel que abstrae la complejidad del muestreo MCMC sin sacrificar flexibilidad para usuarios avanzados_ · _Ecosistema maduro con ArviZ integrado para visualización y diagnóstico de modelos probabilísticos_ · _Comunidad activa y documentación con ejemplos reales que van desde regresión básica hasta modelos jerárquicos_

**Tags:** `bayesian` `probabilistic-ml` `statistics` `open-source` `python`

---

### [Readest](https://github.com/readest/readest)

![](https://img.shields.io/github/stars/readest/readest?style=flat-square&label=⭐) · aparece em 3 listas

_(label: good first issue)_ <br> A modern, feature-rich ebook reader designed for avid readers offering seamless cross-platform access, powerful tools, and an intuitive interface.

> **Análise IA:** Lector de ebooks en Rust con cross-platform. UI moderna, pero es herramienta bastante niche. Resuelve bien el problema si lees en múltiples plataformas.

**Pontos fortes:** _Binaries livianos, sin Electron overhead_ · _Buena integración con formatos estándar (EPUB, PDF)_

**Tags:** `rust` `desktop-app` `ebook-reader` `cross-platform`

---

### [Rider](https://jetbrains.com/rider)

aparece em 3 listas

A cross-platform C# IDE based on the IntelliJ platform and ReSharper

> **Análise IA:** IDE C# multiplataforma: JetBrains quality con soporte .NET nativo. Para devs C# que necesiten IDE pro. Resuelve: debugging, refactoring, performance profiling robusto.

**Pontos fortes:** _Refactoring automático enterprise-grade_ · _Debugging y profiling integrados sin plugins_

**Tags:** `csharp` `ide` `dotnet` `jetbrains` `windows-linux-mac`

---

### [Wave](https://github.com/wavetermdev/waveterm)

![](https://img.shields.io/github/stars/wavetermdev/waveterm?style=flat-square&label=⭐) · aparece em 3 listas

Open-source terminal with built-in file previews, web browsing, and AI tools. [![Open-Source Software][OSS Icon]](https://github.com/wavetermdev/waveterm) ![Freeware][Freeware Icon]

> **Análise IA:** Terminal abierta con previews de archivos, web browsing y tooling AI integrado. Atractivo pero incipiente. Resuelve UX de terminal tradicional pero necesita madurez.

**Pontos fortes:** _UI moderna y responsive comparado con tmux/screen_ · _Web browsing integrado es genuinamente útil_

**Tags:** `terminal` `rust` `ai-integration` `open-source`

---

### [yt-dlp](https://github.com/yt-dlp/yt-dlp)

![](https://img.shields.io/github/stars/yt-dlp/yt-dlp?style=flat-square&label=⭐) · aparece em 3 listas

Downloads videos from almost any online platform, along with information, thumbnails, subtitles, descriptions, and comments (comments only on a select few sites like Youtube and a few small sites). If a site is not supported, or a useful or crucial piece of metadata, including comments, is missing, create an issue.

> **Análise IA:** Descargador de videos robusto que reemplazó youtube-dl. Tira video + metadata desde casi cualquier plataforma. Resuelve problem real: archivado y análisis de contenido multimedia.

**Pontos fortes:** _Coverage absurdo de plataformas (YouTube, Twitch, TikTok, etc)_ · _Desarrollo muy activo con fixes constantes_

**Tags:** `cli` `video-download` `python` `metadata-extraction`

---

### [ActivityWatch](https://activitywatch.net)

aparece em 2 listas

Cross-platform, extensible, and privacy-focused time-tracker. [![Open-Source Software][OSS Icon]](https://github.com/ActivityWatch/activitywatch) ![Freeware][Freeware Icon]

> **Análise IA:** Time tracker multiplataforma enfocado en privacidad. Registra aplicaciones/ventanas activas. Útil para auditar productividad sin cloud.

**Pontos fortes:** _Completamente local, no envía datos a servidores_ · _Extensible via plugins y webhook_

**Tags:** `self-hosted` `privacy` `time-tracking` `cross-platform` `python`

---

### [Agentify](https://github.com/koriyoshi2041/agentify)

![](https://img.shields.io/github/stars/koriyoshi2041/agentify?style=flat-square&label=⭐) · aparece em 2 listas

CLI tool that transforms any OpenAPI spec into 9 agent interface formats (MCP server, AGENTS.md, CLAUDE.md, .cursorrules, Skills, llms.txt, GEMINI.md, A2A Card, CLI) with a single command. Tiered generation strategies for small to large APIs.

> **Análise IA:** Genera 9 formatos de agent interfaces desde OpenAPI specs con un comando. Útil para workflows que requieren múltiples integraciones AI pero muy específico.

**Pontos fortes:** _Soporte a 9 formatos en un comando_ · _Estrategias tiered para APIs chicas y grandes_

**Tags:** `ai` `openapi` `code-generation` `cli`

---

### [AI Git Narrator](https://github.com/pmusolino/ai-git-narrator)

![](https://img.shields.io/github/stars/pmusolino/ai-git-narrator?style=flat-square&label=⭐) · aparece em 2 listas

CLI tool that uses AI to automatically generate high-quality Git commit messages and pull request descriptions.

> **Análise IA:** CLI que genera commit messages y PRs con IA. Resuelve fricción en escritura de commits pero depende de APIs externas. Útil si tenés workflow estructurado.

**Pontos fortes:** _Ahorra tiempo en escritura repetitiva de commits_ · _Mejora consistencia en messages_

**Tags:** `ai` `git` `llm` `cli`

---

### [AppFlowy](https://appflowy.io)

aparece em 2 listas

Build detailed lists of to-do’s for different projects while tracking the status of each one. Open Source Notion Alternative.

> **Análise IA:** IDE Notion-like open-source en Rust/Dart. Listas, tareas, tracking visual. Buen stack tecnológico pero interfaz menos pulida que Notion, comunidad más pequeña.

**Pontos fortes:** _Stack multiplataforma robusto (Rust backend)_ · _AGPL permite self-hosting sin restricciones comerciales_

**Tags:** `rust` `dart` `open-source` `agpl-3.0`

---

### [ashvardanian/stringzilla](https://github.com/ashvardanian/stringzilla)

![](https://img.shields.io/github/stars/ashvardanian/stringzilla?style=flat-square&label=⭐) · aparece em 2 listas

SIMD-accelerated string search, sort, edit distances, alignments, and generators for x86 AVX2 & AVX-512, and Arm NEON [](https://crates.io/crates/stringzilla)

> **Análise IA:** String search/sort SIMD-acelerado (AVX2/AVX-512/NEON). Performance muy buena para bulk string ops, pero nicho especializado.

**Pontos fortes:** _Aceleración real en x86/ARM, benchmarks sólidos_ · _Bindings para múltiples lenguajes_

**Tags:** `simd` `rust` `strings` `performance`

---

### [ast-grep](https://github.com/ast-grep/ast-grep)

![](https://img.shields.io/github/stars/ast-grep/ast-grep?style=flat-square&label=⭐) · aparece em 2 listas

A CLI tool for code structural search, lint and rewriting.

> **Análise IA:** CLI para búsqueda estructural de código, linting y refactoring. AST-based, más potente que regex. Rust, velocidad nativa.

**Pontos fortes:** _Velocidad nativa en Rust, manejo correcto de AST vs regex_ · _Sintaxis de queries amigable para búsquedas complejas_

**Tags:** `ast` `cli` `linting` `refactoring` `rust`

---

### [ATAC](https://github.com/julien-cpsn/atac)

![](https://img.shields.io/github/stars/julien-cpsn/atac?style=flat-square&label=⭐) · aparece em 2 listas

A feature-full TUI API client made in Rust. ATAC is free, open-source, offline and account-less.

> **Análise IA:** TUI API client en Rust tipo Postman pero terminal. Offline, funciona sin cuenta. Para devs que pasan vida en terminal y odian UIs pesadas con propagandas.

**Pontos fortes:** _Completamente offline y funcional_ · _Performance y UX superior a herramientas web pesadas_

**Tags:** `api-client` `tui` `rust` `rest`

---

### [awesome-zsh-plugins](https://github.com/unixorn/awesome-zsh-plugins)

![](https://img.shields.io/github/stars/unixorn/awesome-zsh-plugins?style=flat-square&label=⭐) · aparece em 2 listas

ZSH frameworks, plugins, tutorials & themes.

> **Análise IA:** Curatoria de plugins, temas y recursos para ZSH. Referencia util pero no es herramienta ejecutable, solo lista clasificada.

**Pontos fortes:** _Buena organización y clasificación_ · _Actualizado regularmente con nuevos plugins_

**Tags:** `zsh` `curated-list` `shells` `reference`

---

### [Bartib](https://github.com/nikolassv/bartib)

![](https://img.shields.io/github/stars/nikolassv/bartib?style=flat-square&label=⭐) · aparece em 2 listas

] - A simple timetracker for the command line [](https://github.com/nikolassv/bartib/actions/workflows/test.yml)

> **Análise IA:** Time tracker minimalista CLI en Rust. Registra sesiones en JSON. Nicho ultraespecífico, código activo. Soluciona problema real para dev sin overhead.

**Pontos fortes:** _Binario compilado, cero dependencias runtime_ · _Formato JSON humano-legible, fácil scripting_

**Tags:** `cli` `rust` `time-tracking` `self-hosted`

---

### [Bazel](https://bazel.build)

aparece em 2 listas

A multi-language, fast and scalable build system from Google. [Apache]

> **Análise IA:** Build system multi-lenguaje de Google. Velocidad y escalabilidad superiores. Curva empinada pero estándar en monorepos grandes. Open source.

**Pontos fortes:** _Performance 10x+ vs Make/Maven en builds incrementales_ · _Cache distribuido y reproducibilidad garantizada_

**Tags:** `build-system` `java` `c++` `monorepo`

---

### [boilr](https://github.com/tmrts/boilr)

![](https://img.shields.io/github/stars/tmrts/boilr?style=flat-square&label=⭐) · aparece em 2 listas

Blazingly fast CLI tool for creating projects from boilerplate templates.

> **Análise IA:** CLI para scaffolding de proyectos desde templates boilerplate. Útil para developers que generan muchos repos. Resuelve la tarea pero compite con Cookiecutter, Yeoman y plataformas como Replit.

**Pontos fortes:** _Escrito en Go, arranque instantáneo_ · _Simple y directo, sin dependencias pesadas_

**Tags:** `cli` `golang` `scaffolding` `boilerplate`

---

### [broot](https://github.com/canop/broot)

![](https://img.shields.io/github/stars/canop/broot?style=flat-square&label=⭐) · aparece em 2 listas

A new way to see and navigate directory trees (get an overview of a directory, even a big one; find a directory then `cd` to it; never lose track of file hierarchy while you search; manipulate your files, ...), further reading [dystroy.org/broot](https://dystroy.org/broot/) [](https://crates.io/crates/broot)

> **Análise IA:** Navegador de directorios en TUI con búsqueda y manipulación de archivos. Sustituto moderno de tree/find con UX mejorada.

**Pontos fortes:** _Rendimiento rápido en directorios grandes_ · _Interfaz intuitiva para navegación rápida_

**Tags:** `rust` `cli` `tui` `file-navigation`

---

### [Buck2](https://github.com/facebook/buck2)

![](https://img.shields.io/github/stars/facebook/buck2?style=flat-square&label=⭐) · aparece em 2 listas

Encourages the creation of small, reusable modules consisting of code and resources.

> **Análise IA:** Build system de Facebook basado en módulos reusables. Competidor a Bazel/Gradle/Turborepo. Para monorepos medianos; complejidad comparable a rivals.

**Pontos fortes:** _Incremental builds muy rápido_ · _Rust → mejor rendimiento memory/speed que alternatives JVM_

**Tags:** `build-system` `rust` `monorepo` `facebook`

---

### [carbon-now-cli](https://github.com/mixn/carbon-now-cli)

![](https://img.shields.io/github/stars/mixn/carbon-now-cli?style=flat-square&label=⭐) · aparece em 2 listas

Beautiful images of your code — from right inside your terminal.

> **Análise IA:** Convierte código en imágenes bellas (style Carbon.now.sh) desde terminal. Para screenshots de código en tweets/docs.

**Pontos fortes:** _Workflow integrado sin browser_ · _Output visualmente consistente_

**Tags:** `cli` `code-screenshot` `images` `javascript`

---

### [CLion](https://jetbrains.com/clion)

aparece em 2 listas

Powerful C and C++ IDE. (**Free** for Students)

> **Análise IA:** IDE JetBrains para C/C++. Estándar sólido en embedded y sistemas. Poderoso pero pesado. Competencia fuerte de VS Code + CMake gratis.

**Pontos fortes:** _Análisis semántico muy preciso para C++_ · _Debugger integrado profesional_

**Tags:** `ide` `cpp` `c` `jetbrains`

---

### [config-file-validator](https://github.com/boeing/config-file-validator)

![](https://img.shields.io/github/stars/boeing/config-file-validator?style=flat-square&label=⭐) · aparece em 2 listas

Cross Platform tool to validate configuration files.

> **Análise IA:** Validador cross-platform de archivos de configuración (JSON, YAML, TOML, etc). Boeing lo mantiene. Resuelve problema real en CI/CD y despliegues.

**Pontos fortes:** _Múltiples formatos soportados_ · _Mantenido por empresa seria (Boeing)_

**Tags:** `config-validation` `cli` `golang` `ci-cd`

---

### [Cppcheck](https://cppcheck.sourceforge.net)

aparece em 2 listas

A tool for static C/C++ code analysis. - [source](https://github.com/danmar/cppcheck)

> **Análise IA:** Analizador estático C/C++ open-source. Detecta bugs y malos olores en código C/C++. Integrable en CI/CD, complementario a compilador.

**Pontos fortes:** _Bajo rate de falsos positivos, basado en análisis real de código_ · _Sin dependencias externas, rápido de ejecutar_

**Tags:** `static-analysis` `cpp` `c` `linter` `quality`

---

### [CppSharp](https://github.com/mono/cppsharp)

![](https://img.shields.io/github/stars/mono/cppsharp?style=flat-square&label=⭐) · aparece em 2 listas

Tools and libraries to glue C/C++ APIs to high-level languages. [MIT]

> **Análise IA:** Generador de bindings C/C++ a lenguajes de alto nivel. Para desarrolladores que necesitan integrar librerías nativas en .NET. Resuelve el dolor de mantenimiento de wrappers manuales, pero requiere conocimiento de ambos mundos.

**Pontos fortes:** _Automatiza generación de bindings reduciendo boilerplate_ · _Soporte multiplataforma (Windows, Linux, macOS)_

**Tags:** `interop` `csharp` `c++binding` `code-generation`

---

### [create-go-app/cli](https://github.com/create-go-app/cli)

![](https://img.shields.io/github/stars/create-go-app/cli?style=flat-square&label=⭐) · aparece em 2 listas

Clean project logo. Useful badges (version, code style, test cover, docs). Clear readme with quickstart, understandable installation and usage manual, video screencast, ToC with well-documented project features (with a demo recording of the work in the terminal), project philosophy notes ("the why another"), most frequently asked questions, and more.

> **Análise IA:** CLI scaffolder para Go con documentación exhaustiva. Crea proyectos boilerplate con estructura limpia, badges informativos y guías video. Resuelve el problema real de iniciar Go apps sin decisiones arquitectónicas tediosas.

**Pontos fortes:** _Documentación excepcional con demos video integradas_ · _Cobertura completa: desde instalación hasta filosofía del proyecto_

**Tags:** `cli` `go` `scaffolder` `boilerplate`

---

### [Dash](https://kapeli.com/dash)

aparece em 2 listas

Offline API documentation browser for macOS with instant search access to Vue.js docs and 200+ other frameworks.

> **Análise IA:** Navegador offline de docs API para macOS. 200+ frameworks indexados. Búsqueda instantánea sin red. Herramienta dev premium que paga sola en horas ahorradas, pero macOS-only.

**Pontos fortes:** _Búsqueda subsecond en 200+ docsets_ · _Integración con IDEs (Xcode, VS Code vía snippets)_

**Tags:** `macos` `documentation` `offline` `developer-tools`

---

### [diskonaut](https://github.com/imsnif/diskonaut)

![](https://img.shields.io/github/stars/imsnif/diskonaut?style=flat-square&label=⭐) · aparece em 2 listas

Terminal visual disk space navigator

> **Análise IA:** Explorador de espacio en disco en TUI. Visualización interactiva de qué directorios pesan. Rust nativo, más veloz que `ncdu` en discos grandes.

**Pontos fortes:** _Interfaz TUI responsiva y fluida_ · _Navegación y análisis más ágil que herramientas shell puras_

**Tags:** `rust` `tui` `cli` `disk-analysis`

---

### [dotenv-linter](https://github.com/dotenv-linter/dotenv-linter)

![](https://img.shields.io/github/stars/dotenv-linter/dotenv-linter?style=flat-square&label=⭐) · aparece em 2 listas

Linter for `.env` files [](https://github.com/dotenv-linter/dotenv-linter/actions?query=workflow%3ACI+branch%3Amaster)

> **Análise IA:** Linter para archivos .env en Rust. Herramienta simple y útil para detectar problemas en config. Resuelve problema real pero muy específico.

**Pontos fortes:** _Binario Rust: ultra rápido_ · _Checks prácticos (.env validity, duplicates)_

**Tags:** `rust` `linter` `cli` `dotenv`

---

### [editly](https://github.com/mifi/editly)

![](https://img.shields.io/github/stars/mifi/editly?style=flat-square&label=⭐) · aparece em 2 listas

Declarative video editing API.

> **Análise IA:** API declarativa para edición de video. Define pipelines de efectos, transiciones, overlays programáticamente.

**Pontos fortes:** _Abstracción declarativa sobre FFmpeg_ · _Automatización de edición sin GUI_

**Tags:** `video` `editing` `declarative` `javascript` `ffmpeg`

---

### [einops](https://github.com/arogozhnikov/einops)

![](https://img.shields.io/github/stars/arogozhnikov/einops?style=flat-square&label=⭐) · aparece em 2 listas

- Flexible and powerful tensor operations for readable and reliable code.

> **Análise IA:** Librería Python para tensor reshaping/slicing con sintaxis readable. Resuelve problema real: operaciones tensor sin broadcasting confusion. Alternativa a NumPy puro.

**Pontos fortes:** _Sintaxis Einstein-notation super legible y correcta_ · _Compatible con PyTorch, TensorFlow, JAX backend-agnostic_

**Tags:** `python` `tensor-ops` `numpy` `readable-code`

---

### [fjira](https://github.com/mk-5/fjira)

![](https://img.shields.io/github/stars/mk-5/fjira?style=flat-square&label=⭐) · aparece em 2 listas

A fuzzy-search based terminal UI application for Attlasian Jira

> **Análise IA:** TUI Fuzzy para Jira en terminal. Útil para devs que viven en CLI. Cubre solo lectura y búsqueda, no workflow completo.

**Pontos fortes:** _Interfaz responsiva y fuzzy search fluido_ · _Reduce context switching desde terminal_

**Tags:** `jira` `cli` `rust` `tui`

---

### [fkill](https://github.com/sindresorhus/fkill-cli)

![](https://img.shields.io/github/stars/sindresorhus/fkill-cli?style=flat-square&label=⭐) · aparece em 2 listas

Fabulously kill processes. Cross-platform.

> **Análise IA:** Kill procesos por nombre/patrón cross-platform. Resuelve UX horrible de `kill -9`. Lightweight, Sindre Sorhus quality. Útil para devs que no quieren Task Manager.

**Pontos fortes:** _Interfaz interactiva y confirmación clara_ · _Cross-platform sin inconsistencias_

**Tags:** `process-management` `cli` `node`

---

### [Focalboard](https://focalboard.com)

aparece em 2 listas

Define, organize, track and manage work across individuals and teams (alternative to Trello, Notion and Asana). ) `MIT/AGPL-3.0/Apache-2.0`

> **Análise IA:** Alternativa open-source a Trello/Notion/Asana. Multiplataforma (desktop + web), self-hosted, soporta múltiples licencias. Útil para equipos que quieren escapar de SaaS propietario sin perder funcionalidad colaborativa.

**Pontos fortes:** _Self-hosted y open-source con múltiples licencias_ · _Soporte multiplataforma (desktop + web) desde el mismo código base_

**Tags:** `project-management` `self-hosted` `nodejs` `go` `docker`

---

### [fx](https://github.com/antonmedv/fx)

![](https://img.shields.io/github/stars/antonmedv/fx?style=flat-square&label=⭐) · aparece em 2 listas

Terminal JSON viewer & processor.

> **Análise IA:** Viewer/procesador JSON interactivo para terminal. Minimalista, rápido. Para quien vive con APIs y logs JSON.

**Pontos fortes:** _Interfaz interactiva fluida, binario tiny (~6MB)_ · _Búsqueda y filtrado intuitivo vs jq puro_

**Tags:** `cli` `json` `terminal` `visualization`

---

### [Gebug](https://github.com/moshebe/gebug)

![](https://img.shields.io/github/stars/moshebe/gebug?style=flat-square&label=⭐) · aparece em 2 listas

A tool that makes debugging of Dockerized Go applications super easy by enabling Debugger and Hot-Reload features, seamlessly.

> **Análise IA:** Debugging + hot-reload para Go en Docker. Integra Delve debugger sin perder iteración de desarrollo. Útil para workflows local-as-prod.

**Pontos fortes:** _hot-reload sin restart manual_ · _Delve integrado_

**Tags:** `debugging` `docker` `go` `development` `hot-reload`

---

### [ggc](https://github.com/bmf-san/ggc)

![](https://img.shields.io/github/stars/bmf-san/ggc?style=flat-square&label=⭐) · aparece em 2 listas

A Git CLI tool with both traditional command-line and interactive incremental-search UI, workflow support, and configurable keybindings.

> **Análise IA:** Git CLI con UI incremental y búsqueda interactiva. Mejor UX que git vanilla para workflows complejos. Configurable, pensado para devs que viven en la terminal.

**Pontos fortes:** _búsqueda incremental fluida_ · _keybindings customizables_

**Tags:** `git` `cli` `vcs` `interactive` `go`

---

### [GitButler](https://gitbutler.com)

aparece em 2 listas

Change management with parallel and stacked branches, unlimited undo, agent integrations. [![Open-Source Software][OSS Icon]](https://github.com/gitbutlerapp/gitbutler) ![Freeware][Freeware Icon]

> **Análise IA:** Git UI con branches paralelas/stacked, undo infinito, AI agent. Moderno, resuelve pain-points reales de rebase/cherry-pick. Gratuito OSS, early pero con tracción.

**Pontos fortes:** _Stacked branches + undo infinito elimina rebase pain_ · _Agent integrations reducen manual rebasing_

**Tags:** `git` `vcs` `ui` `ai-agent` `oss`

---

### [GitKraken](https://gitkraken.com)

aparece em 2 listas

The most popular Git GUI for Windows, Mac and Linux.

> **Análise IA:** Git GUI más popular: visualización ramas, merge intuitivo, integración GitHub/GitLab/Bitbucket. Freemium, funcionalidad base sólida pero pro features son pago.

**Pontos fortes:** _Visualización DAG Git impecable, UX fluida_ · _Integración múltiples plataformas (GitHub, GitLab, Bitbucket)_

**Tags:** `git-gui` `version-control` `freemium` `cross-platform`

---

### [GNU Emacs](https://gnu.org/software/emacs)

aparece em 2 listas

An extensible, customizable text editor-and more. `GPL-3.0` `C`

> **Análise IA:** Editor cult con 40+ años de historia. Lisp-based, infinitamente customizable. No es herramienta modern; es religión. Productivo si invertís meses.

**Pontos fortes:** _Customización sin límites (lenguaje vivo)_ · _Comunidad zealot con recursos avanzados_

**Tags:** `editor` `lisp` `cli` `text-editor`

---

### [grex](https://github.com/pemistahl/grex)

![](https://img.shields.io/github/stars/pemistahl/grex?style=flat-square&label=⭐) · aparece em 2 listas

A command-line tool and library for generating regular expressions from user-provided test cases

> **Análise IA:** Genera regex a partir de test cases. Resuelve problema real (auto-generar patterns), útil para one-offs pero no es estándar de industria.

**Pontos fortes:** _Simplifica regex creation para non-experts_ · _Rust puro, performante_

**Tags:** `regex` `rust` `cli` `code-generation`

---

### [helix](https://github.com/helix-editor/helix)

![](https://img.shields.io/github/stars/helix-editor/helix?style=flat-square&label=⭐) · aparece em 2 listas

A post-modern modal text editor inspired by Neovim/Kakoune. [](https://github.com/helix-editor/helix/actions)

> **Análise IA:** Editor modal post-moderno en Rust. Inspirado en Vim/Neovim pero arquitectura limpia. Para devs que odian config bloated pero quieren modal editing out-of-box.

**Pontos fortes:** _Bindings sensatos por defecto vs Vim vanilla_ · _LSP integrado, zero-config para muchos lenguajes_

**Tags:** `editor` `rust` `modal` `cli`

---

### [httpie/httpie](https://github.com/httpie/httpie)

![](https://img.shields.io/github/stars/httpie/httpie?style=flat-square&label=⭐) · aparece em 2 listas

Description of what the project does. Demo screenshots. Project logo. TOC for easy navigation. Build badges. Quick and simple installation and usage sections. Includes an examples section.

> **Análise IA:** CLI HTTP client amigable para APIs REST. Reemplaza curl con sintaxis legible y coloreo automático. Excelente para desarrollo, testing manual y documentación de requests.

**Pontos fortes:** _Sintaxis intuitiva, salida formateada por defecto_ · _Instalación trivial, cero configuración inicial_

**Tags:** `cli` `http` `api-testing` `python`

---

### [Ideone](https://ideone.com)

aparece em 2 listas

An online compiler and debugging tool which allows you to compile source code and execute it online in more than 60 programming languages.

> **Análise IA:** Compilador online soporta 60+ lenguajes. Prototipado rápido, enseñanza, debugging sin setup local. No reemplaza IDE local pero indispensable para coding interviews y demostraciones.

**Pontos fortes:** _Cobertura 60+ lenguajes sin instalar_ · _URL shareable para collaboration_

**Tags:** `online-compiler` `pastebin` `coding-interview`

---

### [Infer](https://github.com/facebook/infer)

![](https://img.shields.io/github/stars/facebook/infer?style=flat-square&label=⭐) · aparece em 2 listas

Modern static analysis tool for verifying the correctness of code.

> **Análise IA:** Static analysis de Facebook para verificar correctitud: null pointers, data races, memory leaks. Para equipos que necesitan análisis automático profundo sin tuning excesivo.

**Pontos fortes:** _Detecta bugs reales que otros pierde (data races, leaks)_ · _Bajo ratio de false positives comparado con competition_

**Tags:** `static-analysis` `verification` `java` `c`

---

### [IterTools TS](https://github.com/smoren/itertools-ts)

![](https://img.shields.io/github/stars/smoren/itertools-ts?style=flat-square&label=⭐) · aparece em 2 listas

_(label: good first issue)_ <br> Extended itertools port for TypeScript and JavaScript. Provides a huge set of functions for working with iterable collections (including async ones).

> **Análise IA:** Colección extendida de funciones iterables (lazy, async) para TS/JS. Útil para procesamiento de streams complejos sin lodash.

**Pontos fortes:** _Soporte nativo de async iterables, raro en ecosistema JS_ · _Lazy evaluation evita materializar colecciones grandes_

**Tags:** `typescript` `javascript` `itertools` `functional`

---

### [JavaCpp](https://github.com/bytedeco/javacpp)

![](https://img.shields.io/github/stars/bytedeco/javacpp?style=flat-square&label=⭐) · aparece em 2 listas

The missing bridge between Java and native C++. [Apache2]

> **Análise IA:** Framework JNI robusto para invocar C++ desde Java. Para equipos que necesitan performance crítica desde JVM sin reescribir en C++. Mejor mantenimiento que JNI puro pero menos usado que SWIG.

**Pontos fortes:** _Sintaxis limpia respecto a JNI nativo_ · _Deployment simplificado con librerías precompiladas_

**Tags:** `jni` `java` `c++` `performance`

---

### [Joplin](https://joplinapp.org)

aparece em 2 listas

Note taking application with markdown editor and encryption support for mobile and desktop platforms. Runs client-side and syncs through a self hosted Nextcloud instance or similar (alternative to Evernote).

> **Análise IA:** App notas con markdown, encriptación, sync por Nextcloud/self-hosted. Open source, multi-plataforma. Alternativa Evernote con control total de datos.

**Pontos fortes:** _Sync descentralizado (Nextcloud), no vendor lock-in_ · _Encriptación end-to-end opcional integrada_

**Tags:** `note-taking` `markdown` `encryption` `self-hosted`

---

### [just](https://github.com/casey/just)

![](https://img.shields.io/github/stars/casey/just?style=flat-square&label=⭐) · aparece em 2 listas

A handy command runner for project-specific tasks

> **Análise IA:** Task runner moderno que reemplaza Makefiles. Define comandos en justfile, ejecuta localmente o en CI/CD. Útil para equipos que necesitan consistencia en workflows sin overhead.

**Pontos fortes:** _Sintaxis limpia y legible vs Makefiles_ · _Excelente integración en proyectos existentes sin cambiar estructura_

**Tags:** `task-runner` `cli` `rust`

---

### [Kaitai Struct](https://kaitai.io)

aparece em 2 listas

File formats and network protocols dissection language and web IDE, generating parsers in C++, C#, Java, JavaScript, Perl, PHP, Python, Ruby.

> **Análise IA:** DSL para parsear formatos binarios y protocolos. Genera parsers en 10+ lenguajes. Útil para reverse-engineering y trabajo con specs complejas.

**Pontos fortes:** _Generación automática de parsers multiplataforma desde spec única_ · _Web IDE integrada para testing interactivo_

**Tags:** `serialization` `parsing` `dsl` `code-generation` `binary-formats`

---

### [KDevelop](https://kdevelop.org)

aparece em 2 listas

IDE by the people behind KDE.

> **Análise IA:** IDE por los devs de KDE, enfocado en C++. Para proyectos Qt/KDE o C++ pesado. Similar a Visual Studio pero más liviano.

**Pontos fortes:** _Integración perfecta con Qt_ · _Debugger robusto, refactoring avanzado_

**Tags:** `ide` `cpp` `kde` `qt` `cross-platform`

---

### [kreuzberg](https://github.com/kreuzberg-dev/kreuzberg)

![](https://img.shields.io/github/stars/kreuzberg-dev/kreuzberg?style=flat-square&label=⭐) · aparece em 2 listas

High-performance document extraction library with a Rust core, supporting 62+ formats including PDF, Office, images with OCR, HTML, email, and archives.

> **Análise IA:** Librería Rust para extracción de documentos. Soporta 62+ formatos con OCR. Resuelve problema real: parsear documents heterogéneos sin invocar mil herramientas. Reciente, promisorio.

**Pontos fortes:** _Cobertura amplía de formatos en single library_ · _Núcleo Rust promete performance vs. tools basadas en Python/Java_

**Tags:** `rust` `document-parsing` `ocr` `pdf` `extraction`

---

### [LargeModGames/spotatui](https://github.com/largemodgames/spotatui)

![](https://img.shields.io/github/stars/largemodgames/spotatui?style=flat-square&label=⭐) · aparece em 2 listas

] - A Spotify terminal client with native streaming, synced lyrics, and real-time audio visualization [](https://github.com/LargeModGames/spotatui/actions/workflows/cd.yml)

> **Análise IA:** Cliente Spotify terminal en Rust con streaming nativo, lyrics sincronizados y visualización de audio en tiempo real. Útil para usuarios de terminal que quieren escapar de la GUI pesada. Resuelve problema real para el nicho.

**Pontos fortes:** _Streaming nativo sin dependencias externas pesadas_ · _Visualización de audio en vivo con baja latencia_

**Tags:** `rust` `cli` `spotify` `audio` `tui`

---

### [LINQPad](https://linqpad.net)

aparece em 2 listas

a C#/VB/F# scratchpad that instantly executes any expression, statement block or program with rich output formatting and a wealth of features. Also lets you interactively query databases in LINQ. [$]

> **Análise IA:** REPL interactivo para C#/VB/F#. Ejecuta código al instante, query LINQ against DBs. Pago. Herramienta niche pero potentísima para desarrolladores .NET explorando datos.

**Pontos fortes:** _Ejecución instant de C#, sin boilerplate_ · _LINQ queries directas contra DBs, debugging visual_

**Tags:** `csharp` `repl` `linq` `dotnet`

---

### [Linus-Mussmaecher/rucola](https://github.com/linus-mussmaecher/rucola)

![](https://img.shields.io/github/stars/linus-mussmaecher/rucola?style=flat-square&label=⭐) · aparece em 2 listas

Terminal-based markdown note manager. [](https://crates.io/crates/rucola-notes) [](https://github.com/Linus-Mussmaecher/rucola/actions/workflows/continuous-testing.yml)

> **Análise IA:** Note manager markdown en terminal, Rust. Para devs que viven en shell y rechazan Electron. Commits recientes, mantenido, resuelve problema real en su nicho.

**Pontos fortes:** _Escribir/organizar notas sin dejar terminal_ · _Rápido, sin dependencias pesadas_

**Tags:** `notes` `markdown` `rust` `tui`

---

### [LosslessCut](https://github.com/mifi/lossless-cut)

![](https://img.shields.io/github/stars/mifi/lossless-cut?style=flat-square&label=⭐) · aparece em 2 listas

Cross platform tool for quick and lossless video and audio trimming using ffmpeg. [![Open-Source Software][OSS Icon] ![Freeware][Freeware Icon]](https://github.com/mifi/lossless-cut)

> **Análise IA:** Herramienta ligera para trimming de video/audio sin recodificación. Usa FFmpeg backend. Ideal para edición rápida no destructiva. Resuelve el problema real de cortar archivos multimedia sin perder calidad.

**Pontos fortes:** _Lossless cutting sin recodificar_ · _Interfaz simple y responsiva_

**Tags:** `ffmpeg` `video-editing` `cross-platform` `cli-gui`

---

### [Mailpit](https://github.com/axllent/mailpit)

![](https://img.shields.io/github/stars/axllent/mailpit?style=flat-square&label=⭐) · aparece em 2 listas

An email and SMTP testing tool for developers.

> **Análise IA:** SMTP mock server en Go para testing email. Ligero, rápido, con web UI. Estándar para dev loops que requieren testing de emails sin spam real.

**Pontos fortes:** _Binario único, cero dependencias_ · _Web UI limpia para inspeccionar mails_

**Tags:** `smtp` `testing` `go` `email` `dev-tools`

---

### [Mailspring](https://getmailspring.com)

aparece em 2 listas

A beautiful, fast, and fully open source mail client. [![Open-Source Software][OSS Icon]](https://github.com/Foundry376/Mailspring) ![Freeware][Freeware Icon]

> **Análise IA:** Cliente email open-source, cross-platform, bonito y rápido. Alternativa viable a Thunderbird/Apple Mail. Soporte activo, comunidad en crecimiento.

**Pontos fortes:** _Diseño moderno y UX pulido_ · _Desarrollo activo con releases regulares_

**Tags:** `email` `open-source` `cross-platform` `electron` `mail-client`

---

### [Marimo](https://github.com/marimo-team/marimo)

![](https://img.shields.io/github/stars/marimo-team/marimo?style=flat-square&label=⭐) · aparece em 2 listas

- Reactive Python notebook — run reproducible experiments, execute as a script, deploy as an app, and version with git.

> **Análise IA:** Notebook Python reactivo, ejecutable como script y deployable como web app. Versionable con git. Alternativa moderna a Jupyter.

**Pontos fortes:** _Reactividad automática (no kernel async confuso)_ · _Export a script y app web sin cambios de código_

**Tags:** `notebook` `python` `reactive` `git-friendly`

---

### [MarkText](https://github.com/marktext/marktext)

![](https://img.shields.io/github/stars/marktext/marktext?style=flat-square&label=⭐) · aparece em 2 listas

Next generation markdown editor, running on platforms of MacOS Windows and Linux. [![Open-Source Software][OSS Icon]](https://github.com/marktext/marktext) ![Freeware][Freeware Icon]

> **Análise IA:** Editor markdown generacional con WYSIWYG fluido, exporta a HTML/PDF. Cross-platform (Electron). Freeware activo. Ideal para escritura técnica/notas, no para código.

**Pontos fortes:** _Preview en vivo impecable, UX intuitiva para no-devs_ · _Export múltiples formatos, themes customizables_

**Tags:** `markdown` `wysiwyg` `electron` `cross-platform` `freeware`

---

### [micro](https://micro-editor.github.io)

aparece em 2 listas

Modern and intuitive terminal-based text editor. [![Open-Source Software][OSS Icon]](https://github.com/ory/editor) ![Freeware][Freeware Icon]

> **Análise IA:** Editor terminal minimalista, moderno. Alternativa ligera a Vim/Neovim con syntax highlighting decente. Bueno si querés algo sin config inicial agobiante.

**Pontos fortes:** _Setup zero-config, intuitivo para usuarios que vienen de VS Code_ · _Muy rápido, footprint bajo_

**Tags:** `terminal-editor` `golang` `cli` `lightweight`

---

### [microsoft/markitdown](https://github.com/microsoft/markitdown)

![](https://img.shields.io/github/stars/microsoft/markitdown?style=flat-square&label=⭐) · aparece em 2 listas

🎖️ 🐍 🏠 - MCP tool access to MarkItDown -- a library that converts many file formats (local or remote) to Markdown for LLM consumption.

> **Análise IA:** MCP tool que expone MarkItDown (convierte archivos a Markdown). Útil para LLMs consumiendo documents variados. Buena idea pero implementación MCP=early, adoption incierta.

**Pontos fortes:** _Conversión multi-formato (PDF, DOCX, Excel, images) a Markdown_ · _Microsoft backing, mantenimiento activo_

**Tags:** `python` `mcp` `markdown-conversion` `llm-tools` `multi-format`

---

### [Mockoon](https://mockoon.com)

aparece em 2 listas

Create mock APIs in seconds. [![Open-Source Software][OSS Icon]](https://github.com/mockoon/mockoon)

> **Análise IA:** Mock server OSS sin setup. Genera endpoints fake en segundos, JSON/YAML config. Perfecto para frontend dev y testing sin backend. UI clara, respuestas customizables.

**Pontos fortes:** _Zero-config mocking, UI intuitiva_ · _Exporta requests/responses, compatible con Postman_

**Tags:** `mock-api` `testing` `http-server` `oss`

---

### [.NET Interactive](https://github.com/dotnet/interactive)

![](https://img.shields.io/github/stars/dotnet/interactive?style=flat-square&label=⭐) · aparece em 2 listas

- .NET Interactive takes the power of .NET and embeds it into your interactive experiences.

> **Análise IA:** .NET embebido en notebooks/REPL interactivos. Para data scientists .NET-istas prototipando, teaching. Buena integración con Jupyter pero ecosistema fragmentado.

**Pontos fortes:** _Integración nativa con C# type-safety en notebooks_ · _Soporte para Markdown + visualización inline_

**Tags:** `dotnet` `repl` `interactive` `jupyter` `notebook`

---

### [nuklear](https://github.com/immediate-mode-ui/nuklear)

![](https://img.shields.io/github/stars/immediate-mode-ui/nuklear?style=flat-square&label=⭐) · aparece em 2 listas

A single-header ANSI C gui library. [PublicDomain]

> **Análise IA:** Single-header GUI en C puro con immediate-mode. Bueno para tools internas, game UI, prototipado rápido. Curva corta, flexible.

**Pontos fortes:** _Archivo único, sin dependencias externas_ · _Paradigma immediate-mode es rápido para UIs dinámicas_

**Tags:** `gui` `c` `single-header` `immediate-mode` `lightweight`

---

### [nushell](https://github.com/nushell/nushell)

![](https://img.shields.io/github/stars/nushell/nushell?style=flat-square&label=⭐) · aparece em 2 listas

_(label: good first issue)_ <br> A modern shell for the GitHub era written in Rust.

> **Análise IA:** Shell moderno en Rust con piping estructurado y sintaxis mejorada. Para devs que quieren escapar de bash/zsh. Resuelve legibilidad y seguridad de scripts.

**Pontos fortes:** _Piping de estructuras (JSON, tablas) nativo sin conversión_ · _Sintaxis limpia y debugging intuitivo vs bash arcano_

**Tags:** `rust` `shell` `cli` `unix`

---

### [OneCompiler](https://onecompiler.com)

aparece em 2 listas

A free AI Powered online compiler supporting over 70 languages, including Java, Python, MySQL, C++, and HTML, for writing, running, and sharing code.

> **Análise IA:** Compilador web con 70+ lenguajes, UI intuitiva, comparte snippets. Prototipado rápido sin instalación. Pero 'AI Powered' es marketing; no resuelve problemas serios, latencia variable.

**Pontos fortes:** _Cero setup, 70+ idiomas_ · _Compartir código via link directo_

**Tags:** `online-ide` `web-compiler` `multi-language` `prototyping`

---

### [OpenLayers3](https://openlayers.org)

aparece em 2 listas

A high-performance, feature-packed library for all your mapping needs.

> **Análise IA:** Librería open-source para mapas web con performance destacado. Competidor directo de Leaflet/Mapbox. Usado en GIS serio y aplicaciones geo de escala.

**Pontos fortes:** _Performance en datasets geoespaciales grandes_ · _Soporte nativo para múltiples formatos (WMS, WFS, etc)_

**Tags:** `maps` `gis` `javascript` `geospatial`

---

### [quick-look-plugins](https://github.com/sindresorhus/quick-look-plugins)

![](https://img.shields.io/github/stars/sindresorhus/quick-look-plugins?style=flat-square&label=⭐) · aparece em 2 listas

List of useful [Quick Look](https://en.wikipedia.org/wiki/Quick_Look) plugins for developers

> **Análise IA:** Listado curatorado de plugins para Quick Look (visor nativo macOS). No es una herramienta sino un repositorio de referencias. Útil si estás en macOS y querés extender el visor de archivos, niche muy específico.

**Pontos fortes:** _Mantenida por Sindre Sorhus (creíble), cubre use case específico bien_

**Tags:** `quicklook` `macos` `plugins` `curated-list`

---

### [readme-md-generator](https://github.com/kefranabg/readme-md-generator)

![](https://img.shields.io/github/stars/kefranabg/readme-md-generator?style=flat-square&label=⭐) · aparece em 2 listas

A CLI that generates beautiful README.md files

> **Análise IA:** CLI que genera README.md bonitos con secciones estándar. Acelera boilerplate inicial pero requiere completar a mano contenido específico del proyecto.

**Pontos fortes:** _Genera README completo en segundos, estructura coherente_ · _Interactivo: guía paso a paso sin leer docs_

**Tags:** `cli` `documentation` `nodejs`

---

### [RepoFlow](https://repoflow.io)

aparece em 2 listas

A simple and easy-to-use package management platform with Docker support alongside other formats like PyPI, Maven, npm, and Helm. Includes smart search, built-in Docker image scanning, and a great free option for both self-hosted and cloud use.

> **Análise IA:** Plataforma de registros de paquetes multi-formato con Docker scanning integrado. Para equipos que necesitan control centralizado de artefactos. Resuelve fragmentación de repos privados.

**Pontos fortes:** _Soporte multi-formato (Docker, PyPI, Maven, npm, Helm) en una sola solución_ · _Scanning de vulnerabilidades en imágenes Docker incluido_

**Tags:** `package-registry` `docker` `self-hosted` `saas`

---

### [Retext](https://github.com/retextjs/retext)

![](https://img.shields.io/github/stars/retextjs/retext?style=flat-square&label=⭐) · aparece em 2 listas

Extensible system for analyzing and manipulating natural language.

> **Análise IA:** Sistema extensible para análisis y manipulación de texto en JavaScript. Plugin-based, bien diseñado. Mejor alternativa que 'natural' para NLP en Node pero menos powerful que spaCy.

**Pontos fortes:** _Arquitectura extensible con plugins, muy modular_ · _API moderna y clara para procesamiento de texto_

**Tags:** `javascript` `nodejs` `nlp` `text-processing` `plugins`

---

### [RustRover](https://jetbrains.com/rust)

aparece em 2 listas

A powerful Rust IDE by JetBrains, free for individual non-commercial use

> **Análise IA:** IDE Rust by JetBrains con análisis, debugging, refactoring. Freemium para no-comercial. Para desarrolladores Rust que quieren IDE polished con intellisense robusto.

**Pontos fortes:** _Intellisense y refactoring superior a VS Code + extensiones_ · _Debugging integrado sin configuración compleja_

**Tags:** `ide` `rust` `jetbrains` `debugger`

---

### [scc](https://github.com/boyter/scc)

![](https://img.shields.io/github/stars/boyter/scc?style=flat-square&label=⭐) · aparece em 2 listas

Sloc Cloc and Code, a very fast accurate code counter with complexity calculations and COCOMO estimates.

> **Análise IA:** Contador de líneas de código ultra-rápido con análisis de complejidad y COCOMO. Reemplazo moderno de cloc. Para auditorías y métricas de codebase.

**Pontos fortes:** _Velocidad extrema (scans millones LOC)_ · _Múltiples lenguajes, salida flexible_

**Tags:** `code-metrics` `golang` `cli` `sloc`

---

### [script](https://github.com/bitfield/script)

![](https://img.shields.io/github/stars/bitfield/script?style=flat-square&label=⭐) · aparece em 2 listas

_(label: good first issue)_ <br> A Go library for doing the kind of tasks that shell scripts are good at: reading files, executing subprocesses, counting lines, matching strings, and so on. Beginners are very welcome and will get detailed code review and help through the PR process.

> **Análise IA:** Librería Go para tareas de shell scripting: lectura de archivos, subprocesos, conteo de líneas, pattern matching. Buena para automatización simple en Go, comunidad abierta a principiantes.

**Pontos fortes:** _API limpia para tareas comunes de shell_ · _Comunidad receptiva con code review detallado_

**Tags:** `go` `scripting` `shell` `io` `subprocess`

---

### [slint-ui/slint](https://github.com/slint-ui/slint)

![](https://img.shields.io/github/stars/slint-ui/slint?style=flat-square&label=⭐) · aparece em 2 listas

[Slint](https://slint.dev/) is a toolkit to efficiently develop fluid graphical user interfaces for embedded devices and desktop applications. [](https://github.com/slint-ui/slint/actions?query=workflow%3ACI)

> **Análise IA:** Toolkit GUI moderno basado en Rust/C++ para embedded y desktop. Genera código nativo eficiente. Alternativa contemporánea a Qt con menos bloat.

**Pontos fortes:** _Performance nativa y compilación anticipada sin runtime pesado_ · _DSL declarativo intuitivo para diseño de UIs_

**Tags:** `gui` `rust` `embedded` `cross-platform` `modern`

---

### [Spack](https://spack.io)

aparece em 2 listas

A flexible package manager that supports multiple versions, configurations, platforms, and compilers.

> **Análise IA:** Package manager flexible para HPC/científico con soporte multi-versión y compiladores. Para labs/investigadores con dependencias complejas en múltiples plataformas.

**Pontos fortes:** _Soporte nativo de múltiples versiones y compiladores en paralelo_ · _Reproducibilidad garantizada en clusters_

**Tags:** `package-manager` `hpc` `python` `multi-version`

---

### [Sphinx](https://github.com/sphinx-doc/sphinx)

![](https://img.shields.io/github/stars/sphinx-doc/sphinx?style=flat-square&label=⭐) · aparece em 2 listas

Sphinx makes it easy to create intelligent and beautiful documentation. [BSD-2-Clause] [website](https://www.sphinx-doc.org)

> **Análise IA:** Generador de documentación para Python/reStructuredText. Estándar para docs Python (Django, numpy, scipy). Madura pero pesada vs Mkdocs moderno.

**Pontos fortes:** _Integración automática de docstrings Python_ · _Extensibilidad vía plugins_

**Tags:** `documentation` `rst` `static-site` `python`

---

### [tauri-apps/tauri](https://github.com/tauri-apps/tauri)

![](https://img.shields.io/github/stars/tauri-apps/tauri?style=flat-square&label=⭐) · aparece em 2 listas

Build smaller, faster, and more secure desktop applications with a web frontend, powered by [WRY](https://github.com/tauri-apps/wry). [](https://github.com/tauri-apps/tauri/actions?query=workflow%3A%22test+library%22)

> **Análise IA:** Framework desktop Rust + web frontend (HTML/CSS/JS). Bundle compacto, seguro, rendimiento nativo. Actualmente la mejor opción vs Electron para minimizar footprint. Comunidad crece.

**Pontos fortes:** _Bundle 15-50MB vs 150+ Electron_ · _Memory-safe por diseño Rust_

**Tags:** `rust` `desktop` `web-frontend` `cross-platform`

---

### [television](https://github.com/alexpasmantier/television)

![](https://img.shields.io/github/stars/alexpasmantier/television?style=flat-square&label=⭐) · aparece em 2 listas

A blazing fast general purpose fuzzy finder TUI

> **Análise IA:** Fuzzy finder TUI escrito en Rust. Alternativa a fzf pero general purpose. Para devs que pasan tiempo en terminal. Resuelve búsqueda rápida de cualquier cosa.

**Pontos fortes:** _Blazing fast, lag-free en datasets enormes_ · _Respeta stdin/stdout, compone bien en pipes_

**Tags:** `rust` `cli` `tui` `fuzzy-search` `performance`

---

### [Termius](https://termius.com)

aparece em 2 listas

A beautiful SSH and SFTP client for Mac. It is also available for mobile. ![Freeware][Freeware Icon] [![App Store][app-store Icon]](https://apps.apple.com/us/app/termius-terminal-ssh-client/id549039908?platform=mac)

> **Análise IA:** Cliente SSH/SFTP multiplataforma con UI pulida. Resuelve necesidad real de terminal remota con UX superior a openssh crudo. Gratis pero propietario.

**Pontos fortes:** _Interfaz moderna y polida vs alternativas CLI puras_ · _Soporte multiplataforma incluyendo iOS/Android_

**Tags:** `ssh` `sftp` `terminal` `mac` `mobile`

---

### [Typora](https://typora.io)

aparece em 2 listas

Truly minimal Markdown editor featuring seamless live preview.

> **Análise IA:** Editor Markdown minimalista con preview en vivo sincronizado. Para escritores técnicos y documentalistas que odian distracciones. Resuelve bien: escribir sin fricciones.

**Pontos fortes:** _Preview en vivo verdaderamente fluido_ · _UI limpia sin botonería innecesaria_

**Tags:** `markdown` `editor` `minimal` `wysiwyg`

---

### [Vectr](https://vectr.com)

aparece em 2 listas

Vectr is a free graphics software used to create vector graphics easily and intuitively. It's a simple yet powerful web and desktop cross-platform tool to bring your designs into reality.

> **Análise IA:** Editor gráfico vectorial web/desktop gratuito. Simple, intuitivo, para diseños básicos. Compite con Inkscape, Figma, Illustrator.

**Pontos fortes:** _Acceso web + desktop, gratis sin limitaciones_ · _Interfaz intuitiva para principiantes_

**Tags:** `vector-graphics` `design` `free` `web-desktop`

---

### [Warp](https://warp.dev)

aparece em 2 listas

Warp is a blazingly fast, rust-based terminal reimagined from the ground up to work like a modern app.

> **Análise IA:** Terminal Rust con UX tipo app moderna. Promete velocidad y features como búsqueda, autocompletado. Competidor directo de iTerm2, Alacritty, Terminal.app.

**Pontos fortes:** _Escrito en Rust, performance real_ · _UX pensada como app moderna, no como emulador retro_

**Tags:** `terminal` `rust` `cli` `cross-platform`

---

### [Water-Run/treepp](https://github.com/water-run/treepp)

![](https://img.shields.io/github/stars/water-run/treepp?style=flat-square&label=⭐) · aparece em 2 listas

A Rust-based native Windows `tree` replacement with diff-level input/output compatibility on successful runs, many more features including essential exclusions and `.gitignore` support, and several-times faster performance.

> **Análise IA:** Reemplazo nativo de `tree` para Windows en Rust. Soporta exclusiones y .gitignore, más rápido. Específico para Windows, pero resuelve un problema real.

**Pontos fortes:** _Performance significativa vs tree nativo Windows_ · _Soporte .gitignore native_

**Tags:** `rust` `windows` `cli` `file-tree`

---

### [xplr](https://github.com/sayanarijit/xplr)

![](https://img.shields.io/github/stars/sayanarijit/xplr?style=flat-square&label=⭐) · aparece em 2 listas

A hackable, minimal, fast TUI file explorer.

> **Análise IA:** File explorer TUI minimalista y hackable en Rust. Para usuarios que quieren personalización extrema y performance. Resuelve la necesidad de navegación de archivos sin bloat.

**Pontos fortes:** _Arquitectura modular permite extensiones vía Lua_ · _Extremadamente ligero, startup instantáneo_

**Tags:** `rust` `tui` `file-manager` `hackable`

---

### [yazi](https://github.com/sxyazi/yazi)

![](https://img.shields.io/github/stars/sxyazi/yazi?style=flat-square&label=⭐) · aparece em 2 listas

Blazing fast terminal file manager, based on async I/O.

> **Análise IA:** File manager TUI en Rust con async I/O nativa. Para terminals pesadas. Compite directo con xplr/lf pero con mejor performance en operaciones I/O grandes.

**Pontos fortes:** _Async I/O real evita bloqueos en carpetas grandes_ · _Integración mouse y preview nativa en terminal_

**Tags:** `rust` `tui` `async` `file-manager`

---


---

<sub>📄 Gerado automaticamente de [juanchi.dev](https://juanchi.dev) · [código do sistema](https://juanchi.dev/blog/series/awesome-curated) · MIT licensed</sub>
