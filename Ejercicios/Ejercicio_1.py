import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

# --------------------------------------------------
# 1. CARGAR EL DATASET
# --------------------------------------------------

archivo = Path(__file__).parent / "datasets_adicionales_fisioterapia.xlsx"

df = pd.read_excel(archivo, sheet_name="Dataset")


# --------------------------------------------------
# 2. REVISAR LOS DATOS
# --------------------------------------------------

print("Primeras filas del dataset:")
print(df.head())

print("\nDimensiones del dataset:")
print(df.shape)

print("\nRango de dolor actual:")
print("Mínimo:", df["dolor_actual"].min())
print("Máximo:", df["dolor_actual"].max())

print("\nValores faltantes:")
print(
    df[
        ["id_paciente", "numero_sesion", "dolor_actual"]
    ].isnull().sum()
)


# --------------------------------------------------
# 3. CREAR LA MATRIZ PARA EL MAPA 2D
# --------------------------------------------------

mapa_dolor = df.pivot_table(
    index="id_paciente",
    columns="numero_sesion",
    values="dolor_actual",
    aggfunc="mean"
)


# --------------------------------------------------
# 4. CREAR LA FIGURA
# --------------------------------------------------

fig, ax = plt.subplots(figsize=(10, 8))

imagen = ax.imshow(
    mapa_dolor,
    aspect="auto",
    cmap="viridis",
    vmin=0,
    vmax=10
)


# --------------------------------------------------
# 5. BARRA DE COLOR
# --------------------------------------------------

cbar = fig.colorbar(imagen, ax=ax)

cbar.set_label(
    "Dolor actual (escala 0–10)"
)


# --------------------------------------------------
# 6. ETIQUETAS
# --------------------------------------------------

ax.set_xlabel("Número de sesión")
ax.set_ylabel("Paciente")

ax.set_xticks(
    range(len(mapa_dolor.columns))
)

ax.set_xticklabels(
    mapa_dolor.columns
)

ax.set_title(
    "Evolución del dolor de los pacientes por sesión"
)


# --------------------------------------------------
# 7. AJUSTAR LA FIGURA
# --------------------------------------------------

plt.tight_layout()


# --------------------------------------------------
# 8. EXPORTAR
# --------------------------------------------------

plt.savefig(
    "T1_mapa_dolor_150dpi.png",
    dpi=150,
    bbox_inches="tight"
)

plt.savefig(
    "T1_mapa_dolor_300dpi.png",
    dpi=300,
    bbox_inches="tight"
)


# --------------------------------------------------
# 9. MOSTRAR EN PANTALLA
# --------------------------------------------------

plt.show()