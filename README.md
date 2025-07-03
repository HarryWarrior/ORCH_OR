# 🧠 Simulación Cuántica de la Teoría Orch-OR: Microtúbulos Neuronales

## 📋 Descripción

Este repositorio implementa una simulación computacional de la teoría **Orchestrated Objective Reduction (Orch-OR)** propuesta por Penrose y Hameroff, modelando procesos cuánticos en microtúbulos neuronales mediante circuitos cuánticos de 13 qubits.

La simulación reproduce:
- 🔗 **Entrelazamiento cuántico** entre protofilamentos
- 🌀 **Superposición cuántica** en estados neurales
- 🧬 **Diferenciación α/β tubulina** 
- 🌡️ **Decoherencia térmica** a condiciones fisiológicas
- ⚡ **Reducción objetiva** y colapso de función de onda

## 🛠️ Instalación

### Requisitos del Sistema
- Python 3.8 o superior
- pip package manager

### 1. Clonar el Repositorio
```bash
git clone https://github.com/TuUsuario/Microtubule-Orch-OR-Simulation.git
cd Microtubule-Orch-OR-Simulation
```

### 2. Instalar Dependencias
```bash
pip install -r requirements.txt
```

### 3. Verificar Instalación
```bash
python --version
python -c "import qiskit; print('Qiskit instalado correctamente')"
```

## 📦 Archivos requirements.txt

El archivo `requirements.txt` incluye todas las dependencias necesarias:

```
qiskit>=0.45.0
qiskit-aer>=0.13.0
matplotlib>=3.7.0
numpy>=1.24.0
scipy>=1.10.0
jupyter>=1.0.0
```

## 🚀 Ejecución

### Simulación Principal (13 Qubits)
```bash
python microtubule_13qubits.py
```

### Simulación Básica (5 Qubits)
```bash
python circuito_5qubits.py
```

## 📊 Códigos de Visualización

Este repositorio incluye **dos sistemas de visualización cuántica**:

### 1. 🌐 Visualizaciones Básicas
**Archivo:** `basic_visualizations.py`
- Histogramas de distribución de estados
- Métricas de complejidad cuántica
- Análisis estadístico de resultados

### 2. 🔬 Visualizaciones Avanzadas
**Archivo:** `advanced_quantum_visualizations.py`
- 🌀 **Esferas de Bloch** para estados individuales
- 🪐 **Q-Sphere** del espacio de Hilbert
- 🏙️ **City Plot** de paisajes cuánticos
- ⏱️ **Evolución temporal** del sistema
- 🔗 **Análisis de entrelazamiento** cuantitativo

```bash
# Ejecutar visualizaciones básicas
python basic_visualizations.py

# Ejecutar visualizaciones avanzadas
python advanced_quantum_visualizations.py
```

## 🔗 Repositorio Relacionado

Para obtener implementaciones adicionales y códigos complementarios, visite nuestro repositorio asociado:

**🔗 [TheonlyqueenAC/Microtubule_Simulation](https://github.com/TheonlyqueenAC/Microtubule_Simulation)**

Este repositorio contiene:
- Implementaciones alternativas de la simulación
- Códigos de análisis complementarios
- Documentación técnica extendida
- Datasets de resultados experimentales

### Descargar Repositorio Complementario
```bash
git clone https://github.com/TheonlyqueenAC/Microtubule_Simulation.git
```

## 📈 Resultados Esperados

La simulación genera:
- **175 patrones cuánticos distintos** de 8,192 posibles (2.14% del espacio de Hilbert)
- **Estados preferenciales** con probabilidades 1.2-1.7%
- **Métricas de complejidad** cuantificables
- **Visualizaciones profesionales** para análisis académico

### Ejemplo de Output
```
🧠 SIMULACIÓN ORCH-OR - MICROTÚBULO DE 13 QUBITS
========================================
Resultados totales: 175 patrones diferentes
Top 5 patrones más frecuentes:
   1. 0000100011100 → 34 veces (1.7%)
   2. 0000000001010 → 30 veces (1.5%)
   3. 1111100011000 → 27 veces (1.3%)
   ...
Complejidad: 175/8192 patrones (2.14%)
Coherencia residual: Detectada ✅
```

## 🎓 Uso Académico

### Estructura de Archivos
```
├── src/
│   ├── microtubule_13qubits.py         # Simulación principal
│   ├── circuito_5qubits.py            # Simulación básica
│   ├── basic_visualizations.py         # Visualizaciones estándar
│   └── advanced_quantum_visualizations.py  # Visualizaciones avanzadas
├── docs/
│   ├── latex_sections.tex             # Secciones LaTeX
│   └── referencias.bib                 # Referencias bibliográficas
├── results/
│   └── sample_outputs/                 # Resultados de ejemplo
├── requirements.txt                    # Dependencias
└── README.md                          # Este archivo
```

### Para Investigadores
- Modifique parámetros en la sección de configuración
- Exporte resultados en formato CSV para análisis estadístico
- Use visualizaciones para presentaciones académicas
- Cite apropiadamente usando las referencias BibTeX incluidas

## 🐛 Solución de Problemas

### Error: ModuleNotFoundError
```bash
pip install --upgrade qiskit qiskit-aer
```

### Error: Operaciones condicionales
Si encuentra errores con `c_if`, su versión de Qiskit usa sintaxis moderna. El código incluye manejo automático de compatibilidad.

### Error: Glyph missing from font
Para resolver warnings de fuentes en matplotlib:
```bash
pip install --upgrade matplotlib
```

## 📚 Referencias

- Penrose, R. & Hameroff, S. (1996). "Orchestrated reduction of quantum coherence in brain microtubules"
- Hameroff, S. & Penrose, R. (2014). "Consciousness in the universe: A review of the 'Orch OR' theory"
- Bandyopadhyay, A. et al. (2014). "Discovery of quantum vibrations in 'microtubules'"

## 📄 Licencia

MIT License - Ver archivo `LICENSE` para detalles.

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor:
1. Fork el repositorio
2. Cree una rama para su feature (`git checkout -b feature/nueva-visualizacion`)
3. Commit sus cambios (`git commit -am 'Agregar nueva visualización'`)
4. Push a la rama (`git push origin feature/nueva-visualizacion`)
5. Abra un Pull Request

## 📧 Contacto

Para preguntas técnicas o colaboraciones académicas, abra un issue en GitHub o contacte a los mantenedores del proyecto.

---

**⭐ Si este proyecto le resulta útil para su investigación, considere darle una estrella y citar apropiadamente en sus publicaciones académicas.**

## 🏷️ Tags

`quantum-computing` `neuroscience` `consciousness` `orch-or` `microtubules` `qiskit` `quantum-simulation` `penrose-hameroff` `quantum-biology` `computational-neuroscience`
