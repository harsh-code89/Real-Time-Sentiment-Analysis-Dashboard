import streamlit as st
from sentiment import analyze_sentiment

def main():
    # Set up the Streamlit app layout
    st.set_page_config(page_title="Real-Time Sentiment Analysis Dashboard", layout="centered")

    # Title and description
    st.title("Real-Time Sentiment Analysis Dashboard")
    st.write("Analyze the sentiment of your text in real-time using TextBlob or VADER.")

    # Sidebar for method selection
    st.sidebar.title("Settings")
    method = st.sidebar.selectbox("Choose Sentiment Analysis Method", ["TextBlob", "VADER"])

    # Text input
    user_input = st.text_area("Enter text to analyze:", "Type your text here...")

    if st.button("Analyze Sentiment"):
        if user_input.strip():
            # Perform sentiment analysis
            result = analyze_sentiment(user_input, method=method.lower())

            # Display results
            st.subheader("Sentiment Analysis Result")
            st.write(f"**Sentiment Label:** {result['label']}")
            st.write(f"**Sentiment Score:** {result['score']:.2f}")
        else:
            st.warning("Please enter some text to analyze.")

if __name__ == "__main__":
    main()
