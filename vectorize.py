# https://python.langchain.com/docs/modules/data_connection/vectorstores/integrations/mongodb_atlas

from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.document_loaders import WebBaseLoader
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import MongoDBAtlasVectorSearch
from langchain.embeddings import HuggingFaceEmbeddings
from pymongo import MongoClient
import params

# Step 1: Load
# loaders = [
#  WebBaseLoader("https://en.wikipedia.org/wiki/AT%26T"),
#  WebBaseLoader("https://en.wikipedia.org/wiki/Bank_of_America")
# ]
# data = []
# for loader in loaders:
#     data.extend(loader.load())

loader = PyPDFLoader("https://arxiv.org/pdf/2303.08774.pdf")
data = loader.load()

# Step 2: Transform (Split)
# text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=0, separators=[
#                                                "\n\n", "\n", "(?<=\. )", " "], length_function=len)
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
docs = text_splitter.split_documents(data)
print('Split into ' + str(len(docs)) + ' docs')

# Step 3: Embed
# https://api.python.langchain.com/en/latest/embeddings/langchain.embeddings.openai.OpenAIEmbeddings.html
embeddings = OpenAIEmbeddings(openai_api_key=params.openai_api_key, disallowed_special=())
# #Load the Embedding Model
# embeddings=HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2', 
#                                  model_kwargs={'device':'cpu'})

# Step 4: Store
# Initialize MongoDB python client
client = MongoClient(params.mongodb_conn_string)
collection = client[params.db_name][params.collection_name]

# Reset w/out deleting the Search Index 
collection.delete_many({})

# Insert the documents in MongoDB Atlas with their embedding
# https://github.com/hwchase17/langchain/blob/master/langchain/vectorstores/mongodb_atlas.py
docsearch = MongoDBAtlasVectorSearch.from_documents(
    docs, embeddings, collection=collection, index_name=params.index_name
)

