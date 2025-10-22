# Transformación de datos para Finanzas y Riesgo Crediticio

## Columnas seleccionadas para el analisis de finanzas y riesgo crediticio

- id
- age
- job
- marital
- education
- balance
- default
- housing
- loan
- deposit (opcional)

## Ajuste de tipos de datos

- **Numéricas:** age, balance
- **Texto:** job, marital, education
- **Booleanas:** default, housing, loan, deposit

## Columnas calculadas

### AgeGroup
- **Objetivo:** Agrupar clientes en segmentos de edad para analizar riesgo y comportamiento según etapa de vida
- **Rangos:**
  - `0` → "Indeterminado" (edad no registrada)
  - `<18` → "Menor de edad" (edad inválida según política)
  - `18–30` → "Joven"
  - `31–65` → "Adulto"
  - `>65` → "Senior"
- **Consideraciones importantes:**
  - Se incluyen grupos especiales para valores no registrados o inválidos
  - Actualmente no hay registros <18, pero se prevé para futuros datos

### BalanceGroup
- **Objetivo:** Agrupar clientes según el saldo para identificar riesgo financiero
- **Rangos (basados en mediana y percentil 75):**
  - `<0` → "Negativo" (clientes en descubierto, alto riesgo)
  - `0–550` → "Bajo" (hasta la mediana, ~50% de clientes)
  - `551–1.708` → "Medio" (hasta el percentil 75)
  - `>1.708` → "Alto" (clientes financieramente sólidos)
- **Consideraciones importantes:**
  - La media (1.528) > mediana (550) debido a valores extremos; por eso se usan percentiles
