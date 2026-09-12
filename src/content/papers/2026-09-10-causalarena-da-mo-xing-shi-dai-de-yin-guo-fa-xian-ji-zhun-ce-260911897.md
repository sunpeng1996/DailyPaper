---
title: 'CausalArena: Benchmarking Causal Discovery in the Foundation Model Era'
title_zh: CausalArena：大模型时代的因果发现基准测试
authors:
- Zi-Rong Li
- Si-Yang Liu
- Tian-Zuo Wang
- Han-Jia Ye
affiliations:
- School of Artificial Intelligence, Nanjing University
arxiv_id: '2609.11897'
url: https://arxiv.org/abs/2609.11897
pdf_url: https://arxiv.org/pdf/2609.11897
published: '2026-09-10'
collected: '2026-09-12'
category: Eval
direction: 因果发现评测 · 大模型适配基准
tags:
- Causal Discovery
- Benchmark
- Foundation Model
- SCM
- Evaluation
one_liner: 推出统一可扩展的因果发现基准CausalArena，解决大模型时代因果发现评测不一致问题
practical_value: '- 做电商/推荐场景因果推断效果验证时，可参考CausalArena的多环境分层评测方案，避免单一数据集过拟合导致的上线效果不符合预期

  - 评估LLM的因果推理能力时，需额外校验预训练数据与测试任务的重叠度，排除数据泄露带来的效果虚高问题

  - 业务侧构建内部因果发现评测集时，可复用「合成SCM+语义可解释SCM+真实业务数据集」的三级结构，兼顾可控性和场景适配性'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有因果发现评测的SCM结构、生成机制、执行协议不统一，大模型时代预训练数据与测试集重叠问题进一步导致固定合成基准的结果可信度低，无法公平横向对比不同算法的真实因果发现能力。
### 方法关键点
CausalArena是遵循统一协议的可演化因果发现基准，覆盖四类测试集：①合成SCM，覆盖多样化结构和生成机制做可控评测；②语义可操作SCM，提供人类可审计的语义落地场景；③公式驱动SCM，测试明确科学机制下的发现能力；④公开真实数据集，做外部有效性校验。
### 关键结果
测试经典、神经网络、预训练三类因果发现方法，发现不同SCM族和协议下算法排名波动极大，单一基准的优异表现无法迁移到其他场景，验证了评测多样性、预训练-测试重叠是大模型时代因果评测的核心挑战。
