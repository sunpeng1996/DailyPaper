---
title: 'IMFuse: Instance-Aware Multi-Layer Fusion for LLM-Enhanced Sequential Recommendation'
title_zh: IMFuse：面向LLM增强序列推荐的实例感知多层融合方法
authors:
- Yuheng Zheng
- Yu Cui
- Bin Wu
- Jian Zhang
- Ye Feng
- Can Wang
- Jiawei Chen
affiliations:
- Zhejiang University
- Zhengzhou University
- University of Science and Technology of China
arxiv_id: '2607.27002'
url: https://arxiv.org/abs/2607.27002
pdf_url: https://arxiv.org/pdf/2607.27002
published: '2026-07-29'
collected: '2026-07-30'
category: RecSys
direction: LLM增强序列推荐 · 多层表征融合
tags:
- Sequential Recommendation
- LLM Embedding
- Multi-layer Fusion
- Instance-aware Modulation
- Semantic Enhancement
one_liner: 提出实例感知的LLM多层表征融合策略提升序列推荐性能，仅引入极低额外参数与计算开销
practical_value: '- 可复用LLM多层表征融合思路：无需局限于LLM最后一层输出，LLM深层存在维度坍塌问题，浅中层包含互补语义信息，融合多粒度表征可稳定提升推荐效果，且适配各类现有语义增强方案

  - 实例感知调制可低成本落地：通过小参数量的路由+共享模板库实现不同品类商品的自适应层权重调整，仅新增0.03M参数，几乎不增加训练推理延迟，可直接插入现有推荐流水线

  - 初始化trick可直接复用：给深层更高的初始权重（深度偏置初始化），能让融合模块训练更快收敛，避免随机初始化导致的效果波动'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有LLM增强序列推荐方案普遍仅采用LLM最后一层隐状态作为语义表征，未充分挖掘其他层的有效信号。经实证分析发现三大问题：1）LLM越深的层维度坍塌越严重，细粒度语义被少数主成分主导；2）不同层编码从粗到细的互补语义，远距离层语义差异显著；3）不同品类商品对语义深度的偏好存在异质性，统一使用最后一层会损失大量有效信息，亟需自适应的多层融合策略。
### 方法关键点
- 全局维度级层偏好学习：构造可学习的「维度×层数」权重矩阵，沿层维度做softmax得到全局融合权重，初始化时引入深度偏置先验，给深层更高初始权重加速收敛
- 实例感知专家调制：以LLM最后一层表征作为商品语义摘要，通过MLP路由得到共享专家模板的权重，动态调整全局层偏好，生成商品专属融合权重，无需为每个商品单独学习参数，保证轻量化
- 模型兼容设计：融合得到的多粒度语义表征直接接入原有ID-语义融合流水线，无需修改下游推荐模型结构，适配各类序列推荐主干与语义增强方案
### 关键实验结果
在4个亚马逊真实电商数据集（服装、美妆、玩具、办公用品）上，对比SASRec、HSTU两类主流序列推荐主干，RLMRec、LLM-ESR等4种SOTA语义增强方案，以及3种通用多层融合基线。IMFuse相对所有基线平均提升6.72%，其中适配SASRec平均提升7.01%，适配HSTU平均提升6.43%，相比通用多层融合方法平均提升3.91%，仅新增0.03M可训练参数，训练推理延迟增加不足5%。
> 最值得记住的结论：LLM各层的语义表征对推荐的价值远不止最后一层，针对商品异质性做自适应多层融合，是极低投入高收益的LLM增强推荐优化方向
