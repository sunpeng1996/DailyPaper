---
title: 'PLoQ: A Prompt-Specific Low-Rank Basis for 4-bit Quantization of LLM Activations'
title_zh: PLoQ：面向LLM激活4位量化的Prompt特定低秩基方法
authors:
- Faraz Tahmasebi
- Michael Pellauer
- Hyoukjun Kwon
- Sitao Huang
affiliations:
- University of California, Irvine
- NVIDIA
arxiv_id: '2611.27092'
url: https://arxiv.org/abs/2611.27092
pdf_url: https://arxiv.org/pdf/2611.27092
published: '2026-11-20'
collected: '2026-11-23'
category: LLM
direction: LLM 低比特推理量化优化
tags:
- Quantization
- W4A4
- LLM Inference
- Low Rank
- KV Cache
one_liner: 提出Prompt自适应低秩分解，同等位宽下提升W4A4 LLM激活量化精度，推理开销极低
practical_value: '- 部署LLM驱动的Agent、生成式推荐、长query理解服务时，可直接复用PLoQ方案，显存占用不变的前提下比SOTA ResQ量化降低最多46%的perplexity损失，仅增加4%
  prefill、8% decoding延迟，性价比极高

  - PLoQ间隔分块采样估计序列主导特征方向的思路，可迁移到长序列用户行为建模、长会话推荐场景，用极低开销捕捉全序列核心特征，避免仅依赖开头特征的偏差

  - 无需修改预训练权重、仅在推理端用自适应低秩分解补偿量化误差的思路，可复用在推荐系统低精度排序模型部署中，无需重新训练即可降低量化精度损失'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有W4A4 LLM激活量化SOTA方案依赖离线校准的静态子空间保护主导特征方向，无法适配不同prompt的分布差异，且不能应用在FFN下投影输入等无权重可吸收变换的位置，导致4位量化精度损失大，限制低比特大模型落地。
### 方法关键点
- 无需修改任何预训练权重，prefill阶段通过随机测距法估计每个prompt专属的低秩主导激活方向基，解码阶段直接复用
- 将激活拆分为低秩主导分量、残差分量，分别用独立尺度量化，在GEMM内部自动恢复分量贡献，整体平均位宽保持和SOTA混合精度方案一致的4.2bit
- 采用间隔分块采样整段prompt估计低秩基，而非仅采样序列开头，提升长序列下的方向估计准确性
- 所有新增操作均与现有推理核融合，避免额外内存读写开销
### 关键实验
在1B~70B参数的Llama、Qwen共6个模型上测试，对比SOTA混合精度量化方案ResQ：同等位宽下2k上下文最多恢复46%的4位激活量化带来的perplexity损失，8k上下文最多恢复41%；Llama-3.1-8B 8k上下文下仅增加4% prefill延迟、8% decoding延迟；零-shot任务MMLU最高提升5.6个百分点。
### 核心结论
无需修改权重的prompt自适应低秩分解，可在极低开销下解决低比特激活量化的精度损失问题，尤其适配长序列大模型部署场景。
