---
title: 'DeltaV: Thinking with Visual State Updates in Unified Large Multimodal Models'
title_zh: DeltaV：统一多模态大模型中基于视觉状态更新的推理方法
authors:
- Pengjie Wang
- Linger Deng
- Zujia Zhang
- Shaojie Zhang
- Zhenbo Luo
- Pei Fu
- Jian Luan
- Xiang Bai
- Yuliang Liu
affiliations:
- Huazhong University of Science and Technology
- MiLM Plus, Xiaomi Inc.
arxiv_id: '2607.08434'
url: https://arxiv.org/abs/2607.08434
pdf_url: https://arxiv.org/pdf/2607.08434
published: '2026-07-09'
collected: '2026-07-10'
category: Multimodal
direction: 多模态大模型 · 增量视觉推理优化
tags:
- Multimodal LLM
- Delta Inference
- Token Routing
- CoT Dataset
- Visual Reasoning
one_liner: 增量视觉更新范式的统一多模态大模型，搭配动态Token路由与百万级多模态CoT数据集，提升推理效率与效果
practical_value: '- 增量视觉更新思路可迁移至多模态推荐场景的商品图个性化修改、轮播素材生成等任务，大幅降低推理Token开销

  - TSIM Router动态分配Token预算的方法可复用至生成式推荐、多模态Agent的资源调度场景，根据任务复杂度动态分配计算资源

  - StructCoT多模态链式推理数据集构建方法可参考，用于训练电商场景多模态导购Agent，提升复杂咨询场景推理准确性'
score: 7
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有统一多模态大模型（ULMM）多步推理时每次生成完整中间视觉状态，存在大量视觉Token冗余，关键状态转换的监督信号被稀释，推理效率与效果受限。

### 方法关键点
1. DeltaV框架以增量视觉更新替代全图生成逻辑，基于历史视觉状态预测仅包含变化部分的紧凑更新Token，避免重复建模不变内容；
2. 引入时序相似度（TSIM）Router，当边际重建收益低于阈值时停止分配新Token，动态匹配更新Token预算与视觉变化幅度；
3. 构建包含1.05M样本、覆盖44个任务域的StructCoT多模态 interleaved 推理数据集，提升模型泛化性。

### 关键结果
- 视觉更新范式平均减少55.6%新生成视觉Token且无重建精度损失，推理效果较全图生成方案提升3.3%
- DeltaV-2B在域内多模态推理任务上超更大规模开源模型8.4%，同参数量下较Qwen3-VL-2B在外部基准领先5.9%
