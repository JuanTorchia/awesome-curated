# 🛠️ DevOps — Awesome Curated

<p><sub>← [Volver al main](../README.es.md)</sub></p>

**18 GEMs · 34 Vale probar**

---

## ⭐ GEMs — estándares de la industria

Herramientas que la comunidad considera default. Si no las conocés, valen la pena.

### [RLlib](https://github.com/ray-project/ray)

![](https://img.shields.io/github/stars/ray-project/ray?style=flat-square&label=⭐) · aparece en 3 listas

RLlib is an industry level, highly scalable RL library for tf and torch, based on Ray. It's used by companies like Amazon and Microsoft to solve real-world decision making problems at scale.

> **Análisis IA:** RL framework distributed basado en Ray. Para empresas que necesitan scale: Amazon/Microsoft lo usan. Resuelve: entrenar agentes complejos en clusters sin morir en el intento.

**Fortalezas:** _Distribución automática sin boilerplate_ · _Integración tight con Ray ecosystem (tune, serve)_

**Tags:** `reinforcement-learning` `ray` `python` `distributed` `pytorch`

---

### [ZooKeeper](https://zookeeper.apache.org)

aparece en 3 listas

ZooKeeper is a centralized service for maintaining configuration information, naming, providing distributed synchronization, and providing group services.

> **Análisis IA:** Servicio centralizado de coordinación distribuida (config, naming, sync). Apache-maduro. Estándar para Kafka, HDFS, HBase pero overhead significativo para casos simples.

**Fortalezas:** _Garantías ACID robustas en operaciones distribuidas_ · _Usado exitosamente en prod masivo (Netflix, Uber)_

**Tags:** `java` `distributed-coordination` `apache` `consensus`

---

### [Ansible](https://github.com/ansible/ansible)

![](https://img.shields.io/github/stars/ansible/ansible?style=flat-square&label=⭐) · aparece en 2 listas

_(label: easyfix)_ <br> A simple IT automation platform

> **Análisis IA:** Ansible automatiza deploy e infraestructura vía agentless SSH. Estándar de la industria para IaC en empresas mid-to-large. Curva aprendizaje suave, YAML-based.

**Fortalezas:** _Agentless (solo SSH), learning curve suave, librerías built-in exhaustivas_ · _Excelente documentación y comunidad mature_

**Tags:** `infrastructure-as-code` `automation` `ssh` `python`

---

### [BorgBackup](https://github.com/borgbackup/borg)

![](https://img.shields.io/github/stars/borgbackup/borg?style=flat-square&label=⭐) · aparece en 2 listas

_(label: easy)_ <br> Deduplicating backup program with compression and authenticated encryption.

> **Análisis IA:** Herramienta de backup deduplicando con compresión y encriptación. Resuelve backups confiables en servidores y NAS sin ocupar espacio innecesario. Estándar en infraestructuras críticas.

**Fortalezas:** _Deduplicación a nivel byte muy eficiente_ · _Encriptación nativa sin dependencias externas_

**Tags:** `backup` `deduplication` `encryption` `python` `self-hosted`

---

### [cadvisor](https://github.com/google/cadvisor)

![](https://img.shields.io/github/stars/google/cadvisor?style=flat-square&label=⭐) · aparece en 2 listas

Analyzes resource usage and performance characteristics of running containers.

> **Análisis IA:** cAdvisor es una herramienta sólida y probada de Google para monitoreo de contenedores. Si corrés Docker o Kubernetes y necesitás métricas de CPU, memoria, red y disco por contenedor, esto es lo que usás. No es hype: es infraestructura real que alimenta stacks de observabilidad serios (Prometheus + Grafana). El problema es que solo es el recolector; necesitás otra capa para almacenar y visualizar. Esencial en setups productivos con contenedores, pero no reemplaza un stack de monitoreo completo.

**Fortalezas:** _Integración nativa con Prometheus: expone métricas listas para scraping sin configuración compleja_ · _Respaldado y mantenido por Google, ampliamente probado en entornos de producción a escala_ · _Granularidad por contenedor: CPU, memoria, red y filesystem con historial de rendimiento_

**Tags:** `containers` `monitoring` `docker` `kubernetes` `metrics`

---

### [cadvisor](https://github.com/google/cadvisor)

![](https://img.shields.io/github/stars/google/cadvisor?style=flat-square&label=⭐) · aparece en 2 listas

Analyzes resource usage and performance characteristics of running containers.

> **Análisis IA:** Analyzes resource usage de containers (CPU, RAM, I/O). Built by Google, standard en Kubernetes. Production-grade monitoring.

**Fortalezas:** _Integración nativa Kubernetes, es el estándar_ · _Overhead mínimo, escala a miles de containers_

**Tags:** `containers` `monitoring` `go` `kubernetes` `metrics`

---

### [CML](https://github.com/iterative/cml)

![](https://img.shields.io/github/stars/iterative/cml?style=flat-square&label=⭐) · aparece en 2 listas

A library for doing continuous integration with ML projects. Use GitHub Actions & GitLab CI to train and evaluate models in production like environments and automatically generate visual reports with metrics and graphs in pull/merge requests. Framework & language agnostic.

> **Análisis IA:** CI/CD agnóstico para ML: entrena modelos en runners de GitHub/GitLab y genera reportes visuales automáticos. Soluciona reproducibilidad y documentación de experimentos en PRs. Maduro y pragmático.

**Fortalezas:** _Integración nativa GitHub/GitLab sin overhead_ · _Genera reportes visuales automáticos inline_

**Tags:** `ci-cd` `mlops` `github-actions` `gitops` `ml-pipeline`

---

### [Concourse](https://concourse-ci.org)

aparece en 2 listas

Concourse is a CI tool that treats pipelines as first class objects and containerizes every step along the way. )

> **Análisis IA:** CI open-source escrito en Go que trata pipelines como first-class objects, containeriza cada paso. Alternativa self-hosted a Jenkins, enfoque declarativo y limpio.

**Fortalezas:** _Arquitetura limpia, pipelines reproducibles, excelente para microservicios_ · _Self-hosted, Apache 2.0, sin vendor lock-in_

**Tags:** `ci-cd` `go` `self-hosted` `open-source` `containers`

---

### [Consul](https://consul.io)

aparece en 2 listas

Consul is a tool for service discovery, monitoring and configuration.

> **Análisis IA:** Service discovery + config management distribuido, estándar Hashicorp. Crítico en infraestructura cloud/Kubernetes, aunque K8s nativo reemplazó parte de su rol.

**Fortalezas:** _Multi-datacenter nativo, DNS integrado_ · _Monitoring y health checks built-in_

**Tags:** `service-discovery` `go` `distributed` `configuration`

---

### [Docker.DotNet](https://github.com/microsoft/docker.dotnet)

![](https://img.shields.io/github/stars/microsoft/docker.dotnet?style=flat-square&label=⭐) · aparece en 2 listas

C#/.NET HTTP client for the Docker remote API.

> **Análisis IA:** Cliente HTTP .NET/C# para Docker Remote API. Integra operaciones docker programáticamente en aplicaciones .NET. Estándar de facto para devs .NET con Docker.

**Fortalezas:** _Única librería oficial .NET para Docker API, mantenida por Microsoft_ · _Cubre API completa de Docker, bien documentada_

**Tags:** `csharp` `dotnet` `docker-api` `client-library`

---

### [GitLab CI](https://about.gitlab.com/solutions/continuous-integration)

aparece en 2 listas

Gitlab's built-in, full-featured CI/CD solution.

> **Análisis IA:** CI/CD integrado nativo en GitLab. Full-featured, no requiere herramienta externa. Excelente si ya usás GitLab; problema si no.

**Fortalezas:** _Integración perfecta con GitLab (webhooks, auth, repos)_ · _Feature-complete sin dependencias externas_

**Tags:** `cicd` `gitlab` `devops` `pipelines`

---

### [k9s](https://github.com/derailed/k9s)

![](https://img.shields.io/github/stars/derailed/k9s?style=flat-square&label=⭐) · aparece en 2 listas

Kubernetes CLI to manage your clusters in style.

> **Análisis IA:** CLI para Kubernetes que reemplaza kubectl en día a día. Dashboard interactivo, fuzzy search, manejo de recursos en estilo. Imprescindible para ops que viven en k8s.

**Fortalezas:** _Interfaz intuitiva y rápida vs kubectl crudo_ · _Comunidad activa, mantenimiento constante_

**Tags:** `kubernetes` `cli` `golang` `devops`

---

### [Nextcloud](https://nextcloud.com)

aparece en 2 listas

Access and share your files, calendars, contacts, mail and [more](https://apps.nextcloud.com/) from any device, on your terms. )

> **Análisis IA:** Suite cloud open-source tipo Dropbox on-premise. PHP/Docker, muy modular con marketplace de apps. Estándar industrial para self-hosted. Resuelve storage, sync, colaboración, mail. Escala bien.

**Fortalezas:** _Ecosistema robusto de apps integradas_ · _Deployment flexible (Docker, bare metal)_

**Tags:** `cloud-storage` `self-hosted` `php` `docker` `collaboration`

---

### [pm2](https://github.com/unitech/pm2)

![](https://img.shields.io/github/stars/unitech/pm2?style=flat-square&label=⭐) · aparece en 2 listas

Production Process Manager for Node.js.

> **Análisis IA:** Process manager Node.js estándar industria: clustering, reload zero-downtime, monitoreo. 16+ años, 4M+ weekly downloads. Alternativa (Supervisor, systemd) existen pero pm2 domina Node ecosystem.

**Fortalezas:** _Zero-downtime restarts_ · _Clustering automático multi-core_

**Tags:** `node.js` `process-manager` `production` `clustering`

---

### [Prometheus](https://prometheus.io)

aparece en 2 listas

Service monitoring system and time series database.

> **Análisis IA:** Time-series database y monitoring system open-source escrito en Go. No exclusivo Docker pero standard para containerized envs. TSDB + alerting combina.

**Fortalezas:** _Estándar industry para metrics en containers/Kubernetes, simple e eficiente_ · _Pull-model, no requiere agentes, bajo overhead_

**Tags:** `monitoring` `tsdb` `go` `open-source` `observability`

---

### [SaltStack](https://github.com/saltstack/salt)

![](https://img.shields.io/github/stars/saltstack/salt?style=flat-square&label=⭐) · aparece en 2 listas

_(label: good first issue)_ <br> Software to automate the management and configuration of any infrastructure or application at scale.

> **Análisis IA:** Orquestación y config management en escala. Alternativa a Ansible, más compleja pero poderosa. Estándar en DevOps empresarial.

**Fortalezas:** _Event-driven, escalable horizontalmente_ · _Masterless o master-based flexible_

**Tags:** `orchestration` `configuration-management` `python` `devops`

---

### [scapy](https://github.com/secdev/scapy)

![](https://img.shields.io/github/stars/secdev/scapy?style=flat-square&label=⭐) · aparece en 2 listas

Python-based interactive packet manipulation program and library.

> **Análisis IA:** Librería Python para manipular paquetes de red a nivel bajo. Herramienta clásica para pentesting, network debugging y análisis de tráfico. Resuelve crafteo de packets complejos.

**Fortalezas:** _API flexible para construir packets arbitrarios y procesar capturados_ · _Estándar de facto en pentesting y research de seguridad_

**Tags:** `python` `networking` `packets` `security` `low-level`

---

### [Træfɪk](https://github.com/containous/traefik)

![](https://img.shields.io/github/stars/containous/traefik?style=flat-square&label=⭐) · aparece en 2 listas

Automated reverse proxy and load-balancer for Docker, Mesos, Consul, Etcd... By [EmileVauge](https://github.com/emilevauge).

> **Análisis IA:** Reverse proxy y load balancer automático. Descubre servicios en Docker/K8S/Consul. Reemplaza nginx manual. Simplifica mucho ops.

**Fortalezas:** _Service discovery automático, no recargas nginx_ · _HTTPS/Let's Encrypt integrado, SSL sin drama_

**Tags:** `reverse-proxy` `load-balancer` `docker` `kubernetes` `go`

---


---

## 👍 Vale probar — sólidas en su nicho

Menos hype que las GEMs, pero confiables si caés en su caso de uso.

### [Bencher](https://bencher.dev)

aparece en 4 listas

Suite of continuous benchmarking tools designed to catch performance regressions in CI.

> **Análisis IA:** Suite de benchmarking en CI escrita en Rust. Atrapa regresiones de performance en PR; menos conocida que alternatives pero solid.

**Fortalezas:** _Detección de regresiones con tolerancia configurable_ · _API HTTP para integraciones custom_

**Tags:** `benchmarking` `ci-cd` `rust`

---

### [Dragonfly](https://github.com/dragonflyoss/dragonfly2)

![](https://img.shields.io/github/stars/dragonflyoss/dragonfly2?style=flat-square&label=⭐) · aparece en 3 listas

Provide efficient, stable and secure file distribution and image acceleration based on p2p technology to be the best practice and standard solution in cloud native architectures.

> **Análisis IA:** P2P para distribución de archivos e imágenes OCI en cloud native. Pull decentralizado en lugar de todos pedir al registry central. Resuelve: throttling, latencia, costo de ancho hacia registry externo.

**Fortalezas:** _Reduce carga en registry central y costo de egress a internet_ · _Compatible con estándares OCI; integra con containerd/Docker nativo_

**Tags:** `p2p` `oci-images` `container-registry` `distributed-systems` `go`

---

### [bandwhich](https://github.com/imsnif/bandwhich)

![](https://img.shields.io/github/stars/imsnif/bandwhich?style=flat-square&label=⭐) · aparece en 2 listas

Track bandwidth utilization by process.

> **Análisis IA:** Herramienta de monitoreo de ancho de banda por proceso. Útil para debugging de performance en desarrollo y producción. Resuelve el problema real de identificar qué proceso consume recursos.

**Fortalezas:** _Precisión en per-process bandwidth tracking_ · _Interfaz TUI clara y responsiva_

**Tags:** `network` `monitoring` `rust` `cli` `performance`

---

### [changedetection.io](https://changedetection.io)

aparece en 2 listas

Stay up-to-date with web-site content changes.

> **Análisis IA:** Monitor de cambios web vía scraping periódico. Soluciona problema real: detectar updates sin suscribirse. Self-hosted, bajo overhead. Comunidad pequeña pero sólida.

**Fortalezas:** _Arquitectura ligera, bajo consumo de recursos_ · _Soporte para múltiples métodos: JSON diff, visual diff, regex_

**Tags:** `web-monitoring` `change-detection` `python` `self-hosted` `docker`

---

### [chasquid](https://blitiri.com.ar/p/chasquid)

aparece en 2 listas

SMTP (email) server with a focus on simplicity, security, and ease of operation.

> **Análisis IA:** SMTP server minimalista en Go. Foco en seguridad, operabilidad simple. Alternativa liviana a Postfix/Exim para setups pequeños o selfhosted. Mantenido activamente, código limpio.

**Fortalezas:** _Footprint mínimo, setup simple, sin configuración retorcida_ · _Seguridad como design principle (TLS requerido, validaciones estrictas)_

**Tags:** `go` `smtp` `email-server` `self-hosted` `security`

---

### [CircleCI](https://circleci.com)

aparece en 2 listas

:yen: Push or pull Docker images from your build environment, or build and run containers right on CircleCI.

> **Análisis IA:** SaaS CI/CD cloud que pushea/pullea imágenes Docker y ejecuta containers en build. Hosted, con free tier limitado. Competencia de GitHub Actions, bueno para legacy.

**Fortalezas:** _Soporte docker nativo, UI madura, buena para equipos sin infra_ · _Pricing por minutos, flexible_

**Tags:** `ci-cd` `saas` `docker` `cloud`

---

### [ctop](https://github.com/bcicen/ctop)

![](https://img.shields.io/github/stars/bcicen/ctop?style=flat-square&label=⭐) · aparece en 2 listas

interface (e.g. htop) for container metrics.

> **Análisis IA:** htop pero para containers. Monitorea métricas en tiempo real (CPU, memoria, I/O) de múltiples contenedores desde terminal. Imprescindible si manejás Docker/Kubernetes en producción.

**Fortalezas:** _interfaz intuitiva similar a htop_ · _monitoreo en vivo sin overhead_

**Tags:** `cli` `monitoring` `docker` `containers` `go`

---

### [Deployer](https://github.com/deployphp/deployer)

![](https://img.shields.io/github/stars/deployphp/deployer?style=flat-square&label=⭐) · aparece en 2 listas

_(label: good-for-beginner)_ <br> A deployment tool written in PHP with support for popular frameworks out of the box.

> **Análisis IA:** Tool deploy en PHP con soporte frameworks populares. Maduro, usado en producción. Alternativa a Capistrano/Fabric pero para PHP.

**Fortalezas:** _Maduro y estable, comunidad PHP lo usa_ · _Zero-downtime deployments out-of-box_

**Tags:** `php` `deployment` `cli`

---

### [dive](https://github.com/wagoodman/dive)

![](https://img.shields.io/github/stars/wagoodman/dive?style=flat-square&label=⭐) · aparece en 2 listas

A tool for exploring each layer in a docker image. By [wagoodman](https://github.com/wagoodman).

> **Análisis IA:** Herramienta para inspeccionionar layers de Docker images. Práctica para debugging de builds, comunidad activa, pero nicho específico.

**Fortalezas:** _UI interactiva clara, muy útil para analizar tamaño de layers_ · _Mantenida activamente_

**Tags:** `docker` `go` `debugging` `cli`

---

### [docker-volume-backup](https://github.com/offen/docker-volume-backup)

![](https://img.shields.io/github/stars/offen/docker-volume-backup?style=flat-square&label=⭐) · aparece en 2 listas

Backup Docker volumes locally or to any S3, WebDAV, Azure Blob Storage, Dropbox or SSH compatible storage.

> **Análisis IA:** Herramienta de backup para volúmenes Docker hacia S3, WebDAV, Azure, Dropbox o SSH. Resuelve urgencia real: automatizar backups sin scripting manual. Ligera, agnóstica de backend.

**Fortalezas:** _Soporta múltiples destinos sin reimplementación_ · _Integración nativa con ecosistema Docker_

**Tags:** `docker` `backup` `s3` `devops`

---

### [dockly](https://github.com/lirantal/dockly)

![](https://img.shields.io/github/stars/lirantal/dockly?style=flat-square&label=⭐) · aparece en 2 listas

An interactive shell UI for managing Docker containers.

> **Análisis IA:** Shell UI interactivo para manejar Docker. Alternativa a docker CLI puro. Útil para DevOps que prefieren TUI.

**Fortalezas:** _Interface visual sobre CLI crudo es más rápido para navegar_ · _Está en GitHub mantenido regularmente_

**Tags:** `docker` `cli` `tui` `containers` `nodejs`

---

### [domcyrus/rustnet](https://github.com/domcyrus/rustnet)

![](https://img.shields.io/github/stars/domcyrus/rustnet?style=flat-square&label=⭐) · aparece en 2 listas

Cross-platform network monitoring TUI with process identification via eBPF/PKTAP and deep packet inspection [](https://github.com/domcyrus/rustnet/actions/workflows/rust.yml) [](https://crates.io/crates/rustnet-monitor)

> **Análisis IA:** Network monitor TUI en Rust con eBPF/PKTAP, process ID + deep packet inspection. Cross-platform, activamente mantenido, herramienta niche pero potente para sysadmins.

**Fortalezas:** _eBPF/PKTAP nativo sin overhead kernel_ · _Process-level network visibility rara en TUI tools_

**Tags:** `network` `tui` `rust` `ebpf` `monitoring`

---

### [Drone](https://github.com/drone/drone)

![](https://img.shields.io/github/stars/drone/drone?style=flat-square&label=⭐) · aparece en 2 listas

Continuous integration server built on Docker and configured using YAML files.

> **Análisis IA:** CI server ligero, Docker-nativo, YAML-first. Estándar en entornos containerizados, alternativa sólida a Jenkins con overhead menor.

**Fortalezas:** _Binario único, deployment trivial_ · _YAML limpio vs XML verboso de Jenkins_

**Tags:** `ci-cd` `docker` `yaml` `go`

---

### [glances](https://nicolargo.github.io/glances)

aparece en 2 listas

Open-source, cross-platform real-time monitoring tool with CLI and web dashboard interfaces and many exporting options.

> **Análisis IA:** Glances es un monitor de sistema ligero con CLI interactivo y dashboard web. Cubre CPU, RAM, disco, red, procesos. Útil para troubleshooting rápido en servers sin overhead.

**Fortalezas:** _Instalación one-liner y sin dependencias pesadas_ · _Exporta a Prometheus, CSV, JSON_

**Tags:** `monitoring` `cli` `python` `cross-platform` `lightweight`

---

### [HertzBeat](https://github.com/dromara/hertzbeat)

![](https://img.shields.io/github/stars/dromara/hertzbeat?style=flat-square&label=⭐) · aparece en 2 listas

An open-source real-time monitoring system with custom-monitor and agentless.

> **Análisis IA:** Sistema de monitoreo open-source real-time, agentless, custom-monitors. Para DevOps/SRE que necesitan observabilidad sin vendor lock.

**Fortalezas:** _Agentless reduces operational overhead_ · _Custom monitors permite casos de uso flexibles_

**Tags:** `monitoring` `observability` `agentless` `open-source`

---

### [lazydocker](https://github.com/jesseduffield/lazydocker)

![](https://img.shields.io/github/stars/jesseduffield/lazydocker?style=flat-square&label=⭐) · aparece en 2 listas

The lazier way to manage everything docker. A simple terminal UI for both docker and docker-compose, written in Go with the gocui library. By [jesseduffield](https://github.com/jesseduffield).

> **Análisis IA:** TUI terminal para Docker y docker-compose en Go. Simplifica operaciones cotidianas de contenedores sin dejar la CLI. Resuelve la fricción de memorizar comandos docker complejos.

**Fortalezas:** _Interfaz intuitiva que acelera workflows docker en desarrollo_ · _Ligera, binario único, sin dependencias externas_

**Tags:** `cli` `go` `docker` `tui` `devops`

---

### [lazyjournal](https://github.com/lifailon/lazyjournal)

![](https://img.shields.io/github/stars/lifailon/lazyjournal?style=flat-square&label=⭐) · aparece en 2 listas

A interface for reading and filtering the logs output of Docker and Podman containers like [Dozzle](dozzle) but for the terminal with support for fuzzy find, regex and output coloring.

> **Análisis IA:** Interfaz terminal para logs de Docker/Podman con fuzzy find, regex y coloring. Alternativa TUI a Dozzle, útil para devops que viven en terminal.

**Fortalezas:** _Fuzzy search integrado en logs_ · _Soporte para Podman además de Docker_

**Tags:** `docker` `podman` `logging` `tui` `cli`

---

### [localtunnel](https://github.com/localtunnel/localtunnel)

![](https://img.shields.io/github/stars/localtunnel/localtunnel?style=flat-square&label=⭐) · aparece en 2 listas

Expose your localhost to the world.

> **Análisis IA:** Tunneling inverso para exponer localhost. Para demos rápidas, webhooks en desarrollo, testing remoto. Soluciona problema real pero con riesgos de seguridad si se descuida.

**Fortalezas:** _Setup instantáneo, cero config_ · _URLs públicas generadas automáticamente sin registrarse_

**Tags:** `tunneling` `networking` `demo` `node`

---

### [Luigi](https://github.com/spotify/luigi)

![](https://img.shields.io/github/stars/spotify/luigi?style=flat-square&label=⭐) · aparece en 2 listas

- Luigi is a Python module that helps you build complex pipelines of batch jobs, handling dependency resolution, workflow management, visualisation, etc..

> **Análisis IA:** Framework Python para pipelines de batch jobs complejos. Maneja dependencias, workflows y visualización. Spotify lo usa en producción. Alternativa ligera a Airflow para equipos medianos.

**Fortalezas:** _API simple y pythónica_ · _Excelente para pipelines medianos sin overhead de infraestructura_

**Tags:** `python` `workflow` `batch` `dag` `spotify`

---

### [MeshCentral](https://meshcentral.com)

aparece en 2 listas

Run your own web server to remotely manage and control computers on a local network or anywhere on the internet.

> **Análisis IA:** Suite de remote management (RDP/SSH/terminal) via web. Node.js + Apache-2.0. Alternativa moderna a TeamViewer/AnyDesk self-hosted. Resuelve problema real pero vendor lock-in al stack Node.

**Fortalezas:** _UI web pulida, terminal remota + file manager integrados_ · _Manejo de múltiples agentes simultáneamente sin fricción_

**Tags:** `nodejs` `remote-management` `web-ui` `self-hosted`

---

### [MyIP](https://github.com/jason5ng32/myip)

![](https://img.shields.io/github/stars/jason5ng32/myip?style=flat-square&label=⭐) · aparece en 2 listas

All in one IP Toolbox. Easy to check all your IPs, IP geolocation, check for DNS leaks, examine WebRTC connections, speed test, ping test, MTR test, check website availability, whois search and more. By [jason5ng32](https://github.com/jason5ng32).

> **Análisis IA:** Toolbox IP todo-en-uno: geolocación, DNS leak check, WebRTC test, speed/ping/MTR, whois. Vue.js frontend. Útil para netops/devops diagnosing. No resuelve problema profundo, es conveniente consolidation.

**Fortalezas:** _UI limpia agrupando tools dispersas, cero instalación (web)_ · _Integra funciones que típicamente requieren múltiples tools CLI_

**Tags:** `vue` `network-tools` `ip-tools` `frontend`

---

### [netdata/netdata#Netdata](https://github.com/netdata/netdata)

![](https://img.shields.io/github/stars/netdata/netdata?style=flat-square&label=⭐) · aparece en 2 listas

🎖️ 🏠 ☁️ 📟 🍎 🪟 🐧 - Discovery, exploration, reporting and root cause analysis using all observability data, including metrics, logs, systems, containers, processes, and network connections

> **Análisis IA:** Observabilidad full-stack: métricas, logs, containers, procesos, red. UI nativa sin Grafana. Buena para infraestructura on-prem con pocos recursos. Integración real pero UI menos pulida que competencia.

**Fortalezas:** _Agente lightweight, baja huella de memoria_ · _RCA integrado sin saltar entre herramientas_

**Tags:** `observability` `metrics` `self-hosted` `c` `agent-based`

---

### [nwiizo/tfmcp](https://github.com/nwiizo/tfmcp)

![](https://img.shields.io/github/stars/nwiizo/tfmcp?style=flat-square&label=⭐) · aparece en 2 listas

🦀 🏠 - A Terraform MCP server allowing AI assistants to manage and operate Terraform environments, enabling reading configurations, analyzing plans, applying configurations, and managing Terraform state.

> **Análisis IA:** MCP server para Terraform, permite a IAs manejar IaC. Arquitectura interesante pero MCP es todavía experimental. Promesa alta pero adopción temprana, riesgos de breaking changes.

**Fortalezas:** _Primer bridge serio entre IAs y Terraform state_ · _Sandboxing seguro de operaciones IaC_

**Tags:** `terraform` `mcp` `ai` `infrastructure`

---

### [orhun/rustypaste](https://github.com/orhun/rustypaste)

![](https://img.shields.io/github/stars/orhun/rustypaste?style=flat-square&label=⭐) · aparece en 2 listas

A minimal file upload/pastebin service

> **Análisis IA:** Pastebin/upload minimalista en Rust. Blazing-fast, self-hosted, sin dependencias pesadas. Para equipos que necesitan control y velocidad sin complejidad.

**Fortalezas:** _Binario estático, deployment trivial_ · _Performance excelente incluso bajo carga_

**Tags:** `rust` `self-hosted` `file-upload` `minimal`

---

### [Outline Server](https://getoutline.org)

aparece en 2 listas

A proxy server that runs a Shadowsocks instance for each access key and a REST API to manage the access keys.

> **Análisis IA:** Servidor proxy Shadowsocks self-hosted moderno. REST API para gestión keys. Docker/Node. Alternativa abierta a VPN comerciales. Admin cómodo pero requiere ops skills.

**Fortalezas:** _API REST para automation_ · _Ligero en recursos_

**Tags:** `proxy` `shadowsocks` `docker` `nodejs` `self-hosted`

---

### [oxker](https://github.com/mrjackwills/oxker)

![](https://img.shields.io/github/stars/mrjackwills/oxker?style=flat-square&label=⭐) · aparece en 2 listas

A simple tui to view & control docker containers. Written in [Rust](https://rust-lang.org/), making heavy use of [ratatui](https://github.com/tui-rs-revival/ratatui) & [Bollard](https://github.com/fussybeaver/bollard),.

> **Análisis IA:** TUI minimalista en Rust para gestionar containers Docker. Interfaz simple, construida con ratatui y Bollard. Útil para devs que viven en terminal, pero no reemplaza docker CLI + dashboards.

**Fortalezas:** _Interfaz responsiva en terminal, cero overhead_ · _Código limpio Rust, muy mantenible_

**Tags:** `rust` `tui` `docker` `terminal` `ratatui`

---

### [Pomerium](https://pomerium.io)

aparece en 2 listas

Identity-aware reverse proxy, successor to now obsolete oauth_proxy. It inserts an OAuth step before proxying your request to the backend, so that you can safely expose your self-hosted websites to public Internet.

> **Análisis IA:** Reverse proxy con OAuth/identity-aware routing. Simplifica exposición segura de internals. Go-based, Docker-ready. Sucesor de oauth_proxy abandonado.

**Fortalezas:** _Solución completa (auth + routing + TLS)_ · _Lightweight vs API gateways monolíticos_

**Tags:** `reverse-proxy` `oauth` `identity` `go` `security`

---

### [Prefect Core](https://github.com/prefecthq/prefect)

![](https://img.shields.io/github/stars/prefecthq/prefect?style=flat-square&label=⭐) · aparece en 2 listas

- Workflow management system that makes it easy to take your data pipelines and add semantics like retries, logging, dynamic mapping, caching, failure notifications, and more.

> **Análisis IA:** Orquestador de workflows con abstracciones para retry, caching, logging. Alternativa a Airflow menos pesada. Resuelve problema: ejecutar DAGs complejos con resiliencia sin montar infraestructura pesada.

**Fortalezas:** _API Pythonica más limpia que Airflow, menos dependencias_ · _Async-first, mejor performance en workflows I/O bound_

**Tags:** `python` `workflow-orchestration` `dag` `job-scheduler` `etl`

---

### [QEMU](https://qemu.org)

aparece en 2 listas

A free and open-source emulator and virtualizer that can perform hardware virtualization. [![Open-Source Software][OSS Icon]](https://github.com/qemu/qemu) ![Freeware][Freeware Icon]

> **Análisis IA:** Virtualizador multiplataforma de Oracle. GUI pulida, snapshot, clonado. Gratuito con GPL/CDDL. Accesible a principiantes, menos overhead que Hyper-V.

**Fortalezas:** _GUI intuitiva, snapshots reversibles_ · _Ligero en recursos, setup rápido_

**Tags:** `virtualization` `vm` `gui` `freeware`

---

### [ryot](https://github.com/ignisda/ryot)

![](https://img.shields.io/github/stars/ignisda/ryot?style=flat-square&label=⭐) · aparece en 2 listas

Track various facets of your life - media, fitness, etc.

> **Análisis IA:** Aplicación de tracking personal para media, fitness y vida en general. Docker-ready, GPL-3.0. Resuelve bien la necesidad de centralizar datos personales sin vendor lock-in.

**Fortalezas:** _Arquitectura modular con Docker_ · _Código abierto GPL-3.0 sin restricciones_

**Tags:** `self-hosted` `docker` `tracking` `privacy-first`

---

### [s5cmd](https://github.com/peak/s5cmd)

![](https://img.shields.io/github/stars/peak/s5cmd?style=flat-square&label=⭐) · aparece en 2 listas

Blazing fast S3 and local filesystem execution tool.

> **Análisis IA:** CLI para operaciones S3 en paralelo, escrito en Go. Resuelve transfers masivos rápido. Para devops/data engineers que usan AWS S3 y necesitan velocidad bruta.

**Fortalezas:** _Ejecución paralela nativa, significativamente más rápido que aws-cli_ · _Sintaxis simple, cero configuración AWS extra_

**Tags:** `cli` `s3` `go` `parallel` `aws`

---

### [Semaphore CI](https://semaphore.io)

aparece en 2 listas

yen: — A high-performance cloud solution that makes it easy to build, test and ship your containers to production.

> **Análisis IA:** SaaS CI/CD cloud optimizada para build, test y ship de containers a producción. High-performance, DX enfocado. Competencia directa CircleCI, GitHub Actions.

**Fortalezas:** _Performance destacada, container-first design, UX limpia_ · _Free tier generoso, bueno para startups_

**Tags:** `ci-cd` `saas` `docker` `cloud`

---

### [SinTan1729/Chhoto URL](https://github.com/sintan1729/chhoto-url)

![](https://img.shields.io/github/stars/sintan1729/chhoto-url?style=flat-square&label=⭐) · aparece en 2 listas

A simple, blazingly fast, selfhosted URL shortener with no unnecessary features.[](https://github.com/SinTan1729/chhoto-url/actions/workflows/docker-release.yml)

> **Análisis IA:** URL shortener minimalista self-hosted en Rust. Rápido, sin bloat, perfecto para quien necesita control total sin complejidad innecesaria.

**Fortalezas:** _Binario compilado ultra-ligero, fácil deployment_ · _Cero dependencias de terceros, control total del data_

**Tags:** `rust` `self-hosted` `url-shortener` `cli`

---

### [sshuttle](https://github.com/sshuttle/sshuttle)

![](https://img.shields.io/github/stars/sshuttle/sshuttle?style=flat-square&label=⭐) · aparece en 2 listas

Transparent proxy server that works as a poor man's VPN.

> **Análisis IA:** Proxy transparente basado en SSH que actúa como VPN económica. Establece túnel sobre SSH existente sin overhead de protocolo VPN. Para quien necesita bypass de redes sin herramientas pesadas.

**Fortalezas:** _Usa SSH existente, sin credenciales extra_ · _Bajo overhead, overhead, funciona en conexiones lentas_

**Tags:** `vpn` `proxy` `ssh` `cli` `python`

---


---

<sub>📄 Generado automáticamente desde [juanchi.dev](https://juanchi.dev) · [código del sistema](https://juanchi.dev/blog/series/awesome-curated) · MIT licensed</sub>
