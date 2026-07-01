---
title: 'Before Thinking, Learn to Decide: Proactive Routing for Efficient Visual Reasoning'
title_zh: 先决策后推理：面向高效视觉推理的主动路由范式PRP
authors:
- Yinan Zhou
- Haokun Lin
- Yichen Wu
- Caifeng Shan
- Zhenan Sun
- Yuxin Chen
- Teng Wang
- Chen Ma
- Li Zhu
- Ying Shan
affiliations:
- Xi'an Jiaotong University
- Tencent IEG ARC Lab
- City University of Hong Kong
- Institute of Automation CAS
- Harvard University
arxiv_id: '2606.30217'
url: https://arxiv.org/abs/2606.30217
pdf_url: https://arxiv.org/pdf/2606.30217
published: '2026-06-29'
collected: '2026-06-30'
category: Reasoning
direction: 多模态推理 · 大小模型路由优化
tags:
- MLLM
- GRPO
- Routing
- Visual Reasoning
- Inference Acceleration
one_liner: 基于GRPO训练的多模态大小模型主动路由方案，推理前决策实现无损精度下最高2.41倍加速
practical_value: '- 电商多模态内容审核/商品理解场景可直接复用该大小模型路由框架，简单query由小模型处理，难query路由至大模型，在不损失效果的前提下降低推理成本30%+

  - 采用GRPO训练置信度打分的方案替代传统SFT特殊token方案，无需大量正负轨迹标注，还可避免SFT导致的模型效果下降，适配标注资源有限的业务场景

  - 流量波动大的实时推荐/广告场景可复用批量动态阈值策略，无需预刷验证集，基于实时请求批量打分排序动态分配算力，兼顾效率和峰值承载能力

  - 同置信度分桶内的Internal Probability Ranking技巧可迁移到query难度分级、召回结果排序等场景，提升细粒度排序的准确性'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
多模态大模型视觉推理依赖长思维链，简单query也会产生不必要的推理开销，传统LLM路由方法存在明显缺陷：token概率路由在多模态场景下与精度相关性极低；SFT训练特殊置信度token方案数据敏感，且需要等小模型输出完整结果才路由，还完全不考虑目标大模型是否能解决当前query，导致路由效率低、收益有限。
### 方法关键点
- 基于GRPO设计Draft Rating Learning（DRL）：让小模型在推理开始前仅输出1-2个打分token即可评估自身对当前query的解决置信度，无需生成完整回答即可完成路由决策。
- 新增Joint Rating Learning（JRL）：同时预测目标大模型对当前query的解决能力，路由策略优先分配大模型擅长的query，而非单纯分配最难的query，最大化大模型价值。
- 训练时设计动态分数替换策略解决优势消失问题，采用任务特定优化分开优化打分token和推理token，不损害小模型原有推理能力。
- 推理时新增同分数桶内的Internal Probability Ranking，基于打分token的logit分布做细粒度排序，进一步提升路由精度。
### 关键结果
在ChartQA、MathVista、MathVerse三个多模态推理基准上对比随机路由、token概率路由、SFT特殊token路由三个基线：JRL方案在MathVista上60% query走小模型时，精度超过单独使用38B大模型，同时实现2.41倍推理加速；DRL方案在保持精度无损的前提下也能实现1.5倍左右的推理加速。
最值得记住的一句话：路由的核心不是把最难的query给大模型，而是把大模型最擅长的query给大模型，才能同时兼顾效果和效率。
