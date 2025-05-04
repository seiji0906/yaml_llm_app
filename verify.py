"""
Verification script for the YAML-configured LLM Application.
This script checks the validity of the YAML configuration and Python code structure.
"""

import os
import sys
import yaml

def verify_yaml_config():
    """Verify the YAML configuration file."""
    try:
        with open("config/config.yaml", "r", encoding="utf-8") as f:
            config = yaml.safe_load(f)
        
        required_sections = ["llm", "tools", "prompt", "agent"]
        for section in required_sections:
            if section not in config:
                print(f"Error: Missing required section '{section}' in config.yaml")
                return False
        
        print("YAML configuration is valid.")
        return True
    except Exception as e:
        print(f"Error verifying YAML configuration: {str(e)}")
        return False

def verify_python_imports():
    """Verify Python imports and module structure."""
    try:
        sys.path.append(os.path.dirname(os.path.abspath(__file__)))
        
        from src.app import load_config
        
        from src.tools.calculator import calculator
        from src.tools.document_search import document_search
        
        print("Python imports are valid.")
        return True
    except Exception as e:
        print(f"Error verifying Python imports: {str(e)}")
        return False

def main():
    """Main verification function."""
    print("Verifying YAML-configured LLM Application...")
    
    yaml_valid = verify_yaml_config()
    imports_valid = verify_python_imports()
    
    if yaml_valid and imports_valid:
        print("\nVerification successful! The code structure and configuration are valid.")
        return 0
    else:
        print("\nVerification failed. Please fix the issues above.")
        return 1

if __name__ == "__main__":
    sys.exit(main())
