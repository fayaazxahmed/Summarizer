# Summarizer
This project uses the Hugging Face Sentence Transformation LLM to create text embeddings from the text in the attached PDF file. Once embdeddings have been crated for the entire file, the OpenAI API is prompted to search through the embeddings for pieces of text that contain information that is relevant when summarizing the contents of the file. The OpenAI prompt results are passed to the LangChain Question Answer Chain along with the embeddings created by the Hugging Face LLM to create and return a summary of the contents of the PDF file.

To run this program, run the following command:
```
streamlit run Main.py
```
