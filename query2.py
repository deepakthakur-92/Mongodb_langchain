import argparse
import params
from pymongo import MongoClient
from langchain.vectorstores import MongoDBAtlasVectorSearch
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.llms import OpenAI
from langchain.retrievers import ContextualCompressionRetriever
from langchain.retrievers.document_compressors import LLMChainExtractor
from langchain.embeddings import HuggingFaceEmbeddings
import warnings

# # Filter out the UserWarning from langchain
# warnings.filterwarnings("ignore", category=UserWarning, module="langchain.chains.llm")

# # Process arguments
# parser = argparse.ArgumentParser(description='Atlas Vector Search Demo')
# parser.add_argument('-q', '--question', help="The question to ask")
# args = parser.parse_args()

# if args.question is None:
#     # Some questions to try...
#     query = "How big is the telecom company?"
#     query = "Who started AT&T?"
#     #query = "Where is AT&T based?"
#     #query = "What venues are AT&T branded?"
#     #query = "How big is BofA?"
#     #query = "When was the financial institution started?"
#     #query = "Does the bank have an investment arm?"
#     #query = "Where does the bank's revenue come from?"
#     #query = "Tell me about charity."
#     #query = "What buildings are BofA branded?"

# else:
#     query = args.question

# print("\nYour question:")
# print("-------------")
# print(query)

# Initialize MongoDB python client
client = MongoClient(params.mongodb_conn_string)
collection = client[params.db_name][params.collection_name]

embeddings=HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2', 
                                 model_kwargs={'device':'cpu'})

# initialize vector store
vectorStore = MongoDBAtlasVectorSearch(
    collection, embeddings, index_name=params.index_name
)

query = "Who started AT&T?"
results = vectorStore.similarity_search(query)
print(results[0].page_content)

