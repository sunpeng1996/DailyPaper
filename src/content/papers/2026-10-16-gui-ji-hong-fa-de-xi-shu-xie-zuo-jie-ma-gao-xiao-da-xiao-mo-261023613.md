---
title: Trajectory-Triggered Sparse Collaborative Decoding
title_zh: 轨迹触发的稀疏协作解码：高效大小模型推理协作方法
authors:
- Amit Ranjan Trivedi
- Sruthikesh Surineni
- Kyong Ho Lee
- Mohit Mittal
- Steven Li
- Rex Hill
affiliations:
- University of Illinois Chicago
- Meta
arxiv_id: '2610.23613'
url: https://arxiv.org/abs/2610.23613
pdf_url: https://arxiv.org/pdf/2610.23613
published: '2026-10-16'
collected: '2026-10-19'
category: LLM
direction: 大模型推理 · 大小模型协作解码
tags:
- Collaborative Decoding
- Speculative Decoding
- LLM Inference
- Trajectory Feature
- Failure Prediction
one_liner: 基于小模型生成轨迹特征预测失败点，按需调用大模型修正，大幅降低推理成本提升准确率
practical_value: '- 大小模型协作的Agent/生成式推荐场景可放弃局部不确定性触发逻辑，改用熵、NLL、logit margin的时序聚合特征做失败预测，AUC可从0.5提升至0.86，触发准确率大幅提升

  - 电商多步推理场景（复杂query解析、用户意图理解、智能客服生成）可复用该框架，仅在高风险节点调用大模型，比固定调度方案准确率高5~20pp，同时控制大模型调用成本

  - 落地可直接复用双门限规则：前128token失败预测AUC≥0.7、大模型单次干预token数≤纯大模型生成长度1.2倍时用闭环SCD，否则降级为级联路由或事后修正，避免负收益

  - 黑盒API大模型场景下该方法无需访问目标模型logit/隐状态，仅通过文本注入实现修正，落地成本远低于投机解码等需要白盒访问的方案'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有大小模型协作方案要么全程用大模型做token级验证（如投机解码）成本极高，要么固定调度调用大模型灵活性差，常用的局部不确定性信号（单token熵、NLL等）预测最终失败的AUC仅0.5~0.53，接近随机，无法准确判断何时需要大模型介入修正。

### 方法关键点
- 提取小模型生成过程中置信度轨迹的85维聚合特征：包含熵、NLL、logit margin、top-k概率的均值、极值、斜率、方差等时序统计量，训练轻量化逻辑回归预测器判断当前轨迹是否会最终失败
- 在线触发策略设置预热窗口、冷却周期、调用预算约束，触发后大模型仅生成有限长度的修正文本，直接追加到上下文后切回小模型继续生成，全程无需修改模型权重、logit或隐状态，完全兼容黑盒API大模型
- 提出双门限部署规则，满足规则时用闭环SCD，否则降级为级联路由或事后修正，规避负收益

### 关键实验
在GSM8K、MATH-500、StrategyQA三个数据集上对比7种baseline：GSM8K的5组大小模型对中，比最优固定调度SCD准确率高5.3~20.0pp，最多覆盖89%的小模型到纯大模型的准确率gap；StrategyQA上比最优固定调度高5.0~8.3pp；MATH-500上仅当早段预测AUC足够、大模型能力达标时获7.0~13.5pp收益。

> 最值得记住的一句话：多步推理场景下，小模型的局部不确定性几乎无法预测最终失败，轨迹级的置信度时序特征才是更可靠的干预触发信号
