from mcp.server.fastmcp import FastMCP


mcp = FastMCP("MCP-Tool-Calling-Agent")


@mcp.tool()
def calculate(a: float, b: float, operation: str) -> float:

    if operation == "add":
        return a + b

    elif operation == "subtract":
        return a - b

    elif operation == "multiply":
        return a * b

    elif operation == "divide":
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

    else:
        raise ValueError("Invalid operation")


@mcp.tool()
def text_stats(text: str) -> dict:

    return {
        "words": len(text.split()),
        "characters": len(text)
    }


@mcp.tool()
def extract_keywords(text: str) -> list[str]:

    ignored_words = {
        "the", "is", "a", "an", "and",
        "or", "to", "of", "in", "for"
    }

    words = text.lower().split()

    keywords = []

    for word in words:
        word = word.strip(".,!?")

        if word not in ignored_words and word not in keywords:
            keywords.append(word)

    return keywords[:10]


@mcp.tool()
def task_priority(urgency: int, importance: int) -> str:

    score = urgency + importance

    if score >= 8:
        return "High Priority"

    elif score >= 5:
        return "Medium Priority"

    return "Low Priority"



@mcp.resource("info://project")
def project_info():

    return """
    MCP Tool Calling Agent
    Built using Python, MCP, LangChain and Groq.
    """


@mcp.resource("info://tools")
def tools_info():

    return """
    Available tools:
    calculate
    text_stats
    extract_keywords
    task_priority
    """


@mcp.resource("info://developer")
def developer_info():

    return """
    This project demonstrates LLM tool usage through MCP.
    """


@mcp.resource("info://guide")
def usage_guide():

    return """
    Calculate numbers.
    Analyze text.
    Extract keywords.
    Evaluate task priority.
    """



@mcp.prompt()
def summarize_prompt(text: str):

    return f"""
    Summarize this text:
    
    {text}
    
    Use simple language.
    """


@mcp.prompt()
def analyze_prompt(topic: str):

    return f"""
    Analyze this topic:
    
    {topic}
    
    Explain main points, advantages and limitations.
    """


if __name__ == "__main__":
    mcp.run()