# LangChain MongoDB Atlas Integration

This repository provides an example of integrating LangChain with MongoDB Atlas for storing and searching document embeddings.

## Installation
### Clone the repository:

```
git clone https://github.com/your_username/your_repository.git
```

### Create a virtual environment:

```
conda create -n venv python=3.8 -y
conda activate venv
```

### Install requirements:

```
pip install -r requirements.txt
```

### Load, transform, embed and store

```
python vectorize.py
```

### Querying the Database

To query the database for similar documents, run the following command:

```
python query.py
```

## To create a search index on the stored embeddings

[Index the vector embeddings](https://www.mongodb.com/developer/languages/python/semantic-search-made-easy-langchain-mongodb/?utm_campaign=devrel&utm_source=youtube&utm_medium=organic_social&utm_content=ZvwUzcMvKiI&utm_term=jay.javed)

## Usage

This code demonstrates the process of loading documents, splitting them into chunks, embedding the chunks, and storing them in MongoDB Atlas for later similarity search.

1. **Load Documents**: The documents can be loaded from various sources such as web pages or PDF files. In this example, a PDF loader is used.

2. **Split Documents**: The loaded documents are split into smaller chunks for better processing.

3. **Embedding**: The text chunks are embedded using OpenAI's embedding model.

4. **Store in MongoDB Atlas**: The embedded chunks are stored in a MongoDB Atlas database for efficient similarity search.