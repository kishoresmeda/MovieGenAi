import streamlit as st
import langchain_helper

st.title("A Movie story generator and reviewer")

story_line = st.sidebar.selectbox("Pick a storyline", ("A son's promise to bring all of the world's gold to his mom",
                                                       "A small town boy falls in love with a super rich girl",
                                                       "A cop has to hunt for a group of bank burglers and his love interest is a part of it",
                                                       "A dyslexic boy's extraordinary talent",
                                                       "A mechanical engineer's hard life in a software company"))

if story_line:
    response = langchain_helper.generate_moviestory_and_review(story_line)
    st.header("**Movie Plot**")

    st.write(response['movie_story'].strip())

    st.write("**Movie review**")
    movie_review = response['movie_review'].strip()
    st.write(movie_review)
    