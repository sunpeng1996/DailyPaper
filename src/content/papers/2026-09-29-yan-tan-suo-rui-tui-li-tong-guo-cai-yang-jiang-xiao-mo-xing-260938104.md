---
title: 'Explore Broadly, Reason Sharply: Push Small Models toward the Frontier via
  Sampling'
title_zh: 广探索、锐推理：通过采样将小模型推理能力推至前沿水平
authors:
- Panagiotis Theodoropoulos
- Nan Jiang
- Xintong Duan
- Ali Hasan
- Yuriy Nevmyvaka
- Evangelos A. Theodorou
- Wei Deng
affiliations:
- Georgia Institute of Technology
- University of Texas at El Paso
- Morgan Stanley
arxiv_id: '2609.38104'
url: https://arxiv.org/abs/2609.38104
pdf_url: https://arxiv.org/pdf/2609.38104
published: '2026-09-29'
collected: '2026-09-30'
category: LLM
direction: LLM推理 · 无训练采样优化
tags:
- Power Sampling
- Parallel Tempering
- LLM Reasoning
- Inference Optimization
- MCMC
one_liner: 提出无需参数更新的并行功率调优采样方法，解决推理采样的探索利用权衡，小模型性能媲美前沿大模型
practical_value: '- 可复用PPT的多副本并行采样+交换框架，无需微调小模型即可提升电商/广告场景下LLM文案生成、多步推理选品的效果，避免RLHF的泛化退化问题

  - 固定horizon加EOS后padding修正截断偏差的trick可直接复用在各类变长序列生成任务中，解决现有MCMC采样生成内容过短、探索不足的问题

  - 等接受率的功率阶梯设计可指导生成式推荐场景下多温度采样的参数调优，相同算力预算下比单副本多步refinement准确率高2~3个百分点

  - 多副本采样的KV cache复用+批量推理优化可将多链运行overhead降至10%以内，业务落地时可有效控制推理成本'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
RL后训练提升LLM推理能力成本高、依赖外部奖励信号，还易出现泛化退化；推理端功率采样存在探索-利用权衡：sharpening过强易困在局部错误推理路径，过弱输出质量差，且传统实现存在截断偏差，导致生成内容偏短、探索受限。

### 方法关键点
- 运行多份不同sharpening等级的LLM副本：低功率副本探索多样化推理路径，高功率副本优化输出质量，副本间通过Metropolis-Hastings规则交换序列，无额外模型计算开销
- 采用固定horizon+EOS后padding的修正方案，彻底解决传统功率采样的结构性截断偏差，保证采样目标分布正确
- 设计等接受率功率阶梯，平衡相邻副本交换效率，避免通信瓶颈；副本数少的场景下采用有序相邻交换调度，效率是奇偶交换的2倍

### 关键实验结果
在数学、STEM、代码共6类基准上测试，对比标准解码、低温解码、单链功率采样、GRPO RL训练等baseline：
- Qwen3-8B上所有基准达到SOTA，比单链功率采样的LCB v5准确率高4.9pct，比GRPO高4.3pct
- Qwen3.5-9B上性能媲美GPT-5、Opus 4.5等前沿大模型，GPQA准确率85.9%、AIME 93.3%、LCB 84.9%，仅需1.72倍单链推理时间，交换开销占比<0.1%
- 相同算力下，比单链多步refinement在AIME、LCB等难任务上准确率高3~3.5pct，性能提升来自交换机制而非单纯增加副本数

最值得记住的结论：小模型的推理能力并未被完全释放，无需参数更新的针对性采样方法即可将其性能推至媲美前沿大模型的水平
