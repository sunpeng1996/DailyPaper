---
title: 'ARCHead: Activation-Metric Residual Correction for Large Language Model Output
  Heads'
title_zh: ARCHead：面向大语言模型输出头的激活度量残差校正量化方法
authors:
- Şuayp Talha Kocabay
- Talha Rüzgar Akkuş
- Kamer Ali Yuksel
affiliations:
- Independent Researcher
- aiXplain, Inc.
arxiv_id: '2608.02703'
url: https://arxiv.org/abs/2608.02703
pdf_url: https://arxiv.org/pdf/2608.02703
published: '2026-08-02'
collected: '2026-08-06'
category: LLM
direction: LLM量化 · LM-head存储压缩
tags:
- Quantization
- LM-Head
- Model Compression
- PTQ
- Low-Rank Approximation
one_liner: 提出专用于LLM输出头的压缩方法ARCHead，实现3.7-3.9倍存储压缩且精度损失可忽略
practical_value: '- 电商/推荐场景部署LLM（客服Agent、生成式推荐文案模型）时，可直接用ARCHead替换AWQ/bitsandbytes保留的BF16
  LM-head，在几乎不损失生成质量、不降低推理吞吐量的前提下，将LM-head存储压缩3.7-3.9倍，降低显存占用

  - 推荐系统大规模Embedding（商品/用户/Query Embedding）量化可借鉴核心思路：先做低秩+低比特基础压缩，再基于真实激活分布的度量空间做残差校正，比普通低比特量化的精度损失降低一个数量级

  - 大词表生成式推荐模型的输出层压缩可直接复用ARCHead实现，避免普通INT4量化导致的logit分布偏移，减少生成结果的错误率'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有主流PTQ方法（AWQ、GPTQ、bitsandbytes等）主要针对Transformer块做量化优化，普遍保留LM-head为BF16/FP16格式；对于大词表LLM，该输出头存储可达1GB以上，是量化后模型剩余最大稠密张量之一。直接对LM-head做普通INT4量化会严重扰动词表logit分布，导致精度大幅下降，缺少专门针对输出头的高效压缩方案。
### 方法关键点
- 基础结构采用量化低秩核心+分组INT4残差，替代原始稠密BF16矩阵，无任何稠密BF16参数残留
- 基于校准数据的隐藏状态计算激活度量变换，在该度量空间对核心残差做低秩SVD校正，优先修正高频激活方向的误差
- 可直接作为drop-in模块替换原有LM-head，与现有Transformer块量化方法完全兼容
### 关键结果
在WikiText-103数据集上验证，对比BF16、普通INT4、SVD+INT4、GPTQ头等量基线：
- Qwen3-8B上仅用25.6%的BF16头存储，相对PPL仅1.007，而同存储的普通INT4相对PPL达1.15
- 替换AWQ/bitsandbytes留下的BF16头仅增加0.006-0.007交叉熵，推理吞吐量变化小于2%
- 跨5个主流模型家族实现3.7-3.9倍的LM-head持久存储压缩
### 核心结论
LM-head量化不能只优化权重空间重构误差，优先修正高频激活方向的误差才能在高压缩比下几乎无损保留模型精度
