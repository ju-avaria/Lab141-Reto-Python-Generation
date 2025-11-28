# 🔍 Ejercicios de investigación


## ☁️ Ejercicio de investigación de Fundamentos de AWS Cloud: primera parte

**1. 📀 Defina qué es IaaS, PaaS y SaaS**

    -IaaS corresponde a infraestructura computacional entregada como servicio, incluyendo redes, máquinas virtuales y almacenamiento.
    -PaaS corresponde a una plataforma completa para desarrollar, probar y desplegar aplicaciones sin gestionar la infraestructura.
    -SaaS corresponde a aplicaciones listas para usar desde la nube sin instalación local ni mantenimiento por parte del usuario.

**2. ☁️ Proporcione seis ventajas de la informática en la nube**

    -Elasticidad para ajustar recursos según demanda.
    -Pago por uso sin invertir en infraestructura física.
    -Disponibilidad global desde múltiples ubicaciones.
    -Seguridad administrada con buenas prácticas definidas.
    -Velocidad de implementación y despliegue ágil.
    -Reducción de costos operativos y mantenimiento.

**3. ✅ Defina qué es una región de AWS y una zona de disponibilidad**

    -Una región es una ubicación geográfica que contiene múltiples zonas de disponibilidad.
    -Una zona de disponibilidad es un centro de datos independiente dentro de una región, diseñado para alta disponibilidad.

**4. 🧑‍💻Enumere todas las regiones de AWS**

    -La lista completa incluye regiones en América, Europa, Asia Pacífico, Medio Oriente y África. Si es necesario puedo agregar el listado completo actualizado con nombres y códigos.

**5. 🛒 ¿Cuáles son las categorías en las que se agrupan los servicios de AWS?**

    -Servicios de cómputo
    -Servicios de almacenamiento
    -Servicios de redes
    -Servicios de bases de datos
    -Servicios de seguridad
    -Servicios de análisis
    -Servicios DevOps
    -Servicios de machine learning
    -Servicios de IoT
    -Otros servicios especializados

**6. 💾📋 ¿Cuál es la diferencia entre el almacenamiento de objetos y el almacenamiento en bloques?**

    -El almacenamiento de objetos como S3 guarda archivos completos con metadatos y está diseñado para acceso distribuido.
    -El almacenamiento en bloques como EBS funciona como un disco duro y es ideal para bases de datos y sistemas operativos.

**7. 🌆Enumere dos servicios de cómputo de AWS y explíquelos**

    -EC2 permite crear máquinas virtuales configurables según memoria, CPU, red y almacenamiento.
    -Lambda permite ejecutar código sin administrar servidores y funciona bajo el modelo serverless por ejecución.

**8. 🌐 Enumere dos servicios de almacenamiento de AWS y explíquelos**

    -S3 ofrece almacenamiento de objetos con alta durabilidad y disponibilidad.
    -EBS ofrece almacenamiento en bloques para instancias EC2 con persistencia.


## 💿 Ejercicio de investigación de bases de datos

**1. 🛢️¿Cuál es la diferencia entre una base de datos relacional y una no relacional?**

    -Una base de datos relacional utiliza tablas con filas y columnas siguiendo un esquema estructurado.
    -Una base de datos no relacional almacena datos de forma flexible, como documentos, grafos o pares clave-valor.

**2. ✳️¿Qué son los índices?**

    -Son estructuras que optimizan las consultas permitiendo localizar información sin recorrer toda la tabla.

**3. *️⃣¿Qué son las claves principales y secundarias?**

    -La clave primaria identifica de manera única cada registro y no permite nulos.
    -La clave secundaria o foránea establece relaciones con otra tabla y garantiza integridad referencial.

**4. ⏺️ ¿Qué son las uniones internas y externas?**

    -Una unión interna devuelve únicamente los registros coincidentes entre tablas.
    -Una unión externa puede devolver registros coincidentes y no coincidentes, según el tipo (left, right o full).

**5. 🔒¿Cuál es la diferencia entre DROP TABLE y TRUNCATE TABLE?**

    -DROP TABLE elimina completamente la tabla junto con su estructura.
    -TRUNCATE TABLE elimina los datos pero conserva la estructura.

**6. 🖥️¿Cuáles son los diferentes tipos de datos de SQL?**

    -Numéricos como INT y DECIMAL
    -Texto como VARCHAR y TEXT
    -Fecha y hora como DATE y DATETIME
    -Booleanos
    -Binarios como BLOB

**7. 📄 Explique las cláusulas WHERE y HAVING**

    -WHERE filtra filas antes de aplicar GROUP BY.
    -HAVING filtra grupos después de agrupaciones o funciones agregadas.


## 📊 Ejercicio de investigación de facturación de AWS 

**1. 🔗 Enumere los distintos tipos de planes de soporte de AWS**

    -Basic
    -Developer
    -Business
    -Enterprise On-Ramp
    -Enterprise

**2. 🧮 Explique la calculadora de costo mensual de AWS**

    -La AWS Pricing Calculator permite estimar costos configurando el consumo de cada servicio. Entrega un desglose mensual detallado según recursos, almacenamiento, transferencia y región.

