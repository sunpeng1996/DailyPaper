---
title: What Would You Click? Personalized Video Thumbnail Generation with Preference-aware
  Highlight Retrieval
title_zh: 基于偏好感知高光检索的个性化视频缩略图生成方法
authors:
- Zhiyu He
- Zecheng Zhao
- Tong Chen
- Zi Huang
- Yiqun Liu
- Min Zhang
arxiv_id: '2607.12882'
url: https://arxiv.org/abs/2607.12882
pdf_url: https://arxiv.org/pdf/2607.12882
published: '2026-07-14'
collected: '2026-07-15'
category: RecSys
direction: 视频推荐优化 · 个性化多模态物料生成
tags:
- Personalized Recommendation
- Diffusion Model
- VLM
- Highlight Retrieval
- CTR Optimization
one_liner: 提出两阶段个性化视频缩略图生成框架，耦合偏好感知高亮检索与VLM引导可控扩散生成
practical_value: '- 电商商品短视频/主图个性化生成可复用两阶段框架：先基于用户交互做偏好感知的高光片段检索，再用VLM+扩散生成符合用户偏好的物料，提升点击率

  - 多模态推荐物料生成场景可借鉴「检索锚点+可控生成」范式，平衡生成内容的个性化度与原内容保真度，避免生成虚假宣传物料

  - 个性化内容生成场景可将细粒度用户-内容交互特征融入检索阶段，无需端到端生成，降低大模型推理成本同时提升可控性'
score: 8
source: arxiv-cs.IR
depth: abstract
---

### 动机
现有视频缩略图生成方案输出全局统一结果，未适配用户个性化偏好差异，无法最大化不同人群点击意愿；现有高亮检测方法无法平衡个性化与内容信息性，生成缩略图易脱离原视频、视觉一致性差。
### 方法关键点
采用两阶段耦合架构：第一阶段为偏好感知高亮检索器，建模细粒度用户-视频交互特征，结合视频语义摘要筛选同时匹配用户偏好和视频上下文的多样化视觉锚点；第二阶段为VLM引导的扩散生成管线，提取锚点的语义视觉特征注入生成过程，在保障个性化的同时维持缩略图视觉一致性与原视频保真度。
### 关键结果
在两个公开数据集上性能超过所有检索类、生成类基线达到SOTA；用户实验显示点击偏好显著提升，可有效拉高用户参与度。
