from langchain.prompts import PromptTemplate
from langchain.chat_models import ollama

from langchain.agents import initialize_agent, Tool, AgentType


def lookup(name: str) -> str:
    llm = ollama(model="llama2", temperature=0)
    template = """given the full name {name_of_person} I want you to get it me the username of their Linkedin profile page.
    your answer should only contain a word
    """  # end we give the output indicator

    tools_for_agent = [
        Tool.from_function(
            name="Crawl Google 4 linkedin profile page",
            func=(),
            description="useful for when you need to get the Linkedin username",
        )
    ]

    agent = initialize_agent(
        tools=tools_for_agent,
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True,
    )
    prompt_template = PromptTemplate(
        template=template, input_variables=["name_of_person"]
    )

    linkedin_profile_id = agent.run(prompt_template.format_prompt(name_of_person=name))
    return linkedin_profile_id
