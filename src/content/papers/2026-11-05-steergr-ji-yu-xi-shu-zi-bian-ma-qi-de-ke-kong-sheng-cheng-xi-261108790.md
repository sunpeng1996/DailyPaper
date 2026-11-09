---
title: 'SteerGR: Steering Generative Recommendation via Sparse Autoencoders for Controllable
  Game Discovery'
title_zh: SteerGR：基于稀疏自编码器的可控生成式游戏推荐框架
authors:
- Sunkyung Lee
- Xiaokai Wei
- Da Long
- Hyunsik Jeon
- Jiajun Wu
- Rithwik Seth
- Jongwuk Lee
- Michelle Gong
- Gungor Polatkan
affiliations:
- Sungkyunkwan University
- Roblox Corporation
arxiv_id: '2611.08790'
url: https://arxiv.org/abs/2611.08790
pdf_url: https://arxiv.org/pdf/2611.08790
published: '2026-11-05'
collected: '2026-11-09'
category: GenRec
direction: 生成式推荐 · 可控性与SAE干预
tags:
- Generative Recommendation
- Sparse Autoencoder
- Controllable Recommendation
- LLM Grounding
- Semantic ID
one_liner: 将稀疏自编码器（SAE）应用于生成式推荐，无需重训即可实现文本概念级的推荐结果调控
practical_value: '- 对于已上线的生成式推荐模型，可通过新增SAE层+文本概念接地的方式实现可控调控，无需重新训练原有推荐模型，改造成本极低，适合快速上线平台管控、用户自定义偏好调整类需求

  - 特征选择阶段不要仅依赖特征与概念的关联度（如Cohen''s d），必须加一步小流量验证干预效果的环节，能让调控效果提升2-3倍，该trick可直接复用在所有SAE干预类业务场景

  - 干预强度α建议选3-4的区间，既能提升目标概念匹配用户的召回准确率（最高+6.2%），又不会让整体推荐准确率下降过多，平衡收益和用户体验

  - 文本概念接地时可直接用现成的文本嵌入模型计算相似度再做标准化，不需要人工给所有物品打标，适合SKU多、更新快的电商/内容/游戏场景'
score: 9
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
生成式推荐（GR）已逐步落地工业场景，但当前方案无法灵活支持平台侧的内容管控、用户侧的探索类需求（如用户明确想玩协作类游戏，但历史行为都是竞速类就无法有效推荐）。此前SAE干预方案主要应用在LLM领域，如何将文本定义的业务/用户需求和GR的内部特征关联、实现无需重训的可控调控是未解决的核心问题。

### 方法关键点
- 前置准备：先训练并冻结生成式推荐模型，再在其Transformer中间层的隐藏态上训练Top-K SAE，得到稀疏特征字典
- 三阶段流程：
  1. 概念定义与接地：用LLM生成跨品类的用户目标概念，用文本嵌入模型计算每个物品、每个用户的概念匹配分
  2. 特征发现与选择：先通过高低概念分用户组的特征激活差异（Cohen's d）筛选候选特征，再通过小流量验证选择干预后目标概念占比提升最高的特征作为调控靶点
  3. 稀疏特征干预：推理时对选中特征的激活值做放大/抑制，修改隐藏态后输入后续层，无需改动原模型参数

### 关键实验结果
基于Roblox真实游戏推荐数据集，分别在Atomic ID、Semantic ID两种工业生成式推荐模型上验证：
- 对比随机选特征、仅按关联度选特征的baseline，SteerGR放大特征后目标概念占比分别提升38.4%（Atomic ID）、11.5%（Semantic ID），是关联度选特征方案的2.6-3倍；抑制特征后目标占比分别下降25.6%、8.3%
- 干预强度α=3-4时，目标概念匹配用户的Recall@10最高提升6.2%，整体准确率下降控制在可接受范围

### 核心结论
SAE做生成式推荐调控的核心不是找和概念关联最强的特征，而是找干预后实际能改变推荐结果的特征。
