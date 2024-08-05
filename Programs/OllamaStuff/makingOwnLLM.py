from langchain.document_loaders import DirectoryLoader

dataPath = "data/books"


# this makes each of the data md files into documents
def load_docs():
    loader = DirectoryLoader(dataPath, glob="*.md")
    documents = loader.load()
    return documents

# this splits said documents into smaller pieces
text_splitter = RecursiveCharacterTextSplitter(
    chunkSize = 1000,
    chunkOverlap = 500,
    lengthFunction = len,
    addStartIndex = True,
)

chunks = text_splitter.split_documents(documents)