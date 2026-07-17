---
title: 'Bridge Evidence: Static Retrieval Utility Does Not Predict Causal Utility
  in Multi-Step Agentic Search'
title_zh: 桥接证据：多步智能体搜索中静态检索效用无法预测因果效用
authors:
- Debayan Mukhopadhyay
- Utshab Kumar Ghosh
- Shubham Chatterjee
affiliations:
- University of Calcutta
- Missouri University of Science and Technology
arxiv_id: '2607.15253'
url: https://arxiv.org/abs/2607.15253
pdf_url: https://arxiv.org/pdf/2607.15253
published: '2026-07-16'
collected: '2026-07-17'
category: Agent
direction: Agent 多步检索效用评估
tags:
- Agentic Search
- Counterfactual Evaluation
- Retrieval Utility
- Entity Relevance
- Multi-hop QA
one_liner: 通过反事实实验证实多步检索智能体中静态与因果检索效用几乎无关，发现约3成桥接证据
practical_value: '- 做电商多轮导购Agent、搜索主动交互Agent的RAG召回时，不要仅优化传统静态相关性（BM25、交叉编码器得分），需额外保留能输出后续检索关键实体的中间文档，避免过滤掉价值极高的桥接证据，比如用户问“夏天敏感肌可用的防晒”时，提到“敏感肌防晒核心成分”的文档即使没有直接推品，也需高优先级召回

  - 评估多步Agent检索系统效果，不要完全依赖单步静态RAG指标，可参考CTU的设计思路，加入下一步query检索质量、总交互轮数等长期收益指标，避免误判中间步骤的文档贡献

  - 多步检索的排序模型可引入OER（Observable Entity Relevance）特征，优先返回携带高区分度实体的文档，可直接提升Agent后续检索准确率、减少交互轮数，该特征仅需候选集统计量即可计算，工程落地成本低'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有检索系统的训练与评估均基于静态效用假设：单独将文档与问题交给无上下文的阅读器模型，以回答质量的提升程度为文档打分，nDCG、MAP、静态RAG评估指标均基于该假设。但该假设在多步推理的检索Agent场景下完全失效：文档的价值可能不在于直接回答当前问题，而在于为Agent提供后续检索的关键线索，此前缺乏对该效用gap的量化实证研究。

### 方法关键点
- 基于ReAct架构的Qwen2.5-7B-Instruct搭建检索Agent，在HotpotQA多跳问答数据集上开展实验
- 提出Counterfactual Trajectory Exploration（CTE）框架：对Agent每一步读取的文档，单独删除该文档后从该步重放轨迹，对比原轨迹得到Counterfactual Trajectory Utility（CTU），整合三个维度变化：最终答案质量、下一步query的检索质量、所需交互轮数
- 静态效用采用Static RAG Utility（SRU）衡量，即无上下文的独立阅读器仅用该文档回答问题的F1提升值
- 引入Observable Entity Relevance（OER）分析桥接文档的作用机制，即实体在相关/非相关文档中的分布区分度

### 关键结果
- 覆盖1000条HotpotQA样本的23322条文档观测显示，SRU与CTU的Spearman相关系数仅为-0.026，几乎统计独立
- 35.7%的文档属于桥接证据：静态效用极低但因果效用极高，删除后会导致Agent轨迹退化；用BM25+交叉编码器作为静态效用代理时，桥接证据占比仍达27.2%
- 高OER的区分度实体出现在Agent下一轮query中的概率是低OER实体的4.02倍，桥接文档的核心作用就是提供这类关键实体

最值得记住的一句话：多步检索Agent场景下，优化静态相关性完全不等于优化实际任务效果，约3成的关键中间文档会被传统检索指标完全漏判。
