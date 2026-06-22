# 🔐 Segurança e Cripto — Awesome Curated

<p><sub>← [Voltar ao main](../README.pt-BR.md)</sub></p>

**1 Human-reviewed · 0 Popular standards · 46 AI candidates · 11 Needs review**

---

## Human-reviewed picks

Tools with a human review label and visible caveats.

### 👤 [themis](https://github.com/cossacklabs/themis)

![](https://img.shields.io/github/stars/cossacklabs/themis?style=flat-square&label=⭐) · 🔥 **Found in 4 active sources: matteocrippa/awesome-swift, akullpp/awesome-java, rust-unofficial/awesome-rust +1 more**

**Review label:** Human Pick · **Caveat:** Security-sensitive tool; evaluate fit and maintenance posture before production use.

High level crypto library for storing data (AES), secure messaging (ECC + ECDSA / RSA + PSS + PKCS#7) and session-oriented, forward secrecy data exchange (ECDH key agreement, ECC & AES encryption). Ported on many languages and platforms, suitable for client-server infastructures.

> **Análise IA:** Esto es valor real. Themis resuelve el problema de siempre: los devs necesitan criptografía seria pero la API de bajo nivel de OpenSSL los mata. Themis ofrece primitivas de alto nivel (cifrado simétrico, mensajería segura, sesiones con forward secrecy) sin que tengas que entender los detalles del protocolo. El soporte multi-lenguaje y multi-plataforma es el diferencial genuino. Ideal para equipos que construyen apps móviles o client-server que manejan datos sensibles y no quieren inventar su propia crypto. No es humo.

**Pontos fortes:** _Abstracción de alto nivel sobre primitivas criptográficas complejas (ECC, AES, ECDH) sin sacrificar seguridad real_ · _Soporte genuino multi-lenguaje y multi-plataforma, útil para equipos con stacks heterogéneos_ · _Incluye forward secrecy en sesiones, algo que muchos devs ignoran y que es crítico para datos sensibles_

**Tags:** `cryptography` `security` `multi-platform` `open-source` `encryption`

---


---

## AI candidates

Automated candidates with enough source signal; these are not human endorsements yet.

### [Agentic Radar](https://github.com/splx-ai/agentic-radar)

![](https://img.shields.io/github/stars/splx-ai/agentic-radar?style=flat-square&label=⭐) · Found in 1 active source: josephmisiti/awesome-machine-learning

**Review label:** AI Candidate · **Caveat:** Candidate still needs human review before endorsement.

Open-source CLI security scanner for agentic workflows. Scans your workflow’s , detects vulnerabilities, and generates an interactive visualization along with a detailed security report. Supports LangGraph, CrewAI, n8n, OpenAI Agents, and more.

> **Análise IA:** CLI security scanner para agentic workflows (LangGraph, CrewAI, n8n). Detecta vulnerabilidades en código de agentes, genera reportes. Resuelve problema real: auditar workflows LLM antes de prod.

**Pontos fortes:** _Soporte multi-framework, case de uso urgente (seguridad agentic)_ · _Output visualizable e insights accionables_

**Tags:** `security` `cli` `agentic-workflows` `langraph` `crewai`

---

### [Apache Shiro](https://shiro.apache.org)

Found in 1 active source: akullpp/awesome-java

**Review label:** AI Candidate · **Caveat:** Candidate still needs human review before endorsement.

Performs authentication, authorization, cryptography and session management.

> **Análise IA:** Framework Apache para autenticación, autorización, criptografía, sesiones. Alternativa a Spring Security. Maduro pero peso pesado.

**Pontos fortes:** _Feature-complete, soporta realm-based auth_ · _Integración simple en apps Java/JVM existentes_

**Tags:** `java` `authentication` `authorization` `security` `apache`

---

### [Bouncy Castle](https://bouncycastle.org/java.html)

Found in 1 active source: akullpp/awesome-java

**Review label:** AI Candidate · **Caveat:** Candidate still needs human review before endorsement.

All-purpose cryptographic library and JCA provider offering a wide range of functions, from basic helpers to PGP/SMIME operations.

> **Análise IA:** Bouncy Castle es la librería criptográfica estándar en Java. Cobertura completa: cifrados, firma, PGP, SMIME. Usado en producción desde 2000+. Imprescindible para cualquier proyecto que necesite crypto serio en JVM.

**Pontos fortes:** _Cobertura criptográfica exhaustiva y bien auditada_ · _Compatibilidad JCA nativa, integración directa con ecosistema Java_

**Tags:** `java` `cryptography` `jca-provider` `pgp` `smime`

---

### [Brave](https://brave.com)

Found in 2 active sources: jivoi/awesome-osint, jaywcjlove/awesome-mac

**Review label:** AI Candidate · **Caveat:** Candidate still needs human review before endorsement.

Web browser with an emphasis on privacy and speed. (https://github.com/brave/brave-browser/)

> **Análise IA:** Chromium fork con privacy-first, bloquea tracking default, BAT rewards opcional. Open-source. Rápido, buena compatibilidad. Rival real a Chrome en velocidad y privacidad balanceada.

**Pontos fortes:** _Built-in ad/tracker blocking_ · _Updates respetan preferencias user_

**Tags:** `chromium` `privacy` `browser` `open-source`

---

### [briansmith/ring](https://github.com/briansmith/ring)

![](https://img.shields.io/github/stars/briansmith/ring?style=flat-square&label=⭐) · Found in 1 active source: rust-unofficial/awesome-rust

**Review label:** AI Candidate · **Caveat:** Candidate still needs human review before endorsement.

Safe, fast, small crypto using Rust and BoringSSL's cryptography primitives.

> **Análise IA:** Crypto library Rust wrapping BoringSSL (Google). APIs seguras para primitivos críticos sin memory issues. Usado en Rustls, browsers. Indispensable si necesitás crypto sin paranoia de FFI bugs.

**Pontos fortes:** _Safety guarantees de Rust + auditoría BoringSSL_ · _Performance sin sacrificar seguridad_

**Tags:** `rust` `crypto` `boringssl` `tls`

---

### [Cryptomator](https://cryptomator.org)

Found in 2 active sources: akullpp/awesome-java, jaywcjlove/awesome-mac

**Review label:** AI Candidate · **Caveat:** Candidate still needs human review before endorsement.

Multi-platform transparent client-side encryption of your files in the cloud.

> **Análise IA:** Encriptación client-side transparente para cloud storage. Multiplataforma, open-source, Java-based. Resuelve problema real: confiar en cloud providers sin revelar contenido.

**Pontos fortes:** _Integración transparente con cloud providers_ · _Zero-knowledge por diseño_

**Tags:** `encryption` `client-side` `java` `cross-platform`

---

### [CryptoSwift](https://github.com/krzyzanowskim/cryptoswift)

![](https://img.shields.io/github/stars/krzyzanowskim/cryptoswift?style=flat-square&label=⭐) · Found in 1 active source: matteocrippa/awesome-swift

**Review label:** AI Candidate · **Caveat:** Candidate still needs human review before endorsement.

Crypto related functions and helpers for Swift implemented in Swift programming language.

> **Análise IA:** Criptografía pura Swift (AES, SHA, HMAC, etc.). Para iOS devs que evitan CommonCrypto. Portable, sin dependencias C. Funciona bien pero no domina.

**Pontos fortes:** _Pure Swift, portable entre plataformas_ · _API clara y docs decentes_

**Tags:** `swift` `cryptography` `ios` `aes`

---

### [DNSDumpster](https://dnsdumpster.com)

Found in 1 active source: jivoi/awesome-osint

**Review label:** AI Candidate · **Caveat:** Candidate still needs human review before endorsement.

is a that will help you discover hosts related to a specific domain.

> **Análise IA:** Web tool para enumerar subdominios vía DNS pasivo. Para pentesters que mapean superficie de ataque. Free pero con limitaciones.

**Pontos fortes:** _Interfaz web simple_ · _Rápido para queries ocasionales_

**Tags:** `dns` `recon` `subdomain-enumeration` `web-tool`

---

### [Element](https://element.io)

Found in 1 active source: jaywcjlove/awesome-mac

**Review label:** AI Candidate · **Caveat:** Candidate still needs human review before endorsement.

Create, share communicate. Chat and call securely.

> **Análise IA:** Chat seguro federated basado en Matrix protocol. Open-source, end-to-end encryption. Alternativa a Slack/Discord para orgs que priorizan privacidad.

**Pontos fortes:** _Protocolo abierto federated, no lock-in_ · _E2E encryption por defecto, auditable_

**Tags:** `matrix` `chat` `encrypted` `federation` `open-source`

---

### [Google Hacking Database (GHDB)](https://exploit-db.com/google-hacking-database)

Found in 1 active source: jivoi/awesome-osint

**Review label:** AI Candidate · **Caveat:** Candidate still needs human review before endorsement.

The GHDB is an index of search queries (we call them dorks) used to find publicly available information, intended for pentesters and security researchers.

> **Análise IA:** Índice de Google dorking queries para pentesting. Referencia fundamental. Imprescindible conocer para recon inicial efectivo, zero costo.

**Pontos fortes:** _Cobertura exhaustiva de técnicas google search_ · _Gratuito y mantenido activamente_

**Tags:** `osint` `google-dorking` `recon` `pentesting`

---

### [hashes](https://github.com/rustcrypto/hashes)

![](https://img.shields.io/github/stars/rustcrypto/hashes?style=flat-square&label=⭐) · Found in 1 active source: rust-unofficial/awesome-rust

**Review label:** AI Candidate · **Caveat:** Candidate still needs human review before endorsement.

Collection of cryptographic hash functions written in pure Rust.

> **Análise IA:** Librería Rust de funciones hash criptográficas puras. Estándar de facto para Rust, mantenida por RustCrypto. Production-ready.

**Pontos fortes:** _Auditoría de seguridad profesional (RustCrypto)_ · _Cobertura completa de algoritmos modernos_

**Tags:** `rust` `cryptography` `hashing` `library`

---

### [Hunter.io](https://hunter.io)

Found in 1 active source: jivoi/awesome-osint

**Review label:** AI Candidate · **Caveat:** Candidate still needs human review before endorsement.

Data broker providing a Web search interface for discovering the email addresses and other organizational details of a company.

> **Análise IA:** Data broker comercial para email discovery de empleados. Efectivo operativamente pero pagado. Alternativa freemium a brute-force. Usado en recon profesional.

**Pontos fortes:** _Precisión alta en email validation_ · _API y bulk processing disponibles_

**Tags:** `osint` `email-discovery` `brute-force` `paid`

---

### [I2P](https://geti2p.net)

Found in 1 active source: jivoi/awesome-osint

**Review label:** AI Candidate · **Caveat:** Candidate still needs human review before endorsement.

The Invisible Internet Project.

> **Análise IA:** Red P2P de enrutamiento de cebollas para anonimato. Para usuarios que necesitan privacidad contra análisis de tráfico. Menos conocida que Tor pero con arquitectura más distribuida.

**Pontos fortes:** _Arquitectura totalmente descentralizada sin directory servers_ · _Resistente a ataques de correlación de tráfico_

**Tags:** `anonymity` `p2p` `overlay-network` `privacy`

---

### [Keybase](https://keybase.io)

Found in 1 active source: jaywcjlove/awesome-mac

**Review label:** AI Candidate · **Caveat:** Candidate still needs human review before endorsement.

Secure groups, files, and chat for everyone! (https://github.com/keybase)

> **Análise IA:** Plataforma de comunicación y colaboración segura con cifrado end-to-end. Open-source pero con desarrollos dispersos, competencia fuerte de Signal y Matrix.

**Pontos fortes:** _Integración con verificación de identidad criptográfica_ · _Chat y archivos en un único ecosistema_

**Tags:** `crypto` `e2e` `chat` `security` `teams`

---

### [KeyCloak](https://keycloak.org)

Found in 1 active source: akullpp/awesome-java

**Review label:** AI Candidate · **Caveat:** Candidate still needs human review before endorsement.

Open Source Identity and Access Management. Apache-2.0 Java

> **Análise IA:** Keycloak es un IAM open-source maduro basado en estándares (OAuth2, OIDC, SAML). Resuelve autenticación/autorización en aplicaciones empresariales. Comunidad activa, pero requiere Java y DevOps experiente.

**Pontos fortes:** _Soporte multi-protocolo robusto (OIDC, SAML, LDAP)_ · _Cluster-ready y escalable horizontalmente_

**Tags:** `iam` `oauth2` `java` `self-hosted` `enterprise`

---

### [kpcyrd/authoscope](https://github.com/kpcyrd/authoscope)

![](https://img.shields.io/github/stars/kpcyrd/authoscope?style=flat-square&label=⭐) · Found in 1 active source: rust-unofficial/awesome-rust

**Review label:** AI Candidate · **Caveat:** Candidate still needs human review before endorsement.

A scriptable network authentication cracker

> **Análise IA:** Cracker de autenticación scriptable en red escrito en Rust. Herramienta de penetration testing para auditoría de credenciales. Útil en labs controlados pero requiere permisos explícitos.

**Pontos fortes:** _Escritura en Rust garantiza seguridad de memoria_ · _Scriptable para automatizar pruebas de autenticación_

**Tags:** `rust` `pentest` `network` `security` `cli`

---

### [kpcyrd/sniffglue](https://github.com/kpcyrd/sniffglue)

![](https://img.shields.io/github/stars/kpcyrd/sniffglue?style=flat-square&label=⭐) · Found in 1 active source: rust-unofficial/awesome-rust

**Review label:** AI Candidate · **Caveat:** Candidate still needs human review before endorsement.

A secure multithreaded packet sniffer

> **Análise IA:** Packet sniffer seguro y multihilo en Rust. Alternativa moderna a tcpdump con mejor manejo de memoria. Para análisis de tráfico y debugging de red.

**Pontos fortes:** _Seguridad de memoria garantizada por Rust_ · _Multithreading nativo sin race conditions_

**Tags:** `rust` `network` `sniffer` `cli` `security`

---

### [LibreWolf](https://librewolf.net)

Found in 2 active sources: jivoi/awesome-osint, jaywcjlove/awesome-mac

**Review label:** AI Candidate · **Caveat:** Candidate still needs human review before endorsement.

A fork of Firefox, focused on privacy, security and freedom. (https://gitlab.com/librewolf-community)

> **Análise IA:** Fork Firefox hardened para privacidad y seguridad. Desactiva telemetría Mozilla, DRM, pocket. Compilado limpio. Ligero pero requiere usuarios tech-savvy. Niche privacy-first.

**Pontos fortes:** _Telemetría completamente removida_ · _Compilación reproducible_

**Tags:** `firefox` `privacy` `hardened` `open-source`

---

### [Lynis](https://cisofy.com/lynis)

Found in 1 active source: veggiemonk/awesome-docker

**Review label:** AI Candidate · **Caveat:** Candidate still needs human review before endorsement.

Auditing tool for UNIX-based systems.

> **Análise IA:** Herramienta de auditoría para UNIX/Linux que escanea vulnerabilidades, compliance, hardening. Estándar en security ops, genera reportes procesables.

**Pontos fortes:** _Amplio coverage de checks de seguridad_ · _Output estructurado, integrable en pipelines_

**Tags:** `security` `audit` `unix` `cli`

---

### [Maltego](https://maltego.com)

Found in 1 active source: jivoi/awesome-osint

**Review label:** AI Candidate · **Caveat:** Candidate still needs human review before endorsement.

Maltego is an open source intelligence (OSINT) and graphical link analysis tool for gathering and connecting information for investigative tasks.

> **Análise IA:** Herramienta OSINT visual de link analysis para correlacionar datos. Potente para investigaciones, pero curva de aprendizaje empinada. Versión free limitada.

**Pontos fortes:** _Visualización excepcional de conexiones entre entidades_ · _Cientos de transforms para datasources_

**Tags:** `osint` `graph-analysis` `link-analysis` `investigacion`

---

### [mariocandela/beelzebub](https://github.com/mariocandela/beelzebub)

![](https://img.shields.io/github/stars/mariocandela/beelzebub?style=flat-square&label=⭐) · Found in 2 active sources: avelino/awesome-go, punkpeye/awesome-mcp-servers

**Review label:** AI Candidate · **Caveat:** Candidate still needs human review before endorsement.

☁️ Beelzebub is a honeypot framework that lets you build honeypot tools using MCP. Its purpose is to detect prompt injection or malicious agent behavior. The underlying idea is to provide the agent with tools it would never use in its normal work.

> **Análise IA:** Honeypot framework con MCP para detectar prompt injection en agentes IA. Idea interesante: proporciona tools carnada que un agente legítimo nunca tocaría. Nicho: seguridad de agentes, no de infraestructura clásica.

**Pontos fortes:** _Enfoque novel: usar herramientas carnada como signal de compromiso en agentes_ · _Integración con MCP standard para extensibilidad_

**Tags:** `honeypot` `security` `ai-safety` `prompt-injection` `mcp`

---

### [mavdol/capsule/mcp-server](https://github.com/mavdol/capsule)

![](https://img.shields.io/github/stars/mavdol/capsule?style=flat-square&label=⭐) · Found in 2 active sources: rust-unofficial/awesome-rust, punkpeye/awesome-mcp-servers

**Review label:** AI Candidate · **Caveat:** Candidate still needs human review before endorsement.

🦀 🏠 🍎 🪟 🐧 Run untrusted Python/JavaScript code in WebAssembly sandboxes.

> **Análise IA:** MCP server que ejecuta código Python/JavaScript untrusted en sandboxes WebAssembly. Previene exploits de agentes maliciosos. Para AI safety critical.

**Pontos fortes:** _Isolación real via WASM, sin escape path obvio_ · _Soporte dual Python/JavaScript_

**Tags:** `mcp` `wasm` `sandbox` `rust` `security`

---

### [orion-rs/orion](https://github.com/orion-rs/orion)

![](https://img.shields.io/github/stars/orion-rs/orion?style=flat-square&label=⭐) · Found in 1 active source: rust-unofficial/awesome-rust

**Review label:** AI Candidate · **Caveat:** Candidate still needs human review before endorsement.

This library aims to provide easy and usable crypto. 'Usable' meaning exposing high-level API's that are easy to use and hard to misuse.

> **Análise IA:** Librería Rust que prioriza API usable y resistente a misuso. Para devs que quieren crypto sin ser expertos. High-level abstractions sobre primitivas peligrosas.

**Pontos fortes:** _API deliberadamente difícil de misusar, errores en compile-time_ · _Documentación clara con ejemplos de misuso común_

**Tags:** `rust` `cryptography` `security` `high-level-api` `library`

---

### [paaster](https://paaster.io)

Found in 1 active source: jivoi/awesome-osint

**Review label:** AI Candidate · **Caveat:** Candidate still needs human review before endorsement.

Paaster is a secure and user-friendly pastebin application that prioritizes privacy and simplicity. With end-to-end encryption and paste history, Paaster ensures that your pasted code remains confidential and accessible.

> **Análise IA:** Pastebin con cifrado end-to-end y historial. Resuelve problema real (privacidad en compartir snippets). Alternativa directa a servicios centralizados pero ecosistema pastebin saturado.

**Pontos fortes:** _E2E encryption nativo_ · _Historial preservado_

**Tags:** `pastebin` `encryption` `privacy` `self-hosted`

---

### [Promptfoo](https://github.com/promptfoo/promptfoo)

![](https://img.shields.io/github/stars/promptfoo/promptfoo?style=flat-square&label=⭐) · Found in 2 active sources: EthicalML/awesome-production-machine-learning, josephmisiti/awesome-machine-learning

**Review label:** AI Candidate · **Caveat:** Candidate still needs human review before endorsement.

LLM red teaming and evaluation framework for testing jailbreaks, prompt injection, and other vulnerabilities with CI/CD integration.

> **Análise IA:** Framework para testear LLMs contra injection, jailbreaks y vulnerabilidades. Red teaming automatizado con CI/CD. Necesario si desplegás LLMs en producción y querés seguridad serio.

**Pontos fortes:** _Cubre vectores de ataque específicos de LLMs_ · _CI/CD integration out-of-box_

**Tags:** `llm-security` `red-teaming` `prompt-injection` `ci-cd` `testing`

---

### [pynacl](https://github.com/pyca/pynacl)

![](https://img.shields.io/github/stars/pyca/pynacl?style=flat-square&label=⭐) · Found in 1 active source: vinta/awesome-python

**Review label:** AI Candidate · **Caveat:** Candidate still needs human review before endorsement.

Python binding to the Networking and Cryptography (NaCl) library.

> **Análise IA:** Wrapper Python para NaCl, librería moderna de crypto. Si necesitás encryptación simétrica, asymétrica o signing, es la opción recomendada por la comunidad Python.

**Pontos fortes:** _API clara y segura por defecto, difícil hacerla mal_ · _Basada en NaCl auditada y battle-tested_

**Tags:** `cryptography` `python` `nacl` `bindings`

---

### [rage](https://github.com/str4d/rage)

![](https://img.shields.io/github/stars/str4d/rage?style=flat-square&label=⭐) · Found in 1 active source: rust-unofficial/awesome-rust

**Review label:** AI Candidate · **Caveat:** Candidate still needs human review before endorsement.

is a simple, modern, and secure file encryption tool, using the age format.

> **Análise IA:** Herramienta de cifrado de archivos moderna en Rust, usa formato age. Simple, rápido, sin opciones criptográficas débiles. Reemplaza GPG para cifrado de archivos básico.

**Pontos fortes:** _Interfaz minimalista, sin opciones inseguras_ · _Rápido, código limpio y auditable_

**Tags:** `encryption` `rust` `file-encryption` `age-format` `cli`

---

### [Redlib](https://github.com/redlib-org/redlib)

![](https://img.shields.io/github/stars/redlib-org/redlib?style=flat-square&label=⭐) · Found in 1 active source: rust-unofficial/awesome-rust

**Review label:** AI Candidate · **Caveat:** Candidate still needs human review before endorsement.

An alternative private front-end to Reddit, with its origins in Libreddit

> **Análise IA:** Frontend privado para Reddit (fork de Libreddit). Reemplaza JS con Rust. Útil si querés Reddit sin tracker. Activa pero depende API Reddit que puede cambiar.

**Pontos fortes:** _Zero JavaScript, performance_ · _Privacy-focused, open source_

**Tags:** `rust` `frontend` `privacy` `reddit`

---

### [rshijack](https://github.com/kpcyrd/rshijack)

![](https://img.shields.io/github/stars/kpcyrd/rshijack?style=flat-square&label=⭐) · Found in 1 active source: rust-unofficial/awesome-rust

**Review label:** AI Candidate · **Caveat:** Candidate still needs human review before endorsement.

TCP connection hijacker, Rust rewrite of shijack.

> **Análise IA:** Hijacker de conexiones TCP reescrito en Rust desde shijack. Herramienta avanzada para auditoría de red e investigación. Uso restrictivo, requiere permisos.

**Pontos fortes:** _Implementación limpia en Rust de técnica clásica_ · _Mantenimiento activo por kpcyrd_

**Tags:** `rust` `pentest` `network` `tcp` `cli`

---

### [safedep/vet](https://github.com/safedep/vet)

![](https://img.shields.io/github/stars/safedep/vet?style=flat-square&label=⭐) · Found in 2 active sources: avelino/awesome-go, punkpeye/awesome-mcp-servers

**Review label:** AI Candidate · **Caveat:** Candidate still needs human review before endorsement.

🎖️ 🏎️ ☁️ 🍎 🪟 🐧 vet-mcp checks open source packages—like those suggested by AI coding tools—for vulnerabilities and malicious code. It supports npm and PyPI, and runs locally via Docker or as a standalone binary for fast, automated vetting.

> **Análise IA:** MCP server que vetea packages npm/PyPI contra vulnerabilidades y código malicioso. Integrable en AI coding tools. Docker o binary standalone.

**Pontos fortes:** _Local execution sin cloud dependency_ · _Coverage dual npm/PyPI con scanning de malware_

**Tags:** `mcp` `dependency-check` `security` `npm` `pypi`

---

### [SecLists](https://github.com/danielmiessler/seclists)

![](https://img.shields.io/github/stars/danielmiessler/seclists?style=flat-square&label=⭐) · Found in 1 active source: jivoi/awesome-osint

**Review label:** AI Candidate · **Caveat:** Candidate still needs human review before endorsement.

Collection of multiple types of lists used during security assessments.

> **Análise IA:** Colección masiva de wordlists y payloads para testing. Estándar en pentesting. Actualizadas regularmente. Imprescindible en arsenal ofensivo.

**Pontos fortes:** _Cobertura exhaustiva: fuzzing, credenciales, patrones_ · _Actualización activa y comunidad robusta_

**Tags:** `wordlist` `payload` `pentesting` `curado`

---

### [sherlock](https://github.com/sherlock-project/sherlock)

![](https://img.shields.io/github/stars/sherlock-project/sherlock?style=flat-square&label=⭐) · Found in 2 active sources: jivoi/awesome-osint, vinta/awesome-python

**Review label:** AI Candidate · **Caveat:** Candidate still needs human review before endorsement.

Hunt down social media accounts by username across social networks.

> **Análise IA:** Script que busca cuentas de redes sociales por username. Útil para OSINT y verificación de brand. Funciona pero es básico: no elude throttling ni captchas sofisticados.

**Pontos fortes:** _Setup trivial, útil para auditorías rápidas de availability de usernames_ · _Soporta muchas plataformas_

**Tags:** `osint` `social-media` `python` `cli`

---

### [Shodan](https://shodan.io)

Found in 1 active source: jivoi/awesome-osint

**Review label:** AI Candidate · **Caveat:** Candidate still needs human review before endorsement.

Shodan is a search engine for the IOT(Internet of Things) that allows you to search variety of servers that are connected to the internet using various searching filters.

> **Análise IA:** Motor de búsqueda de IoT/servidores expuestos públicamente. Crítico para asset discovery, identificar infraestructura vulnerable. Es de facto estándar en auditoría y threat intel.

**Pontos fortes:** _Base de datos masiva de dispositivos indexados_ · _Filtros avanzados (puerto, banner, geolocalización)_

**Tags:** `iot-search` `vulnerability-scanning` `asset-discovery` `threat-intel`

---

### [SpiderFoot](https://spiderfoot.net)

Found in 1 active source: jivoi/awesome-osint

**Review label:** AI Candidate · **Caveat:** Candidate still needs human review before endorsement.

SpiderFoot is an open source intelligence (OSINT) automation platform with over 200 modules for threat intelligence, attack surface monitoring, security assessments and asset discovery.

> **Análise IA:** Plataforma OSINT automatizada con 200+ módulos. Excelente para asset discovery y threat intel sin hands-on. Open source pero requiere setup. Producción-ready.

**Pontos fortes:** _Automatización masiva reduce manual work 70%+_ · _Modular y extensible, open source_

**Tags:** `osint` `automation` `threat-intel` `asset-discovery`

---

### [SQLMap](https://github.com/sqlmapproject/sqlmap)

![](https://img.shields.io/github/stars/sqlmapproject/sqlmap?style=flat-square&label=⭐) · Found in 1 active source: vinta/awesome-python

**Review label:** AI Candidate · **Caveat:** Candidate still needs human review before endorsement.

An automatic SQL injection and database takeover tool.

> **Análise IA:** Herramienta de SQL injection automatizada. Estándar para pentesting y auditorías. Detecta y explota vulnerabilidades SQL; documentación excelente, comunidad activa.

**Pontos fortes:** _Automatización extremadamente efectiva, soporta casi todos los tipos de BD_ · _Actualización constante vs nuevas técnicas de obfuscación_

**Tags:** `penetration-testing` `sql-injection` `python` `automation`

---

### [ssh-vault](https://github.com/ssh-vault/ssh-vault)

![](https://img.shields.io/github/stars/ssh-vault/ssh-vault?style=flat-square&label=⭐) · Found in 2 active sources: rust-unofficial/awesome-rust, avelino/awesome-go

**Review label:** AI Candidate · **Caveat:** Candidate still needs human review before endorsement.

A simple tool to manage secrets using ssh keys for encryption and decryption.

> **Análise IA:** Gestor de secretos minimalista basado en claves SSH. Usa SSH para cifrar/descifrar sin infraestructura extra. Útil para equipos pequeños que ya tienen SSH setup.

**Pontos fortes:** _Cero dependencias externas, aprovecha claves SSH existentes_ · _Muy simple de usar, overhead mínimo_

**Tags:** `secrets-management` `ssh` `encryption` `cli` `golang`

---

### [Swift-Sodium](https://github.com/jedisct1/swift-sodium)

![](https://img.shields.io/github/stars/jedisct1/swift-sodium?style=flat-square&label=⭐) · Found in 1 active source: matteocrippa/awesome-swift

**Review label:** AI Candidate · **Caveat:** Candidate still needs human review before endorsement.

Swift interface to the Sodium library for common crypto operations for iOS and macOS.

> **Análise IA:** Swift binding a libsodium (NaCl moderno). Criptografía contemporánea (AEAD, key exchange). Para quien necesita algo beyond AES. Bien mantenido.

**Pontos fortes:** _Acceso a libsodium battle-tested; AEAD + key derivation_ · _Mantenimiento activo, usado en prod_

**Tags:** `swift` `libsodium` `nacl` `cryptography` `authenticated-encryption`

---

### [Syft](https://github.com/anchore/syft)

![](https://img.shields.io/github/stars/anchore/syft?style=flat-square&label=⭐) · Found in 2 active sources: veggiemonk/awesome-docker, avelino/awesome-go

**Review label:** AI Candidate · **Caveat:** Candidate still needs human review before endorsement.

CLI tool and library for generating a Software Bill of Materials (SBOM) from container images and filesystems. By Anchore.

> **Análise IA:** CLI + librería para generar SBOMs (Software Bill of Materials) desde imágenes container y filesystems. Crítico para seguridad/compliance. Por Anchore, empresa consolidada en supply-chain security.

**Pontos fortes:** _Herramienta en ecosistema maduro (supply-chain security), requisito creciente en enterprise_ · _Activa, open-source, usada en industry_

**Tags:** `sbom` `container-security` `cli` `go` `supply-chain`

---

### [Tails](https://tails.boum.org)

Found in 1 active source: jivoi/awesome-osint

**Review label:** AI Candidate · **Caveat:** Candidate still needs human review before endorsement.

Live operating system aiming to preserve your privacy and anonymity.

> **Análise IA:** Live OS Debian que borra todo al apagar. Para periodistas/activistas que necesitan garantía de no dejar rastros. Solución de privacidad completa, no solo red.

**Pontos fortes:** _Integración transparente de Tor en toda la stack_ · _Amnesia forzada, no hay persistencia accidental_

**Tags:** `anonymity` `live-os` `privacy` `linux`

---

### [The Harvester](https://github.com/laramies/theharvester)

![](https://img.shields.io/github/stars/laramies/theharvester?style=flat-square&label=⭐) · Found in 1 active source: jivoi/awesome-osint

**Review label:** AI Candidate · **Caveat:** Candidate still needs human review before endorsement.

Gather emails, subdomains, hosts, employee names, open ports and banners from different public sources like search engines, PGP key servers and SHODAN computer database.

> **Análise IA:** Herramienta OSINT clásica para recopilación pasiva: emails, subdominios, hosts desde fuentes públicas. Útil en reconocimiento inicial de red, pentesting. Todavía mantiene relevancia aunque algunas fuentes se han degradado.

**Pontos fortes:** _Agregador maduro de múltiples fuentes públicas_ · _Baja curva de entrada, output útil inmediato_

**Tags:** `osint` `reconnaissance` `python` `email-scraping` `cli`

---

### [Tink](https://github.com/google/tink)

![](https://img.shields.io/github/stars/google/tink?style=flat-square&label=⭐) · Found in 1 active source: akullpp/awesome-java

**Review label:** AI Candidate · **Caveat:** Candidate still needs human review before endorsement.

A multi-language, cross-platform library that provides cryptographic APIs that are secure, easy to use correctly, and hard(er) to misuse. [Apache-2.0]

> **Análise IA:** Librería criptográfica multi-lenguaje (Google). Diseño: seguro por defecto, APIs imposibles de misuser. Mejor ergonomía que Crypto++. Estándar moderno en seguridad aplicada.

**Pontos fortes:** _APIs imposibles de misuser por diseño_ · _Soporte multi-lenguaje + plataforma_

**Tags:** `cryptography` `multi-language` `secure-by-default`

---

### [Tor](https://torproject.org)

Found in 1 active source: jivoi/awesome-osint

**Review label:** AI Candidate · **Caveat:** Candidate still needs human review before endorsement.

Free software and onion routed overlay network that helps you defend against traffic analysis.

> **Análise IA:** Red de enrutamiento con cebollas estándar de facto. Para cualquiera que necesite privacidad de red. Probada en batalla durante 20+ años, usado por gobiernos y insurgentes.

**Pontos fortes:** _Red más grande y auditada en privacidad_ · _Triple encriptación, protección contra análisis de tráfico comprobada_

**Tags:** `anonymity` `overlay-network` `privacy` `c`

---

### [vaultwarden](https://github.com/dani-garcia/vaultwarden)

![](https://img.shields.io/github/stars/dani-garcia/vaultwarden?style=flat-square&label=⭐) · Found in 1 active source: rust-unofficial/awesome-rust

**Review label:** AI Candidate · **Caveat:** Candidate still needs human review before endorsement.

Alternative implementation of the Bitwarden server API written in Rust

> **Análise IA:** Clone de Bitwarden API escrito en Rust. Para self-hosters que desconfían de cloud o necesitan auditabilidad. Funciona bien, mantención activa, alternativa seria a Bitwarden.

**Pontos fortes:** _Consumo RAM/CPU mínimo comparado a versión oficial_ · _Deployable en VPS barato sin overhead_

**Tags:** `password-manager` `rust` `self-hosted` `security`

---

### [Virus Total](https://virustotal.com)

Found in 1 active source: jivoi/awesome-osint

**Review label:** AI Candidate · **Caveat:** Candidate still needs human review before endorsement.

Free service that analyzes suspicious files and URLs and facilitates the quick detection of viruses, worms, trojans, and all kinds of malware.

> **Análise IA:** Servicio gratuito de análisis de archivos/URLs contra múltiples antivirus. Escanea malware, trojans, worms. Estándar en OSINT y análisis de seguridad.

**Pontos fortes:** _Base de datos masiva de firmas de 90+ motores_ · _Acceso gratuito sin límites aparentes, API disponible_

**Tags:** `malware` `osint` `antivirus` `saas` `security`

---

### [webpki](https://github.com/briansmith/webpki)

![](https://img.shields.io/github/stars/briansmith/webpki?style=flat-square&label=⭐) · Found in 1 active source: rust-unofficial/awesome-rust

**Review label:** AI Candidate · **Caveat:** Candidate still needs human review before endorsement.

Web PKI TLS X.509 certificate validation in Rust.

> **Análise IA:** Validación X.509/TLS en Rust puro. Reemplaza OpenSSL para PKI sin FFI risk. Core de Rustls. Si implementás TLS o HTTPS client, esto es el gold standard.

**Pontos fortes:** _Validación correcta de certificados sin C deps_ · _Auditoría profesional, usado en producción crítica_

**Tags:** `rust` `tls` `x509` `pkix`

---

### [WiGLE](https://wigle.net)

Found in 1 active source: jivoi/awesome-osint

**Review label:** AI Candidate · **Caveat:** Candidate still needs human review before endorsement.

Wi-fi "wardriving" database. Contains a global map containing crowdsourced information on the location, name, and other properties of wi-fi networks. Software available to download to contribute data to the public infoset.

> **Análise IA:** Base de datos colaborativa global de redes Wi-Fi. Niche pero preciso para wardriving, geolocalización pasiva. Comunidad activa manteniendo datos.

**Pontos fortes:** _Cobertura global con aporte comunitario_ · _Herramienta propia para captura de datos_

**Tags:** `wifi-mapping` `geolocation` `wardriving` `crowdsourced`

---


---

## Needs review

Entries with weak or inconsistent trace evidence. They stay visible for auditability, not endorsement.

### [Botan](https://botan.randombit.net)

Needs trace review

**Review label:** Needs Review · **Caveat:** Candidate still needs human review before endorsement.

Cryptography library written in C++20.

> **Análise IA:** Librería crypto en C++20 con algoritmos modernos. Para devs C++ que necesitan crypto integrada sin OpenSSL o dependencias pesadas.

**Pontos fortes:** _C++20 native, code moderno_ · _Cobertura amplia de algoritmos post-quantum_

**Tags:** `cpp20` `cryptography` `library` `algorithms`

---

### [Crypto++](https://github.com/weidai11/cryptopp)

![](https://img.shields.io/github/stars/weidai11/cryptopp?style=flat-square&label=⭐) · Needs trace review

**Review label:** Needs Review · **Caveat:** Candidate still needs human review before endorsement.

A free C++ class library of cryptographic schemes. [Boost]

> **Análise IA:** Librería C++ crypto consolidada, 25+ años de desarrollo. Estándar industrial para esquemas criptográficos. Pero: C++ puro (overhead), comunidad menor que alternativas modernas como Tink.

**Pontos fortes:** _Amplia cobertura de esquemas criptográficos_ · _Maduro y auditado_

**Tags:** `cpp` `cryptography` `production-ready`

---

### [Firezone](https://firezone.dev)

Needs trace review

**Review label:** Needs Review · **Caveat:** Candidate still needs human review before endorsement.

Secure remote access gateway that supports the WireGuard protocol. It offers a Web GUI, 1-line install script, multi-factor auth (MFA), and SSO. Apache-2.0 Elixir/Docker

> **Análise IA:** VPN/secure gateway moderno con WireGuard, MFA, SSO. Elixir + Docker. Alternativa legítima a OpenVPN/traditional VPN si necesitás remote access corporativo self-hosted con polish moderno.

**Pontos fortes:** _1-line install, setup trivial vs OpenVPN, GUI intuitiva_ · _WireGuard más eficiente y moderno que IPSec/OpenVPN_

**Tags:** `wireguard` `vpn` `self-hosted` `mfa-sso`

---

### [gpg](https://gnupg.org)

Needs trace review

**Review label:** Needs Review · **Caveat:** Candidate still needs human review before endorsement.

Complete and free implementation of the OpenPGP standard. It allows to encrypt and sign your data and communication, features a versatile key management system. GnuPG is a command line tool with features for easy integration with other applications.

> **Análise IA:** Implementación completa y free del estándar OpenPGP. Para encriptación/firma de datos y comunicaciones con CLI integrable a cualquier tool.

**Pontos fortes:** _Estándar industria de 25+ años_ · _Zero-dependency, CLI portable y ubiquo_

**Tags:** `gpg` `encryption` `cli` `openpgp` `portable`

---

### [libsodium](https://github.com/jedisct1/libsodium)

![](https://img.shields.io/github/stars/jedisct1/libsodium?style=flat-square&label=⭐) · Needs trace review

**Review label:** Needs Review · **Caveat:** Candidate still needs human review before endorsement.

P(ortable ackageable) NaCl-based crypto library, opinionated and easy to use. [ISC]

> **Análise IA:** Librería crypto moderna basada en NaCl, diseñada para ser segura por defecto (opciones opinionadas). Estándar en Python (PyNaCl) y en sistemas que necesitan crypto sin sorpresas.

**Pontos fortes:** _API opinionada reduce errores de uso_ · _Ampliamente auditada y confiable_

**Tags:** `cryptography` `nacl` `security` `c`

---

### [Ockam](https://github.com/ockam-network/ockam)

![](https://img.shields.io/github/stars/ockam-network/ockam?style=flat-square&label=⭐) · Needs trace review

**Review label:** Needs Review · **Caveat:** Candidate still needs human review before endorsement.

End-to-end encryption and mutual authentication for distributed applications.

> **Análise IA:** Toolkit para encriptación e2e y autenticación mutua en apps distribuidas. Resuelve confianza en arquitecturas mesh/zero-trust reales.

**Pontos fortes:** _Abstracciones portables para transporte (TCP, UDP, Bluetooth)_ · _Modelo de seguridad auditado para comms distribuidas_

**Tags:** `rust` `cryptography` `distributed` `security`

---

### [OpenSSL](https://github.com/openssl/openssl)

![](https://img.shields.io/github/stars/openssl/openssl?style=flat-square&label=⭐) · Needs trace review

**Review label:** Needs Review · **Caveat:** Candidate still needs human review before endorsement.

A robust, commercial-grade, full-featured, and Open Source cryptography library. [Apache]

> **Análise IA:** Librería crypto de grado comercial, open source, estándar universal. Para cualquier app que necesite encriptación, TLS, o signing con soporte universal.

**Pontos fortes:** _Estándar de facto en todas partes (sistemas, apps, servicios)_ · _Auditoría y madurez incomparables_

**Tags:** `openssl` `cryptography` `tls` `c` `universal`

---

### [s2n](https://github.com/awslabs/s2n)

![](https://img.shields.io/github/stars/awslabs/s2n?style=flat-square&label=⭐) · Needs trace review

**Review label:** Needs Review · **Caveat:** Candidate still needs human review before endorsement.

An implementation of the TLS/SSL protocols. [Apache]

> **Análise IA:** Implementación robusta de TLS/SSL de AWS Labs. Usado en producción para aplicaciones que necesitan criptografía moderna. Bien mantenido, auditado, estándar en infraestructura AWS.

**Pontos fortes:** _Auditorías de seguridad regulares y mantenimiento activo_ · _Optimizaciones de performance específicas para SSL/TLS_

**Tags:** `tls` `ssl` `cryptography` `c` `aws`

---

### [Social Engineer Toolkit (SET)](https://github.com/trustedsec/social-engineer-toolkit)

![](https://img.shields.io/github/stars/trustedsec/social-engineer-toolkit?style=flat-square&label=⭐) · Needs trace review

**Review label:** Needs Review · **Caveat:** Candidate still needs human review before endorsement.

Open source pentesting framework designed for social engineering featuring a number of custom attack vectors to make believable attacks quickly.

> **Análise IA:** Framework pentesting enfocado en ingeniería social. Ataques creíbles preseteados (phishing, spear-phishing, payloads). Usado en red teams reales, documentación sólida.

**Pontos fortes:** _Ataques preseteados realistas y probados_ · _Integración con Metasploit, payloads customizables_

**Tags:** `pentesting` `social-engineering` `framework` `python` `red-team`

---

### [Trail of Bits Security Skills](https://github.com/trailofbits/skills)

![](https://img.shields.io/github/stars/trailofbits/skills?style=flat-square&label=⭐) · Needs trace review

**Review label:** Needs Review · **Caveat:** Candidate still needs human review before endorsement.

by Trail of Bits A very professional collection of over a dozen security-focused skills for code auditing and vulnerability detection. Includes skills for static analysis with CodeQL and Semgrep, variant analysis across codebases, fix verification, and differential code review.

> **Análise IA:** Colección de skills de seguridad para auditoría de código y análisis de vulnerabilidades. Incluye CodeQL y Semgrep. Producción Trail of Bits.

**Pontos fortes:** _Creado por referentes en security (Trail of Bits)_ · _Cubre análisis estático, variante y code review diferencial_

**Tags:** `security` `code-audit` `codeql` `semgrep`

---

### [x64dbg](https://x64dbg.com)

Needs trace review

**Review label:** Needs Review · **Caveat:** Candidate still needs human review before endorsement.

An open-source x64/x32 debugger for windows.

> **Análise IA:** Debugger x64 assembly para Windows. Para reverse engineers que necesitan paso a paso en binarios sin fuentes. Similar a OllyDbg pero actualizado.

**Pontos fortes:** _UI moderna vs OllyDbg antiguo_ · _Breakpoints avanzados, plugin ecosystem activo_

**Tags:** `debugger` `reverse-engineering` `x64` `windows`

---


---

<sub>📄 Gerado automaticamente de [juanchi.dev](https://juanchi.dev) · [código do sistema](https://juanchi.dev/blog/series/awesome-curated) · MIT licensed</sub>
