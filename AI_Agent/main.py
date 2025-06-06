from langchain_core.messages import HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.tools import tool
from langgraph.prebuilt import create_react_agent
from dotenv import load_dotenv

load_dotenv()
@tool
def get_joke() -> str:
    """Tell a random joke."""
    print("Fetching a random joke...")
    return "Why did the scarecrow win an award? Because he was outstanding in his field!"
    return "Why don't scientists trust atoms? Because they make up everything!"
    return "What do you call fake spaghetti? An impasta!"

def main():
    model= ChatGoogleGenerativeAI(model="gemini-2.0-flash", temperature=0)

    tools=[get_joke]
    agent_executor = create_react_agent(model,tools)

    print("Welcome! I'm your AI assistant. How can I help you today? Type 'exit' to quit.")

    while True:
        user_input = input("You: ").strip()
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break

        print("\nAssistant: ",end="")
        for chunk in agent_executor.stream(
            {"messages": [HumanMessage(content=user_input)]}
        ):
            if "agent" in chunk and "messages" in chunk["agent"]:
                for message in chunk["agent"]["messages"]:
                    print(message.content, end="")
        print()

if __name__ == "__main__":
    main()
