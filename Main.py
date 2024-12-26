import streamlit as st
import os
from Summarize import *

#Right click to run with Streamlit
def main():
    st.set_page_config(page_title="Summarizer")
    st.title("PDF Summarizer")

    minimum = st.number_input("Minimum Number of Sentences", min_value = 1, step=1)
    maximum = st.number_input("Maximum Number of Sentences", min_value = minimum, step=1)
    temp = st.slider("Set Temperature",  min_value = 0.0, max_value = 1.0, value = 0.5, step=0.1)

    file = st.file_uploader("Attach File", type="pdf")
    generate = st.button("Generate Summary")

    os.environ["OPENAI_API_KEY"] = "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"

    if generate:
        st.divider()

        try:
            response = summarize(file, minimum, maximum, temp)
            st.subheader("Generated Summary of Attached File:")
            st.write(response)
        
        
        except:
            response = "Error. Summary could not be generated"
            st.subheader("Generated Summary of Attached File:")
            st.write(response)
        

if __name__ == "__main__":
    main()