---
title: 'Beyond Independent Labels: Schwartz-Geometry Decoding for Human Value Detection'
title_zh: 超越独立标签：面向人类价值观检测的Schwartz几何解码
authors:
- Víctor Yeste
- Paolo Rosso
affiliations:
- PRHLT Research Center, Universitat Politècnica de València, Spain
- School of Science, Engineering and Design, Universidad Europea de Valencia, Spain
- Valencian Graduate School and Research Network of Artificial Intelligence (ValgrAI)
arxiv_id: '2607.05052'
url: https://arxiv.org/abs/2607.05052
pdf_url: https://arxiv.org/pdf/2607.05052
published: '2026-07-06'
collected: '2026-07-08'
category: LLM
direction: 多标签分类 · 理论约束解码优化
tags:
- Multi-label Classification
- Decoding Strategy
- Label Coherence
- Schwartz Values
- DeBERTa
one_liner: 提出Schwartz感知后验能量解码器，在不损失F1的前提下提升多标签输出和理论连续体的一致性
practical_value: '- 多标签推荐/分类场景（如用户兴趣打标、商品属性标注）可借鉴后验能量解码思路，不改动训练逻辑的前提下引入领域先验结构（如标签兼容/互斥关系）约束输出一致性，无指标损失

  - 做领域先验结构注入时，优先选择推理端轻量化解码方案，相比训练时加约束的方式效果更稳定，无需修改基线模型训练流程，工程落地成本极低

  - 标签体系有明确逻辑结构的场景，可直接复用「理论几何结构+能量打分重排标签集」框架，不需要额外标注数据即可优化输出合理性'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有人类价值观检测多将19个Schwartz价值观作为独立标签做多标签分类，忽略理论定义的环形连续结构（相邻兼容、对立互斥），输出标签集不符合内在逻辑。
### 方法关键点
对比两种先验结构注入方案：1）训练时加入几何感知目标；2）推理后验阶段引入Schwartz感知能量解码器，对完整标签集联合打分重排，通过选择规则保证F1指标无损失。
### 关键结果
训练时注入仅带来有限收益，效果与随机标签顺序无差异；后验解码器在Macro-F1、Micro-F1完全无下降的前提下，标签集与理论连续体的一致性显著提升，且收益仅来自真实Schwartz结构，随机排列/共现图作为先验无增益；Qwen2.5-72B-Instruct推理时注入连续体的效果仍弱于监督结构化预测。
