"""
AI Tutor - Physics Constants Database and Tools
==============================================

This module provides access to fundamental physical constants for the Physics Agent.
The constants database includes precise values used in physics calculations with
proper units and scientific notation.

Author: AI Tutor Team
Version: 1.0.0

Constants Categories:
- Universal Constants: Speed of light, Planck constant, etc.
- Gravitational Constants: Gravitational constant, Earth's gravity
- Electromagnetic Constants: Elementary charge, permittivity, etc.
- Atomic Constants: Atomic mass unit, Avogadro number, etc.

Reference: CODATA 2018 internationally recommended values
"""

# Fundamental Physical Constants Database
# ======================================
# All values are based on CODATA 2018 internationally recommended constants
# Each constant includes precise values with appropriate units

PHYSICS_CONSTANTS = {
    # Universal Constants
    "speed_of_light": 299792458,                    # m/s (exact, by definition)
    "planck_constant": 6.62607015e-34,              # J⋅s (exact, by definition)
    "reduced_planck_constant": 1.054571817e-34,     # J⋅s (ℏ = h/2π)
    
    # Gravitational Constants
    "gravitational_constant": 6.67430e-11,          # m³⋅kg⁻¹⋅s⁻² (G)
    "earth_gravity": 9.80665,                       # m/s² (standard gravity)
    
    # Electromagnetic Constants  
    "elementary_charge": 1.602176634e-19,           # C (e, exact by definition)
    "vacuum_permittivity": 8.8541878128e-12,        # F/m (ε₀)
    "vacuum_permeability": 1.25663706212e-6,        # H/m (μ₀)
    
    # Atomic and Molecular Constants
    "atomic_mass_unit": 1.66053906660e-27,          # kg (u)
    "avogadro_number": 6.02214076e23,               # mol⁻¹ (Nₐ, exact by definition)
    "boltzmann_constant": 1.380649e-23,             # J/K (k, exact by definition)
    
    # Electron Properties
    "electron_mass": 9.1093837015e-31,              # kg (mₑ)
    "electron_charge_to_mass": -1.75882001076e11,   # C/kg (e/mₑ)
    
    # Proton Properties
    "proton_mass": 1.67262192369e-27,               # kg (mₚ)
    
    # Other Important Constants
    "gas_constant": 8.314462618,                    # J⋅mol⁻¹⋅K⁻¹ (R, exact by definition)
    "stefan_boltzmann_constant": 5.670374419e-8,    # W⋅m⁻²⋅K⁻⁴ (σ)
    "fine_structure_constant": 7.2973525693e-3,     # dimensionless (α ≈ 1/137)
}

def lookup_physics_constant(constant_name: str) -> dict:
    """
    Retrieves the value of a fundamental physical constant from the database.
    
    This function provides the Physics Agent with access to precise values of
    physical constants as defined by international standards (CODATA 2018).
    All constants include appropriate units and precision.
    
    Args:
        constant_name (str): The name of the physical constant to look up.
                           Names should use underscores (e.g., 'speed_of_light')
                           Case-insensitive matching is supported.
    
    Returns:
        dict: A dictionary containing:
            - status (str): 'success' if constant found, 'error' if not found
            - constant_name (str): The original requested constant name  
            - value (float): The numerical value of the constant
            - info (str): Additional information about units and context
    
    Available Constants:
        Universal: speed_of_light, planck_constant, reduced_planck_constant
        Gravitational: gravitational_constant, earth_gravity
        Electromagnetic: elementary_charge, vacuum_permittivity, vacuum_permeability
        Atomic: atomic_mass_unit, avogadro_number, boltzmann_constant
        Particles: electron_mass, proton_mass, electron_charge_to_mass
        Other: gas_constant, stefan_boltzmann_constant, fine_structure_constant
    
    Examples:
        >>> lookup_physics_constant('speed_of_light')
        {
            'status': 'success', 
            'constant_name': 'speed_of_light', 
            'value': 299792458,
            'info': 'Speed of light in vacuum: 299,792,458 m/s (exact, by definition)'
        }
        
        >>> lookup_physics_constant('planck_constant')
        {
            'status': 'success',
            'constant_name': 'planck_constant', 
            'value': 6.62607015e-34,
            'info': 'Planck constant: 6.626 × 10⁻³⁴ J⋅s (exact, by definition)'
        }
    
    Note:
        Constants are based on CODATA 2018 internationally recommended values.
        Some constants are exact by definition in the SI system.
    """
    # Normalize the constant name to lowercase for case-insensitive lookup
    normalized_name = constant_name.lower().strip()
    
    # Look up the constant value in the database
    value = PHYSICS_CONSTANTS.get(normalized_name)
    
    if value is not None:
        # Prepare additional information about the constant
        info = _get_constant_info(normalized_name, value)
        
        return {
            "status": "success", 
            "constant_name": constant_name,
            "value": value,
            "info": info
        }
    else:
        # Generate helpful error message with available constants
        available_constants = list(PHYSICS_CONSTANTS.keys())
        
        return {
            "status": "error", 
            "result": f"Constant '{constant_name}' not found.",
            "available_constants": available_constants,
            "suggestion": "Try using underscores in names, e.g., 'speed_of_light' or 'planck_constant'"
        }


def _get_constant_info(constant_name: str, value: float) -> str:
    """
    Generate descriptive information about a physical constant.
    
    Args:
        constant_name (str): The normalized name of the constant
        value (float): The numerical value of the constant
    
    Returns:
        str: Human-readable description with units and context
    """
    # Mapping of constant names to their descriptions and units
    constant_descriptions = {
        "speed_of_light": "Speed of light in vacuum: 299,792,458 m/s (exact, by definition)",
        "planck_constant": "Planck constant: 6.626 × 10⁻³⁴ J⋅s (exact, by definition)",
        "reduced_planck_constant": "Reduced Planck constant (ℏ): 1.055 × 10⁻³⁴ J⋅s",
        "gravitational_constant": "Gravitational constant (G): 6.674 × 10⁻¹¹ m³⋅kg⁻¹⋅s⁻²",
        "earth_gravity": "Standard gravity on Earth: 9.807 m/s²",
        "elementary_charge": "Elementary charge (e): 1.602 × 10⁻¹⁹ C (exact, by definition)",
        "vacuum_permittivity": "Vacuum permittivity (ε₀): 8.854 × 10⁻¹² F/m",
        "vacuum_permeability": "Vacuum permeability (μ₀): 1.257 × 10⁻⁶ H/m",
        "atomic_mass_unit": "Atomic mass unit (u): 1.661 × 10⁻²⁷ kg",
        "avogadro_number": "Avogadro constant (Nₐ): 6.022 × 10²³ mol⁻¹ (exact, by definition)",
        "boltzmann_constant": "Boltzmann constant (k): 1.381 × 10⁻²³ J/K (exact, by definition)",
        "electron_mass": "Electron rest mass (mₑ): 9.109 × 10⁻³¹ kg",
        "proton_mass": "Proton rest mass (mₚ): 1.673 × 10⁻²⁷ kg",
        "gas_constant": "Gas constant (R): 8.314 J⋅mol⁻¹⋅K⁻¹ (exact, by definition)",
        "stefan_boltzmann_constant": "Stefan-Boltzmann constant (σ): 5.670 × 10⁻⁸ W⋅m⁻²⋅K⁻⁴",
        "fine_structure_constant": "Fine structure constant (α): 7.297 × 10⁻³ ≈ 1/137 (dimensionless)"
    }
    
    return constant_descriptions.get(constant_name, f"Physical constant: {value}")

