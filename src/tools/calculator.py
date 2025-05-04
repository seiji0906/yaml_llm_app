"""Calculator tool for performing arithmetic operations."""

def calculator(expression: str) -> str:
    """
    Evaluates a mathematical expression and returns the result.
    
    Args:
        expression: A string containing a mathematical expression
                   (e.g., "2 + 3", "10 * 5", "20 / 4")
    
    Returns:
        A string representation of the result
    
    Example:
        >>> calculator("2 + 3")
        '5.0'
    """
    try:
        allowed_symbols = set('0123456789+-*/().e ')
        if not all(c in allowed_symbols for c in expression):
            return "Error: Only basic arithmetic operations are allowed"
        
        result = eval(expression)
        return str(float(result))
    except Exception as e:
        return f"Error: {str(e)}"
