---
title: Attribute-Conditioned Multimodal Slot Factorization for Controllable Fashion
  Retrieval
title_zh: 面向可控时尚检索的属性感知多模态槽分解方法
authors:
- Najmeh Forouzandehmehr
- Topojoy Biswas
- Evren Korpeoglu
- Kannan Achan
affiliations:
- Walmart Global Tech
arxiv_id: '2608.12570'
url: https://arxiv.org/abs/2608.12570
pdf_url: https://arxiv.org/pdf/2608.12570
published: '2026-08-12'
collected: '2026-08-14'
category: RecSys
direction: 可控多模态检索 · 语义ID槽分解
tags:
- Multimodal Retrieval
- Controllable RecSys
- Slot Factorization
- Semantic ID
- Vector Quantization
one_liner: 提出MM-slotgate多模态槽编码器，为不同属性自动分配文本/图像权重，提升可控时尚检索约束满足率与可干预性
practical_value: '- 做时尚/多模态商品检索时，可按属性语义差异分配文本/图像权重：视觉属性（颜色、花纹）优先用图像信号，分类属性（品类、受众）优先用文本/类目信号，能大幅提升多约束检索准确率

  - 可复用带缺失模态fallback的槽分解架构：无图商品自动降级为文本编码，保证全品类覆盖；同时独立命名的属性槽支持查询时动态加权、定向干预，满足用户自定义筛选需求

  - 量化槽编码可直接接入生成式推荐/Agent系统：独立语义的槽编码可直接作为Semantic ID的组成部分，支持LLM生成时定向修改特定属性，无需重新生成全量ID'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有时尚检索采用的单块嵌入会混合多属性信号，查询时无法定向控制特定属性的匹配优先级；现有语义ID方法多为物品级隐式离散编码，没有公开可独立控制的命名属性槽，难以同时满足多约束检索准确率和定向干预需求。

### 方法关键点
- 基于Fashion-CLIP提取商品文本和图像嵌入，为颜色、花纹、品类、受众4个命名属性槽分别设置可学习的文本/图像权重门控，无需模态监督即可自动匹配最优权重分配
- 设计无图 fallback 机制：无图商品自动使用纯文本编码，保证全品类覆盖
- 每个槽独立做向量量化生成专属离散编码，训练损失结合属性对齐损失、VQ承诺损失和槽正交正则，避免槽坍缩
- 检索时采用「槽加权余弦相似度+槽匹配logit」的混合打分，支持定向提升特定约束的权重

### 关键实验结果
在H&M 5万商品数据集上测试：
- 宏观ConstraintSatisfied@10达0.7566，比等权多模态 fusion 高5.9%相对提升，比纯fCLIP文本检索高59.1%相对提升
- 颜色属性的CS@10从纯文本的0.321提升到0.889，绝对提升0.568，对应颜色槽自动分配57.4%权重给图像信号
- 量化槽定向干预颜色的Hit@10提升达15.3倍，远高于纯文本方案的1.5倍，且对其他属性匹配率影响极小

### 核心结论
不同属性的最优模态权重存在天然差异，将嵌入按语义分解为可独立控制的命名槽，是同时提升检索准确率和可控性的有效路径
