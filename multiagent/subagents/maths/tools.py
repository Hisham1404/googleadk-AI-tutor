"""
AI Tutor - Mathematics Computational Tools
==========================================

Mathematical computation tools for the Mathematics Agent. This module provides
essential calculator functions for arithmetic operations that ensure precision
and proper error handling for mathematical computations.

Author: AI Tutor Team
Version: 1.0.0

Available Tools:
- calculator: Basic arithmetic operations with error handling

Future Extensions:
- Advanced mathematical functions (trigonometry, logarithms)
- Equation solving algorithms
- Statistical computation tools
- Graphing and visualization tools
"""

def calculator(operation: str, num1: float, num2: float) -> dict:
    """
    Performs basic arithmetic operations with comprehensive error handling.
    
    This tool provides the Mathematics Agent with reliable computational
    capabilities for fundamental arithmetic operations. It includes proper
    error handling for edge cases like division by zero.
    
    Args:
        operation (str): The arithmetic operation to perform.
                        Supported values: 'add', 'subtract', 'multiply', 'divide'
        num1 (float): The first operand (left-hand side of the operation)
        num2 (float): The second operand (right-hand side of the operation)
    
    Returns:
        dict: A dictionary containing:
            - status (str): 'success' if operation completed, 'error' if failed
            - result (float|str): The numerical result or error message
    
    Examples:
        >>> calculator('add', 5.0, 3.0)
        {'status': 'success', 'result': 8.0}
        
        >>> calculator('divide', 10.0, 0.0)
        {'status': 'error', 'result': 'Cannot divide by zero.'}
        
        >>> calculator('multiply', -2.5, 4.0)
        {'status': 'success', 'result': -10.0}
    
    Raises:
        None: All errors are handled internally and returned in the result dict
    """
    # Addition Operation
    if operation == 'add':
        result = num1 + num2
        
    # Subtraction Operation  
    elif operation == 'subtract':
        result = num1 - num2
        
    # Multiplication Operation
    elif operation == 'multiply':
        result = num1 * num2
        
    # Division Operation (with zero-division protection)
    elif operation == 'divide':
        if num2 == 0:
            return {
                "status": "error", 
                "result": "Cannot divide by zero."
            }
        result = num1 / num2
        
    # Invalid Operation Handler
    else:
        return {
            "status": "error", 
            "result": f"Invalid operation '{operation}'. Supported operations: add, subtract, multiply, divide"
        }
    
    # Return successful result
    return {
        "status": "success", 
        "result": result
    }
