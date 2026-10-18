# Cinco ejemplos pequeños que podés reproducir

Elegí un problema, ejecutá un caso mínimo y mirá el resultado antes de sumar otra dependencia al proyecto. Estos ejemplos cubren búsqueda estructural de código, validación de formularios, un archivo de modelo, consulta de vectores y métricas de experimentos.

Pruebas del 18 de octubre de 2026 con datos sintéticos, en contenedores Linux x86-64 descartables. Las comprobaciones se automatizaron con asistencia de IA. Los veredictos existentes del catálogo se conservan. La instalación requiere internet; las ejecuciones finales se hicieron con la red externa desconectada.

```sh
git clone --branch practical-examples-2026-10-18-r2 --depth 1 https://github.com/JuanTorchia/awesome-curated.git
cd awesome-curated/examples/practical
```

[Instalá las dependencias fijadas](examples/practical/README.md) antes de ejecutar los comandos de abajo. Ese archivo separa los entornos Node.js y Python. El paquete incluye [versiones y checksums](examples/practical/versions.json) y [resultados comprobados](examples/practical/expected.json). Se fijaron las versiones Python principales; sus dependencias transitivas no quedaron completamente bloqueadas.

## <a id="ast-grep"></a>Encontrar una llamada real con ast-grep

Una búsqueda textual también encuentra `console.log` dentro de comentarios y strings. El [caso de prueba](examples/practical/ast-grep.mjs) busca una expresión de llamada mediante el parser de JavaScript y reescribe sólo esa coincidencia.

```sh
npm ci
node ast-grep.mjs
```

Con ast-grep **0.51.0**, encuentra **una** llamada y produce `logger.info("hello")`. El comentario y el string quedan iguales. `logger` es un destino ilustrativo: se comprueba la transformación sintáctica, no que reemplazar el logger conserve el comportamiento de la aplicación.

Sirve cuando el patrón depende de la estructura del código. Una migración de todo el repositorio todavía necesita pruebas del comportamiento del reemplazo. [Documentación oficial](https://ast-grep.github.io/guide/quick-start.html).

## <a id="vest"></a>Ver qué campos fallan con Vest

El [caso de prueba](examples/practical/vest.mjs) aplica dos reglas de longitud a una entrada inválida y después a una válida.

```sh
node vest.mjs
```

Con Vest **6.3.4**, los campos inválidos son `["password", "username"]`; la ejecución válida devuelve `hasErrors: false`. El ejemplo usa `suite.run`, la API documentada para esta versión.

Es una prueba de la suite de validación, previa a conectar la UI del formulario. No recorre reglas asíncronas ni define una política de contraseñas de producción. La validación del servidor necesita su propia implementación. [Documentación de Vest](https://vestjs.dev/docs/get_started).

## <a id="netron"></a>Abrir un archivo de modelo con Netron

El [caso de prueba](examples/practical/netron-example.py) crea un ONNX con un nodo `Relu` y forma `[1, 3]`, inicia Netron en el puerto local 18080 y recupera la página y los bytes del modelo.

```sh
/tmp/awesome-chroma-env/bin/python netron-example.py
```

Netron **9.3.2** y ONNX **1.23.2** sirvieron el modelo de **104 bytes** con HTTP **200** y los mismos bytes. Su SHA-256 es `b8f44a12ed8dff00d68bfb2fe6bee423dd7b100422c4ad6cf087b25af23a9c4e`.

Esto confirma que se puede servir ese archivo pequeño. No se comprobó el render del navegador ni se ejecutó inferencia; el nodo `Relu` se verifica en el ONNX generado, no mediante una aserción visual. El puerto 18080 debe estar libre. [Código y uso de Netron](https://github.com/lutzroeder/netron).

## <a id="chroma"></a>Consultar vectores sin descargar un modelo de embeddings

El [caso de prueba](examples/practical/chroma.py) inserta tres vectores one-hot explícitos y consulta con un vector igual al primero.

```sh
/tmp/awesome-chroma-env/bin/python chroma.py
```

Con Chroma **1.5.9**, la colección contiene **3** registros, devuelve `logs` como vecino más cercano y distancia **0.0**.

Los vectores explícitos permiten inspeccionar la carga y la consulta por separado de la generación de embeddings. Esta consulta de coincidencia exacta no mide calidad de búsqueda semántica, persistencia ni escala. Los datos son efímeros. [Documentación de consultas](https://docs.trychroma.com/docs/querying-collections/query-and-get).

## <a id="aim"></a>Recuperar métricas guardadas con Aim

El [caso de prueba](examples/practical/aim-example.py) registra valores sintéticos de loss, cierra la corrida, reabre el repositorio y comprueba la secuencia almacenada.

```sh
/tmp/awesome-aim-env/bin/python aim-example.py
```

Con Aim **3.29.1**, el resultado observado fue **1** corrida, pasos `[0, 1, 2]` y loss `[1.0, 0.5, 0.25]`. El seguimiento del sistema y la captura de terminal están desactivados. Los datos son temporales; no se entrena un modelo ni se comparan trackers. [Documentación de tracking](https://aimstack.readthedocs.io/en/latest/quick_start/setup.html).

## Cómo aprovechar los ejemplos

Elegí el caso que responda a una tarea que ya tenés. El [catálogo actual](TOOLS.md) conserva veredictos, límites y trazas; estos ejemplos fechados son un paquete de reproducción separado, no cinco recomendaciones nuevas. El [snapshot del 18 de octubre](https://github.com/JuanTorchia/awesome-curated/blob/4d851df75e1aeeb861b2046ce4784d5706e7d548/data/latest.json) registra la cobertura usada para la selección.

## Guardalo para después

¿Te sirvió alguno de los ejemplos? Guardá el [repo](https://github.com/JuanTorchia/awesome-curated) con una ⭐ para volver a las versiones, los resultados esperados y los límites de cada caso.

[English](GUIDE.md) · [Catálogo](TOOLS.md) · [Metodología](METHODOLOGY.md)
