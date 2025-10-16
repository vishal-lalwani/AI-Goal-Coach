import streamlit as st
from transformers import pipeline
from ddgs import DDGS

# Load model
@st.cache_resource
def load_model():
    return pipeline(
        "text2text-generation",
        model="google/flan-t5-base",
        device_map="cpu",
        max_new_tokens=300,
    )

generator = load_model()

def search_resources(goal, max_results=3):
    links = []
    with DDGS() as ddgs:
        for r in ddgs.text(f"{goal} tutorials or learning resources", max_results=max_results):
            title = r.get("title", "Untitled")
            link = r.get("href") or r.get("link") or ""
            if link:
                links.append(f"- [{title}]({link})")
            else:
                links.append(f"- {title}")
    return "\n".join(links) if links else "No relevant results found."

# Streamlit UI
st.set_page_config(page_title="AI Goal Coach", layout="centered")
st.title("AI Goal Coach")

st.markdown("Get a **7-day learning plan** for your goal + useful web resources")

goal = st.text_input("Enter your goal (e.g., Learn Python, Build a fitness habit):")

if st.button("Generate Plan") and goal:
    with st.spinner("Thinking..."):
        prompt = f"""
        You are an expert AI coach. Create a 7-day plan to achieve the goal: "{goal}".
        Each day must include:
        1. Focus area
        2. Actionable task
        3. Motivation tip
        Output in a clean, bullet-point format.
        """
        try:
            response = generator(prompt)[0]["generated_text"]
            st.success("Here's your plan:")
            st.markdown(response.replace("\n", "  \n"))

            st.markdown("---")
            st.subheader("Helpful Resources")
            st.markdown(search_resources(goal))
        except Exception as e:
            st.error(f"Error: {e}")

st.caption("Built with HuggingFace Flan-T5 + Streamlit + DuckDuckGo Search")
