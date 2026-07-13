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
            <img src="/media/logo_orange.png" alt="LOOPS" style="max-width:460px;width:80%;height:auto;margin:0 auto 1.2rem;display:block;filter:drop-shadow(0 4px 24px rgba(0,0,0,0.6));">
            <p style="font-size:clamp(1.3rem,3vw,2rem);color:#ffffff;font-weight:600;margin:0 0 0.4rem;text-shadow:0 2px 12px rgba(0,0,0,0.6);">Learning and Optimisation Of Process Systems</p>
            <p style="font-size:clamp(1rem,2vw,1.4rem);color:#ffffff;font-weight:400;margin:0;text-shadow:0 2px 8px rgba(0,0,0,0.5);">UCL Department of Chemical Engineering</p>
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
        <div style="display:flex; flex-wrap:wrap; gap:2.5em; align-items:center;">
          <div style="flex:1; min-width:180px; max-width:220px; text-align:center;">
            <a href="/author/dr-paulina-quintanilla/">
              <img src="/media/paulina.jpg" alt="Dr Paulina Quintanilla" style="width:140px;height:140px;object-fit:cover;border-radius:50%;margin-bottom:0.6em;box-shadow:0 4px 12px rgba(0,0,0,0.15);">
            </a>
            <p style="margin:0 0 0.2em;font-weight:700;"><a href="/author/dr-paulina-quintanilla/">Dr Paulina Quintanilla</a></p>
            <p style="margin:0 0 0.6em;font-size:0.88em;color:#666;">Principal Investigator<br>UCL Chemical Engineering</p>
            <p style="font-size:1.2em;margin:0;line-height:2;">
              <a href="mailto:p.quintanilla@ucl.ac.uk" title="Email"><i class="fas fa-envelope"></i></a>&nbsp;
              <a href="https://profiles.ucl.ac.uk/103850-paulina-quintanilla/about" target="_blank" title="UCL Profile"><i class="fas fa-university"></i></a>&nbsp;
              <a href="https://www.linkedin.com/in/paulinaquintanilla" target="_blank" title="LinkedIn"><i class="fab fa-linkedin"></i></a>&nbsp;
              <a href="https://scholar.google.com/citations?user=1dp-SB4AAAAJ&hl=en" target="_blank" title="Google Scholar"><i class="ai ai-google-scholar"></i></a>&nbsp;
              <a href="https://orcid.org/0000-0002-7717-0556" target="_blank" title="ORCID"><i class="ai ai-orcid"></i></a>
            </p>
          </div>
          <div style="flex:3; min-width:260px;">
            <p>We are the <strong>LOOPS research group</strong> — Learning and Optimisation Of Process Systems — based in the Department of Chemical Engineering at <a href="https://www.ucl.ac.uk">UCL</a>, and part of the <a href="https://www.imperial.ac.uk/process-systems-engineering/">Sargent Centre for Process Systems Engineering</a>. We develop machine learning, optimisation and control methods for processes and physical systems. Current projects include hierarchical MPC–RL control, LLM-guided symbolic regression, physics-based modelling for froth flotation control, stochastic MPC, and more.</p>
          </div>
        </div>
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
      title: Latest News
      subtitle: ''
      text: ''
      count: 3
      filters:
        folders:
          - post
      offset: 0
      order: desc
    design:
      view: compact
      columns: '2'

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
