---
title: Proactive Dimension-Adaptive Denoising for Graph Collaborative Filtering via
  Representation Coherence
title_zh: 基于表征一致性的图协同过滤主动维度自适应去噪方法
authors:
- Wenjun Li
- Dong Zhao
- Jiaying Shi
- Juan Zhang
- Zhaoming Pan
- Zhimin Zhang
affiliations:
- Netease Media Group
arxiv_id: '2611.11801'
url: https://arxiv.org/abs/2611.11801
pdf_url: https://arxiv.org/pdf/2611.11801
published: '2026-11-09'
collected: '2026-11-10'
category: RecSys
direction: 图协同过滤 · 隐式反馈去噪
tags:
- GraphCF
- Denoising
- ImplicitFeedback
- LightGCN
- Recommendation
one_liner: 提出融合主动表征一致性与损失信号的图CF去噪框架，无推理开销且效果优于SOTA
practical_value: '- 现有LightGCN生产管线可无缝替换，推理零额外开销、零参数增加，训练耗时仅提升约4.2%，几乎无痛升级

  - 表征一致性RCD模块可单独复用，和现有损失类去噪方法结合，可补全20%左右的噪声漏判、正样本误判场景

  - 用户活跃度加权的多信号融合策略可直接迁移：冷启动用户自动切回损失信号，解决冷启动下历史表征中心不准的问题

  - 轻量对比正则仅优化embedding几何分布、不参与去噪决策，可低成本加入现有CF训练流程提升表征区分度'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有图CF的隐式反馈去噪完全依赖训练损失这一被动信号，只有噪声引发预测误差后才能被检测，还受负采样、训练阶段、难正样本干扰，漏判误判率高；噪声会通过图传播污染用户表征，尤其在电商、内容推荐等普遍存在的稀疏交互场景下，对效果劣化更明显。

### 方法关键点
1. 设计Representation Coherence Detection (RCD)主动噪声检测模块，计算当前交互表征与用户历史偏好中心的余弦相似度作为一致性得分，独立于损失信号，可提前识别偏离长期偏好的噪声交互
2. 活跃度自适应融合RCD与EMA平滑的CE损失信号：活跃用户权重偏向更可靠的RCD，冷启动用户自动侧重损失信号，规避冷启动下历史中心不准的问题
3. 融合后的噪声评分映射为交互级维度掩码，噪声交互仅开放少量维度参与计算，限制其对整体表征的污染
4. 加入轻量对比正则优化embedding均匀性，提升RCD的区分度，不参与去噪决策

### 关键实验
在Amazon-book、Yelp、MovieLens-1M三个公开数据集上对比SOTA去噪基线DAR，Recall@5分别提升+17.95%、+12.33%、+5.63%，数据越稀疏增益越显著；移除RCD模块后Recall@5下降10.9%，为核心贡献点。

### 核心结论
隐式反馈去噪中，表征一致性与训练损失是正交互补的信号，融合二者能同时降低噪声漏判与正样本误判，且适配全量用户群。
