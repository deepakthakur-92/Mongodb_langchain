import argparse
import params
from pymongo import MongoClient
from langchain.vectorstores import MongoDBAtlasVectorSearch
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.llms import OpenAI
from langchain.retrievers import ContextualCompressionRetriever
from langchain.embeddings import HuggingFaceEmbeddings
import warnings



# Initialize MongoDB python client
client = MongoClient(params.mongodb_conn_string)
collection = client[params.db_name][params.collection_name]

embeddings=OpenAIEmbeddings(openai_api_key=params.openai_api_key)

# initialize vector store
vectorStore = MongoDBAtlasVectorSearch(
    collection, embeddings, index_name=params.index_name
)

#query = "What were the computing requirements for training gpt4"
query = "What is the scope and limitation of gpt4"
results = vectorStore.similarity_search(query)
print(results[0].page_content)

