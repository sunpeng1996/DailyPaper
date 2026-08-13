---
title: 'SAMOT: State-Aware Step Modulation and Optimal Transport Matching for Audio-Visual
  Instance Segmentation'
title_zh: SAMOT：面向音视频实例分割的状态感知步长调制与最优传输匹配
authors:
- Kai Peng
- Yunzhe Shen
- Miao Zhang
- Leiye Liu
- Wei Ji
- Jingjing Li
- Yongri Piao
- Huchuan Lu
affiliations:
- Dalian University of Technology
- Yale University
- Carnegie Mellon University
arxiv_id: '2608.08147'
url: https://arxiv.org/abs/2608.08147
pdf_url: https://arxiv.org/pdf/2608.08147
published: '2026-08-08'
collected: '2026-08-13'
category: Multimodal
direction: 多模态音视频实例分割算法优化
tags:
- Multimodal Fusion
- Instance Segmentation
- Mamba
- Optimal Transport
- State Space Model
one_liner: 提出含自适应步长调制与最优传输匹配的音视频实例分割SOTA框架
practical_value: '- 多模态特征匹配场景可复用OT-MM模块，引入熵正则最优传输+MMD正则优化跨域/跨模态特征对齐，可适配直播带货场景音视频商品特征与商品库的精准匹配

  - 长序列时序建模场景可参考ADSM思路，根据时序波动、模态差异自适应调整Mamba步长，平衡响应速度和长程建模稳定性，可迁移至用户长行为序列召回、直播内容时序理解场景

  - 跨模态隐式匹配效果不佳时，可尝试将匹配问题转化为可解释的最优传输问题，用log域Sinkhorn迭代高效求解，适配多模态广告素材语义匹配、短视频内容打标等场景'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
音视频实例分割（AVIS）需在长视频序列中完成实例级分类、分割、跟踪，存在两大核心痛点：一是模态状态动态变化严重干扰长程建模，二是模态间结构、分布差异大阻碍实例级精准关联；现有方案依赖固定步长Transformer/递归Mamba，无模态状态自适应能力，且隐式匹配逻辑忽略模态间固有分布不一致问题。
### 方法关键点
1. 设计自适应动态步长调制（ADSM）模块，基于时序波动、跨模态差异、历史上下文三类信号自适应调整Mamba步长，兼顾模态状态变化响应速度与长程建模稳定性
2. 设计最优传输匹配调制（OT-MM）模块，将实例级跨模态匹配转化为熵正则最优传输问题，通过log域Sinkhorn迭代高效求解，额外引入MMD正则强化分布级一致性
### 关键结果
在AVIS基准数据集上取得SOTA性能，FSLA指标提升3.76，HOTA指标提升2.75，mAP指标提升2.58
