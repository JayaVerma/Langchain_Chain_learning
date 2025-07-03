from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Import RunnableParallel for running multiple chains in parallel
from langchain.schema.runnable import RunnableParallel

# Load environment variables from the .env file (especially the OpenAI API key)
load_dotenv()

# Initialize the chat model (uses GPT-3.5 by default)
model1 = ChatOpenAI()

# Define a prompt to generate short notes from the input text
prompt1 = PromptTemplate(
    template='Generate short and simple notes from the following text \n {text}',
    input_variables=['text']
)

# Define a prompt to generate 5 short Q&A from the same input text
prompt2 = PromptTemplate(
    template='Generate 5 short question answers from the following text \n {text}',
    input_variables=['text']
)

# Define a prompt to merge both notes and quiz into a final document
prompt3 = PromptTemplate(
    template='Merge the provided notes and quiz into a single document \n notes -> {notes} and quiz -> {quiz}',
    input_variables=['notes', 'quiz']
)

# Output parser to clean and extract string from LLM responses
parser = StrOutputParser()

# Create a parallel chain to run prompt1 and prompt2 at the same time
# Output will be a dict: {'notes': <LLM result>, 'quiz': <LLM result>}
parallel_chain = RunnableParallel({
    'notes': prompt1 | model1 | parser,
    'quiz': prompt2 | model1 | parser
})

# After both outputs are available, feed them into prompt3 to merge
merge_chain = prompt3 | model1 | parser

# Connect both chains: first run parallel_chain, then run merge_chain on its result
chain = parallel_chain | merge_chain

# Input text (about Support Vector Machines)
text = """
Support vector machines (SVMs) are a set of supervised learning methods used for classification, regression and outliers detection.

The advantages of support vector machines are:

Effective in high dimensional spaces.

Still effective in cases where number of dimensions is greater than the number of samples.

Uses a subset of training points in the decision function (called support vectors), so it is also memory efficient.

Versatile: different Kernel functions can be specified for the decision function. Common kernels are provided, but it is also possible to specify custom kernels.

The disadvantages of support vector machines include:

If the number of features is much greater than the number of samples, avoid over-fitting in choosing Kernel functions and regularization term is crucial.

SVMs do not directly provide probability estimates, these are calculated using an expensive five-fold cross-validation (see Scores and probabilities, below).

The support vector machines in scikit-learn support both dense (numpy.ndarray and convertible to that by numpy.asarray) and sparse (any scipy.sparse) sample vectors as input. However, to use an SVM to make predictions for sparse data, it must have been fit on such data. For optimal performance, use C-ordered numpy.ndarray (dense) or scipy.sparse.csr_matrix (sparse) with dtype=float64.
"""

# Run the full chain with the given text input
# Output: Final document merging both notes and quiz
result = chain.invoke({'text': text})

# Print the final output
print(result)