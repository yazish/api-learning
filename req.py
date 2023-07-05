import requests
import os
import openai
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

OPENAI_API_KEY = "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"


openAiKey = OPENAI_API_KEY
openai.api_key = OPENAI_API_KEY

llm = OpenAI(openai_api_key=openAiKey,model_name="gpt-3.5-turbo")

chat = ChatOpenAI(openai_api_key=openAiKey,model_name="gpt-3.5-turbo")

print(llm.predict("what should be the name of a company which make personal chatbots?"))
i = openai.Image.create(
  prompt="A cute baby sea otter",
  n=2,
  size="1024x1024"
)
print(i)



# # prompt = PromptTemplate.from_template("What is a good name for a company that makes {product}?")
# # inp = prompt.format(product="colorful socks")

# # llm.predict(inp)


# template = """Answer the question based on the context below. If the
# question cannot be answered using the information provided answer
# with "I don't know".

# Context: Large Language Models (LLMs) are the latest models used in NLP.
# Their superior performance over smaller models has made them incredibly
# useful for developers building NLP enabled applications. These models
# can be accessed via Hugging Face's `transformers` library, via OpenAI
# using the `openai` library, and via Cohere using the `cohere` library.

# Question: {query}

# Answer: """

# prompt_template = PromptTemplate(
#     input_variables=["query"],
#     template=template
# )


# prompt_template.format(query="Which libraries and model providers offer LLMs?")
