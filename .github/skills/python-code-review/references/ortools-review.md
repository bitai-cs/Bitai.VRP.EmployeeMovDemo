# OR-Tools and Optimization Review

> Reference for the `python-code-review` skill. Load when OR-Tools or another optimization/solver library is present (routing, CP-SAT, linear solver, scheduling).
> Related: [performance-review.md](./performance-review.md), [testing-review.md](./testing-review.md). Business-rule guidance lives in the core `SKILL.md` (Domain Rules vs Technical Rules).

If OR-Tools or another optimization library is present, perform additional domain-aware checks.

Inspect:

- Model correctness
- Variable domains
- Constraint correctness
- Objective function
- Hard vs soft constraints
- Capacity constraints
- Time-window constraints
- Vehicle constraints
- Feasibility assumptions
- Solver configuration
- Time limits
- Search parameters
- Result interpretation

Pay special attention to:

- Constraints that accidentally make the model infeasible
- Missing constraints
- Incorrect units
- Incorrect index mappings
- Off-by-one errors in nodes/vehicles
- Incorrect depot handling
- Incorrect distance/time matrices
- Inconsistent time units
- Incorrect treatment of optional assignments
- Objective terms with incorrect scaling
- Solutions interpreted as feasible without checking solver status

Always distinguish solver status from the existence of a valid business solution.

Do not assume that `OPTIMAL`, `FEASIBLE`, `UNKNOWN`, or `INFEASIBLE` have interchangeable meanings.

Check whether the application correctly handles solver failure or timeout.

For optimization services, pay particular attention to deterministic behavior and reproducibility when the application requires it.

## Business rules vs technical rules

Do not invent business rules. If the model appears inconsistent with a business rule (for example, which passenger/employee categories may share a vehicle), identify the observed behavior, state the assumption, and ask for confirmation rather than reporting a defect.

Example:

> "The current implementation allows two employee categories to share a vehicle. If those categories are required to remain separated by business policy, this is a correctness issue; otherwise the implementation is valid."
