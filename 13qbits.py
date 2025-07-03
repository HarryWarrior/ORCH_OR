# Importar las librerías necesarias
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt
import numpy as np

# =============================================================================
# SIMULACIÓN ORCH-OR: MICROTÚBULO COMPLETO (13 PROTOFILAMENTOS)
# =============================================================================

print("🧠 SIMULACIÓN ORCH-OR - MICROTÚBULO DE 13 QUBITS")
print("=" * 60)
print("Basado en la teoría de Penrose-Hameroff")
print("Cada qubit representa un protofilamento del microtúbulo")
print("=" * 60)

# 1. Crear un circuito cuántico con 13 qubits y 13 bits clásicos
qc = QuantumCircuit(13, 13)

print("\n1️⃣ CONFIGURACIÓN INICIAL:")
print(f"   • Qubits: 13 (representando 13 protofilamentos)")
print(f"   • Bits clásicos: 13 (para mediciones)")

# 2. FASE 1: Superposición inicial (estados de indecisión neuronal)
print("\n2️⃣ FASE 1: SUPERPOSICIÓN CUÁNTICA")
print("   Creando estados de 'indecisión' en los protofilamentos...")

# Aplicar Hadamard a los primeros 8 qubits (procesamiento activo)
for i in range(8):
    qc.h(i)
    print(f"   • H({i}): Protofilamento {i} en superposición")

# 3. FASE 2: Entrelazamiento tipo microtúbulo
print("\n3️⃣ FASE 2: ENTRELAZAMIENTO ESTRUCTURAL")
print("   Creando conexiones entre protofilamentos adyacentes...")

# Entrelazamiento en cadena (como en un microtúbulo real)
for i in range(12):
    qc.cx(i, i+1)
    print(f"   • CNOT({i},{i+1}): Conectando protofilamentos {i}-{i+1}")

# Entrelazamiento cruzado (estabilidad estructural)
print("   Creando conexiones cruzadas para estabilidad...")
qc.cx(0, 6)   # Conexión diametral
qc.cx(1, 7)   # Conexión diametral
qc.cx(2, 8)   # Conexión diametral
print("   • Conexiones diametrales: 0-6, 1-7, 2-8")

# 4. FASE 3: Diferenciación α y β tubulina
print("\n4️⃣ FASE 3: DIFERENCIACIÓN DE TUBULINAS")
print("   Simulando dos tipos de proteínas (α y β tubulina)...")

# α-tubulina (qubits pares) - más estables
for i in range(0, 13, 2):
    qc.rz(0.1, i)  # Pequeña rotación de fase
    if i < 12:
        print(f"   • α-tubulina en posición {i} (estable)")

# β-tubulina (qubits impares) - más dinámicas  
for i in range(1, 13, 2):
    qc.ry(0.2, i)  # Rotación en Y (más dinámica)
    print(f"   • β-tubulina en posición {i} (dinámica)")

# 5. FASE 4: Decoherencia ambiental (ruido térmico a 37°C)
print("\n5️⃣ FASE 4: DECOHERENCIA TÉRMICA")
print("   Simulando efectos del ambiente cerebral caliente...")

# Ruido distribuido por todo el microtúbulo
ruido_positions = [0, 3, 6, 9, 12]  # Distribución espacial
for pos in ruido_positions:
    qc.z(pos)  # Ruido de fase
    print(f"   • Ruido térmico en protofilamento {pos}")

# Ruido de bit-flip en posiciones centrales
qc.x(5)   # Centro del microtúbulo
qc.x(7)   # Centro del microtúbulo
print("   • Ruido de bit-flip en posiciones centrales: 5, 7")

# 6. FASE 5: Reducción Objetiva (colapso de la función de onda)
print("\n6️⃣ FASE 5: REDUCCIÓN OBJETIVA")
print("   Simulando el 'momento consciente' de Penrose...")

# Medición del "nodo central" que inicia el colapso
qc.measure(6, 6)  # Protofilamento central
print("   • Medición en protofilamento central (6)")

