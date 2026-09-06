---
title: 'Translation as a Decision Space: A Multi-Agent Perspective on Low-Resource
  Dialect Generation'
title_zh: 将翻译视为决策空间：低资源方言生成的多智能体视角
authors:
- Hasan Alkhder
- Mohammad Abboush
- Igor Tchappi
- Ahmet Zengin
- Amro Najjar
affiliations:
- Sakarya University
arxiv_id: '2609.04048'
url: https://arxiv.org/abs/2609.04048
pdf_url: https://arxiv.org/pdf/2609.04048
published: '2026-09-03'
collected: '2026-09-06'
category: MultiAgent
direction: 多智能体 · 低资源生成可解释性优化
tags:
- Multi-Agent
- Low-Resource NLP
- Dialect Translation
- Decision Space
- Interpretability
one_liner: 将翻译建模为多智能体探索的决策空间，为低资源方言生成提供可解释优化方案
practical_value: '- 低资源场景可复用「共享主干+多路径智能体」架构，比如小语种电商文案生成、方言用户query理解，无需独立训练多套大模型，大幅降低算力成本

  - 多智能体输出分歧无需判定为错误，可作为决策空间特征信号，用于推荐系统多候选结果的多样性控制、排序逻辑优化

  - 轻量微调做领域/方言适配的方案可直接迁移，比如小语种/垂类电商的商品标题翻译生成，仅需千级样本即可提升领域契合度，远低于全量微调成本'
score: 4
source: arxiv-cs.CL
depth: abstract
---

### 动机
传统神经机器翻译默认单输出机制会隐藏多语言解码中的可选决策路径，在低资源方言场景下，多种语义合法的输出在方言真实性、语体、结构稳定性上差异极大，单路径方案既难满足方言适配要求，也缺乏可解释性。
### 方法关键点
将翻译重构为可被多智能体探索的结构化决策空间，三类翻译智能体共享同一多语言主干，分别采用零-shot直接翻译、轻量微调的方言稳定翻译、英文枢轴翻译三种路径，将智能体间的输出分歧视为可解释的行为信号而非错误，不用传统指标做单一最优筛选。
### 关键结果数字
在土耳其-叙利亚阿拉伯语翻译任务上，轻量稳定微调将方言标记使用率从0.2266提升至0.4988，接近翻倍，同时显著降低结构不稳定性；枢轴翻译会引入标准化压力和可量化的压缩效应，零-shot翻译的决策方差最高。
