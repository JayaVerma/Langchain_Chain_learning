# Import the ChatOpenAI model from LangChain (OpenAI wrapper for chat-based models like GPT-3.5/4)
from langchain_openai import ChatOpenAI

# Load environment variables from a .env file (used to securely load your OpenAI API key)
from dotenv import load_dotenv

# Import PromptTemplate for creating dynamic prompts
from langchain_core.prompts import PromptTemplate

# Import a parser to convert the raw LLM output into plain strings
from langchain_core.output_parsers import StrOutputParser

# Load environment variables (e.g., OPENAI_API_KEY)
load_dotenv()

# Step 1: Define the first prompt that takes a topic and asks the LLM to generate a detailed report
prompt1 = PromptTemplate(
    template='Generate a detailed report on {topic}',
    input_variables=['topic']
)

# Step 2: Define the second prompt to summarize the detailed report into 5 bullet points
prompt2 = PromptTemplate(
    template='Generate a 5 pointer summary from the following text \n {text}',
    input_variables=['text']
)

# Initialize the OpenAI chat model (default: gpt-3.5-turbo)
model = ChatOpenAI()

# Define a parser to convert the LLM's output into a clean string
parser = StrOutputParser()

# Build a sequential chain using LangChain's Runnable system
# Step-by-step:
# 1. prompt1 → generates a report from topic
# 2. model → processes the prompt
# 3. parser → cleans output into string
# 4. prompt2 → summarizes the report
# 5. model → generates summary
# 6. parser → cleans final summary
chain = prompt1 | model | parser | prompt2 | model | parser

# Run the entire chain by providing a topic
result = chain.invoke({'topic': 'Unemployment in India'})

# Print the final summarized output (5-point summary)
print(result)

