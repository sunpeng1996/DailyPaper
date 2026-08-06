---
title: Equitable System-Prompt Selection via Constrained Mixed-Strategy GroupDRO
title_zh: 基于约束混合策略GroupDRO的公平系统提示词选择方法
authors:
- Mengyu Xu
- Qiaoxin Yang
- Zhihan Liu
- Ruiyao Xu
- Zachary Liu
- Kezhen Chen
- Chongyang Gao
affiliations:
- The University of Chicago
- SynAI Technologies, Inc.
- Northwestern University
- Dartmouth College
- Analogy AI, Inc.
arxiv_id: '2608.04339'
url: https://arxiv.org/abs/2608.04339
pdf_url: https://arxiv.org/pdf/2608.04339
published: '2026-08-05'
collected: '2026-08-06'
category: LLM
direction: LLM公平性 · 系统提示词选择优化
tags:
- System Prompt
- GroupDRO
- Fairness
- LLM
- Prompt Selection
one_liner: 为现有提示词池分配权重，兼顾最差分组回答质量与整体平均效果
practical_value: '- 搭建电商/金融/医疗领域的LLM客服、导购Agent时，无需追求单个最优system prompt，可构建包含5-35个不同导向prompt的中等规模池，通过该方法计算权重按比例采样使用，在几乎不降低平均回答质量的前提下，提升低领域素养、小语种等弱势用户群体的回答准确性

  - 搜索Query理解、问答兜底场景可直接复用该框架：先将用户query按表述复杂度、语言、人群标签分组，离线计算各prompt在各分组的效果，求解线性规划得到权重即可上线，无需额外训练模型，落地成本极低

  - 推荐系统的个性化生成文案场景可迁移思路：将不同风格、人群适配的prompt建池，加入CTR/CVR等业务指标的平均约束，用类似的约束GroupDRO方法分配权重，兼顾整体业务效果和小众人群的文案适配度，缩小人群间的效果gap'
score: 8
source: arxiv-stat.ML
depth: full_pdf
---

### 动机
LLM已广泛应用于医疗、消费金融等高风险信息查询场景，但语义完全相同的问题因用户表述差异（比如低领域素养的口语化提问、不同语言、提问框架），得到的回答质量差距极大。现有system prompt优化均面向平均效果，会导致低健康/金融素养等弱势用户群体拿到的回答质量更差，而这类用户恰恰最依赖准确易懂的回答，亟需在几乎不牺牲整体平均回答质量的前提下，提升最差分组的回答效果。

### 方法关键点
- 解耦prompt生成与选择环节，问题定义为从现有prompt池分配权重，而非生成新的prompt文本，离线预先计算每个prompt在各评价分组（按语言、领域素养、资源约束、提问方式等划分）和各评估指标（信息稀释度、完整性、可操作性）下的损失矩阵
- 提出约束混合策略GroupDRO，通过线性规划求解prompt的权重分布，优化目标为最小化所有指标-分组对的最坏损失，同时加入硬约束：整体平均损失不超过平均最优单prompt的(1+ε)倍（实验取ε=0.005，即最多高0.5%）
- 输出的最优权重可直接诊断prompt池的互补性：若权重分散在多个prompt上，说明不同prompt适配不同的分组/评估指标

### 关键结果
- 实验覆盖5款主流LLM，在双语医疗基准MIRA、自建双语消费金融基准（60个种子问题、24个分组、1440个问题变体）上测试
- 对比基线包括无prompt、平均最优单prompt、纯GroupDRO单prompt选择、Prompt Risk Control（PRC）
- 相比无prompt基线，整体平均损失降低13.1%，最差25%分组平均损失降低13.2%，最坏单组损失降低13.7%；所有10个模型-领域设置下，最差25%分组的表现均优于所有单prompt选择方法，且整体平均质量与平均最优单prompt几乎无差异

### 核心结论
不需要费力优化单个最优prompt，中等规模的互补prompt池加简单的带约束权重分配，就能在几乎不损失平均效果的前提下，大幅提升弱势分组的回答质量。
