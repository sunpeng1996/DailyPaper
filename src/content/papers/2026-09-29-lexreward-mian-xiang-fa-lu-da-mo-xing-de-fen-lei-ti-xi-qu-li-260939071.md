---
title: 'LexReward: A Taxonomy-Driven Reward Framework for Legal Language Models'
title_zh: LexReward：面向法律大模型的分类体系驱动奖励框架
authors:
- Yida Cai
- Xin Dai
- Bingxiang He
- Huiyuan Xie
- Yuxiao Ye
- Zhenghao Liu
- Yang Bai
- Zhiyuan Liu
affiliations:
- Peking University
- Northeastern University
- Tsinghua University
arxiv_id: '2609.39071'
url: https://arxiv.org/abs/2609.39071
pdf_url: https://arxiv.org/pdf/2609.39071
published: '2026-09-29'
collected: '2026-10-05'
category: LLM
direction: 大模型领域对齐 · 多维度奖励建模
tags:
- Reward Modeling
- DPO
- LLM Alignment
- Domain LLM
- RLHF
one_liner: 提出覆盖风格、要素、推理链三维度的分类驱动法律大模型奖励框架，支持DPO与RL优化
practical_value: '- 业务领域Agent对齐时可复用多维度拆分奖励的思路，例如电商客服Agent可拆分话术合规、信息准确性、推理逻辑三个独立维度设计奖励规则，替代粗粒度整体打分，大幅提升对齐的可解释性与针对性

  - 分维度生成的 pairwise 偏好数据可直接用于DPO训练，无需构造参考回答，适合标注资源有限、无标准参考答案的业务场景（如定制化商品咨询、售后纠纷处理等）

  - 分维度训练的奖励模型可定向优化对应维度的模型表现，无跨维度负干扰，适合业务分阶段迭代体验的需求（例如先优化客服话术合规性，再定向优化问题解决率）'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有大模型奖励方法多依赖粗粒度整体判断，领域适配性与可解释性差，无法满足法律场景应答需同时覆盖结论正确、表述合规、推理逻辑完整等多维度质量要求。
### 方法关键点
1. 构建三维度法律应答质量分类体系：Style（词汇句法合规性）、Element（法律主体/事实/法条引用准确性）、Chain（推理链的顺序、完整性、正确性、无冗余）
2. 为每个维度定义明确的评估规则与质量等级，生成的pairwise偏好数据可直接用于DPO训练与领域专属奖励模型LexRM训练
3. 分维度LexRM可单独用于RL优化对应维度的模型表现，推理阶段无需依赖参考回答
### 关键结果
基于规则的奖励可精准区分不同质量的法律应答；基于偏好数据的DPO训练可同步提升三个维度的表现；分维度LexRM做RL优化可定向提升对应维度的政策表现，无跨维度负向影响
