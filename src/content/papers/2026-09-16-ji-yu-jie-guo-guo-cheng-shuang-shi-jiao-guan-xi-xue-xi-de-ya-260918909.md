---
title: 'Beyond Outcomes: Dual-View Relational Learning for Efficient Agent Benchmarking'
title_zh: 基于结果-过程双视角关系学习的高效Agent基准压缩方法
authors:
- Xinshuai Guo
- Junjie Wu
- Dolly Deng
- Yinghui Li
- Hai-Tao Zheng
- Suncong Zheng
- Maxm Pan
affiliations:
- Hunyuan Team, Tencent
- Tsinghua University
arxiv_id: '2609.18909'
url: https://arxiv.org/abs/2609.18909
pdf_url: https://arxiv.org/pdf/2609.18909
published: '2026-09-16'
collected: '2026-09-17'
category: Agent
direction: Agent性能评估 · 基准压缩
tags:
- Agent Evaluation
- Benchmark Compression
- Relational Learning
- Trajectory Analysis
- Process Mining
one_liner: 联合建模任务结果与执行过程关系实现24-40倍Agent基准评估压缩，同时提升预测精度与排序一致性
practical_value: '- 电商/导购/客服Agent迭代时可直接复用该方法的基准压缩逻辑，仅用20个左右核心任务即可完成评估，成本降低20倍以上，同时保证不同版本Agent的能力排序一致性

  - 评估Agent能力时可直接复用论文提出的6个通用过程特征，无需依赖业务定制逻辑即可区分结果相似但行为合理性差异大的Agent，优化迭代方向更明确

  - 小样本模型评估场景可复用straight-through hard Top-K选点+核岭回归的架构，比现有SOTA方法训练速度快4-8倍，适合业务快速迭代的高频评估需求'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
Agent基准评估需支持长链路推理、工具调用与环境交互，成本远高于普通LLM静态评估：例如Claude Opus 4.8跑通APEX-Agents全基准需花费1.09万美元，Gemini 3.5 Flash在10路并行下仍需2.7天。现有基准压缩方法仅建模任务最终得分的冗余性，无法区分结果相同但执行过程差异极大的Agent，压缩后子集的预测精度与排序一致性均不足。

### 方法关键点
- 从5类主流Agent基准的大规模轨迹中筛选出6个通用、可自动提取的过程特征（Agent步数、工具失败率、工具类别熵、验证工具占比、写操作执行率、读写验证闭环率），与最终性能强相关且语义冗余低
- 提出DualViewEval端到端框架，同时建模任务维度的结果关系矩阵与过程行为关系矩阵，自适应加权融合后通过核岭回归预测全基准得分
- 采用straight-through hard Top-K门控实现精确大小的子集选择，训练时用分数误差+排序损失联合优化，保证子集同时满足得分预测准、Agent能力排序一致的要求
- 采用交叉折训练避免自预测偏差，验证阶段按MAE与排序误差的排名和选择最优checkpoint，无额外超参调优成本

### 关键结果
在BFCL、τ²-Bench、Terminal-Bench 2、SWE-bench Verified、APEX-Agents 5个主流Agent基准上对比5个SOTA基线，仅用20个任务即可实现24×-40×评估压缩，MAE比最强基线低14.5%-28.2%，Kendall's τ最高提升7.2%，训练速度比SparseEval快4.2×-8.3×，仅用20%的训练Agent数据仍能保持明显优势。

> 最值得记住的结论：Agent能力评估不能只看最终结果，执行过程的行为特征包含大量互补信息，兼顾二者可以用极低的成本获得更可靠的评估结果
