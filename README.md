# PART 1 
## LangChain Sequential Chain — Report and Summary Generator

This part demonstrates how to build a **Sequential Chain in LangChain** using the `Runnable` interface. It walks through how to:

* Take a topic input
* Generate a detailed report using an LLM
* Summarize the report into 5 bullet points

Built using `LangChain`, `OpenAI`, and Python, this is a great starting point to understand **multi-step LLM workflows**.

---

### Key Features

 - Uses `PromptTemplate` to create dynamic, reusable prompts
 - Chains multiple steps using the `|` operator (RunnableSequence)
 - Applies `StrOutputParser` to clean raw LLM responses
 - Demonstrates end-to-end flow: **Topic → Report → Summary**
 - Visualizes the full chain structure using `.get_graph().print_ascii()`

---

### How It Works

1. **Prompt 1**: Ask the LLM to generate a detailed report on a given topic.
2. **Prompt 2**: Summarize that report into 5 concise bullet points.
3. **Model**: `ChatOpenAI` (can be swapped with any other LangChain-supported LLM).
4. **Parser**: Cleans LLM output for passing between steps.

### Flow:

```
User Input → PromptTemplate 1 → LLM → Parser → PromptTemplate 2 → LLM → Parser → Output
```

## 🔐 Setup `.env`

Create a `.env` file in the project root with your OpenAI API key:

```
OPENAI_API_KEY=your-openai-api-key
```

---

## 🚀 Run the Script

```bash
python sequential_chain.py
```

---

## 🧰 File Overview

| File        | Description                                               |
| ----------- | --------------------------------------------------------- |
| `main.py`   | Contains the sequential chain logic and example execution |
| `.env`      | Stores your API key securely (not committed to git)       |
| `README.md` | Documentation and usage instructions                      |

---

# PART 2

## LangChain Parallel-Merge Chain — Notes + Quiz Generator

This project demonstrates how to use **LangChain's `RunnableParallel` and prompt chaining** to generate both:

* Concise notes
* Quiz questions
  from a given input text using a Large Language Model (LLM).

The results from these two parallel tasks are then **merged into a single document**, forming an efficient and intelligent content generation pipeline — perfect for study tools, summarizers, or learning assistants.

---

### Key Highlights

- Uses **RunnableParallel** to run two prompt chains at the same time
- Generates **notes** and **Q\&A** from the same input
- Merges both outputs using another prompt and model
- Shows the power of **LangChain’s Runnable system**

---

## How It Works

```
INPUT TEXT
   │
   ├──▶ Prompt 1: Generate notes       ┐
   │                                   ├──▶ Parallel execution using RunnableParallel
   └──▶ Prompt 2: Generate quiz        ┘
           │
       ┌── Merged using Prompt 3 (notes + quiz)
       │
       ▼
   FINAL OUTPUT (single document)
```

---

## Project Structure

| File        | Description                                                      |
| ----------- | ---------------------------------------------------------------- |
| `main.py`   | Contains the full LangChain pipeline with parallel + merge logic |
| `.env`      | Stores the OpenAI API key securely                               |
| `README.md` | Project documentation and instructions                           |

---

### How to Run

```bash
python parallel_chain.py
```

Expected Output:
A structured document that includes both generated notes and a quiz from the input educational content.


### Visualize Chain Structure

The script prints an ASCII diagram of the pipeline:

```
             text
              │
    ┌─────────┴─────────┐
    ▼                   ▼
prompt1              prompt2
  │                    │
 model                model
  │                    │
parser               parser
    └─────────┬─────────┘
              ▼
           prompt3
              │
            model
              │
           parser
```

---

Absolutely! Here's a complete and well-structured `README.md` for your **LangChain Conditional Branching Chatbot**, built on sentiment classification + response generation.

---
# PART 3

## LangChain Conditional Feedback Responder

**Classify → Branch → Respond** with LLMs using LangChain's `RunnableBranch`

---

This project demonstrates a smart LLM pipeline that:

1. Classifies the **sentiment** of user feedback (positive or negative)
2. **Conditionally routes** the workflow based on sentiment
3. Generates an appropriate **automated response**

Built using **LangChain**, **OpenAI**, and **Pydantic**, it showcases how to **combine structured output + conditional logic + prompt chaining**.

---

### Key Features

- Uses `PydanticOutputParser` to classify structured sentiment
- Implements **conditional logic** using `RunnableBranch`
- Generates context-aware replies using dynamic `PromptTemplate`
- Modular design using LangChain's `Runnable` API
- Includes a fallback route when sentiment isn't identified

---

### Workflow Overview

```
User Feedback (text)
     │
     ▼
[Prompt 1] → Classify Sentiment → 'positive' or 'negative'
     │
     └──────────────┬───────────────┐
                    ▼               ▼
     [Prompt 2: Reply for Positive] [Prompt 3: Reply for Negative]
                    │               │
                    ▼               ▼
              Final AI Response (based on condition)
```

---

### File Structure

| File        | Description                                             |
| ----------- | ------------------------------------------------------- |
| `main.py`   | Main script with conditional logic using RunnableBranch |
| `.env`      | Store your OpenAI API Key (excluded from Git)           |
| `README.md` | Documentation & usage guide                             |

---

### Core Components Explained

| Component              | Purpose                                               |
| ---------------------- | ----------------------------------------------------- |
| `ChatOpenAI()`         | Base LLM used for both classification and generation  |
| `PromptTemplate`       | Used to create flexible prompts for each task         |
| `PydanticOutputParser` | Enforces structured output from the model (sentiment) |
| `RunnableBranch`       | Applies routing logic based on sentiment              |
| `RunnableLambda`       | Acts as fallback in case sentiment isn't detected     |

---

### Future Ideas

* Add neutral sentiment classification
* Log outputs for feedback improvement
* Convert to a **Streamlit app** with chat UI
* Extend with multilingual support or sarcasm detection

---

### Requirements

* Python 3.8+
* OpenAI API Key
* `langchain`, `langchain_openai`, `python-dotenv`


