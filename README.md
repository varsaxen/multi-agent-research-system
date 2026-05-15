# 🧠 Multi-Agent Research & Synthesis System

A production-style **Agentic AI system** built using **Python, LangGraph, and React**, designed to simulate how consulting analysts perform structured research and synthesis.

---

## 🚀 Overview

Consulting analysts spend hours researching topics, gathering information, and producing reports.

This system automates that workflow using a **multi-agent architecture** that:

- Breaks user queries into sub-questions
- Simulates research using specialized agents
- Streams agent reasoning in real time
- Allows human intervention (HITL)
- Produces a final structured report

---

## ✅ Key Features

✔ Multi-agent orchestration using LangGraph  
✔ Supervisor-driven decision workflow  
✔ Real-time streaming using Server-Sent Events (SSE)  
✔ Human-in-the-loop (HITL) approval system  
✔ Clean and interactive React UI  
✔ End-to-end full-stack implementation  

---

## 🧠 Architecture

**Flow:**

- User Query  
  ↓  
- Supervisor Agent  
  ↓  
- Decomposer  
  ↓  
- Researcher  
  ↓  
- ⏸️ Human Review (HITL)  
  ↓  
- Synthesizer  
  ↓  
- Final Summary  

