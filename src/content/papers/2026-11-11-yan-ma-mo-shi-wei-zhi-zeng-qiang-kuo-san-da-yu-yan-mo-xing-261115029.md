---
title: 'Mask-Pattern Position Augmentation: Training-Free Long-Context Extrapolation
  for Diffusion LLMs'
title_zh: 掩码模式位置增强：扩散大语言模型免训练长上下文外推方法
authors:
- Gaurav Sarkar
- Syed Affan Daimi
affiliations:
- International Institute of Information Technology, Hyderabad
arxiv_id: '2611.15029'
url: https://arxiv.org/abs/2611.15029
pdf_url: https://arxiv.org/pdf/2611.15029
published: '2026-11-11'
collected: '2026-11-13'
category: LLM
direction: 扩散LLM · 免训练长上下文外推
tags:
- Diffusion LLM
- Long Context Extrapolation
- RoPE
- Training-free
- Position Embedding
one_liner: 利用扩散LLM独有掩码密度信号做免训练位置增强，2倍上下文下困惑度降6.3倍无检索损失
practical_value: '- 业务中使用扩散LLM做生成式推荐文案、Query补全等场景时，可直接复用MPPA做免训练长窗口扩展，无需重训模型，落地成本极低

  - 针对RoPE插值导致的相位坍塌问题，可借鉴「结合任务特有动态信号加动态偏移」的思路：比如推荐长序列建模可结合用户点击/未点击的隐式掩码信号加偏移，提升精度

  - 该优化仅新增单步前缀求和的轻量计算，完全不影响推理吞吐，适配高并发的推荐/广告生成场景'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
扩散大语言模型（dLLM）采用双向注意力迭代解掩码生成，相比自回归模型更适配短序列批量生成、双向理解类场景，但RoPE位置编码限制其仅能在预训练固定窗口内推理；现有免训练长上下文外推方法直接移植自回归模型的NTK RoPE缩放逻辑，完全忽略dLLM独有、随解码步骤动态变化的掩码模式信号，浪费了天然优化抓手。

### 方法关键点
- 先对超出预训练窗口的位置做线性插值，映射到预训练窗口范围，保证RoPE角度分布符合预训练分布
- 每步解码时计算每个位置的前缀累积掩码密度，给插值后的位置加与掩码密度正相关的动态偏移，抵消插值导致的相邻位置相位坍塌问题
- 偏移量随解码推进、掩码减少自动衰减，后期精调阶段接近纯净插值位置，兼顾早期全局结构生成和后期局部精度
- 完全免训练，仅每步增加一次O(L)的前缀和计算，可直接替换位置ID作为模型输入

### 关键实验结果
基于LLaDA-8B-Instruct（预训练窗口4096）做2倍上下文（8192）实验，对比原生直接外推baseline：
- 8192长度下困惑度从19.51降至3.12，降幅达6.3倍，甚至低于模型在4096窗口内的困惑度
- passkey检索准确率保持100%，大海捞针（NIAH）准确率和原生解码持平，无检索精度损失

### 核心结论
不要直接把自回归LLM的优化方法照搬到扩散LLM，利用dLLM独有的动态掩码信号做适配，能以极低成本获得大幅性能提升。
