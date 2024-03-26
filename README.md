![image](https://github.com/kishoresmeda/MovieGenAi/assets/3530213/8663091d-ae8d-4df9-96ab-58bfd7852540)


# GenAI Movie Story Generator

This repository contains a GenAI application that generates movie stories based on selected storylines. It utilizes the OpenAI API to access the GPT model.

## Installation

To install the necessary dependencies, run the following command:

```bash
pip install -r requirements.txt
```

## Usage

1. Set up your OpenAI API key by assigning it to the `openapi_key` variable inside `langchain_helper.py` file.
2. Write a baseline story inside the `chain.invoke()` method located in the `langchain_helper.py` file and run it for testing purposes.
3. Once you're ready, run the Streamlit application using the following command:

```bash
streamlit run main.py
```

## Streamlit app usage

Here's how you can generate movie stories using this application:

1. Launch the Streamlit application [here](https://makemymovie.streamlit.app/).
2. Select a storyline from the sidebar and wait for the app to make completion
3. You will see the movie story and also the review of the same in the next section

## Demo

Check out the live demo [here](https://makemymovie.streamlit.app/).
