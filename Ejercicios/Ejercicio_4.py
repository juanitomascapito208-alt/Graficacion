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
# 2. CALCULAR EL DOLOR PROMEDIO POR SESIÓN
# --------------------------------------------------

evolucion = (
    df.groupby("numero_sesion")["dolor_actual"]
    .mean()
    .reset_index()
)


# --------------------------------------------------
# 3. ORDENAR LAS SESIONES
# --------------------------------------------------

evolucion = evolucion.sort_values(
    "numero_sesion"
)


# --------------------------------------------------
# 4. MOSTRAR LOS RESULTADOS EN TERMINAL
# --------------------------------------------------

print("Dolor promedio por número de sesión:")
print(evolucion)


# --------------------------------------------------
# 5. CREAR LA FIGURA
# --------------------------------------------------

fig, ax = plt.subplots(
    figsize=(10, 6)
)


# --------------------------------------------------
# 6. CREAR LA LÍNEA DE EVOLUCIÓN
# --------------------------------------------------

ax.plot(
    evolucion["numero_sesion"],
    evolucion["dolor_actual"],
    marker="o",
    linewidth=2,
    label="Dolor promedio"
)


# --------------------------------------------------
# 7. RELLENAR EL ÁREA
# --------------------------------------------------

ax.fill_between(
    evolucion["numero_sesion"],
    evolucion["dolor_actual"],
    0,
    alpha=0.3
)


# --------------------------------------------------
# 8. ETIQUETAR LOS EJES
# --------------------------------------------------

ax.set_xlabel(
    "Número de sesión"
)

ax.set_ylabel(
    "Dolor actual promedio (escala 0–10)"
)

ax.set_title(
    "Evolución del dolor promedio a lo largo de las sesiones"
)


# --------------------------------------------------
# 9. FIJAR LA ESCALA DEL DOLOR
# --------------------------------------------------

ax.set_ylim(0, 10)


# --------------------------------------------------
# 10. MOSTRAR LAS SESIONES EN EL EJE X
# --------------------------------------------------

ax.set_xticks(
    evolucion["numero_sesion"]
)


# --------------------------------------------------
# 11. AGREGAR CUADRÍCULA Y LEYENDA
# --------------------------------------------------

ax.grid(
    axis="y",
    alpha=0.25
)

ax.legend()


# --------------------------------------------------
# 12. AJUSTAR LA FIGURA
# --------------------------------------------------

plt.tight_layout()


# --------------------------------------------------
# 13. EXPORTAR A 300 DPI
# --------------------------------------------------

plt.savefig(
    "T4_evolucion_dolor.png",
    dpi=300,
    bbox_inches="tight"
)


# --------------------------------------------------
# 14. MOSTRAR LA GRÁFICA
# --------------------------------------------------

plt.show()