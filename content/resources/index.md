---
title: Resources
date: 2025-08-01
type: landing

sections:
  - block: markdown
    content:
      title: Learning Resources
      text: |
        <style>
        .res-wrap { --res-purple:#34306b; --res-purple-2:#5a54a0; --res-orange:#e8833a; --res-ink:#1f2333; --res-muted:#5c6270; --res-line:#e7e8ef; --res-bg:#f7f7fb; }
        .res-intro { max-width:760px; margin:0 auto 2.2em; text-align:center; color:var(--res-muted); font-size:1.08rem; line-height:1.6; }
        .res-nav { display:flex; flex-wrap:wrap; justify-content:center; gap:.6em; margin:0 auto 3em; max-width:900px; }
        .res-nav a { text-decoration:none; padding:.5em 1.1em; border-radius:999px; background:#fff; border:1.5px solid var(--res-line); color:var(--res-purple); font-weight:700; font-size:.92rem; transition:all .18s ease; }
        .res-nav a:hover { background:var(--res-purple); color:#fff; border-color:var(--res-purple); transform:translateY(-2px); box-shadow:0 6px 16px rgba(52,48,107,.22); }
        .res-section { margin:0 auto 3.5em; max-width:1080px; scroll-margin-top:90px; }
        .res-head { display:flex; align-items:center; gap:.7em; padding-bottom:.6em; margin-bottom:1.6em; border-bottom:3px solid var(--res-purple); }
        .res-head .res-emoji { font-size:1.9rem; line-height:1; }
        .res-head h3 { margin:0 !important; color:var(--res-purple) !important; font-size:1.55rem !important; }
        .res-head .res-sub { margin-left:auto; color:var(--res-muted); font-size:.9rem; max-width:340px; text-align:right; }
        .res-grid { display:grid; grid-template-columns:repeat(auto-fit,minmax(300px,1fr)); gap:1.4em; }
        .res-card { background:#fff; border:1px solid var(--res-line); border-radius:14px; padding:1.4em 1.5em; box-shadow:0 2px 10px rgba(31,35,51,.05); }
        .res-card h4 { margin:0 0 1em !important; font-size:1.05rem !important; display:flex; align-items:center; gap:.5em; color:var(--res-ink) !important; }
        .res-tag { font-size:.72rem; font-weight:700; letter-spacing:.04em; text-transform:uppercase; padding:.28em .7em; border-radius:6px; }
        .res-tag.books { background:#efeefb; color:var(--res-purple); }
        .res-tag.videos { background:#fdeee2; color:#c25a12; }
        .res-tag.sites { background:#e6f4ee; color:#1f7a53; }
        .res-list { list-style:none; margin:0; padding:0; }
        .res-list li { padding:.55em 0; border-top:1px solid var(--res-line); line-height:1.45; }
        .res-list li:first-child { border-top:none; padding-top:0; }
        .res-list a { color:var(--res-purple); font-weight:700; text-decoration:none; }
        .res-list a:hover { text-decoration:underline; color:var(--res-orange); }
        .res-list .by { display:block; color:var(--res-muted); font-size:.85rem; font-weight:400; margin-top:.1em; }
        .res-note { max-width:820px; margin:1em auto 0; text-align:center; color:var(--res-muted); font-size:.92rem; font-style:italic; }
        </style>

        <div class="res-wrap">
        <p class="res-intro">A curated, growing collection of <strong>freely available</strong> books, video courses and websites for learning the tools we use in the group — from first steps in Python to model predictive control, reinforcement learning and Bayesian optimisation. Everything linked here is free to access.</p>

        <div class="res-nav">
          <a href="#python">🐍 Python</a>
          <a href="#dynamic-modelling">🌀 Dynamic Modelling</a>
          <a href="#optimization">📈 Optimisation &amp; Design Opt.</a>
          <a href="#mpc">🎛️ Model Predictive Control</a>
          <a href="#rl">🤖 Reinforcement Learning</a>
          <a href="#bayes-opt">🎯 Bayesian Optimisation</a>
        </div>
        </div>
    design:
      columns: '1'

  - block: markdown
    content:
      text: |
        <div class="res-wrap">

        <div class="res-section" id="python">
          <div class="res-head">
            <span class="res-emoji">🐍</span>
            <h3>Python</h3>
            <span class="res-sub">Start here if you're new to programming — no prior experience needed.</span>
          </div>
          <div class="res-grid">
            <div class="res-card">
              <h4><span class="res-tag books">Books</span></h4>
              <ul class="res-list">
                <li><a href="https://automatetheboringstuff.com/">Automate the Boring Stuff with Python</a><span class="by">Al Sweigart — practical, beginner-friendly, read free online</span></li>
                <li><a href="https://www.py4e.com/book">Python for Everybody</a><span class="by">Charles Severance — gentle intro to programming</span></li>
                <li><a href="https://greenteapress.com/wp/think-python-2e/">Think Python (2e)</a><span class="by">Allen B. Downey — thinking like a computer scientist</span></li>
                <li><a href="https://python.swaroopch.com/">A Byte of Python</a><span class="by">Swaroop C. H. — concise first introduction</span></li>
              </ul>
            </div>
            <div class="res-card">
              <h4><span class="res-tag videos">YouTube</span></h4>
              <ul class="res-list">
                <li><a href="https://www.youtube.com/watch?v=rfscVS0vtbw">Python Full Course for Beginners</a><span class="by">freeCodeCamp — 4.5 hour complete intro</span></li>
                <li><a href="https://www.youtube.com/playlist?list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU">Python Tutorials</a><span class="by">Corey Schafer — clear, topic-by-topic playlist</span></li>
                <li><a href="https://www.youtube.com/playlist?list=PLlRFEj9H3Oj7Bp8-DfGpfAfDBiblRfl5p">Python for Everybody</a><span class="by">Dr. Chuck (Charles Severance) — full course playlist</span></li>
                <li><a href="https://www.youtube.com/playlist?list=PLQVvvaa0QuDeAams7fkdcwOGBpGdHpXln">Python Programming</a><span class="by">sentdex — hands-on, project-based</span></li>
              </ul>
            </div>
            <div class="res-card">
              <h4><span class="res-tag sites">Websites</span></h4>
              <ul class="res-list">
                <li><a href="https://docs.python.org/3/tutorial/">The Official Python Tutorial</a><span class="by">python.org — the authoritative starting point</span></li>
                <li><a href="https://www.kaggle.com/learn/python">Kaggle: Learn Python</a><span class="by">Free hands-on micro-course with exercises</span></li>
                <li><a href="https://realpython.com/">Real Python</a><span class="by">Well-written tutorials on every topic</span></li>
                <li><a href="https://lectures.scientific-python.org/">Scientific Python Lectures</a><span class="by">NumPy, SciPy, Matplotlib for science &amp; engineering</span></li>
              </ul>
            </div>
          </div>
        </div>

        <div class="res-section" id="dynamic-modelling">
          <div class="res-head">
            <span class="res-emoji">🌀</span>
            <h3>Dynamic Modelling</h3>
            <span class="res-sub">Differential equations, dynamical systems and data-driven models.</span>
          </div>
          <div class="res-grid">
            <div class="res-card">
              <h4><span class="res-tag books">Books</span></h4>
              <ul class="res-list">
                <li><a href="https://databookuw.com/">Data-Driven Science &amp; Engineering</a><span class="by">Brunton &amp; Kutz — free PDF + code + videos</span></li>
                <li><a href="https://www.math.hkust.edu.hk/~machas/differential-equations-for-engineers.pdf">Differential Equations for Engineers</a><span class="by">Jeffrey R. Chasnov — free textbook (HKUST)</span></li>
                <li><a href="https://apmonitor.com/pdc/">Process Dynamics &amp; Control</a><span class="by">APMonitor — course notes, code and examples</span></li>
              </ul>
            </div>
            <div class="res-card">
              <h4><span class="res-tag videos">YouTube</span></h4>
              <ul class="res-list">
                <li><a href="https://www.youtube.com/playlist?list=PLMrJAkhIeNNTYaOnVI3QpH7jgULnAmvPA">Nonlinear Dynamics &amp; Chaos</a><span class="by">Steve Brunton — accessible, visual playlist</span></li>
                <li><a href="https://www.youtube.com/playlist?list=PLMrJAkhIeNNR6DzT17-MM1GHLkuYVjhyt">Engineering Math: Differential Equations &amp; Dynamical Systems</a><span class="by">Steve Brunton</span></li>
                <li><a href="https://www.youtube.com/playlist?list=PLLy_2iUCG87D1CXFxE-SxCFZUiJzQ3IvE">Process Dynamics &amp; Control</a><span class="by">John Hedengren (APMonitor)</span></li>
              </ul>
            </div>
            <div class="res-card">
              <h4><span class="res-tag sites">Websites</span></h4>
              <ul class="res-list">
                <li><a href="https://apmonitor.com/pdc/">APMonitor — Process Dynamics &amp; Control</a><span class="by">Interactive lessons with Python (GEKKO)</span></li>
                <li><a href="https://pysindy.readthedocs.io/">PySINDy</a><span class="by">Discover dynamical models from data</span></li>
                <li><a href="https://docs.scipy.org/doc/scipy/tutorial/integrate.html">SciPy: Integrating ODEs</a><span class="by"><code>solve_ivp</code> tutorial and reference</span></li>
              </ul>
            </div>
          </div>
        </div>

        <div class="res-section" id="optimization">
          <div class="res-head">
            <span class="res-emoji">📈</span>
            <h3>Optimisation &amp; Design Optimisation</h3>
            <span class="res-sub">From convex optimisation foundations to engineering design (MDO).</span>
          </div>
          <div class="res-grid">
            <div class="res-card">
              <h4><span class="res-tag books">Books</span></h4>
              <ul class="res-list">
                <li><a href="https://mdobook.github.io/">Engineering Design Optimization</a><span class="by">Martins &amp; Ning — free PDF, ideal for design opt.</span></li>
                <li><a href="https://web.stanford.edu/~boyd/cvxbook/">Convex Optimization</a><span class="by">Boyd &amp; Vandenberghe — free PDF, the classic</span></li>
                <li><a href="https://algorithmsbook.com/optimization/">Algorithms for Optimization</a><span class="by">Kochenderfer &amp; Wheeler (MIT) — free PDF</span></li>
              </ul>
            </div>
            <div class="res-card">
              <h4><span class="res-tag videos">YouTube</span></h4>
              <ul class="res-list">
                <li><a href="https://www.youtube.com/playlist?list=PL3940DD956CDDC95D">Convex Optimization (EE364a)</a><span class="by">Stephen Boyd — full Stanford lecture course</span></li>
                <li><a href="https://www.youtube.com/playlist?list=PLMrJAkhIeNNRRj7uYIYleqOl1YSXBFljz">Optimization</a><span class="by">Steve Brunton — gradient methods, constraints and more</span></li>
                <li><a href="https://www.youtube.com/playlist?list=PLW8LN2Lb2iAvUuHTb0FbFXFuxlUW1PfQE">Multidisciplinary Design Optimization</a><span class="by">Joaquim Martins — companion to the MDO book</span></li>
              </ul>
            </div>
            <div class="res-card">
              <h4><span class="res-tag sites">Websites</span></h4>
              <ul class="res-list">
                <li><a href="https://www.pyomo.org/">Pyomo</a><span class="by">Python modelling for optimisation problems</span></li>
                <li><a href="https://www.cvxpy.org/">CVXPY</a><span class="by">Convex optimisation, embedded in Python</span></li>
                <li><a href="https://docs.scipy.org/doc/scipy/reference/optimize.html">SciPy Optimize</a><span class="by">Practical solvers for everyday problems</span></li>
                <li><a href="https://neos-guide.org/">NEOS Optimization Guide</a><span class="by">Reference on optimisation problem types</span></li>
              </ul>
            </div>
          </div>
        </div>

        <div class="res-section" id="mpc">
          <div class="res-head">
            <span class="res-emoji">🎛️</span>
            <h3>Model Predictive Control</h3>
            <span class="res-sub">Optimisation-based control — theory, computation and implementation.</span>
          </div>
          <div class="res-grid">
            <div class="res-card">
              <h4><span class="res-tag books">Books</span></h4>
              <ul class="res-list">
                <li><a href="https://sites.engineering.ucsb.edu/~jbraw/mpc/">Model Predictive Control: Theory, Computation &amp; Design</a><span class="by">Rawlings, Mayne &amp; Diehl — free PDF (2nd ed.)</span></li>
                <li><a href="http://www.mpc.berkeley.edu/mpc-course-material">Predictive Control for Linear &amp; Hybrid Systems</a><span class="by">Borrelli, Bemporad &amp; Morari — draft + slides</span></li>
              </ul>
            </div>
            <div class="res-card">
              <h4><span class="res-tag videos">YouTube</span></h4>
              <ul class="res-list">
                <li><a href="https://www.youtube.com/playlist?list=PLn8PRpmsu08ozoeoXgxPSBKLyd4YEHww8">Understanding Model Predictive Control</a><span class="by">MATLAB Tech Talks — clear, intuitive intro</span></li>
                <li><a href="https://www.youtube.com/watch?v=YwodGM2eoy4">Model Predictive Control</a><span class="by">Steve Brunton — concise overview</span></li>
                <li><a href="https://www.youtube.com/playlist?list=PLLy_2iUCG87BW9UyMbfyOaXcv1FTVA83q">Model Predictive Control</a><span class="by">John Hedengren (APMonitor) — hands-on with Python</span></li>
              </ul>
            </div>
            <div class="res-card">
              <h4><span class="res-tag sites">Websites</span></h4>
              <ul class="res-list">
                <li><a href="https://www.do-mpc.com/">do-mpc</a><span class="by">Python toolbox for robust &amp; nonlinear MPC</span></li>
                <li><a href="https://web.casadi.org/">CasADi</a><span class="by">Symbolic framework for optimal control</span></li>
                <li><a href="https://gekko.readthedocs.io/">GEKKO</a><span class="by">Python for dynamic optimisation &amp; MPC</span></li>
              </ul>
            </div>
          </div>
        </div>

        <div class="res-section" id="rl">
          <div class="res-head">
            <span class="res-emoji">🤖</span>
            <h3>Reinforcement Learning</h3>
            <span class="res-sub">Learning to make decisions through interaction and reward.</span>
          </div>
          <div class="res-grid">
            <div class="res-card">
              <h4><span class="res-tag books">Books</span></h4>
              <ul class="res-list">
                <li><a href="http://incompleteideas.net/book/the-book-2nd.html">Reinforcement Learning: An Introduction</a><span class="by">Sutton &amp; Barto — the standard text, free PDF</span></li>
                <li><a href="https://spinningup.openai.com/">Spinning Up in Deep RL</a><span class="by">OpenAI — free, code-first guide to deep RL</span></li>
              </ul>
            </div>
            <div class="res-card">
              <h4><span class="res-tag videos">YouTube</span></h4>
              <ul class="res-list">
                <li><a href="https://www.youtube.com/playlist?list=PLqYmG7hTraZDM-OYHWgPebj2MfCFzFObQ">Introduction to Reinforcement Learning</a><span class="by">David Silver (DeepMind) — the classic course</span></li>
                <li><a href="https://www.youtube.com/playlist?list=PLqYmG7hTraZDVH599EItlEWsUOsJbAodm">DeepMind x UCL RL Lecture Series</a><span class="by">DeepMind &amp; UCL — modern, thorough</span></li>
                <li><a href="https://www.youtube.com/playlist?list=PLMrJAkhIeNNQe1JXNvaFvURxGY4gE9k74">Reinforcement Learning</a><span class="by">Steve Brunton — engineering perspective</span></li>
              </ul>
            </div>
            <div class="res-card">
              <h4><span class="res-tag sites">Websites</span></h4>
              <ul class="res-list">
                <li><a href="https://huggingface.co/learn/deep-rl-course/unit0/introduction">Hugging Face Deep RL Course</a><span class="by">Free, hands-on, with certificates</span></li>
                <li><a href="https://gymnasium.farama.org/">Gymnasium</a><span class="by">Standard API &amp; environments for RL</span></li>
                <li><a href="https://stable-baselines3.readthedocs.io/">Stable-Baselines3</a><span class="by">Reliable RL algorithm implementations</span></li>
              </ul>
            </div>
          </div>
        </div>

        <div class="res-section" id="bayes-opt">
          <div class="res-head">
            <span class="res-emoji">🎯</span>
            <h3>Bayesian Optimisation</h3>
            <span class="res-sub">Sample-efficient optimisation of expensive black-box functions.</span>
          </div>
          <div class="res-grid">
            <div class="res-card">
              <h4><span class="res-tag books">Books</span></h4>
              <ul class="res-list">
                <li><a href="https://bayesoptbook.com/">Bayesian Optimization</a><span class="by">Roman Garnett — free PDF, the definitive text</span></li>
                <li><a href="https://gaussianprocess.org/gpml/">Gaussian Processes for Machine Learning</a><span class="by">Rasmussen &amp; Williams — free PDF (GP foundations)</span></li>
              </ul>
            </div>
            <div class="res-card">
              <h4><span class="res-tag videos">YouTube</span></h4>
              <ul class="res-list">
                <li><a href="https://www.youtube.com/watch?v=C5nqEHpdyoE">Machine Learning - Bayesian Optimization</a><span class="by">Nando de Freitas — clear lecture</span></li>
                <li><a href="https://www.youtube.com/watch?v=_SC5_2vkgbA">Gaussian Process &amp; Bayesian Optimization</a><span class="by">Introductory tutorial talk</span></li>
              </ul>
            </div>
            <div class="res-card">
              <h4><span class="res-tag sites">Websites</span></h4>
              <ul class="res-list">
                <li><a href="https://distill.pub/2020/bayesian-optimization/">Exploring Bayesian Optimization</a><span class="by">Distill.pub — beautiful visual explainer</span></li>
                <li><a href="https://botorch.org/">BoTorch</a><span class="by">Bayesian optimisation in PyTorch</span></li>
                <li><a href="https://gpytorch.ai/">GPyTorch</a><span class="by">Scalable Gaussian processes</span></li>
                <li><a href="https://ax.dev/">Ax</a><span class="by">Adaptive experimentation platform (Meta)</span></li>
              </ul>
            </div>
          </div>
        </div>

        <p class="res-note">Know a great free resource we should add? <a href="/contact/">Get in touch</a> — we'd love to grow this list.</p>

        </div>
    design:
      columns: '1'
---
