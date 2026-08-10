---
title: People Are Not Just Their Countries. Disentangling Social Determinants of LLM
  Value Alignment Across Europe
title_zh: 拆解欧洲LLM价值对齐的社会决定因素：国别之外的群体差异
authors:
- Maria-Louisa Wightman
- Guillaume Bied
- Tijl De Bie
affiliations:
- Ghent University
arxiv_id: '2608.07367'
url: https://arxiv.org/abs/2608.07367
pdf_url: https://arxiv.org/pdf/2608.07367
published: '2026-08-07'
collected: '2026-08-10'
category: LLM
direction: LLM价值对齐 · 群体差异分析
tags:
- LLM Alignment
- Socio-demographic Bias
- Value Alignment
- Cross-cultural Evaluation
- Fairness
one_liner: 基于欧洲社会调查量化10款商用LLM跨群体价值对齐差异，明确国别与社会人口特征的互补作用
practical_value: '- 跨境电商LLM导购、本地化推荐文案生成场景，不能仅按国家做对齐适配，需叠加教育、收入、宗教等1-3个核心社会人口标签做个性化对齐，降低价值观冲突导致的用户流失

  - 做LLM价值对齐评估时可复用欧洲社会调查（ESS）数据集，替代已被多数LLM训练数据污染的世界价值观调查（WVS），提升评估结果可信度

  - 跨群体用户偏好建模可借鉴本文逆倾向加权（IPW）方法校准不同群体的样本分布偏差，避免模型过度拟合高流量高收入群体的偏好

  - 面向欧洲市场的LLM应用优化可优先对齐低对齐度群体：穆斯林、低收入、低教育程度、东欧国家用户，这类群体的体验提升空间最大'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
现有LLM价值对齐研究多以国别/文化为核心分析单元，忽略同一国家内部社会人口结构带来的对齐差异；且常用的世界价值观调查（WVS）已被广泛纳入LLM训练数据，存在评估污染问题，结果可信度不足。
### 方法关键点
- 数据：采用2023-2024年欧洲社会调查（ESS）第11波数据，覆盖30个国家共5万余名受访者，纳入15项社会人口特征、47道价值观相关问题
- 评估设计：选取10款来自中美欧的主流商用LLM，每道题重复调用20次取多数投票作为模型输出，基于Likert量表答案的归一化距离计算0-1区间的对齐分数
- 分析方法：用逆倾向加权（IPW）校准不同国家的人口结构差异，通过线性回归+梯度提升树分解国别、社会人口特征对对齐度方差的解释率
### 关键结果
- 10款LLM整体对齐度区间为0.581~0.745，群体间最大对齐差值达0.0896：高收入、高教育、新教徒、西欧/北欧群体对齐度显著更高，穆斯林、低收入、东欧国家群体对齐度最低
- 国别单独解释的对齐度方差与15项社会人口特征的总解释力相当，IPW校准后国别差异仅缩小不足10%，二者联合最高可解释42.8%的对齐度方差
- 针对抽象价值观的问题集，国别的解释力大幅下降，社会人口特征权重更高
### 核心结论
LLM对高社会经济地位群体的天然价值对齐偏向，会在大规模落地时放大现有社会不平等，面向公众的LLM应用必须叠加多维度群体公平性校准。
