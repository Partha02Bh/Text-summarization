# import cohere

# # Initialize the Cohere client with your API key
# co = cohere.Client("rujUGkqF0GNqEoaU4ifFy2i7oUlUKT4mAgaoJaG4")  # Replace with your Cohere API key

# # Function to summarize text using Cohere
# def summarize_text(input_text):
#     # Create a prompt asking for summarization
#     prompt = f"Summarize the following text:\n\n{input_text}"

#     # Use cohere.generate() to get a summary (model='command-xlarge' is the most common for general tasks)
#     response = co.generate(
#         model='command-xlarge',  # Use the model for generation (command-xlarge is often used)
#         prompt=prompt,  # Provide the summarization prompt
#         max_tokens=150,  # Limit the length of the summary
#         temperature=0.7,  # Adjust creativity; lower for more deterministic output
#         stop_sequences=["\n"]  # Stop after generating the summary
#     )

#     # Extract and return the summary from the response
#     summary = response.generations[0].text.strip()
#     return summary

# # Example input text
# input_text = """
# Cohere is a machine learning company that focuses on natural language processing (NLP) technology. 
# Their core product is an API that enables developers to build AI-powered applications, including text generation, summarization, and sentiment analysis. 
# The company was founded in 2019 and has rapidly gained recognition for its state-of-the-art NLP models. 
# Their models are built on cutting-edge research and provide powerful tools for businesses and developers working with text-based data.
# """

# # Call the summarization function
# summary = summarize_text(input_text)
# print("Summary:")
# print(summary)


import streamlit as st
import cohere

# Initialize the Cohere client
API_KEY = "    "  # Replace with your Cohere API key
co = cohere.Client("rujUGkqF0GNqEoaU4ifFy2i7oUlUKT4mAgaoJaG4")

# Streamlit app
st.title("Text Summarization with Cohere")

# Input text box
input_text = st.text_area("Enter text to summarize:", height=200)

# Button to trigger summarization
if st.button("Summarize"):
    if input_text.strip():
        try:
            # Call the summarize endpoint
            response = co.summarize(
                text=input_text,  # Input text to summarize
                length="medium",  # Options: 'short', 'medium', 'long'
                format="paragraph"  # Format options: 'paragraph', 'bullets'
            )
            # Display the summary
            summary = response.summary.strip()
            st.subheader("Summary:")
            st.write(summary)
        except Exception as e:
            st.error(f"Error summarizing text: {e}")
    else:
        st.warning("Please enter some text to summarize.")
