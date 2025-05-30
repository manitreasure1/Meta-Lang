import yaml
import re


def parser(source_code_path: str, language_yml_path: str) -> str:
    """
    Parses the user's custom language file and replaces its syntax with Python syntax using the provided YAML mapping.
    Args:
        source_code_path (str): Path to the user's source code file (e.g., hello.tl).
        language_yml_path (str): Path to the YAML file containing syntax mappings.
    Returns:
        str: The translated Python code as a string.
    """
    # Load syntax mapping from YAML
    with open(language_yml_path, 'r') as f:
        config = yaml.safe_load(f)
    syntax_map = config.get('syntax', {})

    # Read the source code
    with open(source_code_path, 'r') as f:
        code = f.read()

    # Replace custom syntax with Python syntax using robust regex for word boundaries
    for custom, py in syntax_map.items():
        # Use negative lookbehind and lookahead to match whole words, including at line start/end
        pattern = rf'(?<!\w){re.escape(str(custom))}(?!\w)'
        code = re.sub(pattern, str(py), code)
    
    return code

