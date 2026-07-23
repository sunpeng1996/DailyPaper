---
title: Wavefront Parallelization for Efficient Learned Image Compression
title_zh: 面向高效学习型图像压缩的波前并行化方法
authors:
- Shimon Murai
- Fangzheng Lin
- Kasidis Arunruangsirilert
- Jiro Katto
affiliations:
- Waseda University
- Institute of Science Tokyo
arxiv_id: '2607.19082'
url: https://arxiv.org/abs/2607.19082
pdf_url: https://arxiv.org/pdf/2607.19082
published: '2026-07-21'
collected: '2026-07-23'
category: Other
direction: 学习型图像压缩 · 推理速度优化
tags:
- Image Compression
- Wavefront Parallelization
- Autoregressive Model
- Inference Acceleration
- Neural Network
one_liner: 提出免训练推理加速算法，为预训练自回归图像压缩模型提13倍以上速度且无损率失真性能
practical_value: '- 电商海量商品图像/素材存储、传输场景可直接复用该方法，无需重训现有学习型图像压缩模型即可获得13倍以上推理加速，降本增效

  - 业务中使用自回归类模型（如文案生成、序列预测、图像生成）的场景，可借鉴波前依赖重排思路，仅调整推理计算顺序即可实现免训练提速，避免架构改动和重训成本

  - 对延迟敏感的推理场景，可参考该工作的tradeoff策略，适当放宽严格的依赖约束，灵活平衡业务效果和推理耗时'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
自回归上下文模型是学习型图像压缩的核心组件，率失真性能优异但存在串行推理速度慢的问题，现有加速方案需要修改模型架构并重训，无法直接适配存量预训练模型。
### 方法关键点
借鉴视频编码标准中的波前并行思想，提出完全免训练的推理阶段加速算法：将推理计算顺序重排为最优交错波前顺序，最小化串行执行步骤的同时100%保留原模型的自回归依赖关系；同时支持放宽精确上下文依赖约束，换取更高解码速度。
### 关键结果数字
在Cheng等人的预训练自回归图像压缩模型上实现13倍以上推理加速，完全保留原模型的率失真性能，放宽依赖约束可进一步提升解码速度。
