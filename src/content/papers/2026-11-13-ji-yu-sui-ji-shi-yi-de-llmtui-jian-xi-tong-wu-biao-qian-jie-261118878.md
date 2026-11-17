---
title: 'Label-Free Detection of Structural Bias in LLM-Based Recommender Systems via
  Randomized Paraphrasing: The Case of Verbosity'
title_zh: 基于随机释义的LLM推荐系统无标签结构偏差检测：以冗长性为例
authors:
- Carlos Peláez-González
- David Herrera-Poyatos
- Francisco Herrera
- Andrés Herrera-Poyatos
affiliations:
- University of Granada, Spain
- Andalusian Research Institute in Data Science and Computational Intelligence (DaSCI)
arxiv_id: '2611.18878'
url: https://arxiv.org/abs/2611.18878
pdf_url: https://arxiv.org/pdf/2611.18878
published: '2026-11-13'
collected: '2026-11-17'
category: Eval
direction: LLM推荐系统 · 无标签结构偏差审计
tags:
- LLM4Rec
- Structural Bias
- Label-free Evaluation
- Verbosity Bias
- Paraphrasing
one_liner: 提出无标签框架审计LLM推荐系统结构偏差，证实9款主流模型均存在冗长性偏差
practical_value: '- 可直接复用该无标签审计框架，上线前/迭代后检测LLM推荐的结构偏差（冗长性、措辞、格式等），无需人工标注相关性数据，大幅降低评估成本

  - 针对已验证普遍存在的冗长性偏差，可从两方面优化：一是prompt中增加「忽略描述长度、仅按相关性推荐」的约束；二是平台规范商家商品描述长度范围，避免卖家恶意凑字数获取流量

  - 审计工程实现可参考成本优化方案：预生成的商品释义结果可复用给多版本模型、多轮prompt迭代测试，仅需新增LLM推荐调用即可完成新版本审计，1万条左右query即可覆盖大多数偏差检测需求

  - 统计分析方法可复用：用条件logit模型拆分相关性、表面特征的独立贡献，无需AB实验即可量化不同特征对推荐结果的影响权重'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
LLM推荐系统已广泛应用于电商对话购、语音购物等场景，其推荐结果理应仅由query-商品相关性决定，但实际易受商品描述长度等表面特征干扰。传统评估方法依赖人工标注相关性，成本高、迭代慢，且第三方卖家可能利用偏差优化描述而非提升商品质量，亟需无标签的自动化审计方案。

### 方法关键点
- 基于随机化实验设计：给商品随机分配不同释义模型改写描述，同时随机打乱候选在prompt中的位置，排除位置偏差、检索排序的干扰
- 四步统计pipeline：卡方检验判断是否存在偏差→条件logit模型拆分语义相关性和表面特征的独立贡献→估计特征影响方向→分析相关性和表面特征冲突时的决策逻辑
- 仅需黑盒访问部署的推荐系统，无需任何标注数据，支持多版本模型复用预生成的释义结果

### 关键结果
基于2万条电商查询、Amazon 2023 ML挑战赛商品数据集，测试5个系列共9款LLM推荐模型：所有9款模型均存在显著冗长性偏差，描述长度每提升1个标准差，被选中概率最高提升38%；相关性仍是推荐的第一驱动因素，但当长度和相关性冲突时，相关性带来的选择优势会降低50%以上；DeepSeek-R1蒸馏模型对长度最敏感，GPT-OSS系列对长度最不敏感。

### 核心结论
LLM推荐系统的表面特征偏差普遍存在，无标签审计可以在不依赖标注的前提下快速完成风险排查，是上线前必不可少的验证环节
