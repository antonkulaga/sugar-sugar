# **Predicción Humana de la Glucosa de la Próxima Hora a partir del Contexto Previo del Monitor Continuo de Glucosa (MCG): Un Estudio de Referencia en Línea**

**Protocolo del estudio**

**Investigador Principal:** Anton Kulaga \- Instituto de Bioestadística e Informática en Medicina e Investigación del Envejecimiento (IBIMA), Centro Médico Universitario de Rostock, Rostock, Alemania

**Co-investigadores:** Livia Zaharia (HEALES \- Healthy Life Extension Society, Bruselas, Bélgica)

**Asesoría bioestadística:** Benjamin Otte, M.Sc. \- Departamento de Bioestadística, Instituto de Bioestadística e Informática en Medicina e Investigación del Envejecimiento (IBIMA), Centro Médico Universitario de Rostock, Rostock, Alemania

**Contexto del proyecto:** Este estudio se lleva a cabo como parte del Estudio de Predicción de Precisión de Glucosa Sugar-Sugar, apoyado por HEALES (Healthy Life Extension Society)

**Número de registro:** Ref. A 2026-0064  
**Recibido por el Comité de Ética:** 27 de febrero de 2026

---

## **Resumen**

**Antecedentes:**

Los modelos de aprendizaje automático para la predicción de glucosa reportan métricas de precisión derivadas de conjuntos de datos académicos controlados, pero no existe ningún punto de referencia para la precisión de predicción humana. Los usuarios de MCG anticipan rutinariamente los niveles futuros de glucosa como parte de su autogestión diaria, sin embargo, la calidad de la predicción nunca ha sido evaluada sistemáticamente.

**Objetivos:**

(0) Cuantificar la precisión humana al predecir la glucosa de la próxima hora a partir de 3 horas de historial del MCG;

(1) Comparar la precisión de predicción entre personas con diabetes (PcD) de tipo 1 y tipo 2 y personas sin diabetes, incluyendo prediabetes, bienestar y usuarios sin experiencia previa (no-DM);

(2) Comparar la precisión de predicción entre usuarios de MCG y no usuarios de MCG. Una persona se considera usuario de MCG si ha utilizado uno por más de un mes.

**Diseño:**

Estudio en línea observacional de corte transversal donde se pide a los usuarios que realicen predicciones seis o más veces, con diseño adaptativo de tamaño de muestra en dos etapas.

**Entorno:**

Plataforma basada en web (aplicación Sugar-Sugar) alojada por HEALES con datos de investigación almacenados en el Centro Médico Universitario de Rostock.

**Participantes:**

N objetivo ≈200 adultos (≥18 años): aproximadamente 100 PcD y 100 no-PcD, reclutados a través de redes sociales y organizaciones de diabetes. El diseño adaptativo permite ajuste hasta 150 por grupo según análisis interino. Para el grupo no-DM, hay personas que utilizan sus MCG para seguimiento de condición física, mejora deportiva, mejora del estilo de vida, biohacking, etc. que mostraron interés preliminar en participar.

Los participantes se dividen en cuatro grupos: Usuarios PcD MCG (grupo "PcD MCG"), PcD sin MCG (grupo "PcD sin-MCG"), Usuarios no-PcD MCG (p. ej., para bienestar, deportes, etc., grupo "no-PcD"), Usuarios no-PcD sin-MCG sin experiencia previa (grupo "SEP")

**Procedimientos:**

Se alienta a los participantes con datos de MCG a subir sus propios datos con mediciones previas de glucosa (en adelante, datos históricos) para la tarea de predicción. La tarea es predecir cómo cambiarán los valores de glucosa estimados por el MCG (en adelante, VG) conociendo los valores anteriores. En el caso de nuestra aplicación web, esto se hace de manera intuitiva, dibujando la línea en un gráfico de VG. Para más detalles, consulte la sección 4.2.

