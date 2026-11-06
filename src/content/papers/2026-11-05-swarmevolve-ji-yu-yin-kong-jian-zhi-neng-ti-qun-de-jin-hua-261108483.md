---
title: 'SwarmEvolve: Latent Agent Swarms for Evolutionary Discovery and Optimization'
title_zh: SwarmEvolve：基于隐空间智能体群的进化发现与优化框架
authors:
- Qile Jiang
- George Em Karniadakis
affiliations:
- Brown University
arxiv_id: '2611.08483'
url: https://arxiv.org/abs/2611.08483
pdf_url: https://arxiv.org/pdf/2611.08483
published: '2026-11-05'
collected: '2026-11-06'
category: Agent
direction: 多智能体 · 隐空间进化搜索优化
tags:
- MultiAgent
- Latent Reasoning
- KV Cache
- Evolutionary Search
- LLM
one_liner: 提出基于隐空间推理与KV缓存通信的低开销智能体群进化搜索框架，速度效果双超现有SOTA
practical_value: '- 复用「隐空间推理+KV缓存通信」的多智能体协作范式，替代传统文本交互模式，可直接降低电商推荐场景下多Agent召回/策略迭代模块的推理开销，吞吐量可提升数倍

  - 直接复用基于隐层向量余弦距离的新奇度过滤策略，无需额外调用Embedding模型或LLM判重，可优化推荐候选集去重、多智能体生成营销文案去重的全流程，节省额外算力开销

  - 可借鉴「功能分群+差异化分工」的智能体设计思路，适配电商推荐多目标优化场景：精调群优化爆款策略、融合群跨域兴趣拼接、探索群挖掘长尾需求、冷启动群覆盖新用户，平衡推荐的精度与多样性

  - 「小参LLM+大量低成本隐空间智能体」的架构，可替代高参大模型单模型推理方案，在同等算力预算下提升推荐系统的策略迭代效率，降低业务部署成本'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
现有LLM引导的进化搜索框架依赖智能体文本链思考+交互，推理成本高、速度慢，无法支撑大规模搜索需求，尤其小参数量模型效果远逊于前沿大模型，亟需低成本高吞吐的进化搜索方案。

### 方法关键点
- 智能体全部在隐空间完成推理，无需解码生成文本，每步推理仅需单位置前向传播，推理结果直接存储为KV缓存
- 智能体通过拼接KV缓存完成通信，无需编码/解码文本，配合RoPE旋转校正位置偏移
- 分10个功能明确的智能体群（4个精调群+3个融合群+2个探索群+1个冷启动群），每群45个智能体，基于隐层平均向量的余弦距离做新奇度过滤，保留30个差异最大的智能体的KV缓存喂给总结器生成最终方案
- 全程无需额外训练，基于预训练LLM的输入输出嵌入矩阵做岭回归得到隐空间映射矩阵即可实现隐推理

### 关键实验
在21个数学发现与科学计算问题上，对比OpenEvolve、ShinkaEvolve、CodeEvolve三个SOTA框架，用Qwen3 8B/14B/32B-FP8单GPU跑60分钟：
1. 每小时生成程序数是基线的5~13倍，Qwen3 8B版本生成734个，vs基线最高158个
2. 达到基线60分钟最优成绩的中位数仅需3~8分钟，比基线提速7~20倍
3. Qwen3 8B版本平均得分超过所有基线用Qwen3 32B-FP8的得分，3个任务效果超过AlphaEvolve用前沿大模型得到的结果

### 核心结论
大量低成本的隐空间小智能体协同，能以远低于单一大模型的算力成本，获得更好的进化搜索效果
