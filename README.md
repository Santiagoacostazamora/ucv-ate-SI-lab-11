# Laboratorio: Minimax y Poda Alfa-Beta

## Descripción

Este proyecto implementa los algoritmos **Minimax** y **Poda Alfa-Beta** para resolver árboles de decisión simplificados. El jugador MAX busca obtener el valor más alto y el jugador MIN busca reducirlo.

## Objetivo

Comparar el resultado y la eficiencia de Minimax frente a Poda Alfa-Beta, verificando que ambos obtienen la misma decisión final, pero Alfa-Beta puede evaluar menos nodos.

## Estructura del proyecto

```text
alpha-beta-lab/
├── src/
│   ├── __init__.py
│   ├── game_tree.py
│   ├── minimax.py
│   ├── alpha_beta.py
│   └── main.py
├── tests/
│   ├── __init__.py
│   └── test_algorithms.py
├── .github/workflows/ci.yml
├── .gitignore
├── requirements.txt
├── sonar-project.properties
└── README.md
```

## Instalación

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

En Windows PowerShell:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Ejecución

```bash
python -m src.main
```

## Pruebas

```bash
pytest
pytest --cov=src --cov-report=term-missing --cov-report=xml
```

## Comparación esperada

Minimax explora todas las hojas del árbol. Alfa-Beta obtiene el mismo valor, pero poda ramas cuando detecta que ya no pueden modificar la decisión final.

## Preguntas de análisis

### 1. ¿Por qué Alfa-Beta obtiene el mismo resultado que Minimax si no evalúa todo el árbol?

Porque Alfa-Beta no cambia la regla de decisión de Minimax. Solo evita explorar ramas que matemáticamente ya no pueden mejorar el resultado para MAX ni empeorarlo para MIN.

### 2. ¿Qué representa alpha dentro del algoritmo?

Alpha representa el mejor valor que el jugador MAX ha encontrado hasta el momento en el camino actual.

### 3. ¿Qué representa beta dentro del algoritmo?

Beta representa el mejor valor que el jugador MIN ha encontrado hasta el momento en el camino actual.

### 4. ¿En qué casos la Poda Alfa-Beta ahorra más trabajo?

Ahorra más trabajo cuando las mejores jugadas se exploran primero, porque permite cerrar antes las ramas que ya no influyen en la decisión.

### 5. ¿Por qué el orden de exploración afecta el rendimiento?

Porque un buen orden actualiza alpha y beta rápidamente. Cuando esos límites se cruzan, el algoritmo puede podar más ramas.

### 6. ¿Qué pasaría si el rival no juega de manera racional?

Minimax asume que el rival siempre elige la opción óptima para minimizar nuestro beneficio. Si el rival juega mal o de forma aleatoria, la predicción puede ser conservadora y no reflejar el comportamiento real.

### 7. ¿Cómo se relaciona este algoritmo con motores de ajedrez?

Los motores de ajedrez usan ideas similares para buscar jugadas en árboles enormes. Alfa-Beta ayuda a descartar posiciones que no necesitan evaluarse, aunque los motores modernos agregan heurísticas, tablas de transposición y funciones de evaluación avanzadas.

### 8. ¿Qué limitaciones tiene este enfoque frente a redes neuronales o aprendizaje por refuerzo?

Minimax necesita una representación clara del árbol y una función de evaluación. En problemas muy grandes, inciertos o con información incompleta, las redes neuronales y el aprendizaje por refuerzo pueden aprender patrones desde datos o experiencia, aunque también requieren entrenamiento y recursos computacionales.

## GitHub Actions

El archivo `.github/workflows/ci.yml` ejecuta pruebas automáticamente cuando se realiza un `push` o `pull request` hacia las ramas `main` o `develop`.

## SonarCloud

El archivo `sonar-project.properties` queda preparado para análisis de calidad. Para usarlo, se debe configurar `SONAR_TOKEN` en los secretos del repositorio de GitHub y ajustar `sonar.organization` y `sonar.projectKey`.
