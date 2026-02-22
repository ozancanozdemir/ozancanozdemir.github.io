---
permalink: /
title: "Ozancan Ozdemir"
excerpt: "PhD Candidate • ML for Time Series • Stock Market Forecasting • Public Writing"
author_profile: true
redirect_from:
  - /about/
  - /about.html
---

<div class="hero">
  <img class="hero-img" src="https://upload.wikimedia.org/wikipedia/commons/5/5d/Gezicht_op_Ankara_Rijksmuseum_SK-A-2055.jpeg" alt="View of Ankara">
  <div class="hero-overlay"></div>

  <div class="hero-content">
    <div class="kicker">PhD Candidate · University of Groningen (Bernoulli Institute)</div>
    <h1 class="title">Ozancan Ozdemir</h1>
    <p class="subtitle">
      I build machine learning methods for <strong>sequential data</strong>—especially <strong>time series</strong>—with a focus on
      <strong>stock market forecasting</strong>, robust evaluation, and real-world decision settings.
      I also write publicly about AI, incentives, and institutions.
    </p>

    <div class="cta-row">
      <a class="btn primary" href="https://ozancanozdemir.github.io/cv/">CV</a>
      <a class="btn" href="/publications/">Publications</a>
      <a class="btn" href="/talks/">Talks</a>
      <a class="btn" href="https://x.com/OzancanOzdemir">X</a>
    </div>
  </div>
</div>

<div class="grid">
  <div class="card">
    <h2>About</h2>
    <p>
      I’m a statistician by training (METU, valedictorian for both BSc and MSc cohorts) and currently a PhD Candidate in Groningen.
      My work lives at the intersection of <strong>machine learning</strong>, <strong>deep learning</strong>, and <strong>time series</strong>:
      how we forecast, how we evaluate under distribution shift, and how we design systems that keep working when the world changes.
    </p>
    <p>
      A recurring theme in my research is <strong>financial prediction</strong>—especially <strong>excess return forecasting</strong> using
      fundamental indicators, feature selection, and model comparison. I care less about “benchmark wins” and more about
      <strong>what models learn, what breaks, and what remains stable</strong>.
    </p>
  </div>

  <div class="card">
    <h2>Research interests</h2>
    <ul class="bullets">
      <li><strong>Time series & sequence modeling</strong>: forecasting, representation learning</li>
      <li><strong>Stock market & fundamentals</strong>: excess returns, indicators, feature selection</li>
      <li><strong>Robust evaluation</strong>: distribution shift, generalization, metric design</li>
      <li><strong>Applied ML</strong>: decision-making under uncertainty, interpretability in practice</li>
    </ul>

    <div class="mini">
      <span class="pill">Time Series</span>
      <span class="pill">Deep Learning</span>
      <span class="pill">Forecasting</span>
      <span class="pill">Stock Market</span>
      <span class="pill">Evaluation</span>
    </div>
  </div>
</div>

---

## Writing

<div class="grid2">
  <a class="linkcard" href="https://t24.com.tr/yazarlar/ozancan-ozdemir">
    <div class="icon">
      <!-- Newspaper icon -->
      <svg viewBox="0 0 24 24" fill="none" aria-hidden="true">
        <path d="M6 4h11a2 2 0 0 1 2 2v13a1 1 0 0 1-1 1H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2Z" stroke="currentColor" stroke-width="1.5"/>
        <path d="M8 8h7M8 11h7M8 14h5" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/>
      </svg>
    </div>
    <div>
      <div class="label">T24 Column</div>
      <div class="desc">Essays on AI, society, and public reasoning — in Turkish.</div>
      <div class="hint">Read on T24 →</div>
    </div>
  </a>

  <a class="linkcard" href="https://substack.com/@ozancanozdemir">
    <div class="icon">
      <!-- Notebook icon -->
      <svg viewBox="0 0 24 24" fill="none" aria-hidden="true">
        <path d="M7 4h10a2 2 0 0 1 2 2v14H7a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2Z" stroke="currentColor" stroke-width="1.5"/>
        <path d="M9 8h7M9 11h7M9 14h7" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/>
        <path d="M7 20V4" stroke="currentColor" stroke-width="1.5"/>
      </svg>
    </div>
    <div>
      <div class="label">Substack</div>
      <div class="desc">Shorter notes, drafts, and ongoing thinking — more informal.</div>
      <div class="hint">Open Substack →</div>
    </div>
  </a>
