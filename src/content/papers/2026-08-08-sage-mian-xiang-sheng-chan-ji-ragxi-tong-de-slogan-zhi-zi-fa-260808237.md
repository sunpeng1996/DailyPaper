---
title: 'SAGE: SLO-Aware Adaptive Retrieval for Production RAG Systems'
title_zh: SAGE：面向生产级RAG系统的SLO感知自适应检索方法
authors:
- Muhammad Faizan Raza
- Shuo
- Yang
- Satish Mahadevan Srinivasan
affiliations:
- Pennsylvania State University
arxiv_id: '2608.08237'
url: https://arxiv.org/abs/2608.08237
pdf_url: https://arxiv.org/pdf/2608.08237
published: '2026-08-08'
collected: '2026-08-11'
category: RAG
direction: RAG · 生产级SLO优化
tags:
- RAG
- SLO
- Adaptive Retrieval
- Imitation Learning
- Production System
one_liner: 基于轻量检索特征与离线模仿学习动态调整RAG检索预算，大幅提升SLO合规率降低成本
practical_value: '- 电商导购/智能客服类RAG系统可直接复用自适应检索k策略：用探针检索的轻量特征（BM25/稠密得分分布、排名间隙、跨排序器一致性）做query难度预判，避免固定k的资源浪费与长尾超时

  - 生产落地可参考低成本训练范式：离线遍历检索预算得到每个query的最优k oracle标签，用RandomForest等轻量分类器学习映射，推理开销<1ms且无额外LLM调用

  - 跨场景迁移无需重训：策略仅依赖检索侧特征，更换LLM backbone、切换问答/商品检索场景时均无需重新训练SAGE策略，大幅降低迭代成本'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
生产级RAG系统受严格服务水平目标（SLO）约束，尾延迟、基础设施成本直接影响用户体验与运营支出。现有固定检索预算k的方案无法适配query难度异质性：简单事实类query过度检索浪费资源拉高尾延迟，复杂多跳/时序类query检索不足降低答案质量，运营商被迫在回答质量与SLO合规间做取舍；现有自适应检索方案多依赖额外LLM调用或复杂多步流程，未直接优化生产SLO目标，难以落地。

### 方法关键点
- 轻量嵌入现有混合RAG管线：无需修改现有检索、生成逻辑，无额外LLM调用，推理开销<1ms
- 特征选择：仅复用检索侧已有的轻量信号：BM25/稠密检索得分分布、topK排名间隙、稀疏-稠密排序一致性、query lexical特征
- 训练范式：离线模仿学习，先遍历全量候选预算k得到oracle标签（满足SLO前提下选最小k且回答质量最高），用RandomForest分类器学习特征到k的映射
- 校准机制：在验证集上调整策略输出温度，确保实际部署时满足目标SLO合规率

### 关键结果
在Natural Questions、HotpotQA、UnSeenTimeQA三个数据集，以及Llama、Qwen、Mistral、Gemma四个7-9B LLM上验证：
- 5s P95延迟SLO下，SLO合规率从最优固定基线k=20的30%提升至95%，P95 latency降低36%，检索成本降低51%，仅损失2个点Exact Match
- 单策略跨数据集/跨LLM零样本泛化，SLO合规率稳定提升45-52个点，无回答质量下降

### 核心结论
将RAG检索建模为单query资源分配问题，基于检索侧轻量特征做自适应决策，是兼顾质量、延迟、成本的生产级落地方案
