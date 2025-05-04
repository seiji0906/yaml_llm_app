"""Document search tool for retrieving information from text files."""

def document_search(query: str, document_path: str = "data/documents.txt") -> str:
    """
    Searches for the query in the document and returns relevant sections.
    
    Args:
        query: The search query
        document_path: Path to the document file (default: data/documents.txt)
    
    Returns:
        A string containing the relevant sections of the document
    
    Example:
        >>> document_search("Python")
        'Python is a high-level, interpreted programming language...'
    """
    try:
        with open(document_path, "r", encoding="utf-8") as f:
            content = f.read()
        
        sections = content.split("##")
        
        relevant_sections = []
        for section in sections:
            if query.lower() in section.lower():
                relevant_sections.append(section.strip())
        
        if relevant_sections:
            return "\n\n".join(relevant_sections)
        else:
            return "No relevant information found."
    except Exception as e:
        return f"Error: {str(e)}"
