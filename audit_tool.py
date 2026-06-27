import sympy as sp
from docs.registry import REGISTRY
from docs.theory_log import get_latest_log

# ==============================================================================
# SECTION: CORE UTILITIES (DO NOT MODIFY)
# ==============================================================================

def get_eq_dim(side_str, exclude_var=None):
    """Calculates the sum of dimensions for a given side of an equation."""
    # Create symbols dict excluding the variable we are trying to solve for
    symbols_dict = {name: sp.Symbol(name) for name in REGISTRY.keys() if name != exclude_var}
    
    # sympify the string; if it's just a number, it will have no free_symbols
    expr = sp.sympify(side_str.strip(), locals=symbols_dict)
    
    total_dim = 0
    # Add dimensions for each symbol found in the expression
    for s in expr.free_symbols:
        name = str(s)
        total_dim += REGISTRY.get(name, {}).get("dim", 0)
    return total_dim

# ==============================================================================
# SECTION: ANALYSIS METHODS
# ==============================================================================

def audit_equation(equation_str):
    """Checks if dimensions on LHS and RHS match."""
    if "=" not in equation_str:
        print("Error: Equation must contain '='")
        return

    lhs_str, rhs_str = equation_str.split("=")
    lhs_dim = get_eq_dim(lhs_str)
    rhs_dim = get_eq_dim(rhs_str)

    print(f"\nAuditing: {equation_str.strip()}")
    print(f"  LHS: {lhs_dim} | RHS: {rhs_dim}")
    
    if lhs_dim == rhs_dim:
        print("  RESULT: DIMENSIONALLY CONSISTENT")
    else:
        print("  RESULT: DIMENSIONALLY INCONSISTENT")

def solve_for_missing(equation_str, missing_var="X"):
    """Determines what dimension a missing variable must have to balance."""
    lhs_str, rhs_str = equation_str.split("=")
    
    # Calculate dimensions of everything *except* the missing variable
    lhs_known = get_eq_dim(lhs_str, exclude_var=missing_var)
    rhs_known = get_eq_dim(rhs_str, exclude_var=missing_var)
    
    # Logic: LHS = RHS. If X is on RHS, LHS = RHS_known + dim_X => dim_X = LHS - RHS_known
    # If X is on LHS, LHS_known + dim_X = RHS => dim_X = RHS - LHS_known
    if missing_var in lhs_str:
        dim_x = rhs_known - lhs_known
    else:
        dim_x = lhs_known - rhs_known
        
    print(f"\n--- Solving for '{missing_var}' ---")
    print(f"To balance '{equation_str}', '{missing_var}' must have a dimension of: {dim_x}")

# ==============================================================================
# SECTION: MAIN EXECUTION
# ==============================================================================

if __name__ == "__main__":
    print("--- BMI Dimensional Audit ---")
    
    # Run Audits
    audit_equation("S = M_Pl * R_bridge")

    # This is where your new physical equation goes:
    audit_equation("m_nu = phi_vev * T_shear * R_bridge * V_shadow_inv")
    
    # Run Solvers
    solve_for_missing("m_nu = phi_vev * T_shear * R_bridge * X", missing_var="X")

    # Fetch and display the synthesis log
    log = get_latest_log()
    print(f"\n--- Latest Synthesis Entry ---")
    print(f"Event: {log['event']}")
    print(f"Discovery: {log['discovery']}")
    print(f"Implication: {log['implication']}")
