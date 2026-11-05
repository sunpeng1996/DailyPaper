---
title: Where to Connect? Boosting MLLMs via Dynamic Gated Pathways across ALL ViT
  and LLM Layers
title_zh: 基于ViT与LLM全层动态门控通路的多模态大模型性能优化
authors:
- Yingying Yan
- Jiaqi Tang
- Wei Wei
- Qianzhou Wang
- Lei Zhang
- Jianmin Chen
- Yuyang Xia
- Botong Geng
- Jinjian Wu
- Qifeng Chen
affiliations:
- Northwestern Polytechnical University
- Hong Kong University of Science and Technology
arxiv_id: '2611.06844'
url: https://arxiv.org/abs/2611.06844
pdf_url: https://arxiv.org/pdf/2611.06844
published: '2026-11-04'
collected: '2026-11-05'
category: Multimodal
direction: 多模态大模型 · ViT-LLM跨层融合
tags:
- MLLM
- ViT
- Dynamic Routing
- Cross-Modality Fusion
- Gated Mechanism
one_liner: 全连接动态门控路由DGP自适应匹配LLM各层视觉粒度需求，显著提升MLLM多模态任务性能
practical_value: '- 电商多模态商品理解/搜推场景可复用DGP动态门控逻辑，让LLM不同层按需调用ViT不同粒度视觉特征，提升商品图文匹配、属性识别准确率

  - 多模态Agent视觉信息注入可抛弃传统单层固定注入方案，采用全连接动态路由降低跨模态信息损耗，适配商品穿搭推荐、瑕疵检测等复杂推理任务

  - 跨层动态特征融合思路可迁移到推荐排序模型，给不同深度DNN层动态分配对应粒度的用户/物品特征输入，提升排序效果'
score: 7
source: arxiv-cs.CV
depth: abstract
---

**动机**：主流MLLM仅将固定单层视觉特征注入LLM，忽略不同LLM层对视觉特征粒度的差异化需求；现有多层融合方案多采用编码器侧特征压缩或预定义稀疏连接，无法自适应建模ViT与LLM层级间的跨层交互。
**方法关键点**：动态门控通路（DGP）路由机制建立ViT全层到LLM全层的全连接通路，每个LLM层基于自身语义状态动态筛选所需的ViT层视觉特征，实现跨层级自适应交互。
**关键结果**：基于LLaVA-1.5-7B/13B实现，相比7B基线，SQA$^{I}$提升4.2，MM-Vet提升3.3，VizWiz、LLaVA$^{W}$均提升3.1，在多数基准上超越此前多层视觉融合方案；层路由分析验证不同LLM层可按需选择对应粒度视觉特征，兼具效果与可解释性。
