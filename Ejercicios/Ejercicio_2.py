import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from scipy.stats import linregress


# --------------------------------------------------
# 1. CARGAR EL DATASET
# --------------------------------------------------

archivo = Path(__file__).parent / "datasets_adicionales_fisioterapia.xlsx"

df = pd.read_excel(
    archivo,
    sheet_name="Dataset"
)


# --------------------------------------------------
# 2. SELECCIONAR LAS DOS VARIABLES
# --------------------------------------------------

rom = df["rom"]
fuerza = df["fuerza_porcentaje"]


# --------------------------------------------------
# 3. CALCULAR LA REGRESIÓN LINEAL
# --------------------------------------------------

regresion = linregress(rom, fuerza)

pendiente = regresion.slope
intercepto = regresion.intercept
r = regresion.rvalue
r_cuadrado = r ** 2


# --------------------------------------------------
# 4. CREAR LOS VALORES PARA LA LÍNEA DE TENDENCIA
# --------------------------------------------------

x_linea = np.linspace(
    rom.min(),
    rom.max(),
    100
)

y_linea = pendiente * x_linea + intercepto


# --------------------------------------------------
# 5. CREAR LA FIGURA
# --------------------------------------------------

fig, ax = plt.subplots(
    figsize=(10, 7)
)


# --------------------------------------------------
# 6. CREAR EL GRÁFICO DE DISPERSIÓN
# --------------------------------------------------

ax.scatter(
    rom,
    fuerza,
    alpha=0.5,
    label="Registros de sesiones"
)


# --------------------------------------------------
# 7. AGREGAR LA LÍNEA DE TENDENCIA
# --------------------------------------------------

ax.plot(
    x_linea,
    y_linea,
    linewidth=2,
    label="Tendencia lineal"
)


# --------------------------------------------------
# 8. MOSTRAR ECUACIÓN Y R²
# --------------------------------------------------

texto = (
    f"y = {pendiente:.3f}x + {intercepto:.2f}\n"
    f"R² = {r_cuadrado:.3f}"
)

ax.text(
    0.05,
    0.95,
    texto,
    transform=ax.transAxes,
    verticalalignment="top",
    bbox=dict(
        boxstyle="round",
        alpha=0.8
    )
)


# --------------------------------------------------
# 9. ETIQUETAR LA GRÁFICA
# --------------------------------------------------

ax.set_xlabel(
    "Rango de movimiento (ROM)"
)

ax.set_ylabel(
    "Fuerza muscular (%)"
)

ax.set_title(
    "Relación entre rango de movimiento y fuerza muscular"
)

ax.legend()

ax.grid(
    alpha=0.25
)


# --------------------------------------------------
# 10. AJUSTAR LA FIGURA
# --------------------------------------------------

plt.tight_layout()


# --------------------------------------------------
# 11. EXPORTAR EN PNG A 300 DPI
# --------------------------------------------------

plt.savefig(
    "T2_ROM_vs_fuerza.png",
    dpi=300,
    bbox_inches="tight"
)


# --------------------------------------------------
# 12. MOSTRAR LA GRÁFICA
# --------------------------------------------------

plt.show()