from openai import OpenAI


class LLMClient:

    system_prompt: str
    user_prompt: str
    __token: str

    def __init__(self, system_prompt, token):
        self.system_prompt = system_prompt
        self.__token = token
        self.client = OpenAI(api_key=self.__token)

    def __setUserPrompt(self, website):
        self.user_prompt = f"""You are looking at a website titled {website.title}.
        The content of the website is as follows.
        Please explain the contents to me in simple yet effective way 

        {website.text}"""

    def __getMessagesObj(self):
        return [
            {"role": "system", "content": self.system_prompt},
            {"role": "user", "content": self.user_prompt},
        ]

    def summarize(self, website):
        self.__setUserPrompt(website)
        msgs = self.__getMessagesObj()
        response = self.client.chat.completions.create(
            model="gpt-4.1-mini", messages=msgs
        )
        responseTxt = response.choices[0].message.content
        return responseTxt
