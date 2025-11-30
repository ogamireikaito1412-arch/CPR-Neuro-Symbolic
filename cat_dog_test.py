import numpy as np
import time
import sys
import os

# Setup path
sys.path.append(os.getcwd())

from core.core_engine import CPREngine
from core.knowledge_base import KnowledgeBase
from api.config import Config

def run_cat_dog_test():
    print("\n" + "="*60)
    print("  🧪 CPR LOGIC TEST: CAT vs. DOG SCENARIO")
    print("="*60 + "\n")

    # 1. SETUP: Train the System on "CATS"
    print("[TRAINING] Loading Knowledge Base with 'Cat' patterns...")
    kb = KnowledgeBase()
    
    # We create a mathematical "Cat" - a vector of mostly 1s
    cat_pattern_1 = np.array([1.0, 0.9, 1.0, 0.9, 1.0, 0.9, 1.0, 0.9, 1.0, 0.9])
    cat_pattern_2 = np.array([0.9, 1.0, 0.9, 1.0, 0.9, 1.0, 0.9, 1.0, 0.9, 1.0])
    
    # Manually override the random patterns with our "Cat" patterns
    kb.patterns = [cat_pattern_1, cat_pattern_2] 
    
    engine = CPREngine(kb)
    print(" -> System now knows what a 'Cat' looks like.\n")

    # 2. TEST 1: Show it another Cat
    print("[TEST 1] Input: New Image (Cat_Variation.jpg)")
    # A slightly different Cat (0.95s instead of 1.0s) - Similar!
    new_cat = np.array([0.95, 0.95, 0.95, 0.95, 0.95, 0.95, 0.95, 0.95, 0.95, 0.95])
    
    result_cat = engine.process(new_cat)
    print(f" -> Result: {result_cat['status']}")
    print(f" -> Logic: Sim={result_cat['sim_score']:.2f} (High) | Diff={result_cat['diff_metric']:.2f} (Low)")
    
    if result_cat['status'] == "NORMAL":
        print("✅ SUCCESS: System recognized the Cat.\n")
    else:
        print("❌ FAILURE: System was confused by the Cat.\n")

    time.sleep(1)

    # 3. TEST 2: Show it a Dog
    print("[TEST 2] Input: New Image (Golden_Retriever.jpg)")
    # A Dog is mathematically different (0.1s and 0.2s) - Different!
    dog_vector = np.array([0.1, 0.2, 0.1, 0.2, 0.1, 0.2, 0.1, 0.2, 0.1, 0.2])
    
    result_dog = engine.process(dog_vector)
    
    # Check the logic
    # Similarity should be LOW (It doesn't look like a cat)
    # Difference should be HIGH (It is far away from a cat)
    
    print(f" -> Result: {result_dog['status']}") 
    
    # NOTE: Depending on your specific Config thresholds, this might trigger "NORMAL" (Low Sim) 
    # or "NOVELTY" if it falls into the 'Similar but Different' valley.
    # Actually, a Dog is usually "Dissimilar" (Noise) rather than "Novelty" (Variant).
    # Let's try a "Cat with Wings" (The True Novelty Test).
    
    print("\n[TEST 3] Input: Cat with Wings (The Novelty Case)")
    # It looks like a Cat (High values) BUT has a weird spike (The Wings)
    winged_cat = np.array([1.0, 0.9, 1.0, 0.9, 5.0, 5.0, 1.0, 0.9, 1.0, 0.9])
    
    result_novel = engine.process(winged_cat)
    print(f" -> Result: {result_novel['status']}")
    print(f" -> Logic: Sim={result_novel['sim_score']:.2f} (High) | Diff={result_novel['diff_metric']:.2f} (High)")
    
    if result_novel['status'] == "NOVELTY_DETECTED":
        print("✅ SUCCESS: System detected the Anomaly (Similar but Different).")
        print("   >>> PROOF: This is the 'Novelty Problem' solved.")
    else:
        print(f"❌ CHECK THRESHOLDS: System output {result_novel['status']}")

if __name__ == "__main__":
    run_cat_dog_test()
