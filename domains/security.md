# 🔐 Security & Crypto — Awesome Curated

<p><sub>← [Back to main](../README.md)</sub></p>

**27 GEMs · 32 Worth trying**

---

## ⭐ GEMs — industry standards

Tools the community considers default. If you don't know them yet, they're worth exploring.

### 👤 [themis](https://github.com/cossacklabs/themis)

![](https://img.shields.io/github/stars/cossacklabs/themis?style=flat-square&label=⭐) · 🔥 **appears in 7 lists**

High level crypto library for storing data (AES), secure messaging (ECC + ECDSA / RSA + PSS + PKCS#7) and session-oriented, forward secrecy data exchange (ECDH key agreement, ECC & AES encryption). Ported on many languages and platforms, suitable for client-server infastructures.

> **AI analysis:** Esto es valor real. Themis resuelve el problema de siempre: los devs necesitan criptografía seria pero la API de bajo nivel de OpenSSL los mata. Themis ofrece primitivas de alto nivel (cifrado simétrico, mensajería segura, sesiones con forward secrecy) sin que tengas que entender los detalles del protocolo. El soporte multi-lenguaje y multi-plataforma es el diferencial genuino. Ideal para equipos que construyen apps móviles o client-server que manejan datos sensibles y no quieren inventar su propia crypto. No es humo.

**Strengths:** _Abstracción de alto nivel sobre primitivas criptográficas complejas (ECC, AES, ECDH) sin sacrificar seguridad real_ · _Soporte genuino multi-lenguaje y multi-plataforma, útil para equipos con stacks heterogéneos_ · _Incluye forward secrecy en sesiones, algo que muchos devs ignoran y que es crítico para datos sensibles_

**Tags:** `cryptography` `security` `multi-platform` `open-source` `encryption`

---

### [Bouncy Castle](https://bouncycastle.org/java.html)

appears in 2 lists

All-purpose cryptographic library and JCA provider offering a wide range of functions, from basic helpers to PGP/SMIME operations.

> **AI analysis:** Bouncy Castle es la librería criptográfica estándar en Java. Cobertura completa: cifrados, firma, PGP, SMIME. Usado en producción desde 2000+. Imprescindible para cualquier proyecto que necesite crypto serio en JVM.

**Strengths:** _Cobertura criptográfica exhaustiva y bien auditada_ · _Compatibilidad JCA nativa, integración directa con ecosistema Java_

**Tags:** `java` `cryptography` `jca-provider` `pgp` `smime`

---

### [briansmith/ring](https://github.com/briansmith/ring)

![](https://img.shields.io/github/stars/briansmith/ring?style=flat-square&label=⭐) · appears in 2 lists

Safe, fast, small crypto using Rust and BoringSSL's cryptography primitives.

> **AI analysis:** Crypto library Rust wrapping BoringSSL (Google). APIs seguras para primitivos críticos sin memory issues. Usado en Rustls, browsers. Indispensable si necesitás crypto sin paranoia de FFI bugs.

**Strengths:** _Safety guarantees de Rust + auditoría BoringSSL_ · _Performance sin sacrificar seguridad_

**Tags:** `rust` `crypto` `boringssl` `tls`

---

### [Crypto++](https://github.com/weidai11/cryptopp)

![](https://img.shields.io/github/stars/weidai11/cryptopp?style=flat-square&label=⭐) · appears in 2 lists

A free C++ class library of cryptographic schemes. [Boost] [website](http://www.cryptopp.com/)

> **AI analysis:** Librería C++ crypto consolidada, 25+ años de desarrollo. Estándar industrial para esquemas criptográficos. Pero: C++ puro (overhead), comunidad menor que alternativas modernas como Tink.

**Strengths:** _Amplia cobertura de esquemas criptográficos_ · _Maduro y auditado_

**Tags:** `cpp` `cryptography` `production-ready`

---

### [Cryptomator](https://cryptomator.org)

appears in 2 lists

Multi-platform transparent client-side encryption of your files in the cloud. [![Open-Source Software][OSS Icon] ![Freeware][Freeware Icon]](https://github.com/cryptomator/cryptomator/)

> **AI analysis:** Encriptación client-side transparente para cloud storage. Multiplataforma, open-source, Java-based. Resuelve problema real: confiar en cloud providers sin revelar contenido.

**Strengths:** _Integración transparente con cloud providers_ · _Zero-knowledge por diseño_

**Tags:** `encryption` `client-side` `java` `cross-platform`

---

### [Google Hacking Database (GHDB)](https://exploit-db.com/google-hacking-database)

appears in 2 lists

The GHDB is an index of search queries (we call them dorks) used to find publicly available information, intended for pentesters and security researchers.

> **AI analysis:** Índice de Google dorking queries para pentesting. Referencia fundamental. Imprescindible conocer para recon inicial efectivo, zero costo.

**Strengths:** _Cobertura exhaustiva de técnicas google search_ · _Gratuito y mantenido activamente_

**Tags:** `osint` `google-dorking` `recon` `pentesting`

---

### [gpg](https://gnupg.org)

appears in 2 lists

Complete and free implementation of the OpenPGP standard. It allows to encrypt and sign your data and communication, features a versatile key management system. GnuPG is a command line tool with features for easy integration with other applications.

> **AI analysis:** Implementación completa y free del estándar OpenPGP. Para encriptación/firma de datos y comunicaciones con CLI integrable a cualquier tool.

**Strengths:** _Estándar industria de 25+ años_ · _Zero-dependency, CLI portable y ubiquo_

**Tags:** `gpg` `encryption` `cli` `openpgp` `portable`

---

### [hashes](https://github.com/rustcrypto/hashes)

![](https://img.shields.io/github/stars/rustcrypto/hashes?style=flat-square&label=⭐) · appears in 2 lists

Collection of cryptographic hash functions written in pure Rust.

> **AI analysis:** Librería Rust de funciones hash criptográficas puras. Estándar de facto para Rust, mantenida por RustCrypto. Production-ready.

**Strengths:** _Auditoría de seguridad profesional (RustCrypto)_ · _Cobertura completa de algoritmos modernos_

**Tags:** `rust` `cryptography` `hashing` `library`

---

### [KeyCloak](https://keycloak.org)

appears in 2 lists

Open Source Identity and Access Management.

> **AI analysis:** Keycloak es un IAM open-source maduro basado en estándares (OAuth2, OIDC, SAML). Resuelve autenticación/autorización en aplicaciones empresariales. Comunidad activa, pero requiere Java y DevOps experiente.

**Strengths:** _Soporte multi-protocolo robusto (OIDC, SAML, LDAP)_ · _Cluster-ready y escalable horizontalmente_

**Tags:** `iam` `oauth2` `java` `self-hosted` `enterprise`

---

### [libsodium](https://github.com/jedisct1/libsodium)

![](https://img.shields.io/github/stars/jedisct1/libsodium?style=flat-square&label=⭐) · appears in 2 lists

P(ortable·ackageable) NaCl-based crypto library, opinionated and easy to use. [ISC]

> **AI analysis:** Librería crypto moderna basada en NaCl, diseñada para ser segura por defecto (opciones opinionadas). Estándar en Python (PyNaCl) y en sistemas que necesitan crypto sin sorpresas.

**Strengths:** _API opinionada reduce errores de uso_ · _Ampliamente auditada y confiable_

**Tags:** `cryptography` `nacl` `security` `c`

---

### [Lynis](https://cisofy.com/lynis)

appears in 2 lists

Auditing tool for UNIX-based systems.

> **AI analysis:** Herramienta de auditoría para UNIX/Linux que escanea vulnerabilidades, compliance, hardening. Estándar en security ops, genera reportes procesables.

**Strengths:** _Amplio coverage de checks de seguridad_ · _Output estructurado, integrable en pipelines_

**Tags:** `security` `audit` `unix` `cli`

---

### [OpenSSL](https://github.com/openssl/openssl)

![](https://img.shields.io/github/stars/openssl/openssl?style=flat-square&label=⭐) · appears in 2 lists

A robust, commercial-grade, full-featured, and Open Source cryptography library. [Apache] [website](http://www.openssl.org/)

> **AI analysis:** Librería crypto de grado comercial, open source, estándar universal. Para cualquier app que necesite encriptación, TLS, o signing con soporte universal.

**Strengths:** _Estándar de facto en todas partes (sistemas, apps, servicios)_ · _Auditoría y madurez incomparables_

**Tags:** `openssl` `cryptography` `tls` `c` `universal`

---

### [pynacl](https://github.com/pyca/pynacl)

![](https://img.shields.io/github/stars/pyca/pynacl?style=flat-square&label=⭐) · appears in 2 lists

Python binding to the Networking and Cryptography (NaCl) library.

> **AI analysis:** Wrapper Python para NaCl, librería moderna de crypto. Si necesitás encryptación simétrica, asymétrica o signing, es la opción recomendada por la comunidad Python.

**Strengths:** _API clara y segura por defecto, difícil hacerla mal_ · _Basada en NaCl auditada y battle-tested_

**Tags:** `cryptography` `python` `nacl` `bindings`

---

### [s2n](https://github.com/awslabs/s2n)

![](https://img.shields.io/github/stars/awslabs/s2n?style=flat-square&label=⭐) · appears in 2 lists

An implementation of the TLS/SSL protocols. [Apache]

> **AI analysis:** Implementación robusta de TLS/SSL de AWS Labs. Usado en producción para aplicaciones que necesitan criptografía moderna. Bien mantenido, auditado, estándar en infraestructura AWS.

**Strengths:** _Auditorías de seguridad regulares y mantenimiento activo_ · _Optimizaciones de performance específicas para SSL/TLS_

**Tags:** `tls` `ssl` `cryptography` `c` `aws`

---

### [safedep/vet](https://github.com/safedep/vet)

![](https://img.shields.io/github/stars/safedep/vet?style=flat-square&label=⭐) · appears in 2 lists

🎖️ 🏎️ ☁️ 🍎 🪟 🐧 - vet-mcp checks open source packages—like those suggested by AI coding tools—for vulnerabilities and malicious code. It supports npm and PyPI, and runs locally via Docker or as a standalone binary for fast, automated vetting.

> **AI analysis:** MCP server que vetea packages npm/PyPI contra vulnerabilidades y código malicioso. Integrable en AI coding tools. Docker o binary standalone.

**Strengths:** _Local execution sin cloud dependency_ · _Coverage dual npm/PyPI con scanning de malware_

**Tags:** `mcp` `dependency-check` `security` `npm` `pypi`

---

### [SecLists](https://github.com/danielmiessler/seclists)

![](https://img.shields.io/github/stars/danielmiessler/seclists?style=flat-square&label=⭐) · appears in 2 lists

Collection of multiple types of lists used during security assessments.

> **AI analysis:** Colección masiva de wordlists y payloads para testing. Estándar en pentesting. Actualizadas regularmente. Imprescindible en arsenal ofensivo.

**Strengths:** _Cobertura exhaustiva: fuzzing, credenciales, patrones_ · _Actualización activa y comunidad robusta_

**Tags:** `wordlist` `payload` `pentesting` `curado`

---

### [Shodan](https://shodan.io)

appears in 2 lists

Shodan is a search engine for the IOT(Internet of Things) that allows you to search variety of servers that are connected to the internet using various searching filters.

> **AI analysis:** Motor de búsqueda de IoT/servidores expuestos públicamente. Crítico para asset discovery, identificar infraestructura vulnerable. Es de facto estándar en auditoría y threat intel.

**Strengths:** _Base de datos masiva de dispositivos indexados_ · _Filtros avanzados (puerto, banner, geolocalización)_

**Tags:** `iot-search` `vulnerability-scanning` `asset-discovery` `threat-intel`

---

### [Social Engineer Toolkit (SET)](https://github.com/trustedsec/social-engineer-toolkit)

![](https://img.shields.io/github/stars/trustedsec/social-engineer-toolkit?style=flat-square&label=⭐) · appears in 2 lists

Open source pentesting framework designed for social engineering featuring a number of custom attack vectors to make believable attacks quickly.

> **AI analysis:** Framework pentesting enfocado en ingeniería social. Ataques creíbles preseteados (phishing, spear-phishing, payloads). Usado en red teams reales, documentación sólida.

**Strengths:** _Ataques preseteados realistas y probados_ · _Integración con Metasploit, payloads customizables_

**Tags:** `pentesting` `social-engineering` `framework` `python` `red-team`

---

### [SpiderFoot](https://spiderfoot.net)

appears in 2 lists

SpiderFoot is an open source intelligence (OSINT) automation platform with over 200 modules for threat intelligence, attack surface monitoring, security assessments and asset discovery.

> **AI analysis:** Plataforma OSINT automatizada con 200+ módulos. Excelente para asset discovery y threat intel sin hands-on. Open source pero requiere setup. Producción-ready.

**Strengths:** _Automatización masiva reduce manual work 70%+_ · _Modular y extensible, open source_

**Tags:** `osint` `automation` `threat-intel` `asset-discovery`

---

### [SQLMap](https://github.com/sqlmapproject/sqlmap)

![](https://img.shields.io/github/stars/sqlmapproject/sqlmap?style=flat-square&label=⭐) · appears in 2 lists

An automatic SQL injection and database takeover tool.

> **AI analysis:** Herramienta de SQL injection automatizada. Estándar para pentesting y auditorías. Detecta y explota vulnerabilidades SQL; documentación excelente, comunidad activa.

**Strengths:** _Automatización extremadamente efectiva, soporta casi todos los tipos de BD_ · _Actualización constante vs nuevas técnicas de obfuscación_

**Tags:** `penetration-testing` `sql-injection` `python` `automation`

---

### [Syft](https://github.com/anchore/syft)

![](https://img.shields.io/github/stars/anchore/syft?style=flat-square&label=⭐) · appears in 2 lists

CLI tool and library for generating a Software Bill of Materials (SBOM) from container images and filesystems. By [Anchore](https://github.com/anchore).

> **AI analysis:** CLI + librería para generar SBOMs (Software Bill of Materials) desde imágenes container y filesystems. Crítico para seguridad/compliance. Por Anchore, empresa consolidada en supply-chain security.

**Strengths:** _Herramienta en ecosistema maduro (supply-chain security), requisito creciente en enterprise_ · _Activa, open-source, usada en industry_

**Tags:** `sbom` `container-security` `cli` `go` `supply-chain`

---

### [Tails](https://tails.boum.org)

appears in 2 lists

Live operating system aiming to preserve your privacy and anonymity.

> **AI analysis:** Live OS Debian que borra todo al apagar. Para periodistas/activistas que necesitan garantía de no dejar rastros. Solución de privacidad completa, no solo red.

**Strengths:** _Integración transparente de Tor en toda la stack_ · _Amnesia forzada, no hay persistencia accidental_

**Tags:** `anonymity` `live-os` `privacy` `linux`

---

### [Tink](https://github.com/google/tink)

![](https://img.shields.io/github/stars/google/tink?style=flat-square&label=⭐) · appears in 2 lists

A multi-language, cross-platform library that provides cryptographic APIs that are secure, easy to use correctly, and hard(er) to misuse. [Apache-2.0]

> **AI analysis:** Librería criptográfica multi-lenguaje (Google). Diseño: seguro por defecto, APIs imposibles de misuser. Mejor ergonomía que Crypto++. Estándar moderno en seguridad aplicada.

**Strengths:** _APIs imposibles de misuser por diseño_ · _Soporte multi-lenguaje + plataforma_

**Tags:** `cryptography` `multi-language` `secure-by-default`

---

### [Tor](https://torproject.org)

appears in 2 lists

Free software and onion routed overlay network that helps you defend against traffic analysis.

> **AI analysis:** Red de enrutamiento con cebollas estándar de facto. Para cualquiera que necesite privacidad de red. Probada en batalla durante 20+ años, usado por gobiernos y insurgentes.

**Strengths:** _Red más grande y auditada en privacidad_ · _Triple encriptación, protección contra análisis de tráfico comprobada_

**Tags:** `anonymity` `overlay-network` `privacy` `c`

---

### [vaultwarden](https://github.com/dani-garcia/vaultwarden)

![](https://img.shields.io/github/stars/dani-garcia/vaultwarden?style=flat-square&label=⭐) · appears in 2 lists

](https://github.com/dani-garcia/vaultwarden/actions/workflows/build.yml) - Alternative implementation of the Bitwarden server API written in Rust

> **AI analysis:** Clone de Bitwarden API escrito en Rust. Para self-hosters que desconfían de cloud o necesitan auditabilidad. Funciona bien, mantención activa, alternativa seria a Bitwarden.

**Strengths:** _Consumo RAM/CPU mínimo comparado a versión oficial_ · _Deployable en VPS barato sin overhead_

**Tags:** `password-manager` `rust` `self-hosted` `security`

---

### [Virus Total](https://virustotal.com)

appears in 2 lists

Free service that analyzes suspicious files and URLs and facilitates the quick detection of viruses, worms, trojans, and all kinds of malware.

> **AI analysis:** Servicio gratuito de análisis de archivos/URLs contra múltiples antivirus. Escanea malware, trojans, worms. Estándar en OSINT y análisis de seguridad.

**Strengths:** _Base de datos masiva de firmas de 90+ motores_ · _Acceso gratuito sin límites aparentes, API disponible_

**Tags:** `malware` `osint` `antivirus` `saas` `security`

---

### [webpki](https://github.com/briansmith/webpki)

![](https://img.shields.io/github/stars/briansmith/webpki?style=flat-square&label=⭐) · appears in 2 lists

Web PKI TLS X.509 certificate validation in Rust.

> **AI analysis:** Validación X.509/TLS en Rust puro. Reemplaza OpenSSL para PKI sin FFI risk. Core de Rustls. Si implementás TLS o HTTPS client, esto es el gold standard.

**Strengths:** _Validación correcta de certificados sin C deps_ · _Auditoría profesional, usado en producción crítica_

**Tags:** `rust` `tls` `x509` `pkix`

---


---

## 👍 Worth trying — solid in their niche

Less hype than the GEMs but reliable if you fall into their use case.

### [Honeypots](https://github.com/paralax/awesome-honeypots)

![](https://img.shields.io/github/stars/paralax/awesome-honeypots?style=flat-square&label=⭐) · appears in 3 lists

Deception trap, designed to entice an attacker into attempting to compromise the information systems in an organization.

> **AI analysis:** Catálogo de herramientas y proyectos honeypot. Defiende sistemas detectando atacantes. Para teams de seguridad que necesitan inteligencia de amenazas y tráfico malicioso.

**Strengths:** _Cobertura completa de tipos honeypot_ · _Facilita deployment defensivo_

**Tags:** `security` `honeypots` `threat-detection` `curated-list`

---

### [Agentic Radar](https://github.com/splx-ai/agentic-radar)

![](https://img.shields.io/github/stars/splx-ai/agentic-radar?style=flat-square&label=⭐) · appears in 2 lists

Open-source CLI security scanner for agentic workflows. Scans your workflow’s source code, detects vulnerabilities, and generates an interactive visualization along with a detailed security report. Supports LangGraph, CrewAI, n8n, OpenAI Agents, and more.

> **AI analysis:** CLI security scanner para agentic workflows (LangGraph, CrewAI, n8n). Detecta vulnerabilidades en código de agentes, genera reportes. Resuelve problema real: auditar workflows LLM antes de prod.

**Strengths:** _Soporte multi-framework, case de uso urgente (seguridad agentic)_ · _Output visualizable e insights accionables_

**Tags:** `security` `cli` `agentic-workflows` `langraph` `crewai`

---

### [Apache Shiro](https://shiro.apache.org)

appears in 2 lists

Performs authentication, authorization, cryptography and session management.

> **AI analysis:** Framework Apache para autenticación, autorización, criptografía, sesiones. Alternativa a Spring Security. Maduro pero peso pesado.

**Strengths:** _Feature-complete, soporta realm-based auth_ · _Integración simple en apps Java/JVM existentes_

**Tags:** `java` `authentication` `authorization` `security` `apache`

---

### [Botan](https://botan.randombit.net)

appears in 2 lists

Cryptography library written in `C++20`.

> **AI analysis:** Librería crypto en C++20 con algoritmos modernos. Para devs C++ que necesitan crypto integrada sin OpenSSL o dependencias pesadas.

**Strengths:** _C++20 native, code moderno_ · _Cobertura amplia de algoritmos post-quantum_

**Tags:** `cpp20` `cryptography` `library` `algorithms`

---

### [Brave](https://brave.com)

appears in 2 lists

Web browser with an emphasis on privacy and speed. [![Open-Source Software][OSS Icon]](https://github.com/brave/brave-browser/) ![Freeware][Freeware Icon]

> **AI analysis:** Chromium fork con privacy-first, bloquea tracking default, BAT rewards opcional. Open-source. Rápido, buena compatibilidad. Rival real a Chrome en velocidad y privacidad balanceada.

**Strengths:** _Built-in ad/tracker blocking_ · _Updates respetan preferencias user_

**Tags:** `chromium` `privacy` `browser` `open-source`

---

### [CryptoSwift](https://github.com/krzyzanowskim/cryptoswift)

![](https://img.shields.io/github/stars/krzyzanowskim/cryptoswift?style=flat-square&label=⭐) · appears in 2 lists

Crypto related functions and helpers for Swift implemented in Swift programming language.

> **AI analysis:** Criptografía pura Swift (AES, SHA, HMAC, etc.). Para iOS devs que evitan CommonCrypto. Portable, sin dependencias C. Funciona bien pero no domina.

**Strengths:** _Pure Swift, portable entre plataformas_ · _API clara y docs decentes_

**Tags:** `swift` `cryptography` `ios` `aes`

---

### [DNSDumpster](https://dnsdumpster.com)

appears in 2 lists

is a website that will help you discover hosts related to a specific domain.

> **AI analysis:** Web tool para enumerar subdominios vía DNS pasivo. Para pentesters que mapean superficie de ataque. Free pero con limitaciones.

**Strengths:** _Interfaz web simple_ · _Rápido para queries ocasionales_

**Tags:** `dns` `recon` `subdomain-enumeration` `web-tool`

---

### [Element](https://element.io)

appears in 2 lists

Create, share communicate. Chat and call securely. [![Open-Source Software][OSS Icon] ![Freeware][Freeware Icon]](https://github.com/vector-im)

> **AI analysis:** Chat seguro federated basado en Matrix protocol. Open-source, end-to-end encryption. Alternativa a Slack/Discord para orgs que priorizan privacidad.

**Strengths:** _Protocolo abierto federated, no lock-in_ · _E2E encryption por defecto, auditable_

**Tags:** `matrix` `chat` `encrypted` `federation` `open-source`

---

### [Firezone](https://firezone.dev)

appears in 2 lists

Secure remote access gateway that supports the WireGuard protocol. It offers a Web GUI, 1-line install script, multi-factor auth (MFA), and SSO.

> **AI analysis:** VPN/secure gateway moderno con WireGuard, MFA, SSO. Elixir + Docker. Alternativa legítima a OpenVPN/traditional VPN si necesitás remote access corporativo self-hosted con polish moderno.

**Strengths:** _1-line install, setup trivial vs OpenVPN, GUI intuitiva_ · _WireGuard más eficiente y moderno que IPSec/OpenVPN_

**Tags:** `wireguard` `vpn` `self-hosted` `mfa-sso`

---

### [Hunter.io](https://hunter.io)

appears in 2 lists

Data broker providing a Web search interface for discovering the email addresses and other organizational details of a company.

> **AI analysis:** Data broker comercial para email discovery de empleados. Efectivo operativamente pero pagado. Alternativa freemium a brute-force. Usado en recon profesional.

**Strengths:** _Precisión alta en email validation_ · _API y bulk processing disponibles_

**Tags:** `osint` `email-discovery` `brute-force` `paid`

---

### [I2P](https://geti2p.net)

appears in 2 lists

The Invisible Internet Project.

> **AI analysis:** Red P2P de enrutamiento de cebollas para anonimato. Para usuarios que necesitan privacidad contra análisis de tráfico. Menos conocida que Tor pero con arquitectura más distribuida.

**Strengths:** _Arquitectura totalmente descentralizada sin directory servers_ · _Resistente a ataques de correlación de tráfico_

**Tags:** `anonymity` `p2p` `overlay-network` `privacy`

---

### [Keybase](https://keybase.io)

appears in 2 lists

Secure groups, files, and chat for everyone! [![Open-Source Software][OSS Icon]](https://github.com/keybase) ![Freeware][Freeware Icon]

> **AI analysis:** Plataforma de comunicación y colaboración segura con cifrado end-to-end. Open-source pero con desarrollos dispersos, competencia fuerte de Signal y Matrix.

**Strengths:** _Integración con verificación de identidad criptográfica_ · _Chat y archivos en un único ecosistema_

**Tags:** `crypto` `e2e` `chat` `security` `teams`

---

### [kpcyrd/authoscope](https://github.com/kpcyrd/authoscope)

![](https://img.shields.io/github/stars/kpcyrd/authoscope?style=flat-square&label=⭐) · appears in 2 lists

A scriptable network authentication cracker

> **AI analysis:** Cracker de autenticación scriptable en red escrito en Rust. Herramienta de penetration testing para auditoría de credenciales. Útil en labs controlados pero requiere permisos explícitos.

**Strengths:** _Escritura en Rust garantiza seguridad de memoria_ · _Scriptable para automatizar pruebas de autenticación_

**Tags:** `rust` `pentest` `network` `security` `cli`

---

### [kpcyrd/sniffglue](https://github.com/kpcyrd/sniffglue)

![](https://img.shields.io/github/stars/kpcyrd/sniffglue?style=flat-square&label=⭐) · appears in 2 lists

A secure multithreaded packet sniffer

> **AI analysis:** Packet sniffer seguro y multihilo en Rust. Alternativa moderna a tcpdump con mejor manejo de memoria. Para análisis de tráfico y debugging de red.

**Strengths:** _Seguridad de memoria garantizada por Rust_ · _Multithreading nativo sin race conditions_

**Tags:** `rust` `network` `sniffer` `cli` `security`

---

### [LibreWolf](https://librewolf.net)

appears in 2 lists

A fork of Firefox, focused on privacy, security and freedom. [![Open-Source Software][OSS Icon]](https://gitlab.com/librewolf-community) ![Freeware][Freeware Icon]

> **AI analysis:** Fork Firefox hardened para privacidad y seguridad. Desactiva telemetría Mozilla, DRM, pocket. Compilado limpio. Ligero pero requiere usuarios tech-savvy. Niche privacy-first.

**Strengths:** _Telemetría completamente removida_ · _Compilación reproducible_

**Tags:** `firefox` `privacy` `hardened` `open-source`

---

### [Maltego](https://maltego.com)

appears in 2 lists

Maltego is an open source intelligence (OSINT) and graphical link analysis tool for gathering and connecting information for investigative tasks.

> **AI analysis:** Herramienta OSINT visual de link analysis para correlacionar datos. Potente para investigaciones, pero curva de aprendizaje empinada. Versión free limitada.

**Strengths:** _Visualización excepcional de conexiones entre entidades_ · _Cientos de transforms para datasources_

**Tags:** `osint` `graph-analysis` `link-analysis` `investigacion`

---

### [mariocandela/beelzebub](https://github.com/mariocandela/beelzebub)

![](https://img.shields.io/github/stars/mariocandela/beelzebub?style=flat-square&label=⭐) · appears in 2 lists

☁️ - Beelzebub is a honeypot framework that lets you build honeypot tools using MCP. Its purpose is to detect prompt injection or malicious agent behavior. The underlying idea is to provide the agent with tools it would never use in its normal work.

> **AI analysis:** Honeypot framework con MCP para detectar prompt injection en agentes IA. Idea interesante: proporciona tools carnada que un agente legítimo nunca tocaría. Nicho: seguridad de agentes, no de infraestructura clásica.

**Strengths:** _Enfoque novel: usar herramientas carnada como signal de compromiso en agentes_ · _Integración con MCP standard para extensibilidad_

**Tags:** `honeypot` `security` `ai-safety` `prompt-injection` `mcp`

---

### [mavdol/capsule/mcp-server](https://github.com/mavdol/capsule)

![](https://img.shields.io/github/stars/mavdol/capsule?style=flat-square&label=⭐) · appears in 2 lists

](https://glama.ai/mcp/servers/mavdol/capsule-mcp-server) 🦀 🏠 🍎 🪟 🐧 - Run untrusted Python/JavaScript code in WebAssembly sandboxes.

> **AI analysis:** MCP server que ejecuta código Python/JavaScript untrusted en sandboxes WebAssembly. Previene exploits de agentes maliciosos. Para AI safety critical.

**Strengths:** _Isolación real via WASM, sin escape path obvio_ · _Soporte dual Python/JavaScript_

**Tags:** `mcp` `wasm` `sandbox` `rust` `security`

---

### [Ockam](https://github.com/ockam-network/ockam)

![](https://img.shields.io/github/stars/ockam-network/ockam?style=flat-square&label=⭐) · appears in 2 lists

_(label: good first issue)_ <br> End-to-end encryption and mutual authentication for distributed applications.

> **AI analysis:** Toolkit para encriptación e2e y autenticación mutua en apps distribuidas. Resuelve confianza en arquitecturas mesh/zero-trust reales.

**Strengths:** _Abstracciones portables para transporte (TCP, UDP, Bluetooth)_ · _Modelo de seguridad auditado para comms distribuidas_

**Tags:** `rust` `cryptography` `distributed` `security`

---

### [orion-rs/orion](https://github.com/orion-rs/orion)

![](https://img.shields.io/github/stars/orion-rs/orion?style=flat-square&label=⭐) · appears in 2 lists

This library aims to provide easy and usable crypto. 'Usable' meaning exposing high-level API's that are easy to use and hard to misuse. [](https://github.com/orion-rs/orion/actions/workflows/test.yml)

> **AI analysis:** Librería Rust que prioriza API usable y resistente a misuso. Para devs que quieren crypto sin ser expertos. High-level abstractions sobre primitivas peligrosas.

**Strengths:** _API deliberadamente difícil de misusar, errores en compile-time_ · _Documentación clara con ejemplos de misuso común_

**Tags:** `rust` `cryptography` `security` `high-level-api` `library`

---

### [paaster](https://paaster.io)

appears in 2 lists

Paaster is a secure and user-friendly pastebin application that prioritizes privacy and simplicity. With end-to-end encryption and paste history, Paaster ensures that your pasted code remains confidential and accessible.

> **AI analysis:** Pastebin con cifrado end-to-end y historial. Resuelve problema real (privacidad en compartir snippets). Alternativa directa a servicios centralizados pero ecosistema pastebin saturado.

**Strengths:** _E2E encryption nativo_ · _Historial preservado_

**Tags:** `pastebin` `encryption` `privacy` `self-hosted`

---

### [Promptfoo](https://github.com/promptfoo/promptfoo)

![](https://img.shields.io/github/stars/promptfoo/promptfoo?style=flat-square&label=⭐) · appears in 2 lists

- LLM red teaming and evaluation framework for testing jailbreaks, prompt injection, and other vulnerabilities with CI/CD integration.

> **AI analysis:** Framework para testear LLMs contra injection, jailbreaks y vulnerabilidades. Red teaming automatizado con CI/CD. Necesario si desplegás LLMs en producción y querés seguridad serio.

**Strengths:** _Cubre vectores de ataque específicos de LLMs_ · _CI/CD integration out-of-box_

**Tags:** `llm-security` `red-teaming` `prompt-injection` `ci-cd` `testing`

---

### [rage](https://github.com/str4d/rage)

![](https://img.shields.io/github/stars/str4d/rage?style=flat-square&label=⭐) · appears in 2 lists

is a simple, modern, and secure file encryption tool, using the age format.

> **AI analysis:** Herramienta de cifrado de archivos moderna en Rust, usa formato age. Simple, rápido, sin opciones criptográficas débiles. Reemplaza GPG para cifrado de archivos básico.

**Strengths:** _Interfaz minimalista, sin opciones inseguras_ · _Rápido, código limpio y auditable_

**Tags:** `encryption` `rust` `file-encryption` `age-format` `cli`

---

### [Redlib](https://github.com/redlib-org/redlib)

![](https://img.shields.io/github/stars/redlib-org/redlib?style=flat-square&label=⭐) · appears in 2 lists

An alternative private front-end to Reddit, with its origins in [Libreddit](https://github.com/libreddit/libreddit)

> **AI analysis:** Frontend privado para Reddit (fork de Libreddit). Reemplaza JS con Rust. Útil si querés Reddit sin tracker. Activa pero depende API Reddit que puede cambiar.

**Strengths:** _Zero JavaScript, performance_ · _Privacy-focused, open source_

**Tags:** `rust` `frontend` `privacy` `reddit`

---

### [rshijack](https://github.com/kpcyrd/rshijack)

![](https://img.shields.io/github/stars/kpcyrd/rshijack?style=flat-square&label=⭐) · appears in 2 lists

TCP connection hijacker, Rust rewrite of `shijack`.

> **AI analysis:** Hijacker de conexiones TCP reescrito en Rust desde shijack. Herramienta avanzada para auditoría de red e investigación. Uso restrictivo, requiere permisos.

**Strengths:** _Implementación limpia en Rust de técnica clásica_ · _Mantenimiento activo por kpcyrd_

**Tags:** `rust` `pentest` `network` `tcp` `cli`

---

### [sherlock](https://github.com/sherlock-project/sherlock)

![](https://img.shields.io/github/stars/sherlock-project/sherlock?style=flat-square&label=⭐) · appears in 2 lists

Hunt down social media accounts by username across social networks.

> **AI analysis:** Script que busca cuentas de redes sociales por username. Útil para OSINT y verificación de brand. Funciona pero es básico: no elude throttling ni captchas sofisticados.

**Strengths:** _Setup trivial, útil para auditorías rápidas de availability de usernames_ · _Soporta muchas plataformas_

**Tags:** `osint` `social-media` `python` `cli`

---

### [ssh-vault](https://github.com/ssh-vault/ssh-vault)

![](https://img.shields.io/github/stars/ssh-vault/ssh-vault?style=flat-square&label=⭐) · appears in 2 lists

A simple tool to manage secrets using ssh keys for encryption and decryption.

> **AI analysis:** Gestor de secretos minimalista basado en claves SSH. Usa SSH para cifrar/descifrar sin infraestructura extra. Útil para equipos pequeños que ya tienen SSH setup.

**Strengths:** _Cero dependencias externas, aprovecha claves SSH existentes_ · _Muy simple de usar, overhead mínimo_

**Tags:** `secrets-management` `ssh` `encryption` `cli` `golang`

---

### [Swift-Sodium](https://github.com/jedisct1/swift-sodium)

![](https://img.shields.io/github/stars/jedisct1/swift-sodium?style=flat-square&label=⭐) · appears in 2 lists

Swift interface to the Sodium library for common crypto operations for iOS and macOS.

> **AI analysis:** Swift binding a libsodium (NaCl moderno). Criptografía contemporánea (AEAD, key exchange). Para quien necesita algo beyond AES. Bien mantenido.

**Strengths:** _Acceso a libsodium battle-tested; AEAD + key derivation_ · _Mantenimiento activo, usado en prod_

**Tags:** `swift` `libsodium` `nacl` `cryptography` `authenticated-encryption`

---

### [The Harvester](https://github.com/laramies/theharvester)

![](https://img.shields.io/github/stars/laramies/theharvester?style=flat-square&label=⭐) · appears in 2 lists

Gather emails, subdomains, hosts, employee names, open ports and banners from different public sources like search engines, PGP key servers and SHODAN computer database.

> **AI analysis:** Herramienta OSINT clásica para recopilación pasiva: emails, subdominios, hosts desde fuentes públicas. Útil en reconocimiento inicial de red, pentesting. Todavía mantiene relevancia aunque algunas fuentes se han degradado.

**Strengths:** _Agregador maduro de múltiples fuentes públicas_ · _Baja curva de entrada, output útil inmediato_

**Tags:** `osint` `reconnaissance` `python` `email-scraping` `cli`

---

### [Trail of Bits Security Skills](https://github.com/trailofbits/skills)

![](https://img.shields.io/github/stars/trailofbits/skills?style=flat-square&label=⭐) · appears in 2 lists

by [Trail of Bits](https://github.com/trailofbits) - A very professional collection of over a dozen security-focused skills for code auditing and vulnerability detection. Includes skills for static analysis with CodeQL and Semgrep, variant analysis across codebases, fix verification, and differential code review.

> **AI analysis:** Colección de skills de seguridad para auditoría de código y análisis de vulnerabilidades. Incluye CodeQL y Semgrep. Producción Trail of Bits.

**Strengths:** _Creado por referentes en security (Trail of Bits)_ · _Cubre análisis estático, variante y code review diferencial_

**Tags:** `security` `code-audit` `codeql` `semgrep`

---

### [WiGLE](https://wigle.net)

appears in 2 lists

Wi-fi "wardriving" database. Contains a global map containing crowdsourced information on the location, name, and other properties of wi-fi networks. Software available to download to contribute data to the public infoset.

> **AI analysis:** Base de datos colaborativa global de redes Wi-Fi. Niche pero preciso para wardriving, geolocalización pasiva. Comunidad activa manteniendo datos.

**Strengths:** _Cobertura global con aporte comunitario_ · _Herramienta propia para captura de datos_

**Tags:** `wifi-mapping` `geolocation` `wardriving` `crowdsourced`

---

### [x64dbg](https://x64dbg.com)

appears in 2 lists

An open-source x64/x32 debugger for windows.

> **AI analysis:** Debugger x64 assembly para Windows. Para reverse engineers que necesitan paso a paso en binarios sin fuentes. Similar a OllyDbg pero actualizado.

**Strengths:** _UI moderna vs OllyDbg antiguo_ · _Breakpoints avanzados, plugin ecosystem activo_

**Tags:** `debugger` `reverse-engineering` `x64` `windows`

---


---

<sub>📄 Auto-generated from [juanchi.dev](https://juanchi.dev) · [system source](https://juanchi.dev/blog/series/awesome-curated) · MIT licensed</sub>
