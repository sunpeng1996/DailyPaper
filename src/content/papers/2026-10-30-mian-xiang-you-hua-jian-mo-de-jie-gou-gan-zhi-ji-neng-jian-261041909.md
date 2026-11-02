---
title: Structure-Aware Skill Retrieval and Arbitration for Optimization Modeling
title_zh: 面向优化建模的结构感知技能检索与仲裁框架
authors:
- Anran Liu
- Benzhao Hou
- Zongsheng Cao
- Daichao Wang
- Lang Chen
- Shitong Chen
affiliations:
- Shenzhen University
arxiv_id: '2610.41909'
url: https://arxiv.org/abs/2610.41909
pdf_url: https://arxiv.org/pdf/2610.41909
published: '2026-10-30'
collected: '2026-11-02'
category: Agent
direction: Agent 技能检索与路由优化
tags:
- Agent
- Skill Retrieval
- Structure Awareness
- Routing Arbitration
- RAG
one_liner: 提出ArchOR框架，通过结构感知检索与基线保留仲裁提升优化建模准确率
practical_value: '- 技能检索优化trick：给可复用技能/召回Item附加可扩展的结构化标签（如场景、约束、适用范围），先通过加权Jaccard做粗筛缩小候选集，再做语义重排，可大幅降低语义匹配带来的结构错配问题，适配RAG召回、技能库检索等场景。

  - 新模块工程落地方案：上线新检索/策略模块时不要直接替换稳定基线，设置基线保留仲裁规则，仅当新路线索（置信度、候选排名、执行有效性）足够强时才切换，可在引入新能力的同时避免基线效果回落，适合业务灰度迭代。

  - 存量向量库低开销优化：用低秩原型残差调整已有缓存的向量表征，无需重训编码器、无需重新灌库，即可让表征按结构类别聚类，提升同类型资源的检索召回率，适配存量向量检索系统的冷优化。

  - 可复用结论：单独优化检索侧的Hit@N、MRR指标不直接等价于端到端业务效果提升，必须结合路由策略、业务容错机制，避免召回结果结构符合但不符合隐含业务约束。'
score: 9
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
当前基于LLM的优化建模Agent普遍依赖实例级经验复用，受问题表层措辞干扰严重，经常检索到语义相似但核心结构不匹配的技能，直接替换原有检索逻辑又容易因技能库覆盖不全导致效果回落，急需兼顾结构匹配准确性和基线稳定性的技能路由方案。

### 方法关键点
- 完全复用已有OptSkills技能库和DeepSeek-V4.1-Flash backbone，仅修改检索路由层，无额外训练开销：
  1. **CARL表征优化**：用低秩原型残差调整缓存的技能向量，将向量向所属技能类别的质心偏移，提升同结构技能的表征相似度，参数仅为λ=0.35、残秩r=16；
  2. **S3R检索**：给每个技能附加可扩展的结构签名（包含问题类别、变量模式、约束族、求解器后端等属性），用加权Jaccard相似度做初筛，仅将TOP-K（K=8）候选送入LLM语义重排，大幅缩小检索范围；
  3. **基线保留仲裁**：仅当结构路线索满足「求解有效+基线置信度≤0.62/结构置信度更高/结构候选排名≥7」时才替换原有基线结果，否则保留基线输出。

### 关键实验
在5个优化建模基准（共1100条查询）上对比原OptSkills基线，ArchOR的Macro-Acc提升2.68pp，Micro-Acc提升1.64pp，共多答对18个查询；CARL单独将技能检索Hit@1从0.607提升到0.804，MRR从0.682提升到0.839；若直接替换原有检索逻辑无仲裁，效果反而比基线低1.91pp。

### 核心洞见
单独提升检索召回率不直接等价于端到端效果提升，稳定的基线仲裁机制是新检索模块落地的必要保障。
