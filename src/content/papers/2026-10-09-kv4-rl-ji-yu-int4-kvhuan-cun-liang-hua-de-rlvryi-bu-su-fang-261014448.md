---
title: 'KV4-RL: Unlocking Faster Asynchronous Rollouts for RLVR with INT4 KV Cache
  Quantization'
title_zh: KV4-RL：基于INT4 KV缓存量化的RLVR异步Rollout加速方法
authors:
- Sihwan Park
- Sung-Yub Kim
- Doohyuk Jang
- Eunho Yang
affiliations:
- KAIST
- NAVER Cloud
- AITRICS
arxiv_id: '2610.14448'
url: https://arxiv.org/abs/2610.14448
pdf_url: https://arxiv.org/pdf/2610.14448
published: '2026-10-09'
collected: '2026-10-15'
category: Training
direction: LLM RL训练 · KV缓存量化优化
tags:
- KV Cache
- Quantization
- GRPO
- Asynchronous Rollout
- RLVR
one_liner: 提出带选择性INT8保护的无校准INT4 KV缓存方案，不损失RL训练效果前提下实现最高1.97x Rollout加速
practical_value: '- 生成式推荐/Agent长文本生成的异步批处理场景，可复用选择性量化思路：绝大多数KV用INT4压缩，仅前16个attention
  sink token、最近128个上下文token用INT8存储，兼顾速度与生成质量

  - 做电商文案/商品语义生成的RL对齐训练时，可直接复用该方案加速rollout阶段，实测1.8x左右rollout加速下，最终模型效果损失<0.5pp，算力成本优化明显

  - 长上下文推理服务工程优化：高并发场景下KV浓度上升成为核心瓶颈，优先做KV缓存量化比权重量化能获得更高加速收益，该结论可直接复用'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
异步Rollout是RLVR训练提效的核心手段，可解决长文本生成的长尾利用率低问题，但会将KV处理集中到更少解码步，KV带宽成为新瓶颈；现有权重量化在高并发场景收益有限，直接使用INT4 KV缓存会引发采样器偏移，最终RL训练效果下降，仅靠TIS修正无法完全解决。
### 方法关键点
- 无校准INT4 KV量化：对每个token-head向量单独做仿射量化，配合Hadamard旋转降低离群值影响，无需离线校准即可适配动态更新的RL策略
- 选择性INT8保护机制：固定仅对前16个attention sink token、最近128个上下文token用INT8缓存，额外开销不随上下文长度增长，大幅降低采样器KL散度
- 优化注意力执行逻辑：INT4主缓存和INT8侧缓存分块读取，分别用对应精度算子处理后合并softmax结果，避免全缓存反量化开销
### 关键实验
基于Qwen3-4B/8B模型在数学推理数据集开展GRPO训练，对比BF16、KV8、纯INT4 KV基线：
- Qwen3-8B场景下，累计Rollout加速1.80×，全迭代加速1.27×，最后50轮Rollout加速达1.97×
- 最终6项任务平均准确率与BF16基线差距<0.5pp，纯INT4 KV方案则会掉点4.6pp
### 核心结论
异步高并发长文本生成场景下，KV缓存量化比权重量化的加速收益更高，配合少量关键位置的高精度保护，可在几乎不损失效果的前提下拿到接近2倍的生成速度提升
