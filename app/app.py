import streamlit as st
from pipeline.pipeline import AnimeRecommendationPipeline
from dotenv import load_dotenv
import os



st.set_page_config(page_title="Anime Recommender",layout="wide")

load_dotenv()

@st.cache_resource
def init_pipeline():
    return AnimeRecommendationPipeline()

pipeline = init_pipeline()

st.title("Anime Recommender System")

query = st.text_input("Enter Your Anime preferences eg: light hearted anime with school setting")

if query:
    with st.spinner("Fetching Recommendation........"):
        response = pipeline.recommend(query)
        st.markdown("### Recommended Anime")
        st.write(response)