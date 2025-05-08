# server.py
import requests
from mcp.server.fastmcp import FastMCP
import sys

# Create an MCP server
mcp = FastMCP(
    name="mcp-boardgame-rag",
    dependencies=["requests"],
    description="A tool to search for board games based on user queries.",
    version="0.0.1",
)


# Add an addition tool
@mcp.tool()
def search_board_game(prompt: str, top_n: int = 3) -> list:
    """
    Search for a board game based on a user's description.

    Parameters:
        prompt (str): A question or query, ideally asking for board game suggestions or themes.
                      Example: "มีบอร์ดเกมอะไรที่ดัดแปลงมาจากการ์ตูนญี่ปุ่นเกี่ยวกับการสำรวจดันเจียนบ้าง?"
        top_n (int): The number of top relevant documents to return. Default is 3.

    Returns:
        list: A list of board game documents, each with the following structure:
            str          # A formatted string containing the board game title, meta data, and description

    Example result:
        [
            "Title: Monster Eater Dungeon Meshi (TH) มอนสเตอร์อีทเตอร์ สูตรลับตำรับดันเจียน\nContent: ในเกมนี้ผู้เล่นจะได้เข้าไปสู่โลกของสูตรลับตำรับดันเจียน การ์ตูนดังจากญี่ปุ่นที่มีธีมเกี่ยวกับการสำรวจดันเจียนเพื่อเป้าหมายที่แตกต่างกันไปในเวอร์ชั่นบอร์ดเกม ผู้เล่นจะได้สวมบทบาทเป็นหนึ่งในหัวหน้าจากปาร์ตี้ ไลออส, ชูโร่, ทันซ์, คาบรู และ กองทัพคานาเรีย",
            ...
        ]

    Notes:
        - This tool should only be used for Thai-language prompts specifically related to board games.
        - Double-check the response to ensure it is relevant to the prompt; if not, adjust the prompt and try again.
        - If you want to search for board game expansions or extensions, consider increasing top_n to 5 or more.
    """
    response = requests.post(
        "http://localhost:5001/completions",
        json={"prompt": prompt, "top_n": top_n}
    )
    
    return response.json()["top_documents"]


# # Add a dynamic greeting resource
# @mcp.resource("greeting://{name}")
# def get_greeting(name: str) -> str:
#     """Get a personalized greeting"""
#     return f"Hello, {name}!"