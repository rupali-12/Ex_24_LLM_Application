# import requests
# import streamlit as st


# def get_groq_response(input_text):
#     json_body={
#   "input": {
#     "language": "French",
#     "text": f"{input_text}"
#   },
#   "config": {},
#   "kwargs": {}
# }
#     # response=requests.post("http://127.0.0.1:8000/chain/invoke",json=json_body)   // for localhost
#     response=requests.post("https://ex-24-llm-application.onrender.com/chain/invoke",json=json_body)

#     response_json=response.json()
#     output = response_json["output"]


#     return output

# ## Streamlit app
# st.title("LLM Application Using LCEL")
# input_text=st.text_input("Enter the text you want to convert to french")
# input_text=st.text_input("Translated Text")
# if input_text:
#     st.write(get_groq_response(input_text))

import requests
import streamlit as st

def get_groq_response(input_text, language):
    json_body = {
        "input": {
            "language": language,
            "text": f"{input_text}"
        },
        "config": {},
        "kwargs": {}
    }
    # Use your Render URL here
    response = requests.post("https://ex-24-llm-application.onrender.com/chain/invoke", json=json_body)

    response_json = response.json()
    output = response_json.get("output", "No output received")  # Handle case where output might not be present

    return output

## Streamlit app
st.title("LLM Application Using LCEL")

# Dropdown for language selection
language_options = [
    "French", "Spanish", "German", "Italian", "Portuguese", 
    "Dutch", "Russian", "Chinese", "Japanese", "Korean"
]  # Add more languages as needed
selected_language = st.selectbox("Select language", language_options)

input_text = st.text_area("Enter the text you want to translate", height=150)

if input_text:
    with st.spinner("Translating..."):
        translated_text = get_groq_response(input_text, selected_language)
        
    # Display the translated text
    st.subheader("Translated Text:")
    st.markdown(f"""
    <div style="
        padding: 10px;
        border: 2px solid #4CAF50;
        border-radius: 5px;
        background-color: #f9f9f9;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    ">
        <p style="font-size: 18px; color: #333;">{translated_text}</p>
    </div>
    """, unsafe_allow_html=True)
