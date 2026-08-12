---
title: 'ReRound: Reconstructive Rounding to Resolve Midpoint Ambiguity in Calibration-Free
  LLM Quantization'
title_zh: ReRound：解决无校准LLM量化中点歧义的重建舍入方法
authors:
- He-Yen Hsieh
- H. T. Kung
affiliations:
- Harvard University
arxiv_id: '2608.11045'
url: https://arxiv.org/abs/2608.11045
pdf_url: https://arxiv.org/pdf/2608.11045
published: '2026-08-11'
collected: '2026-08-12'
category: LLM
direction: LLM低比特量化 · 无校准PTQ
tags:
- LLM Quantization
- Post-Training Quantization
- Diffusion Model
- RTN
- Calibration-Free
- Low-bit Inference
one_liner: 基于LLM自身权重训练扩散先验引导中点舍入，无校准实现媲美校准类方法的3/4比特量化效果
practical_value: '- 业务侧部署1-3B小LLM做智能文案生成、Query理解、轻量Agent决策时，可直接用ReRound优化3/4比特量化精度，无需额外校准数据，不改变推理逻辑与性能开销

  - 「仅修改中点区域舍入规则+按矩阵奇异值匹配选最优量化结果」的思路可直接复用在现有小模型量化流程中，不需要修改原有量化的scale、zero point等参数，改造成本极低

  - 算力充足的场景下，可借鉴「用模型自身权重训练轻量扩散先验指导压缩优化」的思路，迁移到CTR模型、召回模型的低比特量化场景，降低压缩带来的精度损失'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有训练后量化（PTQ）的标准近邻舍入（RTN）在权重靠近量化区间中点时存在歧义，微小的距离差异就会决定舍入方向，大量这类歧义累加会显著降低3/4bit低比特量化后的模型精度；校准类量化方法需要额外的激活/文本标注数据，现有无校准方法的精度普遍偏低，难以满足小LLM部署的精度要求。

### 方法关键点
- 用目标LLM自身的64×64权重补丁训练条件扩散模型，生成连续的低比特权重重建结果，作为中点舍入的引导信号
- 设计位置相关的容忍度指标：仅对中点附近一定范围内的权重用重建结果指导舍入，远离中点的权重保持RTN不变，不修改原有量化的scale、zero point、分组大小等核心参数
- 生成多个不同容忍度的量化候选矩阵，选择反量化后前导奇异值与全精度权重最匹配的候选，全程无需任何校准数据

### 关键实验
在Gemma 2 2B、Qwen3 1.7B等8个1-3B小LLM上测试3/4bit权重-only量化，对比RTN、HQQ等无校准baseline：4bit量化下平均精度比RTN高0.2~1.3个点，3bit下高0.1~0.9个点，效果甚至超过需要校准数据的GPTQ、AdaRound等方法；仅修改不超过1%的RTN舍入结果，推理无额外开销，离线量化阶段单GPU处理1B模型仅需几十秒。

仅优化低比特量化的中点舍入规则，不需要校准数据、不改变推理逻辑，就能获得媲美校准类方法的精度收益，是小LLM端侧/离线部署降本的高性价比方案。
