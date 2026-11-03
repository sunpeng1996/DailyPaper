---
title: Multicriteria Recommendation System by Leveraging Predefined, Implicit, and
  Undefined Criteria
title_zh: 融合预定义、隐式与未定义准则的多维度推荐系统
authors:
- Emrul Hasan
- Chen Ding
affiliations:
- Toronto Metropolitan University
arxiv_id: '2611.02040'
url: https://arxiv.org/abs/2611.02040
pdf_url: https://arxiv.org/pdf/2611.02040
published: '2026-11-01'
collected: '2026-11-03'
category: RecSys
direction: 多准则推荐 · 评论语义挖掘
tags:
- Multi-Criteria Recommendation
- Review-based Recommendation
- Semantic Clustering
- Collaborative Filtering
- Sentiment Analysis
one_liner: 通过语义聚类从用户评论提取隐式、未定义准则，结合预定义准则提升多维度推荐精度
practical_value: '- 评论拆分技巧：可按「. + 转折连词（but/while/however等）」拆分用户评论，避免单句包含多维度评价，提升维度对齐准确率

  - 维度对齐方案：电商场景可基于SBERT语义相似度匹配，将评论内容对齐到业务预定义评价维度（如物流/服务/商品质量），低于阈值的内容统一归为「其他维度」补充建模

  - 多源特征融合：可复用「预定义显式评分 + 评论挖掘隐式评分 + 新增维度评分」的融合架构，用DNN学习聚合权重，缓解单一数据源的信息缺失问题

  - 阈值调优经验：语义匹配阈值可在0.2-0.4区间调参，通常0.3左右能实现维度聚类的最优效果，可根据品类特性微调'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
传统多准则推荐仅依赖业务预定义的显式评分维度，无法覆盖用户在评论中自由表达的多元评价视角；纯评论驱动的推荐又忽略了用户提交的显式维度评分，两类方法均存在信息缺失，在数据稀疏场景下评分预测精度不足，难以细粒度捕捉用户偏好。

### 方法关键点
- 评论拆分：按句号+转折连词（but/while/however等）拆分评论为单维度子句，避免单句包含多维度评价
- 维度对齐：用SBERT生成子句与预定义维度的语义向量，通过余弦相似度匹配：相似度高于阈值的子句归为对应预定义维度的隐式评价，低于阈值的统一归为未定义维度
- 评分生成：对每个维度的子句集合做情感分析，输出隐式/未定义维度的评分，结合预定义显式评分构成输入特征
- 模型架构：融合MF与DNN的神经协同过滤模块预测缺失维度评分，再用DNN学习三类维度评分与整体评分的聚合关系，输出最终评分预测

### 关键实验
在TripAdvisor、Beer Advocate两个公开数据集上对比7个SOTA基线，核心结果：
- TripAdvisor数据集：MSE 0.3912、MAE 0.3721，较最优基线MRRRec分别下降3.08%、2.02%，F1达0.9553，提升0.93%
- Beer Advocate数据集：MSE 0.2921、MAE 0.3024，较最优基线分别下降3.65%、2.97%，F1达0.9255，提升1.95%
- 消融实验：同时引入三类维度的效果最优，仅用预定义维度的MSE比全维度高0.678%

### 核心结论
用户的真实偏好由预定义显式反馈、评论对齐到业务维度的隐式反馈、超出业务预设维度的额外反馈共同决定，三类信息缺一不可
