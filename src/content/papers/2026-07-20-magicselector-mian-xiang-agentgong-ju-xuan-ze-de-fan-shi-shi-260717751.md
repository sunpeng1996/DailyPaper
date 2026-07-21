---
title: 'MagicSelector: Joint Optimization for Agent Tool Selection via Counterfactual
  Decomposition and Progressive Reranking'
title_zh: MagicSelector：面向Agent工具选择的反事实分解与渐进重排序联合优化框架
authors:
- HONOR Agentic Search Team
- Zhengzong Chen
- Lei Tang
- Lijun Liu
- Chuandi Jiang
- Fan Yang
- Keyun Chu
- Chu Zhao
- Shihao Liu
- Minghang Li
affiliations:
- HONOR Agentic Search Team
arxiv_id: '2607.17751'
url: https://arxiv.org/abs/2607.17751
pdf_url: https://arxiv.org/pdf/2607.17751
published: '2026-07-20'
collected: '2026-07-21'
category: Agent
direction: Agent 工具调用 · 检索全链路优化
tags:
- Tool Selection
- Task Decomposition
- Counterfactual RL
- Progressive Reranking
- Dynamic Top-K
one_liner: 集成反事实任务分解、渐进重排序、动态TopK的Agent工具选择全链路方案 大幅提升检索精度与OOD泛化能力
practical_value: '- 自蒸馏硬负样本挖掘方法可直接复用在电商搜索/商品重排序、广告定向场景，无需额外人工标注，迭代挖掘当前模型判为高相关的负样本训练，大幅提升相似item的细粒度区分度，不增加线上推理成本

  - 双语义边界动态TopK策略可替换现有RAG、推荐系统的固定TopK截断逻辑，同时监控重排序得分悬崖、相邻item语义偏移两个信号，自适应调整截断数量，兼顾召回率与噪声过滤，降低上下文token消耗

  - 反事实任务分解的奖励设计可迁移至多意图query拆分、电商智能客服复杂咨询拆解场景，以分解后的下游任务增益作为核心奖励信号，避免模型学习伪相关的分解捷径，提升OOD场景泛化性'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
当前Agent工具检索面临三大瓶颈：多轮多意图用户指令直接匹配原子工具易出现严重语义失配，现有RL驱动的任务分解奖励缺乏因果归因，易学习伪相关导致OOD泛化差；传统重排序依赖随机负样本，相似功能工具区分度不足；固定TopK截断无法适配不同query复杂度，要么漏召核心工具，要么引入大量冗余噪声，浪费token且易引发上下文迷失。
### 方法关键点
1. 偏好引导的反事实任务分解：基于GRPO训练策略，融合两类奖励：反事实奖励量化任务分解前后的检索NDCG增益与工具覆盖度提升，偏好奖励由PRM模型评估分解结果的逻辑一致性，避免模型走重复分解等捷径。
2. 自蒸馏驱动的渐进重排序：先通过point-wise训练基础relevance打分模型，再用list-wise优化候选排序，迭代挖掘当前模型判为高得分的错误工具作为硬负样本重训，无需额外标注即可提升相似工具的细粒度区分能力。
3. 双语义边界感知动态TopK：分别计算重排序得分的最大落差点、相邻工具语义相似度的最大落差点，取两者最大值作为截断位置，兼顾核心工具召回与长尾噪声过滤。
### 关键结果
在ToolRet（44K工具）、自建移动端多轮交互基准MTDTool、ToolBench（1.6万API）三大基准上测试，全管线配置相比SOTA prompt类方法ReInvoke，ToolRet N@10提升12.84%，MTDTool N@10提升19.82%，ToolBench N@1提升24.4%，OOD场景下性能也显著领先，同时token效率更高。
### 核心结论
Agent工具检索的最优路径是任务分解、召回、重排序、截断的全链路联合优化，反事实因果奖励是打通上游规划与下游检索信号的高效方案。
