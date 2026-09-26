---
title: How Sensitive Are LLM Leaderboard Claims to Hidden Model Selection?
title_zh: LLM排行榜性能宣称对隐藏模型筛选的敏感度分析
authors:
- Chen Yang
- Xianyang Zhang
- Jun Chen
affiliations:
- Texas A&M University
- Mayo Clinic
arxiv_id: '2609.28177'
url: https://arxiv.org/abs/2609.28177
pdf_url: https://arxiv.org/pdf/2609.28177
published: '2026-09-23'
collected: '2026-09-26'
category: Eval
direction: LLM评估 · 排行榜可信度校验
tags:
- LLM Leaderboard
- Statistical Significance
- Model Evaluation
- Multiple Testing
- Benchmarking
one_liner: 量化LLM排行榜隐藏模型变体筛选对性能宣称统计有效性的影响，给出敏感度评估曲线
practical_value: '- 做算法迭代A/B测试时，可引入同类变体相关性参数校正多轮筛选带来的指标通胀，避免虚假显著性结论

  - 自建业务模型（如LLM RAG/生成式推荐排序模型）排行榜时，可复用敏感度曲线方法校验性能差的统计有效性，避免误判

  - 业务选型对比公开LLM/推荐SOTA模型时，对排行榜相邻名次的微小分差需保留判断，优先做业务场景实测验证'
score: 6
source: arxiv-stat.ML
depth: abstract
---

## 动机
LLM排行榜是当前模型性能的核心评判依据，但厂商普遍私下测试大量模型变体后选择最优提交，导致公布的性能差存在通胀，现有统计校验未考虑该隐藏筛选的影响，宣称可信度无法量化。
## 方法关键点
基于高斯margin模型推导敏感度曲线，以模型家族内部相关性下界为变量，计算给定公开性能差下可支撑的最大隐藏变体数量；明确相关性需匹配排名所用评分与采样模式，分别实测不同采样场景下的复合得分相关性。
## 关键结果
对Open LLM排行榜394个相邻排名的性能宣称审计显示，391个在未考虑筛选影响的前提下就缺乏统计支撑；剩余通过初步校验的宣称，其有效性也高度依赖隐藏模型家族的相关性假设，无需估计未观测的隐藏变体数量即可完成校验。
