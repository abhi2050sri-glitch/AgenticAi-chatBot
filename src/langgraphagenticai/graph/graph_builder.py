
from langgraph.graph import StateGraph,START,END
from  src.langgraphagenticai.state.state import State
from src.langgraphagenticai.nodes.basic_chatbot_node import BasicCHatBotNode
import streamlit as st
class GraphBuilder:
    def __init__(self,model):
        self.llm=model
        self.graph_builder=StateGraph(State)


    def basic_chatbot_build_graph(self):
        self.basic_chatbot_node=BasicCHatBotNode(self.llm)
        #st.write(self.basic_chatbot_node)
        self.graph_builder.add_node("chatbot",self.basic_chatbot_node.process)
        self.graph_builder.add_edge(START,"chatbot")
        self.graph_builder.add_edge("chatbot",END)

    def setup_graph(self,usercase):
     
        if(usercase=="Basic Chatbot"):
            #st.write(usercase)
            self.basic_chatbot_build_graph()    

        return self.graph_builder.compile()   