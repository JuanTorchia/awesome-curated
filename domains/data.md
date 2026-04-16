# 💾 Data & Databases — Awesome Curated

<p><sub>← [Back to main](../README.md)</sub></p>

**35 GEMs · 41 Worth trying**

---

## ⭐ GEMs — industry standards

Tools the community considers default. If you don't know them yet, they're worth exploring.

### [matplotlib](https://github.com/matplotlib/matplotlib)

![](https://img.shields.io/github/stars/matplotlib/matplotlib?style=flat-square&label=⭐) · appears in 3 lists

- A Python 2D plotting library which produces publication-quality figures in a variety of hardcopy formats and interactive environments across platforms.

> **AI analysis:** Python lib para feature engineering: transformers para limpieza, encoding, scaling. Para ML engineers que automatizan feature prep. Resuelve bien: FE repetitivo sin código custom.

**Strengths:** _APIs consistentes, composable transformers_ · _Handlea edge cases (missing values, outliers)_

**Tags:** `feature-engineering` `python` `sklearn` `ml` `preprocessing`

---

### [recharts](https://github.com/recharts/recharts)

![](https://img.shields.io/github/stars/recharts/recharts?style=flat-square&label=⭐) · appears in 3 lists

Redefined chart library built with React and D3.

> **AI analysis:** Recharts es la librería de gráficos para React más usada y con mejor DX del ecosistema. Componentes declarativos, composables, que abstraen D3 sin perder su potencia. Si necesitás charts en React sin querer pelearte con D3 directamente ni pagar licencias de Highcharts, este es el camino estándar. No es la más performante con datasets masivos, pero para el 90% de los dashboards del mundo real cumple de sobra. Maduro, bien mantenido y con buena comunidad.

**Strengths:** _API declarativa y composable que hace que armar gráficos complejos sea intuitivo sin tocar D3 directamente_ · _Amplia variedad de tipos de gráficos (line, bar, area, pie, radar, etc.) listos para usar con buena customización_ · _Excelente integración con el ecosistema React, incluyendo soporte para SSR y responsive containers nativos_

**Tags:** `react` `charts` `d3` `data-visualization` `open-source`

---

### [Streamlit](https://github.com/streamlit/streamlit)

![](https://img.shields.io/github/stars/streamlit/streamlit?style=flat-square&label=⭐) · appears in 3 lists

- Streamlit lets you create apps for your machine learning projects with deceptively simple Python scripts. It supports hot-reloading, so your app updates live as you edit and save your file.

> **AI analysis:** Framework Python para deployar ML apps sin frontend expertise. Hot-reload y state management builtin. Real para prototipado rápido, pero no escala a aplicaciones complejas.

**Strengths:** _Deployable en minutos, zero JavaScript requerido_ · _Perfect para dashboards y demos internos_

**Tags:** `python` `web-framework` `ml-apps` `rapid-prototyping`

---

### [ActiveMQ](https://activemq.apache.org)

appears in 2 lists

Java message broker.

> **AI analysis:** Message broker Java Apache OpenSource. Estándar para async messaging, queuing, pub-sub en arquitecturas Java enterprise.

**Strengths:** _Soporte completo AMQP/OpenWire/MQTT/STOMP_ · _Clustering y persistencia robusto_

**Tags:** `java` `message-broker` `messaging` `apache`

---

### [Apache Airflow](https://github.com/apache/airflow)

![](https://img.shields.io/github/stars/apache/airflow?style=flat-square&label=⭐) · appears in 2 lists

- Data Pipeline framework built in Python, including scheduler, DAG definition and a UI for visualisation.

> **AI analysis:** Framework Python para orquestar pipelines de datos con DAGs, scheduler y UI. Estándar en la industria para ETL a escala. Resuelve el problema real de coordinar tareas complejas con dependencias.

**Strengths:** _Comunidad masiva, documentación exhaustiva y madurez probada en producción_ · _UI visual robusta para monitoreo y debugging de DAGs complejos_

**Tags:** `python` `dag` `scheduler` `etl` `orchestration`

---

### [Apache ECharts](https://github.com/apache/echarts)

![](https://img.shields.io/github/stars/apache/echarts?style=flat-square&label=⭐) · appears in 2 lists

- Apache ECharts is a powerful, interactive charting and data visualization library for browser.

> **AI analysis:** Librería Apache de visualización interactiva en browser. 50K+ stars, soporte enterprise. Estándar para dashboards, reportes y análisis de datos complejos.

**Strengths:** _Ecosistema maduro con miles de ejemplos_ · _Rendering performante incluso con datasets grandes_

**Tags:** `dataviz` `javascript` `interactive` `charts`

---

### [Chart.js](https://chartjs.org)

appears in 2 lists

a javascript library that allows you to create charts easly

> **AI analysis:** Librería JS para gráficos interactivos simples. Estándar para dashboards web básicos. Resuelve bien visualización rápida pero no es para análisis complejos.

**Strengths:** _API sencilla, documentación excelente_ · _Rendimiento decente en browsers_

**Tags:** `javascript` `charts` `visualization` `canvas`

---

### [cleanlab](https://github.com/cleanlab/cleanlab)

![](https://img.shields.io/github/stars/cleanlab/cleanlab?style=flat-square&label=⭐) · appears in 2 lists

- Python library for data-centric AI. Can automatically: find mislabeled data, detect outliers, estimate consensus + annotator-quality for multi-annotator datasets, suggest which data is best to (re)label next.

> **AI analysis:** Librería Python data-centric que identifica datos mislabeled, outliers y estima calidad de anotadores. Core real para ML en producción: encuentra problemas en datos antes que en modelos.

**Strengths:** _Detecta errores de etiquetado automáticamente, ahorra revisión manual costosa_ · _Soporta datasets multi-anotador con estimación de consenso_

**Tags:** `python` `data-quality` `ml-monitoring` `label-errors`

---

### [Dask](https://github.com/dask/dask)

![](https://img.shields.io/github/stars/dask/dask?style=flat-square&label=⭐) · appears in 2 lists

- Distributed parallel processing framework for Pandas and NumPy computations.

> **AI analysis:** Framework paralelo distribuido para Pandas/NumPy. Escala cálculos sin reescribir código. Para data science que supera memoria local.

**Strengths:** _API idéntica a Pandas, learning curve cero_ · _Lazy evaluation optimiza automáticamente_

**Tags:** `python` `distributed-computing` `pandas` `numpy` `parallelization`

---

### [DataFrames](https://github.com/juliadata/dataframes.jl)

![](https://img.shields.io/github/stars/juliadata/dataframes.jl?style=flat-square&label=⭐) · appears in 2 lists

library for working with tabular data in Julia.

> **AI analysis:** Estándar de facto para manipular datos tabulares en Julia. Similar a pandas en Python. Activa, bien mantenida, core del ecosistema Julia para data science.

**Strengths:** _Performance cercana a C para operaciones matriciales_ · _Integración perfecta con ecosistema Julia_

**Tags:** `julia` `dataframes` `data-science` `tabular`

---

### [DataGrip](https://jetbrains.com/datagrip)

appears in 2 lists

DataGrip is a cross-platform IDE that is aimed at DBAs and developers working with SQL databases. It has built-in drivers that support DB2, Derby, H2, HSQLDB, MySQL, Oracle, PostgreSQL, SQL Server, Sqlite and Sybase.

> **AI analysis:** IDE JetBrains para SQL que soporta 10+ motores (MySQL, Postgres, Oracle, SQL Server, etc). Estándar entre DBAs por autocomplete avanzado, refactoring, inspección de esquema. Premium pero indispensable si trabajas SQL 8h/día.

**Strengths:** _Autocomplete contextual y refactoring SQL sin rival_ · _Integración transparente con múltiples engines simultáneos_

**Tags:** `sql` `ide` `dba` `jetbrains`

---

### [dbt-labs/dbt-core](https://github.com/dbt-labs/dbt-core)

![](https://img.shields.io/github/stars/dbt-labs/dbt-core?style=flat-square&label=⭐) · appears in 2 lists

Project banner, super clear description (friendly to people brand new to the product), screenshot of the docs the tool generates, and concise links to other comprehensive pages explaining Getting Started, Joining the dbt Community, Bug Reports, Code Contribution, and Code of Conduct

> **AI analysis:** dbt-core: herramienta de transformación SQL para data pipelines. Standard de la industria analytics. Resuelve: versionear, testear, documentar SQL sin boilerplate.

**Strengths:** _Abstracción SQL elegante (Jinja), dependency resolution automático_ · _Documentación generada en vivo, testing nativo_

**Tags:** `data-engineering` `sql` `python` `analytics` `oss`

---

### [Druid](https://druid.apache.org)

appears in 2 lists

Distributed, column-oriented, real-time analytics data store.

> **AI analysis:** OLAP distribuido, column-store, tiempo-real. Para analytics masivo (millones events/sec). Usado en Airbnb, Netflix. Estándar si escala es requisito.

**Strengths:** _Ingestión real-time a escala; agregaciones sub-segundo en datasets TBs_ · _Sql-like query layer, operacional probado_

**Tags:** `olap` `timeseries` `column-store` `java` `distributed`

---

### [edgartools](https://github.com/dgunning/edgartools)

![](https://img.shields.io/github/stars/dgunning/edgartools?style=flat-square&label=⭐) · appears in 2 lists

`Python` - AI-native SEC EDGAR library with XBRL financials, clean text extraction, 17+ typed forms, and pandas DataFrames.

> **AI analysis:** Librería Python para parsear SEC EDGAR filings con XBRL y dataframes. Cubre 17+ tipos de formularios, limpieza de texto. Estándar para análisis fintech/quant.

**Strengths:** _Coverage completo de forms SEC y XBRL parsing_ · _Output en pandas DataFrames listos para análisis_

**Tags:** `python` `sec` `xbrl` `fintech` `data-extraction`

---

### [etcd](https://github.com/etcd-io/etcd)

![](https://img.shields.io/github/stars/etcd-io/etcd?style=flat-square&label=⭐) · appears in 2 lists

Distributed reliable key-value store for the most critical data of a distributed system by [etcd-io](https://github.com/etcd-io) (former part of CoreOS).

> **AI analysis:** Distributed key-value store crítico. Backbone de Kubernetes, etcd es el estándar de facto para datos críticos en sistemas distribuidos.

**Strengths:** _Raft consensus battle-tested en Kubernetes_ · _Fuerte consistencia garantizada_

**Tags:** `distributed` `key-value` `go` `consensus`

---

### [ExifTool](https://sno.phy.queensu.ca/~phil/exiftool)

appears in 2 lists

Platform-independent Perl library plus a command-line application for reading, writing and editing meta information in a wide variety of files.

> **AI analysis:** Extractor de metadatos EXIF/IPTC/XMP de múltiples formatos. Herramienta de bajo nivel para forensics/privacy audit. CLI potente, estándar en pipelines de análisis.

**Strengths:** _Soporta 150+ formatos diferentes_ · _Estable desde 2003, sine-qua-non en análisis_

**Tags:** `metadata` `cli` `perl` `forensics` `cross-platform`

---

### [Flink](https://flink.apache.org)

appears in 2 lists

Open source platform for distributed stream and batch data processing.

> **AI analysis:** Plataforma Apache para procesamiento distribuido de streams y batches. Estándar industria para data pipelines masivos. Maduro, usado en empresas Fortune 500.

**Strengths:** _Escalabilidad probada en petabytes_ · _API unificada para stream y batch_

**Tags:** `java` `distributed-computing` `stream-processing` `apache`

---

### [ggplot2](https://ggplot2.tidyverse.org)

appears in 2 lists

A data visualization package based on the grammar of graphics.

> **AI analysis:** Librería R para visualización basada en grammar of graphics. Estándar en R para análisis exploratorio. No es ML puro, es viz, pero fundamental en pipelines R.

**Strengths:** _Sintaxis declarativa intuitiva, output publication-ready_ · _Excelente para exploración rápida, 20+ years madurez_

**Tags:** `r` `visualization` `grammar-of-graphics` `data-science`

---

### [Kubo](https://github.com/ipfs/kubo)

![](https://img.shields.io/github/stars/ipfs/kubo?style=flat-square&label=⭐) · appears in 2 lists

Implementation of IPFS, a global, versioned, peer-to-peer filesystem that seeks to connect all computing devices with the same system of files.

> **AI analysis:** Implementación de IPFS en Go, el estándar de facto para sistemas de archivos P2P descentralizados. Robusto, usado en producción, pero requiere infraestructura significativa para casos complejos.

**Strengths:** _Estándar industrial para redes P2P descentralizadas_ · _Active development y comunidad sólida_

**Tags:** `ipfs` `p2p` `go` `distributed` `self-hosted`

---

### [numpy](https://numpy.org)

appears in 2 lists

`Python` - NumPy is the fundamental package for scientific computing with Python. [GitHub](https://github.com/numpy/numpy)

> **AI analysis:** Librería fundamental Python: arrays n-dimensionales eficientes y operaciones vectorizadas. Cimiento de todo el ecosistema scientific/ML Python.

**Strengths:** _Rendimiento C/Fortran subyacente, 100x más rápido que listas Python_ · _API intuitiva, estándar universal en toda la industria_

**Tags:** `python` `arrays` `scientific-computing` `vectorization`

---

### [OpenStreetMap](https://openstreetmap.org)

appears in 2 lists

Collaborative project to create a free editable map of the world. )

> **AI analysis:** Proyecto colaborativo masivo para mapas libres y editables. Base de datos geoespacial comunitaria con millones de contribuidores. Resuelve el problema de mapas privativos y datos geográficos abiertos.

**Strengths:** _Cobertura global con datos actualizados comunitariamente_ · _Integración amplia en proyectos open-source y empresariales_

**Tags:** `geospatial` `osm` `collaborative` `maps` `ruby`

---

### [pandas](https://github.com/pandas-dev/pandas)

![](https://img.shields.io/github/stars/pandas-dev/pandas?style=flat-square&label=⭐) · appears in 2 lists

_(label: good first issue)_ <br> Flexible and powerful data analysis / manipulation library for Python, providing labeled data structures similar to R data.frame objects, statistical functions, and much more

> **AI analysis:** Librería Python data manipulation estándar de la industria. Columnar, rápida, con SQL-like ops. Imprescindible en data science y análisis.

**Strengths:** _Estándar de facto en data science global_ · _Integración profunda con NumPy, Matplotlib, scikit-learn_

**Tags:** `python` `data-science` `pandas` `dataframe`

---

### [pandas](https://pandas.pydata.org)

appears in 2 lists

`Python` - pandas is an open source, BSD-licensed library providing high-performance, easy-to-use data structures and data analysis tools for the Python programming language. [GitHub](https://github.com/pandas-dev/pandas)

> **AI analysis:** Librería de estructuras de datos y análisis para Python (DataFrames, Series). Imprescindible en ciencia de datos, estándar de 20 años. Ningún proyecto Python data-heavy prescinde de pandas.

**Strengths:** _API intuitiva, comunidad gigante_ · _Rendimiento sólido con C backend, integración perfecto con NumPy/Matplotlib_

**Tags:** `dataframe` `data-analysis` `python` `performance`

---

### [pgcli](https://github.com/dbcli/pgcli)

![](https://img.shields.io/github/stars/dbcli/pgcli?style=flat-square&label=⭐) · appears in 2 lists

Postgres client with autocompletion and syntax highlighting.

> **AI analysis:** Cliente Postgres interactivo con autocompletado y syntax highlighting. Estándar entre DBAs y devs Postgres. Resuelve la escritura ergonómica de queries PostgreSQL.

**Strengths:** _Autocompletado inteligente basado en schema, syntax highlighting Postgres-nativo_ · _Comunidad activa, mantenimiento continuo, se considera default entre Postgres users_

**Tags:** `cli` `postgres` `python` `repl`

---

### [Plotly](https://github.com/plotly/plotly.py)

![](https://img.shields.io/github/stars/plotly/plotly.py?style=flat-square&label=⭐) · appears in 2 lists

- An interactive, open source, and browser-based graphing library for Python.

> **AI analysis:** Librería Python interactiva para gráficos. Web-based, responsive, soporta heatmaps, 3D, etc. Estándar en data science.

**Strengths:** _Gráficos interactivos vía web, exporta HTML/PNG sin servidor_ · _Documentación y comunidad masiva_

**Tags:** `data-visualization` `python` `interactive` `web-based`

---

### [pola-rs/polars](https://github.com/pola-rs/polars)

![](https://img.shields.io/github/stars/pola-rs/polars?style=flat-square&label=⭐) · appears in 2 lists

Fast feature complete DataFrame library [](https://github.com/pola-rs/polars/actions)

> **AI analysis:** DataFrame library en Rust, rendimiento brutal vs pandas. Reemplaza decisivamente a pandas para workloads CPU-bound. Estándar emergente en data engineering Rust.

**Strengths:** _10-100x más rápido que pandas en operaciones vectorizadas_ · _Lazy evaluation y query optimization integrados_

**Tags:** `rust` `dataframe` `performance` `data-science`

---

### [protobuf](https://github.com/protocolbuffers/protobuf)

![](https://img.shields.io/github/stars/protocolbuffers/protobuf?style=flat-square&label=⭐) · appears in 2 lists

Protocol Buffers - Google's data interchange format. [BSD]

> **AI analysis:** Formato de intercambio de datos compacto y agnóstico de lenguaje. Estándar de facto en APIs y microservicios. Resuelve versionado y compatibilidad forward/backward.

**Strengths:** _Adopción masiva en industria_ · _Generación automática de código en 15+ lenguajes_

**Tags:** `serialization` `rpc` `schema` `multi-language`

---

### [Redis](https://github.com/redis/redis)

![](https://img.shields.io/github/stars/redis/redis?style=flat-square&label=⭐) · appears in 2 lists

Redis is an open-source, in-memory data store that supports vector similarity search, making it suitable for AI/ML applications such as semantic search and recommendation systems.

> **AI analysis:** In-memory data store ultra rápido con vector similarity search nativo. Estándar industria para caching, sesiones, real-time analytics y ahora embeddings para RAG/semantic search.

**Strengths:** _Velocidad extrema, sub-milisegundo en operaciones típicas_ · _Vector search integrado sin plugins externos, maduro y escalable_

**Tags:** `database` `in-memory` `cache` `vector-search` `c`

---

### [ROOT](https://root.cern.ch)

appears in 2 lists

A modular scientific software framework. It provides all the functionalities needed to deal with big data processing, statistical analysis, visualization and storage.

> **AI analysis:** Framework científico C++ para big data, análisis estadístico, visualización. CERN-maintained. Para física de partículas y research intensivo en datos.

**Strengths:** _Mantenimiento CERN = sólido y long-term_ · _Historial probado en ciencia de 25+ años_

**Tags:** `cpp` `scientific-computing` `big-data` `statistics` `visualization`

---

### [scipy](https://scipy.org)

appears in 2 lists

`Python` - SciPy (pronounced “Sigh Pie”) is a Python-based ecosystem of open-source software for mathematics, science, and engineering. [GitHub](https://github.com/scipy/scipy)

> **AI analysis:** Ecosistema Python maduro para computación científica: álgebra lineal, optimización, procesamiento de señales. Estándar industria hace 20+ años, depencia de facto en ML/ciencia.

**Strengths:** _Rendimiento optimizado en C/Fortran para operaciones numéricas_ · _API estable, documentation exhaustiva, comunidad gigante_

**Tags:** `python` `scientific-computing` `numpy-dependent`

---

### [seaborn](https://github.com/mwaskom/seaborn)

![](https://img.shields.io/github/stars/mwaskom/seaborn?style=flat-square&label=⭐) · appears in 2 lists

- Seaborn is a Python visualization library based on matplotlib. It provides a high-level interface for drawing attractive statistical graphics.

> **AI analysis:** Wrapper de matplotlib para gráficos estadísticos bonitos. Estándar industrial para EDA y papers. API intuitiva, integración con pandas fluida.

**Strengths:** _API declarativa + matplotlib power debajo_ · _Defaults estéticos profesionales sin tweaking_

**Tags:** `visualization` `matplotlib` `statistical-graphics` `python`

---

### [Seaborn](https://seaborn.pydata.org)

appears in 2 lists

A python visualization library based on matplotlib.

> **AI analysis:** Librería de visualización estadística sobre Matplotlib. Gráficos estéticos para EDA y reportes. Resuelve problema: plots complejos (heatmaps, pair plots) con defaults bonitos en pocas líneas.

**Strengths:** _API intuitiva, defaults bonitos, integración fluida con Pandas_ · _Ideal para EDA rápida y comunicación de resultados_

**Tags:** `visualization` `matplotlib` `statistical-graphics` `pandas`

---

### [statsmodels](https://github.com/statsmodels/statsmodels)

![](https://img.shields.io/github/stars/statsmodels/statsmodels?style=flat-square&label=⭐) · appears in 2 lists

Statistical modelling and econometrics in Python.

> **AI analysis:** Librería Python para estadística y econometría. Estándar para análisis econométrico, series temporales. Imprescindible si hacés econometría seria.

**Strengths:** _API exhaustiva para modelos econométricos_ · _Documentación científica y ejemplos robustos_

**Tags:** `python` `statistics` `econometrics` `timeseries`

---

### [TiKV](https://github.com/tikv/tikv)

![](https://img.shields.io/github/stars/tikv/tikv?style=flat-square&label=⭐) · appears in 2 lists

_(label: difficulty/easy)_ <br> A distributed transactional key-value database

> **AI analysis:** Base de datos distribuida key-value transaccional escrita en Rust. Usado por PingCAP, producción-ready. Para quien necesita consistencia ACID en escala.

**Strengths:** _ACID transacciones en ambiente distribuido_ · _Codebase Rust production-grade, usado en scale_

**Tags:** `rust` `distributed-db` `kvstore` `transactional`

---

### [tsfresh](https://github.com/blue-yonder/tsfresh)

![](https://img.shields.io/github/stars/blue-yonder/tsfresh?style=flat-square&label=⭐) · appears in 2 lists

- Automatic extraction of relevant features from time series.

> **AI analysis:** Librería Python para feature extraction automática de series temporales. Resuelve problema específico (análisis TSA) con 700+ features automáticas. Estándar en industry para ML en time-series.

**Strengths:** _Automatización de feature engineering compleja_ · _Integración scikit-learn nativa_

**Tags:** `python` `timeseries` `feature-engineering` `ml`

---


---

## 👍 Worth trying — solid in their niche

Less hype than the GEMs but reliable if you fall into their use case.

### [gradio](https://github.com/gradio-app/gradio)

![](https://img.shields.io/github/stars/gradio-app/gradio?style=flat-square&label=⭐) · appears in 3 lists

- Quickly create and share demos of models - by only writing Python. Debug models interactively in your browser, get feedback from collaborators, and generate public links without deploying anything.

> **AI analysis:** Generador de UIs web minimalista para modelos Python. Creas demo funcional en 10 líneas. Resuelve el problema: demo rápida sin HTML/JS. Excelente para prototipos y sharing.

**Strengths:** _Simplicidad extrema para demos (write-once approach)_ · _Sharing público con URLs ephemeras sin deploy_

**Tags:** `python` `web-ui` `demos` `visualization` `gradio`

---

### [High Charts](https://highcharts.com)

appears in 3 lists



> **AI analysis:** Highcharts es una librería de visualización de datos con más de 15 años en el mercado. Para proyectos enterprise o equipos que necesitan gráficos interactivos complejos con soporte serio, es una opción sólida y probada. El problema es el modelo de licencias: gratuita solo para uso no comercial, lo que la hace costosa para startups. D3.js te da más poder si te bancás la curva de aprendizaje; Chart.js o Recharts cubren el 80% de los casos con menos fricción. Sigue siendo relevante en contextos corporativos donde el soporte importa.

**Strengths:** _Ecosistema maduro con soporte para más de 60 tipos de gráficos incluyendo mapas, stock charts y gantt_ · _Documentación exhaustiva y soporte comercial real, crítico para proyectos enterprise con SLA_ · _Renderizado SVG cross-browser robusto con accesibilidad (WCAG) incorporada_

**Tags:** `javascript` `charts` `data-visualization` `svg` `enterprise`

---

### [AI Job Displacement Tracker](https://github.com/noahaust2/ai-displacement-tracker)

![](https://img.shields.io/github/stars/noahaust2/ai-displacement-tracker?style=flat-square&label=⭐) · appears in 2 lists

- Structured, source-backed dataset tracking 96 AI-attributed workforce reductions (457K workers affected, 13 countries, 13 sectors). Every entry includes source URLs, attribution tier, and job functions.

> **AI analysis:** Dataset estructurado de 96 reducciones de workforce atribuidas a IA (457K workers, 13 países). Útil para investigadores y policy makers que necesitan datos verificados sobre desplazamiento laboral. Resuelve la falta de fuentes confiables en un tema polémico.

**Strengths:** _Datos verificados con URLs de origen_ · _Cubre sectores y geografías variadas_

**Tags:** `dataset` `csv` `labor-economics` `open-data`

---

### [ajitpratap0/GoSQLX](https://github.com/ajitpratap0/gosqlx)

![](https://img.shields.io/github/stars/ajitpratap0/gosqlx?style=flat-square&label=⭐) · appears in 2 lists

](https://glama.ai/mcp/servers/ajitpratap0/GoSQLX) 🏎️ ☁️ 🏠 - 7 SQL tools (validate, format, parse, lint, security scan, metadata extraction, full analysis) over Streamable HTTP. Public remote server at mcp.gosqlx.dev - no install needed. 1.25M+ ops/sec, 6 SQL dialects.

> **AI analysis:** 7 herramientas SQL vía HTTP: validar, formatear, parsear, lintear, security scan. Performance alto (1.25M+ ops/sec), 6 dialectos. Public remote o self-hosted. Resuelve problema real para equipos que procesan SQL.

**Strengths:** _7 funcionalidades SQL integrables vía HTTP, zero install en modo public_ · _Performance extremo (1.25M+ ops/sec), soporte multi-dialecto_

**Tags:** `go` `sql` `http-api` `linting` `security-scan`

---

### [Aleph](https://aleph.occrp.org)

appears in 2 lists

Tool for indexing large amounts of both documents (PDF, Word, HTML) and structured (CSV, XLS, SQL) data for easy browsing and search. It is built with investigative reporting as a primary use case. )

> **AI analysis:** Indexador de documentos y datos estructurados para investigación. Busca en PDFs, CSVs, bases SQL. Diseñado para periodismo de investigación y compliance.

**Strengths:** _Maneja mixed data types (documentos + estructurado) sin fricciones_ · _Escalable con Docker/K8S para datasets masivos_

**Tags:** `search` `indexing` `documents` `docker` `investigative-reporting`

---

### [Another Redis Desktop Manager](https://github.com/qishibo/anotherredisdesktopmanager)

![](https://img.shields.io/github/stars/qishibo/anotherredisdesktopmanager?style=flat-square&label=⭐) · appears in 2 lists

A faster, better and more stable redis desktop manager [GUI client], compatible with Linux, Windows, Mac. What's more, it won't crash when loading massive keys.

> **AI analysis:** GUI para Redis que no crashea con datasets grandes. Más estable que las alternativas oficiales. Si manejás Redis en prod, vale probarlo.

**Strengths:** _Estabilidad genuina con keys masivos, interfaz responsiva_ · _Cross-platform, sin dependencias raras_

**Tags:** `redis` `gui` `database-tools` `electron`

---

### [Apache Ignite](https://github.com/apache/ignite)

![](https://img.shields.io/github/stars/apache/ignite?style=flat-square&label=⭐) · appears in 2 lists

- A memory-centric distributed database, caching, and processing platform for transactional, analytical, and streaming workloads delivering in-memory speeds at petabyte scale - [Demo](https://www.youtube.com/watch?v=Xt4PWQ__YPw).

> **AI analysis:** Plataforma distribuida en-memoria para transaccional + analytics + streaming a escala petabyte. Para infraestructuras críticas que necesitan velocidad subsecond y alta disponibilidad.

**Strengths:** _Escalabilidad horizontal probada en producción empresarial_ · _SQL + compute colocado reducen network roundtrips_

**Tags:** `database` `distributed` `in-memory` `streaming` `apache`

---

### [Apache Solr](https://lucene.apache.org/solr)

appears in 2 lists

Enterprise search platform featuring full-text search, hit highlighting, faceted search, real-time indexing, dynamic clustering, and rich document (e.g., Word, PDF) handling.

> **AI analysis:** Search engine empresarial con full-text, facets, clustering. Alternativa a Elasticsearch. Maduro, en producción desde hace años. Para quien necesita search robusto sin nube.

**Strengths:** _Texto rico (PDF, Word) indexado nativamente_ · _Hit highlighting y faceted search sin plugins extra_

**Tags:** `search` `java` `lucene` `docker` `self-hosted`

---

### [Bread Dataset Viewer](https://github.com/bread-technologies/mle_vscode_extension)

![](https://img.shields.io/github/stars/bread-technologies/mle_vscode_extension?style=flat-square&label=⭐) · appears in 2 lists

A VS Code extension for viewing and exploring large machine learning datasets (CSV, JSON, Parquet, etc.) directly within the editor without VS Code crashing in a clean UI.

> **AI analysis:** Extensión VS Code para explorar datasets grandes (CSV, JSON, Parquet) sin crashes. Resuelve pain point real: VS Code se cuelga con archivos grandes. Interfaz limpia, pero limitado a preview/browse.

**Strengths:** _Soluciona problema específico y molesto_ · _UI intuitiva para data wrangling rápido_

**Tags:** `vscode-extension` `data-exploration` `ml-tooling`

---

### [C3.js](https://c3js.org)

appears in 2 lists

customizable library based on D3.js for easy chart drawing.

> **AI analysis:** Wrapper sobre D3.js que simplifica charts comunes. Buen balance complejidad/poder. Para reportes rápidos sin meterse en D3 puro. Resuelve curva de aprendizaje de D3.

**Strengths:** _Sintaxis mucho más legible que D3 raw_ · _Comunidad activa, muchos ejemplos_

**Tags:** `javascript` `d3` `charts` `visualization`

---

### [csvkit](https://github.com/wireservice/csvkit)

![](https://img.shields.io/github/stars/wireservice/csvkit?style=flat-square&label=⭐) · appears in 2 lists

Utilities for converting to and working with CSV.

> **AI analysis:** Suite de utilidades Python para convertir y manipular CSV. Herramientas CLI clásicas (csvcut, csvgrep, etc). Resuelve transformaciones CSV desde línea de comandos sin escribir código.

**Strengths:** _Utilidades CLI especializadas que evitan escribir scripts Python_ · _Clásico, maduro, comunidad establecida_

**Tags:** `python` `csv` `cli` `data-wrangling`

---

### [Dagster](https://github.com/dagster-io/dagster)

![](https://img.shields.io/github/stars/dagster-io/dagster?style=flat-square&label=⭐) · appears in 2 lists

- A data orchestrator for machine learning, analytics, and ETL.

> **AI analysis:** Orquestador moderno de data pipelines con assets y sensores. Diseñado para ML/analytics. Propone model asset-driven sobre DAGs tradicionales, con mejor DX que Airflow.

**Strengths:** _Abstracción asset-driven más intuitiva que DAGs, testing nativo built-in_ · _Dagit UI moderna y debugging con linaje claro_

**Tags:** `python` `orchestration` `assets` `ml` `data-ops`

---

### [dasel](https://github.com/tomwright/dasel)

![](https://img.shields.io/github/stars/tomwright/dasel?style=flat-square&label=⭐) · appears in 2 lists

Query and update data structures using selectors from the command line. Comparable to jq/yq but supports JSON, YAML, TOML and XML with zero runtime dependencies.

> **AI analysis:** CLI para query/update en JSON, YAML, TOML, XML con selectores. Similar a jq/yq pero multi-format sin dependencias. Resuelve problema real: manipular configs sin aprender jq o yq.

**Strengths:** _Multi-format en una herramienta, cero dependencias runtime (Go binary)_ · _Sintaxis consistente vs aprender jq Y yq por separado_

**Tags:** `cli` `json` `yaml` `toml` `xml`

---

### [DataComPy](https://github.com/capitalone/datacompy)

![](https://img.shields.io/github/stars/capitalone/datacompy?style=flat-square&label=⭐) · appears in 2 lists

A library to compare Pandas, Polars, and Spark data frames. It provides stats and lets users adjust for match accuracy.

> **AI analysis:** Librería Python para comparar DataFrames de Pandas, Polars y Spark con estadísticas detalladas. Resuelve el problema real de validar transformaciones de datos y detectar diferencias en pipelines ETL.

**Strengths:** _Soporte multi-engine (Pandas, Polars, Spark) en una API uniforme_ · _Métricas de match accuracy configurables para validaciones flexibles_

**Tags:** `python` `dataframes` `testing` `etl`

---

### [Deepnote](https://github.com/deepnote/deepnote)

![](https://img.shields.io/github/stars/deepnote/deepnote?style=flat-square&label=⭐) · appears in 2 lists

- Deepnote is a drop-in replacement for Jupyter with an AI-first design, sleek UI, new blocks, and native data integrations. Use Python, R, and SQL locally in your favorite IDE, then scale to Deepnote cloud for real-time collaboration, Deepnote agent, and deployable data apps.

> **AI analysis:** Jupyter moderno con colaboración real-time, integraciones nativas y diseño AI-first. Para data scientists y equipos que necesitan notebooks productivos en la nube sin perder control local.

**Strengths:** _Colaboración real-time integrada nativa_ · _Integración con SQL/datos sin configuración_

**Tags:** `jupyter` `python` `r` `sql` `colaborativo`

---

### [Dolt](https://github.com/dolthub/dolt)

![](https://img.shields.io/github/stars/dolthub/dolt?style=flat-square&label=⭐) · appears in 2 lists

- Dolt is a SQL database that you can fork, clone, branch, merge, push and pull just like a git repository.

> **AI analysis:** SQL database con git-like semantics (branch, merge, push). Innovador conceptualmente pero productización compleja y adopción limitada.

**Strengths:** _Paradigma único: git + SQL en uno_ · _Bueno para data collaboration en equipos pequeños_

**Tags:** `database` `sql` `version-control` `go`

---

### [FlatBuffers](https://github.com/google/flatbuffers)

![](https://img.shields.io/github/stars/google/flatbuffers?style=flat-square&label=⭐) · appears in 2 lists

Memory-efficient serialization library that can access serialized data without unpacking and parsing it.

> **AI analysis:** Serialización sin parsing para datos en memoria. Competidor directo de protobuf, ventaja en acceso sin desempacar. Para sistemas de baja latencia que necesitan eficiencia extrema.

**Strengths:** _Acceso directo a datos sin deserialización completa_ · _Footprint menor que protobuf en algunos casos_

**Tags:** `serialization` `low-latency` `zero-copy` `binary`

---

### [Gephi](https://gephi.org)

appears in 2 lists

is an open-source graph and network visualization software.

> **AI analysis:** Gephi es visualizador de grafos/redes open-source con UI intuitiva. Importa formatos estándar, soporta layouts y análisis. Bueno para exploración ad-hoc, no para pipeline automatizado.

**Strengths:** _UI interactiva potente para exploración visual_ · _Layouts automáticos sofisticados (Force Atlas, etc)_

**Tags:** `graph-visualization` `network-analysis` `java` `desktop-app`

---

### [Hamilton](https://github.com/dagworks-inc/hamilton)

![](https://img.shields.io/github/stars/dagworks-inc/hamilton?style=flat-square&label=⭐) · appears in 2 lists

- Hamilton is a micro-orchestration framework for defining dataflows. Runs anywhere python runs (e.g. jupyter, fastAPI, spark, ray, dask). Brings software engineering best practices without you knowing it. Use it to define feature engineering transforms, end-to-end model pipelines, and LLM workflows. It complements macro-orchestration systems (e.g. kedro, luigi, airflow, dbt, etc.) as it…

> **AI analysis:** Micro-orquestador para dataflows (feature eng, pipelines, LLM workflows). Python-first, corre en Jupyter/FastAPI/Spark/Ray. Resuelve problema: modularizar data transforms sin peso de DAG pesados.

**Strengths:** _Filosofía: 'definition from code', no YAML hell_ · _Corre en múltiples runtimes sin reescribir_

**Tags:** `dataflow` `feature-engineering` `orchestration` `lightweight`

---

### [iredis](https://github.com/laixintao/iredis)

![](https://img.shields.io/github/stars/laixintao/iredis?style=flat-square&label=⭐) · appears in 2 lists

Redis client with autocompletion and syntax highlighting.

> **AI analysis:** Cliente Redis interactivo con autocompletado y syntax highlighting. Mejora UX respecto a redis-cli vanilla. Resuelve el problema de escribir comandos Redis sin errores tipográficos.

**Strengths:** _Autocompletado y syntax highlighting genuinamente útiles para comandos Redis_ · _Soporte para múltiples modos (cluster, sentinel)_

**Tags:** `cli` `redis` `python` `repl`

---

### [Metabase](https://metabase.com)

appears in 2 lists

Easy way for everyone in your company to ask questions and learn from data.

> **AI analysis:** BI tool open-source que democratiza consultas de datos sin SQL. Para empresas que quieren dashboards rápidos sin invertir en Tableau/Power BI. Resuelve la brecha entre data team y business users.

**Strengths:** _UI intuitiva, consultas sin código_ · _Comunidad activa, deployment simple en Docker_

**Tags:** `bi` `dashboard` `agpl` `java` `self-hosted`

---

### [Mingo](https://mingo.io)

appears in 2 lists

Easy to use MongoDB GUI with mind-blowing features.

> **AI analysis:** GUI para MongoDB con UX moderna. Promete features 'mind-blowing' pero descripción genérica. Compite con Compass, Studio 3T, MongoDB Atlas GUI.

**Strengths:** _UI limpia diseñada para UX moderna_ · _Funciona con instancias locales y remotas_

**Tags:** `mongodb` `gui` `database` `nosql`

---

### [mycli](https://github.com/dbcli/mycli)

![](https://img.shields.io/github/stars/dbcli/mycli?style=flat-square&label=⭐) · appears in 2 lists

MySQL client with autocompletion and syntax highlighting.

> **AI analysis:** Cliente MySQL/MariaDB con autocompletado y syntax highlighting. Alternativa mejorada a mysql-cli vanilla. Resuelve UX de escritura de queries sin errores tipográficos.

**Strengths:** _Autocompletado funcional basado en schema actual, syntax highlighting MySQL_ · _Smart suggestions para tablas y columnas_

**Tags:** `cli` `mysql` `python` `repl`

---

### [NSQ](https://nsq.io)

appears in 2 lists

A realtime distributed messaging platform.

> **AI analysis:** Plataforma de messaging distribuido realtime. Go nativo, usado en producción pero mercado dominado por Kafka/RabbitMQ.

**Strengths:** _Extremadamente simple de deployar y operar_ · _Perfecto para casos realtime simples sin overhead_

**Tags:** `go` `messaging` `distributed` `realtime` `queue`

---

### [OpenRefine](https://openrefine.org)

appears in 2 lists

Tool for working with messy data: cleaning, transforming, extending it with web services and linking it to databases.

> **AI analysis:** Tool legacy pero potente para limpiar datos tabularesy enriquecerlos con APIs. Interfaz web intuitiva, scripting en Jython. Sigue siendo estándar en data curation.

**Strengths:** _UI intuitiva para operaciones complejas sin código_ · _Excelente para data wrangling exploratorio_

**Tags:** `data-cleaning` `etl` `jython` `gui` `csv`

---

### [pathwaycom/pathway](https://github.com/pathwaycom/pathway)

![](https://img.shields.io/github/stars/pathwaycom/pathway?style=flat-square&label=⭐) · appears in 2 lists

Performant open-source Python ETL framework with Rust runtime, supporting 300+ data sources.

> **AI analysis:** ETL framework Python con runtime Rust. 300+ sources, low-latency. Real-time analytics y data pipelines. Alternativa a Airflow/Spark más moderna.

**Strengths:** _Runtime Rust = performance y memory efficiency_ · _API pythonica con 300+ connectors out-of-box_

**Tags:** `python` `etl` `rust` `data-pipelines`

---

### [Perspective](https://github.com/finos/perspective)

![](https://img.shields.io/github/stars/finos/perspective?style=flat-square&label=⭐) · appears in 2 lists

Streaming pivot visualization via WebAssembly.

> **AI analysis:** Librería WebAssembly para visualización streaming de datos pivotados. Potente para dashboards tiempo-real, tablas grandes. Comunidad pequeña pero activa (FINOS). No es mainstream.

**Strengths:** _Performance WebAssembly para datasets masivos_ · _Soporte nativo de streaming/actualización incremental_

**Tags:** `webassembly` `data-visualization` `streaming` `pivot` `finos`

---

### [pouchdb](https://github.com/pouchdb/pouchdb)

![](https://img.shields.io/github/stars/pouchdb/pouchdb?style=flat-square&label=⭐) · appears in 2 lists

Javascript db inspired by Apache CouchDB to run well within the browser.

> **AI analysis:** PouchDB sincroniza datos entre navegador y backend (CouchDB compatible). Útil para apps offline-first con sincronización de cola. Menos tracción que IndexedDB nativo moderno.

**Strengths:** _Sincronización bidireccional robusta, manejo elegante de conflictos_ · _API simple y documentación clara_

**Tags:** `database` `offline-first` `sync` `browser`

---

### [PyBroker](https://github.com/edtechre/pybroker)

![](https://img.shields.io/github/stars/edtechre/pybroker?style=flat-square&label=⭐) · appears in 2 lists

`Python` - Algorithmic Trading with Machine Learning.

> **AI analysis:** Framework para trading algorítmico con ML en Python. Backtest, paper trading, integración con brokers. Activa pero espacio competitivo; viable para retail traders educados.

**Strengths:** _ML pipeline integrado para features_ · _Backtest sin boilerplate_

**Tags:** `python` `trading` `machine-learning` `backtesting`

---

### [pyqtgraph](https://github.com/pyqtgraph/pyqtgraph)

![](https://img.shields.io/github/stars/pyqtgraph/pyqtgraph?style=flat-square&label=⭐) · appears in 2 lists

Interactive and realtime 2D/3D/Image plotting and science/engineering widgets.

> **AI analysis:** Plotting interactivo 2D/3D para ciencia e ingeniería. Basado en Qt, rápido, menos overhead que Matplotlib. Útil para dashboards en vivo, análisis interactivo. Estándar en labs.

**Strengths:** _Performance superior a Matplotlib en datasets grandes/updates frecuentes_ · _Widgets especializados (curves, grids, ROI tools) para ciencia_

**Tags:** `python` `visualization` `qt` `plotting` `interactive`

---

### [QuestDB](https://github.com/questdb/questdb)

![](https://img.shields.io/github/stars/questdb/questdb?style=flat-square&label=⭐) · appears in 2 lists

High-performance SQL database for time series. Supports InfluxDB line protocol, PostgreSQL wire protocol, and REST.

> **AI analysis:** Base de datos SQL de alto rendimiento para series de tiempo. Soporta protocolos InfluxDB y PostgreSQL. Resuelve el problema real de consultas rápidas en volúmenes masivos de datos temporales con latencia baja.

**Strengths:** _Ingesta ultra-rápida de datos (millones de puntos/segundo)_ · _Compresión nativa y queries complejas sin denormalización_

**Tags:** `timeseries` `sql` `java` `high-performance` `olap`

---

### [ReactiveSearch](https://github.com/appbaseio/reactivesearch)

![](https://img.shields.io/github/stars/appbaseio/reactivesearch?style=flat-square&label=⭐) · appears in 2 lists

_(label: good first issue-:wave:)_ <br> A UI components library for Elasticsearch: Available for React, Vue and React Native.

> **AI analysis:** Librería React/Vue de componentes UI para Elasticsearch. Acelera construcciones de dashboards de búsqueda. Útil en nicho específico pero no resuelve problema genérico.

**Strengths:** _Integración nativa con Elasticsearch queries_ · _Componentes ready-to-use para filtros y resultados_

**Tags:** `react` `vue` `elasticsearch` `ui-components` `search`

---

### [Redash](https://redash.io)

appears in 2 lists

Connect and query your data sources, build dashboards to visualize data and share them with your company.

> **AI analysis:** Dashboard open-source más ligero que Metabase. Para startups que quieren BI sin overhead. SQL-first, menos UX pero más control técnico.

**Strengths:** _SQL como primera clase, queries explícitas_ · _Deploy muy liviano, bajo memory footprint_

**Tags:** `bi` `dashboard` `bsd` `sql-first` `docker`

---

### [Rerun](https://github.com/rerun-io/rerun)

![](https://img.shields.io/github/stars/rerun-io/rerun?style=flat-square&label=⭐) · appears in 2 lists

- Rerun is an open-source SDK for logging, storing, querying, and visualizing multimodal data, designed for robotics, computer vision, and spatial AI.

> **AI analysis:** SDK open-source para logging y visualización de datos multimodales en robotics y computer vision. Queries, replay y debugging de datos espaciales complejos sin infraestructura pesada.

**Strengths:** _Visualización interactiva 3D/multimodal integrada, no requiere Jupyter_ · _Query language permite inspeccionar datos sin código_

**Tags:** `visualization` `robotics` `spatial-ai` `rust` `python-bindings`

---

### [RisingWave](https://github.com/risingwavelabs/risingwave)

![](https://img.shields.io/github/stars/risingwavelabs/risingwave?style=flat-square&label=⭐) · appears in 2 lists

- A distributed SQL streaming database that unifies stream processing and low-latency serving, ideal for building and serving features for online machine learning.

> **AI analysis:** DB streaming SQL distribuida: unifica stream processing + low-latency serving. Caso de uso ML feature serving real. Rust, PostgreSQL-compatible. Productiva pero nicho (stream + feature store).

**Strengths:** _Feature store + stream en una herramienta (elimina duplicación)_ · _PostgreSQL wire protocol, tooling existing_

**Tags:** `rust` `streaming` `sql` `feature-store` `distributed`

---

### [ticker](https://github.com/achannarasappa/ticker)

![](https://img.shields.io/github/stars/achannarasappa/ticker?style=flat-square&label=⭐) · appears in 2 lists

Terminal stock watcher and stock position tracker.

> **AI analysis:** Módulo Go para indicadores técnicos de stocks, estrategias, backtesting. Coverage de análisis TA completo. Para quienes necesitan framework de trading sistemático en Go.

**Strengths:** _Suite completa TA (50+ indicadores, estrategias prebuilt)_ · _Backtesting framework integrado, performance Go nativo_

**Tags:** `go` `technical-analysis` `indicators` `backtesting` `trading`

---

### [Vaex](https://github.com/vaexio/vaex)

![](https://img.shields.io/github/stars/vaexio/vaex?style=flat-square&label=⭐) · appears in 2 lists

Vaex is a high performance Python library for lazy Out-of-Core DataFrames (similar to Pandas), to visualize and explore big tabular datasets. Vaex uses memory mapping, zero memory copy policy and lazy computations for best performance (no memory wasted).

> **AI analysis:** Librería Python para DataFrames lazy out-of-core con memory mapping. Para datasets que no entran en RAM, similar a Pandas pero vectorizado. Resuelve bottleneck real de memoria.

**Strengths:** _Memory mapping inteligente, cero copia de datos_ · _API similar a Pandas, curva de aprendizaje chica_

**Tags:** `python` `dataframe` `big-data` `out-of-core` `performance`

---

### [Vega-Altair](https://github.com/vega/altair)

![](https://img.shields.io/github/stars/vega/altair?style=flat-square&label=⭐) · appears in 2 lists

- Vega-Altair is a declarative statistical visualization library for Python.

> **AI analysis:** Grammar of graphics declarativa para Python. Gráficos interactivos web sin JavaScript. Ideal para dashboards y exploración, pero menos control que D3/Plotly.

**Strengths:** _Sintaxis limpia y composable_ · _Exporta a HTML standalone con Vega.js eficiente_

**Tags:** `visualization` `declarative` `interactive` `vega` `python`

---

### [vispy](https://github.com/vispy/vispy)

![](https://img.shields.io/github/stars/vispy/vispy?style=flat-square&label=⭐) · appears in 2 lists

GPU-based high-performance interactive OpenGL 2D/3D data visualization library.

> **AI analysis:** Vispy: GPU OpenGL para viz 2D/3D high-performance. Activa, comunidad científica. Mejor que Matplotlib para datos grandes, menos completa que Three.js para web. Niche pero sólido.

**Strengths:** _Rendimiento GPU nativo, maneja millones de puntos_ · _API Python limpia para científicos_

**Tags:** `python` `gpu` `visualization` `opengl` `scientific`

---

### [vizzu](https://github.com/vizzuhq/vizzu-lib)

![](https://img.shields.io/github/stars/vizzuhq/vizzu-lib?style=flat-square&label=⭐) · appears in 2 lists

Library for animated data visualizations and data stories.

> **AI analysis:** Librería especializada en animaciones y narrativa de datos. Menos widespread que ECharts pero enfoque diferente (data storytelling). Vale probar si necesitás animations fluidas.

**Strengths:** _Animaciones smooth entre estados de datos_ · _API pensada para narrativa (data stories)_

**Tags:** `dataviz` `animation` `javascript`

---

### [yfinance](https://github.com/ranaroussi/yfinance)

![](https://img.shields.io/github/stars/ranaroussi/yfinance?style=flat-square&label=⭐) · appears in 2 lists

`Python` - Yahoo! Finance market data downloader (+faster Pandas Datareader).

> **AI analysis:** Downloader de datos de Yahoo Finance para Python. Standard de facto para prototipos/research financiero. Funciona pero Yahoo cambia APIs frecuentemente.

**Strengths:** _Sintaxis simple, comunidad grande_ · _Cubre la mayoría de activos (stocks, cryptos, ETFs)_

**Tags:** `finance` `data-fetching` `python` `stock-market`

---


---

<sub>📄 Auto-generated from [juanchi.dev](https://juanchi.dev) · [system source](https://juanchi.dev/blog/series/awesome-curated) · MIT licensed</sub>
