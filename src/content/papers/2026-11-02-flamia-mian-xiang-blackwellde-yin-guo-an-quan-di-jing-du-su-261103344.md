---
title: 'FLAMIA: FLAsh MIcroscaling Attention for Fast and Causally Safe Training on
  Blackwell'
title_zh: FLAMIA：面向Blackwell的因果安全低精度快速训练Attention内核
authors:
- Fedor Velikonivtsev
- Mikhail Koltakov
- Denis Kuznedelev
affiliations:
- Yandex Research
arxiv_id: '2611.03344'
url: https://arxiv.org/abs/2611.03344
pdf_url: https://arxiv.org/pdf/2611.03344
published: '2026-11-02'
collected: '2026-11-03'
category: Training
direction: 低精度Transformer Attention训练加速
tags:
- FlashAttention
- Quantization
- LLM Training
- Blackwell GPU
- FP8
one_liner: 针对Blackwell GPU设计低精度Attention核，训练加速最高1.42倍且无因果泄露
practical_value: '- 若团队采用NVIDIA Blackwell GPU训练LLM、生成式推荐或Agent相关模型，可直接接入开源FLAMIA内核，在几乎不损失效果的前提下获取最高1.42倍的Attention训练速度提升

  - 做低精度Attention量化时需规避因果泄露风险：放弃全局张量缩放，采用per-token/32-token局部块缩放+指数上取整策略，可在低开销下保证因果正确性

  - 低精度Attention训练需保证前后向数值一致性：反向重计算需复用前向的量化表示、分块策略、指数计算逻辑，不能仅依赖单步梯度余弦相似度判断训练稳定性

  - 处理电商用户行为序列、搜索query序列等变长数据时，可复用论文的packed布局+GPU端动态负载调度方案，无需padding对齐即可降低内存开销、提升计算吞吐'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
Transformer训练中Attention运算占比极高，NVIDIA Blackwell GPU的FP8/FP4张量核吞吐分别是BF16的2倍、4倍，但现有低精度Attention实现存在量化开销大、共享缩放因子导致因果信息泄露、前后向数值不一致引发训练不稳定、变长packed序列需重打包浪费资源等问题，无法充分释放硬件低比特算力。

### 方法关键点
- 双路径设计：提供MXFP8全8-bit训练路径，以及QK采用NVFP4、其余运算采用FP8的混合路径；token块缩放策略让8-bit量化表示可在矩阵转置下复用，减少重复量化开销
- 因果安全防护：所有缩放因子覆盖范围不超过32个连续token，缩放指数上取整避免数值溢出，对角tile采用per-key缩放，彻底阻断未来token通过量化缩放影响前序输出
- 前后向一致性对齐：反向重计算完全复用前向的量化表示、分块规则、指数计算逻辑，dS采用32×32块独立缩放减少小梯度下溢
- 原生支持packed变长序列：无需重打包或padding对齐，GPU端动态负载均衡调度适配长度不均的序列，降低内存开销

### 关键结果
在B200/B300 GPU上与FlashAttention-4、cuDNN、FlashInfer等SOTA基线对比，因果packed序列训练（含量化开销）MXFP8路径实现1.10-1.40×（B200）、1.06-1.42×（B300）的端到端加速；1B参数Llama风格模型预训练100B FineWeb-Edu token，损失仅比BF16基线高0.005-0.014，下游任务平均指标仅下降0.0018-0.0095，效果损失可忽略。

### 核心结论
低精度Attention的有效性不能仅通过单步输出/梯度余弦相似度判断，必须同时验证因果安全性、训练稳定性以及端到端任务表现
