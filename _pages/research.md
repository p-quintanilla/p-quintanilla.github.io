---
layout: archive
permalink: /research/
title: "Research"
author_profile: true
---

![](/_pages/8.png)

## Overview
My expertise is in dynamic modelling for model-based control strategies and optimisation. I am currently working on supply chain optimisation for healthcare manufacturing, design space, machine learning, and control for bioprocesses and energy systems.  

## PhD Research

Froth flotation is the largest tonnage separation process by which valuable mineral particles are separated from the waste rock, based on their surface properties (hydrophobicity). This process is carried out in flotation cells, in which reagents and air are added. Reagents make the valuable mineral particles hydrophobic, so they repel water. Consequently, the valuable mineral particles attach to air bubbles to form bubble-particle aggregates. These aggregates rise to the top of the cell, forming the froth phase. The waste rock remains in the slurry in the cell, known as the pulp phase. While the froth overflows as a concentrate from the top of the cell, the pulp goes out from the bottom as tailings.

**Modelling for predictive control and optimisation**

As froth flotation is a large-scale process, even small improvements in separation efficiency would translate into important economic benefits and improved environmental impact. These improvements can be achieved by incorporating advanced control strategies in the process, such as Model Predictive Control (MPC). MPC has been widely considered one of the most efficient strategies to optimise a multivariable process (such as froth flotation, which is affected by over a hundred variables). However, the implementation of MPC into this process is a major challenge as the most crucial part of this control strategy is model development.

Modelling froth flotation is a difficult task, as it has very complex dynamics as a multiphase (gas-liquid-solid) process with inherent instability. We developed new, dynamic, physics-based flotation froth models for implementation as part of MPC strategies. 


## Some collaborations: 

* “[Bubble Analyser](/software) – An open-source software for bubble size analysis”, which has resulted in a published paper. This software was collaboratively developed by Dr Diego Mesa, Dr Francisco Reyes, and me. We are now working together with two Imperial MSc students from the Applied Computational Science and Engineering program on a 2.0 version to implement several different algorithms, including computer vision and machine learning techniques. I am co-supervising the MSc project entitled: “Bubble Analyser - Identification and characterisation of bubbles using Machine Learning”.

* “Optimal control strategies for hydrogen-vanadium hybrid redox flow batteries using physics-based models”. The aim of this collaboration is (a) to implement a model predictive control strategy in a laboratory-scale battery cell using physics-based models, and (b) to scale up the model predictive control strategy for a stack (many batteries connected in series) system.
