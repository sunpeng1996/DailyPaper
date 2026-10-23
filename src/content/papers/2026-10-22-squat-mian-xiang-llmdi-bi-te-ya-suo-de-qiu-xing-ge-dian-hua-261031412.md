---
title: 'SQuAT: Spherical Lattice Vector Quantization-Aware Training'
title_zh: SQuAT：面向LLM低比特压缩的球形格点向量量化感知训练
authors:
- Sebastian Loeschcke
- Ivan Koryakovskiy
- Tycho F. A. van der Ouderaa
- Riccardo Del Chiaro
- Mart van Baalen
- Paul N. Whatmough
- Markus Nagel
affiliations:
- University of Copenhagen
- Qualcomm AI Research
arxiv_id: '2610.31412'
url: https://arxiv.org/abs/2610.31412
pdf_url: https://arxiv.org/pdf/2610.31412
published: '2026-10-22'
collected: '2026-10-23'
category: Training
direction: LLM低比特压缩 · 量化感知训练
tags:
- VQ
- QAT
- LLM Compression
- E8 Lattice
- STE
one_liner: 提出形状增益分解VQ的分置STE训练方法，实现10B token级VQ-QAT规模化落地
practical_value: '- 端侧部署电商客服Agent、推荐理由生成等小尺寸LLM时，可直接复用SQuAT 2~2.25bpw量化方案，在精度损失可接受范围内将显存占用降低50%以上，提升推理吞吐量

  - 广告/推荐侧大模型打分、语义召回等场景，可借鉴形状增益分解+分置STE的梯度优化思路，优化现有INT4/INT8量化方案的精度损失问题

  - 工程上可复用其分布式最近邻分配、索引缓存、融合Kernel优化方案，将VQ-QAT训练速度提升10倍以上，解决大参数量化训练的算力瓶颈'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
低比特量化是解决LLM部署时显存带宽瓶颈的核心手段，现有标量量化在<3bpw的极低比特下精度损失严重；向量量化（VQ）虽然率失真表现更优，但此前VQ-QAT无法规模化扩展到十亿参数、十亿token训练的工业级场景，且传统联合STE未利用VQ的形状增益分解结构，训练效果差。
### 方法关键点
- 权重分解为方向（shape）和幅值（gain）两个独立分量：方向用E8格点衍生的球形码本量化，幅值用低比特标量量化器独立量化
- 反向传播采用分置STE策略：分别对shape和gain的量化过程应用STE，自动诱导方向分量的切空间更新，等价于隐式黎曼球形优化，无需额外设计球面优化器
- 工程上实现分布式精确最近邻分配：多worker仅同步量化后的离散索引，搭配融合Kernel、索引缓存机制，训练速度提升12.8倍，支持10B token级别的VQ-QAT训练
### 关键实验结果
在LLaMA-3.2-1B/3B、Qwen3-1.7B/4B模型上验证，对比INT-QAT、标准VQ-QAT等基线：
- 2.25bpw比特率下，SQuAT在所有模型和训练预算下的WikiText2困惑度均优于INT-QAT，1B token训练时MMLU最高提升7.9%，GSM8K准确率最高提升4.9%
- 相同码本和初始化下，相比标准联合STE的VQ-QAT，SQuAT在所有任务上均取得一致精度提升
- 1B参数模型训练耗时从62.5s/it降至4.9s/it，接近BF16原生训练速度
### 核心结论
形状增益分解+分置STE的策略，能在几乎无额外开销的前提下大幅提升VQ-QAT的训练效果，是极低比特LLM量化落地的最优方案之一
