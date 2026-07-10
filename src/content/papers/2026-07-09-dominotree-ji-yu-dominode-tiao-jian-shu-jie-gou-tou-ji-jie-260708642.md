---
title: 'DominoTree: Conditional Tree-Structured Drafting with Domino for Speculative
  Decoding'
title_zh: DominoTree：基于Domino的条件树结构投机解码加速方法
authors:
- Saw S. Lin
- Jyh-Shing Roger Jang
affiliations:
- National Taiwan University
arxiv_id: '2607.08642'
url: https://arxiv.org/abs/2607.08642
pdf_url: https://arxiv.org/pdf/2607.08642
published: '2026-07-09'
collected: '2026-07-10'
category: LLM
direction: LLM推理 · 投机解码加速
tags:
- Speculative Decoding
- LLM Inference
- Tree Drafting
- CUDA Graph
- Domino
one_liner: 训练免改的条件树投机解码方案，大幅提升LLM推理速度与每轮接受长度
practical_value: '- 部署LLM服务（如Agent调用、生成式推荐文案生成、Query改写）时，可直接复用DominoTree方案，无需修改模型权重，即可将Qwen3
  4B/8B模型推理提速最高6.6倍，降低推理成本

  - 工程上可借鉴「候选截断+CUDA Graph封装轻量计算」的优化思路，将序列生成任务中频繁的小算子调用开销降低30%以上，避免kernel launch overhead吃掉算法收益

  - 做路径依赖的序列生成优化（如多轮对话、长文案生成）时，可复用「共享主干计算+分支仅跑轻量修正网络」的架构思路，平衡生成质量与计算成本，避免分支重复跑主干的冗余开销'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有投机解码方法存在明显短板：自回归式候选生成单路径接受长度低、顺序计算开销大；块扩散式并行生成仅建模位置边际分布，无路径依赖导致接受率低；DDTree等树结构方法仅支持因式分解的边际分布，无法适配Domino新增的GRU条件修正结构，浪费了Domino的接受率优势。

### 方法关键点
- 完全复用开源Domino权重，无需额外训练：基于DDTree的最佳优先堆框架，将节点得分从位置边际概率替换为Domino的GRU条件修正概率，每条根到节点的路径单独计算修正得分
- 候选截断优化：每个深度仅预计算top-M个边际候选的修正参数，将每节点修正的计算量从全vocab降到M（实验取64），大幅降低计算开销
- GPU原生构建：将每节点的轻量修正计算封装为CUDA Graph，避免Python侧频繁kernel launch的开销，且和Python实现bit-identical，不改变接受率

### 关键实验
在Qwen3-4B/8B模型上，跨GSM8K、HumanEval、Alpaca等8个benchmark测试，对比DFlash、DDTree、CaDDTree、原生Domino基线：Qwen3-4B下最高比自回归解码提速6.6倍，平均每轮接受长度最高10.7个token，比原生Domino整体吞吐量提升9-10%，Alpaca场景最高提升22%；Qwen3-8B下T=0时比DDTree吞吐量提升24%，全温度下保持最高每轮接受长度。

### 最值得记住的一句话
块扩散并行主干+路径依赖轻量条件修正+树结构候选的组合，可在完全无损输出分布的前提下，实现LLM推理吞吐量的大幅提升，且无需修改原有模型权重。
