# 🧠 Multi-Agent Research & Synthesis System

A production-style **Agentic AI system** built using **Python, LangGraph, and React** that simulates how consulting analysts perform structured research and synthesis.

This system demonstrates a full **end-to-end multi-agent workflow** with real-time reasoning visibility and human-in-the-loop control.

---

## 🚀 Overview

Consulting analysts often spend hours performing research, gathering information from multiple sources, and preparing structured reports.

This project automates that workflow using a **multi-agent architecture**, enabling:

- Query decomposition into focused sub-questions  
- Simulated research using specialized agents  
- Real-time streaming of agent reasoning  
- Human-in-the-loop validation before final output  
- Generation of a structured final summary  

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
