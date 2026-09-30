import asyncio

from langchain_groq import ChatGroq
from langchain_mcp_adapters.client import MultiServerMCPClient

from mcp import ClientSession
from mcp.client.stdio import (
    stdio_client,
    StdioServerParameters
)


llm = ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=0.2,
    api_key="api"
)


server_params = StdioServerParameters(
    command="python",
    args=["server.py"]
)



async def main():


    client = MultiServerMCPClient(
        {
            "my_server": {
                "command": "python",
                "args": ["server.py"],
                "transport": "stdio",
            }
        }
    )


    tools = await client.get_tools()


    llm_with_tools = llm.bind_tools(tools)


    async with stdio_client(server_params) as (read, write):

        async with ClientSession(read, write) as session:


            await session.initialize()


            while True:


                user_input = input("\nUser: ")


                if user_input.lower() == "exit":
                    break



                response = await llm_with_tools.ainvoke(
                    user_input
                )


                tool_results = []



                if response.tool_calls:


                    for tool_call in response.tool_calls:


                        tool_name = tool_call["name"]

                        arguments = tool_call["args"]



                        for tool in tools:

                            if tool.name == tool_name:


                                result = await tool.ainvoke(
                                    arguments
                                )


                                tool_results.append(
                                    str(result)
                                )



                    final_response = await llm.ainvoke(
                        f"""
                        User request:
                        {user_input}

                        Tool results:
                        {tool_results}

                        Provide final answer.
                        """
                    )


                    print(
                        "\nAssistant:",
                        final_response.content
                    )


                else:


                    print(
                        "\nAssistant:",
                        response.content
                    )



                if "resource" in user_input.lower():

                    resource = await session.read_resource(
                        "info://project"
                    )

                    print(resource)



                if "summarize" in user_input.lower():

                    prompt = await session.get_prompt(
                        "summarize_prompt",
                        arguments={
                            "text": user_input
                        }
                    )

                    print(prompt)



if __name__ == "__main__":
    asyncio.run(main())