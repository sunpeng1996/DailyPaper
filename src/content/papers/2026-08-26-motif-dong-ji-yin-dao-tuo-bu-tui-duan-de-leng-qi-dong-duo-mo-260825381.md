---
title: 'MOTIF: Motivation-guided Topology Inference for Cold-start Multimodal Recommendation'
title_zh: MOTIF：动机引导拓扑推断的冷启动多模态推荐框架
authors:
- Yurui Shi
- Yuchen Miao
- Ximing Hu
- Zijun Wang
- Chang Han
affiliations:
- Taiyuan University of Technology
- Sydney Smart Technology College, Northeastern University
arxiv_id: '2608.25381'
url: https://arxiv.org/abs/2608.25381
pdf_url: https://arxiv.org/pdf/2608.25381
published: '2026-08-26'
collected: '2026-08-27'
category: RecSys
direction: 冷启动多模态推荐 · LLM增强图重构
tags:
- Cold-start Recommendation
- Multimodal Recommendation
- Graph Contrastive Learning
- LLM4Rec
- Graph Reconstruction
one_liner: 通过离线LLM推理动机重构可迁移物品拓扑，实现低延迟高性能冷启动多模态推荐
practical_value: '- 冷启动场景可复用「离线LLM推理动机→重构物品拓扑→仅用图嵌入在线推理」架构，避免在线LLM调用高延迟，平衡语义能力与推理性能

  - 可尝试将LLM语义作为辅助监督信号而非直接融入预测特征，有效规避语义漂移、表示空间不匹配带来的噪声

  - 多模态物品关联构建时，可融合LLM推理的功能关系（互补/替代/同场景）与原始多模态相似度，提升冷启动物品拓扑连通性

  - 图对比学习可仅对最终层表示做扰动加特征门控校准，降低计算开销的同时提升稀疏场景表示鲁棒性'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
冷启动多模态推荐存在三大耦合问题：稀疏交互掩盖用户真实意图、冷物品拓扑孤立无协同传播路径、基于特征相似度构建的物品图易出现语义漂移（例如外观相似但功能不同的商品被误关联）；现有方法多单独优化语义建模、图重构、表示鲁棒性，无法协同解决上述问题，且直接融合LLM语义特征易引入噪声。

### 方法关键点
- 离线语义动机推理：用冻结LLM分别推理物品的功能、场景、关联关系，以及用户交互动机，编码为语义向量，无在线LLM调用
- 知识增强图重构：融合LLM语义相似度、原始多模态相似度，搭配LLM输出的物品功能关系先验计算边权重，为每个物品保留Top-Kg邻居，重构物品关联图后与原交互图合并
- 加权图对比学习：仅对最终层图嵌入做扰动生成对比视图，加特征激励门控校准表示，降低噪声同时提升鲁棒性
- 语义-结构对齐：设置辅助对齐损失，将LLM语义向量和图嵌入映射到共享空间对齐，无需直接融合语义向量到预测环节
- 预测仅用图嵌入做内积打分，整体损失由BPR排序损失、对比损失、对齐损失和L2正则组成

### 关键实验
在Amazon-Baby、Amazon-Sports、MicroLens-50K三个多模态基准数据集上，对比图协同过滤、多模态推荐、LLM增强推荐等20+基线；整体效果相对最强基线最高提升6.07%，极端冷用户场景相对提升超20%，冷物品场景相对提升超25%；在线推理延迟与LightGCN等轻量图推荐模型相当。

### 核心结论
将LLM导出的知识转化为图结构和表示监督信号，效果优于直接将语义特征融入预测环节，还能避免在线LLM调用的性能开销。
