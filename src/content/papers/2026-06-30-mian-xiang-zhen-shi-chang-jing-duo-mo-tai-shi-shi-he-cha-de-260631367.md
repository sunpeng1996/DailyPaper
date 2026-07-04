---
title: Evidence Triangulation for Multimodal Fact-Checking in the Wild
title_zh: 面向真实场景多模态事实核查的证据三角校验方法
authors:
- Stefanos-Iordanis Papadopoulos
- Zacharias Chrysidis
- Christos Koutlis
- Symeon Papadopoulos
- Panagiotis C. Petrantonakis
affiliations:
- Information Technologies Institute, Centre for Research & Technology, Hellas, Greece
- Department of Electrical and Computer Engineering, Aristotle University of Thessaloniki,
  Greece
arxiv_id: '2606.31367'
url: https://arxiv.org/abs/2606.31367
pdf_url: https://arxiv.org/pdf/2606.31367
published: '2026-06-30'
collected: '2026-07-04'
category: Multimodal
direction: 多模态事实核查 · 证据融合优化
tags:
- Multimodal Fact-Checking
- Evidence Fusion
- Cross-Attention
- VLM
- Misinformation Detection
one_liner: 构建真实多模态事实核查基准X-POSE，提出三通路交叉注意力模型TRENT性能超现有SOTA及商用VLM
practical_value: '- 电商虚假营销内容（图文不符商品宣传、虚假种草笔记）识别场景，可复用三通路交叉注意力+关系融合架构，分别对齐文本、图片、外部合规证据三类信息的蕴含/矛盾关系，提升识别准确率

  - 构建业务场景真实标注数据集时，可参考VLM优化的检索策略引入外部佐证资源，降低人工标注成本同时提升数据集对真实场景的覆盖度

  - 多模态内容审核Agent的推理模块可复用显式建模蕴含、矛盾关系的融合机制，提升审核结果可解释性，降低人工复核成本'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
现有多模态事实核查研究依赖合成训练数据与人工构造基准，无法匹配真实社交平台内容复杂度；现有模型仅聚焦模态内一致性或无约束全融合，难以捕捉待核查内容与外部证据的细粒度语义关系，无法有效识别图文搭配的虚假信息。

### 方法关键点
1. 构建开源基准X-POSE：包含X（原Twitter）平台社区标注的真实多模态帖子，配套经VLM优化检索得到的完整新闻文章作为外部核查证据；
2. 提出TRENT模型：采用三路并行交叉注意力流实现证据三角校验，新增关系融合机制显式建模内容间的蕴含、矛盾关系。

### 关键结果
真实场景测试中TRENT全面优于现有专用SOTA模型与商用VLM，相关代码、提示词模板、数据集全开源。
