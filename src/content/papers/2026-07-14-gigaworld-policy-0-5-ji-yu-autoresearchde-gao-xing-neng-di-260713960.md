---
title: 'GigaWorld-Policy-0.5: A Faster and Stronger WAM Empowered by AutoResearch'
title_zh: GigaWorld-Policy-0.5：基于AutoResearch的高性能低延迟世界动作模型
authors:
- GigaWorld Team
- Angen Ye
- Angyuan Ma
- Boyuan Wang
- Chaojun Ni
- Fangzheng Ye
- Guan Huang
- Guo Li
- Guosheng Zhao
- Haodong Yan
affiliations:
- GigaAI
- Tsinghua University
arxiv_id: '2607.13960'
url: https://arxiv.org/abs/2607.13960
pdf_url: https://arxiv.org/pdf/2607.13960
published: '2026-07-14'
collected: '2026-07-18'
category: Agent
direction: Agent 世界动作模型推理优化
tags:
- WAM
- MoE
- AutoResearch
- Inference Optimization
- Agent Policy
one_liner: 提出动作中心化世界动作模型，结合AutoResearch实现低延迟高泛化的机器人控制策略
practical_value: '- 训练时引入多任务额外监督、推理时仅保留核心任务的范式，可迁移到搜推多任务训练线上部署流程，降低线上推理开销

  - MoE架构按任务拆分专用专家的设计，可复用在搜推多目标模型中，推理时仅激活对应目标的专家，显著降低延迟

  - Agent驱动的自动超参搜索流程，可直接落地到算法迭代调优环节，减少人工调参成本，提升迭代效率'
score: 4
source: huggingface-daily
depth: abstract
---

### 动机
现有World Action Models (WAM) 推理时需显式生成未来视频，计算开销极高，无法支撑实时闭环部署。
### 方法关键点
1. 采用动作中心化范式：训练阶段用未来视觉动态做密集监督，推理阶段仅解码动作、不生成视频，从架构层面压缩推理开销；
2. 预训练采用混合Action-Conditioned World Modeling (AC-WM) 与WAM训练策略，强化视觉动态与机器人动作的耦合度，提升动作表征的下游迁移性；
3. 引入Mixture-of-Transformers架构，将视觉动态建模与动作生成拆分为专用专家，推理时仅激活动作生成专家，降低激活计算量；
4. 落地Agent驱动的AutoResearch流水线自动搜索训练配置，大幅减少超参调优的人工干预与时间成本。
### 关键结果
在本地RTX 4090环境下推理延迟仅85ms，完全保留未来视觉监督的训练收益，同时大幅提升机器人控制的推理效率。