Los participantes sin datos de MCG o que prefieren no subir datos pueden usar datos de terceros de conjuntos de datos públicos anonimizados que se pueden descargar gratuitamente. Hemos recopilado la lista de conjuntos de datos en [https://github.com/GlucoseDAO/glucose\_data\_processing/blob/main/docs/datasets.csv](https://github.com/GlucoseDAO/glucose_data_processing/blob/main/docs/datasets.csv), donde los conjuntos de datos con columna "Downloader" son completamente públicos.

Cada participante completará de 6 a 12 tareas de predicción. En cada tarea, predecirán lo que sucederá durante la próxima hora dibujando puntos en un gráfico mostrado en una aplicación web. Específicamente, predecirán 12 puntos de datos, uno por cada intervalo de 5 minutos durante el período de 60 minutos. Para ayudarlos a realizar estas predicciones, se les mostrarán las 3 horas anteriores de datos como contexto.

Múltiples intentos de predicción por participante son necesarios para obtener estimaciones de precisión fiables a nivel individual y potencia estadística adecuada.

**Fiabilidad de la medición:** Un único intento de predicción proporciona una estimación poco fiable de la capacidad individual debido a la variación aleatoria (p. ej., dificultad del segmento, lapsos momentáneos de atención). El promedio de 6 a 12 intentos produce métricas de precisión estables y reproducibles al reducir el error de medición.

**Potencia estadística:** El diseño de medidas repetidas aumenta sustancialmente la potencia estadística en comparación con los diseños de un solo intento. Con 200 participantes que completan 10 intentos cada uno, el tamaño de muestra efectivo para los análisis dentro de la persona se aproxima a 2.000 observaciones, lo que permite detectar tamaños de efecto pequeños a moderados (d de Cohen ≥ 0,3) que requerirían tamaños de muestra inviablemente grandes en diseños de un solo intento.

**Variabilidad contextual:** Múltiples intentos permiten muestrear a través de diversas dinámicas de glucosa (hora del día, dirección de tendencia, contextos de eventos), asegurando que las estimaciones de precisión reflejen el rendimiento en escenarios representativos en lugar de un único caso atípico.

**Viabilidad:** El rango de 6 a 12 intentos equilibra la precisión de medición con la carga del participante. Las pruebas piloto indicaron participación sostenida durante 15 a 20 minutos (aproximadamente 10 a 12 segmentos), después de lo cual los efectos de fatiga pueden comprometer la calidad de los datos.

Este enfoque sigue la práctica psicométrica estándar para establecer diferencias individuales fiables en tareas cognitivas y se alinea con diseños de medidas repetidas comúnmente utilizados en estudios de referencia del rendimiento humano.

**Medidas de resultado principales:**

Mediremos la precisión de las predicciones usando dos métricas estándar: Error Absoluto Medio (MAE) y Raíz del Error Cuadrático Medio (RMSE), ambos medidos en mg/dL. Estas métricas mostrarán cuánto se desvían las predicciones de los valores reales de glucosa. Calcularemos estas métricas tanto para los modelos de aprendizaje automático como para las predicciones de los participantes humanos.

**Análisis estadístico:**

Comparación grupal de MAE/RMSE por persona entre PcD y no-DM; comparación de predicciones humanas versus modelos de referencia (persistencia, extrapolación lineal). Los análisis secundarios examinan asociaciones entre experiencia y precisión. El análisis tiene en cuenta la estructura de medidas repetidas.

**Ética y difusión:**

Presentado al Comité de Ética, Centro Médico Universitario de Rostock. Estudio no intervencional que utiliza solo datos históricos. Los resultados serán publicados en revistas científicas revisadas por pares.

---

## **1\. Antecedentes y Justificación**

### **1.1 Contexto: Usuarios de MCG y Autopredicción**

Los dispositivos de Monitoreo Continuo de Glucosa (MCG) \[5\] proporcionan mediciones de glucosa en sangre cada 5 minutos, generando perfiles detallados de glucosa de 24 horas. La tecnología MCG es utilizada por varias poblaciones:

**Personas con Diabetes (PcD):**

* Usan datos de MCG para informar su propia dosificación de insulina, programación de comidas y decisiones de actividad
* Desarrollan reconocimiento intuitivo de patrones a través de la experiencia diaria con sus tendencias de glucosa
* Toman decisiones de autogestión basadas en trayectorias de glucosa anticipadas

**Personas Conscientes de la Salud (Usuarios de Bienestar):**

* Personas prediabéticas que monitorean la glucosa para la optimización del estilo de vida
* Usuarios no diabéticos interesados en la salud metabólica y la longevidad
* Atletas y biohackers que rastrean la respuesta de glucosa a la dieta y el ejercicio

En todos los casos, los usuarios hacen sus propias predicciones sobre los niveles futuros de glucosa como parte de la autogestión diaria — este estudio cuantifica esa capacidad de predicción.

### **1.2 El Problema del Punto de Referencia Faltante**

Los modelos de aprendizaje automático actuales para la predicción de glucosa reportan métricas técnicas (RMSE, MAE) pero estas se derivan de **conjuntos de datos académicos controlados**. Según GlucoBench \[1\], los modelos de vanguardia logran:

* **Predicciones a 30 minutos:** RMSE 8–12 mg/dL, MAE 6–10 mg/dL
* **Predicciones a 60 minutos:** RMSE 10–16 mg/dL, MAE 9–13 mg/dL

Sin embargo, estas métricas tienen limitaciones importantes:

1. **Rendimiento controlado vs. del mundo real:** Los puntos de referencia académicos usan conjuntos de datos seleccionados con calidad de datos consistente. Los usuarios reales de MCG tienen lagunas, errores de sensores y registro de eventos inconsistente.
2. **Sin comparación humana:** No sabemos cómo estas métricas de ML se comparan con la capacidad de predicción que los usuarios experimentados de MCG desarrollan a través del uso diario.
3. **Diversidad de población:** Los conjuntos de datos académicos a menudo se enfocan en tipos específicos de diabetes; los usuarios del mundo real incluyen poblaciones diabéticas, prediabéticas y de bienestar con diferentes contextos de predicción.

**Este estudio llena la brecha** estableciendo qué tan bien los usuarios reales de MCG predicen su propia glucosa en condiciones realistas.
Consulte la sección de referencias para más detalles.

### **1.3 Brecha de Investigación e Innovación**

Hasta donde sabemos, **ningún estudio anterior ha cuantificado sistemáticamente la precisión humana al predecir trayectorias de glucosa de la próxima hora**. Este estudio aborda esta brecha crítica mediante:

1. Establecimiento de la precisión de autopredicción humana de referencia en diferentes poblaciones de usuarios
2. Comparación del rendimiento entre los cuatro grupos mencionados: PcD MCG, PcD sin-MCG, no-PcD MCG y SEP
3. Examen de los factores asociados con la precisión de predicción (duración de diabetes, experiencia con MCG)
4. Creación de un punto de referencia del mundo real que complementa las métricas de ML derivadas en laboratorio

### **1.4 Justificación del Estudio**

Esta investigación es necesaria porque:

* **No existe referencia humana:** No sabemos qué tan bien los usuarios experimentados de MCG predicen su propia glucosa
* **Los puntos de referencia académicos son demasiado optimistas:** Las métricas de ML de conjuntos de datos seleccionados no reflejan las condiciones de rendimiento del mundo real
* **Poblaciones de usuarios diversas:** Los usuarios diabéticos, prediabéticos y de bienestar de MCG pueden tener diferentes capacidades de predicción
* **Contexto de autogestión:** Comprender la capacidad de predicción humana informa las expectativas realistas para las herramientas asistidas por IA

---

## **2\. Objetivos e Hipótesis del Estudio**

### **2.1 Objetivos Primarios**

**Objetivo 0:**

Cuantificar con qué precisión los humanos pueden predecir los niveles de glucosa para la próxima hora después de ver las 3 horas anteriores de datos de glucosa, independientemente de si usan MCG o tienen diabetes.

**Objetivo 1:**

Cuantificar y comparar con qué precisión las personas con diabetes (PcD) versus las personas sin diabetes (no-PcD) pueden predecir los niveles de glucosa para la próxima hora después de ver las 3 horas anteriores de datos de glucosa, independientemente de si usan MCG (grupos MCG y no-MCG combinados por pares según estado de diabetes).

**Objetivo 2:**

Cuantificar y comparar la precisión de las personas que ya usan monitores continuos de glucosa versus las personas que no usan MCG al predecir los niveles de glucosa para la próxima hora después de ver las 3 horas anteriores de datos de glucosa, independientemente de su estado de diabetes (grupos PcD y no-PcD combinados por pares según experiencia con MCG)

### **2.2 Objetivos Secundarios**

**Objetivo 3:** Probar si una mayor duración de la diabetes está asociada con una mejor precisión de predicción.

**Objetivo 4:** Probar si una mayor experiencia con MCG está asociada con una mejor precisión.

**Objetivo 5:** Comparar la precisión cuando los participantes predicen usando datos genéricos anonimizados versus sus propios datos de MCG (comparación dentro de la persona).

### **2.3 Hipótesis Formales** Esta sección solo presenta las hipótesis — para los métodos de prueba estadística, consulte la Sección 7\.

#### **Hipótesis Primarias**

**H1 (Diferencia de Grupo — Diferenciador de Diabetes Mellitus):**

* Hipótesis nula (H1.1): MAE medio de personas con diabetes \= MAE medio de personas sin diabetes
* Hipótesis alternativa (H1.2): MAE medio de personas con diabetes ≠ MAE medio de personas sin diabetes — la dirección se establece mediante comparación

*Justificación:* Las personas con diabetes tienen experiencia vivida directa manejando la variabilidad de glucosa y pueden desarrollar reconocimiento intuitivo de patrones a través del uso diario de MCG. Un MAE más bajo indica mejor precisión de predicción.

**H2 (Diferencia de Grupo — Diferenciador de Usuario de MCG):**

* Hipótesis nula (H2.1): MAE medio de personas con MCG \= MAE medio de personas sin MCG
* Hipótesis alternativa (H2.2): MAE medio de personas con MCG ≠ MAE medio de personas sin MCG — la dirección se establece mediante comparación

*Justificación:* GlucoBench \[1\] y estudios relacionados proporcionan puntos de referencia: para predicciones a 60 minutos, los modelos simples logran MAE ~12–20 mg/dL mientras que los modelos de aprendizaje profundo (Transformer, Gluformer) logran MAE ~11–17 mg/dL dependiendo del conjunto de datos y las condiciones. Esperamos que el rendimiento humano caiga en algún lugar de este rango. Esta comparación establece dónde se sitúa la intuición humana en relación con los enfoques algorítmicos.

#### **Hipótesis Secundarias**

**H3 (Efecto de Duración):**

* Hipótesis nula (H3.0): No hay relación entre la duración de la diabetes y el MAE (ρ \= 0)
* Hipótesis alternativa (H3.1): Hay una relación negativa entre la duración de la diabetes y el MAE (ρ \< 0), con los efectos más fuertes en los primeros 5 años

Una mayor duración de la diabetes está asociada con un mayor número de observaciones de valores de glucosa, lo que a su vez resulta en un MAE más bajo (mejor precisión). Estas provienen no solo de las lecturas del MCG sino también de la experiencia acumulada previamente a través de análisis de sangre y observación de eventos como comer, inyectar, deportes y actividad física. Todos estos eventos convertirían a un diabético más experimentado en un predictor más preciso de la variación de glucosa.

*Justificación:* Las personas que han vivido con diabetes por más tiempo han acumulado más experiencia observando cómo responde su glucosa a las comidas, la insulina, el ejercicio, el estrés y otros factores. Esta exposición extendida proporciona más oportunidades para reconocer patrones y desarrollar habilidades intuitivas de predicción.

Mención importante: la duración en nuestro caso solo se correlacionará con el tiempo con diabetes, no con la edad genérica del participante — por lo tanto, no agruparemos a los usuarios según su edad sino según el tiempo real con esta condición. Esto tampoco se verificará contra el número de participantes (p. ej., asumiendo que las personas mayores tienen más experiencia con su condición pero menos participación general en el estudio — eso llevaría a incertidumbre — solo nos importa cómo la duración de la condición refleja la precisión de predicción entre los que participaron)

**H4 (Efecto de Experiencia con MCG):**

* Hipótesis nula (H4.0): No hay relación entre la duración de la experiencia con MCG y el MAE (ρ \= 0)
* Hipótesis alternativa (H4.1): Hay una relación negativa entre la duración de la experiencia con MCG y el MAE (ρ \< 0), con los efectos más fuertes en los primeros 2 años

Una mayor experiencia con MCG está asociada con un MAE más bajo (mejor precisión).

*Justificación:* Los usuarios de MCG toman decisiones diarias basadas en sus tendencias de glucosa — ajustando dosis de insulina, programando comidas y modificando actividades. Este ciclo continuo de retroalimentación crea un entorno de aprendizaje natural donde los usuarios desarrollan habilidades de reconocimiento de patrones a través de la toma repetida de decisiones y la observación de resultados. Los usuarios que han usado MCG por más tiempo han tenido más oportunidades de aprender su dinámica personal de glucosa.

**H5 (Datos Propios vs. Genéricos):**

* Hipótesis nula (H5.1): MAE medio de personas usando datos propios \= MAE medio de personas usando datos genéricos
* Hipótesis alternativa (H5.2): MAE medio de personas usando datos propios ≠ MAE medio de personas usando datos genéricos — la dirección se establece mediante comparación

Los participantes tienen un MAE más bajo (mejor precisión) al predecir sus propios patrones de glucosa versus datos genéricos. Esto se medirá permitiendo a los participantes probar de dos maneras — usando un conjunto de datos genérico o subiendo sus propios datos para predecir. En el segundo caso, los datos serán anonimizados del usuario (no se mostrará ninguna fecha — solo la hora — para evitar recordar la fecha exacta) y se representarán exactamente como en el caso anterior gráficamente.

*Justificación:* Los participantes están familiarizados con sus propios patrones de glucosa, estilo de vida y respuestas típicas a las comidas y actividades. Este conocimiento personal debería proporcionar una ventaja al predecir sus propios datos en comparación con perfiles genéricos desconocidos.

**H6 (Humano vs. Modelos de Referencia):**
Planteamos la hipótesis de que la precisión de predicción humana (MAE) caerá entre modelos de referencia simples y enfoques de IA de vanguardia.

Los modelos de referencia son los métodos de predicción más simples posibles — no requieren entrenamiento ni algoritmos complejos. Nuestras referencias incluyen: (1) modelo de persistencia — asumiendo que la glucosa permanece constante en la lectura actual, (2) extrapolación lineal — trazando una línea recta a través de las lecturas recientes y extendiéndola hacia adelante, y (3) ARIMA — un método estadístico estándar para datos de series temporales.

Esperamos la jerarquía de rendimiento: referencias simples < predicciones humanas < modelos de aprendizaje profundo (p. ej., LSTMs, Transformers). Probaremos si los humanos superan significativamente a las referencias y si el aprendizaje profundo supera significativamente a los humanos.

Esta hipótesis se dejará para la continuación del estudio en el momento en que tengamos un modelo bien definido — En este momento ningún modelo está involucrado en el estudio.

*Justificación:* GlucoBench y estudios relacionados proporcionan puntos de referencia: para predicciones a 60 minutos, los modelos simples logran MAE ~12–20 mg/dL mientras que los modelos de aprendizaje profundo (Transformer, Gluformer \[2,7,8\]) logran MAE ~11–17 mg/dL dependiendo del conjunto de datos y las condiciones. Esperamos que el rendimiento humano caiga en algún lugar de este rango. Esta comparación establece dónde se sitúa la intuición humana en relación con los enfoques algorítmicos.

---

## **3\. Diseño del Estudio**

### **3.1 Tipo de Estudio**

**Diseño:** Observacional, transversal con tareas repetidas de predicción. Para más detalles consulte la Sección 4.2  
**Recolección de datos:** Plataforma en línea basada en web  
**Seguimiento:** Ninguno (participación en una sola sesión)

### **3.2 Clasificación Regulatoria**

Este estudio es un **estudio no intervencional, observacional** que no requiere supervisión médica ni regulación de dispositivos médicos.

#### **3.2.1 Solo Datos Históricos**

* Todos los datos de MCG mostrados a los participantes son **datos históricos, pregrabados** — ya sea de un conjunto de datos anónimo agrupado o de los propios archivos de MCG exportados previamente del participante
* **No se realiza monitoreo de glucosa en tiempo real** durante el estudio
* **Sin conexión a dispositivos MCG activos** — los participantes no necesitan usar ningún equipo de monitoreo para este estudio
* El estudio analiza la precisión de predicción en segmentos de datos pasados, no en el estado de salud actual

#### **3.2.2 Sin Decisiones Médicas ni Diagnósticos**

Este estudio explícitamente **NO**:

* Proporciona ningún diagnóstico médico o pronóstico
* Hace recomendaciones terapéuticas o de tratamiento
* Influye en decisiones clínicas o planes de tratamiento médico
* Ofrece consejos o guías de salud personalizadas
* Genera resultados destinados al uso clínico

**Los resultados son puramente para fines de referencia de investigación** — las puntuaciones de precisión indican solo el rendimiento de predicción y no tienen significado diagnóstico ni terapéutico.

#### **3.2.3 No se Requiere Supervisión Médica**

La supervisión médica no es requerida para este estudio porque:

* **No se administra ninguna intervención médica**
* **No se realizan pruebas diagnósticas**
* **Ningún resultado de salud** depende de la participación o los resultados
* **Ninguna decisión de tratamiento** está informada por el estudio
* La actividad es equivalente a **completar una tarea cognitiva en línea o encuesta**

### **3.3 Población del Estudio**

#### **Criterios de Inclusión**

**Población General (Ambos Grupos):**

* Edad 18 años o mayor
* Capaz de proporcionar consentimiento informado
* Acceso a internet y alfabetización básica en computadora/móvil
* Dispuesto a completar tareas de predicción

**Adicional para Personas con Diabetes (PcD):**

* Diagnóstico de diabetes autoreportado (Tipo 1, Tipo 2 u otro)
* Uso actual o pasado de MCG (cualquier dispositivo)

---

## **4\. Flujo de Trabajo del Participante y Procedimientos**

### **4.1 Estrategia de Reclutamiento**

**Canales de Reclutamiento:**

1. Anuncios en redes sociales (Twitter/X, LinkedIn, grupos de diabetes en Facebook)
2. Organizaciones de pacientes con diabetes y grupos de defensa
3. Redes de la junta asesora científica
4. Canales comunitarios (sitio web del proyecto, Telegram)
5. Conferencias académicas (presentaciones en reuniones de longevidad/diabetes)

Los materiales de reclutamiento específicos se desarrollarán después de obtener la aprobación ética.

### **4.2 Procedimientos del Estudio**

#### **Fase 1: Consentimiento e Información de Referencia**

Los participantes acceden a la aplicación web Sugar-Sugar a través de una URL (dirección web) y completan:

**1\. Consentimiento Informado Electrónico**

* Hoja de información del estudio
* Información de protección de datos (conforme al RGPD)
* Consentimiento por casilla de verificación para participación en el estudio y procesamiento de datos
* Consentimientos opcionales para: subir datos de MCG propios, contacto futuro en caso de que el usuario quiera conocer más detalles sobre los resultados del estudio cuando se complete, comunicaciones promocionales

**2\. Cuestionario de Referencia**
**(será completado por el participante, con precisión, según su conocimiento)**

* Correo electrónico (para identificación única; hasheado para anonimización)
* Edad (años)
* Sexo/género
* País de residencia
* Estado de diabetes (Sí/No)
  * Si Sí: Tipo de diabetes, años desde el diagnóstico
* Uso de MCG (Sí/No)
  * Si Sí: años de uso
* Peso opcional (kg) y altura (cm)

**Nota de Protección de Datos:** Los correos electrónicos se hashean inmediatamente al enviarse para identificación única sin almacenar identificadores personales. Los participantes pueden optar por separado para comunicaciones de re-contacto.

#### **Fase 2: Ensayos de Práctica**

2 ensayos de práctica opcionales para familiarizar a los participantes con la interfaz (los usuarios tienen la opción de no enviar para los primeros 2 ensayos). Los datos del ensayo de práctica se excluyen del análisis.

#### **Fase 3: Tarea de Predicción de Datos Genéricos**

**Estructura de la Tarea:**

* **Número de ensayos:** 6–12 segmentos de predicción por participante
* **Cada segmento:** El participante dibuja 12 puntos de predicción (intervalos de 5 minutos durante 60 minutos)
* **Ventana de contexto mostrada:** 3 horas de datos MCG (36 puntos a resolución de 5 minutos)
* **Fuente de datos:** Datos de MCG desidentificados del conjunto de datos curado del estudio

Los segmentos se seleccionan para proporcionar una mezcla equilibrada de diferentes horas del día, tendencias de glucosa y contextos de eventos. El orden se aleatoriza entre participantes.

**Características de la Interfaz:**

* Gráfico interactivo con cuadrícula de tiempo de 5 minutos
* Los participantes hacen clic/dibujan para crear la curva de predicción
* Visualización de marcadores de eventos (marcas de tiempo de comida/insulina/ejercicio)
* Predicciones editables antes del envío

*A continuación se muestra la interfaz principal para el usuario después de completar los formularios de datos y consentimiento.*
*\-la línea azul y el punto representan los datos históricos graficados para la prueba*

*\-la línea roja son datos predichos por el usuario*

*\-existe la opción de cambiar las unidades de medición — dependiendo de las más familiares para el participante*

*\-hay información sobre qué ronda de las 12 es esta*

*\-el usuario tiene dos opciones en cualquier etapa durante la prueba — enviar o simplemente salir*

*Después de cada ronda el usuario recibe una pantalla de la siguiente manera:*

*\-hay información sobre qué ronda fue*

*\-hay comparación de datos — la línea azul se muestra completamente*

*\-están los resultados de edición numérica*

*\-así como el resultado estadístico por esta ronda*

*\-el usuario nuevamente tiene la opción de salir o continuar a la siguiente ronda*

*Al final del ensayo (máximo 12 rondas) el usuario recibe esta pantalla donde todos los datos se compilan por todo el ensayo. A continuación hay dos ejemplos — uno en el que el usuario ha hecho solo una ronda y uno en el que el usuario ha hecho múltiples rondas. Como se puede ver contiene:*
*\-métricas de precisión*

*\-unidades en que se ejecutó*

*\-valores por cada ronda*

*\-¡clasificación![][image1]*

![][image2]

#### **Fase 4: Subir Datos Propios y Tarea (Opcional)**

**Elegibilidad:** Participantes que indicaron disposición a subir datos de MCG

**Proceso de Subida de Datos:**

1. Subir archivo de exportación del MCG (formato CSV o JSON de dispositivos compatibles, o exportación de Nightscout)
2. Verificaciones de calidad automatizadas (mínimo 5 días consecutivos, validación de datos)
3. Procesamiento de datos en el que convertimos del formato de dispositivo compatible al formato uniforme que usamos para la salida de datos
4. Pseudonimización de datos y almacenamiento seguro

**Tarea de Predicción de Datos Propios:**

* 6–12 segmentos muestreados de los datos de MCG propios del participante
* Segmentos anonimizados (no se muestran fechas/horas)
* Permite comparación dentro de la persona de precisión en datos propios vs. genéricos

#### **Fase 5: Finalización y Retroalimentación**

**Breve Recordatorio de Seguridad (Solo en Primera Vista):**

En la primera participación, se muestra un breve aviso antes de los resultados:

**Solo para fines de investigación** — Estas puntuaciones miden el rendimiento de reconocimiento de patrones, no la capacidad médica. Continúe siguiendo la orientación de su proveedor de atención médica.

Este aviso se muestra una vez por usuario; los usuarios que regresan ven los resultados directamente.

**Visualización de Resultados (mostrada por defecto):**

* Resumen de precisión personal (MAE en mg/dL)
* Rango percentil comparado con otros participantes según el almacenamiento actual de la base de datos en el momento de la participación del usuario. En pocas palabras, tenemos un almacenamiento separado de clasificación — solo necesitamos un ID de usuario anonimizado y rango — desde allí se conoce el número total de participantes y su rendimiento
* Comparación visual de predicciones vs. trayectorias reales
* Opción de "Omitir y terminar" disponible pero no prominente

**Tarjeta de Resultado Compartible (Contenido Controlado por el Usuario):**

Los usuarios pueden crear y compartir una tarjeta de resultado con contenido personalizable:

* **Siempre incluido:** "Participé en el estudio de predicción de glucosa Sugar-Sugar"
* **El usuario puede elegir incluir:** percentil de precisión, puntuación MAE, número de segmentos completados, comparación con otros participantes
* **El usuario controla qué compartir** — la gamificación es una característica clave de participación
* Los usuarios son informados de que compartir puede revelar su interés en temas de glucosa/diabetes

**Sin Asesoramiento Médico:** Los resultados se presentan como métricas de rendimiento del juego/investigación, no como evaluaciones de salud.

---

## **5\. Recolección y Gestión de Datos**

### **5.1 Categorías de Datos**

**Datos de Referencia:** Datos demográficos y de usuario como:

* Correo electrónico (para identificación única; hasheado para anonimización)
* Edad (años)
* Sexo/género
* País de residencia
* Estado de diabetes (Sí/No)
  * Si Sí: Tipo de diabetes, años desde el diagnóstico
* Uso de MCG (Sí/No)
  * Si Sí: años de uso
* Peso opcional (kg) y altura (cm)

**Preferencias de Consentimiento:**

* para participación en el estudio y procesamiento de datos
* para: subir datos de MCG propios, contacto futuro en caso de que el usuario quiera conocer más detalles sobre los resultados del estudio cuando se complete, comunicaciones promocionales

**Datos del Gráfico:**

6–12 segmentos por participante, cada uno conteniendo

**Datos de Predicción:** 12 puntos de predicción (incluyendo valor de glucosa y marca de tiempo),

**Datos de Verdad Fundamental:** 12 valores reales del MCG para evaluación (no mostrados a los participantes hasta después del envío, incluyendo valor de glucosa y marca de tiempo)

**Datos de Resultado:**

Valores de MAE, MSI, RSME, MAPE

### **5.2 Protección de Datos y Cumplimiento del RGPD**

#### **5.2.1 Controlador de Datos, Procesador y Arquitectura**

**Controlador de Datos:** El Institut für Biostatistik und Informatik in der Medizin und Alternsforschung (IBIMA) en la Universitätsmedizin Rostock (UMR) es el controlador de datos para este estudio.

**Implicaciones de este acuerdo:**

* IBIMA/UMR asume plena responsabilidad por el cumplimiento del RGPD y los derechos de los participantes
* Todas las solicitudes de los interesados (acceso, eliminación, retiro) son manejadas por el equipo de investigación en IBIMA

**Procesador de Datos:** HEALES (Healthy Life Extension Society) operará la aplicación web Sugar-Sugar como procesador de datos bajo un Acuerdo de Procesamiento de Datos (APD) con UMR.

**Arquitectura Técnica: Modelo Pull**

El estudio utiliza una arquitectura de "modelo pull" enfocada en seguridad:

\[Participante\] → \[App Sugar-Sugar (servidores HEALES)\] ← \[Recolector de Datos UMR\]

                         ↓                                    ↑

                   \[Caché Temporal\] ──────────────────→ \[Base de Datos de Investigación (UMR)\]

**Cómo funciona:**

1. El participante interactúa con la app Sugar-Sugar alojada en servidores HEALES
2. Los datos de sesión completados se cifran y almacenan temporalmente en caché en los servidores HEALES
3. El sistema de recolección de datos de UMR **extrae** datos de HEALES periódicamente (cada 2 horas) y los descifra
4. Después de una transferencia exitosa, la caché en HEALES se borra
5. Todos los datos de investigación persistentes se almacenan exclusivamente en servidores UMR
6. No existe capacidad de descifrado en el lado HEALES, asegurando la caché temporal

**Ventajas de seguridad:**

* La base de datos de investigación de UMR no tiene acceso entrante de sistemas externos
* HEALES no puede "empujar" datos a UMR — UMR inicia todas las transferencias de datos, el flujo de datos es unidireccional por diseño
* El almacenamiento temporal de datos cifrados en caché sin claves de descifrado en el lado HEALES mitiga los riesgos de acceso no autorizado a la caché
* Superficie de ataque reducida en la infraestructura de datos de investigación
* Separación clara entre capa de aplicación (HEALES) y almacenamiento de datos (UMR)

**Caché temporal en servidores HEALES:**

* Contiene solo datos de sesión completados en espera de transferencia, en forma cifrada
* Retención máxima: 7 días (eliminado automáticamente si la extracción falla)
* Cifrado en reposo
* Sin acceso directo a la caché excepto por el sistema de extracción automatizado
* La caché es procesamiento transitorio, no almacenamiento persistente

**El Acuerdo de Procesamiento de Datos (APD) especifica:**

* HEALES procesa datos solo según las instrucciones de UMR
* Sin almacenamiento persistente de datos de investigación en servidores HEALES
* Sin almacenamiento no cifrado de datos de investigación en servidores HEALES
* La caché se borra inmediatamente después de una extracción exitosa a UMR
* Eliminación automática de la caché después de 7 días independientemente del estado de extracción
* Medidas de seguridad para la caché temporal (cifrado, controles de acceso)
* Derechos de auditoría para UMR
* El acceso del personal de HEALES limitado al mantenimiento técnico únicamente

**Sin otros procesadores externos:**

* Ningún servicio externo de análisis, CDN o de terceros procesa datos de participantes
* Los miembros de la comunidad HEALES (distintos del equipo de investigación enumerado) no tienen acceso a los datos de los participantes

#### **5.2.2 Identificación y Pseudonimización**

**Qué se almacena y por qué:**

1. **Dirección de correo electrónico (texto plano, cifrado en reposo):** Almacenado separadamente de los datos de investigación solo para dos propósitos:
   * Habilitar solicitudes de retiro (el participante nos contacta, ubicamos y eliminamos sus datos)
   * Re-contacto opcional para resultados del estudio (solo si el participante optó por ello)
2. **ID de Estudio:** Identificador alfanumérico aleatorio asignado mediante hashing (p. ej., f5afc4cf-9881-467d-88a1-325eb9558baa) asignado al registrarse
3. **Tabla de vinculación:** Un archivo cifrado separado que mapea ID de Estudio ↔ Dirección de correo electrónico
   * Almacenado en unidad cifrada separada de los datos de investigación
   * Acceso restringido al IP (Anton Kulaga) y co-IP únicamente
   * Propósito: Habilitar retiro y re-contacto opcional
4. **Datos de investigación:** Todos los datos de predicción, subidas de MCG, respuestas del cuestionario almacenados pseudonimizados solo con ID de Estudio (sin correo electrónico, sin nombre)

**Aclaración del Hash:** NO nos basamos en el hashing de correo electrónico para la pseudonimización. El hash se usa solo para la detección de duplicados durante el registro (impidiendo que la misma persona se registre dos veces). La tabla de vinculación contiene el correo electrónico real para propósitos de retiro/re-contacto.

#### **5.2.3 Política de Retención y Eliminación**

| Tipo de Datos | Período de Retención | Desencadenante de Eliminación |
| :---- | :---- | :---- |
| Direcciones de correo electrónico | Hasta finalización del estudio + 12 meses | Tabla de vinculación destruida después del período de gracia |
| Tabla de vinculación | Finalización del estudio + 12 meses | Destruida, convirtiendo los datos en completamente anónimos |
| Datos de investigación (pseudonimizados) | 10 años según estándares de investigación alemanes | N/A — retenidos para reproducibilidad |
| Archivos MCG subidos | Procesados inmediatamente, archivos sin procesar eliminados dentro de 30 días | Automático después de la extracción de segmentos |

#### **5.2.4 Limitaciones del Retiro (Importante)**

**El retiro es posible en cualquier momento HASTA que se destruya la tabla de vinculación** (aproximadamente 12 meses después de la finalización del estudio). Después de este punto:

* Los datos de investigación se vuelven completamente anónimos (no es posible la reidentificación)
* Las solicitudes de retiro no pueden cumplirse ya que no podemos identificar qué datos pertenecen al solicitante
* Esta limitación se indica claramente en el formulario de consentimiento

**Proceso de retiro:**

1. El participante envía un correo electrónico al coordinador del estudio solicitando retiro
2. Ubicamos su ID de Estudio a través de la tabla de vinculación
3. Todos los datos de investigación asociados con ese ID de Estudio se eliminan permanentemente
4. Se envía confirmación al participante

#### **5.2.5 Transferencias de Datos Transfronterizas**

**Ningún dato sale de la Unión Europea.**

* **Base de datos de investigación UMR:** Ubicada en Alemania (UE)
* **Cuenta de nube gestionada por HEALES:** Ubicada en la UE (solo caché temporal, máx. 24 horas)
* Sin servicios de terceros que transfieran datos fuera de la UE
* Sin CDN, análisis externos o servicios en la nube con centros de datos fuera de la UE
* Las comunicaciones por correo electrónico utilizan proveedores de correo electrónico estándar con sede en la UE

Los participantes fuera de la UE pueden participar, pero sus datos se procesan y almacenan exclusivamente dentro de la UE bajo las protecciones del RGPD.

#### **5.2.6 Seguridad del Almacenamiento de Datos**

* **Ubicación de la base de datos de investigación UMR:** Alemania (UE)
* **Ubicación de la caché temporal de HEALES:** UE
* **Cifrado en tránsito:** TLS 1.3 (tanto de la app al usuario como la extracción de UMR a HEALES)
* **Cifrado en reposo:** AES-256 (tanto la base de datos UMR como la caché HEALES)
* **Controles de acceso:** Basados en roles; datos de investigación accesibles al equipo de investigación; tabla de vinculación accesible solo para los IPs
* **Respaldo:** Copias de seguridad cifradas diarias dentro de la UE (solo UMR; la caché de HEALES es transitoria)
* **Registro de auditoría:** Todo acceso a datos registrado

---

## **6\. Medidas de Resultado y Métricas de Precisión**

### **6.1 Métricas Primarias**

Utilizamos métricas estándar de la literatura de predicción de glucosa \[1,9,10\], lo que permite comparación directa con benchmarks de modelos de ML publicados (p. ej., GlucoBench — para más detalles consulte la sección de Referencias).

**Error Absoluto Medio (MAE):** Promedio de la diferencia absoluta entre los valores de glucosa predichos y los reales (en mg/dL). Valores más bajos indican mejor precisión.

 MAE \= (1 / n) × Σ |predicho − real|

* Mide el tamaño típico de los errores de predicción
* Todos los errores se ponderan por igual
* Mismas unidades que la variable objetivo

**Raíz del Error Cuadrático Medio (RMSE):** Raíz cuadrada de las diferencias cuadráticas promedio. Penaliza errores más grandes más fuertemente que el MAE. También reportado en mg/dL.

 RMSE \= sqrt(MSE)

* Misma unidad que la variable objetivo
* Penaliza errores grandes como el MSE
* Más fácil de interpretar que el MSE

**Error Cuadrático Medio (MSE):** El promedio de las diferencias cuadráticas entre los valores predichos y los reales.

 MSE \= (1 / n) × Σ (predicho − real)²

* Penaliza errores grandes más fuertemente
* Sensible a valores atípicos
* Las unidades están elevadas al cuadrado, lo que hace más difícil la interpretación directa

**Error Porcentual Absoluto Medio (MAPE):** El error absoluto promedio expresado como un porcentaje del valor real.

 MAPE \= (100 / n) × Σ |(predicho − real) / real|

* Mide el error relativo
* Independiente de la escala
* Puede ser engañoso cuando los valores reales están cerca de cero

Estas métricas se calculan:

* Por ensayo (a través de los 12 puntos de predicción)
* Por participante (promediado a través de sus 6–12 ensayos)
* Por grupo (para comparaciones de grupos)

### **6.2 Comparaciones con Modelos de Referencia**

Para contextualizar el rendimiento humano, comparamos con modelos de referencia simples usando los mismos segmentos de prueba:

* **Modelo de persistencia:** Predecir que la glucosa permanece constante en el último valor observado
* **Extrapolación lineal:** Proyectar la tendencia de los últimos 30 minutos hacia adelante

Esto se hará después de la recopilación de datos para establecer un punto de partida para la parte futura del estudio donde integraremos modelos de ML. No afectará la recopilación de datos en esta etapa del estudio. Para más detalles consulte H6.

---

## **7\. Plan de Análisis Estadístico**

### **7.1 Descripción General**

El estudio recopila **múltiples mediciones por participante** (6–12 segmentos de predicción cada uno, con 12 puntos por segmento). El análisis tiene en cuenta esta estructura de medidas repetidas. Da una visión más precisa de la habilidad de predicción del participante que una sola medición.

### **7.2 Poblaciones de Análisis**

* **Análisis primario:** Todos los participantes que completan al menos 6 segmentos de datos genéricos analizables
* **Análisis de datos propios:** Participantes que completan al menos 6 segmentos de datos propios
  El número de segmentos de datos propuestos se debe a la variabilidad esperada en las métricas de precisión (MAE/RMSE). Según los datos de GlucoBench, la desviación estándar para la precisión de predicción es de alrededor de 0,18–0,22 en una escala de 0–1. Si solo hubiera 2–3 mediciones por persona, la estimación de su capacidad tendría intervalos de confianza grandes.

## **7.3 Análisis Primarios**

### **H1 (Diferencia de Grupo — Estado de Diabetes)**

**Objetivo**: Comparar la precisión de predicción entre personas con diabetes (PcD) y personas sin diabetes (no-PcD).

**Resumen de Datos**: Cada participante predecirá valores de glucosa para múltiples puntos temporales en diferentes presentaciones de trazas de glucosa. Calcularemos un valor MAE por participante promediando sus errores de predicción a través de todas sus predicciones. Esto nos da una puntuación de precisión resumida por persona.

**Método Estadístico**:

1. **Verificación de Normalidad**: Primero probaremos si los valores MAE están distribuidos normalmente dentro de cada grupo usando la prueba de Shapiro-Wilk (p > 0,05 indica distribución normal).
2. **Comparación de Grupos**:
   * **Si los datos están distribuidos normalmente** (Shapiro-Wilk p > 0,05): Usaremos una **prueba t de muestras independientes**. Esta prueba compara el MAE promedio entre dos grupos teniendo en cuenta la variabilidad dentro de cada grupo y los tamaños de muestra. La prueba t calcula si la diferencia observada en promedios es mayor de lo que se esperaría por azar solo.
   * **Si los datos no son normales** (Shapiro-Wilk p < 0,05): Usaremos la **prueba U de Mann-Whitney**. Esta prueba no paramétrica compara grupos clasificando todas las puntuaciones MAE de mejor a peor (independientemente del grupo), luego probando si un grupo tiende a tener mejores rangos que el otro. Este enfoque es robusto a los valores atípicos y distribuciones sesgadas.
3. **Nivel de Significancia**: α \= 0,05 (bilateral)
4. **Tamaño del Efecto**: Reportaremos la d de Cohen (para prueba t) o la correlación biserial de rangos (para Mann-Whitney) para cuantificar la magnitud de la diferencia.

**Por qué este enfoque**: Usamos estadísticas de resumen por persona (un MAE por participante) en lugar de analizar miles de predicciones individuales porque las predicciones individuales de la misma persona no son independientes — están influenciadas por la estrategia de predicción consistente de esa persona. Resumir a un valor por persona asegura que nuestras pruebas estadísticas cumplan el supuesto de observaciones independientes.

---

### **H2 (Diferencia de Grupo — Experiencia con MCG)**

**Objetivo**: Comparar la precisión de predicción entre personas que actualmente usan MCG y personas que nunca han usado MCG.

**Resumen de Datos**: Igual que H1 — un valor MAE por participante, promediado a través de todas sus predicciones.

**Método Estadístico**: Enfoque idéntico a H1:

1. Prueba de Shapiro-Wilk para evaluar la normalidad
2. Prueba t de muestras independientes (si es normal) o prueba U de Mann-Whitney (si no es normal)
3. Nivel de significancia α \= 0,05 (bilateral)
4. Reportar el tamaño del efecto apropiado

**Justificación**: La misma lógica que H1 — estamos comparando dos grupos independientes en una sola medida de precisión por persona.

---

## **7.4 Análisis Secundarios**

### **H3 (Efecto de Duración — Diabetes)**

**Objetivo**: Probar si una mayor duración de la diabetes está asociada con una mejor precisión de predicción.

**Resumen de Datos**: Para cada participante con diabetes, tenemos:

* **Variable predictora**: Duración de la diabetes en años (variable continua)
* **Variable de resultado**: MAE (un valor por persona, calculado como en H1)

**Método Estadístico**:

1. **Verificación de Normalidad y Linealidad**:
   * Crear un gráfico de dispersión de la duración de la diabetes (eje x) vs. MAE (eje y) para inspeccionar visualmente la relación
   * Usar la prueba de Shapiro-Wilk para verificar si los valores MAE están distribuidos normalmente
   * Examinar el gráfico de dispersión para detectar patrones lineales vs. curvos
2. **Análisis de Correlación**:
   * **Si el MAE está distribuido normalmente Y la relación parece lineal**: Usar el **coeficiente de correlación de Pearson (r)**. Este mide la fuerza y dirección de una relación lineal entre dos variables continuas. Los valores van de -1 (relación negativa perfecta) a +1 (relación positiva perfecta). Esperamos correlación negativa (mayor duración → MAE más bajo).
   * **Si el MAE no es normal O la relación parece no lineal**: Usar la **correlación de rango de Spearman (ρ)**. Esta funciona como Pearson pero usa rangos en lugar de valores reales, lo que la hace robusta a los valores atípicos y capaz de detectar relaciones monótonas (consistentemente crecientes o decrecientes) incluso si no son perfectamente lineales.
3. **Nivel de Significancia**: α \= 0,05 (bilateral)
4. **Análisis Exploratorio**: Porque anticipamos que la relación puede llegar a una meseta (gran mejora en los primeros años, mejora mínima después de 5+ años), adicionalmente:
   * Ajustar un modelo logarítmico: MAE \= β₀ \+ β₁·log(duración \+ 1)
   * Comparar ajuste lineal vs. logarítmico usando valores R²
   * Crear una visualización que muestre cómo cambia el MAE a través de las categorías de duración (<1 año, 1–5 años, 5–10 años, >10 años)

**Por qué este enfoque**: El análisis de correlación es apropiado cuando se examina la relación entre dos variables continuas. Usamos Spearman como respaldo porque las curvas de aprendizaje a menudo muestran rendimientos decrecientes (patrones no lineales), y Spearman puede detectar estas relaciones incluso cuando no son líneas perfectamente rectas.

---

### **H4 (Efecto de Experiencia con MCG)**

**Objetivo**: Probar si una mayor experiencia con MCG está asociada con una mejor precisión de predicción entre los usuarios de MCG.

**Resumen de Datos**:

* **Variable predictora**: Experiencia con MCG en años (variable continua, solo para usuarios de MCG)
* **Variable de resultado**: MAE (un valor por usuario de MCG)

**Método Estadístico**: Enfoque idéntico a H3:

1. Visualización del gráfico de dispersión y verificación de normalidad (Shapiro-Wilk)
2. Correlación de Pearson (si normal/lineal) o correlación de Spearman (si no normal/no lineal)
3. Modelado logarítmico exploratorio para probar efectos de meseta
4. Nivel de significancia α \= 0,05

**Justificación**: La misma lógica que H3 — esperamos que los usuarios de MCG muestren una mejora rápida inicialmente, con un aprendizaje que llega a una meseta después de que hayan internalizado los patrones comunes de glucosa.

---

### **H5 (Datos Propios vs. Datos Genéricos)**

**Objetivo**: Probar si los participantes predicen con más precisión cuando ven sus propios datos de glucosa en comparación con datos genéricos anonimizados.

**Resumen de Datos**: Esta es una **comparación dentro de la persona**. Los participantes que completan ambas condiciones tendrán:

* **MAE de datos propios**: Error promedio a través de todas las predicciones en sus propias trazas de glucosa personales
* **MAE de datos genéricos**: Error promedio a través de todas las predicciones en trazas anonimizadas
* **Puntuación de diferencia**: MAE genérico − MAE propio (los valores positivos indican mejor rendimiento en datos propios)

**Método Estadístico**:

1. **Por qué análisis pareado**: Usamos pruebas "pareadas" porque tenemos **dos mediciones de la misma persona** (precisión en datos propios vs. precisión en datos genéricos). Esto es fundamentalmente diferente de H1–H2 donde comparamos personas diferentes. Las pruebas pareadas tienen en cuenta que la misma persona aparece en ambas condiciones, controlando factores específicos de la persona como la habilidad general de predicción, la atención, la motivación, etc.
2. **Verificación de Normalidad**: Prueba de Shapiro-Wilk en las **puntuaciones de diferencia** (no en los valores MAE brutos)
3. **Comparación**:
   * **Si las puntuaciones de diferencia están distribuidas normalmente**: Usar **prueba t de muestras pareadas**. Esto prueba si la diferencia promedio entre condiciones es significativamente diferente de cero, teniendo en cuenta la correlación dentro de la persona.
   * **Si las puntuaciones de diferencia no son normales**: Usar la **prueba de rangos con signo de Wilcoxon**. Este es el equivalente no paramétrico de la prueba t pareada — clasifica las diferencias absolutas y prueba si las diferencias positivas (mejor rendimiento en datos propios) son más comunes que las negativas.
4. **Nivel de Significancia**: α \= 0,05 (bilateral)
5. **Tamaño del Efecto**: Reportar la d de Cohen para diseño pareado

**Por qué este enfoque**: Las pruebas pareadas son más potentes que las pruebas independientes porque eliminan la variabilidad debida a las diferencias individuales. Si la Persona A es simplemente naturalmente mejor en las tareas de predicción que la Persona B, eso no importa — solo nos importa si cada persona se desempeña de manera diferente en los dos tipos de datos.

---

### **H6 (Humano vs. Modelos de Referencia)**

**Nota**: Esta hipótesis se pospone para trabajo futuro cuando se implementen los modelos de referencia. Cuando se analice, usaremos enfoques de comparación pareada similares, comparando el MAE de cada participante con el MAE logrado por los modelos computacionales en las mismas trazas de glucosa.

---

## **Tabla Resumen de Métodos Estadísticos**

| Hipótesis | Tipo de Comparación | Prueba Primaria | Prueba Alternativa | Cuándo Usar la Alternativa |
| ----- | ----- | ----- | ----- | ----- |
| H1 | Grupos independientes (PcD vs. no-PcD) | Prueba t independiente | U de Mann-Whitney | Shapiro-Wilk p < 0,05 |
| H2 | Grupos independientes (MCG vs. sin-MCG) | Prueba t independiente | U de Mann-Whitney | Shapiro-Wilk p < 0,05 |
| H3 | Correlación (duración vs. MAE) | r de Pearson | ρ de Spearman | No normal o no lineal |
| H4 | Correlación (experiencia MCG vs. MAE) | r de Pearson | ρ de Spearman | No normal o no lineal |
| H5 | Comparación pareada (propio vs. genérico) | Prueba t pareada | Rangos con signo de Wilcoxon | Puntuaciones de diferencia no normales |

**Todas las pruebas usan nivel de significancia α \= 0,05. Se reportarán tamaños de efecto para todos los análisis.**

### **7.5 Expectativas de Tamaño del Efecto**

Basado en GlucoBench y la literatura relacionada de predicción de glucosa para **horizontes de predicción de 60 minutos**:

**Rendimiento de Modelos de Benchmarks Publicados (MAE en mg/dL):**

El rendimiento varía considerablemente entre conjuntos de datos y condiciones. Rangos representativos de la literatura:

* **Regresión lineal / ARIMA \[7,8\]:** MAE ~12–20 mg/dL (datos ID de GlucoBench), RMSE ~23–27 mg/dL (otros estudios)
* **Aprendizaje profundo (Transformer, Gluformer \[2,7,8\]):** MAE ~11–17 mg/dL dependiendo del conjunto de datos
* **Modelos personalizados de vanguardia:** MAE ~15–17 mg/dL (enfoques recientes basados en LLM \[3\])

Nota: Los valores varían sustancialmente según el tamaño del conjunto de datos, las características de la población y si la evaluación es in-distribution (ID) vs. out-of-distribution (OD). GlucoBench informa que los modelos de aprendizaje profundo generalizan considerablemente mejor que las referencias simples en datos OD.

**Tamaños de Efecto Esperados para las Hipótesis del Estudio:**

Dada esta variabilidad, usamos suposiciones conservadoras:

* **H1 (PcD vs. no-DM):** Asumiendo SD ~8–12 mg/dL entre participantes y una diferencia significativa de ~3–5 mg/dL entre grupos, esto representa d de Cohen ~0,3–0,5 (efecto pequeño a mediano).
* **H2 (Humano vs. referencias):** La brecha entre modelos simples y avanzados es típicamente ~5–10 mg/dL. Esperamos que los humanos caigan dentro de este rango. Para más descripción de la distribución esperada humana consulte el tamaño de muestra.
* **H3, H4 (Correlaciones de duración/MCG):** Esperamos correlaciones de r ~0,15–0,30 entre experiencia y precisión, basadas en suposiciones de curva de aprendizaje.
* **H5 (Propio vs. genérico):** Esperamos una mejora de ~2–4 mg/dL al predecir datos propios (efecto pareado). Esto es importante ya que cubre la diferencia esperada entre el valor de glucosa en sangre real y el valor de glucosa estimado (VGE) que proporcionan los MCG.

**Advertencia importante:** Estas estimaciones de tamaño del efecto se derivan de la variabilidad entre modelos de ML en benchmarks, no de estudios previos de predicción humana (que no existen). La distribución real del rendimiento humano es desconocida y será establecida por este estudio. Enfatizamos que estos números se estiman basándose en los artículos mencionados en la sección de referencias, especialmente el artículo de GlucoBench.

---

## **8\. Tamaño de la Muestra**

### **8.1 Inscripción Objetivo**

**Objetivo:** Aproximadamente 200 participantes en total

* Aproximadamente 100 personas con diabetes (PcD)
* Aproximadamente 100 personas sin diabetes (no-DM)
* Entre los PcD: objetivo para 70–90 participantes que suban datos propios

**Mínimo viable:** Aproximadamente 150 participantes (75 por grupo)

### **8.2 Justificación**

Los objetivos de tamaño de muestra se basan en estimaciones de tamaño del efecto derivadas de benchmarks de modelos de ML, con reconocimiento de incertidumbre:

**Manejo de medidas repetidas:** Cada participante realiza 6–12 predicciones, lo que significa que nuestros datos tienen una estructura de medidas repetidas. Tomamos esto en cuenta de dos maneras: (1) nuestros análisis primarios usarán promedios por persona (un valor MAE por participante), lo que satisface el supuesto de independencia para pruebas t y correlaciones, y (2) para análisis más detallados, usaremos modelos de efectos mixtos que modelan explícitamente la correlación entre medidas repetidas de la misma persona.

**Diferencias significativas:** Consideramos una diferencia de 3–4 mg/dL en el MAE como clínicamente significativa porque es aproximadamente la mitad del error de medición de los propios dispositivos MCG (que tienen una diferencia relativa absoluta media del 8–10% de la glucosa en sangre, o aproximadamente 7–9 mg/dL a niveles típicos de glucosa). Una correlación de r=0,25 explica aproximadamente el 6% de la varianza, lo cual, aunque modesto, valdría la pena entender para el diseño de intervenciones futuras.

**H1 (Comparación del grupo diabetes vs. no-diabetes):** Para detectar una diferencia de 4 mg/dL en el error absoluto medio (MAE) entre grupos, asumiendo una desviación estándar de 10 mg/dL (d de Cohen ≈ 0,4), necesitamos 80–100 participantes por grupo. Usamos una prueba unilateral con α=0,025 aquí porque la literatura previa sugiere que las personas con diabetes podrían predecir mejor, aunque la dirección no es segura. Este ajuste de Bonferroni tiene en cuenta el testeo de dos comparaciones primarias (H1 y H2).

**H2 (Usuarios de MCG vs. no usuarios):** Mismo cálculo que H1 — esperamos tamaños de efecto similares y necesitamos aproximadamente 80–100 por grupo. La naturaleza pareada de algunas comparaciones dentro de los participantes (donde la misma persona realiza múltiples predicciones) en realidad nos da poder estadístico adicional, pero estamos siendo conservadores en nuestras estimaciones.

**H3 y H4 (Análisis de correlación):** Para detectar una correlación de r=0,25 entre duración de la experiencia y precisión de predicción con el 80% de poder, necesitamos 100–120 participantes. El rango (100–120) refleja la incertidumbre en la fuerza de correlación real — si la correlación real es más débil que r=0,25, necesitaríamos el extremo superior de ese rango. Elegimos r=0,25 como nuestro objetivo porque las correlaciones más pequeñas tendrían una importancia práctica limitada.

**H5 (Comparación de datos propios vs. datos genéricos):** Esta es una comparación dentro de la persona, por lo que tenemos más poder estadístico. Para detectar una diferencia de 3 mg/dL en mediciones pareadas (asumiendo un SD pareado de 6 mg/dL), necesitamos aproximadamente 70 participantes que completen ambas tareas. El diseño pareado es más eficiente porque cada persona sirve como su propio control.

**Advertencia Importante:** Incertidumbre del Tamaño de la Muestra

Nuestros cálculos de tamaño de muestra están basados en el rendimiento del modelo de ML, pero el comportamiento humano puede diferir:

Por qué importa:

* Los modelos de ML son consistentes → variabilidad predecible (SD ~10 mg/dL)
* Los humanos son variables → diferencias individuales, efectos de aprendizaje, fatiga
* Riesgo: Si el SD humano real difiere de las suposiciones, el poder cambia drásticamente

Ejemplos:

| Escenario | SD Asumida | SD Real | N planificada por grupo | Poder Real | Estado |
| ----- | ----- | ----- | ----- | ----- | ----- |
| Optimista | 10 mg/dL | 8 mg/dL | 100 | ~95% | Sobrepotenciado |
| Caso base | 10 mg/dL | 10 mg/dL | 100 | 80% | Adecuado |
| Conservador | 10 mg/dL | 12 mg/dL | 100 | ~65% | Subpotenciado |
| Pesimista | 10 mg/dL | 15 mg/dL | 100 | ~45% | Severamente subpotenciado |

**Resultado:** El estudio podría estar subpotenciado para detectar efectos reales o desperdiciar recursos con inscripción innecesaria.

---

**Solución Propuesta:** Diseño Adaptativo de Dos Etapas

**Etapa 1 –** Análisis Interino (N=60–75 por grupo)

* Calcular SDs y tamaños de efecto observados de datos humanos reales
* Recalcular el tamaño de muestra requerido usando estimaciones empíricas
* Ajustar el objetivo de reclutamiento para mantener el 80% de poder

**Etapa 2 –** Reclutamiento Ajustado

* Continuar inscripción hasta el objetivo revisado basado en los hallazgos interinos
* Reglas de decisión pre-especificadas:
  * *"Si SD observada \= 8 mg/dL → parar en 100 por grupo (ya sobrepotenciado)"*
  * *"Si SD observada \= 12 mg/dL → aumentar a 130 por grupo"*
  * *"Si SD observada >15 mg/dL → aumentar a máximo 150 por grupo"*
* Límite máximo: 150 por grupo

Beneficios:

* Asegura poder adecuado con datos del mundo real
* Evita sobre-reclutamiento si la variabilidad es menor de lo esperado
* Previene la subpotenciación severa si la variabilidad es mayor

**8.3 Resultado Esperado**

Con nuestra inscripción objetivo (100 por grupo, potencialmente ampliable a 150), deberíamos tener poder adecuado para todos los análisis planificados asumiendo que nuestras estimaciones de variabilidad son aproximadamente correctas. Pero el valor real de este estudio no es solo probar nuestras hipótesis específicas — es establecer los primeros benchmarks empíricos para la precisión de predicción de glucosa humana.

Incluso si descubrimos que los humanos son mucho más variables que los modelos de ML, eso es un hallazgo que vale la pena publicar. Nos diría que la capacidad de predicción humana es fundamentalmente menos consistente que los enfoques algorítmicos, lo que tiene implicaciones para cómo diseñamos y evaluamos las herramientas de apoyo a la decisión clínica.

**Datos faltantes y exclusiones:** Usaremos análisis de casos completos para los resultados primarios (participantes que terminan al menos 6 segmentos de predicción válidos). Si los datos faltantes superan el 10% de los participantes reclutados, realizaremos análisis de sensibilidad comparando completadores vs. no completadores en características de referencia. No esperamos datos faltantes sustanciales porque la tarea es en línea y toma solo 15–20 minutos.

**Multiplicidad:** Tenemos dos hipótesis primarias (H1 y H2) usando la corrección de Bonferroni (α=0,025 por prueba). Las hipótesis secundarias (H3, H4, H5) son exploratorias y se reportarán con valores p nominales sin ajuste, claramente etiquetadas como análisis exploratorios.

**Quién realiza el análisis:** Los análisis estadísticos primarios serán realizados por Anton Kulaga (IP) con orientación de Benjamin Otte (asesor bioestadístico). Todos los análisis se realizarán en Python usando paquetes estándar. El código de análisis se pondrá a disposición pública junto con los resultados publicados.

**Factores de confusión:** El diseño transversal del estudio limita nuestra capacidad para controlar los factores de confusión. Recopilaremos y reportaremos variables clave (edad, duración de la diabetes, experiencia con MCG) y realizaremos análisis estratificados donde el tamaño de la muestra lo permita. Las comparaciones primarias (PcD vs. no-PcD, MCG vs. sin-MCG) son descriptivas en lugar de causales, por lo que los factores de confusión son menos problemáticos que en los estudios de intervención.

**Confirmatorio vs. exploratorio:** H1 y H2 son hipótesis confirmatorias con niveles de significancia ajustados por Bonferroni. H3, H4 y H5 son exploratorias y se reportarán como tales, con intervalos de confianza y tamaños de efecto en lugar de depender únicamente de los valores p.

---

## **9\. Control de Calidad de Datos**

### **9.1 Verificaciones Automatizadas**

* Validación de unicidad del correo electrónico
* Validación del rango de edad
* Verificaciones del tiempo de finalización
* Validación del punto de predicción (los 12 puntos requeridos)
* Verificaciones de calidad de datos MCG para subidas

### **9.2 Criterios de Exclusión para el Análisis**

* Segmentos con predicciones incompletas (menos de 12 puntos)
* Segmentos con datos de contexto MCG excesivamente faltantes
* Participantes con menos de 5 segmentos válidos

---

## **10\. Análisis Riesgo-Beneficio**

### **10.1 Riesgos para los Participantes**

#### **10.1.1 Riesgos Físicos**

**Ninguno.** Este es un estudio observacional en línea sin intervenciones físicas:

* Sin procedimientos médicos
* Sin administración de medicamentos
* Sin visitas en persona requeridas
* **Sin monitoreo de salud en tiempo real** — todos los datos son históricos
* **Sin conexión a dispositivos médicos activos** — los participantes no necesitan usar ningún equipo

#### **10.1.2 Riesgos Psicológicos**

**Mínimos:**

* Posible frustración con las tareas de predicción (mitigada con instrucciones claras, ensayos de práctica)
* Leve ansiedad de rendimiento (mitigada enfatizando el propósito de investigación)
* Preocupaciones de privacidad sobre compartir datos de MCG (mitigadas con participación opcional, explicación completa de protección de datos)

**Evaluación General:** Riesgos comparables a completar un cuestionario o encuesta en línea.

### **10.2 Beneficios**

**Beneficios Directos para los Participantes:** Ninguno (solo estudio de investigación). Los resultados no constituyen asesoramiento médico.

**Importantes Descargos de Responsabilidad Comunicados a los Participantes:**

* Las puntuaciones de precisión miden solo el rendimiento de predicción — no tienen significado diagnóstico ni terapéutico
* Los resultados no deben usarse para ajustar la dosificación de insulina, elecciones dietéticas o cualquier decisión médica
* Los participantes deben continuar siguiendo la orientación de su proveedor de atención médica de forma independiente

**Beneficios Indirectos:**

* Contribuir al conocimiento científico
* Perspectiva personal sobre la capacidad de predicción
* Apoyar el desarrollo de mejores herramientas de predicción de glucosa

---

## **11\. Protección del Participante y Ética**

### **11.1 Consentimiento Informado**

Nota importante — todo consentimiento se dará haciendo clic en las casillas de verificación correspondientes en la interfaz en línea y se almacenará digitalmente. Si no se da el consentimiento obligatorio, al participante no se le permite continuar, deteniendo cualquier participación sin consentir.

**Puerta de Verificación de Edad:**

Antes de acceder a cualquier contenido del estudio, los participantes deben confirmar que tienen 18 años o más:

* La primera pantalla muestra: "Este estudio está abierto a adultos de 18 años o más. Por favor confirme su edad para continuar."
* Dos botones: "Tengo 18 años o más" (procede al consentimiento) / "Tengo menos de 18" (muestra mensaje: "Gracias por su interés, pero este estudio solo está abierto a adultos. Por favor cierre esta página.")
* Si se selecciona "menor de 18": No se recopilan datos, la sesión termina inmediatamente, sin cookies ni identificadores almacenados
* Esta puerta de edad aparece antes de cualquier recopilación de datos personales

**Proceso de Consentimiento Bilingüe:**

El estudio proporciona materiales de consentimiento informado en inglés y alemán. Los participantes seleccionan su idioma preferido al inicio:

* **Selección de Idioma:** Los participantes eligen "English" o "Deutsch" en la página de inicio
* **Materiales Completos:** Toda la información de consentimiento, instrucciones del estudio y retroalimentación se muestran en el idioma seleccionado
* **Contenido Equivalente:** Ambas versiones de idioma contienen información idéntica, asegurando igual comprensión independientemente de la preferencia de idioma

**El Formulario de Consentimiento Electrónico incluye:**

* Información clara del estudio en lenguaje no técnico
* Énfasis en la participación voluntaria
* Explicación de la protección de datos y derechos del RGPD
* Procedimientos y limitaciones del retiro (retiro posible hasta la anonimización de datos)
* Información de contacto

**Casillas de Consentimiento (obligatorias):**

* Confirmo que tengo 18 años o más, he leído y entendido la información del estudio, y voluntariamente acepto participar
* Consiento el procesamiento de datos con fines de investigación y entiendo que puedo retirarme hasta la anonimización de datos (RGPD Art. 6(1)(a), 9(2)(a))

**Casillas de Consentimiento Opcional (claramente separadas del consentimiento del estudio):**

* Acepto subir mis propios datos de MCG para la tarea de datos propios opcional
* Acepto ser recontactado para los resultados del estudio (correo electrónico almacenado solo para este propósito)

**Comunicaciones Promocionales (Separadas del Consentimiento del Estudio):**

Cualquier opt-in para comunicaciones promocionales sobre HEALES o proyectos relacionados es:

* Presentado en una página SEPARADA DESPUÉS de la finalización del estudio (no durante el consentimiento)
* Claramente etiquetado como no relacionado con la participación en el estudio
* No tiene ningún efecto en la participación en el estudio ni en el manejo de datos
* Puede rechazarse sin ninguna consecuencia

### **11.2 Compensación**

Sin compensación monetaria. Los incentivos no monetarios incluyen retroalimentación personalizada de precisión y tarjeta de resultado compartible.

### **11.3 Seguro**

No se requiere seguro específico del estudio debido al riesgo mínimo (equivalente a encuesta en línea).

---

## **12\. Cronograma**

El cronograma del estudio es flexible y se ajustará según el progreso del reclutamiento y las necesidades operativas. Las fases generales incluyen:

1. **Preparación:** Presentación ética, finalización de plataforma, preparación de material de reclutamiento
2. **Prueba Piloto:** Pruebas a pequeña escala con recopilación de retroalimentación
3. **Reclutamiento y Recopilación de Datos:** Continuo hasta alcanzar la inscripción objetivo
4. **Análisis:** Procesamiento de datos, análisis estadístico
5. **Difusión:** Preparación de manuscrito, publicación, comunicación con participantes

Los cronogramas específicos se determinarán según la fecha de aprobación ética y el éxito del reclutamiento.

---

## **13\. Limitaciones**

### **13.1 Sesgo de Selección**

Los participantes son voluntarios autoseleccionados, lo que puede no representar a la población general de usuarios de MCG.

### **13.2 Benchmarks Académicos vs. del Mundo Real**

Si bien este estudio utiliza condiciones más realistas que los conjuntos de datos académicos controlados, los participantes en línea pueden diferir de los usuarios típicos de MCG.

### **13.3 Diseño de Sesión Única**

Sin seguimiento longitudinal; no se pueden evaluar los efectos del aprendizaje a lo largo del tiempo.

---

## **14\. Información de Contacto**

**Investigador Principal:**

 Anton Kulaga  
 Instituto de Bioestadística e Informática en Medicina e Investigación del Envejecimiento (IBIMA)  
 Centro Médico Universitario de Rostock  
 Correo electrónico: anton.kulaga@uni-rostock.de

**Co-investigadores:**

Livia Zaharia, MSc  
 HEALES \- Healthy Life Extension Society  
 Correo electrónico: [liviazaharia2020@gmail.com](mailto:liviazaharia2020@gmail.com)

**Asesor bioestadístico:**

Benjamin Otte, MSc  
 Instituto de Bioestadística e Informática en Medicina e Investigación del Envejecimiento (IBIMA)  
 Centro Médico Universitario de Rostock  
 Correo electrónico: benjamin.otte@uni-rostock.de

**Gestor de Datos:**  
 Nikolay Usanov, MSc  
 HEALES \- Healthy Life Extension Society  
 Ingeniero de ML y Bioinformático

**Junta Asesora:**

* Prof. Georg Fullen \- Centro Médico Universitario de Rostock
* Irina Gaynanova, PhD (Asesora Estadística) \- Texas A\&M University
* Renat Sergazinov, PhD (Asesor Técnico) \- Autor de GlucoBench

## Referencias:

\[1\] Sergazinov, R., Chun, E., Rogovchenko, V., Fernandes, N., Kasman, N., & Gaynanova, I. (2024). GlucoBench: Curated List of Continuous Glucose Monitoring Datasets with Prediction Benchmarks. International Conference on Learning Representations (ICLR). https://doi.org/10.48550/arXiv.2410.05780

\[2\] Sergazinov, R., Armandpour, M., & Gaynanova, I. (2023). Gluformer: Transformer-Based Personalized Glucose Forecasting with Uncertainty Quantification. IEEE International Conference on Acoustics, Speech, and Signal Processing (ICASSP). https://doi.org/10.48550/arXiv.2209.04526

\[3\] Yang, F., Wang, X., Liu, Y., et al. (2024). From Glucose Patterns to Health Outcomes: A Generalizable Foundation Model for Continuous Glucose Monitor Data Analysis. arXiv. https://doi.org/10.48550/arXiv.2408.11876

\[4\] Battelino, T., Danne, T., Bergenstal, R. M., et al. (2019). Clinical Targets for Continuous Glucose Monitoring Data Interpretation: Recommendations from the International Consensus on Time in Range. Diabetes Care, 42(8), 1593-1603. https://doi.org/10.2337/dci19-0028

\[5\] Rodbard, D. (2016). Continuous Glucose Monitoring: A Review of Successes, Challenges, and Opportunities. Diabetes Technology & Therapeutics, 18(S2), S2-3-S2-13. https://doi.org/10.1089/dia.2015.0417

\[6\] Hall, H., Perelman, D., Breschi, A., et al. (2018). Glucotypes reveal new patterns of glucose dysregulation. PLOS Biology, 16(7), e2005143. https://doi.org/10.1371/journal.pbio.2005143

\[7\] Jaloli, M., & Cescon, M. (2022). Long-term Prediction of Blood Glucose Levels in Type 1 Diabetes Using a CNN-LSTM-Based Deep Neural Network. Journal of Diabetes Science and Technology, 17(6), 1590-1601. https://doi.org/10.1177/19322968221092785

\[8\] Li, K., Daniels, J., Liu, C., Herrero, P., & Georgiou, P. (2019). Convolutional recurrent neural networks for glucose prediction. IEEE Journal of Biomedical and Health Informatics, 24(2), 603-613. https://doi.org/10.1109/JBHI.2019.2908488

\[9\] Gaynanova, I., Punjabi, N., & Crainiceanu, C. (2022). Modeling continuous glucose monitoring (CGM) data during sleep. Biostatistics, 23(1), 223-239. https://doi.org/10.1093/biostatistics/kxaa023

\[10\] Broll, S., Urbanek, J., Buchanan, D., et al. (2021). Interpreting blood glucose data with R package iglu. PLOS ONE, 16(4), e0248560. https://doi.org/10.1371/journal.pone.0248560

---

**Regulaciones Aplicables:**

* RGPD / BDSG (protección de datos) \- SÍ
* Directrices de ética de investigación alemanas \- SÍ
* Regulaciones de dispositivos médicos (MDR) \- NO aplicable
* AMG (ley farmacéutica) \- NO aplicable

---

**FIN DEL DOCUMENTO**

*Para preguntas o aclaraciones, por favor contacte:*  
 *Anton Kulaga: anton.kulaga@uni-rostock.de*  
 *Livia Zaharia: livia.zaharia@uni-rostock.de*
