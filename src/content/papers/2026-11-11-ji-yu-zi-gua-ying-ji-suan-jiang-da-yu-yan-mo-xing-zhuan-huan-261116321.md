---
title: From Large Language Models to Efficient System One Models via Adaptive Computation
title_zh: 基于自适应计算将大语言模型转换为高效System One决策模型
authors:
- Minh-Anh Nguyen
affiliations:
- Nanyang Technological University, Singapore
arxiv_id: '2611.16321'
url: https://arxiv.org/abs/2611.16321
pdf_url: https://arxiv.org/pdf/2611.16321
published: '2026-11-11'
collected: '2026-11-13'
category: Agent
direction: Agent 快速决策模块效率优化
tags:
- System1
- Adaptive Computation
- Early Exit
- Self-Distillation
- LLM Inference
one_liner: 提出NESTONE框架通过嵌套自蒸馏训练与隐状态早出门控，将LLM高效转换为多深度System One决策模型
practical_value: '- 电商/推荐Agent的快速决策场景（如用户意图识别、工具路由、低风险内容审核）可直接复用NESTONE的嵌套自蒸馏训练方案，一次训练得到多深度模型，无需单独训练小模型，节省训练成本，12层/16层浅层模型精度比单独训练高2.9/1.8个点

  - 推理侧可复用隐状态门控早出机制，基于输入难度动态分配计算量：简单请求走浅层出口可降低16%~27% latency，复杂请求走深层出口保精度，尤其适合大流量低延迟要求的推荐/广告请求预处理场景

  - 现有LLM微调的决策类任务可先做层重要性分析：决策信息基本集中在中间层，尾层6层左右可直接砍掉不损失精度，无需修改训练逻辑即可快速降低推理成本'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
LLM-based Agent中大量高频轻量决策（如工具选择、意图识别、安全审核）属于System One场景，现有方案微调LLM时保留全量backbone，所有请求都要跑完整层，延迟高；而直接截断backbone或单独训练小模型都会大幅掉精度，且小模型基本是大模型的退化版本，没有专属优化收益，亟需兼顾精度和效率的System One模型转换方案。

### 方法关键点
- 先做层归因分析：发现决策信息80%集中在中间层（Qwen3.5-4B的15-23层），最后6层可直接移除无精度损失；单独训练的小模型90%左右正确决策和全量模型重合，仅2-3个点的独特正确预测，几乎是全量模型的退化版本
- 提出NESTONE训练框架：嵌套多深度前缀子模型共享全量模型的最后2层和决策头，子模型同时用黄金标签和全量模型的输出做自蒸馏，一次训练得到多个不同深度的出口
- 推理侧加轻量门控：每个中间出口用logistic回归基于隐状态预测当前出口是否能输出正确结果，超过阈值则直接输出，否则继续跑更深层，无需重复计算

### 关键结果数字
基于Qwen3.5-4B在7个决策基准上测试：
1. 单NESTONE checkpoint的各深度出口均优于或平于单独训练的同深度模型，12层出口精度高2.9个点，16层高1.8个点，24层精度和32层全量模型仅差0.6个点，延迟降25%
2. 隐状态门控早出可在不损失96%大流量场景精度的前提下，简单请求平均层数降到20.2层，比固定24层出口降16%计算量，最高可降27%

**最值得记住的一句话**：System One类决策任务的信息集中在LLM中间层，无需全层推理，嵌套自蒸馏+隐状态早出是兼顾精度和效率的最优方案之一。
