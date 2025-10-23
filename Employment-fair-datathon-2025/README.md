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

------------------------------

## Bases de datos usadas:

Hemos descargado el dataset de la opción 1. Contiene los datos del municipio de Barcelona para 2023. Se puede ver el fichero [Aquí](https://github.com/cvilafer/Datato_Equipo1_Reto3/blob/main/Consumo_agua.parquet)

Lo hemos cargado desde el fichero .parquet en python a un dataframe de pandas y lo hemos exportado a un [excel](https://github.com/cvilafer/Datato_Equipo1_Reto3/blob/main/Consumo_agua.xlsx) para poderlo analizar en Power BI.

De la opción 2 del ACA hemos descargado el gráfico del estado de los embalses desde 2020 hasta 2023 para ver la evolución de la sequía.

## Campos del dataset:

Secció censal/Sección censal/Census section: Se ha renombrado el nombre a **Censo** y contiene la sección censal

Districte/Distrito/District: Se ha renombrado el nombre a **Distrito** y contiene el Distrito del consumo

Municipi/Municipio/Municipality: Se ha renombrado el nombre a **Municipio** y contiene el Municipio del consumo

Data/Fecha/Date: Se ha renombrado el nombre a **Fecha** y contiene la fecha del consumo

Ús/Uso/Use: Se ha renombrado el nombre a **Uso** y contiene el tipo de uso Industrial/Comercial/Doméstico

Nombre de comptadors/Número de contadores/Number of meters: Se ha renombrado el nombre a **Número de contadores** y contiene el número de contadores que hay

Consum acumulat (L/dia)/Consumo acumulado (L/día)/Accumulated consumption (L/day): Se ha renombrado a **Consumo acumulado (L/día)** y contiene el consumo en litros acumulados del día

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


