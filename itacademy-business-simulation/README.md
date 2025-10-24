# Escenario profesional y roles

El proyecto simula un **entorno empresarial en el sector bancario**, donde el equipo de análisis de datos trabaja para apoyar la toma de decisiones estratégicas sobre clientes, riesgos financieros y marketing.

## Roles del equipo

- **Analista de Finanzas y Riesgo Crediticio**  
  - Ingrid Tobío Pérez - [LinkedIn](https://www.linkedin.com/in/ingrid-tobio/)  
  - Bárbara Junqueira –  [LinkedIn](https://www.linkedin.com/in/junqueirabs/)

- **Analista de Marketing y Comunicación**  
  - Carlos Moreno García – [LinkedIn](https://www.linkedin.com/in/morenogarciacarlos/)  
  - Pau León Ozón – [LinkedIn](https://www.linkedin.com/in/pauleonozon/)  

- **Perfil del Cliente**  
  - Favila Valdés-Bango Martín – [LinkedIn](https://www.linkedin.com/in/favila-vald%C3%A9s-bango-mart%C3%ADn-9ab146271/)
  - Maeloc Valdés Moutinho – [LinkedIn](https://www.linkedin.com/in/maeloc-valdes/)  

---

# Objetivos del proyecto

## Objetivo general

Analizar datos de clientes, marketing y finanzas para **apoyar la toma de decisiones estratégicas** en un entorno bancario, generando insights accionables, dashboards y comunicando hallazgos claros.  

El proyecto se desarrolló abordando una serie de **desafíos estratégicos** que guiaron el análisis y la toma de decisiones.

## Desafíos que guiaron el desarrollo

- **Finanzas y riesgo crediticio:**  
  - ¿Cómo afectan los saldos bajos al riesgo de incumplimiento de crédito? ¿Qué ajustes de política de crédito se recomiendan?  
  - ¿Cómo afectan préstamos e hipotecas al saldo medio y al riesgo de incumplimiento?  
  - ¿Qué umbrales de saldo podrían indicar mayor riesgo de morosidad?  
  - **Aporte destacado:** Construcción de un **score de riesgo financiero** para priorizar estrategias de mitigación de riesgos.

- **Marketing y comunicación:**  
  - ¿Cuál es la relación entre el número de contactos realizados y la tasa de éxito? ¿Cómo optimizar la frecuencia de contacto?  
  - ¿Qué impacto tiene el tipo de contacto (móvil o telefónico) en la tasa de conversión?  
  - ¿Cómo influyen los días de la semana en la efectividad de las campañas? ¿Qué días deberían priorizarse para maximizar resultados?  

- **Perfil del Cliente:**  
  - ¿Qué perfiles demográficos muestran más propensión a contratar productos financieros?  
  - ¿Qué diferencias existen en el comportamiento financiero entre los distintos segmentos demográficos?  
  - ¿Qué combinaciones de características demográficas (edad, nivel educativo, ocupación) son comunes entre clientes que utilizan múltiples productos financieros?  

- **Desafío transversal:**  
  - ¿Cómo debe adaptarse la estrategia del negocio para alinearse con tendencias emergentes y maximizar oportunidades de mercado?  
  - ¿Es necesario ajustar las ofertas actuales o crear nuevas según cambios en comportamiento financiero y competencias a nivel nacional?

---

# Estructura y nomenclatura

## Nomenclatura de archivos

Para mantener consistencia en todo el proyecto, se siguen las siguientes normas:
- **Carpetas:** primera letra en mayúscula, resto en minúscula. Ejemplo: Finance, Marketing, Customer.  
- **Archivos:** todo en minúsculas, usando guiones bajos (_) para separar palabras y extensiones claras.

### Formato general para los archivos:

Todos los archivos deben seguir el patrón: **banca_DD.MM_XX**
  Donde:
  - **DD.MM** → Fecha de inicio del desafío.  
  - **XX** → Descripción concisa del contenido o propósito del archivo.

### Fechas de inicio de los desafíos

| Desafío | Fecha | Patrón de archivo |
|---------|-------|-----------------|
| Desafío 1 | 16/09 | banca_16.09_XX |
| Desafío 2 | 22/09 | banca_22.09_XX |
| Desafío 3 | 06/10 | banca_06.10_XX |
| Desafío 4 | 13/10 | banca_13.10_XX |

### Ejemplos de nombres

- **eda** → Script para Análisis Exploratorio de Datos  
  - Ejemplo: `banca_22.09_eda.ipynb`  
- **data_cleaning** → Script de limpieza y preparación de datasets  
  - Ejemplo: `banca_22.09_data_cleaning.ipynb`  

### Estructura

- **Organización de carpetas:**  
  - Carpetas **generales** (`Data/`, `Results/`, `Scripts/`) contienen trabajo conjunto de todo el equipo.  
  - Carpetas **por roles** (`Analysis/Finance`, `Analysis/Marketing`, `Analysis/Customer`) contienen análisis y resultados específicos de cada área. 

```
Itacademy_business_simulation/
├── Data/                         # Carpeta de datasets originales y procesados (trabajo conjunto)
│
├── Scripts/                      # Scripts de limpieza, transformación y análisis de datos (trabajo conjunto)
│
├── Results/                      # Resultados finales (KPIs y presentaciones)
│   ├── KPIs/                     # Indicadores clave de desempeño
│   └── Presentations/            # Presentaciones de resultados generales
│
├── Analysis/                     # Trabajo de análisis de datos por área (Finance, Marketing, Customer)
│   ├── Finance/
│   │   ├── Diagrams/             # Diagramas y visualizaciones financieras
│   │   ├── Notebooks/            # Notebooks de Python para análisis financiero
│   │   ├── Pbix/                 # Dashboards en Power BI de finanzas y riesgo crediticio
│   │   └── Summaries/            # Resúmenes y construcción del score de riesgo financiero
│   │
│   ├── Marketing/
│   │   ├── Diagrams/             # Diagramas y visualizaciones de marketing
│   │   ├── Notebooks/            # Notebooks de Python para análisis de marketing
│   │   └── Pbix/                 # Dashboards en Power BI de marketing
│   │
│   └── Customer/
│       ├── Animations/           # Animaciones y visualizaciones dinámicas de clientes
│       ├── Data_processed/       # Datos procesados para análisis de clientes
│       ├── Notebooks/            # Notebooks de Python para análisis del perfil de clientes
│       └── Pbix/                 # Dashboards en Power BI del perfil de clientes
│
├── README.md                      # Documentación general del proyecto
└── LICENSE                        # Licencia MIT del proyecto
```
---

# Tecnología utilizada

El proyecto se desarrolló con herramientas orientadas al análisis de datos, visualización y generación de insights en el sector bancario:

- **Python**: para análisis, limpieza de datos y modelado (Pandas, NumPy, Matplotlib, Seaborn).  
- **Power BI**: dashboards de finanzas, marketing y perfil de clientes.  
- **Tableau**: utilizado como herramienta de remplazo donde Power BI no estaba disponible por fallos del servidor.  
- **SQL**: soporte para consultas y preparación de datos .  
- **Jupyter Notebooks**: desarrollo de análisis exploratorio y documentación del flujo de trabajo.

---

# Guía de consulta rápida a carpetas mas relevantes

- Abrir [`Analysis/`](./Analysis/) para revisar trabajo por área (trabajo por roles Finance, Marketing, Customer).  
  - [`Finance/`](./Analysis/Finance/) → Análisis de finanzas y riesgo crediticio. 
    - [`Pbix/`](./Analysis/Finance/Pbix/) → Dashboards en Power BI.   
    - [`Notebooks/`](./Analysis/Finance/Notebooks/) → Notebooks de Python para análisis financiero.
    - [`Summaries/`](./Analysis/Finance/Summaries/) → Construcción del **score de riesgo financiero**, aporte clave para la gestión de riesgos.      
  - [`Marketing/`](./Analysis/Marketing/) → Análisis de marketing y comunicación. 
    - [`Pbix/`](./Analysis/Marketing/Pbix/) → Dashboards en Power BI de marketing. 
    - [`Notebooks/`](./Analysis/Marketing/Notebooks/) → Notebooks de análisis de marketing.  
  - [`Customer/`](./Analysis/Customer/) → Análisis del perfil de cliente. 
    - [`Pbix/`](./Analysis/Customer/Pbix/) → Dashboards en Power BI del perfil de clientes.  
    - [`Notebooks/`](./Analysis/Customer/Notebooks/) → Notebooks de análisis del perfil de clientes.

- Explorar [`Results/`](./Results/) para KPIs y presentaciones finales (trabajo conjunto).  
  - [`KPIs/`](./Results/KPIs/) → Indicadores clave de desempeño.  
  - [`Presentations/`](./Results/Presentations/) → Presentaciones de resultados generales.  
- Revisar [`Scripts/`](./Scripts/) si quieres ejecutar limpieza o transformación de datos (trabajo conjunto).
- Consultar [`Data/`](./Data/) para ver datasets originales y procesados (trabajo conjunto de todo el equipo).

---

## 👥 Autoría

- Ingrid Tobío Pérez – [LinkedIn](https://www.linkedin.com/in/ingrid-tobio/)  
- Bárbara Junqueira – [LinkedIn](https://www.linkedin.com/in/junqueirabs/)
- Carlos Moreno García – [LinkedIn](https://www.linkedin.com/in/morenogarciacarlos/)  
- Pau León Ozón – [LinkedIn](https://www.linkedin.com/in/pauleonozon/)  
- Favila Valdés-Bango Martín – [LinkedIn](https://www.linkedin.com/in/favila-vald%C3%A9s-bango-mart%C3%ADn-9ab146271/)  
- Maeloc Valdés Moutinho – [LinkedIn](https://www.linkedin.com/in/maeloc-valdes/)  

- **Mentora:** Verónica Figueroa – [LinkedIn](https://www.linkedin.com/in/ver%C3%B3nica-figueroa-projectmanager/)

---

# Licencia

Este proyecto se distribuye bajo la licencia **MIT License**.  
Esto permite que cualquier persona pueda usar, copiar, modificar y distribuir el proyecto, siempre citando al autor original.  

Para más detalles, consulta el archivo [`LICENSE`](./LICENSE) en el repositorio.