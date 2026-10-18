<div align="center">

# 🎯 Awesome Curated

Leer en otros idiomas: [🇬🇧 English](README.md) · **🇪🇸 Español** · [🇧🇷 Português (BR)](README.pt-BR.md) · [🇨🇳 中文](README.zh-CN.md) · [🇯🇵 日本語](README.ja.md)

### Un **radar semanal** de herramientas dev encontradas en repos `awesome-*` activos, con trazas de fuentes y una selección revisada por humano.

[![Human Picks](https://img.shields.io/badge/Human_Picks-5-gold?style=for-the-badge)](#human-reviewed-picks)
[![Sources](https://img.shields.io/badge/Sources-20-purple?style=for-the-badge)](SOURCES.md)
[![Updated](https://img.shields.io/badge/Updated-2026-10-18-green?style=for-the-badge)](UPDATE-SUMMARY.md)
[![Evidence](https://img.shields.io/badge/Evidence-public_snapshot-blue?style=for-the-badge)](data/latest.json)
[![License](https://img.shields.io/badge/License-MIT-blue?style=for-the-badge)](LICENSE)

</div>

---

## Empezá por un problema

| Tarea | Herramienta | Probala |
|---|---|---|
| Buscar y reescribir código | [ast-grep](https://github.com/ast-grep/ast-grep) · Worth Trying | [Probala](GUIDE.es.md#ast-grep) |
| Validar un formulario | [Vest](https://github.com/ealush/vest) · Worth Trying | [Probala](GUIDE.es.md#vest) |
| Inspeccionar un modelo | [Netron](https://github.com/lutzroeder/netron) · Human Pick | [Probala](GUIDE.es.md#netron) |

[Ejemplos reproducibles](GUIDE.es.md) · Inglés / español · versiones fijas, datos de prueba, resultados y límites. Las pruebas automatizadas no cambian los veredictos.

### Un resultado antes de instalar

**Antes**

```js
// console.log("comment")
const text = "console.log(123)";
console.log("hello");
```

**Después**

```js
// console.log("comment")
const text = "console.log(123)";
logger.info("hello");
```

ast-grep 0.51.0 reescribe una llamada JavaScript; el comentario y el string quedan iguales. Se comprueba la sintaxis, no que cambiar el logger conserve el comportamiento de la aplicación. [Probala](GUIDE.es.md#ast-grep).

---

## ⭐ Guardalo para después

¿Te sirvió alguno de los ejemplos? Guardá el [repo](https://github.com/JuanTorchia/awesome-curated) con una ⭐ para volver a las versiones, los resultados esperados y los límites de cada caso. [Ver qué cambió](UPDATE-SUMMARY.md).

### Snapshot de confianza

- **Última actualización generada**: 2026-10-18
- **fuentes activas**: 20
- **Human Picks**: 5
- **Metodología**: [METHODOLOGY.md](METHODOLOGY.md)
- **Fuentes rastreadas**: [SOURCES.md](SOURCES.md)
- **Resumen de cambios**: [UPDATE-SUMMARY.md](UPDATE-SUMMARY.md)
- **Snapshot de evidencia**: [data/latest.json](data/latest.json)
- **Catálogo consultable**: [TOOLS.md](TOOLS.md)
- **Estándares populares**: 1
- **Estado Needs Review (revisar trazas)**: 0
- **AI Candidates pendientes de aval humano**: 229
- Los candidatos no tienen el aval de Juan. Consultá el catálogo y las páginas por dominio.

---

## 🗺️ Encontrá tu stack

[🌐 **Web** · 11](domains/web.es.md) · [🤖 **IA y ML** · 79](domains/ai-ml.es.md) · [🛠️ **DevOps** · 12](domains/devops.es.md) · [📱 **Mobile** · 1](domains/mobile.es.md) · [💾 **Datos y Bases** · 45](domains/data.es.md) · [🔐 **Seguridad y Cripto** · 9](domains/security.es.md) · [⚡ **Performance** · 3](domains/performance.es.md) · [🧰 **Herramientas Dev** · 75](domains/tooling.es.md) · [🎨 **Otros** · 11](domains/other.es.md)

---

<a id="human-reviewed-picks"></a>

## ⭐ Selección revisada por humano

Herramientas revisadas por humano y las tareas que ayudan a resolver.

<!-- staff-picks:start -->
### 👤 [BayesWitnesses/m2cgen](https://github.com/bayeswitnesses/m2cgen)

<!-- pick:rationale -->

**Por qué importa:** Elimina dependencias de runtime de ML en producción: el código generado es nativo y standalone.

<!-- pick:evidence -->

**Evidencia:** Encontrada en 4 fuentes activas: rust-unofficial/awesome-rust, fffaraz/awesome-cpp, josephmisiti/awesome-machine-learning +1 more · [trazas](data/latest.json)

<!-- pick:review -->

**Revisión:** Human Pick

<!-- pick:caveat -->

**Nota / revisión:** Más adecuada para equipos con un flujo de ML o datos compatible.

### 👤 [Netron](https://github.com/lutzroeder/netron)

<!-- pick:rationale -->

**Por qué importa:** Visualizador práctico de modelos ML con soporte amplio para formatos como ONNX, TensorFlow y PyTorch.

<!-- pick:evidence -->

**Evidencia:** Encontrada en 3 fuentes activas: EthicalML/awesome-production-machine-learning, academic/awesome-datascience, josephmisiti/awesome-machine-learning · [trazas](data/latest.json)

<!-- pick:review -->

**Revisión:** Human Pick

<!-- pick:caveat -->

**Nota / revisión:** Más adecuada para equipos con un flujo de ML o datos compatible.

### 👤 [Sniffnet](https://github.com/gyulyvgc/sniffnet)

<!-- pick:rationale -->

**Por qué importa:** Monitor de tráfico de red multiplataforma con UI accesible para debugging y seguridad sin fricción.

<!-- pick:evidence -->

**Evidencia:** Encontrada en 3 fuentes activas: rust-unofficial/awesome-rust, jaywcjlove/awesome-mac, MunGell/awesome-for-beginners · [trazas](data/latest.json)

<!-- pick:review -->

**Revisión:** Human Pick

<!-- pick:caveat -->

**Nota / revisión:** Conviene hacer una prueba acotada antes de una adopción amplia.

### 👤 [themis](https://github.com/cossacklabs/themis)

<!-- pick:rationale -->

**Por qué importa:** API de alto nivel sobre primitivas criptográficas para evitar partir de componentes básicos.

<!-- pick:evidence -->

**Evidencia:** Encontrada en 3 fuentes activas: rust-unofficial/awesome-rust, fffaraz/awesome-cpp, avelino/awesome-go · [trazas](data/latest.json)

<!-- pick:review -->

**Revisión:** Human Pick

<!-- pick:caveat -->

**Nota / revisión:** Herramienta sensible para la seguridad: evaluá su adecuación y mantenimiento antes de usarla en producción.

### 👤 [Bencher](https://bencher.dev)

<!-- pick:rationale -->

**Por qué importa:** Continuous benchmarking para detectar regresiones de performance en CI/CD con umbrales configurables.

<!-- pick:evidence -->

**Evidencia:** Encontrada en 2 fuentes activas: fffaraz/awesome-cpp, avelino/awesome-go · [trazas](data/latest.json)

<!-- pick:review -->

**Revisión:** Human Pick

<!-- pick:caveat -->

**Nota / revisión:** La cobertura entre fuentes es limitada.
<!-- staff-picks:end -->

---

## Candidatos para revisión humana

- [yt-dlp](https://github.com/yt-dlp/yt-dlp) — Dev Tooling · Found in 3 active sources: agarrharr/awesome-cli-apps, jivoi/awesome-osint, vinta/awesome-python
- [Deepchecks](https://github.com/deepchecks/deepchecks) — AI & ML · Found in 3 active sources: EthicalML/awesome-production-machine-learning, academic/awesome-datascience, josephmisiti/awesome-machine-learning
- [Colossal-AI](https://github.com/hpcaitech/colossalai) — Dev Tooling · Found in 3 active sources: EthicalML/awesome-production-machine-learning, josephmisiti/awesome-machine-learning, MunGell/awesome-for-beginners
- [Feature Engine](https://github.com/feature-engine/feature_engine) — AI & ML · Found in 3 active sources: EthicalML/awesome-production-machine-learning, josephmisiti/awesome-machine-learning, vinta/awesome-python
- [askbudi/roundtable](https://github.com/askbudi/roundtable) — AI & ML · Found in 2 active sources: vuejs/awesome-vue, punkpeye/awesome-mcp-servers

Los candidatos no son recomendaciones personales. Pedí revisión mediante GitHub issues o consultá la cola completa en TOOLS.md. [GitHub issues](https://github.com/JuanTorchia/awesome-curated/issues/new/choose) · [TOOLS.md](TOOLS.md)

---

## ⭐ Picks revisados y candidatos por dominio

### 🌐 Web

| Tool | Qué hace | Señal |
|---|---|---|
| 👤 [**Vest**](https://github.com/ealush/vest) | Validations framework inspired by unit testing frameworks. | Found in 2 active sources: vuejs/awesome-vue, MunGell/awesome-for-beginners · Worth Trying |
| [**D3js**](https://d3js.org) | is a powerful data visualization javascript library. | Found in 2 active sources: jivoi/awesome-osint, academic/awesome-datascience · AI Candidate |
| [**grpc**](https://github.com/grpc/grpc) | Remote Procedure Calls (RPCs) provide a useful abstraction for building distributed applications and services. The... | Found in 2 active sources: fffaraz/awesome-cpp, vinta/awesome-python · AI Candidate |

📖 8 más en la [página detallada →](domains/web.es.md)

### 🤖 IA y ML

| Tool | Qué hace | Señal |
|---|---|---|
| 👤 [**BayesWitnesses/m2cgen**](https://github.com/bayeswitnesses/m2cgen) | A CLI tool to transpile trained classic machine learning models into a native Rust code with zero dependencies. | Found in 4 active sources: rust-unofficial/awesome-rust, fffaraz/awesome-cpp, josephmisiti/awesome-machine-learning +1 more · Human Pick |
| 👤 [**Netron**](https://github.com/lutzroeder/netron) | Netron is a viewer for neural network, deep learning and machine learning models. | Found in 3 active sources: EthicalML/awesome-production-machine-learning, academic/awesome-datascience, josephmisiti/awesome-machine-learning · Human Pick |
| 👤 [**Mem0**](https://github.com/mem0ai/mem0) | Mem0 enhances AI assistants and agents with an intelligent memory layer, enabling personalized AI interactions. | Found in 3 active sources: EthicalML/awesome-production-machine-learning, vinta/awesome-python, MunGell/awesome-for-beginners · Worth Trying |

📖 76 más en la [página detallada →](domains/ai-ml.es.md)

### 🛠️ DevOps

| Tool | Qué hace | Señal |
|---|---|---|
| 👤 [**bandwhich**](https://github.com/imsnif/bandwhich) | Track bandwidth utilization by process. | Found in 2 active sources: agarrharr/awesome-cli-apps, rust-unofficial/awesome-rust · Worth Trying |
| [**BorgBackup**](https://github.com/borgbackup/borg) | Deduplicating backup program with compression and authenticated encryption. | Found in 2 active sources: vinta/awesome-python, MunGell/awesome-for-beginners · AI Candidate |
| [**ctop**](https://github.com/bcicen/ctop) | interface (e.g. htop) for container metrics. | Found in 2 active sources: agarrharr/awesome-cli-apps, avelino/awesome-go · AI Candidate |

📖 9 más en la [página detallada →](domains/devops.es.md)

### 📱 Mobile

| Tool | Qué hace | Señal |
|---|---|---|
| [**RunAnywhere**](https://github.com/runanywhereai/runanywhere-sdks) | RunAnywhere is a production-ready SDK for running AI models (LLMs, speech-to-text, text-to-speech) on-device for... | Found in 2 active sources: EthicalML/awesome-production-machine-learning, josephmisiti/awesome-machine-learning · AI Candidate |

📖 [Página completa del dominio →](domains/mobile.es.md)

### 💾 Datos y Bases

| Tool | Qué hace | Señal |
|---|---|---|
| [**gradio**](https://github.com/gradio-app/gradio) | Quickly create and share demos of models by only writing Python. Debug models interactively in your browser, get... | Found in 3 active sources: EthicalML/awesome-production-machine-learning, josephmisiti/awesome-machine-learning, vinta/awesome-python · AI Candidate |
| [**matplotlib**](https://github.com/matplotlib/matplotlib) | A Python 2D plotting library which produces publication-quality figures in a variety of hardcopy formats and... | Found in 3 active sources: EthicalML/awesome-production-machine-learning, vinta/awesome-python, MunGell/awesome-for-beginners · AI Candidate |
| [**Streamlit**](https://github.com/streamlit/streamlit) | Streamlit lets you create apps for your machine learning projects with deceptively simple Python scripts. It... | Found in 3 active sources: EthicalML/awesome-production-machine-learning, josephmisiti/awesome-machine-learning, vinta/awesome-python · AI Candidate |

📖 42 más en la [página detallada →](domains/data.es.md)

### 🔐 Seguridad y Cripto

| Tool | Qué hace | Señal |
|---|---|---|
| 👤 [**themis**](https://github.com/cossacklabs/themis) | High level crypto library for storing data (AES), secure messaging (ECC + ECDSA / RSA + PSS + PKCS#7) and... | Found in 3 active sources: rust-unofficial/awesome-rust, fffaraz/awesome-cpp, avelino/awesome-go · Human Pick |
| [**Brave**](https://brave.com) | Web browser with an emphasis on privacy and speed. (https://github.com/brave/brave-browser/) | Found in 2 active sources: jivoi/awesome-osint, jaywcjlove/awesome-mac · AI Candidate |
| [**LibreWolf**](https://librewolf.net) | A fork of Firefox, focused on privacy, security and freedom. (https://gitlab.com/librewolf-community) | Found in 2 active sources: jivoi/awesome-osint, jaywcjlove/awesome-mac · AI Candidate |

📖 6 más en la [página detallada →](domains/security.es.md)

### ⚡ Performance

| Tool | Qué hace | Señal |
|---|---|---|
| 👤 [**Bencher**](https://bencher.dev) | Suite of continuous benchmarking tools designed to catch performance regressions in CI. MIT/Apache-2.0 Rust | Found in 2 active sources: fffaraz/awesome-cpp, avelino/awesome-go · Human Pick |
| [**Cython**](https://github.com/cython/cython) | Cython is an optimising static compiler for both the Python programming language and the extended Cython programming... | Found in 2 active sources: fffaraz/awesome-cpp, vinta/awesome-python · AI Candidate |
| [**Numba**](https://github.com/numba/numba) | A compiler for Python array and numerical functions. | Found in 2 active sources: EthicalML/awesome-production-machine-learning, vinta/awesome-python · AI Candidate |

📖 [Página completa del dominio →](domains/performance.es.md)

### 🧰 Herramientas Dev

| Tool | Qué hace | Señal |
|---|---|---|
| 👤 [**Sniffnet**](https://github.com/gyulyvgc/sniffnet) | Cross-platform application to monitor your network traffic with ease | Found in 3 active sources: rust-unofficial/awesome-rust, jaywcjlove/awesome-mac, MunGell/awesome-for-beginners · Human Pick |
| 👤 [**ast-grep**](https://github.com/ast-grep/ast-grep) | A CLI tool for code structural search, lint and rewriting. | Found in 2 active sources: agarrharr/awesome-cli-apps, rust-unofficial/awesome-rust · Worth Trying |
| 👤 [**ATAC**](https://github.com/julien-cpsn/atac) | A feature-full TUI API client made in Rust. ATAC is free, open-source, offline and account-less. | Found in 2 active sources: agarrharr/awesome-cli-apps, rust-unofficial/awesome-rust · Worth Trying |

📖 72 más en la [página detallada →](domains/tooling.es.md)

### 🎨 Otros

| Tool | Qué hace | Señal |
|---|---|---|
| [**AI Job Displacement Tracker**](https://github.com/noahaust2/ai-displacement-tracker) | Structured, source-backed dataset tracking 96 AI-attributed workforce reductions (457K workers affected, 13... | Found in 2 active sources: EthicalML/awesome-production-machine-learning, academic/awesome-datascience · AI Candidate |
| [**beets**](https://github.com/beetbox/beets) | A music library manager and MusicBrainz tagger. | Found in 2 active sources: agarrharr/awesome-cli-apps, vinta/awesome-python · AI Candidate |
| [**croc**](https://github.com/schollz/croc) | Easily and securely send files or folders from one computer to another. | Found in 2 active sources: agarrharr/awesome-cli-apps, avelino/awesome-go · AI Candidate |

📖 8 más en la [página detallada →](domains/other.es.md)

---

## 🎯 Cómo se curó

1. **Discovery**: GitHub API (GraphQL batched) detecta repos `awesome-*` mantenidos activamente.
2. **Scoring multidimensional**: freshness, actividad, popularidad, profundidad y salud de la comunidad ponderados en un único score.
3. **Evidencia de fuentes**: se agrupan entradas con la misma URL normalizada. Para publicar se exigen trazas coincidentes de al menos dos fuentes activas distintas; el contador guardado no alcanza por sí solo.
4. **Clasificación IA**: Claude (Anthropic) asigna `GEM | WORTH_TRYING | MEH | HYPE | DEAD` con razonamiento por item.
5. **Veredicto humano**: un curador humano confirma o overridea las sugerencias IA. Tools con 👤 tienen veredicto humano.

Más detalle técnico → [Blog series en juanchi.dev](https://juanchi.dev/blog/series/awesome-curated)

---

## 🤖 Por qué confiar en esta lista

- **Transparente**: metodología, reglas de inclusión/exclusión y límites publicados en [METHODOLOGY.md](METHODOLOGY.md)
- **Auto-regulada**: si un `awesome-*` deja de mantenerse, cae al BENCH y eventualmente sale
- **Human-in-the-loop**: no es IA sola. Tools con ⭐ GEM pasan primero por Claude, después por veredicto humano de [Juan Torchia](https://juanchi.dev)
- **Reproducible**: este README se regenera semanalmente. El sistema documentado en [juanchi.dev/blog/series/awesome-curated](https://juanchi.dev/blog/series/awesome-curated)

## 🤝 Contribuir

- 🐛 ¿Tool mal clasificada? → [Abrí un issue](https://github.com/JuanTorchia/awesome-curated/issues/new)
- ➕ ¿Falta una tool importante? → Issue con el link + justificación
- 📝 ¿Querés proponer una fuente? → Mandá un repo `awesome-*` que debamos scrapear

## 📬 Newsletter

Recibí el digest mensual con las tools nuevas que entran al roster → [juanchi.dev/newsletter](https://juanchi.dev/newsletter)

---

<div align="center">
<sub>📄 Generado automáticamente desde [juanchi.dev](https://juanchi.dev) · [código del sistema](https://juanchi.dev/blog/series/awesome-curated) · MIT licensed</sub>
</div>
