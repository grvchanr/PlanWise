# PlanWise – AI Structural Layout & Material Intelligence

PlanWise is an advanced AI-driven structural intelligence system designed to automate architectural analysis, provide smart material recommendations, and visualize structural integrity in interactive 3D environments.

---

## 🏗️ Problem Statement
Traditional structural planning is often manual, time-consuming, and prone to human error. Developing a safe and efficient floor plan requires deep engineering knowledge to select appropriate materials and assess structural risks. Architects and developers frequently lack real-time, explainable insights into how their layout decisions impact material costs and structural stability.

## 💡 Solution
PlanWise bridges the gap between architectural design and structural engineering. By utilizing an autonomous **AI Pipeline**, the system analyzes floor plan geometry, identifies load-bearing elements, recommends high-performance materials, and provides **explainable engineering reasoning**. This is all presented through a premium **Interactive 3D Visualization** dashboard, allowing users to "see" the structural health of their designs before a single brick is laid.

## 🚀 Features
- **Flexible Input:** Upload raw floor plan images for automated vision parsing or provide structured JSON definitions.
- **Automated Structural Analysis:** Intelligent detection of load-bearing walls and architectural room clusters.
- **Smart Material Recommendation Engine:** Context-aware selection of materials (Brick, Concrete, Steel, Timber) based on structural requirements.
- **Explainable Engineering Reasoning:** AI-generated justifications for each structural decision, providing transparency into the recommendation logic.
- **Interactive 3D Visualization:** High-fidelity Plotly-based 3D rendering with orbit controls and dynamic views.
- **Toggleable Analysis Panels:** Detailed data overlays showing risk scores, material properties, and room-by-room analysis.
- **Clean Modern UI:** A premium Glassmorphic dashboard designed for clarity and professional presentation.

## 🛠️ Tech Stack
- **Backend:** Python (Flask, OpenCV for vision parsing, AI logic)
- **Frontend:** HTML5, CSS3 (Vanilla), JavaScript (ES6+)
- **Visualization:** Plotly.js / 3D Mesh Rendering
- **Data Handling:** JSON (Schema-based input/output)
- **Version Control:** Git & GitHub

## 📐 Architecture Overview
The PlanWise system follows a deterministic linear pipeline:
1. **Input:** User provides a Floor Plan Image or Room/Wall JSON.
2. **Processing:** The engine parses geometry and identifies structural constraints.
3. **Recommendation:** The Material Intelligence layer predicts the best-fit materials and risk scores.
4. **Output:** A comprehensive structural report is generated in JSON format.
5. **Visualization:** The report is fed into the 3D engine for interactive rendering.

## 📂 Project Structure
- `app.py`: CLI entry point for running the pipeline locally.
- `pipeline.py`: The central orchestrator that manages data flow between analysis layers.
- `server.py`: Flask backend serving the API and supporting real-time frontend streaming.
- `materials.py`: Logic for material scoring, risk assessment, and recommendation heuristics.
- `explain.py`: Engineering-based explanation generator for AI insights.
- `data.py`: Default mock data and initial configuration definitions.
- `vision_parser.py`: OpenCV-based module for extracting room layouts from 2D images.
- `render_rooms.py`: 3D rendering engine built on Plotly.
- `input.json`: Configuration file for defining room dimensions and wall types.
- `floorplan_3d.html`: The generated interactive 3D visualization page.
- `frontend/`: Contains the dashboard UI (`index.html`, `style.css`, `app.js`).

## ⚙️ How to Run

### 1. Clone the repository
```bash
git clone https://github.com/your-repo/planwise.git
cd planwise
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the Pipeline
To analyze the default floor plan and generate a report:
```bash
python pipeline.py
```

### 4. Open the 3D Visualization
The single-file interactive plot is saved as `floorplan_3d.html`. You can open it directly:
```bash
open floorplan_3d.html
```

### 5. Launch the Dashboard (Recommended)
To run the full **PlanWise Dashboard** with all analytical panels and AI insights:
```bash
python3 server.py
```
Then visit **http://localhost:5000** in your browser.

## 🔮 Future Improvements
- **ML-Based Recommendations:** Training models on historical CAD data for more nuanced material selection.
- **Native CAD Parsing:** Direct support for `.dwg` and `.dxf` file formats.
- **Cloud Deployment:** Seamless synchronization with construction management platforms.
- **Real-Time Updates:** Dynamic re-analysis as users modify floor plans in the UI.

---

## 👥 Contributors
- **[Your Name/Team Name]** - *Initial Work & Architecture*
- *Join the project and start contributing!*

---
*PlanWise: Precision Structural Intelligence, Reimagined.*
