# ShipOrKill: AI-Powered Product Discovery Agent 🚢

**An autonomous "Red Team" agent that helps Product Managers validate hypotheses in seconds, not weeks.**

[![Streamlit App]([https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://ship-or-kill.streamlit.app/](https://pmshiporkill-ddmu5ai4t2zgizhg5upmyn.streamlit.app/))
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 🧐 The Problem
In Product Management, the "Discovery Phase" is often plagued by confirmation bias and slow feedback loops. We fall in love with our solutions before fully validating the problem.
* **Manual Research is slow:** Scouring Reddit, competitors, and technical docs takes days.
* **Internal Bias:** It's hard to be objective about your own ideas.
* **The "Cold Start":** Sometimes the hardest part is just generating the initial hypothesis.

## 💡 The Solution
**ShipOrKill** is a decision-support agent built on **Google's Gemini 2.0 Flash**. It acts as an objective third-party analyst, instantly evaluating product concepts against the three core lenses of product risk:

1.  **Desirability (User Value):** Does the market actually care? (Simulates user sentiment analysis).
2.  **Viability (Business Value):** Is there a business model? (Analyzes competition and monetization).
3.  **Feasibility (Technical Value):** Can it be built? (Identifies necessary APIs and technical bottlenecks).

## ⚙️ How It Works (Architecture)
This tool moves beyond simple "chat" by utilizing **Chain-of-Thought (CoT) Prompting** to force the model into a structured reasoning process.

```mermaid
graph LR
    A[User Input: Hypothesis] --> B{Agent Brain};
    B -->|Step 1| C[Desirability Check];
    B -->|Step 2| D[Viability Check];
    B -->|Step 3| E[Feasibility Check];
    C & D & E --> F[Synthesis & Risk Scoring];
    F --> G[Strategic Memo Output];

## ⚙️ Key Features
1. 🚀 Validator Mode: Inputs a raw feature idea and outputs a structured "Go/No-Go" memo, flagging critical risks and technical dependencies.
2. 💡 Ideator Mode: Overcomes writer's block by generating high-potential, contrarian B2B SaaS ideas for specific domains (e.g., "Healthcare", "Logistics").
3.  ⚡ Real-time Latency: Built on Gemini 2.0 Flash for near-instant inference, enabling rapid "idea-to-validation" loops.

## 🛠️ Tech Stack
1. LLM Engine: Google Gemini 2.0 Flash (via google-generativeai SDK).
2. Frontend: Streamlit (Python-based web framework).
3. Prompt Engineering: Few-Shot & Chain-of-Thought techniques to enforce "Senior PM" persona constraints.

## Get Started

1.  Clone the repository.
2.  Install the required dependencies using `pip install -r requirements.txt`.
3.  Run the application using `streamlit run app.py`.


## License

This project is licensed under the MIT License.
