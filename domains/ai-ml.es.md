# 🤖 IA y ML — Awesome Curated

<p><sub>← [Volver al main](../README.es.md)</sub></p>

**36 GEMs · 78 Vale probar**

---

## ⭐ GEMs — estándares de la industria

Herramientas que la comunidad considera default. Si no las conocés, valen la pena.

### 👤 [BayesWitnesses/m2cgen](https://github.com/bayeswitnesses/m2cgen)

![](https://img.shields.io/github/stars/bayeswitnesses/m2cgen?style=flat-square&label=⭐) · 🔥 **aparece en 7 listas**

A CLI tool to transpile trained classic machine learning models into a native Rust code with zero dependencies. [](https://github.com/BayesWitnesses/m2cgen/actions)

> **Análisis IA:** Esto resuelve un problema muy concreto y doloroso: deployar un modelo de ML sin cargar con scikit-learn, joblib o cualquier runtime de Python. Entrenás en Python, exportás a Go, Java o lo que necesites, y lo corrés en producción sin dependencias. Ideal para embedded, microservicios livianos o entornos donde instalar Python es un problema. El límite es que solo soporta modelos clásicos (árboles, regresión, SVM); si estás en deep learning, no te sirve. Valor real y bien acotado.

**Fortalezas:** _Elimina dependencias de runtime de ML en producción: el código generado es nativo y standalone_ · _Soporte genuinamente amplio de lenguajes destino (12+), cubriendo stacks enterprise como Java y C# además de modernos como Go y Dart_

**Tags:** `machine-learning` `code-generation` `model-export` `open-source` `multi-language`

---

### [XGBoost](https://github.com/dmlc/xgboost)

![](https://img.shields.io/github/stars/dmlc/xgboost?style=flat-square&label=⭐) · 🔥 **aparece en 5 listas**

- XGBoost is an optimized distributed gradient boosting library designed to be highly efficient, flexible and portable.

> **Análisis IA:** Un clásico que se ganó su lugar con resultados reales. XGBoost es el algoritmo que dominó Kaggle durante años y sigue siendo referencia obligada para datos tabulares. No es hype: es matemática sólida con implementación optimizada. Si trabajás con datasets estructurados y necesitás precisión sin entrar en deep learning, esto es tu herramienta. El soporte multi-lenguaje y la integración con Spark/Hadoop lo hacen viable tanto para prototipo como para producción a escala. Biblioteca madura y battle-tested.

**Fortalezas:** _Performance excepcional en datos tabulares: históricamente supera a otros algoritmos en benchmarks y competencias reales_ · _Soporte nativo para entornos distribuidos (Spark, Hadoop, Flink) sin cambios mayores en el código_

**Tags:** `machine-learning` `gradient-boosting` `python` `distributed` `open-source`

---

### [Apache Spark](https://github.com/apache/spark)

![](https://img.shields.io/github/stars/apache/spark?style=flat-square&label=⭐) · aparece en 3 listas

- Micro-batch processing for streams using the apache spark framework as a backend supporting stateful exactly-once semantics.

> **Análisis IA:** Memory layer para AI agents con persistencia de contexto. Para chatbots/assistants que necesiten continuidad cross-session. Promesa: no perder contexto entre interacciones.

**Fortalezas:** _Abstracción limpia memory store_ · _Soporta múltiples backends (vector DB, SQL)_

**Tags:** `ai-agents` `memory` `python` `storage` `llm`

---

### [Awesome Machine Learning](https://github.com/josephmisiti/awesome-machine-learning)

![](https://img.shields.io/github/stars/josephmisiti/awesome-machine-learning?style=flat-square&label=⭐) · aparece en 3 listas

*(GitHub)*

> **Análisis IA:** El repo de awesome-ml de referencia absoluta. Con más de 60k stars y años de curaduría, es el punto de entrada obligado para cualquier dev que quiere orientarse en el ecosistema ML: frameworks, librerías, datasets, papers, todo organizado por lenguaje. No es hype, es infraestructura de conocimiento. El problema es que la velocidad del campo lo deja siempre un poco desactualizado, y la cantidad de entradas puede abrumar sin criterio de calidad claro.

**Fortalezas:** _Cobertura exhaustiva organizada por lenguaje de programación, útil tanto para pythonistas como para devs de R, Julia o Go_ · _Punto de entrada canónico con décadas de curaduría comunitaria y miles de contribuidores reales_

**Tags:** `machine-learning` `awesome-list` `recursos` `open-source` `curated-list`

---

### [SpaCy](https://github.com/explosion/spacy)

![](https://img.shields.io/github/stars/explosion/spacy?style=flat-square&label=⭐) · aparece en 3 listas

- spaCy is a library for advanced Natural Language Processing in Python and Cython.

> **Análisis IA:** Librería NLP production-ready con tokenización, tagging, parsing. Más veloz y práctica que NLTK. Resuelve bien procesamiento de texto en pipelines reales, no research.

**Fortalezas:** _Performance alta en C (Cython), listo para producción_ · _Modelos pre-entrenados optimizados y muy documentados_

**Tags:** `nlp` `python` `spacy` `nlp-pipeline` `production`

---

### [Stable Baselines](https://github.com/dlr-rm/stable-baselines3)

![](https://img.shields.io/github/stars/dlr-rm/stable-baselines3?style=flat-square&label=⭐) · aparece en 3 listas

- A fork of OpenAI Baselines, implementations of reinforcement learning algorithms.

> **Análisis IA:** Implementaciones de algoritmos RL (DQN, PPO, A2C) basadas en OpenAI Baselines. Para researchers y practitioners que necesitan baseline sólidos. Mantención activa, PyTorch/TensorFlow ready.

**Fortalezas:** _APIs consistentes y bien testeadas_ · _Soporta múltiples backends (Torch, TF, JAX)_

**Tags:** `reinforcement-learning` `python` `pytorch` `tensorflow`

---

### [Vercel AI](https://github.com/vercel/ai)

![](https://img.shields.io/github/stars/vercel/ai?style=flat-square&label=⭐) · aparece en 3 listas

- Vercel AI is a TypeScript toolkit designed to help you build AI-powered applications using popular frameworks like Next.js, React, Svelte, Vue and runtimes like Node.js.

> **Análisis IA:** Toolkit TypeScript para integrar IA en Next.js/React/Node.js. Abstrae múltiples proveedores de LLMs. Resuelve: construir apps IA rápido sin lock-in de proveedor.

**Fortalezas:** _Abstracción consistente entre modelos_ · _Integración perfecta con Next.js_

**Tags:** `typescript` `nextjs` `react` `llm-integration`

---

### [ashvardanian/NumKong](https://github.com/ashvardanian/numkong)

![](https://img.shields.io/github/stars/ashvardanian/numkong?style=flat-square&label=⭐) · aparece en 2 listas

SIMD-accelerated vector distances and similarity functions for x86 AVX2 & AVX-512, and Arm NEON [](https://crates.io/crates/simsimd)

> **Análisis IA:** Librería Rust de distancias vectoriales con SIMD nativo para x86 AVX2/AVX-512 y ARM NEON. Resuelve el cuello de botella real de cómputo en búsqueda vectorial y ML. Essential para sistemas críticos en performance.

**Fortalezas:** _SIMD puro sin overhead de binding a C_ · _Soporta múltiples arquitecturas (AVX2, AVX-512, NEON) con fallback automático_

**Tags:** `rust` `simd` `vector-search` `avx512` `neon`

---

### [Detectron2](https://github.com/facebookresearch/detectron2)

![](https://img.shields.io/github/stars/facebookresearch/detectron2?style=flat-square&label=⭐) · aparece en 2 listas

- Detectron2 is Facebook AI Research's next generation library that provides state-of-the-art detection and segmentation algorithms.

> **Análisis IA:** SOTA para detección y segmentación de objetos. PyTorch-based, de Meta. Código production-ready, benchmarks líderes. Estándar en computer vision moderno, compite con YOLOv8.

**Fortalezas:** _SOTA accuracy en coco/benchmarks_ · _Código limpio, extensible, models variados preentrenados_

**Tags:** `python` `computer-vision` `detection` `segmentation` `pytorch`

---

### [Dlib](https://github.com/davisking/dlib)

![](https://img.shields.io/github/stars/davisking/dlib?style=flat-square&label=⭐) · aparece en 2 listas

zap: - A toolkit for making real world machine learning and data analysis applications in C++. [Boost] [website](http://dlib.net/)

> **Análisis IA:** JAX combina Autograd con compilador XLA para ML research. Diferenciación automática funcional y JIT compilation. Potente pero curva de aprendizaje vertical para quién viene de NumPy/PyTorch.

**Fortalezas:** _Composición funcional elegante, vectorization transparente_ · _Performance comparable a TensorFlow en operaciones complejas_

**Tags:** `python` `automatic-differentiation` `jit-compiler` `numpy-compatible`

---

### [EspNet](https://github.com/espnet/espnet)

![](https://img.shields.io/github/stars/espnet/espnet?style=flat-square&label=⭐) · aparece en 2 listas

ESPnet is an end-to-end speech processing toolkit for tasks like speech recognition, translation, and enhancement, using PyTorch and Kaldi-style data processing.

> **Análisis IA:** Toolkit end-to-end consolidado para speech processing: ASR, traducción, enhancement. Stack PyTorch + Kaldi. Estándar en academia, buena docs, comunidad activa. Algo pesado para tareas simples.

**Fortalezas:** _Cobertura completa de pipelines speech_ · _Buena documentación y ejemplos reproducibles_

**Tags:** `speech-processing` `pytorch` `asr` `end-to-end`

---

### [Evidently](https://github.com/evidentlyai/evidently)

![](https://img.shields.io/github/stars/evidentlyai/evidently?style=flat-square&label=⭐) · aparece en 2 listas

- Evidently is an open-source framework to evaluate, test and monitor ML and LLM-powered systems.

> **Análisis IA:** Framework para evaluar, testear y monitorear sistemas ML/LLM. Métricas data drift, model performance, LLM outputs. Para equipos con modelos en producción. Resuelve observabilidad de ML.

**Fortalezas:** _Reportes interactivos muy claros sobre data drift_ · _Cobertura amplia: tabular, NLP, CV, LLM_

**Tags:** `python` `mlops` `monitoring` `data-drift` `testing`

---

### [Faiss](https://github.com/facebookresearch/faiss)

![](https://img.shields.io/github/stars/facebookresearch/faiss?style=flat-square&label=⭐) · aparece en 2 listas

- Faiss is a library for efficient similarity search and clustering of dense vectors.

> **Análisis IA:** Librería de búsqueda de similitud vectorial de Meta Research. Estándar en RAG, recomendación, clustering. GPU-acelerada. Producción en scale.

**Fortalezas:** _Performance SOTA en búsqueda de k-NN sobre millones de vectores_ · _Índices especializados (HNSW, IVF) con tuning fino_

**Tags:** `machine-learning` `similarity-search` `vector-db` `gpu` `python`

---

### [GoCV](https://github.com/hybridgroup/gocv)

![](https://img.shields.io/github/stars/hybridgroup/gocv?style=flat-square&label=⭐) · aparece en 2 listas

Package for computer vision using OpenCV 4 and beyond.

> **Análisis IA:** Binding Go para OpenCV 4+. Std de facto para CV en Go. Activo, bien mantenido, excelente para servicios CV en producción. Comunidad sólida.

**Fortalezas:** _Binding limpio y completo a OpenCV 4_ · _Performance cercano a C++ nativo sin overhead_

**Tags:** `go` `opencv` `computer-vision` `binding` `production-ready`

---

### [Gymnasium](https://github.com/farama-foundation/gymnasium)

![](https://img.shields.io/github/stars/farama-foundation/gymnasium?style=flat-square&label=⭐) · aparece en 2 listas

- Gymnasium is an open source Python library for developing and comparing reinforcement learning algorithms by providing a standard API to communicate between learning algorithms and environments, as well as a standard set of environments compliant with that API.

> **Análisis IA:** Estándar de facto para RL en Python. Gymnasium reemplazó a OpenAI Gym, proporciona API unificada para entrenar agentes contra ambientes simulados. Imprescindible si hacés RL serio.

**Fortalezas:** _API estable y bien documentada, compatibilidad con 1000+ ambientes_ · _Mantenimiento activo por Farama Foundation, reemplazo directo de Gym con mejoras_

**Tags:** `reinforcement-learning` `python` `api-standard` `simulation`

---

### [huggingface/tokenizers](https://github.com/huggingface/tokenizers)

![](https://img.shields.io/github/stars/huggingface/tokenizers?style=flat-square&label=⭐) · aparece en 2 listas

Hugging Face's tokenizers for modern NLP pipelines (original implementation) with bindings for Python. [](https://github.com/huggingface/tokenizers/actions)

> **Análisis IA:** Tokenizadores ultra-optimizados de HF. Referencia en NLP moderno, usado en casi todo pipeline serio. Rust puro con bindings Python, 10-100x más rápido que alternativas.

**Fortalezas:** _Performance extremo, manejo eficiente de vocabularios grandes_ · _Integración perfecta con transformers HF, bindings Python de primera clase_

**Tags:** `nlp` `tokenization` `rust` `huggingface`

---

### [InterpretML](https://github.com/interpretml/interpret)

![](https://img.shields.io/github/stars/interpretml/interpret?style=flat-square&label=⭐) · aparece en 2 listas

InterpretML implements the Explainable Boosting Machine (EBM), a modern, fully interpretable machine learning model based on Generalized Additive Models (GAMs). This open-source package also provides visualization tools for EBMs, other glass-box models, and black-box explanations.

> **Análisis IA:** ML interpretable con Explainable Boosting Machines (EBM). Resuelve el problema real de explicabilidad en modelos sin sacrificar performance. Para data scientists que necesitan auditar decisiones.

**Fortalezas:** _Modelos interpretables por defecto, no post-hoc_ · _Visualizaciones robustas para stakeholders no-técnicos_

**Tags:** `interpretable-ml` `python` `glass-box` `visualization`

---

### [Jax](https://github.com/jax-ml/jax)

![](https://img.shields.io/github/stars/jax-ml/jax?style=flat-square&label=⭐) · aparece en 2 listas

- Composable transformations of Python+NumPy programs: differentiate, vectorize, JIT to GPU/TPU, and more.

> **Análisis IA:** Framework ML Python: diferenciación automática, vectorización y JIT a GPU/TPU. Estándar en research de IA, compite con PyTorch. Más funcional, menos mainstream.

**Fortalezas:** _Transformaciones composables superiores a PyTorch_ · _JIT compilation transparente a cualquier backend_

**Tags:** `python` `ml` `jit` `gpu` `autodiff`

---

### [Kaldi](https://github.com/kaldi-asr/kaldi)

![](https://img.shields.io/github/stars/kaldi-asr/kaldi?style=flat-square&label=⭐) · aparece en 2 listas

Kaldi is a toolkit for speech recognition written in C++ and licensed under the Apache License v2.0. Kaldi is intended for use by speech recognition researchers.

> **Análisis IA:** Toolkit C++ de referencia para ASR, usado en investigación y producción. Proporciona componentes sólidos para speech recognition end-to-end. Estándar de facto en academia.

**Fortalezas:** _Estándar en investigación ASR desde 2010+_ · _Componentes modulares y bien documentados para researchers_

**Tags:** `speech-recognition` `asr` `c++` `toolkit` `kaldi`

---

### [LlamaIndex](https://github.com/run-llama/llama_index)

![](https://img.shields.io/github/stars/run-llama/llama_index?style=flat-square&label=⭐) · aparece en 2 listas

- LlamaIndex (GPT Index) is a data framework for your LLM application.

> **Análisis IA:** Data framework para RAG/retrieval en LLM apps. Estándar en la industria para augment LLMs con docs. Maduro, bien mantenido, opción default.

**Fortalezas:** _Integración completa con 50+ data sources y LLMs_ · _Abstracciones de retrieval robustas (query engines)_

**Tags:** `rag` `retrieval` `llm-framework` `python`

---

### [Milvus](https://github.com/milvus-io/milvus)

![](https://img.shields.io/github/stars/milvus-io/milvus?style=flat-square&label=⭐) · aparece en 2 listas

Milvus is a cloud-native, open-source vector database built to manage embedding vectors generated by machine learning models and neural networks.

> **Análisis IA:** Vector database cloud-native para embeddings. Estándar en RAG/search, competidor serio de Pinecone con mejor control operacional.

**Fortalezas:** _Self-hosted option viable vs Pinecone SaaS_ · _Escalabilidad y performance demostrada en prod_

**Tags:** `vector-database` `embeddings` `cloud-native` `python`

---

### [Ollama](https://github.com/ollama/ollama)

![](https://img.shields.io/github/stars/ollama/ollama?style=flat-square&label=⭐) · aparece en 2 listas

- Get up and running with large language models, locally.

> **Análisis IA:** Ejecuta LLMs localmente sin GPU costosa. Para developers, researchers y quién necesita privacidad. Reemplaza dependencia de APIs remotas. Instalación trivial, interface elegante.

**Fortalezas:** _Setup one-liner, soporte para decenas de modelos (Llama, Mistral, etc.)_ · _Sin dependencias cloud, control total de datos_

**Tags:** `llm` `local-inference` `docker` `go` `open-source`

---

### [oneDNN](https://github.com/oneapi-src/onednn)

![](https://img.shields.io/github/stars/oneapi-src/onednn?style=flat-square&label=⭐) · aparece en 2 listas

An open-source cross-platform performance library for deep learning applications. [Apache] [website](https://01.org/onednn)

> **Análisis IA:** Performance library para DL, optimiza kernels CPU/GPU. Usada por PyTorch/TensorFlow internamente. Para production DL en hardware especializado, es GEM.

**Fortalezas:** _Optimizaciones hardware-specific probadas en producción_ · _Mantenida por Intel, estándar de facto_

**Tags:** `deep-learning` `cpp` `cpu-optimization` `gpu`

---

### [Optuna](https://github.com/optuna/optuna)

![](https://img.shields.io/github/stars/optuna/optuna?style=flat-square&label=⭐) · aparece en 2 listas

- Optuna is an automatic hyperparameter optimisation software framework, particularly designed for machine learning.

> **Análisis IA:** Framework para optimización automática de hiperparámetros con algoritmos sofisticados (TPE, Bayesiano). Resuelve problema real: buscar hyper-params sin tedio, escala a miles de trials.

**Fortalezas:** _Algoritmos avanzados incorporados (TPE, CMA-ES), better than grid search_ · _Distributed ready, integración con Ray/Dask_

**Tags:** `hyperparameter-optimization` `bayesian-search` `ml-pipeline`

---

### [PEFT](https://github.com/huggingface/peft)

![](https://img.shields.io/github/stars/huggingface/peft?style=flat-square&label=⭐) · aparece en 2 listas

- Parameter-Efficient Fine-Tuning (PEFT) methods enable efficient adaptation of pre-trained language models (PLMs) to various downstream applications without fine-tuning all the model's parameters.

> **Análisis IA:** Framework HuggingFace para adaptar LLMs con pocas memoria/compute (LoRA, QLoRA, prefix-tuning). Esencial para fine-tuning eficiente. Estándar industrial de facto en ML.

**Fortalezas:** _Reduce parámetros entrenables en 90%+; compatible con cualquier modelo HF_ · _Comunidad masiva, docs exhaustivas_

**Tags:** `fine-tuning` `lora` `transformers` `python` `huggingface`

---

### [PyOD](https://github.com/yzhao062/pyod)

![](https://img.shields.io/github/stars/yzhao062/pyod?style=flat-square&label=⭐) · aparece en 2 listas

> Python Outlier Detection, comprehensive and scalable Python toolkit for detecting outlying objects in multivariate data. Featured for Advanced models, including Neural Networks/Deep Learning and Outlier Ensembles.

> **Análisis IA:** Toolkit Python para detección de outliers en datos multivariados. Soporta algoritmos clásicos y redes neuronales. Madura, bien mantenida, estándar en data science.

**Fortalezas:** _50+ algoritmos, desde Isolation Forest a autoencoders_ · _Interfaz sklearn-compatible, integra sin fricción_

**Tags:** `python` `anomaly-detection` `machine-learning` `scikit-compatible`

---

### [PySyft](https://github.com/openmined/pysyft)

![](https://img.shields.io/github/stars/openmined/pysyft?style=flat-square&label=⭐) · aparece en 2 listas

- A Python library for secure, private Deep Learning. PySyft decouples private data from model training, using Multi-Party (MPC) within PyTorch.

> **Análisis IA:** ML con privacidad usando multi-party computation. Resuelve problema real de datos sensibles sin exponerlos. Niche empresarial/healthcare, importante pero adopción lenta.

**Fortalezas:** _Único framework maduro para privacy-preserving ML en Python_ · _Integración cleancon PyTorch existente_

**Tags:** `privacy-preserving` `federated-learning` `python` `pytorch` `mpc`

---

### [PyTorch Lightning](https://github.com/lightning-ai/pytorch-lightning)

![](https://img.shields.io/github/stars/lightning-ai/pytorch-lightning?style=flat-square&label=⭐) · aparece en 2 listas

- PyTorch Lightning pretrains, finetunes and deploys AI models on multiple GPUs, TPUs with zero code changes.

> **Análisis IA:** Wrapper de PyTorch que abstrae boilerplate para entrenamiento distribuido en multi-GPU/TPU. Estándar de facto en research deep learning. Resuelve problema real: pasar de 1 GPU a multi-device sin reescribir código.

**Fortalezas:** _Reduce líneas de código boilerplate en 70%+ sin sacrificar control_ · _Integración nativa con multi-GPU/TPU, logging, checkpoints automáticos_

**Tags:** `pytorch` `deep-learning` `distributed-training` `python` `ml`

---

### [Qdrant](https://github.com/qdrant/qdrant)

![](https://img.shields.io/github/stars/qdrant/qdrant?style=flat-square&label=⭐) · aparece en 2 listas

An open source vector similarity search engine with extended filtering support [](https://github.com/qdrant/qdrant/actions)

> **Análisis IA:** Vector DB open-source production-grade: búsqueda similarity + filtering avanzado. Rust, rápido, bien mantenido. Estándar emergente junto a Pinecone. Ideal para RAG, recsys, semantic search.

**Fortalezas:** _Filtering avanzado (mejor que Pinecone v1)_ · _Cluster distribuido nativo, prod-ready_

**Tags:** `vector-db` `rust` `similarity-search` `filtering` `self-hosted`

---

### [Sacred](https://github.com/idsia/sacred)

![](https://img.shields.io/github/stars/idsia/sacred?style=flat-square&label=⭐) · aparece en 2 listas

Python tool to help you configure, organize, log and reproduce experiments. Like a notebook lab in the context of Chemistry/Biology. The community has built multiple add-ons leveraging the proposed standard.

> **Análisis IA:** Framework Python para reproducibilidad experimental con logging y tracking integrado. Estándar en ML research hace años. Comunidad activa construyó plugins (Neptune, MLflow). Si hacés experimentos iterativos, vale.

**Fortalezas:** _Estándar de facto en ML academia_ · _Ecosystem de add-ons maduro_

**Tags:** `python` `reproducibility` `ml-experiment` `logging` `research`

---

### [scikit-learn](https://scikit-learn.org)

aparece en 2 listas

A Python module for machine learning built on top of SciPy.

> **Análisis IA:** Librería ML Python con algoritmos clásicos (clustering, regression, classification). Estándar absoluto, first choice para ML tradicional y baseline models.

**Fortalezas:** _Documentación de oro, API consistente_ · _Ecosistema maduro con miles de ejemplos_

**Tags:** `python` `machine-learning` `scikit-learn` `scipy`

---

### [TF-Agents](https://github.com/tensorflow/agents)

![](https://img.shields.io/github/stars/tensorflow/agents?style=flat-square&label=⭐) · aparece en 2 listas

- A reliable, scalable and easy to use TensorFlow library for contextual bandits and reinforcement learning.

> **Análisis IA:** TF-Agents es librería TensorFlow para reinforcement learning y contextual bandits. APIs claras, bien documentada, producción-ready. Nicho específico pero sólido si necesitás RL.

**Fortalezas:** _APIs consistentes y documentación corporate-grade_ · _Algoritmos RL comprobados (DQN, PPO, DDPG)_

**Tags:** `reinforcement-learning` `tensorflow` `python` `contextual-bandits`

---

### [vLLM](https://github.com/vllm-project/vllm)

![](https://img.shields.io/github/stars/vllm-project/vllm?style=flat-square&label=⭐) · aparece en 2 listas

- vLLM is a high-throughput and memory-efficient inference and serving engine for LLMs.

> **Análisis IA:** Motor inference/serving de LLMs con throughput y memoria optimizados. PagedAttention elimina fragmentación. Standard para servir Llama/Mistral en producción.

**Fortalezas:** _PagedAttention revolucionó memory efficiency_ · _Soporte multi-LoRA y batching dinámico nativo_

**Tags:** `llm-inference` `serving` `cuda` `python`

---

### [Vowpal Wabbit](https://github.com/vowpalwabbit/vowpal_wabbit)

![](https://img.shields.io/github/stars/vowpalwabbit/vowpal_wabbit?style=flat-square&label=⭐) · aparece en 2 listas

Vowpal Wabbit is a machine learning system which pushes the frontier of machine learning with techniques such as online, hashing, allreduce, reductions, learning2search, active, and interactive learning.

> **Análisis IA:** Sistema ML orientado a escala con técnicas avanzadas: online learning, hashing, allreduce, reductions. Usado en producción para problemas donde el streaming y la eficiencia importan. Excelente para bandit problems y structured prediction.

**Fortalezas:** _Performance extremo en datasets masivos y streaming_ · _Soporte único para técnicas avanzadas (learning2search, active learning)_

**Tags:** `online-learning` `streaming` `c++` `ml-research` `vowpal-wabbit`

---

### [Wav2Letter++](https://github.com/facebookresearch/wav2letter)

![](https://img.shields.io/github/stars/facebookresearch/wav2letter?style=flat-square&label=⭐) · aparece en 2 listas

Public domain, a fast open source speech processing toolkit written entirely in C++ and uses the ArrayFire tensor library and the flashlight machine learning library for maximum efficiency. [BSD]

> **Análisis IA:** Toolkit speech processing optimizado, C++/Lua, Facebook Research. Excelente si procesás audio/speech, pero dominio muy específico.

**Fortalezas:** _Extremadamente optimizado para speech, dominante en research_ · _Integración con librería flashlight moderna_

**Tags:** `c++` `lua` `speech-processing` `audio` `facebook`

---

### [YOLOv8](https://github.com/ultralytics/ultralytics)

![](https://img.shields.io/github/stars/ultralytics/ultralytics?style=flat-square&label=⭐) · aparece en 2 listas

Ultralytics' YOLOv8 implementation with C++ support for real-time object detection and tracking, optimized for edge devices.

> **Análisis IA:** YOLOv8 de Ultralytics: detección de objetos en tiempo real, state-of-the-art en velocidad/accuracy. Estándar industrial hoy, C++ para edge. Soluciona real computer vision problem.

**Fortalezas:** _Accuracy/speed tradeoff superior a competencia, muy usado en industry_ · _Soporte robusto para deployment edge con C++_

**Tags:** `yolo` `object-detection` `python` `cpp` `edge-ai`

---


---

## 👍 Vale probar — sólidas en su nicho

Menos hype que las GEMs, pero confiables si caés en su caso de uso.

### [CatBoost](https://github.com/catboost/catboost)

![](https://img.shields.io/github/stars/catboost/catboost?style=flat-square&label=⭐) · aparece en 4 listas

General purpose gradient boosting on decision trees library with categorical features support out of the box. It is easy to install, contains fast inference implementation and supports CPU and GPU (even multi-GPU) computation.

> **Análisis IA:** CatBoost es la opción seria de Yandex para gradient boosting y resuelve un problema concreto que XGBoost y LightGBM manejan mal: variables categóricas. En vez de obligarte a hacer encoding manual (one-hot, target encoding con leakage), lo maneja internamente con ordered boosting. Ideal para devs de ML con datos tabulares sucios llenos de categorías. No es hype: benchmarks lo confirman competitivo. El trade-off es mayor costo computacional por defecto y curva de tuning no trivial.

**Fortalezas:** _Manejo nativo de variables categóricas sin preprocesamiento manual, reduciendo leakage y trabajo tedioso_ · _Inferencia rápida con soporte multi-GPU real, útil para producción con volumen alto_ · _API consistente con scikit-learn, lo que facilita integración en pipelines existentes_

**Tags:** `gradient-boosting` `machine-learning` `categorical-features` `gpu` `python`

---

### [Feature Engine](https://github.com/feature-engine/feature_engine)

![](https://img.shields.io/github/stars/feature-engine/feature_engine?style=flat-square&label=⭐) · aparece en 3 listas

- Feature-engine is a Python library that contains several transformers to engineer features for use in machine learning models.

> **Análisis IA:** Micro-batch stream processing con Spark: exactly-once semantics. Para pipelines que necesiten garantías fuertes en datos en movimiento. Resuelve: pérdida de datos ~0.

**Fortalezas:** _Garantías exactly-once nativas_ · _Integración con Spark SQL/MLlib_

**Tags:** `spark` `streaming` `scala` `java` `distributed`

---

### [H2O-3](https://github.com/h2oai/h2o-3)

![](https://img.shields.io/github/stars/h2oai/h2o-3?style=flat-square&label=⭐) · aparece en 3 listas

- Fast scalable Machine Learning platform for smarter applications: Deep Learning, Gradient Boosting & XGBoost, Random Forest, Generalized Linear Modeling (Logistic Regression, Elastic Net), K-Means, PCA, Stacked Ensembles, Automatic Machine Learning (AutoML), etc..

> **Análisis IA:** Plataforma ML enterprise con AutoML, deep learning y modelos distribuidos. Para organizaciones que necesitan piped end-to-end sin armarse con 5 librerías. Overkill para hobby projects.

**Fortalezas:** _AutoML robusto que compite con modelos manuales_ · _Escalado horizontal nativo con HDFS/Spark_

**Tags:** `machine-learning` `automl` `java` `distributed` `h2o`

---

### [m2cgen](https://github.com/bayeswitnesses/m2cgen)

![](https://img.shields.io/github/stars/bayeswitnesses/m2cgen?style=flat-square&label=⭐) · aparece en 3 listas

A tool that allows the conversion of ML models into native code (Java, C, Python, Go, JavaScript, Visual Basic, C#, R, PowerShell, PHP, Dart) with zero dependencies.

> **Análisis IA:** Resuelve un problema real y concreto: deployar modelos de ML sin arrastrar todo el ecosistema de Python/scikit-learn a producción. ¿Necesitás inferencia en un microservicio Java, un sistema legacy en C# o una app mobile en Dart? m2cgen convierte tu modelo entrenado a código nativo puro, sin dependencias. Ideal para devs que trabajan en entornos con restricciones de infraestructura o que no quieren levantar un servidor de inferencia solo para un modelo de regresión. No sirve para deep learning complejo, pero para modelos clásicos es una joya discreta.

**Fortalezas:** _Elimina dependencias en runtime: el código generado es standalone, sin necesitar librerías de ML instaladas en producción_ · _Soporte amplio de lenguajes (11+) y modelos clásicos de scikit-learn, XGBoost y LightGBM, cubriendo los casos de uso más comunes_ · _Ideal para entornos restringidos como sistemas embebidos, aplicaciones legacy o servicios donde instalar Python es inviable_

**Tags:** `machine-learning` `code-generation` `model-deployment` `scikit-learn` `open-source`

---

### [Mem0](https://github.com/mem0ai/mem0)

![](https://img.shields.io/github/stars/mem0ai/mem0?style=flat-square&label=⭐) · aparece en 3 listas

- Mem0 enhances AI assistants and agents with an intelligent memory layer, enabling personalized AI interactions.

> **Análisis IA:** Capa de memoria para AI agents. Persiste contexo entre calls, mejora hallucinations. Mercado emergente, pero promete ser pieza clave en AI applications stateful.

**Fortalezas:** _API simple para integrar memoria en agentes_ · _Soporte de múltiples backends (vector DB, SQL)_

**Tags:** `ai-memory` `python` `agents` `llm`

---

### [Scikit-Image](https://github.com/scikit-image/scikit-image)

![](https://img.shields.io/github/stars/scikit-image/scikit-image?style=flat-square&label=⭐) · aparece en 3 listas

A collection of algorithms for image processing in Python.

> **Análisis IA:** Suite de algoritmos de procesamiento de imágenes en Python. Filtros, transformaciones, análisis. Complemento a OpenCV, más alto nivel. Resuelve tasks específicas de visión sin compilar C.

**Fortalezas:** _API Pythonica y bien documentada vs OpenCV C++_ · _Integración perfecta con scipy/numpy ecosystem_

**Tags:** `python` `image-processing` `computer-vision` `scipy`

---

### [agent-of-empires](https://github.com/njbrake/agent-of-empires)

![](https://img.shields.io/github/stars/njbrake/agent-of-empires?style=flat-square&label=⭐) · aparece en 2 listas

A TUI/CLI for managing multiple AI coding agent sessions with tmux, git worktrees, and Docker sandboxing [](https://github.com/njbrake/agent-of-empires/actions)

> **Análisis IA:** TUI para orquestar agentes de código con tmux+git. Resuelve pain point real pero target muy específico (dev teams con agentes AI). Promesa pero mercado chico.

**Fortalezas:** _Integración tmux+git worktrees es elegante_ · _Docker sandboxing nativo evita contaminación_

**Tags:** `cli` `tui` `ai-agents` `rust` `tmux`

---

### [Aim](https://github.com/aimhubio/aim)

![](https://img.shields.io/github/stars/aimhubio/aim?style=flat-square&label=⭐) · aparece en 2 listas

- A super-easy way to record, search and compare AI experiments.

> **Análisis IA:** Plataforma de tracking para experimentos ML. Registra, busca y compara runs. Resuelve problema real: organizar caos de hiperparámetros y métricas en desarrollo iterativo de modelos.

**Fortalezas:** _Interfaz intuitiva, UI limpia vs Weights&Biases_ · _Opción self-hosted, sin vendor lock-in_

**Tags:** `experiment-tracking` `mlops` `self-hosted` `dashboard`

---

### [askbudi/roundtable](https://github.com/askbudi/roundtable)

![](https://img.shields.io/github/stars/askbudi/roundtable?style=flat-square&label=⭐) · aparece en 2 listas

📇 ☁️ 🏠 🍎 🪟 🐧 - Meta-MCP server that unifies multiple AI coding assistants (Codex, Claude Code, Cursor, Gemini) through intelligent auto-discovery and standardized MCP interface, providing zero-configuration access to the entire AI coding ecosystem.

> **Análisis IA:** Meta-servidor MCP que unifica múltiples asistentes AI (Claude, Cursor, Gemini) con auto-discovery. Para devs que cambian entre tools y quieren interfaz única.

**Fortalezas:** _Auto-discovery de assistentes sin config_ · _Abstracción elegante sobre MCP fragmentado_

**Tags:** `mcp` `ai-assistants` `claude` `cursor` `gemini`

---

### [Awesome RAG Production](https://github.com/yigtwxx/awesome-rag-production)

![](https://img.shields.io/github/stars/yigtwxx/awesome-rag-production?style=flat-square&label=⭐) · aparece en 2 listas

A curated collection of battle-tested tools, frameworks, and best practices for building, scaling, and monitoring production-grade Retrieval-Augmented Generation (RAG) systems. Covers frameworks, vector databases, retrieval & reranking, evaluation, observability, deployment, and security.

> **Análisis IA:** Curación de herramientas y patterns para RAG en producción. Cubre desde vectorDB hasta observabilidad. Referencia útil para arquitecturas, no código ejecutable.

**Fortalezas:** _Mapeo exhaustivo del ecosistema RAG moderno_ · _Enfoque en aspectos de producción (monitoring, deployment, security)_

**Tags:** `rag` `llm` `production` `curated-list`

---

### [BentoML](https://github.com/bentoml/bentoml)

![](https://img.shields.io/github/stars/bentoml/bentoml?style=flat-square&label=⭐) · aparece en 2 listas

- BentoML is an open source framework for high performance ML model serving.

> **Análisis IA:** Framework para servir ML models en production. Maneja containerización, versioning, scaling. Para equipos que necesitan MLOps sin Kubernetes expertise. Resuelve gap modelo-a-servicio.

**Fortalezas:** _Integra con PyTorch/TF/sklearn sin cambios code_ · _Deployment a cloud (AWS/GCP/Azure) semi-automático_

**Tags:** `python` `mlops` `model-serving` `containerization`

---

### [Bread WandB Viewer](https://github.com/bread-technologies/bread_wandb_viewer_extension)

![](https://img.shields.io/github/stars/bread-technologies/bread_wandb_viewer_extension?style=flat-square&label=⭐) · aparece en 2 listas

A VS Code extension to view Weights & Biases experiments, logs, and artifacts within the IDE, eliminating the need to switch to the web UI & preserving data privacy by being 100% offline.

> **Análisis IA:** Extensión VS Code que replica W&B web UI offline. Bueno para devs que quieren no saltar del editor. Privacy win (100% offline). Pero: duplica UI, mantiene sincronización compleja.

**Fortalezas:** _Privacy/offline first_ · _Reduce context switching en iteración_

**Tags:** `vscode-extension` `weights-and-biases` `ml-monitoring`

---

### [burn](https://github.com/tracel-ai/burn)

![](https://img.shields.io/github/stars/tracel-ai/burn?style=flat-square&label=⭐) · aparece en 2 listas

Burn is a new comprehensive dynamic Deep Learning Framework built using Rust with extreme flexibility, compute efficiency and portability as its primary goals

> **Análisis IA:** Framework ML nativo Rust, dinámico, con GPU support. Burn apunta a portabilidad y eficiencia vs PyTorch. Joven pero promisorio para producción Rust puro.

**Fortalezas:** _No depende de Python/PyTorch, control total desde Rust_ · _Backend abstraction permite GPU/CPU/WebGPU transparente_

**Tags:** `rust` `deep-learning` `gpu` `dynamic-computation`

---

### [candle](https://github.com/huggingface/candle)

![](https://img.shields.io/github/stars/huggingface/candle?style=flat-square&label=⭐) · aparece en 2 listas

Candle is a minimalist ML framework for Rust with a focus on performance (including GPU support) and ease of use.

> **Análisis IA:** Framework ML minimalista HF en Rust. GPU support, diseño limpio, alternativa a Burn pero más joven. Bueno para experimentación rápida y modelos custom sin boilerplate.

**Fortalezas:** _API simple, sintaxis clara, menos boilerplate que otros frameworks_ · _Soporte GPU maduro (CUDA/Metal), performance competitivo_

**Tags:** `rust` `deep-learning` `gpu` `minimalist`

---

### [Catalyst](https://github.com/catalyst-team/catalyst)

![](https://img.shields.io/github/stars/catalyst-team/catalyst?style=flat-square&label=⭐) · aparece en 2 listas

High-level utils for PyTorch DL & RL research. It was developed with a focus on reproducibility, fast experimentation and code/ideas reusing. Being able to research/develop something new, rather than write another regular train loop.

> **Análisis IA:** Framework high-level para PyTorch que abstrae training loops repetitivos. Bueno para reproducibilidad y reutilización de código en investigación, pero menos adoptado que Hugging Face.

**Fortalezas:** _Callbacks y logging robustos para experimentos_ · _Soporte out-of-box para RL y DL research_

**Tags:** `pytorch` `training-framework` `python` `reproducibility`

---

### [CCV](https://github.com/liuliu/ccv)

![](https://img.shields.io/github/stars/liuliu/ccv?style=flat-square&label=⭐) · aparece en 2 listas

C-based/Cached/Core Computer Vision Library, A Modern Computer Vision Library. [BSD]

> **Análisis IA:** Librería C de computer vision (BSD). Ligera, moderna, alternativa a OpenCV. Buena para embedidos/performance crítico.

**Fortalezas:** _footprint pequeño_ · _performance optimizado_

**Tags:** `c` `computer-vision` `library` `bsd` `performance`

---

### [Chroma](https://github.com/chroma-core/chroma)

![](https://img.shields.io/github/stars/chroma-core/chroma?style=flat-square&label=⭐) · aparece en 2 listas

- Chroma is an open-source embedding database.

> **Análisis IA:** Base de datos vectorial open-source para embeddings. Esencial para RAG, búsqueda semántica y apps con LLMs. Resuelve el problema real de persistir y queryar vectores a escala.

**Fortalezas:** _Integración nativa con LangChain y frameworks de IA_ · _API simple y bien documentada para CRUD vectorial_

**Tags:** `vector-db` `embeddings` `rag` `python` `open-source`

---

### [ClearML](https://github.com/clearml/clearml)

![](https://img.shields.io/github/stars/clearml/clearml?style=flat-square&label=⭐) · aparece en 2 listas

Auto-Magical CI/CD to streamline your AI workload. Experiment Management, Data Management, Pipeline, Orchestration, Scheduling & Serving in one MLOps/LLMOps solution.

> **Análisis IA:** Plataforma all-in-one para MLOps: experiment tracking, data mgmt, pipelines, orquestación, serving. Para teams que quieren single source of truth. Resuelve fragmentación de herramientas.

**Fortalezas:** _Cobertura end-to-end impresionante (raro en una tool)_ · _UI intuitiva, setup rápido sin Kubernetes requerido_

**Tags:** `python` `mlops` `orchestration` `experiment-tracking` `pipelines`

---

### [CloudForest](https://github.com/ryanbressler/cloudforest)

![](https://img.shields.io/github/stars/ryanbressler/cloudforest?style=flat-square&label=⭐) · aparece en 2 listas

Fast, flexible, multi-threaded ensembles of decision trees for machine learning in pure Go.

> **Análisis IA:** Ensembles de árboles de decisión en Go puro. Fast, multi-threaded, bueno para ML clásico. Niche pero sólido para quien use Go y ML.

**Fortalezas:** _Performance nativo en Go_ · _Implementación limpia sin dependencias externas_

**Tags:** `go` `machine-learning` `decision-trees` `performance`

---

### [Context Engineering Kit](https://github.com/neolabhq/context-engineering-kit)

![](https://img.shields.io/github/stars/neolabhq/context-engineering-kit?style=flat-square&label=⭐) · aparece en 2 listas

by [Vlad Goncharov](https://github.com/LeoVS09) - Hand-crafted collection of advanced context engineering techniques and patterns with minimal token footprint focused on improving agent result quality.

> **Análisis IA:** Técnicas avanzadas de context engineering para agentes IA con bajo token footprint. Para users de Claude que optimizan prompts en producción.

**Fortalezas:** _Enfoque explícito en eficiencia de tokens_ · _Patterns de ingeniería contexto hand-crafted_

**Tags:** `prompt-engineering` `token-optimization` `context` `agents`

---

### [CoreNLP](https://nlp.stanford.edu/software/corenlp.shtml)

aparece en 2 listas

Stanford CoreNLP provides a set of natural language analysis tools which can take raw English language text input and give the base forms of words.

> **Análisis IA:** Suite NLP de Stanford con herramientas clásicas: tokenization, PoS tagging, parsing, NER. Estándar en investigación y educación. Pierde tracción vs transformers, pero aún útil para pipelines simples.

**Fortalezas:** _Referencia académica impecable, APIs limpias_ · _Performance sólido para tareas clásicas_

**Tags:** `nlp` `java` `stanford` `pos-tagging` `ner`

---

### [CuML](https://github.com/rapidsai/cuml)

![](https://img.shields.io/github/stars/rapidsai/cuml?style=flat-square&label=⭐) · aparece en 2 listas

- cuML is a suite of libraries that implement machine learning algorithms and mathematical primitives functions that share compatible APIs with other RAPIDS projects.

> **Análisis IA:** cuML implementa ML clásico y deep learning con GPU vía CUDA. APIs compatibles con scikit-learn. Aceleración real en datasets grandes, pero ecosistema RAPIDS requiere GPU NVIDIA.

**Fortalezas:** _Aceleración GPU drop-in para algoritmos standard_ · _APIs familiares tipo scikit-learn_

**Tags:** `gpu` `cuda` `machine-learning` `python` `rapids`

---

### [Cursor](https://cursor.com)

aparece en 2 listas

An IDE with chat, edit, generate and debug features. Forked from VSCodium, so the interface is similar to VS Code. Uses OpenAI.

> **Análisis IA:** IDE AI-native fork de VSCodium con chat y generación de código integrada. Compite con GitHub Copilot pero requiere OpenAI key. UI familiar VS Code, pero modelo depende de tu quota.

**Fortalezas:** _Chat nativo + edición en contexto fluida_ · _Generación de código rápida, heredita estabilidad VSCode_

**Tags:** `ai-ide` `vscode-fork` `chat` `code-generation` `proprietary`

---

### [dagger/container-use](https://github.com/dagger/container-use)

![](https://img.shields.io/github/stars/dagger/container-use?style=flat-square&label=⭐) · aparece en 2 listas

🏎️ 🏠 🐧 🍎 🪟 - Containerized environments for coding agents. Multiple agents can work independently, isolated in fresh containers and git branches. No conflicts, many experiments. Full execution history, terminal access to agent environments, git workflow. Any agent/model/infra stack.

> **Análisis IA:** Dagger feature: entornos containerizados para coding agents multi-agente aislados con git workflow. Resuelve conflicto real entre agentes paralelos. Buena ejecución pero early-stage.

**Fortalezas:** _Aislamiento real sin conflictos between agents_ · _Historial de ejecución + acceso terminal_

**Tags:** `containers` `agents` `ci-cd` `dagger` `orchestration`

---

### [DEAP](https://github.com/deap/deap)

![](https://img.shields.io/github/stars/deap/deap?style=flat-square&label=⭐) · aparece en 2 listas

- A novel evolutionary computation framework for rapid prototyping and testing of ideas. It seeks to make algorithms explicit and data structures transparent. It works in perfect harmony with parallelisation mechanisms such as multiprocessing and SCOOP.

> **Análisis IA:** Framework de computación evolutiva con énfasis en transparencia de estructuras. Sólido para investigación en algoritmos genéticos, multiobjetivo y sistemas complejos. Nicho académico.

**Fortalezas:** _Diseño limpio, estructuras de datos transparentes_ · _Integración nativa con multiprocessing y SCOOP_

**Tags:** `evolutionary-computation` `python` `genetic-algorithms` `parallelizable`

---

### [DeepDetect](https://github.com/jolibrain/deepdetect)

![](https://img.shields.io/github/stars/jolibrain/deepdetect?style=flat-square&label=⭐) · aparece en 2 listas

- Machine Learning production server for TensorFlow, XGBoost and Cafe models written in C++ and maintained by Jolibrain.

> **Análisis IA:** Servidor ML production-ready para TensorFlow/XGBoost/Caffe en C++. Para deployments enterprise que necesitan model serving robusto y bajo latency.

**Fortalezas:** _Multi-framework support (TF, XGBoost, Caffe)_ · _Performance optimizado, C++ puro_

**Tags:** `cpp` `ml-serving` `tensorflow` `xgboost` `production`

---

### [Determined](https://github.com/determined-ai/determined)

![](https://img.shields.io/github/stars/determined-ai/determined?style=flat-square&label=⭐) · aparece en 2 listas

- Deep learning training platform with integrated support for distributed training, hyperparameter tuning, and model management (supports Tensorflow and Pytorch).

> **Análisis IA:** Plataforma enterprise para training DL: distributed training, HPO, model registry. Completa pero overkill para investigadores. Competencia: Weights & Biases, MLflow, kubeflow.

**Fortalezas:** _Integración nativa TensorFlow+PyTorch con HPO sin boilerplate_ · _Model registry y experiment tracking built-in_

**Tags:** `mlops` `distributed-training` `hyperparameter-tuning` `python`

---

### [dspy](https://github.com/stanfordnlp/dspy)

![](https://img.shields.io/github/stars/stanfordnlp/dspy?style=flat-square&label=⭐) · aparece en 2 listas

- A framework for programming with foundation models.

> **Análisis IA:** Framework para programar LLM pipelines con type hints. Abstracción elegante vs prompts ad-hoc pero curva de adopción y maduro relativo.

**Fortalezas:** _Composabilidad de componentes tipo módulos reutilizables_ · _Buena integración con herramientas de evals_

**Tags:** `llm-framework` `prompt-engineering` `python` `stanford`

---

### [Flashlight](https://github.com/flashlight/flashlight)

![](https://img.shields.io/github/stars/flashlight/flashlight?style=flat-square&label=⭐) · aparece en 2 listas

- A fast, flexible machine learning library written entirely in C++ from the Facebook AI Research and the creators of Torch, TensorFlow, Eigen and Deep Speech.

> **Análisis IA:** ML library C++ de FAIR/Meta. Fast y flexible, pero territorio de investigadores. Menos tracción que PyTorch en industria.

**Fortalezas:** _Performance nativa C++, sin overhead Python_ · _Diseño flexible para experimentos research_

**Tags:** `machine-learning` `cpp` `facebook-ai` `research`

---

### [GoLearn](https://github.com/sjwhitworth/golearn)

![](https://img.shields.io/github/stars/sjwhitworth/golearn?style=flat-square&label=⭐) · aparece en 2 listas

General Machine Learning library for Go.

> **Análisis IA:** Librería ML general para Go con soporte para clasificación, regresión, clustering. Maintained pero nicho. Go no domina ML como Python; herramienta honesta pero comunidad pequeña.

**Fortalezas:** _Diseño modular, soporte varios algoritmos, documentación presente_ · _Performance nativa de Go para inference_

**Tags:** `machine-learning` `go` `classification-regression`

---

### [gorgonia](https://github.com/gorgonia/gorgonia)

![](https://img.shields.io/github/stars/gorgonia/gorgonia?style=flat-square&label=⭐) · aparece en 2 listas

graph-based computational library like Theano for Go that provides primitives for building various machine learning and neural network algorithms.

> **Análisis IA:** Graph-based ML library para Go estilo Theano, primitivas para redes neuronales y algoritmos ML. Niche: si querés deep learning nativo en Go sin cgo pesado.

**Fortalezas:** _Computación en grafos flexible, soporte para autodiff_ · _Sin dependencias C++ pesadas, integración limpia con Go_

**Tags:** `go` `neural-networks` `graph-based` `autodiff`

---

### [gorse](https://github.com/zhenghaoz/gorse)

![](https://img.shields.io/github/stars/zhenghaoz/gorse?style=flat-square&label=⭐) · aparece en 2 listas

An offline recommender system backend based on collaborative filtering written in Go.

> **Análisis IA:** Sistema recomendador offline en Go con collaborative filtering. Nicho específico de ML. Bueno si necesitás recomendaciones sin cloud, pero comunidad pequeña.

**Fortalezas:** _Pure Go, sin Python overhead_ · _Designed para offline batch processing_

**Tags:** `go` `recommender-system` `collaborative-filtering` `ml`

---

### [Haystack](https://github.com/deepset-ai/haystack)

![](https://img.shields.io/github/stars/deepset-ai/haystack?style=flat-square&label=⭐) · aparece en 2 listas

- Haystack is an open source NLP framework to interact with your data using Transformer models and LLMs (GPT-3 and alike). Haystack offers production-ready tools to quickly build ChatGPT-like question answering, semantic search, text generation, and more.

> **Análisis IA:** Framework NLP para QA, búsqueda semántica y generación con Transformers/LLMs. Para equipos armando pipelines RAG production-ready. Documentación sólida pero con overhead vs soluciones especializadas.

**Fortalezas:** _Abstracciones maduras para RAG (retriever-reader)_ · _Integración nativa con Hugging Face y LLMs populares_

**Tags:** `nlp` `llm` `rag` `transformers` `python`

---

### [Hopsworks](https://github.com/logicalclocks/hopsworks)

![](https://img.shields.io/github/stars/logicalclocks/hopsworks?style=flat-square&label=⭐) · aparece en 2 listas

A data-intensive platform for AI with the industry's first open-source feature store. The Hopsworks Feature Store provides both a feature warehouse for training and batch based on Apache Hive and a feature serving database, based on MySQL Cluster, for online applications.

> **Análisis IA:** Plataforma completa para ML ops con feature store open-source. Combina warehouse (Hive) para training y base de datos (MySQL Cluster) para serving online. Resuelve el problema real de gestionar features en producción.

**Fortalezas:** _Feature store dual (batch + online) en un solo producto_ · _Integración nativa con ecosistema Hadoop/Hive_

**Tags:** `feature-store` `ml-ops` `apache-hive` `mysql-cluster` `python`

---

### [Ignite](https://github.com/pytorch/ignite)

![](https://img.shields.io/github/stars/pytorch/ignite?style=flat-square&label=⭐) · aparece en 2 listas

- Ignite is a high-level library to help with training and evaluating neural networks in PyTorch flexibly and transparently.

> **Análisis IA:** PyTorch Ignite es wrapper de alto nivel para training loops. Reduce boilerplate, soporta distributed training y checkpointing. Útil si usás PyTorch y querés abstraer detalles.

**Fortalezas:** _Simplifica distributed training sin sacrificar control_ · _Bien integrada con PyTorch ecosystem_

**Tags:** `pytorch` `deep-learning` `training-loops` `python`

---

### [Infer.NET](https://dotnet.github.io/infer)

aparece en 2 listas

Infer.NET is a framework for running Bayesian inference in graphical models. One can use Infer.NET to solve many different kinds of machine learning problems, from standard problems like classification, recommendation or clustering through customized solutions to domain-specific problems. Infer.NET has been used in a wide variety of domains including information retrieval, bioinformatics,…

> **Análisis IA:** Framework .NET para Bayesian inference en graphical models. Robusto para problemas probabilísticos. Nicho solido pero limitado a ecosistema .NET.

**Fortalezas:** _Framework Bayesian especializado con APIs claras_ · _Usado en production en virology, information retrieval_

**Tags:** `dotnet` `bayesian-inference` `probabilistic` `graphical-models`

---

### [Infinity](https://github.com/infiniflow/infinity)

![](https://img.shields.io/github/stars/infiniflow/infinity?style=flat-square&label=⭐) · aparece en 2 listas

The AI-native database built for LLM applications, providing incredibly fast vector and full-text search. Developed using C++20

> **Análisis IA:** Base de datos vectorial nativa para IA, optimizada en C++20 para búsqueda rápida de vectores y full-text. Apunta a reemplazar Pinecone/Weaviate en casos de self-hosted. Resuelve latencia en retrieval para RAG.

**Fortalezas:** _Velocidad en C++20 vs Python puro_ · _Full-text + vector search combinado_

**Tags:** `vector-db` `c++` `self-hosted` `llm` `search`

---

### [JAX](https://github.com/google/jax)

![](https://img.shields.io/github/stars/google/jax?style=flat-square&label=⭐) · aparece en 2 listas

JAX is Autograd and XLA, brought together for high-performance machine learning research.

> **Análisis IA:** Dlib es toolkit C++ compacto para ML y visión. Incluye SVM, clustering, detección facial. Bueno para deployment embebido, pero inferior en redes deep vs TensorFlow/PyTorch.

**Fortalezas:** _Single header/binario, cero dependencies_ · _Algoritmos clásicos optimizados, excelente para producción embebida_

**Tags:** `cpp` `machine-learning` `computer-vision` `lightweight` `embedded`

---

### [Jieba-PHP](https://github.com/fukuball/jieba-php)

![](https://img.shields.io/github/stars/fukuball/jieba-php?style=flat-square&label=⭐) · aparece en 2 listas

A PHP port of Python's jieba. Chinese text segmentation for natural language processing.

> **Análisis IA:** Port de Jieba (segmentador chino) a PHP. Resuelve problema específico: segmentación de texto chino sin dependencias externas. Nicho muy acotado.

**Fortalezas:** _Única opción nativa PHP para segmentación chino_ · _Sin dependencias del sistema_

**Tags:** `php` `nlp` `chinese` `text-processing`

---

### [kagan-sh/kagan](https://github.com/kagan-sh/kagan)

![](https://img.shields.io/github/stars/kagan-sh/kagan?style=flat-square&label=⭐) · aparece en 2 listas

](https://glama.ai/mcp/servers/kagan-sh/kagan) 🐍 🏠 🍎 🪟 🐧 - AI-powered Kanban TUI and MCP server for autonomous development workflows. Orchestrates 14 coding agents across task tracking, isolated git worktrees, review, and merge.

> **Análisis IA:** Kanban TUI con MCP server que orquesta 14 agentes de IA para workflows autónomos. Maneja git worktrees, review y merge. Muy específico para dev automation.

**Fortalezas:** _Integración profunda con git worktrees y ciclo de review_ · _Orquestación de múltiples agentes simultáneamente_

**Tags:** `mcp` `tui` `kanban` `ai-agents` `python`

---

### [keras-tuner](https://github.com/keras-team/keras-tuner)

![](https://img.shields.io/github/stars/keras-team/keras-tuner?style=flat-square&label=⭐) · aparece en 2 listas

- Keras Tuner is an easy-to-use, distributable hyperparameter optimisation framework that solves the pain points of performing a hyperparameter search. Keras Tuner makes it easy to define a search space and leverage included algorithms to find the best hyperparameter values.

> **Análisis IA:** Tuner simplificado pensado para Keras/TensorFlow. Define search space declarativamente, ejecuta optimización. Resuelve problema: HP tuning accesible sin PhD en Bayesian stats.

**Fortalezas:** _API minimalista, aprende en 10 minutos_ · _Integración nativa con Keras, sin fricción_

**Tags:** `keras` `tensorflow` `hyperparameter-tuning` `beginner-friendly`

---

### [Kornia](https://github.com/kornia/kornia)

![](https://img.shields.io/github/stars/kornia/kornia?style=flat-square&label=⭐) · aparece en 2 listas

- Kornia is a differentiable computer vision library built on PyTorch that provides a rich set of differentiable image processing and geometric vision algorithms.

> **Análisis IA:** Librería de computer vision diferenciable sobre PyTorch. Implementa algoritmos clásicos (warping, homografia, flow) y modernos (kornia.enhance). Integración nativa con autograd.

**Fortalezas:** _Operaciones geométricas GPU-nativas_ · _Diferenciable end-to-end para vision+learning loops_

**Tags:** `computer-vision` `pytorch` `differentiable` `geometry`

---

### [LangChain](https://github.com/langchain-ai/langchain)

![](https://img.shields.io/github/stars/langchain-ai/langchain?style=flat-square&label=⭐) · aparece en 2 listas

- LangChain assists in building applications with LLMs through composability.

> **Análisis IA:** Framework de orquestación para LLMs. Compone chains y agents, abstraesiendo prompts y memoria. Estándar de facto para prototipos con GPT, pero genera lock-in y overhead.

**Fortalezas:** _Ecosistema gigante de integraciones (OpenAI, Anthropic, Hugging Face)_ · _Abstracción consistente para chains complejos y memory management_

**Tags:** `llm` `python` `framework` `agent-orchestration`

---

### [LightlyTrain](https://github.com/lightly-ai/lightly-train)

![](https://img.shields.io/github/stars/lightly-ai/lightly-train?style=flat-square&label=⭐) · aparece en 2 listas

- Pretrain computer vision models on unlabeled data for industrial applications.

> **Análisis IA:** Toolkit para preentrenamiento de modelos computer vision en datos sin etiquetar. Self-supervised learning para aplicaciones industriales, reduce labeling overhead.

**Fortalezas:** _Preentrenamiento sin labels reduce tiempo de etiquetado significativamente_ · _Optimizado para producción industrial, no research_

**Tags:** `computer-vision` `self-supervised` `pytorch` `python`

---

### [linfa](https://github.com/rust-ml/linfa)

![](https://img.shields.io/github/stars/rust-ml/linfa?style=flat-square&label=⭐) · aparece en 2 listas

a comprehensive toolkit to build Machine Learning applications with Rust

> **Análisis IA:** Ecosistema ML robusto para Rust: supervised/unsupervised, preprocessing, validación. Comunidad activa, diseño seguro. Alternativa seria a scikit-learn pero Rust tiene menor masa crítica en ML.

**Fortalezas:** _Type-safe, zero-cost abstractions_ · _API consistente, bien documentada_

**Tags:** `rust` `machine-learning` `supervised` `unsupervised`

---

### [LocalAI](https://github.com/mudler/localai)

![](https://img.shields.io/github/stars/mudler/localai?style=flat-square&label=⭐) · aparece en 2 listas

- LocalAI is a drop-in replacement REST API that's compatible with OpenAI API specifications for local inferencing.

> **Análisis IA:** Drop-in OpenAI API compatible para inference local. Rust+Go backend. Resuelve privacidad y costo, funciona bien para modelos medianos.

**Fortalezas:** _Compatible OpenAI, fácil switchear_ · _Support GPU y CPU, bajo overhead_

**Tags:** `ai` `llm` `self-hosted` `openai-compatible`

---

### [Ludwig](https://github.com/ludwig-ai/ludwig)

![](https://img.shields.io/github/stars/ludwig-ai/ludwig?style=flat-square&label=⭐) · aparece en 2 listas

- Ludwig is a low-code framework for building custom AI models like LLMs and other deep neural networks.

> **Análisis IA:** Ludwig abstrae configs YAML para entrenar LLMs y redes deep learning. Low-code, sin escribir training loops. Bueno para prototipado rápido, pero menos flexible que TensorFlow/PyTorch directo.

**Fortalezas:** _Configuración declarativa YAML, rápido de iterar_ · _Soporta transfer learning y fine-tuning LLMs_

**Tags:** `low-code` `llm` `deep-learning` `python` `no-code`

---

### [MCP Memory Service](https://github.com/doobidoo/mcp-memory-service)

![](https://img.shields.io/github/stars/doobidoo/mcp-memory-service?style=flat-square&label=⭐) · aparece en 2 listas

Universal memory service with semantic search, autonomous consolidation, and multi-client support for AI applications.

> **Análisis IA:** MCP service para memoria persistente con búsqueda semántica y consolidación autónoma. Nicho específico: agentes IA que necesitan contexto de sesiones previas. Idea sólida pero adoption desconocida.

**Fortalezas:** _Consolidación autónoma de memoria sin manual_ · _Multi-client, útil para orquestación de agentes_

**Tags:** `mcp` `memory` `semantic-search` `ai-agents` `server`

---

### [mljar-supervised](https://github.com/mljar/mljar-supervised)

![](https://img.shields.io/github/stars/mljar/mljar-supervised?style=flat-square&label=⭐) · aparece en 2 listas

- A Python package for AutoML on tabular data with feature engineering, hyper-parameters tuning, explanations and automatic documentation.

> **Análisis IA:** AutoML para datos tabulares con ingeniería de features, tuning y explicabilidad. Para data scientists que quieren baseline automático. Bueno para competencias pero overkill para producción simple.

**Fortalezas:** _Automatiza feature engineering ahorrando semanas_ · _Reportes HTML de explicabilidad incluidos_

**Tags:** `automl` `tabular-data` `python` `feature-engineering`

---

### [MLX](https://github.com/ml-explore/mlx)

![](https://img.shields.io/github/stars/ml-explore/mlx?style=flat-square&label=⭐) · aparece en 2 listas

- MLX is an array framework for machine learning on Apple silicon.

> **Análisis IA:** Framework de arrays optimizado para ML en Apple silicon. Alternativa a NumPy/PyTorch pensada para Macs. Resuelve problema real: ejecutar modelos eficiente en hardware Apple sin overhead de frameworks genéricos.

**Fortalezas:** _Optimizado nativamente para Metal en Macs, rendimiento superior vs PyTorch en ese hardware_ · _Bajo nivel de abstracción, contrario a los framework pesados_

**Tags:** `numpy-alternative` `apple-silicon` `machine-learning` `array-framework`

---

### [mlxtend](https://github.com/rasbt/mlxtend)

![](https://img.shields.io/github/stars/rasbt/mlxtend?style=flat-square&label=⭐) · aparece en 2 listas

A library consisting of useful tools for data science and machine learning tasks.

> **Análisis IA:** Toolkit Python para data science/ML con utilities variadas. Maduro, bien mantenido, usado en industria. Complementa scikit-learn bien, no es core pero es útil.

**Fortalezas:** _Colección robusta de algoritmos y evaluadores ML_ · _Documentación sólida, comunidad activa_

**Tags:** `python` `machine-learning` `data-science` `scikit-learn`

---

### [modAL](https://github.com/modal-python/modal)

![](https://img.shields.io/github/stars/modal-python/modal?style=flat-square&label=⭐) · aparece en 2 listas

A modular active learning framework for Python, built on top of scikit-learn.

> **Análisis IA:** Framework modular para active learning en Python sobre scikit-learn. Útil para proyectos de ML que necesitan reducir labeling manual. Resuelve un problema real pero de nicho específico.

**Fortalezas:** _Integración nativa con scikit-learn_ · _API clara para pipelines de active learning_

**Tags:** `python` `machine-learning` `active-learning` `scikit-learn`

---

### [Netron](https://netron.app)

aparece en 2 listas

Visualizer for neural network and machine learning models.

> **Análisis IA:** Visualizador web para inspeccionar arquitecturas de redes neuronales (ONNX, TF, PyTorch). Lee modelos, muestra grafo. Útil para debug y documentación, no para training.

**Fortalezas:** _UI limpia e intuitiva_ · _Soporta múltiples formatos (ONNX, SavedModel, etc)_

**Tags:** `visualization` `neural-network` `onnx` `model-inspection`

---

### [Nimbalyst](https://nimbalyst.com)

aparece en 2 listas

An agent management environment for Claude Code and Codex. Interactive visual editing of markdown, mockups, excalidraw, code. Parallel session management.

> **Análisis IA:** Entorno agentes IA (Claude Code). Edición visual markdown/mockups/código con sesiones paralelas. Producto beta, propuesta única pero info limitada sobre usabilidad real.

**Fortalezas:** _Sesiones paralelas para multi-agent workflows_ · _Integración mockups+código en mismo editor_

**Tags:** `ai-agents` `claude` `visual-editing` `markdown` `beta`

---

### [Opik](https://github.com/comet-ml/opik)

![](https://img.shields.io/github/stars/comet-ml/opik?style=flat-square&label=⭐) · aparece en 2 listas

- Opik is an open-source platform for evaluating, testing and monitoring LLM applications.

> **Análisis IA:** Plataforma open-source para evaluar, testear y monitorear aplicaciones LLM. Trazabilidad de prompts y outputs con métricas de evaluación integradas.

**Fortalezas:** _Dashboard unificado para debugging de LLM pipelines_ · _Evaluación automática de outputs con criterios personalizados_

**Tags:** `python` `llm-monitoring` `evaluation` `open-source`

---

### [Opik](https://comet.com/site/products/opik)

aparece en 2 listas

Open source engineering platform to debug, evaluate, and monitor your LLM applications, RAG systems, and agentic workflows with comprehensive tracing, automated evaluations, and production-ready dashboards.

> **Análisis IA:** Platform open-source para debugging y evaluación de LLM apps con tracing y evals. Competencia fuerte (Langsmith), pero madurez todavía alcanzando. Buena para early adopters.

**Fortalezas:** _Trazado granular de LLM chains_ · _Evals automatizadas para reproducibility_

**Tags:** `llm` `observability` `tracing` `evals` `agentic`

---

### [Oryx 2](https://github.com/oryxproject/oryx)

![](https://img.shields.io/github/stars/oryxproject/oryx?style=flat-square&label=⭐) · aparece en 2 listas

Framework for building real-time, large-scale machine learning applications. Includes end-to-end applications for collaborative filtering, classification, regression, and clustering.

> **Análisis IA:** Framework Java para ML en tiempo real a escala (collab filtering, classification, regression, clustering). Construido sobre Spark, Apache Kafka. Excelente para pipelines de producción con datos streaming.

**Fortalezas:** _Integración nativa Spark + Kafka para pipelines reales_ · _Aplicaciones end-to-end listos para ajustar_

**Tags:** `java` `machine-learning` `realtime` `spark` `kafka`

---

### [pgmpy](https://github.com/pgmpy/pgmpy)

![](https://img.shields.io/github/stars/pgmpy/pgmpy?style=flat-square&label=⭐) · aparece en 2 listas

A Python library for probabilistic graphical models and Bayesian networks.

> **Análisis IA:** Librería Python para modelos gráficos probabilísticos y redes Bayesianas. Nicho bien definido: inferencia, estructura learning. Comunidad activa pero pequeña.

**Fortalezas:** _Única librería seria en Python para PGMs_ · _Documentación decente con ejemplos reales_

**Tags:** `probabilistic-graphical-models` `bayesian` `python` `inference`

---

### [PyCaret](https://github.com/pycaret/pycaret)

![](https://img.shields.io/github/stars/pycaret/pycaret?style=flat-square&label=⭐) · aparece en 2 listas

) - low-code library for training and deploying models (scikit-learn, XGBoost, LightGBM, spaCy)

> **Análisis IA:** Low-code ML library que envuelve scikit-learn, XGBoost, LightGBM. Acelera prototipado rápido de modelos. Para data scientists sin experiencia en tuning. Resuelve el problema de ciclos largos de experimentación.

**Fortalezas:** _Reduce drasticamente tiempo de baseline a production_ · _Soporte multi-algoritmo out-of-the-box con comparación automática_

**Tags:** `python` `ml` `low-code` `automl` `sklearn`

---

### [rust-bert](https://github.com/guillaume-be/rust-bert)

![](https://img.shields.io/github/stars/guillaume-be/rust-bert?style=flat-square&label=⭐) · aparece en 2 listas

Rust native ready-to-use NLP pipelines and transformer-based models (BERT, DistilBERT, GPT2,...)

> **Análisis IA:** Pipelines NLP listas para usar en Rust puro. BERT/GPT2/DistilBERT sin Python. Alternativa lightweight si necesitás inference Rust, pero entrenamiento está en Python.

**Fortalezas:** _Zero Python dependency, deploy simple en binarios Rust_ · _Soporta modelos HF populares, descarga automática_

**Tags:** `rust` `nlp` `transformers` `inference`

---

### [Scikit-Opt](https://github.com/guofei9987/scikit-opt)

![](https://img.shields.io/github/stars/guofei9987/scikit-opt?style=flat-square&label=⭐) · aparece en 2 listas

Swarm Intelligence in Python (Genetic Algorithm, Particle Swarm Optimization, Simulated Annealing, Ant Colony Algorithm, Immune Algorithm, Artificial Fish Swarm Algorithm in Python)

> **Análisis IA:** Implementa 6 algoritmos de IA colectiva (GA, PSO, recocido simulado, hormigas, etc.). Para problemas de optimización combinatorial. Código educativo pero código de producción mejor optimizado en C/Rust.

**Fortalezas:** _Cobertura amplia de algoritmos heurísticos_ · _API consistente entre implementaciones_

**Tags:** `optimization` `swarm-intelligence` `genetic-algorithm` `python`

---

### [SGLang](https://github.com/sgl-project/sglang)

![](https://img.shields.io/github/stars/sgl-project/sglang?style=flat-square&label=⭐) · aparece en 2 listas

- SGLang is a fast serving framework for large language models and vision language models.

> **Análisis IA:** Framework para serving LLMs con optimizaciones de latencia (batching, pipelining). Resuelve cuello de botella real en inference pero competencia fragmentada.

**Fortalezas:** _Throughput 3-10x mejor que vLLM en casos multi-GPU_ · _Soporte para vision models_

**Tags:** `llm-serving` `inference-optimization` `python` `cuda`

---

### [SHAPash](https://github.com/maif/shapash)

![](https://img.shields.io/github/stars/maif/shapash?style=flat-square&label=⭐) · aparece en 2 listas

- Shapash is a Python library that provides several types of visualization that display explicit labels that everyone can understand.

> **Análisis IA:** Wrapper sobre SHAP que genera visualizaciones interpretables de modelos ML. Para stakeholders no técnicos que necesitan explicar decisiones de ML de forma clara.

**Fortalezas:** _Visualizaciones muy legibles para ejecutivos y reguladores_ · _Integración cercana con SHAP, reutiliza cálculos_

**Tags:** `python` `explainability` `shap` `visualization`

---

### [SHOGUN](https://github.com/shogun-toolbox/shogun)

![](https://img.shields.io/github/stars/shogun-toolbox/shogun?style=flat-square&label=⭐) · aparece en 2 listas

The Shogun Machine Learning Toolbox. [GPLv3]

> **Análisis IA:** Toolbox ML clásico en C++. Soporte scikit-learn-like pero compilado. Proyecto activo pero nicho: solo si necesitás ML traditional en C++.

**Fortalezas:** _Soporte exhaustivo de algoritmos clásicos ML_ · _Performance nativa C++, productizable_

**Tags:** `machine-learning` `cpp` `scikit-learn-alternative`

---

### [skill-seekers/Skill_Seekers](https://github.com/yusufkaraaslan/skill_seekers)

![](https://img.shields.io/github/stars/yusufkaraaslan/skill_seekers?style=flat-square&label=⭐) · aparece en 2 listas

](https://glama.ai/mcp/servers/yusufkaraaslan/Skill_Seekers) 🐍 🏠 🍎 🪟 🐧 - Transform 17 source types (docs, GitHub repos, PDFs, videos, Jupyter, Confluence, Notion, Slack/Discord) into AI-ready skills and RAG knowledge. 35 MCP tools for scraping, packaging, enhancing, and exporting to vector databases (Weaviate, Chroma, FAISS, Qdrant). Supports 16+ target platforms.

> **Análisis IA:** MCP server: ingesta desde 17 fuentes (GitHub, PDF, Notion, etc.) → skills + RAG. 35 herramientas MCP incluidas. Soluciona pipeline real pero dependencia de MCP adoption y complejidad de setup.

**Fortalezas:** _17 fuentes soportadas en una herramienta_ · _Exporta a 5+ vector DBs (Weaviate, Chroma, FAISS, Qdrant)_

**Tags:** `mcp` `rag` `knowledge-extraction` `multi-source` `python`

---

### [skorch](https://github.com/skorch-dev/skorch)

![](https://img.shields.io/github/stars/skorch-dev/skorch?style=flat-square&label=⭐) · aparece en 2 listas

A scikit-learn compatible neural network library that wraps PyTorch.

> **Análisis IA:** Wrapper scikit-learn sobre PyTorch, combina usabilidad sklearn con poder torch. Excelente para transición PyTorch + sklearn workflows.

**Fortalezas:** _Compatibilidad directa con sklearn pipelines/validación cruzada_ · _Reduce boilerplate PyTorch manteniendo flexibilidad_

**Tags:** `python` `pytorch` `scikit-learn` `wrapper`

---

### [spaGO](https://github.com/nlpodyssey/spago)

![](https://img.shields.io/github/stars/nlpodyssey/spago?style=flat-square&label=⭐) · aparece en 2 listas

Self-contained Machine Learning and Natural Language Processing library in Go.

> **Análisis IA:** Librería ML/NLP en Go puro, sin dependencias externas. Útil para pipelines en Go que necesiten procesamiento de texto, pero menor ecosistema que Python/PyTorch.

**Fortalezas:** _Zero dependencies, embebible en aplicaciones Go_ · _Performance competitivo en tareas NLP clásicas_

**Tags:** `nlp` `go` `machine-learning` `self-contained`

---

### [spfunctions/simplefunctions-cli](https://github.com/spfunctions/simplefunctions-cli)

![](https://img.shields.io/github/stars/spfunctions/simplefunctions-cli?style=flat-square&label=⭐) · aparece en 2 listas

](https://glama.ai/mcp/servers/spfunctions/simplefunctions-cli) 📇 ☁️ - Calibrated world model for AI agents from 9,700+ prediction markets. 16 MCP tools covering real-time world state, market search, thesis management, edge detection, and content enrichment across Kalshi and Polymarket. `get_world_state` returns ~800 tokens of calibrated probabilities — no API key needed.

> **Análisis IA:** MCP server que expone 16 herramientas sobre mercados de predicción (Kalshi, Polymarket). Devuelve ~800 tokens de probabilidades calibradas sin API key. Para agentes que necesitan world state en tiempo real.

**Fortalezas:** _Datos de 9700+ mercados, sin autenticación requerida_ · _Output estructurado y calibrado para LLMs_

**Tags:** `mcp` `prediction-markets` `forecasting` `api`

---

### [Superpowers](https://github.com/obra/superpowers)

![](https://img.shields.io/github/stars/obra/superpowers?style=flat-square&label=⭐) · aparece en 2 listas

by [Jesse Vincent](https://github.com/obra) - A strong bundle of core competencies for software engineering, with good coverage of a large portion of the SDLC - from planning, reviewing, testing, debugging... Well written, well organized, and adaptable. The author refers to them as "superpowers", but many of them are just consolidating engineering best practices - which sometimes does feel…

> **Análisis IA:** Bundle de prácticas de ingeniería software (planning, review, testing, debug) como prompts/técnicas. Para devs con Claude Code que busquen estructura en el ciclo de vida.

**Fortalezas:** _Cobertura amplia del ciclo de vida completo_ · _Bien organizado y adaptable a contextos específicos_

**Tags:** `prompt-engineering` `sdlc` `best-practices` `claude`

---

### [TabGAN](https://github.com/diyago/tabular-data-generation)

![](https://img.shields.io/github/stars/diyago/tabular-data-generation?style=flat-square&label=⭐) · aparece en 2 listas

- Synthetic tabular data generation using GANs (CTGAN), Diffusion Models, and LLMs with adversarial filtering, privacy metrics, and sklearn integration.

> **Análisis IA:** Generación de datos tabulares sintéticos vía CTGAN, Diffusion y LLMs con filtering adversarial. Resuelve problema real (datos sensibles, balanceo). Integración sklearn clara.

**Fortalezas:** _Múltiples backends (GAN, diffusion, LLM)_ · _Métricas de privacidad y sklearn-compatible_

**Tags:** `synthetic-data` `gan` `tabular` `privacy` `python`

---

### [tch-rs](https://github.com/laurentmazare/tch-rs)

![](https://img.shields.io/github/stars/laurentmazare/tch-rs?style=flat-square&label=⭐) · aparece en 2 listas

Rust bindings for the C++ API of PyTorch

> **Análisis IA:** Bindings Rust para PyTorch C++. Opción válida si necesitás Rust + PyTorch sin overhead Python, pero tch-rs tiene mantenimiento esporádico vs Candle.

**Fortalezas:** _Acceso directo a PyTorch performance desde Rust_ · _Sintaxis cercana a PyTorch, curva aprendizaje menor_

**Tags:** `rust` `pytorch` `bindings` `deep-learning`

---

### [TensorZero](https://github.com/tensorzero/tensorzero)

![](https://img.shields.io/github/stars/tensorzero/tensorzero?style=flat-square&label=⭐) · aparece en 2 listas

data & learning flywheel for LLMs that unifies inference, observability, optimization, and experimentation

> **Análisis IA:** Framework para cerrar el loop de inferencia LLM con observabilidad y optimización. Resuelve problema real (costo + latencia de LLMs) pero ecosystem inmaduro.

**Fortalezas:** _Unifica inference, evals y feedback en una interfaz_ · _Buena integración con providers (OpenAI, Anthropic)_

**Tags:** `llm` `inference` `observability` `python`

---

### [TPOT](https://github.com/epistasislab/tpot)

![](https://img.shields.io/github/stars/epistasislab/tpot?style=flat-square&label=⭐) · aparece en 2 listas

Tool that automatically creates and optimizes machine learning pipelines using genetic programming. Consider it your personal data science assistant, automating a tedious part of machine learning.

> **Análisis IA:** AutoML con programación genética que arma pipelines automáticamente. Útil para exploración rápida pero tiende a generar modelos complejos sin garantía de generalización.

**Fortalezas:** _Automatiza feature engineering y selección de algoritmos_ · _Generación explícita de código Python ejecutable_

**Tags:** `automl` `genetic-programming` `python` `pipeline-optimization`

---

### [unsloth](https://github.com/unslothai/unsloth)

![](https://img.shields.io/github/stars/unslothai/unsloth?style=flat-square&label=⭐) · aparece en 2 listas

- Fine-tuning & Reinforcement Learning for LLMs. Train OpenAI gpt-oss, DeepSeek-R1, Qwen3, Gemma 3, TTS 2x faster with 70% less VRAM.

> **Análisis IA:** Fine-tuning de LLMs optimizado para memory/speed. Promete 2x speedup y 70% menos VRAM. Útil para quien quiera entrenar modelos abiertos localmente. Hype moderado pero claims verificables.

**Fortalezas:** _Realmente reduce VRAM 60-70% con optimizaciones de kernel personalizadas_ · _Activamente mantenido, comunidad creciente en Hugging Face_

**Tags:** `llm` `fine-tuning` `qlora` `python` `pytorch`

---

### [USearch](https://github.com/unum-cloud/usearch)

![](https://img.shields.io/github/stars/unum-cloud/usearch?style=flat-square&label=⭐) · aparece en 2 listas

Similarity Search Engine for Vectors and Strings [](https://crates.io/crates/usearch)

> **Análisis IA:** Engine de búsqueda de similaridad para vectores y strings. Rust + multi-lenguaje, compite con FAISS/Milvus pero más minimalista.

**Fortalezas:** _Soporte nativo para strings y vectores en mismo engine_ · _Bindings en múltiples lenguajes_

**Tags:** `vector-search` `similarity-search` `rust` `c++` `embedding`

---

### [Windsurf](https://windsurf.com)

aparece en 2 listas

An IDE with chat, edit, generate and debug features. Forked from VSCodium, so the interface is similar to VS Code. Formerly known as Codeium.

> **Análisis IA:** IDE basado en VSCode con AI chat integrado. Alternativa a Cursor con interfaz familiar. Early stage: funciona pero aún está puliendo features y estabilidad.

**Fortalezas:** _Interfaz VSCode hace rampa de entrada baja para usuarios existentes_ · _AI chat decente para sugerencias inline_

**Tags:** `ide` `ai-coding` `electron` `vscode-fork`

---

### [xLearn](https://github.com/aksnzhy/xlearn)

![](https://img.shields.io/github/stars/aksnzhy/xlearn?style=flat-square&label=⭐) · aparece en 2 listas

A high performance, easy-to-use, and scalable machine learning package, which can be used to solve large-scale machine learning problems. xLearn is especially useful for solving machine learning problems on large-scale sparse data, which is very common in Internet services such as online advertising and recommender systems.

> **Análisis IA:** Librería ML especializada en datos sparse a escala. Resuelve problemas reales de ads y recomendación. C++ puro, rendimiento comprobado. Nicho específico pero establecido.

**Fortalezas:** _Excelente rendimiento en datasets sparse de alta dimensión_ · _API simple para problemas de clasificación y ranking a escala_

**Tags:** `machine-learning` `sparse-data` `c++` `scalable`

---

### [ZenML](https://github.com/zenml-io/zenml)

![](https://img.shields.io/github/stars/zenml-io/zenml?style=flat-square&label=⭐) · aparece en 2 listas

- ZenML is an extensible, open-source MLOps framework to create reproducible ML pipelines with a focus on automated metadata tracking, caching, and many integrations to other tools.

> **Análisis IA:** Framework MLOps open-source para pipelines reproducibles con metadata tracking automático y caching. Integra con múltiples backends. Apunta a ML en producción, no a research.

**Fortalezas:** _Metadata tracking y caching built-in reduce overhead_ · _Flexible: soporta múltiples orquestadores y backends_

**Tags:** `mlops` `ml-pipelines` `metadata-tracking` `python`

---


---

<sub>📄 Generado automáticamente desde [juanchi.dev](https://juanchi.dev) · [código del sistema](https://juanchi.dev/blog/series/awesome-curated) · MIT licensed</sub>
