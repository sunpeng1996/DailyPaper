---
title: Are Performance-Optimization Benchmarks Reliably Measuring Coding Agents?
title_zh: 《性能优化基准对编码Agent的度量可靠性研究》
authors:
- Zhi Chen
- Zhensu Sun
- Yuling Shi
- David Lo
- Lingxiao Jiang
affiliations:
- Singapore Management University
- Shanghai Jiao Tong University
arxiv_id: '2607.01211'
url: https://arxiv.org/abs/2607.01211
pdf_url: https://arxiv.org/pdf/2607.01211
published: '2026-06-30'
collected: '2026-07-04'
category: Eval
direction: 编码Agent · 基准评测可靠性分析
tags:
- Coding-Agent
- Benchmark
- Performance-Optimization
- Evaluation
- Leaderboard
one_liner: 审计三类代码性能优化基准的可靠性问题，揭示编码Agent排行榜评分偏差来源
practical_value: '- 做Agent能力评估时，需在多环境下回放基准任务验证有效性，避免单环境运行时波动导致的评估偏差

  - 自定义排行榜评分规则时，需控制长尾难例的权重占比，避免少数任务主导最终排名，降低评估可信度

  - 对公开榜单结果不要盲目信任，需拆分到子任务维度分析真实能力缺口，避免被聚合排名误导'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
当前代码库级性能优化基准（GSO、SWE-Perf、SWE-fficiency）的排行榜分数被广泛用作编码Agent能力进阶的核心依据，但评分易受运行时波动、基准专属规则、任务饱和等因素干扰，可靠性存疑。
### 方法关键点
1. 跨4类谷歌云机器回放3个基准共740个优化任务的官方参考补丁，校验跨环境有效性；
2. 对比公共提交在不同基准评分规则下的排名差异；
3. 统计有效任务的公共提交性能达标率。
### 关键结果
- 跨机器全回放满足原生有效性规则的任务占比：GSO 38.2%、SWE-Perf 7.9%、SWE-fficiency 82.5%；
- GSO与SWE-fficiency共有的8个公共提交中，28组两两对比有9组排名不一致，SWE-fficiency最难10个任务权重占比达58.5%~82.8%；
- 85.3%的有效任务已有公共提交性能持平/超过参考补丁，99.8%的任务提交优于未优化基线。
