# 🤖 NeoCode

**NeoCode** is an AI-powered DevOps tool designed to modernize legacy codebases and prepare them for cloud-native deployment. Built for Zopdev Summer of Code, it supports multi-language static analysis, safe refactoring, and Helm chart generation.

---

## 💡 Features

-  Static code analysis for Java, Python, and C++
-  Language-specific refactor engine
-  Helm chart generator for Kubernetes deployment
-  Safe, tested, and modular design
-  No modification of source files — read-only and isolated

---

## 🧩 Architecture

```plaintext
Legacy Code → Analyzer → Refactor Engine → Helm Generator → Charts → CI/CD
```

# How to use
```
python core/orchestrator.py python samples/legacy.py
python core/orchestrator.py java samples/legacy.java
python core/orchestrator.py cpp samples/legacy.cpp
```
