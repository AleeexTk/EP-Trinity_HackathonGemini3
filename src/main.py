
import sys
import os
import asyncio

# Fix path to include core
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from core.trinity_core import FormalResonanceEngine, TriangleColor
from core.evolution_protocol import run_evolution_demo
from core.vision_monitor import TrinityVisionMonitor

async def main():
    print("""
    ████████████████████████████████████████████████
    █      EVOPYRAMID - TRINITY SEQUENCER v1.0     █
    █      SEC_LEVEL: ONEGA // STATUS: ONLINE      █
    ████████████████████████████████████████████████
    """)
    
    # Initialize Engine
    engine = FormalResonanceEngine()
    
    # Simulating Triad Dialogue
    print("\n[📢] Activating Triad of Evolution...")
    
    # 🟨 GOLD Input
    print("\n--- GOLD TRAILBLAZER INPUT ---")
    res_gold = await engine.process('optimizing logic flow for rapid deployment', "GOLD")
    print(res_gold['result'])
    
    # 🟥 RED Input
    print("\n--- RED PROVOCATEUR INPUT ---")
    res_red = await engine.process('❓ why are we optimizing if the foundation is weak?', "RED")
    print(res_red['result'])
    
    # 🟩 GREEN Input
    print("\n--- GREEN SOUL INPUT ---")
    res_green = await engine.process('#[D123] { "intent": "human_harmony", "value": 100 }', "GREEN")
    print(res_green['result'])
    
    # Vision Demo
    print("\n[👁️] Activating Vision Portal...")
    monitor = TrinityVisionMonitor()
    vision_result = monitor.analyze_stream("mock_image_data")
    
    if "triad" in vision_result:
        print(f"BLACK: {vision_result['triad'].get('black')}")
        print(f"RED: {vision_result['triad'].get('red')}")
        print(f"GOLD: {vision_result['triad'].get('gold')}")
    
    print(f"Consensus: {vision_result['consensus']}")
    print(f"Coherence: {vision_result['coherence_score']}")

    # Evolution Demo
    print("\n[🧬] Running Quantum Evolution Protocol...")
    await run_evolution_demo()
    
    print("\n[🏁] SYSTEM READY FOR HACKATHON SUBMISSION.")

if __name__ == "__main__":
    asyncio.run(main())
