---
title: Selection-Aware Stress Testing for Interactive Agents
title_zh: 面向交互式Agent的选择感知压力测试框架
authors:
- Yang Xu
- Chenang Li
- Jiefu Zhang
- Haixiang Sun
- Zhou Li
- Vaneet Aggarwal
affiliations:
- Purdue University
- University of California, Irvine
arxiv_id: '2608.30916'
url: https://arxiv.org/abs/2608.30916
pdf_url: https://arxiv.org/pdf/2608.30916
published: '2026-08-31'
collected: '2026-09-01'
category: Agent
direction: Agent评估 · 鲁棒性压力测试
tags:
- Interactive Agent
- Evaluation
- Stress Testing
- Robustness
- Statistical Validation
one_liner: 提出选择感知语义压力测试SASST，解决交互式Agent评估的结论不可复现问题
practical_value: '- 上线Agent/生成式推荐工作流前可借鉴SASST的发现/确认集拆分逻辑，将开发集观测到的指标增益拿到独立验证集复现，避免把采样噪声当成真实收益上线踩坑

  - 做A/B实验/算法效果评估时，可复用其有效样本量(ESS)、密度比、稳定性校验逻辑，过滤掉样本量不足/分布偏移过大的子群结论

  - 对LLM4Rec/Agent推荐这类易过拟合benchmark的场景，可引入其多声明联合置信界方法，降低多指标/多子群分析的假阳性率'
score: 8
source: arxiv-stat.ML
depth: full_pdf
---

### 动机
当前交互式Agent评估普遍存在「先用同一基准选最优工作流，再挖掘该工作流表现弱势的任务子群」的流程缺陷，结论完全依赖同一数据集的结果，易把采样噪声误判为真实规律，导致开发集观测到的指标增益上线后消失，缺乏可复现的统计保障。

### 方法关键点
- 拆分任务集群为完全独立的发现集、确认集：发现集仅基于任务预执行特征（如目标长度、所需工具）学习重加权规则，规则完全冻结后才可访问确认集数据
- 内置四重校验：有效样本量(ESS)、密度比、分布偏移半径（KMS/MMD度量）、规则稳定性，过滤依赖少量任务、偏移过大、稳定性不足的规则，支持返回无有效结论的中立结果
- 采用多声明联合置信界做统计校验，理论上保证结论的条件渐近有效性

### 关键结果
- 模拟实验：任务数≥1000时，点估计覆盖率94.75~95.30%，接近预设95%置信水平；200个任务集群下，植入的脆弱点端到端检测率64.6%，假阳性率仅1.7~1.8%
- 真实Agent实验：基于τ-bench 80个任务、480轮交互，发现集观测到Qwen3-8B的Plan+Verifier比ReAct高3.75pp的增益，在确认集完全消失，两组实验均未得到可复现的工作流优势结论

> 值得记住的结论：Agent评估中开发集的指标增益有极大概率是过拟合的，未经过独立确认集验证的结论不能作为上线决策依据
