---
title: 'D3D: Decoupled Diffusion Drafting for Asynchronous Speculative Decoding'
title_zh: D3D：面向异步投机解码的解耦扩散草稿生成方法
authors:
- Baoyou Chen
- Ruiqiao Mei
- Guancong Lin
- Tao Song
- Weihao Yuan
- Qun Liu
- Siyu Zhu
affiliations:
- Shanghai Innovation Institute
- Shanghai Academy of AI for Science
- Fudan University
- Nanjing University
- Huawei Technologies Co., Ltd.
arxiv_id: '2611.06425'
url: https://arxiv.org/abs/2611.06425
pdf_url: https://arxiv.org/pdf/2611.06425
published: '2026-11-03'
collected: '2026-11-06'
category: LLM
direction: LLM推理加速 · 投机解码
tags:
- Speculative Decoding
- Diffusion Model
- LLM Inference
- Layer Pruning
- Asynchronous Execution
one_liner: 提出无需依赖目标模型隐状态的独立扩散草稿生成器，实现高加速比的异步投机解码
practical_value: '- 业务中使用LLM做文案生成、Query理解、Agent推理时，可直接复用D3D的异步投机解码框架，在不改变输出分布的前提下提升推理速度，降低服务延迟和GPU成本

  - 做小模型蒸馏/裁剪时，可借鉴「按业务目标（而非模型精度）引导剪枝+蒸馏恢复」的思路：比如推荐场景的排序小模型，可按AUC/GMV影响程度剪枝，用蒸馏恢复效果，平衡精度和推理速度

  - 做扩散模型适配序列任务时，可复用「块级去噪+辅助自回归监督」的训练范式，提升扩散模型生成连续序列的质量，可迁移到生成式推荐的Item序列生成场景'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有基于扩散的并行投机解码方法需要依赖目标模型的最新隐状态生成候选token，导致草稿生成和验证必须串行执行，无法完全发挥并行生成的速度优势；同时草稿模型的冗余层会增加推理延迟，抵消候选接受长度提升带来的收益。

### 方法关键点
- 训练阶段：基于目标模型生成的回复数据，用「块级去噪损失+指数衰减位置权重+辅助自回归监督」训练独立的扩散草稿模型，无需依赖目标模型隐状态即可生成候选token块
- 剪枝阶段：按每层对候选接受长度的影响程度逐层剪枝，每次剪枝后用「调整后的教师分布蒸馏+原训练目标」做恢复训练，最小化接受长度损失的同时降低草稿模型延迟
- 推理阶段：在目标模型验证当前候选块的同时，草稿模型提前生成多种可能验证结果对应的后续候选块，验证完成后直接复用匹配的候选块，实现异步执行，完全隐藏草稿生成延迟

### 关键结果
在GSM8K、MATH、HumanEval、MT-Bench等7个基准上，以Qwen3-8B和Qwen3-32B为目标模型，对比DFlash、EAGLE-3、PARD-2等基线：剪去36层中的5层时仍保留99%以上的平均接受长度；平均解码加速比分别达到5.00×和5.71×，比基线最高提升12.6%和45.7%，GSM8K上Qwen3-32B最高加速7.48×。

最值得记住的一句话：投机解码的优化不能只关注候选接受长度，还要通过消除执行依赖、裁剪冗余计算实现延迟隐藏，才能获得真实的端到端速度提升。
