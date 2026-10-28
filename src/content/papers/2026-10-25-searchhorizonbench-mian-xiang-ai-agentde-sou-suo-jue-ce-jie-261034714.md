---
title: 'SearchHorizonBench: A Benchmark for Search Value in AI Agents'
title_zh: SearchHorizonBench：面向AI Agent的搜索决策价值评估基准
authors:
- Jingjie Ning
- Xueqi Li
- Yibo Kong
affiliations:
- Carnegie Mellon University
arxiv_id: '2610.34714'
url: https://arxiv.org/abs/2610.34714
pdf_url: https://arxiv.org/pdf/2610.34714
published: '2026-10-25'
collected: '2026-10-28'
category: Agent
direction: Agent 搜索决策价值评估
tags:
- Agent
- Search Decision
- Benchmark
- RAG
- Utility Evaluation
one_liner: 提出带配对执行、成本核算的AI Agent搜索价值评估基准，量化搜索增益与决策效用
practical_value: '- 电商导购Agent/检索增强推荐系统可复用配对执行方案，量化每次RAG召回的边际增益，避免无效召回浪费算力

  - 搜索推荐的自适应触发策略可参考收益-成本拆解框架，按业务场景自定义token成本、正确答单价值，计算最优触发阈值

  - 可复用Brier误差分解方法，将预测误差拆解为成功率水平误差和增益误差，分别优化召回触发模型的不同能力'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有AI Agent的搜索决策大多仅关注回答正确率，未量化搜索的边际收益与对应token、时间成本，也缺乏统一基准评估「什么时候该搜索」的决策质量，无法平衡效果与成本。

### 方法关键点
- 采用配对执行设计：每个状态下同时执行Think（基于现有上下文回答）和Search（新增检索后回答）两条分支，各重复4次，消除生成噪声干扰，精准计算搜索真实增益
- 定义三层评估指标：动作成功率预测精度、搜索增益预测精度、决策效用（回答收益减去搜索、推理的token成本）
- 配套可复用的校准方法、误差拆解工具和冻结数据集拆分，支持不同搜索策略、模型的公平对比

### 关键结果
基准覆盖3168个多跳问答、自然查询类问题，累计45632次执行、8880次预测：
1. 历史校准方法将Brier误差降低16.2%，其中88.9%的改进来自任务先验
2. 搜索增益的标准差达21.4个百分点，不同query搜索价值差异极大，但现有历史estimator仅能解释不到2%的增益方差
3. 参考token成本下，基于增益信息的搜索选择策略比最优固定动作提升2.49个百分点的效用，增益信息贡献了99%以上的提升

**最值得记住的一句话**：Agent搜索决策的核心价值来自对query级搜索增益的精准预判，而非通用成本估计或任务先验。
