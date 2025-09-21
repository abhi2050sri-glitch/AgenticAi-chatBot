import streamlit as st
from langchain_core.messages import HumanMessage, AIMessage

class DisplayResultStreamlit:
    def __init__(self, usecase, graph, user_message):
        self.usecase = usecase
        self.graph = graph
        self.user_message = user_message

    def display_result_on_ui(self):
        st.write("🚀 Chatbot Activated")

        if "chat_history" not in st.session_state:
            st.session_state.chat_history = []

        if self.usecase == "Basic Chatbot":
            # Add user message to history
            st.session_state.chat_history.append(HumanMessage(content=self.user_message))

            # Invoke graph with full history
            try:
                response = self.graph.invoke(st.session_state.chat_history)
                st.session_state.chat_history.append(response)  # response is likely an AIMessage
            except Exception as e:
                st.error(f"Error during response streaming: {e}")
                return

            # Display full chat history
            for msg in st.session_state.chat_history:
                role = "user" if isinstance(msg, HumanMessage) else "assistant"
                with st.chat_message(role):
                    st.write(msg.content)