# Agentic AI Roadmap Projects

This repository contains projects I’m developing while learning and experimenting with the **Agentic AI Roadmap**.  
It will serve as a living collection of code examples, experiments, and frameworks as I progress through building agents — from the simplest vanilla implementations to more advanced frameworks like Autogen, LangGraph, or MCP.

---

## 📌 Project List
- **Vanilla Agent**  
- *(More to be added as I move forward...)*

---

## 🟢 Vanilla Agent
A **Vanilla Agent** is the most minimal form of an AI agent — built without any external frameworks.  
It uses just the raw LLM API, a loop, and a set of tools/functions you define.
┌────────────┐
│ User Input │
└─────┬──────┘
      │
      ▼
┌──────────────────────┐
│ Send to LLM + Tools │
└─────────┬────────────┘
          │
          ▼
┌───────────────────────────────┐
│ LLM decides:                  │
│  • Answer directly            │
│  • Or call a tool (with args) │
└─────────┬─────────────────────┘
          │
   ┌──────┴────────┐
   │               │
   ▼               ▼
Direct Answer   Tool Call
   │               │
   ▼               ▼
┌─────────────────────────┐
│ LLM produces Final Text │
└─────────────────────────┘


