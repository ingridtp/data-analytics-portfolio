# Datató del Saló de l’Ocupació 2025

## Contexto del evento

Este análisis fue desarrollado en el marco del **Datató del Saló de l’Ocupació 2025** en Barcelona, organizado por **IT Academy de Barcelona Activa** junto a **Mobile World Capital Barcelona**, como parte del **Mobile World Congress**.  

El evento tuvo lugar los días **15 y 16 de octubre de 2025**. Durante la primera jornada (**15 de octubre, de 9:00 a 19:00**), los participantes trabajaron en el desarrollo de los retos propuestos, seleccionando uno de los tres retos disponibles. Nuestro equipo decidió abordar **el Reto 3**, centrado en el análisis de consumo de agua y presión hídrica en el Área Metropolitana de Barcelona.

---

# Reto 3: Consumo de Agua y Presión Hídrica en el Área Metropolitana de Barcelona

## Tópico: Medio ambiente y sostenibilidad
## Agenda 2030: ODS 6 – Agua limpia y saneamiento | ODS 13 – Acción por el clima

## Descripción:

El agua es un recurso natural fundamental para el bienestar de la población, el funcionamiento de la economía y la sostenibilidad ambiental. Sin embargo, en las ciudades, el consumo de agua se ha mantenido elevado o incluso en aumento, a pesar de una mayor concienciación ciudadana y de las campañas de ahorro.

En un contexto de cambio climático, con períodos de sequía más prolongados, temperaturas más altas y precipitaciones más irregulares, esta situación genera una presión cada vez más intensa sobre el sistema hídrico.

El Área Metropolitana de Barcelona es un claro ejemplo de esta tensión: alta densidad de población, intensa actividad económica y un uso extensivo del recurso hídrico en todos los sectores.

Los patrones de consumo varían mucho según el momento del día, la estación del año, el tipo de uso (doméstico, comercial o industrial) y el contexto climático. Esto dificulta identificar con claridad dónde y cuándo se producen usos excesivos o ineficientes que podrían corregirse mediante medidas específicas.

## Objetivo y entrega de datos:

¿Cómo se distribuye el consumo de agua en el Área Metropolitana de Barcelona en función del tipo de uso, la estación del año, el momento del día y las condiciones ambientales?

A partir de los datos disponibles, identifica zonas y períodos con consumos elevados o ineficientes, construye indicadores clave para su seguimiento, y propone recomendaciones para una mejor gestión del recurso hídrico.

## Bases de datos sugeridas:

1. [Datos de consumo de agua](https://www.abdatachallenge.cat/) en la ciudad de Barcelona proporcionados por Aigües de Barcelona (es necesario registrarse para obtener los datos).

2. Este [enlace](https://aca.gencat.cat/ca/laigua/consulta-de-dades/dades-obertes/cataleg-dades-obertes/) dirige al Catálogo de Datos Abiertos de la Agencia Catalana del Agua (ACA), donde se pueden consultar y descargar diversos conjuntos de datos relacionados con la gestión del agua en Cataluña.

3. [Datos climatológicos](https://www.aemet.es/ca/serviciosclimaticos/datosclimatologicos) de AEMET (Agencia Estatal de Meteorología).

---

# Desarrollo

Análisis descriptivo del consumo de agua en el Área Metropolitana de Barcelona durante 2023, evaluando patrones según el tipo de uso (doméstico, comercial e industrial) y facilitando su visualización en Power BI.

## Bases de datos usadas

- **Consumo de agua 2023 (Barcelona)**: 
Dataset de Aigües de Barcelona ([ver archivo](https://github.com/cvilafer/Datato_Equipo1_Reto3/blob/main/Consumo_agua.parquet)), exportado a  CSV para su análisis y visualización en Power BI.

- **Embalses de Cataluña 2020-2023 (ACA)**: Gráficos del estado de los embalses para analizar la evolución de la sequía.

## Campos del dataset principal

| Campo original | Nombre usado | Descripción |
|----------------|-------------|------------|
| Secció censal / Census section | **Censo** | Sección censal |
| Districte / District | **Distrito** | Distrito del consumo |
| Municipi / Municipality | **Municipio** | Municipio del consumo |
| Data / Date | **Fecha** | Fecha del consumo |
| Ús / Use | **Uso** | Tipo de uso: Industrial / Comercial / Doméstico |
| Nombre de comptadors / Number of meters | **Número de contadores** | Número de contadores registrados |
| Consum acumulat (L/dia) / Accumulated consumption | **Consumo acumulado (L/día)** | Consumo diario acumulado en litros |


## Herramientas usadas para análisis:

Power BI, Python

## Conclusiones datos analizados:

En el Power BI se puede ver el [análisis de los datos](Analisis_consumo_agua.pbix).

Observamos que el mayor consumo es el Industrial, excepto en los meses de febrero a abril que fué el doméstico.

El distrito que más aporta al consumo industrial es Sants-Montjuic (Zona Franca...)

El que aporta más al consumo doméstico es Ciutat Vella.

Y el Eixample es el que más aporta al consumo comercial.

Observamos una caída muy importante del consumo doméstico hacia abril de 2023 (distritos d'Eixample y Ciutat Vella). Justo coincide con la sequía y con la activación de excepcionalidad de marzo 2023:

https://www.totbarcelona.cat/es/sociedad/los-hogares-de-barcelona-reducen-el-consumo-agua-en-plena-sequia-438255/#:~:text=Cuando%20el%20marzo%20del%202023,litro%20menos%20que%20en%20marzo

![Noticia sequía](https://github.com/cvilafer/Datato_Equipo1_Reto3/blob/main/noticia_sequia1.png)

![Agua cuencas internas Catalunya](https://github.com/cvilafer/Datato_Equipo1_Reto3/blob/main/agua_cuencas_internas_catalunya.png)


