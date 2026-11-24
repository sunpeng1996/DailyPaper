---
title: 'Look Back, Draft Ahead: Corrective Prefix Attention for Parallel Speculative
  Decoding'
title_zh: 基于修正前缀注意力的并行投机解码加速方法
authors:
- Mohammad Mahdi Moradi
- Ali Pourranjbar
- Zongzuo Wang
- Mingming Zhu
- Ben Feng
- Boxing Chen
affiliations:
- Huawei Technologies, Toronto Research Center, Ascend Team
arxiv_id: '2611.31112'
url: https://arxiv.org/abs/2611.31112
pdf_url: https://arxiv.org/pdf/2611.31112
published: '2026-11-23'
collected: '2026-11-24'
category: LLM
direction: LLM推理 · 投机解码加速
tags:
- Speculative Decoding
- LLM Inference
- Attention Mechanism
- Parallel Decoding
- Model Acceleration
one_liner: 提出修正前缀注意力CPA，提升并行投机解码接受率，无推理额外开销，最高加速3.37倍
practical_value: '- 电商客服Agent、生成式推荐文案生成等依赖LLM推理的业务可直接集成CPA到vLLM推理栈，无推理额外开销即可获得25%左右的解码速度提升，降低推理成本

  - 可借鉴无推理开销的自回归辅助损失设计：训练阶段额外增加干净前缀的下一词预测损失，本文中该方法在所有benchmark带来2-3%的性能提升，适合推荐query改写、商品文案生成等小模型微调场景

  - 固定候选短列表预计算两两交互的技巧可复用：生成式推荐的候选序列排序、多轮Agent回复候选重排等场景，可提前预计算所有候选对的交互得分，将序列决策的NN计算转为查表累加，大幅降低延迟'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
并行投机解码可一次生成整个token块，但块内只要出现1个早期错误token，后续所有token都会被目标模型拒绝，现有优化要么仅能感知局部相邻token，要么需要额外的神经计算开销，无法兼顾长上下文依赖和低推理延迟。

### 方法关键点
- 提出Corrective Prefix Attention (CPA)，每个候选token可关注块内所有更早的已选token，提前预计算固定top-K候选短列表的所有两两交互表，序列选择阶段仅需查表、累加和轻量打分，无需重复NN推理
- 训练阶段新增无推理开销的自回归辅助损失，让共享骨干在干净前缀上学习下一词预测，对齐验证阶段的真实场景，推理阶段无需新增任何计算步骤
- 仅增加<0.1%目标模型参数量的轻量选择器，无需修改推理架构

### 关键实验
在8个数学、代码、对话benchmark上，基于Qwen3-4B/8B目标模型在Ascend NPU测试，对比DFlash、DSpark、EAGLE-3等baseline：每轮验证比DSpark多提交13-15%的token，比DFlash多25-26%；贪心解码下平均加速3.35×（4B）、3.37×（8B），采样下平均加速2.86×，均为最优；接受长度提升不直接等于速度提升，当K>16、block size>16时，额外预计算开销会抵消接受长度的收益。

### 最值得记住的一句话
投机解码的额外上下文收益只有低于其带来的计算开销时，才能转化为实际的速度提升。
