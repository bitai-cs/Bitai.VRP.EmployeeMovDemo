import argparse
import json
import os
from dataclasses import asdict

from config import load_settings
from problem import build_solver_input
from reporting import ensure_output_dir, write_all_outputs
from scenario import build_scenario
from solver import HAS_SOLUTION_STATUSES, solve_vrp

SOLVER_INPUT_JSON_FILENAME = "solver_input.json"


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Resolve a VRP demo from a parameter file.")
    parser.add_argument(
        "--env-file",
        default=".env",
        help="Path to the scenario configuration file (default: .env).",
    )
    parser.add_argument(
        "--export-solver-input",
        action="store_true",
        help="Export the built solver input to a JSON file and exit without solving.",
    )
    return parser.parse_args()


def main() -> None:
    print("Starting VRP demo...")
    args = _parse_args()
    
    print(f"Loading settings from {args.env_file}...")
    settings = load_settings(env_file=args.env_file)
    print("Settings loaded successfully.")
    print("Building scenario...")
    scenario = build_scenario(settings)
    print("Scenario built successfully.")

    print("Building solver input...")
    problem = build_solver_input(settings, scenario)
    print("Solver input built successfully.")

    if args.export_solver_input:
        ensure_output_dir(settings.output_dir)
        json_path = os.path.join(settings.output_dir, SOLVER_INPUT_JSON_FILENAME)
        with open(json_path, "w", encoding="utf-8") as handle:
            json.dump(asdict(problem), handle, indent=2)
        print(f"Solver input exported to: {json_path}")
        return

    print("Solving VRP...")
    solution = solve_vrp(problem)
    print("VRP solving completed.")

    if solution.status not in HAS_SOLUTION_STATUSES:
        print(f"No feasible solution found with these parameters! (status={solution.status})")
        return

    print("\nSolution found\n")
    print(f"Employees served: {solution.total_covered_service_points}/{settings.number_of_employees} ({len(solution.omitted_service_points)} omitted)")
    for route in solution.solved_routes:
        print(f"Vehicle {route.vehicle_id}: {route.start_node_label} -> {route.end_node_label} | served={route.covered_demand} | distance={route.modeled_route_distance:.3f} km | time={route.modeled_route_duration} min")
    write_all_outputs(settings, scenario, solution)


if __name__ == "__main__":
    main()
