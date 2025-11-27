from datetime import datetime


class VectorDatabase:
    def __init__(self):
        self.data = []
    def store(self, experience):
        self.data.append(experience)
        return f'exp_{len(self.data)}'
    def find_similar(self, current_reasoning, max_results):
        return self.data[:max_results]


class OutcomeTracker:
    def record_outcome(self, experience_id, outcome):
        pass


class PatternCorrelator:
    pass


class Experience:
    def __init__(self, experience_id):
        self.experience_id = experience_id


class ExperienceMemory:
    """
    ENHANCED: Stores and retrieves learning experiences efficiently
    """
    
    def __init__(self):
        self.experience_db = VectorDatabase()
        self.outcome_tracker = OutcomeTracker()
        self.pattern_correlator = PatternCorrelator()
    
    def store_experience(self, reasoning_result, outcome, feedback):
        experience = {
            'reasoning_input': reasoning_result.get('input_data'),
            'pattern_matches': reasoning_result.get('pattern_matches'),
            'deviations_detected': reasoning_result.get('deviations'),
            'hypotheses_generated': reasoning_result.get('hypotheses'),
            'actual_outcome': outcome,
            'expert_feedback': feedback,
            'timestamp': datetime.now(),
            'domain': reasoning_result.get('domain'),
            'confidence_metrics': reasoning_result.get('confidence')
        }
        
        experience_id = self.experience_db.store(experience)
        self.outcome_tracker.record_outcome(experience_id, outcome)
        
        return Experience(experience_id)
    
    def find_similar_experiences(self, current_reasoning, max_results=10):
        similar_experiences = self.experience_db.find_similar(
            current_reasoning, max_results
        )
        relevant_experiences = [
            exp for exp in similar_experiences 
            if self.is_relevant_to_current(exp, current_reasoning)
        ]
        return sorted(relevant_experiences, key=lambda x: x.get('outcome_quality', 0), reverse=True)
    
    def is_relevant_to_current(self, exp, current_reasoning):
        return True
    
    def get_confident_experiences(self, min_confidence):
        return [e for e in self.experience_db.data if e.get('confidence_metrics', 0) >= min_confidence]
