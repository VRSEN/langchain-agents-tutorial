import tweepy
from langchain.agents import initialize_agent, load_tools
from langchain.agents.agent_toolkits import ZapierToolkit
from langchain.llms import OpenAI
from langchain.memory import ConversationBufferMemory
from langchain.utilities.zapier import ZapierNLAWrapper
from langchain.tools import BaseTool

consumer_key = "<CONSUMER_KEY>"
consumer_secret = "<CONSUMER_SECRET>"
access_token = "<ACCESS_TOKEN>"
access_token_secret = "<ACCESS_TOKEN_SECRET>"

client = tweepy.Client(
    consumer_key=consumer_key, consumer_secret=consumer_secret,
    access_token=access_token, access_token_secret=access_token_secret
)


class TweeterPostTool(BaseTool):
    name = "Twitter Post Tweet"
    description = "Use this tool to post a tweet to twitter."

    def _run(self, text: str) -> str:
        """Use the tool."""
        return client.create_tweet(text=text)

    async def _arun(self, query: str) -> str:
        """Use the tool asynchronously."""
        raise NotImplementedError("BingSearchRun does not support async")


if __name__ == '__main__':

    llm = OpenAI(temperature=0, api_key="<OPENAI_API_KEY>")
    memory = ConversationBufferMemory(memory_key="chat_history")

    zapier = ZapierNLAWrapper(zapier_nla_api_key="<ZAPIER_NLA_API_KEY>")
    toolkit = ZapierToolkit.from_zapier_nla_wrapper(zapier)

    tools = [TweeterPostTool()] + toolkit.get_tools() + load_tools(["human"])

    agent = initialize_agent(tools, llm, memory=memory, agent="conversational-react-description", verbose=True)

    while True:
        message = input("You: ")
        assistant_message = agent.run(message)
        print(assistant_message)
