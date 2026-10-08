---
title: Layerwise Error Attribution for Fast and Robust Mixed-Precision Post-Training
  Quantization
title_zh: 基于分层误差归因的快速鲁棒混合精度训练后量化方法
authors:
- Samy Houache
- Yann Traonmilin
- Jean-François Aujol
affiliations:
- Univ. Bordeaux
- Thales AVS
- CNRS
arxiv_id: '2610.09877'
url: https://arxiv.org/abs/2610.09877
pdf_url: https://arxiv.org/pdf/2610.09877
published: '2026-10-07'
collected: '2026-10-08'
category: Training
direction: 模型压缩 · 混合精度训练后量化
tags:
- Post-training Quantization
- Mixed Precision
- Model Compression
- Layerwise Error Attribution
- Robust Quantization
one_liner: 提出分层概率误差归因的无求解器混合精度PTQ方法，兼顾速度、精度与校准数据鲁棒性
practical_value: '- 部署端侧/嵌入式的生成式推荐、Agent推理模型时，可复用本文的分层局部误差分数+无求解器贪心位宽分配逻辑，无需依赖复杂整数规划求解器，量化速度提升至少一个量级

  - 推荐场景的校准数据常存在用户行为噪声、脏样本，用本文的概率误差归因方法做PTQ，可避免校准数据污染导致的量化后模型效果暴跌，实测噪声下性能损失比SOTA方法低90%以上

  - 量化大参数量推荐排序、LLM召回模型时，可复用本文按层/块分组分配位宽的思路，在保证业务效果的前提下最大化压缩率，降低推理成本'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有混合精度PTQ方法存在两个核心痛点：一是位宽分配依赖整数规划、Pareto搜索等外部求解器，计算速度慢，不支持快速迭代；二是量化效果对校准数据质量敏感，数据存在噪声/污染时效果暴跌，无法适配边缘端、嵌入式设备的模型部署需求。

### 方法关键点
- 提出分层概率量化误差分析框架，将每层的量化误差拆分为前层传播误差与当前层本地扰动两部分，避免全局误差分析的悲观性
- 基于本地扰动项设计可分离的层/块敏感度分数，仅需1次全精度前向传播即可完成所有候选位宽的分数计算，无需多次网络评估
- 采用无求解器的贪心位宽分配策略：初始所有块设为最高位宽，每次迭代选择「单位比特节省带来的分数增量最小」的块降低位宽，直到满足内存预算

### 关键实验结果
在DRUNet图像去噪任务上测试，平均4比特权重预算下，干净校准数据时效果与SOTA的CLADO方法持平（仅低0.008dB PSNR）；校准数据污染时，PSNR比CLADO最高高7.5dB；位宽分配速度比AIMET快28×，比CLADO快2570×；迁移到潜扩散模型时，FID比Q-Diffusion低1.773，配对PSNR比均匀4比特量化高10.1dB。

### 最值得记住的一句话
混合精度PTQ无需依赖复杂的全局优化求解器，基于分层局部误差的轻量贪心分配即可达到SOTA效果，同时兼具强鲁棒性与超高速优势
