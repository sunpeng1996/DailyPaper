---
title: Kronecker Delta Rule for Long Context Linear Attention
title_zh: 基于克罗内克Delta规则的长上下文线性注意力架构KronLSTM
authors:
- Anamaria-Roberta Hartl
- Levente Zólyomi
- Michael List
- Günter Klambauer
- Sebastian Böck
- Sepp Hochreiter
affiliations:
- Institute for Machine Learning, Johannes Kepler University Linz
- NXAI GmbH, Linz
arxiv_id: '2610.26834'
url: https://arxiv.org/abs/2610.26834
pdf_url: https://arxiv.org/pdf/2610.26834
published: '2026-10-18'
collected: '2026-10-20'
category: LLM
direction: 长上下文大模型 · 线性注意力优化
tags:
- Linear-Attention
- Long-Context-LLM
- KronLSTM
- Associative-Memory
- Efficient-Inference
one_liner: 提出低干扰克罗内克Delta更新规则，推出稳定高效的长上下文线性注意力模型KronLSTM，性能超越现有同类方案
practical_value: '- 长上下文电商推荐/Agent场景下，KronLSTM可作为Transformer注意力层的drop-in替换，恒定内存占用+线性计算复杂度，适配万级长度的用户行为序列建模、多轮对话Agent记忆模块，推理延迟更低

  - 克罗内克Delta低干扰记忆更新规则可迁移到RAG系统的记忆写入逻辑，仅当新记忆的key、value同时与旧记忆重叠时才修改，大幅降低长会话下历史记忆的扰动率，提升用户偏好召回准确率

  - 训练吞吐量比同类Gated DeltaNet-2高11~18%，适合作为长序列垂域大模型的基座架构选型，降低电商/广告领域长文本、长行为序列预训练的算力成本'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有线性注意力方案存在两大痛点：DeltaNet类模型记忆更新时会干扰所有key重叠的历史存储，长上下文下信息衰减严重；xLSTM类模型依赖额外归一化/稳定器模块，高学习率下易出现梯度爆炸、训练不稳定。Transformer软注意力的O(n²)复杂度也无法适配万级以上长上下文场景的推理需求。
### 方法关键点
- 提出克罗内克Delta更新规则，仅沿当前key-value对对应的单一矩阵方向修改记忆，只有key、value同时与历史存储重叠时才会产生干扰，侵入性远低于传统Delta规则
- 设计KronLSTM架构，搭配向量遗忘门、erase门、write门三门控机制，数学上可证明记忆范数全局有界，无需额外稳定器/归一化状态，训练全程稳定
- 支持chunkwise并行训练，可直接替换Transformer中的注意力层，兼容现有训练框架
### 关键实验
1.5B参数模型预训练100B token，对比Mamba-3、Gated DeltaNet、Kimi Delta Attention等基线：纯线性模式下6个通用任务平均准确率达59.72，比最强基线高1.6个点，LAMBADA困惑度低至11.72；16k长上下文NIAH任务混合模式下平均准确率全任务领先；32k上下文扩展后仍保持性能优势，训练吞吐量比GDN-2高11~18%。
### 核心结论
线性注意力的记忆更新干扰是长上下文性能衰减的核心瓶颈，最小侵入式的定向更新规则可同时兼顾训练稳定性、推理效率与长上下文记忆能力
