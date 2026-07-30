---
title: 'Learning from the Future: Privileged Self-Distillation for Sequential Recommendation'
title_zh: 面向序列推荐的特权自蒸馏框架：从未来交互中学习
authors:
- Jiakai Tang
- Yang Zhang
- See-Kiong Ng
- Xu Chen
- Wen Chen
- Jian Wu
- Han Zhu
affiliations:
- 中国人民大学高瓴人工智能学院
- 新加坡国立大学
- 阿里巴巴集团
arxiv_id: '2607.27055'
url: https://arxiv.org/abs/2607.27055
pdf_url: https://arxiv.org/pdf/2607.27055
published: '2026-07-29'
collected: '2026-07-30'
category: RecSys
direction: 序列推荐 · 自蒸馏训练优化
tags:
- Sequential Recommendation
- Self-Distillation
- Privileged Information
- Transformer
- Knowledge Distillation
one_liner: 基于双注意力掩码的序列推荐特权自蒸馏，利用训练可见的未来交互实现无额外推理开销提效
practical_value: '- 训练阶段可直接复用日志中已有的用户未来交互作为特权监督信息，无需额外引入特征，适配所有Transformer类序列推荐backbone，推理侧零改动无额外开销

  - 双掩码自蒸馏架构无需单独预训练教师模型，单阶段端到端训练即可落地，工程实现复杂度低，可直接嵌入现有训练pipeline

  - advantage-reachability动态门控、EMA动量教师两个trick可单独复用，适配其他自蒸馏、知识蒸馏场景，缓解训练不稳定、负迁移问题'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有序列推荐为匹配推理时的因果约束，仅用用户历史前缀交互与one-hot下一跳标签训练，监督信息密度极低，日志中大量已记录的用户未来交互被完全浪费；直接采用双向掩码训练（如BERT4Rec）会存在训练推理不一致问题，效果反而普遍弱于单向因果模型，亟需一种既能利用未来交互丰富监督信号、又不破坏推理因果性的低成本训练方案。
### 方法关键点
- 同一Transformer backbone通过双注意力掩码生成双视图：特权教师用双向掩码同时读取前缀+未来交互，学生用因果掩码仅读取前缀，参数完全共享，无额外参数开销
- 优势可达门：按批次计算师生分布KL散度的百分位阈值，仅蒸馏散度低于阈值的可迁移信号，过滤仅依赖未来信息、因果学生无法复现的不可迁移信号
- 动量平均教师：通过参数EMA生成稳定的教师分布，避免自蒸馏的自反馈噪声，训练全程无需单独预训练教师
- 单阶段端到端训练，损失为教师的交叉熵损失+学生的蒸馏损失，推理仅输出学生视图结果，无额外计算开销
### 关键结果
在Amazon Video Games、CDs&Vinyl、Yelp三个公开数据集上，适配SASRec、BERT4Rec、UniSRec三类主流序列backbone，对比RD、S4Rec等7种基线方法，平均比原生backbone提升19.8%，比各场景最优基线平均提升9.9%；其中在BERT4Rec场景增益最高，NDCG@10在CDs&Vinyl数据集上提升达75.4%。
> 值得记住：训练时可用、推理时不可用的未来交互是低成本高价值的特权信息，通过自蒸馏可安全转化为因果模型的性能增益，无需任何推理侧改动
