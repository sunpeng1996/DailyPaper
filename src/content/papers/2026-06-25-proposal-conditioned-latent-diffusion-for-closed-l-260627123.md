---
title: Proposal-Conditioned Latent Diffusion for Closed-Loop Traffic Scenario Generation
title_zh: Proposal-Conditioned Latent Diffusion for Closed-L
authors:
- Shubham Vaijanath Phoolari
- Aleyna Kara
- Christoph Lauer
- Steven Peters
arxiv_id: '2606.27123'
url: https://arxiv.org/abs/2606.27123
pdf_url: https://arxiv.org/pdf/2606.27123
published: '2026-06-25'
collected: '2026-06-27'
category: Agent
direction: Agent
tags:
- Agent
- LLM
one_liner: Closed-loop traffic simulation remains challenging because it must generate
  interactive multi-a...
practical_value: '- 可先根据论文标题和摘要判断是否进入人工精读列表。

  - 当前未配置 DeepSeek API Key，已使用规则摘要兜底；配置 Key 后会恢复中文精读、打分和业务可借鉴点生成。'
score: 8
source: arxiv-cs.CV
depth: abstract
---

### 摘要

Closed-loop traffic simulation remains challenging because it must generate interactive multi-agent behaviors that are scene-consistent and controllable throughout rollout. Prior diffusion-based approaches achieve strong realism, but their computational cost can hinder deployment in time-constrained replanning loops for autonomous vehicle planning and simulation. We present a diffusion-based scenario generation framework conditioned on instance-centric scene context and multimodal proposal priors, with optional test-time guidance for shaping safety-critical behaviors. A compact action-latent representation and proposal-based initialization improve sampling efficiency and reduce per-step runtime without retraining. Experiments on the Waymo Open Motion Dataset demonstrate a favorable balance among realism, safety, and controllability across diverse interactive scenarios, while showing that test-time guidance enables systematic trade-offs among competing objectives.

> 当前运行未检测到 DeepSeek API Key，本卡片由规则降级流程生成。
