import streamlit as st
import google.generativeai as genai

# Dán Key vào đây
genai.configure(api_key="AIzaSyANU1NJC7CZxy9tQIqBlWWdYMcx0-71JBo")
model = genai.GenerativeModel('gemini-1.5-flash')

st.title("📖 StoryAI: Xây Dựng Truyện")

if "chat" not in st.session_state:
    st.session_state.chat = model.start_chat(history=[])

# Nhập bối cảnh
theme = st.text_input("Nhập bối cảnh (VD: Tu tiên, Mạt thế, Cyberpunk):")
if st.button("Bắt đầu hành trình"):
    prompt = f"Viết chương 1 cho bối cảnh: {theme}. Viết chi tiết, văn phong tiểu thuyết, có hội thoại và kết thúc bằng 3 lựa chọn cho người chơi."
    response = st.session_state.chat.send_message(prompt)
    st.write(response.text)

# Phần chơi tiếp
user_action = st.text_input("Bạn làm gì tiếp theo hoặc chọn 1 trong 3 lựa chọn trên?")
if st.button("Viết chương tiếp theo"):
    response = st.session_state.chat.send_message(user_action)
    st.write(response.text)
