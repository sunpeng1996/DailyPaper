---
title: 'Mo'' Models, Mo'' Problems: How to best select model pools when designing
  Multi-Agent Systems'
title_zh: 多智能体系统模型池最优选择方法评估与设计建议
authors:
- Sara Vera Marjanović
- Jiacheng Xu
- Aleksandr Laptev
- Grigor Nalbandyan
- Erik Arakelyan
- Evelina Bakhaturina
affiliations:
- University of Copenhagen
- NVIDIA
arxiv_id: '2609.17306'
url: https://arxiv.org/abs/2609.17306
pdf_url: https://arxiv.org/pdf/2609.17306
published: '2026-09-15'
collected: '2026-09-16'
category: Agent
direction: 多智能体系统 · 模型池选择优化
tags:
- Multi-Agent
- Model Selection
- MAS
- LLM Ensemble
- Routing
one_liner: 系统评估8种多智能体模型池选择策略，证实同架构家族选模型性能最优
practical_value: '- 搭建业务多Agent系统时优先选择同架构家族的模型组成池子，避免盲目堆叠不同架构模型导致性能下降，比随机选模型效果更稳定

  - 对于路由类多Agent系统，优先选择正确答案多样性（IoU）高的模型组合，可获得比单一模型更高的性能收益

  - 不要迷信垂直领域微调的specialist模型，实测通用模型在垂直任务上的表现往往优于同参数的领域微调模型，可减少不必要的微调成本

  - 多数投票/LLM-as-Judge类多Agent系统要严格控制模型池规模，池内模型数量越多性能衰减越严重，优先控制k≤5'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
当前多Agent系统（MAS）被广泛用于复杂推理、任务调度等场景，但开源模型总量已接近300万款，现有研究几乎没有明确如何从海量模型中选择最优候选池，实践中盲目扩充模型池往往会引入大量噪声，导致MAS性能反而低于单SOTA模型，急需可落地的模型池选择标准。

### 方法关键点
- 覆盖2类主流MAS架构：生成前路由类、生成后聚合类（含多数投票、LLM-as-Judge两种工业界常用实现）
- 对比8种模型池选择策略：预评估维度（模型大小、架构家族、大模型推荐）、后评估维度（准确率、正确答案多样性IoU、错误多样性、准确率+多样性加权）
- 评测覆盖3个高难度科学推理基准：HLE、GPQA-Diamond、Frontier Science-Olympiad，共23款跨架构、参数范围2B~1.6T的模型参与测试

### 关键结果
- 同架构家族模型组成的MAS性能最优，在HLE数据集上比随机选模型的MAS相对性能高15%~22%，是唯一能稳定超过单SOTA模型的选择策略
- 模型池规模k≥10时，90%以上的异构MAS性能比池内最优单模型下降3%~11%，k越大衰减越严重
- 垂直领域微调模型的表现普遍弱于同参数的通用模型，在化学/物理子任务上通用Llama-3.1-8B比同底座的领域微调模型准确率高4%~7%

最值得记住的结论：多智能体系统的性能瓶颈往往不是模型多样性不够，而是模型池选择不当引入的噪声，盲目堆模型不如精准选择同架构小池
