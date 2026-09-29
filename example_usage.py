from client import TrajectoryEvaluator

actual = [{"tool": "sql_query"}, {"tool": "plot_chart"}]
golden = [{"tool": "sql_query"}, {"tool": "plot_chart"}]

eval_res = TrajectoryEvaluator.evaluate_trajectory(actual, golden)
print("Trajectory Evaluation Result:", eval_res)
