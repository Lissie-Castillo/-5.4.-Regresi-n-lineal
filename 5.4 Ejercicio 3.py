import numpy as np
import matplotlib.pyplot as plt

# Datos del experimento: presión (kPa) y caudal (L/min)
x = np.array([50, 70, 90, 110, 130])     # Presión en kPa
y = np.array([15, 21, 27, 33, 39])       # Caudal en L/min

# Cálculo de los coeficientes de regresión lineal
n = len(x)
sum_x = np.sum(x)
sum_y = np.sum(y)
sum_xy = np.sum(x * y)
sum_x2 = np.sum(x**2)

b = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x**2)
a = (sum_y - b * sum_x) / n

print("Coeficientes de la regresión lineal:")
print(f"a (intercepto) = {a:.4f} L/min")
print(f"b (pendiente) = {b:.4f} L/min/kPa")

# Estimación para x = 100 kPa
x_estimado = 100
y_estimado = a + b * x_estimado
print(f"\nCaudal estimado a 100 kPa: {y_estimado:.2f} L/min")

# Predicción para graficar
x_vals = np.linspace(min(x), max(x), 100)
y_pred = a + b * x_vals

# Gráfica
plt.figure(figsize=(8,6))
plt.plot(x, y, 'o', label='Datos experimentales')
plt.plot(x_vals, y_pred, '-', color='red', label=f'Regresión lineal: y = {a:.2f} + {b:.2f}x')
plt.axvline(x_estimado, color='gray', linestyle='--', label=f'Estimación en x = {x_estimado} kPa')
plt.axhline(y_estimado, color='gray', linestyle='--')
plt.scatter(x_estimado, y_estimado, color='black', zorder=5)
plt.xlabel('Presión (kPa)')
plt.ylabel('Caudal (L/min)')
plt.title('Regresión Lineal: Caudal en función de la Presión')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()