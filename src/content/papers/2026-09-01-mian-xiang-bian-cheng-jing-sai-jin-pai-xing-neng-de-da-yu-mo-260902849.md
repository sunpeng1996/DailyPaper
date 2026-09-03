---
title: Post-Training Language Models for Gold-Medal Performance in Coding Competitions
title_zh: 面向编程竞赛金牌性能的大语言模型后训练方法
authors:
- Aleksander Ficek
- Sean Narenthiran
- Mehrzad Samadi
- Somshubra Majumdar
- Boris Ginsburg
affiliations:
- NVIDIA
arxiv_id: '2609.02849'
url: https://arxiv.org/abs/2609.02849
pdf_url: https://arxiv.org/pdf/2609.02849
published: '2026-09-01'
collected: '2026-09-03'
category: Reasoning
direction: 代码推理 · 大模型后训练与测试时优化
tags:
- LLM
- Reasoning
- SFT
- RL
- Test-Time Compute
- Code Generation
one_liner: 提出端到端后训练管线与GenCorrect迭代优化策略，IOI2026得分超人类最高选手
practical_value: '- GenCorrect的迭代反馈+多样性选择思路可迁移到电商Agent场景：生成营销文案/推荐理由后，用点击率/转化率反馈迭代候选，用多样性采样避免局部最优，提升内容效果

  - 资源约束下的选型策略可复用：小模型走SFT+RL深度后训练路线，大模型走少量SFT+测试时优化路线，可根据推荐/广告场景的算力预算灵活选择

  - NVFP4低比特量化的精度-吞吐量trade-off方案可直接参考：在电商大模型推理（如个性化文案生成、实时推荐解释）场景下，用小幅度精度损失换数倍吞吐量提升，满足线上时延要求

  - 训练数据分层加权思路可借鉴：给高难度/长尾任务分配更多合成训练样本，在推荐场景里可针对低转化率/冷启动样本增广训练数据，提升长尾场景效果'
score: 9
source: huggingface-daily
depth: full_pdf
---

### 动机
编程竞赛（如IOI、ICPC）是检验LLM复杂逻辑推理、约束下问题求解能力的核心硬基准，现有金牌性能方案多为闭源，各组件贡献边界不清晰，同时如何在训练/推理资源约束下最大化效果也是工业落地的核心痛点。
### 方法关键点
- 数据层：筛选2.2万道跨度20年的竞赛编程题，用强Teacher模型生成120万（小模型）/47.7万（大模型）推理轨迹，包含自修正样本，全量排除评估集数据避免污染
- 训练层：30B MoE小模型（3B激活参数）采用3轮SFT + GRPO RL（可执行代码二进制奖励）路线，550B MoE大模型（55B激活参数）仅用1轮SFT降低训练成本
- 推理层：提出GenCorrect迭代优化策略，每轮生成200个候选，用Token shingle多样性聚类选10个提交，基于子任务得分反馈迭代最多5轮；IOI2026适配版最后一轮扩至1000候选，搭配NVFP4量化实现3.7倍吞吐量提升
### 关键实验
在IOI2025、ICPC2025、LiveCodeBench Pro三个无污染评估集上测试，对比DeepSeek-V4、GLM-5.2、GPT-OSS-120B等SOTA基线：Nano-CC在IOI2025得分从基础130提升至291（SFT+RL）、468（加GenCorrect）超金牌线；Ultra-CC在IOI2026 live测试得535.4分，超金牌线174.3分，超人类最高选手37.1分，是首个在IOI上超越人类冠军的AI系统。
### 核心结论
在推理预算充足的场景下，SFT提供核心能力底座，测试时反馈驱动的迭代优化带来的效果增益往往超过模型规模和RL训练的提升。
