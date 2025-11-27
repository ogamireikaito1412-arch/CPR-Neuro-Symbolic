import random
from core.core_engine import LearnableCPREngine


def main():
    print("Initializing LearnableCPREngine...")
    engine = LearnableCPREngine()
    
    domains = ['medical', 'legal', 'financial']
    
    print("\n=== Starting 10-step simulation ===\n")
    
    for step in range(1, 11):
        print(f"--- Step {step} ---")
        
        input_data = {
            'case_id': f'case_{step}',
            'features': [random.random() for _ in range(5)],
            'category': random.choice(['A', 'B', 'C'])
        }
        domain = random.choice(domains)
        
        result = engine.reasoning_cycle(input_data, domain)
        
        print(f"Domain: {domain}")
        print(f"Deviations found: {len(result['deviations'])}")
        print(f"Hypotheses generated: {len(result['hypotheses'])}")
        print(f"Confidence: {result['confidence']:.2f}")
        print()
    
    print("=== Simulation complete ===")


if __name__ == "__main__":
    main()

