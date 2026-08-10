---
title: "New preprint: DASyR-LLM — domain-aware symbolic regression with LLMs for kinetic model discovery"
date: 2026-08-10
summary: "Our new preprint introduces DASyR-LLM, a framework that pairs symbolic regression with large language models to discover interpretable kinetic models from noisy data — with equivalent accuracy using up to 79% fewer experiments."
tags: ["preprint", "AI for Science", "symbolic regression", "LLMs", "model discovery"]
---

How can we discover the equations that govern a chemical or biological process — directly from noisy experimental data, and without wasting experiments? 🤖

Our new preprint, **DASyR-LLM: Domain-Aware Symbolic Regression with LLMs for Kinetic Model Discovery**, by **Roberto Aliaga Medina, Paulina Quintanilla and Antonio del Rio Chanona**, tackles exactly this.

### The idea

DASyR-LLM closes the loop between experimentation and modelling. Starting from noisy experimental data, it runs an iterative, LLM-guided symbolic regression cycle:

1. **Run a new experiment**, chosen via model-based design of experiments so each one is maximally informative;
2. **Symbolic regression** proposes candidate kinetic models as interpretable equations;
3. an **LLM critiques** those candidates using scientific domain knowledge — for example, recognising that a rate law should use Monod-type saturation terms;
4. the LLM **proposes new candidate models**, which feed the next round.

Because the LLM injects *domain awareness*, the search is steered toward models that are not only accurate but also physically meaningful.

### The result

Across the case studies, DASyR-LLM recovers interpretable kinetic models with **equivalent predictive accuracy (R² > 0.98)** while needing **up to 79% fewer experiments** than conventional symbolic regression.

### Read more

- 📄 **Preprint:** [arXiv:2608.05120](https://arxiv.org/abs/2608.05120)
- 💻 **Code:** [Zenodo record](https://zenodo.org/records/21793266)
- 🔗 **[View the announcement on LinkedIn](https://www.linkedin.com/posts/robertoaliagam_aiforscience-largelanguagemodels-symbolicregression-ugcPost-7491190801058652160-BFv8/?utm_source=share&utm_medium=member_desktop&rcm=ACoAABVxaAABUyjSi_mbKwqgIF2F8ffBOna0wIA)**

Huge congratulations to **Roberto Aliaga Medina**, who led this work while finishing his MSc in Chile! 🎉
