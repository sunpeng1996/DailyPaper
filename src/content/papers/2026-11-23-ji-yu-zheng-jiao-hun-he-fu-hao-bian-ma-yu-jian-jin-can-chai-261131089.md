---
title: Orthogonally Mixed Sign Coding with Progressive Residual Refinement for Transformer
  Weight Compression
title_zh: 基于正交混合符号编码与渐进残差优化的Transformer权重压缩方法
authors:
- Anindya Roy Chowdhury
- Atanu Barai
- Nandakishore Santhi
affiliations:
- Los Alamos National Laboratory
arxiv_id: '2611.31089'
url: https://arxiv.org/abs/2611.31089
pdf_url: https://arxiv.org/pdf/2611.31089
published: '2026-11-23'
collected: '2026-11-24'
category: LLM
direction: LLM压缩 · 后训练无监督权重量化
tags:
- Post-training Quantization
- Transformer Compression
- LLM Inference
- Residual Coding
- Orthogonal Transform
one_liner: 提出无训练无CDF的渐进残差符号量化框架，无需codebook即可灵活平衡Transformer权重存储与精度
practical_value: '- 业务侧部署小参数LLM做商品文案生成/推荐query改写时，可复用该无训练量化方案，无需微调就能降低显存占用，仅需调整残差阶段数平衡精度与存储成本

  - 量化时可复用激活感知缩放（AAS）技巧：哪怕权重MSE上升，只要对齐激活统计特征做等价缩放，就能显著降低下游任务的PPL损失，适合推荐/广告场景下游效果优先的量化需求

  - 可复用16位存储量化统计量的trick：相比32位统计量，能再降低约15%的量化后模型体积，几乎不会带来精度损失，适合端侧/边缘侧部署LLM推荐Agent的场景'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
当前LLM部署面临权重存储、传输、推理显存占用高的痛点，主流后训练量化方法要么需要预学习codebook、依赖CDF统计，要么无法灵活调整存储-精度 trade-off，难以适配电商/推荐场景下不同部署环境（端侧/云端/边缘）的差异化资源约束，亟需无需训练、可灵活调优的量化方案。

### 方法关键点
- 设计CDF-free的渐进残差符号编码框架：对权重残差做归一化后，通过种子生成的随机正交矩阵混合，仅编码混合后向量的符号，结合最小二乘拟合增益做权重重建，无需预训练codebook、无需统计CDF
- 实现渐进残差优化：每轮编码上一轮的重建误差，仅当残差RMSE下降时才保留当前阶段，可通过调整残差阶段数直接控制存储-精度平衡，无需重新量化
- 引入激活感知缩放：基于校准数据的激活统计对权重做等价变换，不改变模型计算逻辑的前提下，大幅降低量化带来的下游任务精度损失

### 关键实验
在WikiText-2数据集上测试GPT-2 Large、Llama-3-8B，对比GPTQ、AWQ、QuaRot等主流量化方法：5残差阶段下，GPT-2 Large全权重量化PPL达32.16，仅比全精度高7.6%；Llama-3-8B全权重量化PPL达12.73，仅比全精度高15%；用16位存储统计量可再降15%存储开销，精度几乎无损失。

### 核心结论
权重量化的效果不能仅看权重MSE，对齐激活分布的优化哪怕提升了权重重建误差，也能大幅降低下游任务的精度损失。
