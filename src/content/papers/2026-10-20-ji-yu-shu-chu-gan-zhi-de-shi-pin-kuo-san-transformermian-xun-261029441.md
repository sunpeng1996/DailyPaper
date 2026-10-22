---
title: 'Sparsity Should Be ALLOTted by Output: Training-Free Allocation of Block-Sparse
  Attention for Video Diffusion Transformers'
title_zh: 基于输出感知的视频扩散Transformer免训练块稀疏注意力分配方法ALLOT
authors:
- Tianze Xia
- Xiaoling Zhou
- Ruya Lan
- Yiqiao Liao
- Chengru Song
- Shiming Xiang
affiliations:
- UCAS
- CASIA
- PKU
- KlingAI Research
arxiv_id: '2610.29441'
url: https://arxiv.org/abs/2610.29441
pdf_url: https://arxiv.org/pdf/2610.29441
published: '2026-10-20'
collected: '2026-10-22'
category: Multimodal
direction: 视频扩散Transformer · 免训练稀疏注意力加速
tags:
- Diffusion Transformer
- Block-Sparse Attention
- Training-Free
- Inference Acceleration
- Video Generation
one_liner: 提出免训练的ALLOT稀疏分配方案，同等延迟下大幅提升视频扩散模型生成质量
practical_value: '- 电商AIGC广告/商品短视频生成场景可直接复用ALLOT框架，无需修改现有稀疏注意力内核，仅替换分配逻辑即可在保质量的前提下降低DiT推理成本

  - LLM/多模态模型的稀疏注意力、KV cache优化可参考「离线探测敏感度+轨迹校准+全局延迟预算优化」的思路，避免人工设置启发式规则，敏感度跨输入稳定仅需离线测量一次

  - 多步生成类任务（扩散采样、Agent多轮规划）的资源分配可复用拉格朗日松弛求解方案，在固定延迟约束下全局最优分配每一步的计算量'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
视频扩散Transformer（DiT）的3D注意力计算成本随token数平方增长，单GPU生成720p/81帧视频需近1小时，稀疏注意力是核心降本方案。但现有稀疏度分配方法要么依赖人工启发式规则（如前10%去噪步全量）泛化性差，要么用局部指标（注意力质量、单步误差）无法反映对最终生成质量的影响，导致稀疏后质量下降明显。
### 方法关键点
- 核心观察：不同层、不同去噪步的稀疏化对最终视频质量的敏感度差异可达数百倍，同模型下同稀疏策略的敏感度排序跨输入高度稳定（Spearman相关0.8~1.0）
- 框架分为三步：1）细胞探测：离线测量每个层在不同噪声水平、不同稀疏度下的单步输出误差；2）轨迹校准：分窗口测量稀疏化后的最终视频误差，校准每一步的误差传播增益，修正单步误差对最终质量影响的低估；3）延迟约束优化：基于实测的不同稀疏度下的内核延迟，用拉格朗日松弛法全局求解每个<层,步>单元的最优稀疏度，满足总延迟预算
- 完全兼容现有块稀疏注意力的选择策略和内核，仅替换稀疏度分配逻辑，无需重训模型
### 关键结果
在Wan2.1、Wan2.2、HunyuanVideo三个主流视频DiT系列、6种稀疏注意力策略上测试，对比9种现有分配方案：
- 同等延迟下，在XAttention策略上比所有基线PSNR高1.53~7.31dB，在HunyuanVideo上最高提升11.8dB
- 集成到4个官方开源稀疏管线中，9个测试场景下6个领先、3个打平，最高在HunyuanVideo上同时实现PSNR提升3.38dB、端到端加速比从1.75×升至1.9×
- 离线校准仅需4个探测视频、8个校准prompt，单模型校准成本6~23GPU小时，更换延迟预算仅需4秒CPU重求解

稀疏资源分配不要只看局部指标，基于最终输出质量的离线预校准+全局优化，能在零额外推理开销、无训练的前提下大幅提升稀疏方案的性价比。
