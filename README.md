# 🧠 Multi-Agent Research & Synthesis System

A production-style **Agentic AI system** built using **Python, LangGraph, and React**, designed to simulate how consulting analysts perform structured research and synthesis workflows.

This system demonstrates a complete **end-to-end multi-agent pipeline**, including real-time reasoning visibility and human-in-the-loop (HITL) control.

---

## 🚀 Overview

Consulting analysts often spend hours researching topics, gathering information from multiple sources, and preparing structured reports.

This project automates that workflow using a coordinated **multi-agent architecture** that:

- Breaks user queries into focused sub-questions  
- Simulates research using specialized agents  
- Streams agent reasoning in real time  
- Allows human validation before final output  
- Produces a structured, synthesized summary  

---

## ✅ Key Features

✔ Multi-agent orchestration using LangGraph  
✔ Supervisor-driven workflow control  
✔ Real-time streaming using Server-Sent Events (SSE)  
✔ Human-in-the-loop (HITL) approval system  
✔ Interactive React-based UI  
✔ End-to-end full-stack implementation  

---

## 🧠 Architecture

**System Flow:**

User Query  
↓  
Supervisor Agent  
↓  
Decomposer  
↓  
Researcher  
↓  
⏸️ Human Review (HITL)  
↓  
Synthesizer  
↓  
Final Summary  

---

## 📡 System Flow (Detailed)

1. User inputs a research query through the UI  
2. Supervisor determines next step  
3. Decomposer splits query into sub-questions  
4. Researcher gathers relevant information (simulated)  
5. UI streams agent reasoning in real time  
6. System pauses for human approval  
7. User provides feedback / approval  
8. System resumes and produces final summary  

---

## 🖥️ Frontend (React)

📂 Located in:
