"""
YAML-configured LLM Application using LangChain v0.3.

This application loads configuration from YAML files and creates an LLM agent
that can use tools like a calculator and document search.
"""

import os
import yaml
from typing import Dict, List, Any

from langchain_openai import ChatOpenAI
from langchain.agents import AgentExecutor, create_react_agent
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.tools import Tool

from src.tools.calculator import calculator
from src.tools.document_search import document_search

def load_config(config_path: str = "config/config.yaml") -> Dict[str, Any]:
    """
    Load configuration from a YAML file.
    
    Args:
        config_path: Path to the configuration file
    
    Returns:
        A dictionary containing the configuration
    """
    with open(config_path, "r", encoding="utf-8") as f:
        config = yaml.safe_load(f)
    return config

def create_llm(llm_config: Dict[str, Any]) -> ChatOpenAI:
    """
    Create an LLM instance based on the configuration.
    
    Args:
        llm_config: LLM configuration dictionary
    
    Returns:
        A ChatOpenAI instance
    """
    provider = llm_config.get("provider", "openai")
    
    if provider == "openai":
        model_name = llm_config.get("model_name", "gpt-3.5-turbo")
        temperature = llm_config.get("temperature", 0.7)
        max_tokens = llm_config.get("max_tokens", 1000)
        
        return ChatOpenAI(
            model_name=model_name,
            temperature=temperature,
            max_tokens=max_tokens
        )
    else:
        raise ValueError(f"Unsupported LLM provider: {provider}")

def create_tools(tools_config: List[Dict[str, Any]]) -> List[Tool]:
    """
    Create tool instances based on the configuration.
    
    Args:
        tools_config: List of tool configuration dictionaries
    
    Returns:
        A list of Tool instances
    """
    tools = []
    
    for tool_config in tools_config:
        name = tool_config.get("name")
        description = tool_config.get("description", "")
        function_name = tool_config.get("function")
        
        if function_name == "calculator":
            tools.append(
                Tool(
                    name=name,
                    description=description,
                    func=calculator
                )
            )
        elif function_name == "document_search":
            doc_path = tool_config.get("path", "data/documents.txt")
            
            def search_with_path(query: str) -> str:
                return document_search(query, doc_path)
            
            tools.append(
                Tool(
                    name=name,
                    description=description,
                    func=search_with_path
                )
            )
    
    return tools

def create_prompt(prompt_config: Dict[str, Any]) -> ChatPromptTemplate:
    """
    Create a prompt template based on the configuration.
    
    Args:
        prompt_config: Prompt configuration dictionary
    
    Returns:
        A ChatPromptTemplate instance
    """
    template = prompt_config.get("template", [])
    
    return ChatPromptTemplate.from_messages(template)

def create_agent(
    llm: ChatOpenAI,
    tools: List[Tool],
    prompt: ChatPromptTemplate,
    agent_config: Dict[str, Any]
) -> AgentExecutor:
    """
    Create an agent based on the configuration.
    
    Args:
        llm: LLM instance
        tools: List of tools
        prompt: Prompt template
        agent_config: Agent configuration dictionary
    
    Returns:
        An AgentExecutor instance
    """
    agent_type = agent_config.get("type", "zero_shot_react_description")
    max_iterations = agent_config.get("max_iterations", 5)
    verbose = agent_config.get("verbose", True)
    
    if agent_type == "zero_shot_react_description":
        agent = create_react_agent(llm, tools, prompt)
        
        return AgentExecutor(
            agent=agent,
            tools=tools,
            max_iterations=max_iterations,
            verbose=verbose
        )
    else:
        raise ValueError(f"Unsupported agent type: {agent_type}")

def main():
    """Main function to run the application."""
    if not os.environ.get("OPENAI_API_KEY"):
        print("Warning: OPENAI_API_KEY environment variable is not set.")
        print("Please set it using: export OPENAI_API_KEY='your-api-key'")
        return
    
    config = load_config()
    
    llm = create_llm(config.get("llm", {}))
    
    tools = create_tools(config.get("tools", []))
    
    prompt = create_prompt(config.get("prompt", {}))
    
    agent = create_agent(llm, tools, prompt, config.get("agent", {}))
    
    print("YAML-configured LLM Application")
    print("Type 'exit' to quit")
    
    while True:
        user_input = input("\nYou: ")
        
        if user_input.lower() in ["exit", "quit", "q"]:
            break
        
        try:
            response = agent.invoke({"input": user_input})
            print(f"\nAgent: {response['output']}")
        except Exception as e:
            print(f"\nError: {str(e)}")

if __name__ == "__main__":
    main()
