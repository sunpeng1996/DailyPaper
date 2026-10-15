---
title: 'Revisiting Generative vs. Dense Retrieval: A Static Value Prior Reverses the
  Gap'
title_zh: 重审生成式检索与稠密检索：静态价值先验可逆转性能差距
authors:
- Renbo Tu
- Yang Liu
- Shuying Sun
affiliations:
- Shopify
- University of Toronto
arxiv_id: '2610.19065'
url: https://arxiv.org/abs/2610.19065
pdf_url: https://arxiv.org/pdf/2610.19065
published: '2026-10-13'
collected: '2026-10-15'
category: GenRec
direction: 生成式推荐 · 检索方案对比
tags:
- Generative Retrieval
- Dense Retrieval
- Semantic ID
- Sequential Recommendation
- Popularity Bias
one_liner: 为稠密检索结果增加静态物品价值先验重排，即可全面超过生成式检索效果
practical_value: '- 暂时不用盲目上大参数量GR方案，现有DR加静态价值重排（融合流行度、评分、品牌权重）就能达到更好效果，大幅节省推理成本

  - 推荐评估不能只看精确召回，要补充最佳相关商品价值、全列表价值加权指标（如vNDCG），更贴合电商营收类业务目标

  - GR的价值优势本质来自对流行高价值商品的偏好，若业务要弱化马太效应、优化长尾商品曝光，优先选DR加可解释的价值先验更可控

  - 冷启动召回场景下DR效果远优于GR，冷品占比高的品类无需尝试GR方案'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
电商场景下生成式检索（GR）被宣传为稠密检索（DR）的下一代候选生成方案，但工业界缺乏控制变量的公平对比，现有仅关注精确目标召回的评估指标未兼顾商品商业价值，无法判断GR的优势是否真实适配业务需求。

### 方法关键点
- 对齐对比框架：基于LIGER架构，GR和DR使用完全相同的交互数据、商品库、T5编码器，仅检索输出逻辑不同：GR通过约束解码输出Semantic ID，DR通过编码器输出的用户向量与物品向量余弦相似度排序
- 电商适配指标设计：新增最佳相关商品价值（BV）衡量返回列表中最高价值相关品的表现，新增vNDCG衡量全列表的价值加权排序效果，补足传统召回指标的缺陷
- 零训练成本优化：静态价值先验由商品log流行度、评分Wilson下界、品牌影响力三个静态属性加权得到，无需重新训练DR模型，仅对召回top200结果做一次重排即可生效

### 关键实验结果
- 公开数据集：在Amazon Toys 2014、2023（商品库为前者13.6倍）上，DR加先验后BV@50反超GR，2014年相对提升0.043、2023年提升0.022；vNDCG@50分别比GR高11.6%、9.4%，Recall@50始终高于GR
- 工业数据集：14B参数的GR效果远低于参数仅为其1/47的DR编码器，DR加先验后NDCG@50再提升11.8%

### 最值得记住的结论
现阶段电商候选生成场景下，GR并没有不可替代的优势，其价值领先本质来自对流行高价值商品的偏好，DR加简单的静态价值重排即可实现全面超越。
