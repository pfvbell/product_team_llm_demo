## App Example

import streamlit as st
import openai as ai

API_ENDPOINT = "https://api.openai.com/v1/chat/completions"
## Use your own API key: https://platform.openai.com/account/api-keys

try:
  ai.api_key = st.secrets["openai_api_key"]
except:
  st.text('Add API Key')

def chatgpt_call(prompt, model, temperature):
  completion = ai.ChatCompletion.create(
    model=model, 
    messages=[{"role": "user", "content": prompt}],
    temperature=temperature
  )
  return completion['choices'][0]['message']['content']

st.header('Product Team Example App')
topic = st.text_input('Topic you want to learn')
model = 'gpt-3.5-turbo' # 'gpt-4'
temperature = 0
st.sidebar.markdown("This app uses OpenAI's generative AI. Please use it carefully and check any output as it could be biased or wrong. ")

prompt = f"You are an expert teacher. Explain this concept to me as if I am 5 years old: {topic}"

explanation = chatgpt_call(prompt, model, temperature)

generate = st.button('Generate Response')

if generate:
  st.markdown(explanation)
  st.balloons()
