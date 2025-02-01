import streamlit as st
import google.generativeai as genai
import os

from dotenv import load_dotenv
load_dotenv()



genai.configure(api_key=os.getenv('GENAI_API_KEY'))

generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 40,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
    model_name="gemini-1.5-pro",
    generation_config=generation_config,
    system_instruction="""
    Welcome to Linga AI Solutions! PVT. LTD. We specialize in AI and robotics solutions, offering cutting-edge products such as AI-powered restaurant service robots, retail assistant bots, and industrial automation solutions. Our chatbot can help you explore our products, inquire about pricing and custom solutions, get technical support, learn about career and internship opportunities, or contact us for business inquiries.
    Whether you need a conversational AI assistant, object detection models, or automation tools, we provide tailored solutions to meet your needs. If you're looking for setup guidance, software updates, or troubleshooting, we’re here to assist.
    Interested in joining our AI and robotics team? Check out our career and internship programs.
    For any questions, feel free to reach us via email at lingalingeswaran@gmail.com, by phone at 0774157029, or visit our website at LingaAIsolutions.com and the Company is in Moratuwa. Mr. Lingeswaran is the CEO of the company.He is a Moratuwa University Engineering graduate.He graduated as an engineer from University of Moratuwa Faculty of Engineering.
    Welcome to Linga AI Solutions PVT.LTD 😊""",
)

chat_session = model.start_chat(history=[])

# Streamlit UI
st.title("Linga AI Solutions Chatbot")
st.write("Ask me anything about our AI and robotics solutions! 😊")

# Initialize chat history in Streamlit session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["text"])

# User input
user_input = st.chat_input("Type your message here...")
if user_input:
    # Append user message
    st.session_state.messages.append({"role": "user", "text": user_input})
    with st.chat_message("user"):
        st.write(user_input)
    
    # Get response
    response = chat_session.send_message(user_input)
    bot_reply = response.text
    
    # Append model response
    st.session_state.messages.append({"role": "model", "text": bot_reply})
    with st.chat_message("model"):
        st.write(bot_reply)
