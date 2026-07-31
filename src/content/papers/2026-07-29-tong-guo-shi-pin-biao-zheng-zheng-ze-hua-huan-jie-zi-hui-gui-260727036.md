---
title: Mitigating Compounding Error via Video Representation Regularization
title_zh: 通过视频表征正则化缓解自回归视频生成的误差累积问题
authors:
- Taiye Chen
- Qi Zhang
- Yisen Wang
affiliations:
- Peking University
arxiv_id: '2607.27036'
url: https://arxiv.org/abs/2607.27036
pdf_url: https://arxiv.org/pdf/2607.27036
published: '2026-07-29'
collected: '2026-07-31'
category: Training
direction: 视频生成模型 · 训练正则化优化
tags:
- Video Diffusion
- Representation Regularization
- Autoregressive Generation
- Compounding Error
- Effective Rank
one_liner: 揭示视频世界模型误差累积与隐表征维度坍塌关联，提出轻量正则化提升长视频生成鲁棒性
practical_value: '- 自回归类业务场景（如电商短视频生成、长营销文案生成、长序列推荐预测）可引入effective rank作为隐表征监控指标，提前预判误差累积导致的效果退化

  - 遇到自回归长序列生成漂移问题时不要盲目堆训练数据，实验证明纯数据缩放无法缓解误差累积，优先考虑增加隐表征正则化约束

  - 提出的表征正则化仅为训练侧轻量改动，不需要修改推理逻辑，可快速迁移到各类自回归生成任务（如商品短视频生成、多轮Agent对话生成）'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
基于视频扩散的世界模型实现长程自回归视频生成时，滑动窗口推理存在严重误差累积问题，会随推理步数增加持续降低帧质量；现有研究对误差累积的底层机制缺乏明确认知，且主流的纯数据缩放范式无法提升模型的抗误差漂移能力。
### 方法关键点
1. 分析模型内部表征动态，发现误差累积与隐表征维度坍塌强耦合，生成漂移发生时表征的effective rank会骤降，可作为误差累积的量化指标
2. 提出轻量的视频表征正则化训练约束，稳定隐表征分布，抑制迭代误差累积
### 关键结果
在VBench基准的Aesthetic Quality、Imaging Quality指标上，相比Diffusion Forcing基线，分别从38.65提升至55.56、44.37提升至72.08，大幅提升长视频生成鲁棒性