</div>

---

## Selected work & talks

If you’re looking for an overview of my work:
- <a href="/publications/">Publications</a>
- <a href="/talks/">Talks</a>
- <a href="https://ozancanozdemir.github.io/cv/">CV</a>

---

<style>
  /* Layout */
  .hero { position: relative; border-radius: 18px; overflow: hidden; margin: 0 0 1.25rem 0; }
  .hero-img { width: 100%; height: 360px; object-fit: cover; display:block; }
  .hero-overlay { position:absolute; inset:0; background: linear-gradient(90deg, rgba(0,0,0,.74), rgba(0,0,0,.28)); }
  .hero-content { position:absolute; inset:0; padding: 28px; display:flex; flex-direction:column; justify-content:flex-end; gap: 10px; }
  .kicker { color: rgba(255,255,255,.88); font-size: .95rem; letter-spacing: .2px; }
  .title { color:#fff; margin:0; font-size: 2.25rem; line-height:1.1; }
  .subtitle { color: rgba(255,255,255,.90); margin: 0; max-width: 980px; font-size: 1.05rem; }
  .cta-row { display:flex; flex-wrap:wrap; gap:10px; margin-top: 8px; }

  /* Buttons */
  .btn { display:inline-block; padding:10px 14px; border-radius: 999px; text-decoration:none;
         border: 1px solid rgba(255,255,255,.38); color:#fff; background: rgba(255,255,255,.10);
         backdrop-filter: blur(6px); }
  .btn:hover { background: rgba(255,255,255,.16); }
  .btn.primary { border-color: rgba(255,255,255,.55); background: rgba(255,255,255,.18); }

  /* Cards */
  .grid { display:grid; grid-template-columns: 1.2fr .8fr; gap: 14px; margin: 10px 0 0 0; }
  .card { border: 1px solid rgba(0,0,0,.08); border-radius: 16px; padding: 16px; background: rgba(255,255,255,.75); }
  .card h2 { margin-top: 0; }

  /* Interest list + pills */
  .bullets { margin: .5rem 0 0 1.1rem; }
  .bullets li { margin: .35rem 0; line-height: 1.35; }
  .mini { display:flex; flex-wrap:wrap; gap:8px; margin-top: 12px; }
  .pill { display:inline-block; padding: 6px 10px; border-radius: 999px; font-size: .9rem;
          border: 1px solid rgba(0,0,0,.10); background: rgba(0,0,0,.03); }

  /* Writing link cards */
  .grid2 { display:grid; grid-template-columns: 1fr 1fr; gap: 14px; }
  .linkcard { display:flex; gap: 12px; align-items:flex-start; text-decoration:none;
              border: 1px solid rgba(0,0,0,.10); border-radius: 16px; padding: 14px;
              background: rgba(255,255,255,.80); }
  .linkcard:hover { transform: translateY(-1px); transition: transform .12s ease; }
  .icon { width: 40px; height: 40px; border-radius: 12px; display:flex; align-items:center; justify-content:center;
          border: 1px solid rgba(0,0,0,.08); background: rgba(0,0,0,.03); color: rgba(0,0,0,.70); flex: 0 0 auto; }
  .icon svg { width: 22px; height: 22px; }

  .label { font-weight: 700; color: rgba(0,0,0,.88); }
  .desc { color: rgba(0,0,0,.72); margin-top: 2px; }
  .hint { margin-top: 8px; font-weight: 600; color: rgba(0,0,0,.82); }

  /* Responsive */
  @media (max-width: 980px) {
    .grid { grid-template-columns: 1fr; }
    .grid2 { grid-template-columns: 1fr; }
    .hero-img { height: 320px; }
    .title { font-size: 2.0rem; }
  }
</style>
