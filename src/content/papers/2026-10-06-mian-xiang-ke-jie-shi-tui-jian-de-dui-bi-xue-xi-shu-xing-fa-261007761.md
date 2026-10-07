---
title: Contrastive Learning for Aspect Representation towards Explainable Recommendation
title_zh: 面向可解释推荐的对比学习属性表征方法
authors:
- Emrul Hasan
- Chen Ding
affiliations:
- Toronto Metropolitan University
arxiv_id: '2610.07761'
url: https://arxiv.org/abs/2610.07761
pdf_url: https://arxiv.org/pdf/2610.07761
published: '2026-10-06'
collected: '2026-10-07'
category: GenRec
direction: 生成式可解释推荐 · 对比学习属性表征
tags:
- Contrastive Learning
- Explainable Recommendation
- Aspect Representation
- Review-based Recommendation
- Multi-task Learning
one_liner: 融合对比学习属性表征与ID特征，同时提升可解释推荐的准确率与解释生成质量
practical_value: '- 业务中做可解释推荐时，可跳过外部属性抽取工具，采用「预定义领域属性+对比学习」方案直接从用户评论中学习属性表征，大幅降低跨品类适配成本

  - 多任务调参可参考论文经验：解释生成、对比学习任务权重设为1.0，评分预测权重设为0.5，在保证推荐准确率的前提下优先提升解释的个性化与合理性

  - 多源特征融合场景可复用门控机制，自动控制ID类协同特征与文本类语义特征的贡献占比，比直接拼接效果更稳定

  - 新用户/新商品冷启动场景下，加入评论属性表征可显著降低评分预测误差，比纯ID特征方案的MAE最高降低35%'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
传统可解释推荐存在两大痛点：一是依赖ID类协同特征，与自然语言语义空间对齐度低，导致生成的解释个性化不足、可读性差；二是多数属性感知方案依赖外部属性抽取工具，跨域适配成本高，且ID特征在数据稀疏场景下表征能力弱，无法同时兼顾推荐准确率与解释质量。
### 方法关键点
- 提出CLARER多任务框架，由三大模块组成：MLP建模用户/物品ID的评分特征，Transformer编码器+对比学习学习评论的属性感知表征，Transformer解码器生成自然语言解释
- 预定义各领域属性类目（如餐饮类的服务、口味、环境等），用Sentence-BERT得到属性嵌入，以评论为正样本、随机无关属性为负样本做对比学习，得到与属性对齐的评论语义表征
- 采用门控机制融合ID评分特征与属性表征，多任务联合优化：MSE损失用于评分预测，交叉熵损失用于解释生成，对比损失用于属性表征学习，三个任务按加权系数共同训练
### 关键实验
在Yelp餐饮、亚马逊电影、TripAdvisor酒店三个公开数据集上与SERMON、PETER等SOTA可解释推荐模型对比：评分预测任务中，Yelp数据集RMSE降低29%、MAE降低35%，亚马逊数据集RMSE降19%、MAE降18%，TripAdvisor数据集RMSE降14%、MAE降16%；解释生成任务中Yelp数据集ROUGE-2提升近4倍，多数指标领先基线。
### 值得记住的一句话
无需依赖外部属性工具的对比学习属性表征，可同时提升推荐准确率与解释生成质量，跨域适配性更强。
