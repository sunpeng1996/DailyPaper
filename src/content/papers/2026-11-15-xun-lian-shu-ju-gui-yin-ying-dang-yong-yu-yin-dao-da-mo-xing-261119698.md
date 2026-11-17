---
title: Data Attribution Should Steer Pretraining
title_zh: 训练数据归因应当用于引导大模型预训练过程
authors:
- Glenn Matlin
- Chandreyi Chakraborty
- Mohammed Rehan Parwani
- Saehee Eom
- Anthony Wen-Ming Zang
- Akhil Theerthala
- Arjun Chatterjee
- Tejas Khandwekar
- Brandon Michaels
- Alvin Deng
affiliations:
- Georgia Institute of Technology
- MATS Program
- Georgia Tech AI Safety Initiative
- University of Illinois Urbana-Champaign
- EleutherAI
arxiv_id: '2611.19698'
url: https://arxiv.org/abs/2611.19698
pdf_url: https://arxiv.org/pdf/2611.19698
published: '2026-11-15'
collected: '2026-11-17'
category: LLM
direction: 大模型预训练 · 数据归因优化
tags:
- Data-Attribution
- Pre-Training
- Data-Curation
- Capability-Provenance
- LLM-Training
one_liner: 提出数据归因引导预训练的闭环框架，挖掘可复用的跨语料数据筛选准则
practical_value: '- 做电商/推荐场景垂直LLM预训练/持续训练时，可复用归因-决策闭环：先跑小模型归因定位对目标能力（如商品理解、话术生成）增益最高的数据属性，避免全量数据试错，降低训练成本

  - 垂直场景数据筛选不要只依赖静态质量分（如perplexity、人工优质标签），可结合归因结果召回静态分低但对特定任务增益高的样本，比如用户真实评价、客服对话等raw数据

  - 动态数据调度时直接复用归因挖掘的可迁移数据属性，而非单次训练的高影响样本列表，适配不同训练阶段的模型需求，如冷启动阶段补常识数据、后期补垂直场景数据'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有预训练数据筛选多依赖静态质量规则、人工标注或单次训练的影响力排序，要么无法适配不同训练阶段的模型动态需求，要么得到的样本排序仅能用于单次训练不可复用，且静态质量信号常与实际训练增益脱节，导致数据筛选效率低、资源浪费严重。
### 方法关键点
- 提出能力溯源框架，将数据归因目标从单次训练的样本排序转向挖掘可复用、可验证的数据属性，作为跨训练、跨语料的通用筛选准则
- 构建归因-决策闭环：依次完成能力观测→归因解释→假设验证→策略更新四个步骤，明确5类归因决策对应的证据要求，避免错误迁移归因结论
- 提出等成本评估准则：验证归因得到的筛选规则时，需将归因的计算/人力成本纳入总预算，与同等成本下的基线筛选方法做公平对比
### 已验证效果
已有公开实验显示，基于归因挖掘的细粒度token级毒内容过滤策略，可将LLM的隐式/显式毒性降低4~10倍，同时保持通用语言建模能力不下降；静态质量分类器、嵌入相似性等基线方法在125M~7B规模LLM的预训练数据筛选中，效果常劣于随机选择或数据模型方法。
### 核心结论
过去训练中影响最大的样本未必是未来训练最需要的样本，归因的核心价值在于挖掘背后的可复用规律，而非单次的样本排序。
