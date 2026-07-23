---
title: Scaling Laws for Hypernetwork-Based Knowledge Injection in Large Language Models
title_zh: 大语言模型基于超网络的训练时知识注入缩放定律研究
authors:
- Nischay Dhankhar
- Dos Baha
- Abulhair Saparov
affiliations:
- Nace AI
- Purdue University
arxiv_id: '2607.19604'
url: https://arxiv.org/abs/2607.19604
pdf_url: https://arxiv.org/pdf/2607.19604
published: '2026-07-20'
collected: '2026-07-23'
category: LLM
direction: LLM知识注入 · 超网络缩放定律
tags:
- Hypernetwork
- Knowledge Injection
- LoRA
- Scaling Law
- OOD Generalization
one_liner: 首次系统揭示超网络知识注入的幂律缩放规律，OOD泛化显著优于LoRA、全量微调
practical_value: '- 垂类电商/广告LLM知识注入可优先选超网络方案，比LoRA/全量微调OOD泛化更强，适配用户多样化口语化、跨域query

  - 固定算力预算下优先提升目标LLM规模，其性能增益是缩放超网络宽/深度的2倍以上，ROI更高

  - 垂类Agent的知识注入可复用该架构，无需修改基础LLM参数，既避免灾难性遗忘，也支持快速切换领域

  - 若要提升对query改写、格式变化的鲁棒性，仅靠缩放模型增益有限，需搭配语义对齐的训练数据增强策略'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有LoRA、全量微调等训练时知识注入方案存在灾难性遗忘、OOD泛化差的问题，超网络作为知识注入新方案缺少系统的缩放规律指导，架构设计无据可依。

### 方法关键点
- 训练时超网络接收输入事实集，直接生成LoRA权重注入冻结的目标LLM，不修改基础模型参数
- 沿4个独立轴开展缩放实验：超网络宽度、超网络深度、目标LLM规模、单样本注入事实数
- 构建百万级多跳问答数据集MegaWikiQA，覆盖39个知识域，包含显式OOD评测集

### 关键结果
- 目标LLM规模缩放的性能增益最高，ID验证损失幂律指数为-0.226，是超网络宽/深度缩放的2倍以上
- 超网络OOD泛化缩放指数显著高于对比方案：OOD改写query指数-0.107 vs LoRA的-0.083、全量微调的-0.069；OOD多选指数-0.171 vs LoRA的-0.119、全量微调的-0.101，且优势随目标模型规模扩大持续增大
- 超网络深度和宽度缩放的性能增益相当，单样本注入事实数增加的增益最低

### 核心结论
训练时知识注入若需强泛化能力，超网络方案随模型规模扩大的优势会越来越明显，是比LoRA、全量微调更适合规模化落地的领域知识注入方案
