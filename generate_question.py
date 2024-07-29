import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.chains import LLMChain
import streamlit as st
from langchain_utils import generate_prompt

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

llm = ChatOpenAI(api_key=OPENAI_API_KEY, model_name="gpt-4o-mini")

prompt_path = "prompts/generate_question.prompt"
prompt = generate_prompt(prompt_path, "{first_story}, {second_story}, {select}")

first_story = "옛날 어느 곳에 한 평민이 살았는데 산의 정기를 받아서 겨드랑이에 날개(비늘)가 있고 태어나자 이내 날아다니고 힘도 센 장수 아들을 기적적으로 낳았다.그런데 부모는 이 아기장수가 크면 장차 역적이 되어서 집안을 망칠 것이라고 해서 아기장수를 돌로 눌러 죽인다.아기장수가 죽을 때 유언으로 콩 다섯 섬과 팥 다섯 섬을 같이 묻어 달라고 하였다"
second_story = "얼마후 관군이 와서 아기장수를 내놓으라고 하여 이미 부모가 죽었다고 하니 무덤을 가르쳐 달라고 하는 것을 그 어머니가 실토하여 가 보았더니 콩은 말이 되고 팥은 군사가 되어 아기장수가 막 일어나려고 하고 있었다. 그러나 그만 관군에게 들켜서 성공 직전에 죽임을 당하였다."
st.session_state.select = "false"

chain = LLMChain(llm=llm, prompt=prompt, verbose=True)
result = chain(
    {
        "first_story": first_story,
        "second_story": second_story,
        "select": st.session_state.select,
    }
)

# question과 option들을 session_state에 저장
question_idx = result["text"].find("1")
st.session_state.question = result["text"][:question_idx]
first_option_idx = result["text"].find("2", question_idx)
st.session_state.first_option = result["text"][question_idx:first_option_idx]
st.session_state.second_option = result["text"][first_option_idx:]

st.write(st.session_state.question)
st.write(st.session_state.first_option)
st.write(st.session_state.second_option)

# 나중에 버튼이 생기면 없어질 부분
import generate_false_story
