---
layout: archive
permalink: /research/
author_profile: false
---

![](/_pages/8.png)

We work across three connected research areas, using machine learning, optimisation and control to tackle problems in processes, systems, and materials with a sustainability focus.

<hr>

## Machine Learning &amp; Artificial Intelligence

<div style="display:flex; flex-wrap:wrap; gap:2em; align-items:flex-start; margin-bottom:1.5em;">
  <div style="flex:1; min-width:280px;">
    <p>We develop machine learning methods that enable engineering systems to learn from data, improve predictions, and support decision-making under uncertainty. Our research combines statistical learning, probabilistic modelling, and physics-informed AI to create models that are both accurate and scientifically meaningful.</p>
    <p>A particular focus is the integration of domain knowledge into machine learning, ensuring that AI systems remain interpretable, robust, and reliable when applied to complex real-world problems. We are interested in hybrid models that combine first-principles understanding with data-driven learning, as well as methods for uncertainty quantification, online learning, and autonomous model development.</p>
    <p><strong>Research topics:</strong></p>
    <ul>
      <li>Physics-informed machine learning</li>
      <li>Hybrid modelling and digital twins</li>
      <li>Gaussian processes and probabilistic modelling</li>
      <li>Scientific machine learning</li>
      <li>Bayesian optimisation</li>
      <li>Reinforcement learning</li>
      <li>Explainable and trustworthy AI</li>
      <li>AI-assisted model discovery</li>
    </ul>
  </div>
  <div style="flex:0 0 320px;">
    <!-- TODO: add a figure summarising Machine Learning & AI research, e.g. images/research/ml-ai.png -->
    <img src="/images/research/ml-ai.png" alt="Machine Learning & AI research summary" style="width:100%; border-radius:8px;">
  </div>
</div>

<hr>

## Optimisation &amp; Control

<div style="display:flex; flex-wrap:wrap; gap:2em; align-items:flex-start; margin-bottom:1.5em;">
  <div style="flex:1; min-width:280px;">
    <p>We develop optimisation and control methods for complex engineering systems operating in dynamic and uncertain environments. Our goal is to design intelligent decision-making frameworks that improve efficiency, safety, sustainability, and economic performance.</p>
    <p>Our research spans real-time optimisation, model predictive control, stochastic optimisation, and digital twins. We combine mathematical models, machine learning, and feedback control to create closed-loop systems that adapt to changing operating conditions and continuously improve performance.</p>
    <p>Applications include energy systems, chemical processes, resource recovery, decarbonisation technologies, and advanced manufacturing.</p>
    <p><strong>Research topics:</strong></p>
    <ul>
      <li>Model predictive control (MPC)</li>
      <li>Economic and stochastic MPC</li>
      <li>Real-time optimisation</li>
      <li>Dynamic modelling and simulation</li>
      <li>Digital twins</li>
      <li>State estimation and monitoring</li>
      <li>Decision-making under uncertainty</li>
      <li>Autonomous process operation</li>
    </ul>
  </div>
  <div style="flex:0 0 320px;">
    <!-- TODO: add a figure summarising Optimisation & Control research, e.g. images/research/optimisation-control.png -->
    <img src="/images/research/optimisation-control.png" alt="Optimisation & Control research summary" style="width:100%; border-radius:8px;">
  </div>
</div>

<hr>

## AI for Science &amp; Materials Discovery

<div style="display:flex; flex-wrap:wrap; gap:2em; align-items:flex-start; margin-bottom:1.5em;">
  <div style="flex:1; min-width:280px;">
    <p>We use artificial intelligence and optimisation to accelerate scientific discovery and the development of sustainable technologies. We create closed-loop discovery frameworks that can rapidly identify promising materials, processes, and operating conditions.</p>
    <p>Our vision is to move beyond using AI solely for prediction and towards AI systems that actively support scientific reasoning, hypothesis generation, experiment design, and knowledge discovery. We are particularly interested in creating autonomous discovery platforms that integrate machine learning, optimisation, and experimental data to accelerate innovation.</p>
    <p>Applications include materials discovery, energy technologies, mineral processing, and other challenges related to sustainability and the net-zero transition.</p>
    <p><strong>Research topics:</strong></p>
    <ul>
      <li>AI for Science</li>
      <li>Autonomous discovery systems</li>
      <li>Materials informatics</li>
      <li>Scientific knowledge extraction</li>
      <li>Optimal experimental design</li>
      <li>Closed-loop experimentation</li>
      <li>Scientific foundation models</li>
      <li>Sustainable materials and technologies</li>
    </ul>
  </div>
  <div style="flex:0 0 320px;">
    <!-- TODO: add a figure summarising AI for Science & Materials Discovery research, e.g. images/research/ai-science.png -->
    <img src="/images/research/ai-science.png" alt="AI for Science & Materials Discovery research summary" style="width:100%; border-radius:8px;">
  </div>
