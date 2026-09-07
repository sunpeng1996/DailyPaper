---
title: 'GUT: Quantifying and Optimizing the Reasoning Uncertainty of LLMs via Graph
  Complexity'
title_zh: GUT：基于图复杂度的LLM推理不确定性量化与优化方法
authors:
- Shuang Liang
- Xin-Yu Hu
- Xiang-Jun Ou
- Shao-Qun Zhang
affiliations:
- 南京大学计算机软件新技术国家重点实验室
- 南京大学智能科学与技术学院
arxiv_id: '2609.05284'
url: https://arxiv.org/abs/2609.05284
pdf_url: https://arxiv.org/pdf/2609.05284
published: '2026-09-04'
collected: '2026-09-07'
category: Reasoning
direction: LLM推理 · 不确定性量化与优化
tags:
- Reasoning Uncertainty
- Graph Complexity
- Uncertainty Quantification
- LLM Reasoning
- Reinforcement Learning
one_liner: 提出基于DAG图复杂度的LLM推理不确定性量化与优化框架，性能显著优于现有45种UQ方法
practical_value: '- 电商导购Agent、智能客服场景可复用GUT-Q方法评估推理链不确定性，提前拦截错误率高的回答，降低客诉

  - 生成式推荐场景中，用GUT-Q的DAG建模+NLI节点合并方法统计候选路径复杂度，可快速过滤低质量生成结果

  - 小模型推理能力优化时，可复用GUT-O思路，将负不确定性作为GRPO奖励信号，在不损失精度的前提下降低输出波动

  - 多轮对话、搜索query改写的不确定性评估，可直接复用GUT-Q的Top-d% token不确定性聚合策略，比单token熵更精准'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
现有LLM推理不确定性量化方法存在明显缺陷：自prompt评估受生成随机性影响误差大，序列建模方法忽略推理各步骤的潜在分支，无法精准刻画token分布、采样带来的固有不确定性；而电商导购Agent、智能客服、生成式推荐等业务场景对LLM输出的稳定性要求极高，亟需可解释、高精度的不确定性量化与优化方案。
### 方法关键点
- **GUT-Q量化模块**：先采样多条CoT链构建推理DAG，采用小参数NLI模型双向互验合并语义等价节点，避免自prompt的不确定性传播；计算token级4种不确定性（负最大概率、平均对数概率、熵、负token概率），按Top-d%/Head-d%/Tail-d%策略聚合为步骤级节点不确定性；最终通过3种图复杂度指标（不确定性加权宽度、加权高度、不确定性传播UP）量化整体推理不确定性。
- **GUT-O优化模块**：针对图复杂度的非可微问题，选择可微的Mean Token Log Probability（MTLP）作为不确定性代理，将负MTLP作为GRPO强化学习的奖励信号优化LLM参数，规避不可导问题实现端到端优化。
### 关键实验结果
在4个不同规模的Qwen3模型、5个覆盖数学推理、逻辑推理、QA的数据集上对比45种UQ基线方法，GUT-Q-UP平均比最优基线PRR高11.79%、AUROC高13.33%、AUPRC高9.66%；GUT-O平均降低推理不确定性13.95%，同时提升推理精度1.93%。
### 核心结论
将推理链的分支结构用DAG建模，结合小NLI模型做等价节点合并，是比传统序列建模、自prompt评估更精准的LLM推理不确定性量化路径。
