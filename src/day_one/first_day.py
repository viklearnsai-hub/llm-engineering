import os
from dotenv import load_dotenv
from website import Website
from llmClient import LLMClient

load_dotenv()
api_key = os.getenv("OPEN_AI_API_KEY")


system_prompt = """You are a AI Expert who has indept understanding of the conepts in AI and you are also 
                   an excelent teacher who can explain the concept in simple terms without skipping over any of the concept,
                   ignoring texts that might be related to navigation

                """
web = Website(
    "https://medium.com/@amanatulla1606/transformer-architecture-explained-2c49e2257b4c"
)
web.webscrape()
client = LLMClient(system_prompt, api_key)
print(client.summarize(web))
