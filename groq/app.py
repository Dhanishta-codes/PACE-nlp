import streamlit as st

# Sample extracted content from the "PDF"
texts = ["""
The NASA PACE (Plankton, Aerosol, Cloud, ocean Ecosystem) mission is a critical effort to understand global climate change. PACE provides measurements of clouds, aerosols, and ocean ecosystems to better predict climate dynamics and human impacts on the environment.

Key objectives include:
1. Understanding how aerosols influence the Earth's climate.
2. Studying the role of ocean ecosystems in regulating carbon in the atmosphere.

This mission is essential for improving our understanding of climate change and developing mitigation strategies.
"""]

# Function to find relevant text based on user query with improved matching
def find_relevant_texts(query, texts):
    relevant_texts = []
    query_words = query.lower().split()  # Split query into words

    for text in texts:
        text_lower = text.lower()
        if any(word in text_lower for word in query_words):  # Match any word from the query
            relevant_texts.append(text)
    
    return relevant_texts

# Streamlit app title
st.title("NASA PACE Chatbot")

# Input box for user question
prompt1 = st.text_input("Enter your question from the NASA PACE mission documents")

# Button to trigger chatbot logic
if st.button("Get Answer"):
    # Search for relevant text based on the user input
    relevant_texts = find_relevant_texts(prompt1, texts)
    
    if relevant_texts:
        st.write("Relevant Information:")
        for text in relevant_texts:
            st.write(text)  # Display relevant results
    else:
        st.write("Sorry, no information found for that question.")