# Colapso condicional propagándose
print("   • Propagación del colapso (si está disponible)...")
try:
    with qc.if_test((6, 1)):  # Si el centro colapsa a |1⟩
        qc.x(5)  # Afecta vecinos
        qc.x(7)  # Afecta vecinos
        print("   • Colapso propagado a vecinos 5 y 7")
except:
    print("   • (Colapso condicional no disponible en esta versión)")

# 7. FASE 6: Mediciones en diferentes "bases neurales"
print("\n7️⃣ FASE 6: MEDICIONES NEURALES")
print("   Midiendo en diferentes 'perspectivas' del procesamiento...")

# Base X (procesamiento intuitivo)
intuitive_qubits = [1, 3, 5]
for q in intuitive_qubits:
    qc.h(q)  # Cambio a base X
    qc.measure(q, q)
    print(f"   • Base intuitiva (X): protofilamento {q}")

# Base Y (procesamiento emocional)
qc.ry(np.pi/2, 9)  # Rotación a base Y
qc.measure(9, 9)
print("   • Base emocional (Y): protofilamento 9")

# Base Z (procesamiento lógico) - el resto
logical_qubits = [0, 2, 4, 8, 10, 11, 12]
for q in logical_qubits:
    qc.measure(q, q)
    print(f"   • Base lógica (Z): protofilamento {q}")

# 8. VISUALIZACIÓN Y SIMULACIÓN
print("\n8️⃣ SIMULACIÓN DEL MICROTÚBULO")
print("=" * 40)

# Mostrar el circuito
print("\nEstructura del circuito cuántico:")
try:
    print(qc.draw(fold=-1))
except:
    print("(Circuito muy grande para mostrar - 13 qubits)")

# Simular
print("\nEjecutando simulación...")
simulator = AerSimulator()
job = simulator.run(qc, shots=2048)  # Más shots para mejor estadística
result = job.result()
counts = result.get_counts(qc)

# 9. ANÁLISIS DE RESULTADOS
print("\n9️⃣ ANÁLISIS DE CONSCIENCIA CUÁNTICA")
print("=" * 40)

print(f"\nResultados totales: {len(counts)} patrones diferentes")
print(f"Total de mediciones: {sum(counts.values())}")

# Mostrar los 5 patrones más frecuentes
print("\n🔍 Top 5 patrones más frecuentes:")
sorted_counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)
for i, (pattern, count) in enumerate(sorted_counts[:5]):
    probability = count / sum(counts.values()) * 100
    print(f"   {i+1}. {pattern} → {count} veces ({probability:.1f}%)")

# Métricas de complejidad
total_patterns = len(counts)
max_possible = 2**13
complexity_ratio = total_patterns / max_possible * 100

print(f"\n📊 MÉTRICAS DE CONSCIENCIA:")
print(f"   • Complejidad: {total_patterns}/{max_possible} patrones ({complexity_ratio:.2f}%)")
print(f"   • Entropía cuántica: {'Alta' if total_patterns > 100 else 'Media' if total_patterns > 50 else 'Baja'}")
print(f"   • Coherencia residual: {'Detectada' if total_patterns < 1000 else 'Perdida'}")

# 10. VISUALIZACIÓN
print("\n🔟 VISUALIZACIÓN DE RESULTADOS")
print("Generando histograma...")

plt.figure(figsize=(15, 8))
plot_histogram(counts, figsize=(15, 8))
plt.title("🧠 Orch-OR: Patrones de Consciencia en Microtúbulo (13 Qubits)", fontsize=14)
plt.xlabel("Estados Cuánticos (13 bits)", fontsize=12)
plt.ylabel("Frecuencia de Ocurrencia", fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

print("\n✅ SIMULACIÓN COMPLETADA")
print("=" * 60)
print("🎓 INTERPRETACIÓN ACADÉMICA:")
print("• Cada pico representa un 'estado consciente' posible")
print("• La distribución muestra cómo el cerebro 'elige' entre opciones")
print("• Patrones no aleatorios sugieren procesamiento cuántico")
print("• Complejidad moderada indica balance entre orden y caos")
print("=" * 60)