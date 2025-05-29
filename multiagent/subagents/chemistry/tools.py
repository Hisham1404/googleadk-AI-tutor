"""
AI Tutor - Chemistry Elements Database and Tools
==============================================

This module provides access to chemical element information for the Chemistry Agent.
The elements database includes atomic properties, symbols, and masses for common
elements used in chemistry education and problem solving.

Author: AI Tutor Team
Version: 1.0.0

Database Contents:
- Main group elements: Hydrogen, alkali metals, halogens, noble gases
- Transition metals: Iron, copper, zinc, silver, gold, etc.
- Metalloids and nonmetals: Carbon, nitrogen, oxygen, silicon, etc.
- Other important elements for chemistry education

Reference: IUPAC atomic masses and standard chemical data
"""

# Chemical Elements Database
# ==========================
# Contains fundamental properties of chemical elements commonly encountered
# in chemistry education. All atomic masses are based on IUPAC standards.

ELEMENT_DATA = {
    # Period 1 Elements
    "hydrogen": {"symbol": "H", "atomic_number": 1, "atomic_mass": 1.008, "group": 1, "period": 1},
    "helium": {"symbol": "He", "atomic_number": 2, "atomic_mass": 4.0026, "group": 18, "period": 1},
    
    # Period 2 Elements
    "lithium": {"symbol": "Li", "atomic_number": 3, "atomic_mass": 6.94, "group": 1, "period": 2},
    "beryllium": {"symbol": "Be", "atomic_number": 4, "atomic_mass": 9.0122, "group": 2, "period": 2},
    "boron": {"symbol": "B", "atomic_number": 5, "atomic_mass": 10.811, "group": 13, "period": 2},
    "carbon": {"symbol": "C", "atomic_number": 6, "atomic_mass": 12.011, "group": 14, "period": 2},
    "nitrogen": {"symbol": "N", "atomic_number": 7, "atomic_mass": 14.007, "group": 15, "period": 2},
    "oxygen": {"symbol": "O", "atomic_number": 8, "atomic_mass": 15.999, "group": 16, "period": 2},
    "fluorine": {"symbol": "F", "atomic_number": 9, "atomic_mass": 18.998, "group": 17, "period": 2},
    "neon": {"symbol": "Ne", "atomic_number": 10, "atomic_mass": 20.180, "group": 18, "period": 2},
    
    # Period 3 Elements
    "sodium": {"symbol": "Na", "atomic_number": 11, "atomic_mass": 22.990, "group": 1, "period": 3},
    "magnesium": {"symbol": "Mg", "atomic_number": 12, "atomic_mass": 24.305, "group": 2, "period": 3},
    "aluminum": {"symbol": "Al", "atomic_number": 13, "atomic_mass": 26.982, "group": 13, "period": 3},
    "silicon": {"symbol": "Si", "atomic_number": 14, "atomic_mass": 28.086, "group": 14, "period": 3},
    "phosphorus": {"symbol": "P", "atomic_number": 15, "atomic_mass": 30.974, "group": 15, "period": 3},
    "sulfur": {"symbol": "S", "atomic_number": 16, "atomic_mass": 32.065, "group": 16, "period": 3},
    "chlorine": {"symbol": "Cl", "atomic_number": 17, "atomic_mass": 35.453, "group": 17, "period": 3},
    "argon": {"symbol": "Ar", "atomic_number": 18, "atomic_mass": 39.948, "group": 18, "period": 3},
    
    # Period 4 Elements (selected important ones)
    "potassium": {"symbol": "K", "atomic_number": 19, "atomic_mass": 39.098, "group": 1, "period": 4},
    "calcium": {"symbol": "Ca", "atomic_number": 20, "atomic_mass": 40.078, "group": 2, "period": 4},
    "chromium": {"symbol": "Cr", "atomic_number": 24, "atomic_mass": 51.996, "group": 6, "period": 4},
    "manganese": {"symbol": "Mn", "atomic_number": 25, "atomic_mass": 54.938, "group": 7, "period": 4},
    "iron": {"symbol": "Fe", "atomic_number": 26, "atomic_mass": 55.845, "group": 8, "period": 4},
    "nickel": {"symbol": "Ni", "atomic_number": 28, "atomic_mass": 58.693, "group": 10, "period": 4},
    "copper": {"symbol": "Cu", "atomic_number": 29, "atomic_mass": 63.546, "group": 11, "period": 4},
    "zinc": {"symbol": "Zn", "atomic_number": 30, "atomic_mass": 65.38, "group": 12, "period": 4},
    "bromine": {"symbol": "Br", "atomic_number": 35, "atomic_mass": 79.904, "group": 17, "period": 4},
    
    # Period 5 Elements (selected important ones)
    "silver": {"symbol": "Ag", "atomic_number": 47, "atomic_mass": 107.868, "group": 11, "period": 5},
    "iodine": {"symbol": "I", "atomic_number": 53, "atomic_mass": 126.904, "group": 17, "period": 5},
    
    # Period 6 Elements (selected important ones)
    "tungsten": {"symbol": "W", "atomic_number": 74, "atomic_mass": 183.84, "group": 6, "period": 6},
    "gold": {"symbol": "Au", "atomic_number": 79, "atomic_mass": 196.967, "group": 11, "period": 6},
    "lead": {"symbol": "Pb", "atomic_number": 82, "atomic_mass": 207.2, "group": 14, "period": 6},
    
    # Other useful elements
    "molybdenum": {"symbol": "Mo", "atomic_number": 42, "atomic_mass": 95.94, "group": 6, "period": 5},
}

