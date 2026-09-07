---
title: 'Compression Beyond the Uncompressed: A Two-Stage Training Recipe for Soft
  Context Compression in RAG'
title_zh: 超越未压缩性能的RAG软上下文压缩两阶段训练方案
authors:
- Shuyu Guo
- Shuo Zhang
- Zhaochun Ren
affiliations:
- Shandong University
- Bloomberg
- Leiden University
arxiv_id: '2609.05152'
url: https://arxiv.org/abs/2609.05152
pdf_url: https://arxiv.org/pdf/2609.05152
published: '2026-09-04'
collected: '2026-09-07'
category: RAG
direction: RAG优化 · 软上下文压缩
tags:
- RAG
- Soft Context Compression
- Knowledge Distillation
- Reinforcement Learning
- LoRA
- Inference Acceleration
one_liner: 提出两阶段训练的DEX-Comp软压缩方法，16倍压缩下效果超未压缩RAG，推理提速4-24倍
practical_value: '- 蒸馏阶段仅复用基准模型正确样本初始化的trick可直接迁移到电商导购RAG、用户行为序列压缩等蒸馏任务，避免模型学习错误行为

  - 难例定向强化学习的范式可复用在客服问答、商品属性召回等场景，在不增加推理成本的前提下突破现有基线性能上限

  - 压缩器与解码器用独立LoRA适配、软压缩embedding离线预存的工程设计，适合商品库等更新频率低的业务场景，可大幅降低推理延迟'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
RAG通过引入外部知识大幅提升LLM知识密集型任务表现，但过长的检索上下文会显著抬升推理延迟、挤占上下文窗口，现有软上下文压缩方法依赖对未压缩RAG的全量蒸馏，性能天然被基准模型上限约束，无法发挥连续embedding的高表征容量优势。

### 方法关键点
- 两阶段训练范式DEX-Comp：阶段1 Pure Distillation仅用未压缩RAG回答正确的样本做KL蒸馏，给压缩器和适配解码器做初始化，避免学习基准模型的错误行为
- 阶段2 Hard Exploration仅在未压缩RAG回答错误的样本上用GRPO做强化学习，引导模型探索适配压缩表征的计算模式，突破基准性能上限
- 工程设计：压缩器与解码器共用骨干LLM，用两个独立LoRA适配器训练，压缩后的文档embedding可离线预计算缓存，推理时直接调用

### 关键实验
在NQ、TriviaQA、HotpotQA等5个开放域QA基准，检索深度覆盖top5到top30，对比未压缩RAG、LLMLingua-2、PISCO等基线：16倍压缩率下，所有检索深度效果均超过未压缩RAG，平均CEM/LLM评测指标分别提升3.12%/2.53%；top30检索场景下推理提速23.73倍、显存降低4.02倍、计算量减少13.61倍，泛化性跨骨干模型、跨领域数据集均有效。

**最值得记住的一句话**：软上下文压缩的性能上限并不受限于未压缩RAG，通过定向蒸馏+难例探索的训练范式可在大幅压缩的同时实现效果反超
