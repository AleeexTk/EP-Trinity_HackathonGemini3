
import os
import json
import time
from typing import Dict, Any, Optional
from datetime import datetime

# Try to import generative AI, handle if missing
try:
    import google.generativeai as genai
    from PIL import Image
    HAS_GENAI = True
except ImportError:
    HAS_GENAI = False
    print("⚠️ module 'google.generativeai' or 'PIL' not found. Install with: pip install google-generativeai pillow")

class TrinityVisionMonitor:
    """
    Trinity Vision Monitor - The 'Killer Feature'
    Real-time visual analysis using Gemini 1.5 Flash with Trinity Triad Consensus.
    """
    
    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or os.getenv("GEMINI_API_KEY")
        self.model = None
        
        if HAS_GENAI and self.api_key:
            try:
                genai.configure(api_key=self.api_key)
                # Using Gemini 1.5 Flash for low latency
                self.model = genai.GenerativeModel('gemini-1.5-flash')
                print("👁️ Trinity Vision Monitor: ONLINE (Gemini 1.5 Flash)")
            except Exception as e:
                print(f"❌ Trinity Vision Monitor Init Failed: {e}")
        else:
            mode = "SIMULATION" if not HAS_GENAI else "MISSING_KEY"
            print(f"⚠️ Trinity Vision Monitor: {mode} MODE")

    def analyze_stream(self, image_source: Any) -> Dict[str, Any]:
        """
        Analyzes a visual input (file path, PIL Image, or screen region).
        """
        start_time = time.time()
        
        # 1. Image Pre-processing
        image = self._load_image(image_source)
        if not image:
            return {"error": "Invalid image source", "coherence": 0.0}

        # 2. Construct the Trinity Triad Prompt
        prompt = self._get_triad_prompt()

        # 3. Inference (Real or Simulated)
        if self.model:
            try:
                response = self.model.generate_content([prompt, image])
                result = self._parse_response(response.text)
            except Exception as e:
                return {"error": str(e), "coherence": 0.0}
        else:
            result = self._simulate_inference()

        # 4. Metabolic Processing
        latency = round((time.time() - start_time) * 1000, 2)
        result["metadata"] = {
            "latency_ms": latency,
            "model": "gemini-1.5-flash" if self.model else "simulation",
            "timestamp": datetime.now().isoformat()
        }
        
        return result

    def _load_image(self, source: Any):
        if not HAS_GENAI: return "dummy_image"
        
        try:
            if isinstance(source, str):
                if os.path.exists(source):
                    return Image.open(source)
                return source # Return string as mock data
            elif isinstance(source, Image.Image):
                return source
            return None
        except Exception:
            return source if isinstance(source, str) else None


    def _get_triad_prompt(self) -> str:
        return """
        ACT AS THE TRINITY CORE (Cognitive Middleware).
        Analyze this visual input from a real-time environment (Game/Web/Interface).
        
        Execute a 3-way internal dialogue to determine the best course of action:
        
        🖤 BLACK (Strategist):
        - Scan for threats, critical metrics, and tactical data.
        - Tone: Cold, objective, imperative.
        
        🟥 RED (Provocateur):
        - Look for traps, hidden risks, or anomalies.
        - Tone: Skeptical, aggressive, questioning.
        
        🟨 GOLD (Trailblazer):
        - Synthesize data into an optimal path/solution.
        - Tone: Constructive, algorithmic, solution-oriented.
        
        Output MUST be valid JSON:
        {
            "triad": {
                "black": "...",
                "red": "...",
                "gold": "..."
            },
            "consensus": "Final executable directive",
            "coherence_score": 0.95
        }
        """

    def _parse_response(self, text: str) -> Dict:
        # Basic JSON extraction
        try:
            start = text.find('{')
            end = text.rfind('}') + 1
            if start != -1 and end != -1:
                return json.loads(text[start:end])
        except Exception:
            pass
        
        # Fallback if JSON fails
        return {
            "triad": {"raw": text},
            "consensus": "Parsing failed, raw output preserved.",
            "coherence_score": 0.5
        }

    def _simulate_inference(self) -> Dict:
        """Fallback for demo/testing without API key"""
        time.sleep(0.5) # Simulate latency
        return {
            "triad": {
                "black": "Visual input unavailable. Running heuristic scans.",
                "red": "Is this a blindfold test? Where is the data?",
                "gold": "Initiating standard protocol sequence 01."
            },
            "consensus": "Awaiting visual uplink.",
            "coherence_score": 1.0
        }

if __name__ == "__main__":
    # Test run
    monitor = TrinityVisionMonitor()
    print(json.dumps(monitor.analyze_stream("test.jpg"), indent=2, ensure_ascii=False))
