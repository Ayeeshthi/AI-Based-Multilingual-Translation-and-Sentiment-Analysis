import streamlit as st
from translate import Translator
from textblob import TextBlob

# Add custom CSS for enhanced UI
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap');

    .stApp {
        background: linear-gradient(135deg, #000000, #1a1a1a);
        color: #FFFFFF;
        font-family: 'Poppins', sans-serif;
    }
    .stButton>button {
        background-color: #1E90FF;
        color: white;
        font-weight: bold;
        border-radius: 10px;
        padding: 10px 20px;
        border: 2px solid #FFFFFF;
        transition: background-color 0.3s, transform 0.3s;
    }
    .stButton>button:hover {
        background-color: #00BFFF;
        transform: scale(1.05);
    }
    .stTextInput>div>div>input, .stTextArea>div>textarea {
        background-color: #333333;
        color: white;
        font-size: 18px;
        padding: 15px;
        border-radius: 10px;
        border: 1px solid #FFFFFF;
    }
    .stSidebar {
        background-color: #1a1a1a;
    }
    .stSidebar h1, .stSidebar h2, .stSidebar h3, .stSidebar h4, .stSidebar h5, .stSidebar h6 {
        color: #FFFFFF;
    }
    .result-card {
        background-color: #262626;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0px 4px 15px rgba(0, 0, 0, 0.2);
        margin: 20px 0;
    }
    footer {
        font-family: 'Poppins', sans-serif;
        text-align: center;
        padding: 10px;
        font-size: 14px;
        color: #888;
    }
    </style>
""", unsafe_allow_html=True)

# Streamlit App
def main():
    st.title("Real-Time Translation with Sentiment Analysis")

    # Sidebar options for languages
    st.sidebar.header("Translation Settings")
    source_lang = st.sidebar.selectbox("Select Source Language", [
        "en", "es", "fr", "de", "zh", "hi", "ar", "ru", "ja", "ko", "it", "pt", "nl", "sv", "tr"
    ])
    target_lang = st.sidebar.selectbox("Select Target Language", [
        "en", "es", "fr", "de", "zh", "hi", "ar", "ru", "ja", "ko", "it", "pt", "nl", "sv", "tr"
    ])

    st.subheader("Enter Text to Translate:")
    user_input = st.text_area("")

    if st.button("Translate"):
        if user_input:
            # Perform translation using the translate package
            translator = Translator(from_lang=source_lang, to_lang=target_lang)
            translation = translator.translate(user_input)
            
            # Sentiment Analysis using TextBlob
            blob = TextBlob(user_input)
            sentiment = blob.sentiment.polarity
            
            # Display the results in a card
            st.markdown("<div class='result-card'>", unsafe_allow_html=True)
            st.subheader("Translation")
            st.write(translation)
            st.subheader("Sentiment Analysis")
            if sentiment > 0:
                st.write("Positive")
            elif sentiment < 0:
                st.write("Negative")
            else:
                st.write("Neutral")
            st.markdown("</div>", unsafe_allow_html=True)
        else:
            st.error("Please enter text for translation.")

    # Footer
    st.markdown("<footer>Powered by Streamlit | Designed by Mohammed Rayyan Ahmed</footer>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
