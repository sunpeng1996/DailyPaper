---
title: 'HyFlash: A Prefix-Memory Prior for On-Device Speculative Decoding'
title_zh: HyFlash：面向端侧投机解码的前缀记忆先验轻量并行草稿器
authors:
- Jongwoo Ko
- Pashmina Cameron
affiliations:
- Microsoft Applied Sciences Group
arxiv_id: '2611.07263'
url: https://arxiv.org/abs/2611.07263
pdf_url: https://arxiv.org/pdf/2611.07263
published: '2026-11-05'
collected: '2026-11-06'
category: LLM
direction: LLM推理优化 · 端侧投机解码
tags:
- Speculative Decoding
- On-Device LLM
- Mamba-2
- KV Cache
- Inference Acceleration
one_liner: 提出混合局部注意力与固定大小循环记忆的并行草稿器，在端侧内存约束下提升投机解码效率与接受率
practical_value: '- 端侧电商Agent/智能导购场景可直接复用该架构，用2层浅草稿器实现15%+的LLM生成速度提升，内存开销仅增加5MiB，无需改动大模型权重

  - 长上下文个性化推荐、商品文案生成场景可借鉴局部注意力+固定大小SSM的混合设计，替代全量KV cache降低70%+的上下文存储开销，同时保留长程用户偏好建模能力

  - 低资源LLM部署可参考其4bit GPTQ量化方案，草稿器接受率损失小于1%的前提下，端侧推理速度再提升4%左右，适合边缘设备的广告文案、搜索推荐query生成场景'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
端侧部署LLM时内存资源极度紧张，16GB级设备扣除系统、大模型权重与KV cache开销后，留给投机解码草稿器的预算通常不足1GiB。现有并行草稿器要么采用全上下文注意力导致KV cache开销随序列长度线性增长，要么用窗口注意力丢失长程上下文信息，浅容量草稿器难以同时建模长程依赖和草稿位置间的细粒度交互，严重限制端侧LLM在长对话推荐、工具调用Agent等场景的生成效率。

### 方法关键点
- 引入前缀记忆先验，将长程上下文建模与局部/块内交互完全解耦：循环记忆仅从大模型已确认的输出特征更新，草稿生成阶段保持只读，避免未验证的投机内容污染历史状态
- 每层采用混合架构：滑动窗口注意力建模最近512个上下文token与草稿块内的双向交互，Mamba-2 SSM将全量历史上下文压缩为固定大小状态，两路特征经过归一化与加权融合后输出
- 内存开销恒定：KV cache仅存储窗口内内容，循环状态大小不随上下文长度增长，2层草稿器的上下文存储开销仅为5MiB

### 关键实验
基于Qwen3-4B、Phi-4-reasoning两个目标模型，对比DFlash、DSpark等SOTA并行草稿器，覆盖数学、代码、聊天、长上下文共10+基准测试。核心结果：
1. 通用场景下，对比DSpark，Qwen3-4B平均解码速度从1.95×提升至2.15×（+10%），Phi-4-14B从2.22×提升至2.58×（+16.2%）
2. 32K长上下文场景下，平均接受长度比滑动窗口注意力高20%以上，比全上下文注意力高1.5倍以上
3. 4bit GPTQ量化后，草稿器平均接受率仅下降0.8%，推理速度进一步提升4.3%

### 核心结论
小容量模型约束下，将长程记忆与局部交互解耦的归纳偏置，效率远高于盲目增加模型深度或KV cache容量
