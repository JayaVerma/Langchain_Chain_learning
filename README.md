# PART 1 
## LangChain Sequential Chain — Report and Summary Generator

This part demonstrates how to build a **Sequential Chain in LangChain** using the `Runnable` interface. It walks through how to:

* Take a topic input
* Generate a detailed report using an LLM
* Summarize the report into 5 bullet points

Built using `LangChain`, `OpenAI`, and Python, this is a great starting point to understand **multi-step LLM workflows**.

---

### 📌 Key Features

 - Uses `PromptTemplate` to create dynamic, reusable prompts
 - Chains multiple steps using the `|` operator (RunnableSequence)
 - Applies `StrOutputParser` to clean raw LLM responses
 - Demonstrates end-to-end flow: **Topic → Report → Summary**
 - Visualizes the full chain structure using `.get_graph().print_ascii()`

---

### 🧠 How It Works

1. **Prompt 1**: Ask the LLM to generate a detailed report on a given topic.
2. **Prompt 2**: Summarize that report into 5 concise bullet points.
3. **Model**: `ChatOpenAI` (can be swapped with any other LangChain-supported LLM).
4. **Parser**: Cleans LLM output for passing between steps.

### 🔁 Flow:

```
User Input → PromptTemplate 1 → LLM → Parser → PromptTemplate 2 → LLM → Parser → Output
```


## 🛠️ Installation

```bash
git clone https://github.com/your-username/langchain-sequential-report.git
cd langchain-sequential-report
pip install -r requirements.txt
```

---

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

