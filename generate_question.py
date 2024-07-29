import os, re
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.prompts import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)

load_dotenv()

llm = ChatOpenAI(model="gpt-4o-mini")


def load_prompt(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        prompt = file.read().strip()
    return prompt


prompt_path = "prompts/generate_question.prompt"
system_prompt = load_prompt(prompt_path)
custom_prompt = ChatPromptTemplate.from_messages(
    [
        SystemMessagePromptTemplate.from_template(system_prompt),
        HumanMessagePromptTemplate.from_template(
            "{first_story}, {second_story}, {select}"
        ),
    ]
)
first_story = "옛날 어느 곳에 한 평민이 살았는데 산의 정기를 받아서 겨드랑이에 날개(비늘)가 있고 태어나자 이내 날아다니고 힘도 센 장수 아들을 기적적으로 낳았다.그런데 부모는 이 아기장수가 크면 장차 역적이 되어서 집안을 망칠 것이라고 해서 아기장수를 돌로 눌러 죽인다.아기장수가 죽을 때 유언으로 콩 다섯 섬과 팥 다섯 섬을 같이 묻어 달라고 하였다"
second_story = "얼마후 관군이 와서 아기장수를 내놓으라고 하여 이미 부모가 죽었다고 하니 무덤을 가르쳐 달라고 하는 것을 그 어머니가 실토하여 가 보았더니 콩은 말이 되고 팥은 군사가 되어 아기장수가 막 일어나려고 하고 있었다. 그러나 그만 관군에게 들켜서 성공 직전에 죽임을 당하였다."
select = "false"

chain = custom_prompt | llm
result = chain.invoke(
    {"first_story": first_story, "second_story": second_story, "select": select}
)

pattern = r"\((.*?)\)"
options = re.findall(pattern, result.content)
print(options)
first_option, second_option = options[-2], options[-1]
print(result.content)
print(first_option)
print(second_option)
