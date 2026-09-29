---
title: 'MeqMuon: Matrix-Equilibrating Muon for LLM Pretraining'
title_zh: MeqMuon：面向大语言模型预训练的矩阵均衡Muon优化器
authors:
- Chang-Wei Shi
- Xu Wang
- Wu-Jun Li
affiliations:
- 南京大学计算机科学与技术学院、软件新技术国家重点实验室
arxiv_id: '2609.35701'
url: https://arxiv.org/abs/2609.35701
pdf_url: https://arxiv.org/pdf/2609.35701
published: '2026-09-28'
collected: '2026-09-29'
category: Training
direction: LLM预训练·优化器设计
tags:
- LLM Pretraining
- Optimizer
- Muon
- Memory Efficiency
- Convergence
one_liner: 提出自适应行列均衡的MeqMuon优化器，LLM预训练收敛优于基线且降低21.6%优化器内存
practical_value: '- 垂直领域小LLM（如电商导购LLM、推荐系统意图理解LLM）预训练可直接替换现有AdamW/Muon为MeqMuon，既降低预训练PPL提升模型效果，又降低优化器内存开销

  - 自适应行列归一化思路可迁移到推荐系统Embedding矩阵更新，缓解用户/商品Embedding行/列量级不均衡问题，提升Embedding质量

  - 移除AdamW二阶矩存储的设计可复用在大推荐模型离线训练优化中，减少GPU显存占用，支持更大batch或更大模型规模'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
LLM预训练规模持续增长，训练成本高企，现有Muon优化器仅采用行归一化无法适配更新矩阵的行/列不同不均衡模式，且依赖AdamW更新非隐藏层参数需存储二阶矩，内存开销大，收敛效率仍有提升空间。
### 方法关键点
1. 对隐藏层2D权重，先正交化动量矩阵，再根据行/列变异系数自适应选择行/列归一化，自动适配不同不均衡模式
2. 对词嵌入、LM头这类其余2D参数，采用行列双侧归一化替换AdamW更新，无需存储二阶矩
3. 对1D参数，采用全局RMS归一化动量进行更新
4. 完全移除所有AdamW二阶矩存储，大幅降低优化器状态内存占用
### 关键实验
在英文C4数据集上预训练Llama、SmolLM2、Qwen2三个系列共6个规模（60M~0.5B）模型，对比AdamW、SCALE、Muon、NorMuon基线：
- 所有模型规模下MeqMuon验证集PPL均为最低，相比Muon，Llama-350M PPL从16.04降至15.94，Qwen2-0.5B PPL从18.79降至18.63
- 相比Muon/NorMuon，MeqMuon在Qwen2-0.5B上优化器状态内存降低21.6%
### 核心结论
针对参数矩阵的不均衡模式做自适应归一化，是兼顾LLM训练收敛效果与内存效率的高性价比优化方向
