---
title: Hierarchical Multimodal Interaction Reasoning for Dyadic Relationship Recognition
title_zh: 面向二元关系识别的分层多模态交互推理方法
authors:
- Wang Tang
- Fethiye Irmak Dogan
- Linbo Qing
- Ce Zhu
- Hatice Gunes
affiliations:
- Chengdu University of Information Technology
arxiv_id: '2610.36249'
url: https://arxiv.org/abs/2610.36249
pdf_url: https://arxiv.org/pdf/2610.36249
published: '2026-10-26'
collected: '2026-11-08'
category: Reasoning
direction: 多模态交互 · 社交关系推理
tags:
- Multimodal
- Sparse Routing
- Hierarchical Learning
- Transformer
- Social Computing
one_liner: 提出分层多模态推理框架HiRe-DRR，通过稀疏路由优化双人社交关系识别精度
practical_value: '- 稀疏路由分专家处理不同特征交互的思路，可迁移至多模态推荐的用户/商品多信号融合场景，针对不同用户群分层配置特征权重

  - 从粗到细的分层监督损失（HC-Loss）可复用在层级分类任务（如用户价值分层、商品类目预测、社交关系分层），显著降低错分类概率

  - 多模态特征高低层拆分逻辑可借鉴到直播/短视频场景的用户互动关系识别，优化基于社交关系的内容推荐效果'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
现有二元社交关系识别方法直接将多模态异质特征投影到共享空间做平层分类，忽略不同亲密度关系依赖的交互模式差异：远关系仅需直接行为对应特征即可识别，近关系需情感、行为、多模态协同响应特征支撑，现有方案泛化性差。
### 方法关键点
1. 提出HiRe-DRR分层多模态交互推理框架，从特征层级、交互类型、关系层级三个维度组织识别证据，拆分人脸、肢体、语音、文本特征为高低层表示，构建同/异质跨主体交互
2. 设计MoI-Former，将不同交互作为专属专家，通过关系感知稀疏路由筛选相关证据同时保留上下文交互信息
3. 提出HC-Loss，通过由粗到细的分层监督挖掘社交关系的层级特性，实现结构化推理
### 关键结果
在3个二元关系基准数据集上性能全面优于现有图像、视频、多模态SOTA方法，可解释性分析验证远关系依赖低层同质交互、近关系依赖高层异质交互的结论
