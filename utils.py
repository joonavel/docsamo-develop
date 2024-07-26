import streamlit as st

def switch_page(page_name: str):
    """_summary_

    Args:
        page_name (str): _description_

    Raises:
        RerunException: _description_
        ValueError: _description_

    Returns:
        _type_: _description_
    """
    from streamlit.runtime.scriptrunner import RerunData, RerunException
    from streamlit.source_util import get_pages

    def standardize_name(name: str) -> str:
        return name.lower().replace("_", " ")
    
    page_name = standardize_name(page_name)

    pages = get_pages("navigator.py")  # OR whatever your main page is called

    for page_hash, config in pages.items():
        if standardize_name(config.get("page_name", "")) == page_name:
            raise RerunException(
                RerunData(
                    page_script_hash=page_hash,
                    page_name=page_name,
                )
            )

    page_names = [standardize_name(config.get("page_name", "")) for config in pages.values()]

    raise ValueError(f"Could not find page {page_name}. Must be one of {page_names}")


def show_sidebar():
    with st.sidebar:
        if st.button("user"):
            switch_page("user")
        if st.button("user_analysis"):
            switch_page("user_analysis")
        if st.button("settings"):
            switch_page("settings")