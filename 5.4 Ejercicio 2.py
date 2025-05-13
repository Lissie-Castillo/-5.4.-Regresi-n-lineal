import numpy as np
import matplotlib.pyplot as plt

# Datos del experimento: posición (cm) y temperatura (°C)
x = np.array([0, 2, 4, 6, 8])       # Posición en cm
y = np.array([100, 92, 85, 78, 71]) # Temperatura en °C

# Cálculo de los coeficientes de regresión lineal
n = len(x)
sum_x = np.sum(x)
sum_y = np.sum(y)
sum_xy = np.sum(x * y)
sum_x2 = np.sum(x**2)

b = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x**2)
a = (sum_y - b * sum_x) / n

print("Coeficientes de la regresión lineal:")
print(f"a (intercepto) = {a:.4f} °C")
print(f"b (pendiente) = {b:.4f} °C/cm")

# Estimación para x = 5 cm
x_estimado = 5
y_estimado = a + b * x_estimado
print(f"\nTemperatura estimada en x = {x_estimado} cm: {y_estimado:.2f} °C")

# Predicción para graficar
x_vals = np.linspace(min(x), max(x), 100)
y_pred = a + b * x_vals

# Gráfica
plt.figure(figsize=(8,6))
plt.plot(x, y, 'o', label='Datos experimentales')
plt.plot(x_vals, y_pred, '-', color='red', label=f'Regresión lineal: y = {a:.2f} + {b:.2f}x')
plt.axvline(x_estimado, color='gray', linestyle='--', label=f'Estimación en x = {x_estimado} cm')
plt.axhline(y_estimado, color='gray', linestyle='--')
plt.scatter(x_estimado, y_estimado, color='black', zorder=5)
plt.xlabel('Posición (cm)')
plt.ylabel('Temperatura (°C)')
plt.title('Regresión Lineal: Transferencia de Calor')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()