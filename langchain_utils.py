from langchain.prompts import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)


def load_prompt(file_path: str) -> str:
    """
    prompt를 불러오는 함수입니다.

    Args:
        file_path (str): 파일 경로

    Returns:
        str : prompt
    """
    with open(file_path, "r", encoding="utf-8") as file:
        prompt = file.read().strip()
    return prompt


def generate_prompt(file_path: str, prompt_variable: str) -> ChatPromptTemplate:
    """
    prompt template를 만드는 함수

    Args:
        file_path (str): 파일 경로
        prompt_variable (str): prompt안에 변수

    Returns:
        ChatPromptTemplate: prompt template
    """
    system_prompt = load_prompt(file_path)
    custom_prompt = ChatPromptTemplate(
        messages=[
            SystemMessagePromptTemplate.from_template(system_prompt),
            HumanMessagePromptTemplate.from_template(prompt_variable),
        ]
    )
    return custom_prompt
