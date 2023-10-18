from langchain.prompts import PromptTemplate
from langchain.chat_models import ollama

from langchain.agents import initialize_agent, Tool,AgentType


def lookup(name : str)  -> str:
    llm = ollama(model="llama2",temperature=0)
    template = """given the full name {name_of_person} I want you to get it me the username of their Linkedin profile page.
    your answer should only contain a word
    """ #end we give the output indicator

    tools_for_agent = [Tool(name="Crawl Google 4 linkedin profile page",
                            func=(lambda x : x),
                            description="useful for when you need to get the Linkedin username")]

