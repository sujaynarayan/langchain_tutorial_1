import streamlit as st
from langchain.llms import OpenAI
from langchain.llms import AzureOpenAI

#OpenAI variables
apiKey="c60ee65f0b324c80be6f1c441f6ccc96" #from keys
api_type="azure" #OpenAI playground params
api_base="https://bionicsopenapiservice.openai.azure.com/" #OpenAI playground params
api_version="2022-12-01" #OpenAI playground params
deployment_name="text-davinci-003"
model_name="text-davinci-003"
# end of OpenAI variables

st.title('Bionics Custom Chat GPT App')

openai_api_key = st.sidebar.text_input('OpenAI API Key')

def generate_response(input_text):
  llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)
  #llm = AzureOpenAI(deployment_name=deployment_name, model_name=model_name)
  st.info(llm(input_text))

with st.form('my_form'):
  text = st.text_area('Enter text:', 'What are the three key pieces of advice for learning how to code?')
  submitted = st.form_submit_button('Submit')
  if not openai_api_key.startswith('sk-'):
    st.warning('Please enter your OpenAI API key!')#, icon='')
  if submitted and openai_api_key.startswith('sk-'):
    generate_response(text)