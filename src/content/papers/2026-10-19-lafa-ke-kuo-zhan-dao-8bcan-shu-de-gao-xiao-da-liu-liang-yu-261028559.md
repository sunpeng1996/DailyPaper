---
title: Large Flow Language Models
title_zh: Lafa：可扩展到8B参数的高效大流量语言模型
authors:
- Arnav Chavan
- Chanhyuk Lee
- Udbhav Bamba
- Jaehoon Yoo
- Seunghoon Hong
- Aditi Raghunathan
- Jinwoo Kim
affiliations:
- UC Berkeley
- Amazon
- KAIST
- Carnegie Mellon University
arxiv_id: '2610.28559'
url: https://arxiv.org/abs/2610.28559
pdf_url: https://arxiv.org/pdf/2610.28559
published: '2026-10-19'
collected: '2026-10-21'
category: LLM
direction: 大语言模型 · 流建模与推理加速
tags:
- FlowLM
- InferenceAcceleration
- SpeculativeDecoding
- LLM
- FlowMatching
one_liner: 适配预训练AR模型构建块级异步流大模型，不足30B token训练实现2.54倍推理吞吐量
practical_value: '- 可直接复用自投机解码框架，基于同一模型同时做流生成草稿+AR验证，无需额外小模型即可获得2倍以上吞吐量，适合推荐场景下的query改写、商品文案生成等低延迟需求

  - 预训练AR模型转流模型的适配方案可复用：块内双向注意力+固定词嵌入L2 norm仅训练方向+联合AR与去噪损失，仅需少量训练数据即可完成适配，降低大模型二次开发成本

  - 流训练会保留甚至增强原有AR模型的能力，做生成加速的同时不会损失原有LLM的指令遵循、推理能力，可直接用于Agent的工具调用、多轮对话等场景的提速'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前主流自回归（AR）大语言模型推理为逐token串行生成，延迟高成为落地瓶颈；多token预测、离散扩散等并行生成方案要么效果损失大，要么训练成本极高；连续流语言模型此前仅在小模型、简单任务上验证，缺乏十亿级参数规模下的高效训练、落地路径。

### 方法关键点
- 架构设计块级异步流模型Lafa：块间保持因果注意力，支持prefix KV cache复用；块内采用双向注意力+可学习的左偏异步token级时间调度，适配文本从左到右的生成特性
- 训练方案：基于预训练AR模型直接适配，新增adaLN做时间条件注入，固定词嵌入L2范数仅训练向量方向，联合前缀AR交叉熵、块去噪交叉熵、嵌入平方误差三类损失训练
- 推理方案：支持多步流解码、蒸馏后flow map少步/单步生成，同时利用训练保留的AR能力实现自投机解码：流生成块级草稿后做AR验证，输出与greedy AR完全一致

### 关键结果
在指令遵循、数学推理、代码生成6个基准测试上，Lafa 7B效果优于同规模AR SFT、MTP、离散扩散基线，自投机解码模式下实现**2.54倍**于同规模AR模型的吞吐量，效果无损失；8B规模模型效果与SOTA离散扩散模型Efficient-DLM相当，训练token量减少**18倍以上**。

### 核心结论
连续流建模可通过适配预训练AR模型实现低成本规模化落地，在不损失效果的前提下大幅提升LLM推理吞吐量，是比现有MTP、离散扩散更具性价比的并行生成方案。
