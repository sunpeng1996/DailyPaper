---
title: Object-Centric Residual RL for Zero-Shot Sim-to-Real VLA Enhancement
title_zh: Object-Centric Residual RL for Zero-Shot Sim-to-Re
authors:
- Kinam Kim
- Namiko Saito
- Heecheol Kim
- Katsushi Ikeuchi
- Jaegul Choo
- Yasuyuki Matsushita
arxiv_id: '2606.18953'
url: https://arxiv.org/abs/2606.18953
pdf_url: https://arxiv.org/pdf/2606.18953
published: '2026-06-16'
collected: '2026-06-29'
category: Multimodal
direction: Multimodal
tags:
- Multimodal
- LLM
one_liner: Vision-Language-Action (VLA) models can generalize across diverse manipulation
  tasks, but their...
practical_value: '- 可先根据论文标题和摘要判断是否进入人工精读列表。

  - 当前未配置 LLM API Key，已使用规则摘要兜底；配置 Key 后会恢复中文精读、打分和业务可借鉴点生成。'
score: 6
source: huggingface-daily
depth: abstract
---

### 摘要

Vision-Language-Action (VLA) models can generalize across diverse manipulation tasks, but their imitation-learning-based policies remain brittle in precise physical interactions due to compounding execution errors; Can a reinforcement learning policy trained purely in simulation improve the robustness of real-world VLAs zero-shot? Residual RL, which learns a corrective policy on top of a frozen VLA, offers a natural framework, but existing approaches face a fundamental sim-to-real dilemma: privileged-state methods require lossy distillation for deployment; image-based methods suffer from the visual domain gap; and real-world RL is costly and unsafe. We propose an object-centric residual RL framework that refines VLA actions using object poses, enabling a compact observation space that transfers consistently between simulation and reality. To align the two domains, we additionally replay the same teleoperation demonstrations in simulation to train a sim counterpart of the real-world VLA. The residual RL policy is trained only in simulation with pose noise injection and dropout, and transfers zero-shot to the real robot. Across five manipulation tasks on a real Franka Research 3 (FR3) robot, our method improves the success rate from 42% to 76% zero-shot, and the improved rollouts can be further reused to retrain the base VLA for self-improvement without additional teleoperation. Project page: https://www.microsoft.com/en-us/research/articles/object-centric-residual-rl/

> 当前运行未检测到 LLM API Key，本卡片由规则降级流程生成。
