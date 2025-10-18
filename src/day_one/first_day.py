import os
from dotenv import load_dotenv
from day_one.llm_client import LLMClient
from day_one.website import Website

load_dotenv()
api_key = os.getenv("OPEN_AI_API_KEY")


SYSTEM_PROMPT = """You are a AI Expert who has indept understanding of the conepts in AI and you are also
                   an excelent teacher who can explain the concept in simple terms without skipping over any of the concept,
                   ignoring texts that might be related to navigation
                """
web = Website(
    "https://medium.com/@amanatulla1606/transformer-architecture-explained-2c49e2257b4c"
)
web.webscrape()
client = LLMClient(SYSTEM_PROMPT, api_key)
print(client.summarize(web))
