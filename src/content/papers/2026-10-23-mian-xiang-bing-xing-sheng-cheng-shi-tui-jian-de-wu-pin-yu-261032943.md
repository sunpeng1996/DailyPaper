---
title: Knowledge Distillation across Item and Code Spaces for Parallel Generative
  Recommendation
title_zh: 面向并行生成式推荐的物品与编码空间跨域知识蒸馏
authors:
- Yixuan Xu
- Hailin Liu
- Linxiang Peng
- Can Yang
affiliations:
- The Hong Kong University of Science and Technology
- University of Science and Technology of China
arxiv_id: '2610.32943'
url: https://arxiv.org/abs/2610.32943
pdf_url: https://arxiv.org/pdf/2610.32943
published: '2026-10-23'
collected: '2026-10-26'
category: GenRec
direction: 生成式推荐 · 跨空间知识蒸馏
tags:
- Generative Recommendation
- Semantic ID
- Knowledge Distillation
- Parallel Prediction
- Sequential Recommendation
one_liner: 提出两种跨空间蒸馏目标优化并行语义ID生成式推荐，分别大幅提升召回与排序性能
practical_value: '- 业务侧可根据目标选择蒸馏损失：偏召回选IDM，偏排序选CMM，无需修改推理链路即可提升并行语义ID生成式推荐的效果

  - 训练时可复用梯度校准trick：用硬标签损失与蒸馏损失的梯度L2范数中位数比作为蒸馏权重的校准系数，避免多损失量级差异导致训练不稳定

  - 如需兼顾召回与排序，无需联合训练两个蒸馏损失，分别训练IDM、CMM模型后做分数融合的效果优于联合训练，落地成本更低

  - 交互稀疏的场景下，语义ID的前两层残差编码即可覆盖大部分排序收益，无需蒸馏所有输出头，可节省训练算力'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有并行语义ID生成式推荐仅用观测到的下一个交互物品的硬标签训练，无法提供同用户历史下其他候选物品的分布信息；传统序列推荐模型可输出物品级预测分布，但教师的物品空间与学生的编码空间不匹配，知识无法直接迁移，限制了并行生成式推荐的效果上限。
### 方法关键点
- **IDM（Item Distribution Matching）**：将学生模型的多位置并行编码预测，通过固定的物品-Semantic ID映射重构为全物品的排序分布，与教师模型的物品分布做软交叉熵对齐
- **CMM（Code Marginal Matching）**：通过固定的物品-Semantic ID映射，将教师的物品分布投影到每个编码位置的边缘分布，与学生对应输出头的分类分布做KL散度对齐
- 训练时硬标签损失与蒸馏损失加权结合，用两类损失的梯度L2范数中位数比校准蒸馏权重，避免量级偏差影响训练稳定性
### 关键实验
在Amazon Beauty、Toys、Sports三个公开基准数据集上，对比SASRec、BERT4Rec、RPG、AsymRec等SOTA序列/生成式推荐模型，IDM相对硬标签训练的基线平均提升Recall@10 15.39%，CMM相对基线平均提升NDCG@10 8.28%；两者的分数融合可进一步提升全指标效果。
### 最值得记住的结论
并行语义ID生成式推荐的知识蒸馏无需修改模型并行推理结构，在重构物品空间对齐偏召回、在编码边缘空间对齐偏排序，可按需选择适配业务目标
