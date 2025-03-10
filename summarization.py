from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate
load_dotenv()


model = ChatGoogleGenerativeAI(model = "gemini-2.0-flash")

st.header("summarization tool")
user_input = st.text_area("Enter your text to summarize:")
temp = PromptTemplate(
    template="Summarize the given text : {text}",

    input_variables=["text"]
)


if st.button("Summarize"):
    if user_input.strip():
        chain = temp | model  # Creating a LangChain pipeline
        res = chain.invoke({"text": user_input})  # Correctly passing input variable
        
        if res:
            st.subheader("Summary:")
            st.write(res.content)
        else:
            st.error("Error: No response from the model.")
    else:
        st.warning("Please enter some text to summarize.")


