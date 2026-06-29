---
title: 'PhysisForcing: Physics Reinforced World Simulator for Robotic Manipulation'
title_zh: 'PhysisForcing: Physics Reinforced World Simulator'
authors:
- Peiwen Zhang
- Yufan Deng
- Shangkun Sun
- Juncheng Ma
- Duomin Wang
- Jonas Du
- Zilin Pan
- Ye Huang
- Hao Liang
- Songyan Huang
arxiv_id: '2606.28128'
url: https://arxiv.org/abs/2606.28128
pdf_url: https://arxiv.org/pdf/2606.28128
published: '2026-06-25'
collected: '2026-06-29'
category: Multimodal
direction: Multimodal
tags:
- Multimodal
- LLM
one_liner: Video generation models have emerged as a promising paradigm for embodied
  world simulation. How...
practical_value: '- 可先根据论文标题和摘要判断是否进入人工精读列表。

  - 当前未配置 LLM API Key，已使用规则摘要兜底；配置 Key 后会恢复中文精读、打分和业务可借鉴点生成。'
score: 9
source: huggingface-daily
depth: abstract
---

### 摘要

Video generation models have emerged as a promising paradigm for embodied world simulation. However, both general-domain video generators and robot-specific data fine-tuned models can still produce physically implausible manipulations, including discontinuous motion trajectories and inconsistent robot-object interactions, which limits their reliability as world simulators. Through extensive experiments, we find that such physical instability mainly arises from two factors: deformation of moving objects and implausible spatio-temporal correlations among interacting entities, particularly during contact. Building on this observation, we propose PhysisForcing, a scalable training framework that strengthens physical consistency by focusing supervision on physics-informative regions through joint optimization of pixel-level and semantic-level features. The framework consists of a pixel-level trajectory alignment loss, which supervises DiT features using reference point trajectories, and a semantic-level relational alignment loss, which aligns DiT features with inter-region relations extracted from a frozen video understanding encoder. Extensive experiments on R-Bench, PAI-Bench, and EZS-Bench show that PhysisForcing consistently improves embodied video generation over strong baselines, improving the Wan2.2-I2V-A14B and Cosmos3-Nano base models on R-Bench by 22.3\% and 9.2\% (7.1\% and 3.7\% over vanilla finetuning), with the Cosmos3-Nano variant attaining the best overall score. Beyond generation, as a world model under the WorldArena action-planner protocol it raises the closed-loop success rate from 16.0\% to 24.0\% and further improves downstream policy success, indicating that physically aligned video models yield stronger representations for robotic manipulation.

> 当前运行未检测到 LLM API Key，本卡片由规则降级流程生成。
