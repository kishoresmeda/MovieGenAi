from pprint import pprint
from langchain.chains import SequentialChain
from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import streamlit as st

import os

openapi_key=st.secrets['OPEN_API_SECRET']
os.environ['OPEN_API_KEY'] = openapi_key

def generate_moviestory_and_review(storyline):

    # Chain 1 to print Movie story
    llm = OpenAI(temperature=0.1, openai_api_key=openapi_key) # temp ranges btw 0 and 1. How create you want the LLM to be. Usually 0.6 or 0.7 is used

    prompt_template_story = PromptTemplate(

        input_variables = ['storyline'],
        template="I want to write a movie story based on the story line - {storyline}. Can you write an engaging story that is not more than 100 words"
    )

    story_chain = LLMChain(llm=llm, prompt=prompt_template_story, output_key="movie_story")

    # Chain 2 to get the review of the generated story from story chain
    prompt_template_review = PromptTemplate(
        input_variables = ['movie_story'],
        template="Write a short review on the movie story -{movie_story} and include a few good points and areas of improvement"
    )

    story_review_chain = LLMChain(llm=llm, prompt=prompt_template_review, output_key="movie_review")

    chain = SequentialChain(
    chains = [story_chain, story_review_chain],
    input_variables = ['storyline'],
    output_variables = ['movie_story', 'movie_review']
    )

    response = chain.invoke({'storyline':storyline})

    return response

if __name__ == "__main__":
    pprint(generate_moviestory_and_review("A son's promise to bring all of the world's gold to his mom"))





