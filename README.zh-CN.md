<div align="center">

# 🎯 Awesome Curated

其他语言版本: [🇬🇧 English](README.md) · [🇪🇸 Español](README.es.md) · [🇧🇷 Português (BR)](README.pt-BR.md) · **🇨🇳 中文** · [🇯🇵 日本語](README.ja.md)

### 一个**每周开发工具雷达**，整理活跃 `awesome-*` 仓库收录的工具，提供来源记录和人工审核的精选。

[![Human Picks](https://img.shields.io/badge/Human_Picks-5-gold?style=for-the-badge)](#human-reviewed-picks)
[![Sources](https://img.shields.io/badge/Sources-20-purple?style=for-the-badge)](SOURCES.md)
[![Updated](https://img.shields.io/badge/Updated-2026-10-18-green?style=for-the-badge)](UPDATE-SUMMARY.md)
[![Evidence](https://img.shields.io/badge/Evidence-public_snapshot-blue?style=for-the-badge)](data/latest.json)
[![License](https://img.shields.io/badge/License-MIT-blue?style=for-the-badge)](LICENSE)

</div>

---

## 从问题开始

| 任务 | 工具 | 试用 |
|---|---|---|
| 搜索和改写代码 | [ast-grep](https://github.com/ast-grep/ast-grep) · Worth Trying | [试用](GUIDE.md#ast-grep) |
| 验证表单 | [Vest](https://github.com/ealush/vest) · Worth Trying | [试用](GUIDE.md#vest) |
| 检查模型图 | [Netron](https://github.com/lutzroeder/netron) · Human Pick | [试用](GUIDE.md#netron) |

[可复现示例](GUIDE.md) · 英语 / 西班牙语：固定版本、测试数据、结果与限制。自动化测试不改变审核标签。

### 安装前先看一个结果

**修改前**

```js
// console.log("comment")
const text = "console.log(123)";
console.log("hello");
```

**修改后**

```js
// console.log("comment")
const text = "console.log(123)";
logger.info("hello");
```

ast-grep 0.51.0 改写一个 JavaScript 调用，注释和字符串保持不变。这只验证语法，不保证更换 logger 后应用行为不变。 [试用](GUIDE.md#ast-grep).

---

## ⭐ 收藏以便下次查找

示例对你有用吗？给[仓库](https://github.com/JuanTorchia/awesome-curated)加一颗星，方便下次查找固定版本、预期结果和各个示例的限制。[查看更新](UPDATE-SUMMARY.md)。

### 信任快照

- **最新生成更新**: 2026-10-18
- **活跃来源**: 20
- **Human Picks**: 5
- **方法论**: [METHODOLOGY.md](METHODOLOGY.md)
- **跟踪来源**: [SOURCES.md](SOURCES.md)
- **更新摘要**: [UPDATE-SUMMARY.md](UPDATE-SUMMARY.md)
- **证据快照**: [data/latest.json](data/latest.json)
- **可查阅目录**: [TOOLS.md](TOOLS.md)
- **常用标准工具**: 1
- **Needs Review 状态（复核来源）**: 0
- **等待人工认可的 AI Candidates**: 229
- 候选工具尚未获得 Juan 的认可。请查看目录和领域页面。

---

## 🗺️ 找到你的技术栈

[🌐 **Web** · 11](domains/web.zh-CN.md) · [🤖 **AI 与机器学习** · 79](domains/ai-ml.zh-CN.md) · [🛠️ **DevOps** · 12](domains/devops.zh-CN.md) · [📱 **移动端** · 1](domains/mobile.zh-CN.md) · [💾 **数据与数据库** · 45](domains/data.zh-CN.md) · [🔐 **安全与加密** · 9](domains/security.zh-CN.md) · [⚡ **性能** · 3](domains/performance.zh-CN.md) · [🧰 **开发工具** · 75](domains/tooling.zh-CN.md) · [🎨 **其他** · 11](domains/other.zh-CN.md)

---

<a id="human-reviewed-picks"></a>

## ⭐ 人工审核精选

经过人工审核的工具及其适用任务。

<!-- staff-picks:start -->
### 👤 [BayesWitnesses/m2cgen](https://github.com/bayeswitnesses/m2cgen)

<!-- pick:rationale -->

**为什么重要:** Turns trained ML models into native code, reducing production runtime dependencies.

<!-- pick:evidence -->

**证据:** 收录于 4 个活跃来源: rust-unofficial/awesome-rust, fffaraz/awesome-cpp, josephmisiti/awesome-machine-learning +1 more · [来源记录](data/latest.json)

<!-- pick:review -->

**审核:** Human Pick

<!-- pick:caveat -->

**说明 / 审核:** 更适合具有相应机器学习或数据工作流的团队。

### 👤 [Netron](https://github.com/lutzroeder/netron)

<!-- pick:rationale -->

**为什么重要:** Makes model inspection practical across ONNX, TensorFlow, PyTorch, and related ML formats.

<!-- pick:evidence -->

**证据:** 收录于 3 个活跃来源: EthicalML/awesome-production-machine-learning, academic/awesome-datascience, josephmisiti/awesome-machine-learning · [来源记录](data/latest.json)

<!-- pick:review -->

**审核:** Human Pick

<!-- pick:caveat -->

**说明 / 审核:** 更适合具有相应机器学习或数据工作流的团队。

### 👤 [Sniffnet](https://github.com/gyulyvgc/sniffnet)

<!-- pick:rationale -->

**为什么重要:** Provides a low-friction network traffic monitor for debugging and security checks.

<!-- pick:evidence -->

**证据:** 收录于 3 个活跃来源: rust-unofficial/awesome-rust, jaywcjlove/awesome-mac, MunGell/awesome-for-beginners · [来源记录](data/latest.json)

<!-- pick:review -->

**审核:** Human Pick

<!-- pick:caveat -->

**说明 / 审核:** 广泛采用前，应先进行有针对性的小范围试用。

### 👤 [themis](https://github.com/cossacklabs/themis)

<!-- pick:rationale -->

**为什么重要:** Gives teams a higher-level API over cryptographic primitives without starting from raw building blocks.

<!-- pick:evidence -->

**证据:** 收录于 3 个活跃来源: rust-unofficial/awesome-rust, fffaraz/awesome-cpp, avelino/awesome-go · [来源记录](data/latest.json)

<!-- pick:review -->

**审核:** Human Pick

<!-- pick:caveat -->

**说明 / 审核:** 涉及安全的工具；用于生产前需评估适用性与维护状况。

### 👤 [Bencher](https://bencher.dev)

<!-- pick:rationale -->

**为什么重要:** Adds continuous benchmarking to CI so performance regressions can be caught before release.

<!-- pick:evidence -->

**证据:** 收录于 2 个活跃来源: fffaraz/awesome-cpp, avelino/awesome-go · [来源记录](data/latest.json)

<!-- pick:review -->

**审核:** Human Pick

<!-- pick:caveat -->

**说明 / 审核:** 跨来源覆盖有限。
<!-- staff-picks:end -->

---

## 等待人工审核的候选工具

- [yt-dlp](https://github.com/yt-dlp/yt-dlp) — Dev Tooling · Found in 3 active sources: agarrharr/awesome-cli-apps, jivoi/awesome-osint, vinta/awesome-python
- [Deepchecks](https://github.com/deepchecks/deepchecks) — AI & ML · Found in 3 active sources: EthicalML/awesome-production-machine-learning, academic/awesome-datascience, josephmisiti/awesome-machine-learning
- [Colossal-AI](https://github.com/hpcaitech/colossalai) — Dev Tooling · Found in 3 active sources: EthicalML/awesome-production-machine-learning, josephmisiti/awesome-machine-learning, MunGell/awesome-for-beginners
- [Feature Engine](https://github.com/feature-engine/feature_engine) — AI & ML · Found in 3 active sources: EthicalML/awesome-production-machine-learning, josephmisiti/awesome-machine-learning, vinta/awesome-python
- [askbudi/roundtable](https://github.com/askbudi/roundtable) — AI & ML · Found in 2 active sources: vuejs/awesome-vue, punkpeye/awesome-mcp-servers

候选工具不代表个人推荐。可通过 GitHub issues 请求审核，或在 TOOLS.md 查看完整队列。 [GitHub issues](https://github.com/JuanTorchia/awesome-curated/issues/new/choose) · [TOOLS.md](TOOLS.md)

---

## ⭐ 按领域分类的已审阅推荐和候选项

### 🌐 Web

| 工具 | 作用 | 信号 |
|---|---|---|
| 👤 [**Vest**](https://github.com/ealush/vest) | Validations framework inspired by unit testing frameworks. | Found in 2 active sources: vuejs/awesome-vue, MunGell/awesome-for-beginners · Worth Trying |
| [**D3js**](https://d3js.org) | is a powerful data visualization javascript library. | Found in 2 active sources: jivoi/awesome-osint, academic/awesome-datascience · AI Candidate |
| [**grpc**](https://github.com/grpc/grpc) | Remote Procedure Calls (RPCs) provide a useful abstraction for building distributed applications and services. The... | Found in 2 active sources: fffaraz/awesome-cpp, vinta/awesome-python · AI Candidate |

📖 更多 8 个见[详细页面 →](domains/web.zh-CN.md)

### 🤖 AI 与机器学习

| 工具 | 作用 | 信号 |
|---|---|---|
| 👤 [**BayesWitnesses/m2cgen**](https://github.com/bayeswitnesses/m2cgen) | A CLI tool to transpile trained classic machine learning models into a native Rust code with zero dependencies. | Found in 4 active sources: rust-unofficial/awesome-rust, fffaraz/awesome-cpp, josephmisiti/awesome-machine-learning +1 more · Human Pick |
| 👤 [**Netron**](https://github.com/lutzroeder/netron) | Netron is a viewer for neural network, deep learning and machine learning models. | Found in 3 active sources: EthicalML/awesome-production-machine-learning, academic/awesome-datascience, josephmisiti/awesome-machine-learning · Human Pick |
| 👤 [**Mem0**](https://github.com/mem0ai/mem0) | Mem0 enhances AI assistants and agents with an intelligent memory layer, enabling personalized AI interactions. | Found in 3 active sources: EthicalML/awesome-production-machine-learning, vinta/awesome-python, MunGell/awesome-for-beginners · Worth Trying |

📖 更多 76 个见[详细页面 →](domains/ai-ml.zh-CN.md)

### 🛠️ DevOps

| 工具 | 作用 | 信号 |
|---|---|---|
| 👤 [**bandwhich**](https://github.com/imsnif/bandwhich) | Track bandwidth utilization by process. | Found in 2 active sources: agarrharr/awesome-cli-apps, rust-unofficial/awesome-rust · Worth Trying |
| [**BorgBackup**](https://github.com/borgbackup/borg) | Deduplicating backup program with compression and authenticated encryption. | Found in 2 active sources: vinta/awesome-python, MunGell/awesome-for-beginners · AI Candidate |
| [**ctop**](https://github.com/bcicen/ctop) | interface (e.g. htop) for container metrics. | Found in 2 active sources: agarrharr/awesome-cli-apps, avelino/awesome-go · AI Candidate |

📖 更多 9 个见[详细页面 →](domains/devops.zh-CN.md)

### 📱 移动端

| 工具 | 作用 | 信号 |
|---|---|---|
| [**RunAnywhere**](https://github.com/runanywhereai/runanywhere-sdks) | RunAnywhere is a production-ready SDK for running AI models (LLMs, speech-to-text, text-to-speech) on-device for... | Found in 2 active sources: EthicalML/awesome-production-machine-learning, josephmisiti/awesome-machine-learning · AI Candidate |

📖 [完整领域页面 →](domains/mobile.zh-CN.md)

### 💾 数据与数据库

| 工具 | 作用 | 信号 |
|---|---|---|
| [**gradio**](https://github.com/gradio-app/gradio) | Quickly create and share demos of models by only writing Python. Debug models interactively in your browser, get... | Found in 3 active sources: EthicalML/awesome-production-machine-learning, josephmisiti/awesome-machine-learning, vinta/awesome-python · AI Candidate |
| [**matplotlib**](https://github.com/matplotlib/matplotlib) | A Python 2D plotting library which produces publication-quality figures in a variety of hardcopy formats and... | Found in 3 active sources: EthicalML/awesome-production-machine-learning, vinta/awesome-python, MunGell/awesome-for-beginners · AI Candidate |
| [**Streamlit**](https://github.com/streamlit/streamlit) | Streamlit lets you create apps for your machine learning projects with deceptively simple Python scripts. It... | Found in 3 active sources: EthicalML/awesome-production-machine-learning, josephmisiti/awesome-machine-learning, vinta/awesome-python · AI Candidate |

📖 更多 42 个见[详细页面 →](domains/data.zh-CN.md)

### 🔐 安全与加密

| 工具 | 作用 | 信号 |
|---|---|---|
| 👤 [**themis**](https://github.com/cossacklabs/themis) | High level crypto library for storing data (AES), secure messaging (ECC + ECDSA / RSA + PSS + PKCS#7) and... | Found in 3 active sources: rust-unofficial/awesome-rust, fffaraz/awesome-cpp, avelino/awesome-go · Human Pick |
| [**Brave**](https://brave.com) | Web browser with an emphasis on privacy and speed. (https://github.com/brave/brave-browser/) | Found in 2 active sources: jivoi/awesome-osint, jaywcjlove/awesome-mac · AI Candidate |
| [**LibreWolf**](https://librewolf.net) | A fork of Firefox, focused on privacy, security and freedom. (https://gitlab.com/librewolf-community) | Found in 2 active sources: jivoi/awesome-osint, jaywcjlove/awesome-mac · AI Candidate |

📖 更多 6 个见[详细页面 →](domains/security.zh-CN.md)

### ⚡ 性能

| 工具 | 作用 | 信号 |
|---|---|---|
| 👤 [**Bencher**](https://bencher.dev) | Suite of continuous benchmarking tools designed to catch performance regressions in CI. MIT/Apache-2.0 Rust | Found in 2 active sources: fffaraz/awesome-cpp, avelino/awesome-go · Human Pick |
| [**Cython**](https://github.com/cython/cython) | Cython is an optimising static compiler for both the Python programming language and the extended Cython programming... | Found in 2 active sources: fffaraz/awesome-cpp, vinta/awesome-python · AI Candidate |
| [**Numba**](https://github.com/numba/numba) | A compiler for Python array and numerical functions. | Found in 2 active sources: EthicalML/awesome-production-machine-learning, vinta/awesome-python · AI Candidate |

📖 [完整领域页面 →](domains/performance.zh-CN.md)

### 🧰 开发工具

| 工具 | 作用 | 信号 |
|---|---|---|
| 👤 [**Sniffnet**](https://github.com/gyulyvgc/sniffnet) | Cross-platform application to monitor your network traffic with ease | Found in 3 active sources: rust-unofficial/awesome-rust, jaywcjlove/awesome-mac, MunGell/awesome-for-beginners · Human Pick |
| 👤 [**ast-grep**](https://github.com/ast-grep/ast-grep) | A CLI tool for code structural search, lint and rewriting. | Found in 2 active sources: agarrharr/awesome-cli-apps, rust-unofficial/awesome-rust · Worth Trying |
| 👤 [**ATAC**](https://github.com/julien-cpsn/atac) | A feature-full TUI API client made in Rust. ATAC is free, open-source, offline and account-less. | Found in 2 active sources: agarrharr/awesome-cli-apps, rust-unofficial/awesome-rust · Worth Trying |

📖 更多 72 个见[详细页面 →](domains/tooling.zh-CN.md)

### 🎨 其他

| 工具 | 作用 | 信号 |
|---|---|---|
| [**AI Job Displacement Tracker**](https://github.com/noahaust2/ai-displacement-tracker) | Structured, source-backed dataset tracking 96 AI-attributed workforce reductions (457K workers affected, 13... | Found in 2 active sources: EthicalML/awesome-production-machine-learning, academic/awesome-datascience · AI Candidate |
| [**beets**](https://github.com/beetbox/beets) | A music library manager and MusicBrainz tagger. | Found in 2 active sources: agarrharr/awesome-cli-apps, vinta/awesome-python · AI Candidate |
| [**croc**](https://github.com/schollz/croc) | Easily and securely send files or folders from one computer to another. | Found in 2 active sources: agarrharr/awesome-cli-apps, avelino/awesome-go · AI Candidate |

📖 更多 8 个见[详细页面 →](domains/other.zh-CN.md)

---

## 🎯 如何精选

1. **发现**: GitHub API (GraphQL 批量) 检测活跃维护的 `awesome-*` 仓库。
2. **多维评分**: freshness、活跃度、流行度、深度和社区健康度加权成单一分数。
3. **来源证据**：规范化 URL 相同的条目会合并。发布需要至少两个不同活跃来源的匹配记录；仅有已存储的出现次数不足以满足条件。
4. **AI 分类**: Claude (Anthropic) 为每个条目分配 `GEM | WORTH_TRYING | MEH | HYPE | DEAD` 并提供推理。
5. **人工审核**: 人类策展人确认或覆盖 AI 建议。标记 👤 的工具经过人工审核。

技术详情 → [juanchi.dev 博客系列](https://juanchi.dev/blog/series/awesome-curated)

---

## 🤖 为什么信任此列表

- **透明**: 方法论、纳入规则、排除规则和限制都发布在 [METHODOLOGY.md](METHODOLOGY.md)
- **自调节**: 如果某个 `awesome-*` 停止维护,会落入 BENCH,最终退出
- **人机协作**: 不是纯 AI。⭐ GEM 工具先经 Claude,再经 [Juan Torchia](https://juanchi.dev) 人工审核
- **可复现**: 此 README 每周重新生成。系统文档见 [juanchi.dev/blog/series/awesome-curated](https://juanchi.dev/blog/series/awesome-curated)

## 🤝 贡献

- 🐛 工具分类错误? → [提交 Issue](https://github.com/JuanTorchia/awesome-curated/issues/new)
- ➕ 缺少重要工具? → 提交 Issue 附链接 + 理由
- 📝 想推荐新源? → 提议一个我们应该扫描的 `awesome-*` 仓库

## 📬 Newsletter

每月获取进入 roster 的新工具摘要 → [juanchi.dev/newsletter](https://juanchi.dev/newsletter)

---

<div align="center">
<sub>📄 自动生成自 [juanchi.dev](https://juanchi.dev) · [系统源码](https://juanchi.dev/blog/series/awesome-curated) · MIT licensed</sub>
</div>
