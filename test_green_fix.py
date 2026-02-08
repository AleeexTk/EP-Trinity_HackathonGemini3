
import asyncio
import os
import sys

# Fix path to include core
sys.path.append(os.path.join(os.path.dirname(__file__), '.'))
from core.trinity_core import FormalResonanceEngine

async def test_green_fix():
    engine = FormalResonanceEngine()
    # This should have been blocked before the fix
    result = await engine.process('#[D123] { "intent": "human_harmony", "value": 100 }', "GREEN")
    print(f"Status: {result['status']}")
    print(f"Result: {result['result']}")
    if result['status'] == 'success':
        print("✅ GREEN FIX VERIFIED: JSON structural characters are now allowed.")
    else:
        print("❌ GREEN FIX FAILED: Still blocked.")
        print(f"Violations: {result.get('violations')}")

if __name__ == "__main__":
    asyncio.run(test_green_fix())
