---
title: 'When Steering Shifts Discourse: Identifying and Intervening on Discourse-Level
  Changes due to Activation Steering in LLMs'
title_zh: 大语言模型激活转向引发的话语层面非预期偏移的识别与干预
authors:
- Shivam Adarsh
- Hetianyu Huang
- Lau Safin
- Maria Maistro
- Christina Lioma
affiliations:
- University of Copenhagen
arxiv_id: '2610.41661'
url: https://arxiv.org/abs/2610.41661
pdf_url: https://arxiv.org/pdf/2610.41661
published: '2026-10-30'
collected: '2026-11-02'
category: LLM
direction: LLM激活转向的副作用识别与修复
tags:
- ActivationSteering
- LLMAlignment
- InferenceControl
- DiscourseAnalysis
- SideEffectMitigation
one_liner: 识别15种激活转向导致的非预期话语偏移，提出双向量干预方案恢复78%偏移且保留93%预期转向效果
practical_value: '- 做Agent/LLM导购的行为控制时，可复用这套细粒度话语维度检测框架，避免Activation Steering导致回复话术风格偏移（比如原本要热情，结果转向后变生硬、逻辑缺失）

  - 激活转向叠加干预向量的架构可直接复用：针对业务关心的话术属性（比如正式度、证据支撑、推理深度）预训练对应维度向量，推理时和行为向量叠加注入，兼顾行为控制和输出质量

  - 干预强度β与转向强度α成比例缩放的设计可直接复用，避免固定强度导致的过校正或校正不足，降低调参成本

  - 用LLM judge做细粒度文本属性标注的流程（加人工校验一致性、多轮投票降噪）可迁移到电商文案质量评估、用户回复质检等场景'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
Activation Steering 是LLM推理阶段无需微调权重、修改提示即可控制行为、安全属性的轻量技术，但其引发的非预期输出变化仅用困惑度等粗粒度指标衡量，无法定位具体语义层面的偏移，也没有针对性修复方案，严重限制该技术在业务场景的落地可靠性。
### 方法关键点
- 先通过Open-Ended检测+人工归并得到26个候选话语维度，再经LLM judge多轮打分+人工一致性校验，筛选出15个存在中度及以上一致性的受影响维度，包括歧义、矛盾、正式度、推理深度、证据支撑等
- 采用Contrastive Activation Addition (CAA) 构建行为控制向量，针对每个受影响话语维度构建正负样本对比数据集，提取对应维度矫正向量
- 提出3种干预方案：同层叠加行为+矫正向量、不同层分别注入两类向量、将矫正向量正交于行为向量后叠加，矫正强度β与原转向强度α成比例缩放，避免过校正
### 关键实验
- 覆盖Llama-3.1-8B、Qwen3-8B、Gemma-2-9B 3个开源模型，11个行为控制数据集，共8284个样本
- 86%的（模型、数据集、维度）三元组存在统计显著的话语偏移，且偏移程度与困惑度相关性最高仅0.38，无法用困惑度替代检测
- 针对6个高频受影响维度的干预可恢复78%的非预期话语偏移，同时保留93%的预期转向行为，74%的干预后输出无明显质量缺陷
### 核心结论
Activation Steering的副作用远不止困惑度上升，而是会系统性改变输出的话语属性，针对具体维度的定向矫正可以在几乎不损失转向效果的前提下大幅提升输出质量。
