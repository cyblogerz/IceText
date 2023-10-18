from langchain.prompts import PromptTemplate
from langchain.llms import Ollama
from langchain.chains import LLMChain
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler   
from third_parties.linkedin import scrape_linkedin_profile


if __name__ == "__main__":

    summary_template = """
    given the information{information} of a person from I want you to create:
    1. a short summary
    2. two interesting facts about them 
    """
    
    summary_prompt_template = PromptTemplate(input_variables=["information"] ,template=summary_template)
    llm = Ollama(model="llama2", callback_manager = CallbackManager([StreamingStdOutCallbackHandler()]))
    chain = LLMChain(llm=llm,prompt=summary_prompt_template)

    linkedin_data = scrape_linkedin_profile(linked_in_username="pranavajay")
    print(chain.run(information=linkedin_data))

    




    

