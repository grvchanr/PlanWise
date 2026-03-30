# PlanWise Architecture – System Design & Intelligence Flow

This document details the modular architecture and decision-making logic behind **PlanWise**, an AI-driven structural intelligence system.

---

## 1. System Overview
PlanWise operates as a deterministic **Structural Intelligence Pipeline**. It transforms raw architectural data (rooms and walls) into an analyzed, material-optimized 3D model. The system is designed to be modular, separating geometric parsing from engineering logic and visualization.

## 2. Data Flow
The data moves through the system in a linear, traceable path:

```text
[Input Layer]      [Processing Layer]       [Intelligence Layer]      [Output Layer]       [Visualization Layer]
  input.json   -->    pipeline.py      -->     materials.py      -->   output.json    -->      Frontend UI
                                       -->     explain.py        -->                        (Plotly / 3D)
```

1.  **Input:** Geometric definitions of rooms and walls.
2.  **Orchestration:** `pipeline.py` sequences the analysis steps.
3.  **Analysis:** Each wall is passed to the Material Engine and Reasoning Engine.
4.  **Serialization:** Results are consolidated into a standardized JSON payload.
5.  **Rendering:** The frontend consumes the JSON to build the interactive 3D scene.

---

## 3. Components Breakdown

### A) Input Layer
*   **Structured Data:** Accepts `input.json` containing room coordinates and wall properties.
*   **Vision Parser (Optional):** Employs OpenCV via `vision_parser.py` to extract these geometries from 2D floor plan images.

### B) Processing Layer (`pipeline.py`)
*   Acts as the **Central Nervous System**.
*   Maps raw wall data to engineering-friendly attributes (e.g., converting "type" to load-bearing booleans).
*   Manages the "Phased Analysis" (Layout → Walls → Analysis → Materials → Final) to support real-time streaming to the UI.

### C) Intelligence Layer
*   **Material Engine (`materials.py`):** Uses a rule-based heuristic to rank materials based on cost-strength tradeoffs.
*   **Reasoning Engine (`explain.py`):** A **Hybrid AI** system. It uses LLMs (Gemini/GPT-4) to generate engineering insights or reverts to a high-fidelity fallback rule-engine if APIs are unavailable.

### D) Output Layer
*   Generates `output.json`, a rich manifest containing:
    *   Optimized material selections.
    *   Risk scores (0-100).
    *   AI-generated engineering justifications.

### E) Visualization Layer
*   **3D Engine:** Uses Plotly's `Mesh3d` to render rooms as cuboids and walls as high-priority structural elements.
*   **UI Architecture:** A modern Glassmorphic dashboard in the `frontend/` folder, served by the Flask server (`server.py`) at `http://localhost:5000`.

---

## 4. Decision Logic
The Material Engine uses a **Ranked Predicate System** to determine the best construction method:

| Condition | Primary Recommendation | Rationale |
| :--- | :--- | :--- |
| **Load-Bearing + Long Span (>5m)** | **RCC / Steel Frame** | Requires high axial strength and deflection control. |
| **Load-Bearing (Normal)** | **RCC / Hollow Block** | Focus on compressive load distribution. |
| **Non-Load Bearing** | **Red Brick / AAC Blocks** | Prioritizes cost-efficiency and thermal insulation. |

**Extensibility:** New materials can be added to the `MATERIAL_DATABASE` by defining their cost, strength, and durability tokens without touching the core logic.

---

## 5. Explainability Layer
PlanWise avoids "black-box" AI. Every recommendation is coupled with an engineering explanation that covers:
*   **The "Why":** Why this specific material was chosen for the given span and load.
*   **Future Risks:** Predicted issues like moisture ingress or thermal expansion.
*   **Mitigation:** Actionable engineering solutions to ensure long-term stability.

---

## 6. UI Architecture
The dashboard is split into three functional zones:
1.  **The Control Sidebar:** For uploading plans and triggering the AI pipeline.
2.  **The 3D Workspace:** An interactive Plotly stage for real-time model interaction.
3.  **The Intelligence Drawer:** A toggleable data panel that displays the granular analysis results for specifically selected walls or rooms.

---

## 7. Integration & Scalability
*   **Separation of Concerns:** The backend logic is completely decoupled from the rendering layer, allowing the engine to be integrated into existing CAD software or mobile apps via API.
*   **Future Evolution:**
    *   **ML Integration:** The current rule-based material selection can be replaced with a Deep Learning model trained on millions of structural data points.
    *   **Cloud Scalability:** `server.py` is designed to be easily containerized (Docker) and deployed to high-performance cloud clusters.
    *   **Real-Time Simulation:** Transitioning from static analysis to real-time Finite Element Analysis (FEA) for dynamic stress testing.

---
*PlanWise Architecture v1.0 — Precision via Probabilistic & Rule-Based Intelligence.*
