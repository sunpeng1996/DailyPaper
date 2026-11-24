---
title: 'NoveltyGate: Novelty, Not Error, Decides Which VLA Prefix Tokens to Compute
  Exactly'
title_zh: NoveltyGate：基于新颖度而非误差决策VLA前缀token计算路由
authors:
- Lemeng Qi
affiliations:
- Johns Hopkins University
arxiv_id: '2611.31099'
url: https://arxiv.org/abs/2611.31099
pdf_url: https://arxiv.org/pdf/2611.31099
published: '2026-11-23'
collected: '2026-11-24'
category: LLM
direction: 大模型推理优化 · 动态路由
tags:
- Low-rank Compression
- Inference Acceleration
- Dynamic Routing
- VLA
- CUDA Graph
one_liner: 提出免训练的NoveltyGate动态路由，为VLA前缀计算加速1.61倍且保留原任务性能
practical_value: '- 做LLM4Rec/多模态Agent推理加速时，可复用「按输入新颖度而非近似误差选token计算路径」的思路，避免误差-依赖gap导致的效果损失

  - 动态路由逻辑可选择每层决策1次而非每次矩阵乘决策，避免中间张量搬运，保持张量形状静态可适配CUDA图提升推理速度

  - 免训练的压缩路由方案可快速落地到生成式推荐、多模态商品理解等在线业务，无需重新训练大模型降低落地成本'
score: 7
source: arxiv-cs.LG
depth: abstract
---

### 动机
Flow-matching VLA模型（如π0.5）每次控制步都要重编码图像和指令，前缀FFN层占73%以上计算量；传统基于近似误差选择token做精确计算的思路存在误差-依赖gap：大误差集中在模型依赖度极低的token，优先优化这些token反而会导致整体效果下降。

### 方法关键点
提出免训练的NoveltyGate路由机制，每层在矩阵乘前对每个前缀token做一次新颖度判断（是否落在校准阶段见过的子空间外），新颖token走原始MLP，非新颖token走低秩MLP；每层仅决策1次，无需移动宽中间张量，张量形状静态可整合成单个CUDA图运行。

### 关键结果
在LIBERO数据集上，π0.5前缀计算最高加速1.61×；相同计算量下，动作偏差比通道裁剪、低秩压缩方法小2.7~2.9×，完全保留闭环任务成功率。
