# Importar las librerías necesarias
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

# 1. Crear un circuito cuántico con 5 qubits y 5 bits clásicos
qc = QuantumCircuit(5, 5)

# 2. Aplicar compuertas Hadamard para superposición
qc.h(0)  # Superposición en q0
qc.h(1)  # Superposición en q1
qc.h(2)  # Superposición en q2

# 3. Entrelazamiento entre qubits
qc.cx(0, 1)  # Entrelazamiento entre q0 y q1
qc.cx(1, 2)  # Entrelazamiento entre q1 y q2
qc.cx(2, 3)  # Entrelazamiento entre q2 y q3
qc.cx(3, 4)  # Entrelazamiento entre q3 y q4

# 4. Simulación de decoherencia (ruido)
qc.z(0)  # Ruido de fase en q0
qc.x(1)  # Error de bit flip en q1
qc.y(2)  # Ruido combinado en q2

# 5. Simulación del colapso de la función de onda
# Medición condicional basada en un umbral
qc.measure(0, 0)  # Medir q0 y almacenar el resultado en c[0]
with qc.if_test((0, 1)):  # Si c[0] == 1
    qc.x(1)  # Aplicar X en q1

# 6. Mediciones en diferentes bases
qc.h(3)  # Cambio a la base X para q3
qc.measure(3, 3)  # Medición en la base X para q3

qc.h(4)  # Cambio a la base X para q4
qc.measure(4, 4)  # Medición en la base X para q4

# 7. Mediciones estándar en la base Z
qc.measure(1, 1)  # Medición en la base Z para q1
qc.measure(2, 2)  # Medición en la base Z para q2

# 8. Visualizar el circuito
print("Circuito cuántico:")
print(qc.draw())

# 9. Simular el circuito
simulator = AerSimulator()  # Usar AerSimulator
job = simulator.run(qc, shots=1024)
result = job.result()
counts = result.get_counts(qc)

# 10. Obtener y visualizar los resultados
print("\nResultados de la medición:")
print(counts)

# Graficar el histograma de resultados
plot_histogram(counts)
plt.title("Simulación Cuántica de Conciencia")
plt.show()