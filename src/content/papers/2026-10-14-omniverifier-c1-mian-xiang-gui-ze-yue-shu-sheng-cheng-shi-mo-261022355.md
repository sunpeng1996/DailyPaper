---
title: 'OmniVerifier-C1: Decomposed Graded Verifier for Rule-Governed Generative World
  Modeling'
title_zh: OmniVerifier-C1：面向规则约束生成式世界建模的分解式分级验证器
authors:
- Bowei Liu
- Xinchen Zhang
- Xuhuan Li
- Tianlin Zhang
- Kaian Jiang
- Jingwei Liu
- Congyang Zhao
- Yifei Qian
- Junhong Liu
- Zhiheng Li
affiliations:
- Tsinghua University
- Amap, Alibaba Group
- Microcyto
- Peking University
arxiv_id: '2610.22355'
url: https://arxiv.org/abs/2610.22355
pdf_url: https://arxiv.org/pdf/2610.22355
published: '2026-10-14'
collected: '2026-10-17'
category: Agent
direction: 世界建模Agent · 多模态分级验证
tags:
- Multimodal Verifier
- Reinforcement Learning
- World Modeling
- Generative Agent
- Graded Verification
one_liner: 提出分解式分级多模态验证器与解耦RL训练策略，提升验证泛化性，支撑结构化世界建模Agent
practical_value: '- 电商多模态生成内容（如AI商详、海报）审核可复用分级验证逻辑：将复杂合规规则拆解为细粒度子项分别校验，再融合得到全局连续评分，替代传统二分类审核，降低漏判/误判率

  - 推荐系统多模态物料打分场景可借鉴解耦RL训练策略：先优化子规则维度的二分类判断能力，再对齐全局评分，用局部精准反馈降低全局打分模型的训练难度

  - 生成式推荐内容合规校验场景，若有基准物料可用，优先选择成对验证范式（对比候选与基准内容），可获得比单点打分更准确的校验结果'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
传统生成式视觉验证器仅输出二分类判断，在多模态组合规则场景下鲁棒性差、反馈粒度粗，无法支撑规则约束下的生成式世界建模与Agent能力迭代。
### 方法关键点
1. 提出分级验证器OmniVerifier-C1，自动将复杂prompt/环境规则拆解为细粒度子项，输出各子项校验结果+全局连续评分，反馈可解释性更强；
2. 采用解耦RL训练策略，联合优化子问题级二分类判断与全局对齐打分，用局部精准反馈支撑全局可靠评分；
3. 存在ground truth图像时，优先采用成对验证范式，校验准确率优于单点打分方案。
### 关键结果
文生图场景下，单点分级验证器效果显著优于传统二分类验证器；迷宫、数独等结构化世界建模任务中，成对验证范式有效性得到实证，可支撑结构化世界建模Agent落地。
