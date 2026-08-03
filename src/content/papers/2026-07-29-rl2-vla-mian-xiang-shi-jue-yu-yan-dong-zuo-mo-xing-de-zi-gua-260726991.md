---
title: 'RL^2-VLA: Adaptive RL Latent Compositional Steering with Test-Time Scaling
  for Vision-Language-Action Models'
title_zh: RL²-VLA：面向视觉语言动作模型的自适应RL隐空间组合引导与测试时缩放
authors:
- Derek Ming Siang Tan
- Shailesh Shailesh
- Srikrishna Iyer
- William Wei Jie Teo
- Yuanliang Ju
- Qiao Gu
- Guillaume Sartoretti
affiliations:
- National University of Singapore
- University of Toronto
- Singapore Technologies Engineering
arxiv_id: '2607.26991'
url: https://arxiv.org/abs/2607.26991
pdf_url: https://arxiv.org/pdf/2607.26991
published: '2026-07-29'
collected: '2026-08-03'
category: Agent
direction: 具身Agent · VLA模型推理时优化
tags:
- VLA
- Offline RL
- Test-Time Adaptation
- Latent Representation
- Embodied Agent
one_liner: 提出自适应推理时RL隐空间组合引导框架，无需微调预训练VLA，显著提升跨域任务成功率
practical_value: '- 推理时自适应干预思路可直接迁移到生成式推荐、LLM导购Agent场景：仅在基座模型预测置信度低于阈值时触发RAG/重排/冷启动策略，既提升长尾场景效果，又降低不必要的算力开销

  - 隐空间组合引导方法可复用：无需微调基座大模型，仅训练轻量小模型对齐基座隐空间特征，补充基座未覆盖的长尾行为模式，低成本提升OOD场景表现

  - 状态感知的策略缩放逻辑可参考：先对基座输出做成功/失败预判断，再匹配对应干预策略，避免高置信度场景下的不必要扰动，平衡效果与用户体验'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
预训练VLA模型在高难度、跨域任务上表现显著退化，现有测试时引导方法生成的动作同质化严重，易出现关联失效；且全时间步采用统一干预策略，会扰动基座原本输出的准确动作。

### 方法关键点
1. 设计RL²自适应推理时引导框架，训练轻量离线RL策略，以冻结预训练VLA提取的高表达隐向量为输入条件，推理时将RL策略的流速度与VLA的流速度组合，融合大规模模仿学习的行为先验与离线RL带来的动作多样性，覆盖示范数据外的长尾行为。
2. 发现推理引导在成功/失败状态下遵循完全不同的缩放规律，仅在预测到基座VLA可能失败时触发组合引导，避免对高置信度准确动作的不必要扰动。

### 关键结果
跨SIMPLER、PolaRiS两个基准测试，跨域场景下成功率最高提升+17.3%，真实世界实验验证效果可从仿真环境迁移到实际部署。