def elements_lookup(element_name: str) -> dict:
    """
    Retrieves comprehensive information about a chemical element from the database.
    
    This function provides the Chemistry Agent with accurate atomic data for
    chemical elements commonly encountered in chemistry education. The data
    includes atomic properties essential for chemical calculations and understanding.
    
    Args:
        element_name (str): The name of the chemical element to look up.
                          Names should be in English (e.g., "carbon", "hydrogen")
                          Case-insensitive matching is supported.
    
    Returns:
        dict: A dictionary containing:
            - status (str): 'success' if element found, 'error' if not found
            - element (str): The properly capitalized element name
            - symbol (str): The chemical symbol (1-2 letters)
            - atomic_number (int): The number of protons in the nucleus
            - atomic_mass (float): The atomic mass in atomic mass units (u)
            - group (int): The periodic table group number (1-18)
            - period (int): The periodic table period number (1-7)
    
    Available Elements:
        Period 1: hydrogen, helium
        Period 2: lithium, beryllium, boron, carbon, nitrogen, oxygen, fluorine, neon
        Period 3: sodium, magnesium, aluminum, silicon, phosphorus, sulfur, chlorine, argon
        Period 4: potassium, calcium, chromium, manganese, iron, nickel, copper, zinc, bromine
        Others: silver, gold, lead, tungsten, iodine, molybdenum
    
    Examples:
        >>> elements_lookup('carbon')
        {
            'status': 'success',
            'element': 'Carbon',
            'symbol': 'C',
            'atomic_number': 6,
            'atomic_mass': 12.011,
            'group': 14,
            'period': 2
        }
        
        >>> elements_lookup('gold')
        {
            'status': 'success',
            'element': 'Gold',
            'symbol': 'Au',
            'atomic_number': 79,
            'atomic_mass': 196.967,
            'group': 11,
            'period': 6
        }
    
    Note:
        Atomic masses are based on IUPAC recommended values.
        Group and period numbers follow the modern IUPAC numbering system.
    """
    # Normalize the element name for case-insensitive lookup
    query = element_name.lower().strip()
    
    # Look up the element in the database
    if query in ELEMENT_DATA:
        info = ELEMENT_DATA[query]
        
        return {
            "status": "success", 
            "element": element_name.title(),  # Properly capitalize the name
            "symbol": info['symbol'],
            "atomic_number": info['atomic_number'],
            "atomic_mass": info['atomic_mass'],
            "group": info['group'],
            "period": info['period'],
            "description": _get_element_description(query, info)
        }
    else:
        # Generate helpful error message with available elements
        available_elements = sorted(list(ELEMENT_DATA.keys()))
        
        return {
            "status": "error", 
            "result": f"Element '{element_name}' not found in the database.",
            "available_elements": available_elements,
            "suggestion": "Check spelling or try a different element name. Use full element names like 'carbon' or 'hydrogen'."
        }


def _get_element_description(element_name: str, element_data: dict) -> str:
    """
    Generate a descriptive summary of an element's properties.
    
    Args:
        element_name (str): The normalized element name
        element_data (dict): The element's data from the database
    
    Returns:
        str: A human-readable description of the element
    """
    symbol = element_data['symbol']
    atomic_num = element_data['atomic_number']
    mass = element_data['atomic_mass']
    group = element_data['group']
    period = element_data['period']
    
    # Element category based on position in periodic table
    if group == 1 and atomic_num > 1:
        category = "alkali metal"
    elif group == 2:
        category = "alkaline earth metal"
    elif group == 17:
        category = "halogen"
    elif group == 18:
        category = "noble gas"
    elif 3 <= group <= 12:
        category = "transition metal"
    elif group >= 13 and atomic_num in [5, 14, 32, 33, 51, 52, 84]:
        category = "metalloid"
    elif group >= 13:
        category = "post-transition metal" if atomic_num > 12 else "metal"
    else:
        category = "nonmetal"
    
    return f"{element_name.title()} ({symbol}) is a {category} in group {group}, period {period}. Atomic mass: {mass} u"
