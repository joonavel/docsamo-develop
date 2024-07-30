from langchain_community.document_loaders import AsyncChromiumLoader
import os
from langchain_community.document_transformers import BeautifulSoupTransformer
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains.openai_functions import (
    create_extraction_chain,
)  # extract 함수 사용(llm과 schema 할당)
from langchain_openai import (
    ChatOpenAI,
)  # llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0) 할당
from langchain_core.prompts import ChatPromptTemplate  # prompt 설정불러오기

from dotenv import load_dotenv

load_dotenv()

# url에 접근시킴 = USER_AGENT, AsyncChromiumLoader(url주소 할당), 객체 이용해서 불러오고 html 변수 할당
os.environ["USER_AGENT"] = "myagent"
urls = ["https://encykorea.aks.ac.kr/Article/E0063994"]
loader = AsyncChromiumLoader(urls)
html = loader.load()

# bs_transformer 에 soup할당, url->html ,tags_to_extract 를 통해 객체 지정("div","span","a")
bs_transformer = BeautifulSoupTransformer()
docs_transformed = bs_transformer.transform_documents(html, tags_to_extract=["p"])

# docs_transformed-> list안에 langchain_core.documents.base.Document 클래스가 들어있고 확인하는 코드구현
print(type(docs_transformed))  # list
print(type(docs_transformed[0]))  # langchain_core.documents.base.Document
print(type(docs_transformed[0].page_content))  # str

# RecursiveCharacterTextSplitter 통해 가져온 정보를 chunk 로 쪼개기
splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
    chunk_size=1000, chunk_overlap=0
)
splits = splitter.split_documents(docs_transformed)

# create_extraction_chain 의 schema 사용을 위한 코드 구현
schema = {
    "properties": {
        "핵심사건": {"type": "string"},
    },
    "required": ["핵심사건"],
}

# llm 모델 입력
llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)

# 프롬프트 설정
prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "입력으로 들어올 내용은 전래동화에 대한 정보를 담고 있는 페이지야. 여기서 전래동화의 줄거리 부분을 추출해줘.",
        ),
        ("human", "{input}"),
    ]
)

chain = create_extraction_chain(schema=schema, llm=llm, prompt=prompt)
result = chain  # 반환 받는 값을 넣어줄 변수 할당

# 우리가 입력으로 넣고 싶은 값이 해당 class 안에 page_content라는 속성으로 가지고 있어서 이를 해결하기 위해 아래와 같이 코드 구현.
# splits 텍스트가 이미 chunk 단위 쪼개진 상태에서 핵심사건 추출하는 코드
print(result.invoke({"input": splits}))

# 전체 텍스트에서 핵심사건 추출하는 코드
print(result.invoke({"input": docs_transformed[0].page_content}))

# llm에 모델 이름 입력 - 완료
# apikey 와 load env 코드 작성 - 완료
# chunk -23번줄 코드 입력 그런데 size 크기 정하기(알아서 size 조정)

# schema 와 함께 이용할 prompt 방법이 있나? 성공!
# prompt 설정 성공!


# 아직 미완성 된 부분
# 임베딩 화 한 정보를 넣어줄 저장소(chromadb)
# 처리한 데이터 redis에 할당 docker 컨터이너에 연결.
