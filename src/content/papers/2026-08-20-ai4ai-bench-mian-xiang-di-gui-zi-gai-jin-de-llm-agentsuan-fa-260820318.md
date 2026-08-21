---
title: 'AI4AI-Bench: Benchmarking LLM Agents in Algorithmic Design for Recursive Self-Improvement'
title_zh: AI4AI-Bench：面向递归自改进的LLM Agent算法设计能力评测基准
authors:
- Yizhe Chi
- Wenyi Li
- Deyao Hong
- Xiaoqiu Wang
- Mingju Gao
- Kaisen Yang
- Bingxiang He
- Youjie Zheng
- Calvin Xiao
- Qinhuai Na
affiliations:
- Navers Lab
- Einsia.AI
- Tsinghua University
arxiv_id: '2608.20318'
url: https://arxiv.org/abs/2608.20318
pdf_url: https://arxiv.org/pdf/2608.20318
published: '2026-08-20'
collected: '2026-08-21'
category: Agent
direction: Agent 递归自改进能力评测
tags:
- Agent Benchmark
- Recursive Self-Improvement
- LLM Agent
- Training Algorithm
- RSI
one_liner: 首个隔离评测LLM Agent训练算法设计能力的基准，覆盖10类主流训练算法任务
practical_value: '- 可复用「4小时开发窗口+12小时独立重跑评估」的框架，评测内部Agent优化推荐系统训练流程的效果，避免过拟合代理指标

  - 优化Agent任务效果时可优先提升推理链长度/思考轮次，能显著提升Agent触碰核心算法逻辑的概率，ROI高于单纯加算力

  - 内部AI工程化流程可参考论文的变更分类规则，区分调参、流程改动和核心算法改动，更精准量化团队算法创新贡献'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
递归自改进（RSI）的复利效应核心来自训练算法层的优化，但现有相关基准大多聚焦数据调优、超参搜索、系统工程优化，无法隔离评测Agent对核心训练算法的设计改进能力，缺少统一标准衡量当前LLM Agent在该维度的真实水平。

### 方法关键点
- 覆盖10类主流训练算法家族的冻结仓库任务，包括SFT、GRPO、DPO、奖励建模、模型剪枝、权重平均等，每类任务配套不可修改的离线隐藏评估器
- 采用非对称评估协议：Agent仅能在4小时探索窗口内访问代理指标，提交的代码会在独立环境从零开始重跑最多12小时，用隐藏评估器打分，完全避免数据泄露
- 设计统一归一化评分体系：0分为无信息模型，0.1分为仓库原生算法基线，1.0分为任务理论最优值，跨任务得分可直接对比
- 对代码变更自动分类，明确区分「仅改动运行流程（调参、checkpoint策略、容量配置）」和「改动核心学习逻辑（损失、监督信号、更新规则、训练数据）」两类变更

### 关键结果
评测6款主流LLM系统的29种配置，整体平均得分0.166，最优系统平均得分仅0.250，距离理论最优值还有极大差距；超53%的提交仅改动运行流程，未触碰核心学习逻辑；触碰核心学习逻辑的提交平均得分0.226，显著高于仅改流程的提交的0.126；提升Agent推理努力程度可将触碰核心逻辑的提交占比从8%提升到64%，平均得分从0.094提升到0.196。

最值得记住的结论：当前LLM Agent的算法设计能力仅略优于现有开源基线，提升推理努力程度主要提升的是Agent触碰核心算法层的意愿，而非优化算法本身的能力。
