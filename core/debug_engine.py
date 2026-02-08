
import asyncio
from core.trinity_core import FormalResonanceEngine

async def debug_trinity():
    print("Initializing engine...")
    engine = FormalResonanceEngine()
    print("Process call...")
    try:
        res = await engine.process("Test message", "GOLD")
        print("Result:", res)
    except Exception as e:
        print("Caught EXCEPTION:", e)
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    asyncio.run(debug_trinity())
