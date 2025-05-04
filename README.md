# YAML-configured LLM Application

This project demonstrates how to build an LLM application using LangChain v0.3, where all configurations (prompts, tools, agent settings) are defined in YAML format.

## Features

- Configuration-driven LLM application using YAML
- OpenAI integration with GPT models
- Tool support (Calculator and Document Search)
- Flexible and extensible architecture

## Project Structure

```
yaml_llm_app/
├── config/
│   └── config.yaml       # Main configuration file
├── data/
│   └── documents.txt     # Sample data for document search
├── src/
│   ├── tools/
│   │   ├── __init__.py
│   │   ├── calculator.py     # Calculator tool implementation
│   │   └── document_search.py # Document search tool implementation
│   ├── __init__.py
│   └── app.py            # Main application code
├── requirements.txt      # Project dependencies
└── README.md             # Project documentation
```

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/seiji0906/yaml_llm_app.git
   cd yaml_llm_app
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Set up your OpenAI API key:
   ```
   export OPENAI_API_KEY='your-api-key'
   ```

## Usage

Run the application:
```
python -m src.app
```

The application will start an interactive session where you can ask questions. The LLM agent will use the configured tools to help answer your questions.

Example queries:
- "What is 25 * 16?"
- "Tell me about Python programming language."
- "What is LangChain?"

Type 'exit' to quit the application.

## Configuration

The application is configured using YAML files in the `config/` directory. The main configuration file is `config.yaml`, which defines:

- LLM settings (provider, model, temperature, etc.)
- Tools configuration (name, description, function, etc.)
- Prompt templates
- Agent settings (type, max iterations, etc.)

You can modify this file to customize the application behavior.

## Extending

To add new tools:

1. Create a new tool implementation in the `src/tools/` directory
2. Update the `config.yaml` file to include the new tool
3. Update the `create_tools` function in `app.py` to handle the new tool type

## License

MIT
