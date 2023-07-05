from langchain.document_loaders import OutlookMessageLoader

loader = OutlookMessageLoader()

data = loader.load()

