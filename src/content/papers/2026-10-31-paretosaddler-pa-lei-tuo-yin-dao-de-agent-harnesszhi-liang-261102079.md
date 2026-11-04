---
title: 'ParetoSaddler: Pareto-Guided Optimization of Agent Harnesses for Quality and
  Cost'
title_zh: ParetoSaddler：帕累托引导的Agent Harness质量成本双优框架
authors:
- Xingzhi Qian
- Sungho Park
- Rongyuan Tan
- Jianbo Yu
- Jue Zhang
- Lorenzo Cavallaro
- Menglin Xia
- Yanzhi Chen
- Xinnuo Xu
- Yu Kang
affiliations:
- Microsoft
- University College London
- Pohang University of Science and Technology
- Southern University of Science and Technology
- Southeast University
arxiv_id: '2611.02079'
url: https://arxiv.org/abs/2611.02079
pdf_url: https://arxiv.org/pdf/2611.02079
published: '2026-10-31'
collected: '2026-11-04'
category: Agent
direction: Agent Harness 质量成本双目标优化
tags:
- Agent Optimization
- Multi-Objective Optimization
- Pareto Optimization
- Bayesian Bootstrap
- Harness Optimization
one_liner: 结合帕累托优化与贝叶斯自助法，实现不修改模型权重的Agent Harness质量成本双提升
practical_value: '- 落地Agent系统（如电商导购Agent、客服Agent）时，可将中间迭代的候选晋升规则与最终上线的质量成本权衡解耦，避免过早淘汰暂时trade-off不佳但后续能带来更大提升的中间方案

  - 帕累托筛选+贝叶斯自助法的统计校验逻辑可直接复用，解决LLM执行随机性导致的效果评估波动问题，比如生成式推荐文案、Query改写的迭代优化中，用该方法判断方案提升是否可信，避免偶然波动误判

  - 打破「提升质量必然增加成本」的固有认知，LLM4Rec、生成式广告等场景优化时，可同时将token成本作为优化目标，反而可能得到比单优化质量更好的效果'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有Agent Harness自动优化方法大多仅优化任务质量，实际落地还需兼顾token成本等约束。若直接将最终部署的质量成本权衡规则用于中间迭代的候选筛选，会过早淘汰暂时trade-off不佳但后续可支撑更大提升的候选；再加上LLM执行本身存在随机性，单次或平均结果的评估可信度低，容易误判候选优劣。

### 方法关键点
- 核心架构分离**中间探索阶段的候选晋升**与**最终部署阶段的方案选择**，中间迭代仅要求候选在质量或成本任一维度有可信提升，无需满足最终上线的权衡要求
- 采用多次重复执行消除单次运行的随机性，每个候选在小批量验证集跑R次，得到质量、成本的多组观测值
- 引入贝叶斯自助法做统计校验，计算候选在任一维度有提升的统计置信度，仅当置信度超过阈值γ时才晋升到下一阶段做全量开发集评估
- 维护所有通过校验的候选池和帕累托前沿，迭代结束后再根据部署偏好（加权、约束、帕累托前沿）选择最终上线方案

### 关键实验
在ClawMark和GAIA2两个长序列Agent基准上测试，对比纯质量优化的AutoSaddler、多目标基线Meta-Harness：ClawMark上质量从70.86%提升到81.35%，单任务成本从$1.17降到$1.01；GAIA2上质量从56.22%提升到62.89%，单任务成本从$0.78降到$0.45，效果优于纯质量优化方案。

最值得记住的结论：多目标优化过程中，中间阶段放宽筛选规则保留更多单维度有提升的候选，反而能得到比单目标优化更优的最终结果
