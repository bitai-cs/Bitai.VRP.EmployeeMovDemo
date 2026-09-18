import argparse

from config import load_settings
from problem import build_solver_input
from reporting import write_all_outputs
from scenario import build_scenario
from solver import HAS_SOLUTION_STATUSES, solve_vrp


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Resolve a VRP demo from a parameter file.")
    parser.add_argument(
        "--env-file",
        default=".env",
        help="Path to the scenario configuration file (default: .env).",
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

    print("Solving VRP...")
    solution = solve_vrp(problem)
    print("VRP solving completed.")

    if solution.status not in HAS_SOLUTION_STATUSES:
        print(f"No se encontro solucion factible con estos parametros! (status={solution.status})")
        return

    print("\nSolucion encontrada\n")
    print(f"Empleados servidos: {solution.total_covered_service_points}/{settings.number_of_employees} ({len(solution.omitted_service_points)} omitidos)")
    for route in solution.solved_routes:
        print(f"Vehiculo {route.vehicle_id}: {route.start_node_label} -> {route.end_node_label} | atendidos={route.covered_demand} | distancia={route.modeled_route_distance:.3f} km | tiempo={route.modeled_route_duration} min")
    write_all_outputs(settings, scenario, solution)


if __name__ == "__main__":
    main()
