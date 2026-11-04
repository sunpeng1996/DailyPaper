---
title: 'Rethinking Next-Visit Diagnosis Prediction Beyond Aggregate Metrics: Retrieval--Memory
  Multi-Agent Adjudication'
title_zh: 超越聚合指标的次诊预测：检索-记忆多智能体裁决框架LONGINUS
authors:
- Heejoon Koo
affiliations:
- University of Illinois Urbana-Champaign
arxiv_id: '2611.03826'
url: https://arxiv.org/abs/2611.03826
pdf_url: https://arxiv.org/pdf/2611.03826
published: '2026-11-02'
collected: '2026-11-04'
category: MultiAgent
direction: 多智体协作 检索记忆融合决策
tags:
- MultiAgent
- RAG
- Memory Augmented LLM
- Evaluation Framework
- Ensemble Learning
one_liner: 提出检索-记忆多智能体裁决框架，兼顾次诊预测的聚合性能与细分场景效果
practical_value: '- 多源预测融合可复用「共识保留+分歧裁决」策略：先保留多路召回/多模型的共同预测结果，仅对差异候选做二次判断，大幅降低推理成本同时避免固定权重的融合偏差，适合电商推荐多路召回融合场景

  - 内部检索可复用多query设计：按候选和用户历史的关系（当前交互/历史出现/从未接触）拆分多路径检索，比单一全局检索更能覆盖长尾、复购类item，适配长周期用户行为的兴趣唤醒需求

  - 多模块融合时隐藏候选来源可规避固有偏置：裁决阶段不透露候选来自哪个召回/排序模块，仅基于内容判断，减少模型对单一来源的偏好，提升融合鲁棒性

  - 评估体系可借鉴多维度拆解逻辑：不要仅看全局AUC/召回率，按item的时序属性（新兴趣/复购/留存）、用户历史长度分层评估，更易定位模型的真实短板'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有次诊预测任务仅用聚合指标评估，掩盖了两类核心挑战：分布层面标签长尾、单次预测标签数不固定；时序层面诊断分为持续、新增、复现三类状态，且两类挑战都随患者历史长度变化，导致看似效果优异的基准（如直接复用上次诊断的规则方法）完全无法预测新增、复发病例，实际落地价值有限。

### 方法关键点
- 提出统一的维度拆解评估框架，同时覆盖聚合指标、标签分布、时序状态、用户历史长度四个维度，可迁移到各类序列预测任务
- 设计训练-free的LONGINUS多智能体框架：1）检索视图：按诊断历史状态拆分为当前、历史、未出现三类query做患者内部检索，用最佳秩去重合并结果生成预测；2）记忆视图：将全量就诊历史总结为结构化记忆卡（慢性病、复发病、风险因素等）生成预测；3）裁决模块：保留两个视图的共识预测，仅对差异候选做来源隐藏的裁决，避免对单一视图的偏置

### 关键结果数字
在MIMIC-III、MIMIC-IV两个医疗数据集，4个主流LLM backbone（Gemini、GPT-OSS、Llama 3.3等）验证下：1）LONGINUS在22/24个细分时序场景下取得最优F1，其中新增诊断F1最高比基线提升0.035，复现诊断F1最高提升0.028；2）聚合指标与现有最优基线持平，单用户预测最多仅需4次LLM调用。

**最值得记住的一句话**：全局聚合指标往往会奖励「偷懒」的基准方法（如直接复用用户上次交互结果），只有分层拆解评估才能找到模型的真实优化空间。
