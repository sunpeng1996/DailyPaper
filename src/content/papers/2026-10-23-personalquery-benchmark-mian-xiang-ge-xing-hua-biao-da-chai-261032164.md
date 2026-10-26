---
title: PersonalQuery-Benchmark:Evaluating Retrieval Robustness to Personalized User
  Expression Differences
title_zh: PersonalQuery-Benchmark：面向个性化表达差异的检索鲁棒性评测基准
authors:
- Wenyu Liang
- Hongzhi Yin
- Tongtong Wu
- Fan Liu
- Kexin Dai
- Weiqing Wang
affiliations:
- Monash University, Australia
- University of Queensland, Australia
- Southeast University, China
arxiv_id: '2610.32164'
url: https://arxiv.org/abs/2610.32164
pdf_url: https://arxiv.org/pdf/2610.32164
published: '2026-10-23'
collected: '2026-10-26'
category: QueryRec
direction: Query检索鲁棒性 · 个性化表达差异评测
tags:
- Personalized Retrieval
- Robustness Evaluation
- Query Benchmark
- User Expression Modeling
- E-commerce Search
one_liner: 构建覆盖3类电商域共6516条查询的基准，可评测检索系统对用户个性化表达差异的鲁棒性
practical_value: '- 优化电商搜索query理解模块时，可复用该研究的用户个性化句法/拼写错误建模方法，针对高活用户构建专属表达画像，做自适应query改写与纠错，降低同义不同表达的召回排序波动

  - 评估内部检索/排序模型鲁棒性时，可借鉴其「固定核心语义+仅改变表达形式」的对照评测范式，避免语义偏差干扰鲁棒性评估结论

  - 构造检索模型训练增强数据时，可复用其基于用户历史表达生成个性化query变体的方法，提升模型对不同用户表达习惯的泛化能力'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有个性化检索系统大多仅建模用户需求差异，忽略相同需求下不同用户的表达差异（句法结构、拼写习惯等），且现有公开数据集缺乏稳定用户标识、长期表达历史和意图匹配的对照query，无法系统性评估检索系统对这类表达差异的鲁棒性，导致很多模型表面效果优异，但对真实用户的个性化表达适应性不足。
### 方法关键点
- 定义两类个性化表达维度：个性化句法表达（用户的句子组织、修饰结构偏好）、个性化拼写错误（用户的长期拼写错误类型、频率偏好）
- 基于亚马逊用户历史评论，通过同产品监督对比学习学习用户句法表示，拟合低秩加对角高斯分布建模用户句法特征的分布范围
- 采用GECToR+ERRANT工具抽取用户历史拼写错误，构建用户专属的上下文相关错误分布
- 控制query核心检索语义完全一致，生成符合用户表达习惯的对照query对，保证语义相似度≥0.9，仅保留表达形式差异
### 关键实验结果
基准覆盖亚马逊3个商品域（乐器、视频游戏、母婴）共6516条query实例，评测5类主流检索架构（词法、稀疏、稠密、晚交互、混合）+2个LLM排序模型。结果显示：仅句法差异就会导致最高52.2%的Flip@1（同意图不同query的Top1命中结果不一致），个性化拼写错误会带来最高8%的MRR下降，且模型整体检索效果与对表达差异的鲁棒性无正相关。

**最值得记住的结论**：相同检索需求下，用户的个性化表达差异会显著影响检索排序效果，高整体效果的检索模型不一定具备更强的表达鲁棒性