**3. ⚖️ Enumere y explique los diferentes modelos de precios de Amazon EC2**

    -On-Demand permite pagar por uso sin compromisos.
    -Reserved Instances ofrece descuentos a cambio de un compromiso de uno o tres años.
    -Savings Plans ofrece flexibilidad con descuentos según un monto de uso comprometido por hora.
    -Spot Instances ofrece precios reducidos utilizando capacidad sobrante.
    -Dedicated Hosts entrega hardware físico dedicado para cumplir requisitos específicos.


## 🎆 Ejercicio de investigación de Fundamentos de AWS Cloud: segunda parte

**1. ⚙️ Explique el modelo de responsabilidad compartida de AWS**

    -AWS es responsable de la seguridad de la nube, incluyendo infraestructura y hardware.
    -El cliente es responsable de la seguridad en la nube, como configuraciones, datos e identidades.

**2. 🗂️ Explique un rol de AWS Identity and Access Management (IAM)**

    -Un rol es una identidad con permisos definidos que puede ser asumida por usuarios, aplicaciones o servicios para ejecutar acciones específicas.

**3. 📄Explique una política de AWS Identity and Access Management (IAM)**

    -Una política es un documento JSON que define permisos, acciones permitidas o denegadas y recursos afectados.

**4. 💿 Describa una Amazon Machine Image (AMI)**

    -Una AMI es una plantilla que contiene el sistema operativo, configuraciones y paquetes necesarios para lanzar nuevas instancias EC2.

**5. 📟 Enumere los distintos tipos de instancias de Amazon EC2 con casos de uso**

    -General Purpose para aplicaciones generales.
    -Compute Optimized para procesamiento intensivo.
    -Memory Optimized para bases de datos grandes.
    -Storage Optimized para cargas con alto rendimiento de I/O.
    -Accelerated Computing para procesamiento con GPU.

**6. 💽 Explique Amazon Virtual Private Cloud (VPC)**

    -Una VPC es una red privada virtual que permite definir direcciones IP, subredes, ruteo, gateways y reglas de seguridad.

**7. 🌐 Diferencie entre una subred pública y una privada**

    -Una subred pública tiene una ruta hacia un Internet Gateway.
    -Una subred privada no tiene acceso directo a internet y depende de mecanismos internos como NAT.


## 🗂️ Ejercicio de investigación de AWS Well-Architected Framework

**1. ⛩️¿Cuáles son los cinco pilares de Well-Architected Framework?**

    -Excelencia operativa
    -Seguridad
    -Fiabilidad
    -Eficiencia del rendimiento
    -Optimización de costos

**2. ⚙️ ¿Cuáles son las tres áreas de excelencia operativa en la nube?**

    -Preparar
    -Operar
    -Evolucionar

**3. 🔗 ¿Cuáles son los principios de diseño que refuerzan la seguridad del sistema?**

    -Trazabilidad
    -Automatización de controles
    -Protección en capas
    -Principio de privilegio mínimo
    -Validación continua

**4. 🖌️ ¿Cuáles son los principios de diseño que aumentan la fiabilidad?**

    -Recuperación automática
    -Pruebas frecuentes
    -Escalabilidad
    -Implementaciones pequeñas
    -Diseño orientado a fallos

**5. ⚖️ ¿En qué áreas hay que centrarse para lograr la eficiencia del rendimiento?**

    -Selección adecuada de recursos
    -Uso de arquitecturas serverless
    -Monitoreo constante
    -Uso de autoescalado

**6. 🔒 ¿Cuáles son los distintos enfoques para utilizar los recursos de AWS de forma rentable?**

    -Pago por demanda
    -Apagado de recursos no utilizados
    -Uso de Spot Instances
    -Caching
    -Autoescalado


## 💿 Ejercicio de investigación de AWS CloudFormation

**1. 💽 ¿Qué es el aprovisionamiento de la configuración?**

    -Es el proceso de crear recursos e infraestructura de manera automatizada y consistente.

**2. 🪢 ¿Qué es la administración de la configuración? Enumere herramientas comunes**

    -Corresponde al proceso de mantener configuraciones correctas en sistemas y servidores.
    -Herramientas comunes: Ansible, Chef, Puppet, SaltStack.

**3. 📋 ¿Qué es la integración continua?**

    -Es la práctica de integrar código de manera frecuente con validaciones y pruebas automáticas.

**4. ⛓️ ¿Qué es la entrega continua?**

    -Automatiza la preparación del software para que siempre esté listo para desplegarse.

**5. 📳 ¿Qué es AWS CloudFormation? Enumere tres ventajas de CloudFormation**

    -CloudFormation es un servicio que permite crear infraestructura mediante plantillas.
    -Sus ventajas son repetibilidad, automatización y reducción de errores manuales.

**6. ⚔️ ¿Qué son JSON y YAML? Enumere tres diferencias entre ellos**

    -YAML es más legible que JSON.
    -JSON utiliza llaves y corchetes, mientras YAML se basa en indentación.
    -YAML soporta referencias internas y JSON no.

**7. 🔋 ¿Qué es una pila en AWS CloudFormation?**

    -Una pila es un conjunto de recursos que se crean y administran como una unidad a partir de una plantilla.