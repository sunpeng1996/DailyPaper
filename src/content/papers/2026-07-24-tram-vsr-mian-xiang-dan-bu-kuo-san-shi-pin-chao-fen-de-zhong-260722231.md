---
title: 'TRaM-VSR: Importance-Aware Token Routing and Merging for One-Step Diffusion
  Video Super-Resolution'
title_zh: TRaM-VSR：面向单步扩散视频超分的重要性感知令牌路由与合并
authors:
- Sicheng Gao
- Zhuyun Zhou
- Yixuan Liu
- Tong Shen
- Zongwei Wu
- Radu Timofte
affiliations:
- Advanced Micro Devices Inc.
- Computer Vision Lab, CAIDAS & IFI, University of Würzburg
arxiv_id: '2607.22231'
url: https://arxiv.org/abs/2607.22231
pdf_url: https://arxiv.org/pdf/2607.22231
published: '2026-07-24'
collected: '2026-07-27'
category: Other
direction: 扩散模型效率优化 · 令牌动态路由
tags:
- Diffusion Transformer
- Token Routing
- Video Super-Resolution
- Inference Acceleration
- DiT
one_liner: 提出融合双先验的令牌路由合并框架，提升单步扩散VSR推理效率同时保质量与时序一致性
practical_value: '- 重要性感知的token分路计算思路可迁移到电商多模态长内容推理场景：将价格、卖点等核心信息token走高精度计算流，背景、冗余描述走压缩流，在不损失关键信息的前提下降低LLM推理成本

  - 离线规划器校准token重要性、动态分配不同网络层计算量的方法，可复用在生成式推荐（如商品文案、卖点生成）的多步推理过程中，平衡生成质量与速度

  - 多粒度计算资源适配思路可用于推荐系统商品视频预处理环节：动态识别视频中商品主体、营销信息等关键区域分配更多算力，提升超分/转码等预处理任务效率'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
基于大规模Diffusion Transformer（DiT）先验的单步扩散视频超分（VSR）感知质量优异，但时空稠密token序列的注意力计算复杂度为平方级，现有效率优化方案易出现不可逆细节丢失、时序闪烁问题，落地难度高。
### 方法关键点
1. 融合运动敏感时序特征与语义文本相似度计算token重要性，精准定位动态物体、结构边界等高价值区域
2. 引入离线规划器校准重要性得分，指导网络块最优分组路由，适配扩散模型不同深度的多粒度特性
3. 分组内高重要性token走高保真局部计算流，低信息量token聚合为紧凑全局流，计算资源分配随网络深度动态调整
### 关键结果
在保持SOTA重建精度、鲁棒时序一致性的前提下，实现显著的推理加速，无明显细节丢失与时序闪烁问题。
