---
title: "New preprint: hierarchical MPC–RL control for multi-timescale battery systems"
date: 2026-10-05
summary: "Our new preprint proposes a hierarchical control framework that combines model predictive control and reinforcement learning to balance second-by-second market decisions with long-term battery health, extending battery lifetime by 84% and increasing profit by 34% compared with MPC baselines."
tags: ["preprint", "reinforcement learning", "MPC", "batteries"]
image:
  placement: 1
  focal_point: "Center"
---

How can a battery chase profit opportunities that last seconds without wearing itself out over the following months? 🔋

Our new preprint, **Hierarchical Control via MPC-RL for Multi-Timescale Battery Systems**, by **Rasa Pourjam, Ehecatl Antonio del Río Chanona and Paulina Quintanilla**, is now on arXiv. It is the full paper behind the work we [presented at the IFAC World Congress in Busan](/post/ifac-busan-presentation/).

### The idea

Many systems have to make fast operational decisions while meeting slow, long-horizon targets. We separate the two with a hierarchy:

1. a **high-level model predictive control (MPC) layer** optimises long-horizon setpoints on the slow timescale, where battery degradation plays out;
2. a **low-level reinforcement learning agent**, trained in advance, tracks those setpoints in real time to make the most of short-term opportunities.

Using reinforcement learning at the fast level means the controller can learn nonlinear policies without linearising the model, and without solving a heavy optimisation problem at every step.

### The result

We applied the framework to a **battery energy storage system** operating in frequency regulation markets, where profit is made in seconds but degradation builds up over weeks to months. Compared with MPC baselines, the approach **extended battery lifetime by 84%** and **increased operational profit by 34%**.

### Read more

- 📄 **Preprint:** [arXiv:2610.03508](https://arxiv.org/abs/2610.03508)
- 📚 **[Publication page](/publication/mpc-rl-battery/)**

Congratulations to **Rasa Pourjam**, who led this work! 🎉
