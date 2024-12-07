from re import search

from dotenv import load_dotenv
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_groq import ChatGroq
import os

from langchain_text_splitters import CharacterTextSplitter, RecursiveCharacterTextSplitter

load_dotenv()

current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, "employees", "portfolio-techstacks.csv")
persistent_directory = os.path.join(current_dir, "db", "chroma_db")

urls = ["https://jobs.nike.com/job/R-41366?from=job%20search%20funnel"]

loader = WebBaseLoader(urls)
document = loader.load()

# text_splitter = RecursiveCharacterTextSplitter(chunk_size= 1000)
# docs = text_splitter.split_documents(document)
#
# print(f"Number of chunks: {len(docs)}")
# print(f"First chunk: \n{docs[1].page_content}")
# print(f"lenth 2 chunk: \n{len(docs[1].page_content)}")


# embeddings = OpenAIEmbeddings(model = "text-embedding-3-small")
#
# if not os.path.exists(persistent_directory):
#     print(f"\n --- Creating vectore store in {persistent_directory} ---")
#     db = Chroma.from_documents(docs, embeddings, persist_directory=persistent_directory)
#     print(f"--- Created vector store in {persistent_directory} ---")
# else:
#     print(f"Vector store at {persistent_directory} already exist")
#     db = Chroma(persist_directory=persistent_directory, embedding_function=embeddings)
#
# retriever = db.as_retriever(
#     search_type = "similarity",
#     search_kwargs = {"k": 3},
# )
#
#
# query = "I need job informations"
#
# relevant_docs = retriever.invoke(query)
#
# print("\n--- Relevant DOcs ---")
# for i, doc in enumerate(relevant_docs, 1):
#     print(f"Document {i}: \n {doc.page_content}\n")
#     if doc.metadata:
#         print(f"Source: {doc.metadata.get('source', 'Unknown')}\n")


model= ChatGroq(model = "llama-3.2-3b-preview")

system_prompt = """The scraped text is from the career's page of a website.
            Your job is  to extract the job postings and return them in JSON format containing the following keys: `role`, `experience`, `skills` and `description`.
            Only return the valid JSON."""

messages = [
    SystemMessage(content = system_prompt),
    HumanMessage(content= str(document))
]

result = model.invoke(messages)

print("Full result:", result)
print("Only content:", result.content)