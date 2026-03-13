# /*

SQL Analysis Script
Proyecto: AdBoost Analytics – Campaign Performance
Autor: IngAamira

Descripción:
Consultas analíticas para evaluar el rendimiento de campañas
publicitarias en múltiples plataformas.

Tabla base:
campaign_data (consolidated_campaign_data.csv)

Campos utilizados:

* plataforma
* fecha
* campaña
* impresiones
* clics
* visualizaciones_video
* visualizaciones_100
* costo
  ==========================================================
  */

/* ======================================================
CONSULTA 1
CTR promedio por plataforma y por mes
Ordenado de mayor a menor
====================================================== */

SELECT
plataforma,
DATE_TRUNC('month', fecha) AS mes,
AVG(clics * 1.0 / NULLIF(impresiones,0)) AS ctr_promedio
FROM campaign_data
GROUP BY
plataforma,
DATE_TRUNC('month', fecha)
ORDER BY
ctr_promedio DESC;

/* ======================================================
CONSULTA 2
Campaña con mejor CTR en todo el periodo
Se excluyen registros con métricas no representativas
====================================================== */

SELECT
campaña,
plataforma,
SUM(clics) AS total_clics,
SUM(impresiones) AS total_impresiones,
SUM(clics) * 1.0 / NULLIF(SUM(impresiones),0) AS ctr
FROM campaign_data
WHERE
impresiones > 100
AND clics > 10
GROUP BY
campaña,
plataforma
ORDER BY
ctr DESC
LIMIT 1;

/* ======================================================
CONSULTA 3
Plataforma con mejor VCR en todo el periodo
====================================================== */

SELECT
plataforma,
SUM(visualizaciones_100) * 1.0 /
NULLIF(SUM(visualizaciones_video),0) AS vcr
FROM campaign_data
GROUP BY
plataforma
ORDER BY
vcr DESC
LIMIT 1;

/* ======================================================
CONSULTA 4
Tabla agregada por plataforma con métricas de performance
====================================================== */

SELECT
plataforma,

```
SUM(impresiones) AS impresiones_totales,
SUM(clics) AS clics_totales,
SUM(visualizaciones_video) AS visualizaciones_video_totales,

SUM(clics) * 1.0 /
NULLIF(SUM(impresiones),0) AS ctr,

SUM(costo) AS costo_total,

SUM(costo) /
NULLIF(SUM(clics),0) AS cpc,

SUM(costo) /
NULLIF(SUM(impresiones),0) * 1000 AS cpm,

SUM(costo) /
NULLIF(SUM(visualizaciones_video),0) AS cpv,

SUM(visualizaciones_100) * 1.0 /
NULLIF(SUM(visualizaciones_video),0) AS vcr
```

FROM campaign_data
GROUP BY
plataforma
ORDER BY
costo_total DESC;
