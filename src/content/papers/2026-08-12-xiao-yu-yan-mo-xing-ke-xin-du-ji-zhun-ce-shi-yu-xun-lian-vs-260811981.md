---
title: 'Benchmarking Trustworthiness of SLMs: Pre-trained vs. Compressed'
title_zh: 小语言模型可信度基准测试：预训练原生 vs 压缩版本
authors:
- Haokun Lin
- Kaijie Zhu
- Haobo Xu
- Yichen Wu
- Zhichao Lu
- Qingfu Zhang
- Zhenan Sun
affiliations:
- 中国科学院自动化研究所
- 清华大学
- 哈佛医学院
- 香港城市大学
arxiv_id: '2608.11981'
url: https://arxiv.org/abs/2608.11981
pdf_url: https://arxiv.org/pdf/2608.11981
published: '2026-08-12'
collected: '2026-08-13'
category: LLM
direction: 小语言模型 · 可信度评估与压缩选型
tags:
- SLM
- Model Compression
- Quantization
- Pruning
- Trustworthiness
- Knowledge Distillation
one_liner: 系统评测不同构建路径SLM的可信度，给出低资源场景高可信SLM的落地选型方案
practical_value: '- 资源受限场景（端侧推荐Agent、离线RAG推理）优先选GPTQ 4-bit量化的稍大模型，比同部署效率的原生小SLM可信度高12%左右，延迟仅高1.2-1.5倍

  - 放弃用剪枝方式压缩LLM：剪枝会导致鲁棒性、公平性最多下降10%，远不如量化的保真效果

  - 要提升低资源部署模型的安全性，可基于高可信大模型做知识蒸馏，能进一步提升SLM全维度可信度约1.6%

  - 压缩选型优先级：量化（优先GPTQ>AWQ）> 原生预训练小SLM > 剪枝，3-8bit GPTQ量化对1.5B以上模型的可信度影响小于2%'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
SLM是端侧推荐、嵌入式Agent等低资源场景的核心选型，现有SLM构建分为两类：从头训练小参数模型、压缩大模型，但不同路径得到的SLM在公平性、鲁棒性、隐私、伦理等可信度维度的表现缺乏统一评测，落地易踩安全风险。

### 方法关键点
- 评测维度覆盖伦理、隐私、鲁棒性、公平性4个核心可信度方向，采用TrustLLM基准的配套评测数据集
- 对比三类SLM构建路径：原生预训练小模型（0.36B-1B参数）、剪枝压缩（SparseGPT、Wanda等方法）、量化压缩（GPTQ、AWQ等方法），额外验证知识蒸馏对可信度的增益
- 实验控制压缩后模型的参数规模、推理延迟对齐，确保不同路径的对比公平性

### 关键结果
- 评测数据集包含ETHICS、AdvGLUE、Social-Chem-101等权威可信度基准，基线覆盖MobiLlama、SmolLM2、Qwen2.5小参数版等主流原生SLM，以及剪枝/量化后的7B级大模型
- 剪枝后的7B模型可信度最多下降10%，半结构化2:4稀疏剪枝的退化更严重；GPTQ 4-bit量化的1.5B模型可信度比同部署效率的0.5B原生SLM高12%左右；3-8bit GPTQ量化对1.5B以上模型的可信度影响小于2%
- 基于7B高可信大模型蒸馏得到的3B模型，整体可信度比原生3B模型提升1.6%，全维度均有收益

**最值得记住的结论：构建低资源部署的高可信SLM，优先对高可信大模型做GPTQ量化，效果远好于直接使用从头训练的小参数模型**
