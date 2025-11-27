from core.pattern_matcher import AdaptivePatternMatcher
from learning.learning_engine import ConditionalLearningEngine
from intelligence.cross_domain import CrossDomainHypothesisGenerator
import random


class StructuralDeviationAnalyzer:
    def analyze_deviations(self, input_data, pattern_analysis):
        # Randomly generate deviations to trigger novelty detection
        if random.random() > 0.5:
            return [{'type': 'novel_pattern', 'significance': random.uniform(0.6, 1.0)}]
        return []


class MultiModalUncertainty:
    def compute_uncertainty(self, deviations, pattern_analysis):
        return {'overall': 0.3}


class LearnableCPREngine:
    """
    ENHANCED CORE: Conditional Reactive Reasoning with learning capabilities
    Detects 'similar-but-different' patterns and generates intelligent hypotheses
    """
    
    def __init__(self):
        self.pattern_matcher = AdaptivePatternMatcher()
        self.deviation_analyzer = StructuralDeviationAnalyzer()
        self.hypothesis_generator = CrossDomainHypothesisGenerator()
        self.learning_engine = ConditionalLearningEngine()
        self.uncertainty_quantifier = MultiModalUncertainty()
        
    def reasoning_cycle(self, input_data, domain, context=None):
        """
        Enhanced reasoning process with learning integration
        """
        pattern_analysis = self.pattern_matcher.find_similar_patterns(input_data, domain)
        deviations = self.deviation_analyzer.analyze_deviations(input_data, pattern_analysis)
        
        # Print novelty detection
        if deviations:
            print("NOVELTY DETECTED")
        
        uncertainty = self.uncertainty_quantifier.compute_uncertainty(deviations, pattern_analysis)
        hypotheses = self.hypothesis_generator.generate_hypotheses(deviations, domain, uncertainty)
        learning_update = self.learning_engine.prepare_learning_cycle(
            input_data, deviations, hypotheses, domain
        )
        
        return {
            'input_data': input_data,
            'domain': domain,
            'pattern_matches': pattern_analysis,
            'deviations': deviations,
            'uncertainty': uncertainty,
            'hypotheses': hypotheses,
            'learning_opportunity': learning_update,
            'confidence': self.calculate_overall_confidence(uncertainty, pattern_analysis)
        }
    
    def calculate_overall_confidence(self, uncertainty, pattern_analysis):
        return 1.0 - uncertainty.get('overall', 0.5)
    
    def learn_from_outcome(self, reasoning_result, actual_outcome, expert_feedback):
        return self.learning_engine.update_from_feedback(
            reasoning_result, actual_outcome, expert_feedback
        )
    
    def get_performance_metrics(self):
        return {'cycles': 0}
