# Portafolio de Análisis de Datos – Ingrid Tobío Pérez

Este repositorio reúne proyectos desarrollados por Ingrid Tobío Pérez en el ámbito de Análisis de Datos y Business Intelligence, integrando herramientas como Python, SQL y Power BI para el procesamiento, modelado y visualización de datos en distintos contextos profesionales.

Algunos proyectos fueron desarrollados individualmente, mientras que otros corresponden a trabajo en equipo, donde se indican los roles y responsabilidades específicas.

---

## Proyectos

---

### ToBio Life – Proyecto Final (IT Academy Bootcamp)

**Escenario:** Proyecto final - Especialización (IT Academy Bootcamp - Nivel II)
**Tema:** Análisis de operación piloto de ToBio Life  

**Contexto:**  
Proyecto individual basado en los dos primeros meses de operación de ToBio Life, una marca de productos artesanales y naturales, incluyendo modelado relacional y analítico, procesos ETL y visualización de resultados.

**Descripción:**  
Análisis de datos de operación piloto, construcción de modelos relacionales y analíticos, creación de dashboards en Power BI y generación de reportes
**Duración**: 2 semanas

**Herramientas:** Python | SQL | Power BI | DAX

**Licencia:** Proyecto académico (no comercial)

**Enlaces importantes:**  
- [Carpeta del proyecto](./tobiolife-analytics/)  
- [Dashboards y análisis Power BI](./tobiolife-analytics/PBI/)  
- [Informe final del proyecto](./tobiolife-analytics/Informe/)  
- [Presentación final](./tobiolife-analytics/Presentacion/)  
- [Scripts ETL en Python](./tobiolife-analytics/Data/tobiolife_etl/)

---

### Datató del Saló de l’Ocupació 2025

**Evento:** Datató 2025 – Barcelona Activa & Mobile World Capital  
**Tema:** Consumo de Agua y Presión Hídrica en el Área Metropolitana de Barcelona  

**Contexto:**  
El análisis se desarrolló en el marco del Datató 2025, centrado en el consumo de agua y presión hídrica en el Área Metropolitana de Barcelona, evaluando patrones según tipo de uso y distrito.

**Descripción:**  
Análisis descriptivo del consumo de agua en 2023, clasificando patrones por tipo de uso (industrial, doméstico y comercial) y por distrito.
**Duración**: 10 horas

**Herramientas:** Power BI | Python  

**Licencia:** MIT (excepto datasets externos de Aigües de Barcelona)  

**Enlaces importantes:** 

**Enlaces importantes:**  
- [Carpeta del proyecto](./employment-fair-datathon-2025/)  
- [Dashboards en Power BI](./employment-fair-datathon-2025/analysis/)  

---

### IT Academy Business Simulation – Sector Bancario

**Escenario:** Prácticas profesionales – Simulador empresarial (IT Academy Bootcamp - Nivel III)  
**Tema:** Simulación empresarial aplicada al análisis de datos en el sector financiero  

**Contexto:**  
El proyecto simuló un entorno empresarial real en el sector bancario, permitiendo analizar clientes, riesgos financieros y marketing. Cada integrante del equipo asumió un rol específico para desarrollar análisis y dashboards de apoyo a la toma de decisiones.

**Rol de Ingrid Tobío:** Analista de Finanzas y Riesgo Crediticio (trabajo compartido con Barbara Junqueira)  

**Descripción:**  
Desarrollo de un flujo de análisis que soporta decisiones estratégicas en finanzas, marketing y perfil de clientes, incluyendo score de riesgo financiero, optimización de campañas y segmentación de clientes. 
**Duración:** 4 semanas.

**Enfoques principales:**
- **Finanzas y riesgo crediticio:** Score de riesgo financiero (mi área principal)  
- **Marketing:** Optimización de frecuencia y tipo de contacto (trabajo de equipo)  
- **Clientes:** Segmentación de comportamiento y perfil demográfico (trabajo de equipo)  

**Herramientas:** Python | Power BI | Tableau | SQL | Jupyter Notebooks  

**Licencia:** MIT (excepto datos de terceros, si aplica)  

**Enlaces importantes:**
- [Carpeta del proyecto](./itacademy-business-simulation/)  
- [Presentaciones y reportes finales](./itacademy-business-simulation/Results/Presentations/)  
- [Dashboards y análisis de Finanzas](./itacademy-business-simulation/Analysis/Finance/Pbix/)  
- [Notebooks financieros](./itacademy-business-simulation/Analysis/Finance/Notebooks/)
- [Score de riesgo financiero](./itacademy-business-simulation/Analysis/Finance/Summaries)  

---

## Tecnologías utilizadas

- **Python:** Análisis, limpieza de datos, modelado y ETL (Pandas, NumPy, Matplotlib, Seaborn, SQLAlchemy)  
- **Power BI:** Dashboards y análisis visual interactivo  
- **Tableau:** Visualización complementaria  
- **SQL / MySQL:** Consultas y modelado relacional y analítico  
- **DAX:** Cálculos y métricas personalizadas en Power BI  
- **Jupyter Notebooks:** Análisis exploratorio y documentación de flujo de trabajo  
- **ERD/Diagramas:** Modelado conceptual y lógico de sistemas de datos  

---

## Estructura general del repositorio

```
data-analytics-portfolio/
├── employment-fair-datathon-2025/   # Datató 2025: Análisis del consumo de agua en el Área Metropolitana de Barcelona
│   ├── Data/                         # Datasets originales y procesados
│   ├── analysis/                     # Dashboards y análisis en Power BI
│   └── scripts/                      # Scripts de procesamiento y transformación de datos
│
├── itacademy-business-simulation/    # Simulación empresarial en sector bancario (proyecto grupal)
│   ├── Data/                         # Datasets del proyecto
│   ├── Analysis/                     # Carpetas de análisis por roles: Finance, Marketing, Customer
│   ├── Scripts/                       # Scripts de procesamiento y análisis
│   └── Results/                      # Resultados finales: KPIs y presentaciones
│
├── tobiolife-analytics/              # Proyecto final individual ToBio Life
│   ├── Data/                          # Datos crudos, modelo relacional y analítico, ETL
│   ├── PBI/                           # Dashboards, cálculos DAX y visualizaciones
│   ├── Informe/                        # Informe final del proyecto
│   └── Presentacion/                  # Presentación final
│
├── README.md                          # Documentación principal del portafolio
└── LICENSE                            # Licencia del repositorio
```

---

## Licencia y condiciones de uso

**Licencia general:**  
El código, scripts y documentación de este repositorio están bajo la Licencia MIT, permitiendo su uso, copia, modificación y distribución, siempre que se mantenga la atribución original.

**Condiciones de uso de datos y archivos de Power BI:**  
- Los datasets y archivos Power BI incluidos en los proyectos son solo para análisis y visualización interna del proyecto.  
- No se permite redistribuir los datos originales ni los dashboards sin autorización de los proveedores (por ejemplo, Aigües de Barcelona).  
- Cualquier uso externo debe respetar los términos de los proveedores de datos.  
- Más información sobre los datos originales: [Aigües de Barcelona – Datos Abiertos](https://www.aguasdebarcelona.cat/ca/dades-obertes).

---

## Contacto

**Autora:** Ingrid Tobío Pérez – GitHub: [@ingridtp](https://github.com/ingridtp)  
**Correo:** ingrid.tobio@gmail.com
