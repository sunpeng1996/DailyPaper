---
title: 'T3R: Training-Free Two-Stage Token Refinement Towards Efficient and Robust
  VLA Models'
title_zh: T3R：免训练两阶段Token优化实现高效鲁棒VLA模型
authors:
- Mohammed Hassan
- Zhenyang Chen
- Zheng Wang
- Zhixin Zhu
- Tianlong Chen
- Yingyan
- Lin
- Chaojian Li
affiliations:
- The University of Texas at Austin
- Georgia Institute of Technology
- University of Illinois Urbana-Champaign
- Hong Kong University of Science and Technology
- University of North Carolina at Chapel Hill
arxiv_id: '2611.08413'
url: https://arxiv.org/abs/2611.08413
pdf_url: https://arxiv.org/pdf/2611.08413
published: '2026-11-05'
collected: '2026-11-07'
category: Multimodal
direction: 多模态大模型 · 推理效率优化
tags:
- VLA
- Token Pruning
- Training-Free
- Inference Efficiency
- Multimodal LLM
one_liner: 提出免训练两阶段Token精简框架，在VLA模型上同时提升推理效率与分布偏移下鲁棒性
practical_value: '- 多模态商品推荐/直播内容理解场景可复用两阶段Token优化思路：先剪枝无关视觉Token降低算力，再用显著性引导注意力偏置提升关键内容权重，兼顾效率与效果

  - 免训练优化思路可直接落地存量多模态LLM服务，无需重训即可降低推理时延，适配大分辨率商品图、直播流等长序列多模态输入场景

  - 分布偏移下的鲁棒性优化技巧可迁移到跨域推荐/搜索场景，通过过滤无关输入上下文减少OOD样本对排序、生成结果的干扰'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
VLA模型推理成本高，大量冗余视觉Token不仅带来额外算力开销，还会引入无关背景干扰，分布偏移场景下预测准确率下降明显。
### 方法关键点
提出免训练两阶段Token优化框架T3R：1）第一阶段采用分割引导的Token剪枝，移除无关视觉Patch，降低算力同时消除干扰上下文；2）第二阶段采用显著性引导的注意力偏置，将保留Token的注意力向动作关键视觉区域、语言指令倾斜，进一步提升决策相关性。
### 关键结果数字
在LIBERO-Spatial数据集上剪枝85%视觉Token仍匹配原模型成功率，分布偏移扰动下成功率最高提升7个百分点；单步推理新增开销仅7.8ms，高分辨率输入下LLM前向推理速度最高提升3.3倍，多相机场景下效率-精度收益最优。
