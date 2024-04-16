# LangChain MongoDB Atlas Integration

This repository provides an example of integrating LangChain with MongoDB Atlas for storing and searching document embeddings.

## Installation
### Clone the repository:

```
git clone https://github.com/your_username/your_repository.git
cd your_repository
```

### Create a virtual environment:

```
conda create -n cpullama python=3.8 -y
conda activate cpullama
```

### Install requirements:

```
pip install -r requirements.txt
```

### Querying the Database

To query the database for similar documents, run the following command:

```
python query.py
```

## Usage

This code demonstrates the process of loading documents, splitting them into chunks, embedding the chunks, and storing them in MongoDB Atlas for later similarity search.

1. **Load Documents**: The documents can be loaded from various sources such as web pages or PDF files. In this example, a PDF loader is used.

2. **Split Documents**: The loaded documents are split into smaller chunks for better processing.

3. **Embedding**: The text chunks are embedded using OpenAI's embedding model.

4. **Store in MongoDB Atlas**: The embedded chunks are stored in a MongoDB Atlas database for efficient similarity search.