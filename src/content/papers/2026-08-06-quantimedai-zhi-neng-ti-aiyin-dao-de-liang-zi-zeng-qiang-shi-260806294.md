---
title: 'QuanTiMedAI: Quantum-Enhanced Time-Series Model guided by Agentic AI for Cardiac
  Arrest Mortality Prediction'
title_zh: QuanTiMedAI：智能体AI引导的量子增强时序心脏骤停死亡率预测模型
authors:
- Mutasim Fuad Sarker
- Adiba Rahman Namira
- Wafa Binte Alam
- Md Adnan Arefeen
- Mahzabeen Emu
- Sumaiya Tabassum Nimi
affiliations:
- North South University, Dhaka, Bangladesh
- Memorial University, St. John’s, NL, Canada
arxiv_id: '2608.06294'
url: https://arxiv.org/abs/2608.06294
pdf_url: https://arxiv.org/pdf/2608.06294
published: '2026-08-06'
collected: '2026-08-09'
category: Agent
direction: Agent 引导的时序预测模型优化
tags:
- Agentic LLM
- Time Series Prediction
- Quantum ML
- Feature Selection
- Low-parameter Model
one_liner: 提出Agent LLM特征挖掘结合小参数量子循环网络的时序预测框架，效果超同类SOTA
practical_value: '- 可复用Agentic LLM做领域特征挖掘的思路，替代传统人工/规则特征筛选，落地到电商用户行为时序预测、商品动销预测场景，降低特征工程成本

  - 小参数非线性增强时序模型的架构思路可迁移到低资源端侧推荐/预测场景，用极少参数实现优于传统RNN的效果，降低推理延迟

  - Agent+轻量化时序模型的两阶段架构可复用在搜索广告的用户行为序列建模、冷启动流量预测等任务，平衡效果与算力消耗'
score: 4
source: arxiv-cs.AI
depth: abstract
---

### 动机
ICU心脏骤停死亡率预测现有方案依赖入院早期静态特征，忽略患者住院期间生理指标的时序演化规律，传统时序模型参数规模大、特征筛选高度依赖人工领域经验。
### 方法关键点
采用两阶段架构：第一阶段用Agentic LLM做临床知识引导的自动化特征挖掘，替代传统特征选择方法；第二阶段采用轻量化量子循环网络做时序感知的死亡率预测，通过非线性特征增强提升效果，同时严格控制参数量。
### 关键结果
在MIMIC-IV心脏骤停患者队列上AUROC达0.852，仅用605个参数，比当前SOTA基线提升约2.9%，效果超越传统循环网络且参数量大幅降低，各模块贡献经消融实验验证。
