---
title:
date: 2025-08-01
type: landing

sections:
  - block: slider
    content:
      slides:
        - title: ''
          content: |
            <img src="/media/logo_orange.png" alt="LOOPS" style="max-width:420px;width:80%;height:auto;margin:0 auto 1rem;display:block;filter:drop-shadow(0 4px 20px rgba(0,0,0,0.5));">
            <p style="font-size:clamp(1rem,2.2vw,1.4rem);opacity:0.9;margin:0;">Learning and Optimization Of Process Systems</p>
            <p style="font-size:clamp(0.85rem,1.5vw,1.05rem);opacity:0.7;margin:0.4rem 0 0;">UCL Department of Chemical Engineering</p>
          align: center
          background:
            image:
              filename: ucl-building.jpg
              filters:
                brightness: 0.4
            position: center
            color: '#2d2050'
          link:
            icon: arrow-down
            icon_pack: fas
            text: Learn more
            url: '#research'
        - title: Machine Learning · Optimisation · AI for Science
          content: |
            Data-driven models, advanced control, and AI-assisted discovery for processes and physical systems.
          align: center
          background:
            image:
              filename: research_topics_together.png
              filters:
                brightness: 0.3
            position: center
            color: '#0e0c1a'
          link:
            icon: flask
            icon_pack: fas
            text: Explore our research
            url: research
        - title: Join the LOOPS Group
          content: |
            We are always looking for motivated researchers. Get in touch!
          align: center
          background:
            image:
              filename: ucl-join.jpg
              filters:
                brightness: 0.4
            position: center
            color: '#1a1030'
          link:
            icon: envelope
            icon_pack: fas
            text: Contact us
            url: contact
    design:
      slide_height: '100vh'
      is_fullscreen: true
      loop: true
      interval: 6000

  - block: markdown
    id: research
    content:
      title: Our Research
      subtitle: ''
      text: |
        We are the **LOOPS research group** — Learning and Optimization Of Process Systems — based in the Department of Chemical Engineering at [UCL](https://www.ucl.ac.uk), and part of the [Sargent Centre for Process Systems Engineering](https://www.imperial.ac.uk/process-systems-engineering/). We develop machine learning, optimisation and control methods for processes and systems with a sustainability focus.
    design:
      columns: '1'

  - block: features
    content:
      title: ''
      items:
        - name: Machine Learning & AI
          icon: brain
          icon_pack: fas
          description: Physics-informed ML, hybrid models, Gaussian processes, Bayesian optimisation, reinforcement learning and explainable AI.
        - name: Optimisation & Control
          icon: sliders-h
          icon_pack: fas
          description: Model predictive control, economic MPC, real-time optimisation, digital twins and autonomous process operation.
        - name: AI for Science
          icon: flask
          icon_pack: fas
          description: AI-assisted discovery, materials informatics, optimal experimental design and closed-loop experimentation.

  - block: collection
    content:
      title: Latest Publications
      text: ''
      count: 5
      filters:
        folders:
          - publication
        exclude_featured: false
      offset: 0
      order: desc
    design:
      view: citation
      columns: '1'

  - block: markdown
    content:
      title: ''
      subtitle: ''
      text: |
        {{% cta cta_link="./people/" cta_text="Meet the team →" %}}
    design:
      columns: '1'
---
