from typing import TypedDict
from langchain_community.chat_models import ChatOllama
from langchain_core.prompts import PromptTemplate
from langgraph.graph import StateGraph, END

# 1. Define the State
class PipelineState(TypedDict):
    document_text: str
    compliance_rules: str
    analysis_report: str

# 2. Initialize the Local Free LLM (Ollama)
llm = ChatOllama(
    model="llama3", 
    temperature=0.1
)

# 3. Define the Node Functions
def check_compliance(state: PipelineState) -> dict:
    prompt = PromptTemplate.from_template(
        "You are a compliance officer. Review the following document against these rules.\n\n"
        "Rules:\n{rules}\n\n"
        "Document:\n{document}\n\n"
        "Generate a detailed compliance report. List violations, if any."
    )
    
    chain = prompt | llm
    result = chain.invoke({
        "rules": state["compliance_rules"],
        "document": state["document_text"]
    })
    
    return {"analysis_report": result.content}

# 4. Build the Graph
workflow = StateGraph(PipelineState)
workflow.add_node("analyze_compliance", check_compliance)
workflow.set_entry_point("analyze_compliance")
workflow.add_edge("analyze_compliance", END)

compliance_pipeline = workflow.compile()