"""Agent Trajectory Pass/Fail Evaluator.
100% Python Standard Library.
"""

class TrajectoryEvaluator:
    """Evaluates agent execution step trajectories against target golden sequences."""
    @staticmethod
    def evaluate_trajectory(actual_steps, expected_steps):
        actual_tools = [s.get("tool") for s in actual_steps if "tool" in s]
        expected_tools = [s.get("tool") for s in expected_steps if "tool" in s]

        match_count = 0
        min_len = min(len(actual_tools), len(expected_tools))
        for i in range(min_len):
            if actual_tools[i] == expected_tools[i]:
                match_count += 1

        precision = match_count / max(len(actual_tools), 1)
        recall = match_count / max(len(expected_tools), 1)
        f1 = (2 * precision * recall) / max((precision + recall), 1e-6)

        return {
            "passed": actual_tools == expected_tools,
            "precision": round(precision, 4),
            "recall": round(recall, 4),
            "f1_score": round(f1, 4),
            "actual_tools": actual_tools,
            "expected_tools": expected_tools
        }
