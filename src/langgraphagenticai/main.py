import streamlit as st
import os
from src.langgraphagenticai.ui.streamlitui.loadui import LoadStreamlitUI
from src.langgraphagenticai.LLMS.groqllm import GroqLLM
from src.langgraphagenticai.graph.graph_builder import GraphBuilder
from src.langgraphagenticai.ui.streamlitui.display_result import DisplayResultStreamlit
def load_langgraph_agenticai_app():
    ui=LoadStreamlitUI()
    user_input=ui.load_streamlit_ui()

    if not user_input:
        st.error("Error: LLM model could not be initiated")
        return
    
    user_message=st.chat_input("Enter your message")  #st.chat_message("Enter your message",width="stretch")
    #st.write(user_message)
    if user_message:
        try:
           # st.write(user_input)
            obj_llm_config=GroqLLM(user_controls_input=user_input)
           # st.write(obj_llm_config)
            model=obj_llm_config.get_llm_model()
            #st.write(model)
            if not model:
                st.error("Error: LLM model could not be initialized")
                return
            
            usecase=user_input.get('selected_Usercases')
            if not usecase:
                st.error("Error: no use case selected")
            #st.write(model)
            #st.write(usecase)
           # graph_builders= GraphBuilder(model)
            #st.write(graph_builders)
            try:
                #graph=graph_builders.setup_graph(usecase)
                #st.write(graph)
                DisplayResultStreamlit(usecase,model,user_message).display_result_on_ui()

            except Exception as e:
                st.error(f"Error:ABCD,{e}")    

        except Exception as e:    
            st.error(f"EFGH,{e}")
    
