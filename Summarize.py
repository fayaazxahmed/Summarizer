from langchain.chains.question_answering import load_qa_chain
from langchain_openai import ChatOpenAI
from langchain_community.chat_models import ChatOpenAI
from Index import *
from pypdf import PdfReader

def summarize(pdf, min, max, temp):
    if pdf is not None:
        read_pdf = PdfReader(pdf)
        pdf_text = ""
        for page in read_pdf.pages:
            pdf_text += page.extract_text()
        
        extractText = process_text(pdf_text)
        prompt = ("Summarize the content of the uploaded PDF file in %s to %s sentences" %(min,max))

        if prompt:
            #Perform a search for matches within the indexed embeddings 
            knowledgeBase = extractText.similarity_search(prompt)
            ChatGPTModel = "gpt-4o-mini"

            #Temperature ranges from 0 to 1, sets the randomness of the response
            llm = ChatOpenAI(model = ChatGPTModel, temperature = temp)
            
            #Load a question answering chain and pass in the model that will perform the searches
            chain = load_qa_chain(llm, chain_type = "stuff")

            #Run the chain, specify the knowledge base containing the embeddings to be searched and the search prompt itself
            response = chain.run(input_documents = knowledgeBase, question = prompt)
            return response