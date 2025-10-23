# Datató del Saló de l’Ocupació 2025

## Contexto del evento

Este análisis se desarrolló en el marco del **Datató del Saló de l’Ocupació 2025** en Barcelona, organizado por **IT Academy de Barcelona Activa** junto a **Mobile World Capital Barcelona**, como parte del **Mobile World Congress**.  

El evento tuvo lugar los días **15 y 16 de octubre de 2025**. Durante la primera jornada (**15 de octubre, de 9:00 a 19:00**), los participantes trabajaron en el desarrollo de los retos propuestos, seleccionando uno de los tres disponibles. Nuestro equipo abordó **el Reto 3**, centrado en el análisis de consumo de agua y presión hídrica en el Área Metropolitana de Barcelona.

---

# Reto 3: Consumo de Agua y Presión Hídrica en el Área Metropolitana de Barcelona

## Tópico: Medio ambiente y sostenibilidad

## Agenda 2030: ODS 6 – Agua limpia y saneamiento | ODS 13 – Acción por el clima

## Descripción

El agua es un recurso natural fundamental para el bienestar de la población, el funcionamiento de la economía y la sostenibilidad ambiental. Sin embargo, en las ciudades, el consumo de agua se ha mantenido elevado o incluso en aumento, a pesar de campañas de ahorro y concienciación ciudadana.

En un contexto de cambio climático, con sequías más prolongadas, temperaturas más altas y precipitaciones irregulares, esta situación genera una presión cada vez más intensa sobre el sistema hídrico.  

El Área Metropolitana de Barcelona es un ejemplo de esta tensión: alta densidad de población, intensa actividad económica y un uso extensivo del recurso hídrico en todos los sectores.  

Los patrones de consumo varían según el momento del día, la estación, el tipo de uso (doméstico, comercial o industrial) y el contexto climático, dificultando la identificación de consumos excesivos o ineficientes.

## Objetivo y entrega de datos

Analizar cómo se distribuye el consumo de agua en el Área Metropolitana de Barcelona según tipo de uso, estación, momento del día y condiciones ambientales.  
Se busca identificar zonas y períodos con consumos elevados o ineficientes, generar indicadores clave y proponer recomendaciones para una mejor gestión hídrica.

## Bases de datos sugeridas

1. [Datos de consumo de agua](https://www.abdatachallenge.cat/) en la ciudad de Barcelona proporcionados por Aigües de Barcelona (registro requerido).  
2. [Catálogo de Datos Abiertos de ACA](https://aca.gencat.cat/ca/laigua/consulta-de-dades/dades-obertes/cataleg-dades-obertes/) para datos sobre gestión hídrica en Cataluña.  
3. [Datos climatológicos de AEMET](https://www.aemet.es/ca/serviciosclimaticos/datosclimatologicos).

---

# Desarrollo

Análisis descriptivo del consumo de agua en 2023 en el Área Metropolitana de Barcelona, evaluando patrones según el tipo de uso (doméstico, comercial e industrial) y facilitando su visualización en Power BI.

## Dataset

- **Consumo de agua 2023 (Barcelona)**: Dataset de Aigües de Barcelona disponible en [Parquet](https://raw.githubusercontent.com/ingridtp/data-analytics-portfolio/main/Employment-fair-datathon-2025/Data/Consumo_agua.parquet) y [CSV](https://raw.githubusercontent.com/ingridtp/data-analytics-portfolio/main/Employment-fair-datathon-2025/Data/Consumo_agua.csv), para su análisis y visualización en Power BI.

## Campos del dataset principal

| Campo original            | Nombre usado             | Descripción                                  |
|---------------------------|-------------------------|---------------------------------------------|
| Secció censal             | **Censo**               | Sección censal                              |
| Districte                 | **Distrito**            | Distrito del consumo                         |
| Municipi                  | **Municipio**           | Municipio del consumo                        |
| Data                      | **Fecha**               | Fecha del consumo                            |
| Ús                        | **Uso**                 | Tipo de uso: Industrial / Comercial / Doméstico |
| Nombre de comptadors      | **Número de contadores**| Número de contadores registrados            |
| Consum acumulat (L/dia)  | **Consumo acumulado (L/día)** | Consumo diario acumulado en litros      |

## Herramientas usadas

- Power BI  
- Python

## Estructura
```
Employment-fair-datathon-2025/
├── Data/                         # Carpeta de datasets originales y procesados
│   ├── Consumo_agua.parquet      # Dataset original en formato Parquet
│   ├── Consumo_agua.csv          # Exportación a CSV del dataset
│
├── analysis/                      # Archivos de análisis y visualización de datos
│   └── Analisis_consumo_agua.pbix       # Archivo de Power BI con dashboards y análisis
│
├── scripts/                       # Scripts en Python para procesamiento y transformación de datos
│   └── convertir_fichero_parquet_a_csv.py  # Script para convertir el archivo Parquet a CSV
│
├── README.md                       # Documentación principal del proyecto, incluye contexto, desarrollo y resultados
└── LICENSE                         # Licencia del proyecto (por ejemplo, MIT)

```


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


