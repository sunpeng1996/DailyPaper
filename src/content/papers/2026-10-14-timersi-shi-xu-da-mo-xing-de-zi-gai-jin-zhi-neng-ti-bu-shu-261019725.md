---
title: 'TimeRSI: Towards Self-Improved Agentic Deployment for Time-Series Foundation
  Models'
title_zh: TimeRSI：时序大模型的自改进智能体部署框架
authors:
- Haoxin Liu
- Deqing Fu
- Lucheng Fu
- Yiqiao Jin
- Rushi Qiang
- Harshavardhan Kamarthi
- B. Aditya Prakash
affiliations:
- Georgia Institute of Technology
- University of Southern California
- Samay AI
arxiv_id: '2610.19725'
url: https://arxiv.org/abs/2610.19725
pdf_url: https://arxiv.org/pdf/2610.19725
published: '2026-10-14'
collected: '2026-10-16'
category: Agent
direction: Agent · 时序大模型自改进部署
tags:
- Time-series Foundation Model
- Coding Agent
- Recursive Self-Improvement
- Pipeline Optimization
- Time-series Forecasting
one_liner: 通过编码智能体迭代优化时序大模型部署流水线，冻结权重即可提升跨任务预测表现
practical_value: '- 电商需求预测、库存调度、流量预测等时序场景可直接复用该框架，在不更新预训练时序大模型权重的前提下，通过智能体自动生成特征工程、后处理规则适配业务场景，节省人工调优成本

  - 「迭代优化候选策略+在线自适应选择」两阶段架构可迁移到生成式推荐prompt优化、召回策略迭代场景：先用历史数据完成候选策略效果验证，再在线上根据实时上下文选择最优策略，降低上线风险

  - 编码智能体操作空间设计可参考：限定仅修改预处理、特征工程、后处理三层，不动核心模型权重，既控制智能体操作边界避免故障，又能覆盖大部分业务适配需求'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
时序大模型（TSFM）零样本预测能力强，但业务落地需要针对场景做输入输出适配：直接推理无法利用领域知识，易出现系统性误差；人工定制部署pipeline依赖专家经验，成本高迭代慢。现有基于编码智能体的流水线优化方案未针对时序预测的周期性、分布漂移特性设计反馈迭代和动态选择机制，效果不稳定。

### 方法关键点
- 全程冻结TSFM权重，仅通过修改部署pipeline代码优化效果，核心分为两个阶段：
  1. 迭代pipeline优化：编码智能体基于任务描述、历史预测误差，迭代修改预处理、特征工程、上下文选择、后处理四层代码，在历史预测窗口验证效果，筛选top候选pipeline组成部署集；
  2. 自适应pipeline选择：每次预测时根据当前时序的趋势、波动等特征匹配历史相似窗口，选择加权历史误差最低的候选pipeline输出结果，预测完成后更新误差反馈库。

### 关键实验
覆盖TIME基准98个任务共11.1万预测实例、FEV-bench基准100个任务共23.5万预测实例，对比30+SOTA方案，跨6个点预测、概率预测指标全部排名第一；相比直接推理的TimesFM 3.0，TIME数据集MASE下降1.52%、CRPS下降1.61%，FEV-bench MASE Skill提升2.79个百分点、SQL Skill提升2.26个百分点；更换不同编码智能体、不同TSFM backbone均能获得稳定增益。

> 最值得记住的一句话：大模型落地的性能增益很多时候不需要调整核心权重，优化外层部署pipeline就能拿到可观收益，智能体是实现这类自动化优化的极佳载体
