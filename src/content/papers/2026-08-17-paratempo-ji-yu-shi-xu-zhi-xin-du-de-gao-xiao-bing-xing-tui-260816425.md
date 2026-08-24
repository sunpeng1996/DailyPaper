---
title: 'ParaTempo: Efficient Parallel Reasoning via Temporal Confidence'
title_zh: ParaTempo：基于时序置信度的高效并行推理框架
authors:
- Xuteng Zhang
- Wenhao Zeng
- Xiaodong Gu
- Chao Hu
- Haotian Lin
- Yuling Shi
- Min Wang
- Beijun Shen
affiliations:
- Shanghai Jiao Tong University
- University of Pennsylvania
arxiv_id: '2608.16425'
url: https://arxiv.org/abs/2608.16425
pdf_url: https://arxiv.org/pdf/2608.16425
published: '2026-08-17'
collected: '2026-08-24'
category: Reasoning
direction: LLM并行推理 · 算力动态调度优化
tags:
- Parallel Reasoning
- Temporal Confidence
- Inference Efficiency
- Dynamic Resource Allocation
- Training-Free
one_liner: 无需训练的异步并行推理框架，通过分支级时序置信度动态调度算力，降推理成本保精度
practical_value: '- Agent多路径推理场景可直接复用temporal confidence设计：定期探测导购/决策Agent的中间答案分布，滑动窗口聚合后做低潜力分支剪枝、收敛分支提前终止，可降低复杂用户问题求解的推理成本

  - 生成式推荐多候选生成场景可迁移异步调度架构：对多分支生成的商品候选/推荐文案，动态回收低置信度分支算力，重分配给高潜力分支，平衡生成质量和响应耗时

  - 无需训练的自适应阈值校准方法可直接落地：先用少量warmup样本计算当前任务的剪枝分位数阈值，避免人工调参适配搜索query理解、文案生成等不同业务场景'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
并行推理通过多路径探索提升LLM复杂任务准确率与鲁棒性，但传统固定预算方案给所有分支分配相同算力，忽略推理进度异质性：已收敛分支生成冗余token，低潜力分支浪费算力。现有控制信号存在三类缺陷：最终答案共识滞后、token级置信度与最终答案关联性弱、单次中间探测噪声大，无法高效实现分支级动态调度。
### 方法关键点
- 提出**temporal confidence**信号：定期探测每个分支的中间答案分布，通过滑动窗口聚合最近W次探测结果，计算聚合分布的负熵指数，表征分支向固定答案收敛的程度，噪声远低于token级/单次探测信号
- 异步分支控制：先通过warmup阶段的前Nwarm次探测结果，用分位数校准当前任务的剪枝阈值，之后动态执行三类操作：低置信度分支剪枝、连续X次探测主导答案达标的分支提前退休（保留投票权停止生成）、释放的算力用于从高置信度分支fork新分支保持探索多样性
- 全局终止机制：当置信度加权的多分支投票中主导答案占比超过阈值时全局停止推理，最终结果由置信度加权投票得到
### 关键实验
在AIME2026、HMMT2025/2026、GPQA四个数理推理基准上测试，对比Self-Consistency、ESC、Parallel-Probe等基线：相比传统Self-Consistency，平均 latency 降低21.8%~32.2%，总生成token减少18.1%~30.3%，准确率仅下降1.1个百分点以内；对比最强基线Parallel-Probe，准确率提升3.8~3.9个百分点，latency最高降低10.6%。
### 核心结论
无需训练的分支级时序聚合置信度，是比token级/单次中间探测更稳定可靠的并行推理调度信号，可在几乎无损精度的前提下显著降低推理成本。
