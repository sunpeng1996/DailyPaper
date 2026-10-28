---
title: Where Should the Evaluation Budget Go in LLM-Driven Agent Scaffold Evolution?
title_zh: LLM驱动Agent工作流演化的评估预算分配优化方法
authors:
- Sichun Luo
- Yi Huang
- Mukai Li
- Haochen Luo
- Guanzhi Deng
- Haibo Wang
- Jian Xu
- Zefa Hu
- Junlan Feng
- Qi Liu
affiliations:
- The University of Hong Kong
- JIUTIAN Research, China Mobile
- City University of Hong Kong
- Carnegie Mellon University
- Tsinghua University
arxiv_id: '2610.37276'
url: https://arxiv.org/abs/2610.37276
pdf_url: https://arxiv.org/pdf/2610.37276
published: '2026-10-27'
collected: '2026-10-28'
category: Agent
direction: Agent工作流演化 · 评估资源分配
tags:
- LLM Agent
- Evaluation Allocation
- Scaffold Evolution
- Successive Halving
- Item Response Theory
one_liner: 提出EvalAlloc框架分离搜索与选优阶段的评估资源，用一半成本达到甚至超过全量评估性能
practical_value: '- 做Agent工作流迭代优化时，可拆分「搜索阶段反馈」和「最终最优方案选择」两个阶段分配评估资源，搜索阶段用稀疏反馈降本，最终阶段集中预算做高置信度排序，能大幅降本同时保效果

  - 多方案对比评估时，优先选择对性能区分度高的共享评估样本集，搭配固定校准的响应模型做评分校准，能大幅提升小样本下的方案排序准确率

  - 可复用warm-started successive halving策略，全量复用历史评估结果，仅补充缺失评估项，进一步降低最优方案选择的评估成本

  - 推荐系统召回/排序策略迭代的离线评估可复用该逻辑：策略搜索阶段用小样本集快速过滤，top策略池再用全量评估，提升迭代效率'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
LLM驱动Agent工作流演化依赖评估反馈引导候选迭代与最终选优，但全量评估所有候选的执行成本极高，现有方法未区分评估在「引导搜索」「最终选优」两个场景的差异化需求，难以实现成本与效果的最优平衡。
### 方法关键点
- 核心逻辑拆分评估的两类作用：搜索阶段仅需要低成本、可比的反馈引导迭代方向，最终选优阶段才需要高置信度结果区分头部候选
- 三阶段架构：1）核心校准：前10个候选全量评估，筛选高区分度的共享评估样本核心集，校准低秩MIRT响应模型并固定item参数；2）共享核心演化：后续候选仅在固定共享核心+小部分自适应样本上评估，用固定模型校准评分保证跨候选可比性；3）热启动选优：全量复用历史评估结果，用配对连续减半策略仅补充缺失评估，搭配重校准响应模型修正评分，筛选最优方案
### 关键结果
在HotpotQA、HoVer、DROP、IFBench四个基准，ShinkaEvolve、AdaEvolve两个演化框架下测试，EvalAlloc仅用约50%的全量评估cell成本，平均测试性能较全量评估高1.2%~1.9%，显著优于随机稀疏评估、级联评估等基线。
### 核心结论
Agent迭代优化中，评估资源不需要均匀分配给所有候选，区分搜索和选优的不同需求定向分配，能以极低的效果损耗换得翻倍的评估效率提升
