---
title: 'More Correct Mass, Worse Answers: Why Power Sampling Can Fail and How to Fix
  It'
title_zh: Power采样失效机制诊断与支持保留的推理优化修复方法
authors:
- Haohui Yang
- Jiaxing Sun
- Xiujun Ma
affiliations:
- Peking University
arxiv_id: '2608.14420'
url: https://arxiv.org/abs/2608.14420
pdf_url: https://arxiv.org/pdf/2608.14420
published: '2026-08-14'
collected: '2026-08-17'
category: Reasoning
direction: LLM推理 · 采样优化 · 多轨迹聚合
tags:
- Power Sampling
- Self-Consistency
- LLM Reasoning
- Multi-Trajectory Aggregation
- Distribution Sharpening
one_liner: 定位Power采样多轨迹聚合失效的两大根因，提出相对秩SoftSat修复方法消除精度大幅衰退
practical_value: '- 电商Agent多路径推理（复杂用户咨询多答案聚合、推荐理由多候选投票）场景避免直接使用固定指数Power采样，防止高概率错误路径压制多条低概率正确路径导致决策准确率下降

  - 多候选生成+聚合场景（搜索Query改写排序、商品文案多候选选优）可直接复用Relative-Rank SoftSat加权方案，仅对base生成的候选池按内部概率相对秩做饱和加权，无额外推理成本即可提升聚合效果

  - 评估多采样优化方案效果不能仅参考pass@k，需同时关注答案级margin和不同问题下分布变形的一致性，避免出现部分场景效果好、部分场景大幅衰退的不稳定问题'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
Power采样是无验证器的推理时优化方法，可将概率权重向模型认为更可靠的完整生成轨迹倾斜，原本被认为是多采样推理的通用前端，但实际应用中出现正确轨迹总占比提升、多轨迹聚合后最终准确率反而下降的悖论，最大降幅可达18.5pp，现有研究仅关注单样本准确率和pass@k，未考虑下游聚合对分布支撑的要求。

### 方法关键点
- 定位两大失效根因：覆盖率失配（全局锐化让少量高概率错误路径吸收过多权重，压制多条中等概率正确路径，即便pass@k高也会导致聚合错误）；剂量失配（固定指数对不同问题的分布变形程度差异极大，部分问题出现分布接近坍塌的情况）
- 提出Relative-Rank SoftSat方案：将原始绝对对数似然替换为同问题内的相对秩，解决剂量失配；对高秩轨迹的加权增益做饱和截断，避免少数路径权重过高，保留多路径支撑
- 工程优化：无需多次运行Power采样，直接对base生成的N条轨迹做重要性加权聚合，和原生自洽性推理计算成本完全一致，无额外模型调用

### 关键结果
在BigCodeBench、LiveAoPSBench、PHYSICS三个推理基准，Nemotron-4B、Qwen3.5-9B、Ministral-8B三个模型上测试，固定指数Power采样在7/9的场景下精度下降，最大降幅18.474pp；SoftSat修复后消除所有大幅衰退，在5/9场景下精度优于原生均匀自洽性，最大增益1.491pp，最大衰退仅1.004pp；和直接运行Power-SMC相比，加权实现的决策一致性达99.55%，推理速度提升7.42倍。

最值得记住的结论：锐化后的分布不仅要通过单轨迹质量和pass@k评估，更要保留下游决策规则所需的支撑结构，才不会出现单路径质量提升但多路径聚合效果下降的悖论。
