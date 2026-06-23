---
layout: archive
permalink: /research/
author_profile: false
---

![](/_pages/8.png)

## Overview

My expertise lies in **dynamic modelling** for **model-based control** strategies and **optimisation**. Currently, I am focused on applying **computer-aided tools** to real-world problems, ranging from supply chain optimization for personalised medical treatments to model-based control of mineral processing and multi-scale modelling and optimization of energy systems and decarbonization technologies. 

Currently, one of my key interests is integrating **machine learning tools** for combining **data-driven models** with **physics-based models**. This approach combines the strengths of both types of models, allowing for more accurate and efficient predictions of process performance. By leveraging machine learning algorithms, we can extract meaningful insights from large amounts of data, identifying patterns that may not be obvious with traditional modelling techniques. Then, **digital twins** (i.e. virtual replicas of real-world systems) can be developed and used to simulate the behaviour of the physical system in real-time, allowing for **improved control and optimisation** of the process. By combining data-driven models with physics-based models, we can create more accurate representations of complex systems, enabling us to make **better-informed decisions** and optimise systems more effectively.

## Ongoing research and collaborations: 

* "**Experimentally-validated dynamic modelling for optimal scheduling of pressure swing adsorption in CO<sub>2</sub> capture**" at Brunel University London as part of the Brunel Research Initiative & Enterprise Fund (BRIEF) 2024/25 (competitive grant).
  
* "**Gaussian process regression for model predictive control**", Imperial College London.

* “**Grey-box recursive parameter identification of a nonlinear dynamic model for mineral flotation**”, Eindhoven University of Technology, The Netherlands.

* "**Laboratory-scale system to control moisture content in column leaching**", Universidad Tecnica Federico Santa Maria, Chile. 

* “**[Bubble Analyser](/software) – An open-source software for bubble size analysis**”, which has resulted in a published paper. This software was collaboratively developed by Dr Diego Mesa, Dr Francisco Reyes, and me. We are now working together with two Imperial MSc students from the Applied Computational Science and Engineering program on a 2.0 version to implement several different algorithms, including computer vision and machine learning techniques. I am co-supervising the MSc project entitled: “Bubble Analyser - Identification and characterisation of bubbles using Machine Learning”.
 

## PhD Research:
## _"Dynamic physics-based flotation models for effective predictive control"_

My PhD research was about developing and implementing dynamic flotation models for model-based control.

But...

### Why do we care about optimising mineral processes?

Building clean technologies for the transition to 100% green energy is creating a massive demand for a range of minerals. For example, copper mines would have to ramp up production considerably to satisfy the extra 7% predicted demand. Meeting that demand, however, is becoming more and more challenging as ores are becoming lower grade, deeper, and more complex. This implies that there is an urgent need to optimise current processes to extract the necessary minerals and metals in a more sustainable and efficient way. The largest tonnage separation process used to separate valuables minerals from the waste rock is called froth flotation.

### What is froth flotation?

Froth flotation is the largest tonnage separation process by which valuable mineral particles are separated from the waste rock, based on their surface properties (hydrophobicity). This process is carried out in flotation cells, in which reagents and air are added. Reagents make the valuable mineral particles hydrophobic, so they repel water. Consequently, the valuable mineral particles attach to air bubbles to form bubble-particle aggregates. These aggregates rise to the top of the cell, forming the froth phase. The waste rock remains in the slurry in the cell, known as the pulp phase. While the froth overflows as a concentrate from the top of the cell, the pulp goes out from the bottom as tailings.

<img width="867" alt="image" src="https://user-images.githubusercontent.com/79862171/232215478-6197f533-e304-49df-a7d2-602b762b0eaf.png">


### Modelling for model-based control

As froth flotation is a large-scale process, even small improvements in separation efficiency would translate into important economic benefits and improved environmental impact.Flotation is a multiphase process that exhibits inherent instabilities, and thus complex dynamics. One of the most efficient ways to increase flotation performance is by implementing advanced controllers, such as Model Predictive Control (MPC). The effectiveness of MPC strategies relies on the model that represents the dynamics of the process, which has often hindered its application in froth flotation. MPC studies have primarily used kinetic models to phenomenologically represent the attachment-detachment of mineral particles in the pulp phase. While kinetic models can adequately represent the phenomena in the pulp phase, they are not suitable to model the complex phenomena in the froth phase. This is particularly relevant since froth phase phenomena are key drivers of froth performance yet are often neglected in flotation models. 

<img width="1143" alt="image" src="https://user-images.githubusercontent.com/79862171/232250279-71eab6e8-7165-4b98-a86e-5578bfc57e2a.png">

Unlike other flotation models for control in the literature, the model proposed here includes, for the first time, important variables related to froth stability, such as bursting rate and air recovery, as well as simplified phenomenological equations to calculate froth recovery and entrainment. The model also incorporates pulp-froth interface physics, which enables a more accurate prediction of relevant flotation variables. A comprehensive sensitivity analysis of the parameters involved in the model is presented, highlighting the predictions' relevance for overflowing bubble size and bursting rate. An analysis of the degrees of freedom of the model was also carried out and determined that two variables are available for control purposes, for which air and tailings flowrates were chosen.

<img width="1140" alt="image" src="https://user-images.githubusercontent.com/79862171/232250315-cded08a8-63a4-46db-90fa-2b2f99343c08.png">

<img width="1150" alt="image" src="https://user-images.githubusercontent.com/79862171/232250349-b220f279-6bb9-41b5-802c-4619f0c51fd7.png">


### Model-based control using the proposed dynamic model

Using the proposed dynamic model, a novel economic model predictive control (E-MPC) strategy was developed for a single froth flotation tank. To ensure a global optimum for the flotation bank, a centralized E-MPC strategy was implemented. 

![image](https://user-images.githubusercontent.com/79862171/232250396-204d1b92-5733-4d61-a431-83e24280a6b7.png)

The E-MPC strategies were implemented in both simulations and a laboratory-scale flotation rig. The simulation results demonstrated a significant improvement in metallurgical recovery in all cases while maintaining the concentrate grade at a minimum of 20%. 

<img width="1029" alt="image" src="https://user-images.githubusercontent.com/79862171/232250513-22f6e029-5f13-4610-ad31-d27a38714abc.png">

The implementation of E-MPC in the laboratory-scale flotation rig also improved recoveries, though some challenges in convergence were identified for flotation bank control due to the high computational demand of the centralized system. Further work is therefore needed to include algorithms that are less computationally demanding. Implementing the predictive control strategy has, nevertheless, provided encouraging results, demonstrating the model's potential for integration into a larger flotation control system.

<img width="1040" alt="image" src="https://user-images.githubusercontent.com/79862171/232250649-6dd72e16-904b-442c-8a04-46f8b14799d1.png">


