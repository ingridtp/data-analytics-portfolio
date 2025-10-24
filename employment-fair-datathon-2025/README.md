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

## Campos del dataset principal

| Campo original                             | Nombre usado             | Descripción                                  |
|-------------------------------------------|-------------------------|---------------------------------------------|
| Secció censal / Sección censal / Census section | **Censo**               | Sección censal                              |
| Districte / Distrito / District            | **Distrito**            | Distrito del consumo                         |
| Municipi / Municipio / Municipality        | **Municipio**           | Municipio del consumo                        |
| Data / Fecha / Date                        | **Fecha**               | Fecha del consumo                            |
| Ús / Uso / Use                             | **Uso**                 | Tipo de uso: Industrial / Comercial / Doméstico |
| Nombre de comptadors / Número de contadores / Number of meters | **Número de contadores**| Número de contadores registrados            |
| Consum acumulat (L/dia) / Consumo acumulado (L/día) / Accumulated consumption (L/day) | **Consumo acumulado (L/día)** | Consumo diario acumulado en litros |

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

## Guía rápida del archivo Power BI

El análisis de consumo de agua en el Área Metropolitana de Barcelona está disponible en el archivo de Power BI: [Analisis_consumo_agua.pbix](analysis/Analisis_consumo_agua.pbix)

### Descripción de las pestañas
1. **Consumo general**: Visualización del consumo total de agua en el área metropolitana, agregando todos los tipos de uso.  
2. **Consumo general por distrito**: Comparativa del consumo total por distrito, facilitando la identificación de zonas con mayor demanda.  
3. **Consumo Industrial por distrito**: Visualización del consumo industrial por cada distrito.  
4. **Consumo doméstico por distrito**: Visualización del consumo doméstico por distrito.  
5. **Consumo comercial por distrito**: Visualización del consumo comercial por distrito.

## Conclusiones del análisis descriptivo

El análisis de los datos en Power BI ([ver archivo](analysis/Analisis_consumo_agua.pbix)) permite identificar patrones clave en el consumo de agua durante 2023:

- **Consumo general**: Más del **50%** del consumo corresponde al sector **Industrial**, que es el mayor consumidor durante la mayoría del año, excepto entre febrero y abril, cuando predomina el consumo **doméstico**.  
- **Distritos con mayor consumo total**: Sants-Montjuïc, Eixample, Ciutat Vella, Sant Martí y Horta-Guinardó concentran más del **70%** del consumo total, siendo **Sants-Montjuïc** el distrito con mayor consumo.  

- **Consumo industrial**: Sants-Montjuïc, Eixample, Ciutat Vella y Sant Martí representan más del **65%** del consumo industrial, con **Sants-Montjuïc** concentrando el **25%** del total.  

- **Consumo doméstico**: Ciutat Vella, Sant Martí, Eixample y Horta concentran más del **65%** del consumo doméstico, siendo **Ciutat Vella** el distrito con mayor consumo (**21%**). Se observan consumos anómalos en **febrero, marzo y abril** en Ciutat Vella, y en abril en Eixample.  

- **Consumo comercial**: Eixample, Ciutat Vella, Sant Martí y Sants concentran más del **60%** del consumo comercial, con **Eixample** liderando con el **27%**.

- **Impacto de la sequía y medidas aplicadas**: Se observa una caída notable del consumo doméstico en abril de 2023, coincidiendo con la entrada en vigor de medidas excepcionales de ahorro de agua ([fuente](https://www.totbarcelona.cat/es/sociedad/los-hogares-de-barcelona-reducen-el-consumo-agua-en-plena-sequia-438255/)).

> Estas conclusiones corresponden al análisis descriptivo. Para un **diagnóstico más profundo**, se recomienda cruzar con otros datos (climáticos, demográficos, industriales) para asociar posibles causas. De manera preliminar, los patrones observados se pueden relacionar con la aplicación de las medidas de abril 2023.

---

## 👥 Autoría

- **Autora:** Ingrid Tobío Pérez  
- **Mentora:** Alana Oliveri

## 📬 Contacto

- Email: ingrid.tobio@gmail.com  
- GitHub: [@ingridtp](https://github.com/ingridtp)  
- LinkedIn: [Ingrid Tobío Pérez](https://www.linkedin.com/in/ingrid-tobio/)

---

## Licencia y condiciones de uso

### Licencia del repositorio
El código, scripts y documentación de este repositorio están bajo la **Licencia MIT**. Esto permite su uso, copia, modificación y distribución, siempre que se mantenga la atribución original.

### Condiciones de uso de los datos y archivos de Power BI
- Los datasets y el archivo de Power BI ([Analisis_consumo_agua.pbix](analysis/Analisis_consumo_agua.pbix)) **no están cubiertos por la Licencia MIT**, ya que son proporcionados por terceros (Aigües de Barcelona).  
- Estos archivos son **solo para análisis y visualización interna del proyecto**.  
- Se pueden explorar los datos, filtrar y exportar visualizaciones, **respetando la confidencialidad de los datos**.  
- No se permite redistribuir los datos originales ni el archivo de Power BI sin autorización de Aigües de Barcelona.  
- Para más información y consulta de los datos originales, ver [Aigües de Barcelona – Datos Abiertos](https://www.abdatachallenge.cat/).


