---
title: 'DecompRL: Solving Harder Problems by Learning Modular Code Generation'
title_zh: DecompRL：基于模块化代码生成学习解决更难的任务
authors:
- Juliette Decugis
- Fabian Gloeckle
- Francis Bach
- Taco Cohen
- Gabriel Synnaeve
affiliations:
- Meta FAIR
- Inria
- École Normale Supérieure
- CERMICS
- École des Ponts ParisTech
arxiv_id: '2607.02390'
url: https://arxiv.org/abs/2607.02390
pdf_url: https://arxiv.org/pdf/2607.02390
published: '2026-07-02'
collected: '2026-07-03'
category: MultiAgent
direction: 多Agent RL · 模块化任务生成优化
tags:
- Reinforcement Learning
- Modular Generation
- Multi-Agent RL
- LLM Training
- Cost Optimization
one_liner: 提出DecompRL多Agent RL框架，训练LLM生成模块化代码，降GPU成本50倍，高token预算下超现有基线
practical_value: '- 复杂Agent任务可参考「任务拆解+模块重组」范式，比如将电商大促活动页生成拆为选品、文案、布局三个独立模块，生成多版本后组合穷举候选，用规则/轻量模型校验替代反复LLM推理，可降低GPU成本最高一个数量级

  - logmeanexp平滑奖励函数可直接迁移到推荐系统RL排序、多轮对话Agent的多目标优化场景，解决高pass@k下奖励稀疏、梯度消失问题，平衡探索与利用

  - 多模块协同LLM训练可复用「分阶段顺序训练+留一基线credit分配」方案，避免多策略联合训练的熵坍缩、奖励崩溃问题，提升训练稳定性'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有LLM解决复杂问题的两类主流方案均存在瓶颈：重复采样的GPU成本随尝试次数线性增长，RL优化单样本准确率会损失采样多样性，当基础策略生成正确解的概率接近0时，两类方案均无法突破搜索空间限制，亟需将GPU密集的生成瓶颈转移到低成本CPU计算上。
### 方法关键点
- 分层生成范式：训练两个合作策略，分解策略将复杂问题拆为n个独立子函数（带明确签名和docstring），实现策略为每个子函数生成k个独立实现，组合后最多得到k^n个候选解，GPU推理成本仅为k*n tokens
- RL优化设计：采用logmeanexp奖励函数平滑插值平均与最大奖励，适配高pass@k优化目标，平衡探索与利用，避免奖励稀疏导致的梯度消失
- 训练机制：分阶段顺序训练，先固定实现策略训练30k步分解策略，再固定分解策略训练30k步实现策略，搭配留一基线计算优势，降低多策略协同的梯度方差，解决credit分配问题
### 关键实验结果
在CodeContest、LiveCodeBench数据集上，基于Qwen 2.5 7B、Llama 3.1 8B、Code World Model 32B验证，对比GRPO、pass@8训练、SPO等基线：500k token预算下solve rate达0.48，超基线2个百分点；同等512个候选解评估量下，GPU token生成量降低~50倍；超过10^5 tokens/问题的高预算场景下，性能全面超越所有标准RL基线，可覆盖普通生成无法解决的难任务。

**最值得记住的结论**：只要任务可分层拆解、验证成本远低于生成成本，就可以通过模块化重组将GPU推理瓶颈转移到CPU，用极低边际成本拓展大模型的问题解决边界。
