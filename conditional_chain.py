from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Import tools to build conditional branching logic
from langchain.schema.runnable import RunnableBranch, RunnableLambda

# Import parser to convert LLM output into Pydantic-validated objects
from langchain_core.output_parsers import PydanticOutputParser

# Pydantic is used to define the structured output schema
from pydantic import BaseModel, Field

# Literal defines fixed values the field can accept
from typing import Literal
# Load environment variables from .env file (e.g., OPENAI_API_KEY)
load_dotenv()

# Initialize the LLM (ChatGPT-3.5 by default)
model = ChatOpenAI()

# Parser to convert LLM output into plain text (used later in response generation)
parser = StrOutputParser()

# Define a Pydantic model for structured output
class Feedback(BaseModel):
    # Only allow 'positive' or 'negative' as possible values
    sentiment: Literal['positive', 'negative'] = Field(description='Give the sentiment of the feedback')

# Create a parser that ensures the LLM output conforms to the Feedback schema
parser2 = PydanticOutputParser(pydantic_object=Feedback)

# Prompt to classify feedback sentiment using LLM
prompt1 = PromptTemplate(
    template='Classify the sentiment of the following feedback text into postive or negative \n {feedback} \n {format_instruction}',
    input_variables=['feedback'],
    # Insert parser-generated format instructions as a fixed part of the prompt
    partial_variables={'format_instruction':parser2.get_format_instructions()}
)

# Chain for sentiment classification: Prompt → LLM → Pydantic parser
classifier_chain = prompt1 | model | parser2

# Prompt to generate a response for positive feedback
prompt2 = PromptTemplate(
    template='Write an appropriate response to this positive feedback \n {feedback}',
    input_variables=['feedback']
)

# Prompt to generate a response for negative feedback
prompt3 = PromptTemplate(
    template='Write an appropriate response to this negative feedback \n {feedback}',
    input_variables=['feedback']
)

# Conditional branching logic using RunnableBranch:
# - If sentiment is 'positive' → use prompt2
# - If sentiment is 'negative' → use prompt3
# - Else → return fallback message using RunnableLambda
branch_chain = RunnableBranch(
    (lambda x: x.sentiment == 'positive', prompt2 | model | parser),
    (lambda x: x.sentiment == 'negative', prompt3 | model | parser),
    RunnableLambda(lambda x: "could not find sentiment")
)

# Complete pipeline:
# Step 1: Classify feedback → Step 2: Choose response path based on sentiment
chain = classifier_chain | branch_chain

# Test the full chain with a positive feedback input
print(chain.invoke({'feedback': 'This is a beautiful phone'}))