</div>

<hr>

## Ongoing projects and collaborations

* "**Experimentally-validated dynamic modelling for optimal scheduling of pressure swing adsorption in CO<sub>2</sub> capture**" at Brunel University London as part of the Brunel Research Initiative & Enterprise Fund (BRIEF) 2024/25 (competitive grant).

* "**Gaussian process regression for model predictive control**", Imperial College London.

* "**Grey-box recursive parameter identification of a nonlinear dynamic model for mineral flotation**", Eindhoven University of Technology, The Netherlands.

* "**Laboratory-scale system to control moisture content in column leaching**", Universidad Tecnica Federico Santa Maria, Chile.

* "**[Bubble Analyser](/software) – An open-source software for bubble size analysis**", which has resulted in a published paper. This software was collaboratively developed by Dr Diego Mesa, Dr Francisco Reyes, and Dr Paulina Quintanilla. We are now working with two Imperial MSc students from the Applied Computational Science and Engineering programme on a 2.0 version implementing computer vision and machine learning techniques, including the project "Bubble Analyser - Identification and characterisation of bubbles using Machine Learning".

<hr>

## Featured case study: dynamic physics-based flotation models for predictive control

_This work, from Dr Paulina Quintanilla's PhD research, is a flagship example of how our Optimisation & Control research is applied to mineral processing._

### Why do we care about optimising mineral processes?

Building clean technologies for the transition to 100% green energy is creating a massive demand for a range of minerals. For example, copper mines would have to ramp up production considerably to satisfy the extra 7% predicted demand. Meeting that demand, however, is becoming more and more challenging as ores are becoming lower grade, deeper, and more complex. This implies that there is an urgent need to optimise current processes to extract the necessary minerals and metals in a more sustainable and efficient way. The largest tonnage separation process used to separate valuable minerals from the waste rock is called froth flotation.

### What is froth flotation?

Froth flotation is the largest tonnage separation process by which valuable mineral particles are separated from the waste rock, based on their surface properties (hydrophobicity). This process is carried out in flotation cells, in which reagents and air are added. Reagents make the valuable mineral particles hydrophobic, so they repel water. Consequently, the valuable mineral particles attach to air bubbles to form bubble-particle aggregates. These aggregates rise to the top of the cell, forming the froth phase. The waste rock remains in the slurry in the cell, known as the pulp phase. While the froth overflows as a concentrate from the top of the cell, the pulp goes out from the bottom as tailings.

<img width="867" alt="image" src="https://user-images.githubusercontent.com/79862171/232215478-6197f533-e304-49df-a7d2-602b762b0eaf.png">

### Modelling for model-based control

As froth flotation is a large-scale process, even small improvements in separation efficiency would translate into important economic benefits and improved environmental impact. Flotation is a multiphase process that exhibits inherent instabilities, and thus complex dynamics. One of the most efficient ways to increase flotation performance is by implementing advanced controllers, such as Model Predictive Control (MPC). The effectiveness of MPC strategies relies on the model that represents the dynamics of the process, which has often hindered its application in froth flotation. MPC studies have primarily used kinetic models to phenomenologically represent the attachment-detachment of mineral particles in the pulp phase. While kinetic models can adequately represent the phenomena in the pulp phase, they are not suitable to model the complex phenomena in the froth phase. This is particularly relevant since froth phase phenomena are key drivers of froth performance yet are often neglected in flotation models.

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
