import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from langchain_community.chat_message_histories import SQLChatMessageHistory
from langchain_core.runnables import RunnableWithMessageHistory
import uuid
## chat_model = GoogleGenerativeAI(api_key=api_key, model= "models/gemini-1.5-pro")


api_key = st.secrets["API"]["API_KEY"]
chat_model = ChatGoogleGenerativeAI(api_key=api_key, model= "models/gemini-1.5-pro")


## streamlit UI
st.set_page_config(page_title="Data Science Tutor", layout="wide")
st.title('🎓AI Powered Data Science Tutor')

query = st.text_area(label = 'enter the query',placeholder= 'explain the topics related to data science')
submit = st.button('submit')
if "session_id" not in st.session_state:
    st.session_state.session_id = str(uuid.uuid4())

### creation the connection to database in order to save the history
def get_message_from_history():
    chat_history = SQLChatMessageHistory(
        session_id = st.session_state.session_id,
        connection = "sqlite:///data/sqlite.db")
    return chat_history

 ### langchain components
 ### logic-1: creating the template
if submit:
    if not query.strip():
        st.error("Please enter the feilds.")
           ### langchain components
           ### logic-1: creating the template
    else:
        chat_template = ChatPromptTemplate(messages=[
        ("system","""You are an AI Tutor specializing in Data Science. 
         Your role is to assist students by answering their questions in detail, providing clear explanations with examples. 
         If a student asks a question outside the scope of Data Science, politely guide them to focus on relevant topics."""),
        MessagesPlaceholder(variable_name='history'),
        ("human","""{human_input}""")
        ])
    ## logic-2: creating the model
        chat_model = ChatGoogleGenerativeAI(api_key=api_key, model= "models/gemini-1.5-pro")
    ## logic-3:creating outparser
        output_parser = StrOutputParser()
    ## chaining all the components
        chain = chat_template | chat_model | output_parser
        chaining = RunnableWithMessageHistory(
            chain,
            get_message_from_history,
            input_messages_key="human_input",
            history_messages_key="history")
        ##user_id  = "Tutor"
        ## thread_id = uuid.uuid4()
        user_id = st.session_state.session_id 
        config = {"configurable":{"session_id":user_id}}
        human_input = {"human_input":query}
        response = chaining.stream(human_input,config=config)
        st.write(response)