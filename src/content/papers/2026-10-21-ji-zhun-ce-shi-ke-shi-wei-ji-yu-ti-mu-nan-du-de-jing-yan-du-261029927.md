---
title: Your Benchmark Is an Empirical Measure Over Difficulty
title_zh: 基准测试可视为基于题目难度的经验度量体系
authors:
- Yifan Sun
- Naicheng Yu
- Jiawen Gong
- Jingyan Shen
- Huan Zhang
affiliations:
- University of Illinois Urbana-Champaign
- University of California San Diego
- New York University
arxiv_id: '2610.29927'
url: https://arxiv.org/abs/2610.29927
pdf_url: https://arxiv.org/pdf/2610.29927
published: '2026-10-21'
collected: '2026-10-23'
category: Eval
direction: 大模型基准测试评估与优化
tags:
- Benchmark
- Evaluation
- Difficulty Measurement
- BenchFill
- Test Generation
one_liner: 提出基于难度分布的基准评估框架，诊断两类失效模式，给出难度定向补全算法BenchFill
practical_value: '- 业务A/B测试/离线评估指标构造可借鉴难度分层思路，对核心难例（如推荐冷启动用户/长尾item匹配、Agent复杂任务执行）设置合理权重，避免简单case占比过高掩盖核心能力差异

  - 模型迭代的测试集优化可复用BenchFill的难度定向改写思路，自动补充当前测试集覆盖不足的难度区间case，更精准捕捉模型迭代的真实收益

  - LLM4Rec/Agent业务的能力评估可引入文中的度量偏差、覆盖缺口两个诊断指标，排查当前评估体系与真实业务场景难度分布的对齐度，避免评估结论误导迭代方向'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有基准测试仅通过平均得分评估模型表现，忽略题目难度分布的影响，易导致模型排名结论偏差、无法检测局部能力提升两类核心问题。
### 方法关键点
1. 提出基于难度分布的基准评估视角，形式化定义两类失效模式：基准难度分布与目标场景不匹配的「度量偏差」、难度区间覆盖不足的「覆盖缺口」；
2. 设计两个带理论保证的诊断指标，量化两类失效问题；
3. 提出BenchFill难度定向改写算法，自动补充缺口区间的测试用例。
### 关键结果
- 覆盖7个领域的25个主流基准测试分析显示：多数基准对特定难度区间加权过高，排名结论需谨慎解读；约30%难度区间存在覆盖缺口，大幅限制模型迭代收益的检测能力；
- BenchFill可降低40%以上的局部覆盖缺口。
