---
title: Learning to Rank Explanations for Recommendation with Language Models
title_zh: 基于大语言模型的推荐解释语句排序方法
authors:
- Ben Kabongo
- Vincent Guigue
affiliations:
- Sorbonne University
- CNRS
- ISIR
- AgroParisTech
- UMR MIA Paris-Saclay
arxiv_id: '2611.04775'
url: https://arxiv.org/abs/2611.04775
pdf_url: https://arxiv.org/pdf/2611.04775
published: '2026-11-03'
collected: '2026-11-04'
category: RecSys
direction: 可解释推荐 · 解释语句排序
tags:
- Explainable Recommendation
- Statement Ranking
- Contrastive Learning
- Dual Encoder
- LoRA
one_liner: 提出全文本驱动的双编码器LMStaR框架，实现推荐场景下个性化解释语句的精准排序
practical_value: '- 电商推荐的可解释模块可优先采用「评论提取候选解释+排序」的方案，替代生成式解释，完全避免幻觉，且支持用NDCG等标准排序指标做离线评估，上线风险更低

  - 可直接复用LMStaR的双编码器架构：查询编码器编码用户最近交互历史+目标商品元数据，语句编码器预编码所有候选解释，用LoRA微调，比全量微调NDCG@5高0.84~2.66个百分点，训练成本低效果好

  - 用户交互历史仅需取最近4条就能拿到大部分收益，无需复杂的历史筛选策略，既节省token消耗，又能保证排序效果

  - 训练好的模型支持跨域迁移，无需目标域数据微调就能超过零-shot模型和传统ID类排序基线，适合冷启动类目快速上线解释功能'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
当前可解释推荐的生成式方案易产生无事实依据的幻觉，评估难度大；传统ID类解释排序方法对语义信息利用不足，效果往往不如用户历史流行度基线，无法满足个性化解释需求。
### 方法关键点
- 采用双编码器架构：查询编码器输入「检索指令+用户历史交互+目标商品元数据」，语句编码器独立编码候选解释，映射到共享嵌入空间，用余弦相似度计算相关性
- 采用多正例InfoNCE对比损失训练，将用户-商品对对应的真实评论提取的解释作为正例，同商品其他解释作为负例，无需依赖用户/商品ID特征
- 采用LoRA做参数高效微调，效果优于全量微调
### 关键结果
在Amazon Beauty、Amazon Toys、Yelp三个公开数据集上对比15个基线：NDCG@1全领域领先，比SOTA CLER高3.5、8.25、1.06个百分点（相对提升11.8%~65.9%）；亚马逊两个数据集NDCG@5也领先13.4%~34.2%；微调后的小模型效果优于大零-shot模型，跨域无需微调即可超过传统基线。
### 核心结论
做可解释推荐时，优先选择真实评论提取的候选解释排序方案，比生成式方案更可控可评估，纯文本双编码器+LoRA微调即可实现远超传统ID类方法的效果
