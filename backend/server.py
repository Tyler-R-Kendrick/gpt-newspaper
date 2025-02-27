from flask import Flask, jsonify, request
from flask_cors import CORS
from backend.langgraph_agent import MasterAgent
from flask import Flask, jsonify, request
from flask_cors import CORS
from backend.langgraph_agent import MasterAgent

# Get your frontend URL (assuming port 5000)
frontend_origin = "https://symmetrical-funicular-9794v7j96745c9744-5000.app.github.dev"

backend_app = Flask(__name__)
CORS(backend_app, 
     origins=[frontend_origin, "*"], 
     supports_credentials=True,
     methods=["GET", "POST", "OPTIONS"],
     allow_headers=["Content-Type", "Authorization"])

@backend_app.route('/', methods=['GET'])
def index():
    return jsonify({"status": "Running"}), 200

@backend_app.route('/generate_newspaper', methods=['POST'])
def generate_newspaper():
    try:
        data = request.json
        master_agent = MasterAgent()
        newspaper = master_agent.run(data["topics"], data["layout"])
        return jsonify({"path": newspaper}), 200
    except Exception as e:
        
        return jsonify({"error": str(e)}), 500    
