import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path


# --------------------------------------------------
# 1. CARGAR EL DATASET
# --------------------------------------------------

archivo = Path(__file__).parent / "datasets_adicionales_fisioterapia.xlsx"

df = pd.read_excel(
    archivo,
    sheet_name="Dataset"
)


# --------------------------------------------------
# 2. REVISAR LOS DIAGNÓSTICOS
# --------------------------------------------------

print("Diagnósticos encontrados:")
print(df["diagnostico"].value_counts())


# --------------------------------------------------
# 3. AGRUPAR LOS DATOS POR DIAGNÓSTICO
# --------------------------------------------------

estadisticas = (
    df.groupby("diagnostico")["dolor_actual"]
    .agg(["mean", "std", "count"])
    .reset_index()
)


# --------------------------------------------------
# 4. CAMBIAR NOMBRES PARA ENTENDERLOS MEJOR
# --------------------------------------------------

estadisticas.columns = [
    "diagnostico",
    "dolor_promedio",
    "desviacion_estandar",
    "cantidad_registros"
]


# --------------------------------------------------
# 5. ORDENAR DE MAYOR A MENOR DOLOR
# --------------------------------------------------

estadisticas = estadisticas.sort_values(
    "dolor_promedio",
    ascending=False
)


# --------------------------------------------------
# 6. MOSTRAR LOS RESULTADOS EN TERMINAL
# --------------------------------------------------

print("\nEstadísticas por diagnóstico:")
print(estadisticas)


# --------------------------------------------------
# 7. CREAR LA FIGURA
# --------------------------------------------------

fig, ax = plt.subplots(
    figsize=(11, 7)
)


# --------------------------------------------------
# 8. CREAR LAS BARRAS
# --------------------------------------------------

ax.bar(
    estadisticas["diagnostico"],
    estadisticas["dolor_promedio"],
    yerr=estadisticas["desviacion_estandar"],
    capsize=5
)


# --------------------------------------------------
# 9. ETIQUETAR LOS EJES
# --------------------------------------------------

ax.set_xlabel(
    "Diagnóstico"
)

ax.set_ylabel(
    "Dolor actual promedio (escala 0–10)"
)

ax.set_title(
    "Dolor promedio registrado por diagnóstico"
)


# --------------------------------------------------
# 10. ESTABLECER ESCALA DEL DOLOR
# --------------------------------------------------

ax.set_ylim(0, 10)


# --------------------------------------------------
# 11. GIRAR LAS ETIQUETAS
# --------------------------------------------------

plt.xticks(
    rotation=35,
    ha="right"
)


# --------------------------------------------------
# 12. AGREGAR CUADRÍCULA
# --------------------------------------------------

ax.grid(
    axis="y",
    alpha=0.25
)


# --------------------------------------------------
# 13. AJUSTAR LA FIGURA
# --------------------------------------------------

plt.tight_layout()


# --------------------------------------------------
# 14. EXPORTAR EN PNG A 300 DPI
# --------------------------------------------------

plt.savefig(
    "T3_dolor_por_diagnostico.png",
    dpi=300,
    bbox_inches="tight"
)


# --------------------------------------------------
# 15. MOSTRAR LA GRÁFICA
# --------------------------------------------------

plt.show()