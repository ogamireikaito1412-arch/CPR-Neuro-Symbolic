from datetime import datetime
from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import uuid

from core.core_engine import LearnableCPREngine

# Storage for reasoning results
reasoning_storage = {}

# Initialize engine
cpr_engine = LearnableCPREngine()


def generate_reasoning_id():
    return str(uuid.uuid4())


def get_reasoning_by_id(reasoning_id):
    return reasoning_storage.get(reasoning_id)


class CPRRequestHandler(BaseHTTPRequestHandler):
    
    def _send_json_response(self, data, status=200):
        self.send_response(status)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(data).encode())
    
    def do_GET(self):
        if self.path == '/system/status':
            response = {
                "status": "operational",
                "learning_cycles": cpr_engine.learning_engine.get_learning_stats(),
                "pattern_database": cpr_engine.pattern_matcher.get_database_stats(),
                "performance_metrics": cpr_engine.get_performance_metrics()
            }
            self._send_json_response(response)
        else:
            self._send_json_response({"error": "Not found"}, 404)
    
    def do_POST(self):
        content_length = int(self.headers.get('Content-Length', 0))
        body = self.rfile.read(content_length)
        
        try:
            data = json.loads(body) if body else {}
        except json.JSONDecodeError:
            self._send_json_response({"error": "Invalid JSON"}, 400)
            return
        
        if self.path == '/reasoning/analyze':
            try:
                result = cpr_engine.reasoning_cycle(
                    data.get('input_data', {}),
                    data.get('domain', 'medical'),
                    data.get('context')
                )
                
                reasoning_id = generate_reasoning_id()
                reasoning_storage[reasoning_id] = result
                
                response = {
                    "success": True,
                    "reasoning_id": reasoning_id,
                    "analysis": result,
                    "timestamp": datetime.now().isoformat()
                }
                self._send_json_response(response)
            except Exception as e:
                self._send_json_response({"error": str(e)}, 500)
        
        elif self.path == '/learning/feedback':
            try:
                reasoning_id = data.get('reasoning_id')
                original_reasoning = get_reasoning_by_id(reasoning_id)
                
                if original_reasoning is None:
                    self._send_json_response({"error": "Reasoning not found"}, 404)
                    return
                
                learning_result = cpr_engine.learn_from_outcome(
                    original_reasoning,
                    data.get('actual_outcome', {}),
                    data.get('expert_feedback')
                )
                
                response = {
                    "success": True,
                    "learning_applied": learning_result,
                    "system_improved": True
                }
                self._send_json_response(response)
            except Exception as e:
                self._send_json_response({"error": str(e)}, 500)
        else:
            self._send_json_response({"error": "Not found"}, 404)


def run_server(port=8080):
    server = HTTPServer(('localhost', port), CPRRequestHandler)
    print(f"CPR API Server running on http://localhost:{port}")
    server.serve_forever()


if __name__ == "__main__":
    run_server()
