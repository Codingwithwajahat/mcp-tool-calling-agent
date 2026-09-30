
# MCP Tool Calling AI Agent 🚀

An AI agent built using **MCP (Model Context Protocol)**, **LangChain**, and **Groq LLM** that enables LLM-based tool calling and external tool integration.

## Features

- MCP Server & Client integration
- LLM-based tool selection
- Dynamic tool calling
- MCP Resources
- MCP Prompt templates
- Async Python workflow

## Architecture

User
 ↓
LangChain Agent
 ↓
Groq LLM
 ↓
MCP Client
 ↓
MCP Server
 ↓
Tools / Resources / Prompts

## Available Tools

- Calculator
- Text Statistics
- Keyword Extractor
- Task Priority Analyzer

## MCP Resources

- Project information
- Tool documentation
- Usage guidelines

## MCP Prompts

- Summarization prompt
- Topic analysis prompt

## Tech Stack

- Python
- MCP
- LangChain
- Groq LLM
- AsyncIO

## How It Works

1. User sends a request.
2. LLM decides whether a tool is needed.
3. MCP executes the selected tool.
4. Result is returned to the LLM.
5. Agent generates the final response.

## Run

bash
pip install -r requirements.txt
python agent.py

## Project Structure

mcp-tool-calling-agent/

├── agent.py
├── server.py
└── README.md

Built as part of my AI Engineering learning journey 🚀
