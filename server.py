import os
from flask import Flask, request, jsonify, Response, send_from_directory
from flask_cors import CORS
from pipeline import run_pipeline, generate_phases_stream
from vision_parser import parse_floor_plan
import data

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

app = Flask(__name__, static_folder='frontend')
CORS(app)

# Serve the main dashboard
@app.route('/')
def home():
    return send_from_directory(app.static_folder, 'index.html')

# Serve other static assets (js, css)
@app.route('/<path:path>')
def serve_static(path):
    if path != "" and os.path.exists(app.static_folder + '/' + path):
        return send_from_directory(app.static_folder, path)
    else:
        return send_from_directory(app.static_folder, 'index.html')


@app.route('/analyze', methods=['POST'])
def analyze():
    try:
        if request.is_json:
            req_data = request.get_json()
            if "rooms" not in req_data or "walls" not in req_data:
                return jsonify({"error": "Missing 'rooms' or 'walls' in JSON payload"}), 400
            
            return Response(generate_phases_stream(req_data), mimetype="application/x-ndjson")
            
        elif 'file' in request.files:
            file = request.files['file']
            image_data = file.read()
            
            try:
                parsed_data = parse_floor_plan(image_data)
            except Exception as parse_error:
                print(f"Vision parsing error: {parse_error}")
                parsed_data = {
                    "rooms": data.rooms,
                    "walls": data.walls
                }
            
            return Response(generate_phases_stream(parsed_data), mimetype="application/x-ndjson")
            
        else:
            return jsonify({"error": "Unsupported Content-Type"}), 400
            
    except Exception as e:
        import traceback
        traceback.print_exc()
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    print("Starting PLANWISE Backend Server on port 5000...")
    app.run(port=5000, debug=True)
