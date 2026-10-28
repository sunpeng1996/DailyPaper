---
title: Can Test-Time Memory Evolution Outperform Test-Time Training for Scientific
  Discovery?
title_zh: 测试时记忆演化（TTME）：科学发现场景下优于测试时训练的高效适配方法
authors:
- Yepeng Liu
- Shengmai Chen
- Xuandong Zhao
- Chengzhi Liu
- Dawn Song
- Xin Eric Wang
- Yuheng Bu
affiliations:
- UC Santa Barbara
- UC Berkeley
arxiv_id: '2610.32046'
url: https://arxiv.org/abs/2610.32046
pdf_url: https://arxiv.org/pdf/2610.32046
published: '2026-10-22'
collected: '2026-10-28'
category: LLM
direction: LLM测试时自适应 · 非参数记忆优化
tags:
- Test-Time Adaptation
- External Memory
- LLM Efficiency
- Scientific Discovery
- Non-parametric Adaptation
one_liner: 提出固定权重的双模块测试时记忆演化方法，在科学发现任务上效果优于TTT且算力成本大幅降低
practical_value: '- 可将双记忆模块（Guideline+Strategy）迁移到搜索推荐Agent的在线迭代场景，无需在线微调LLM，将落地踩坑经验存入Guideline
  Memory、提分策略提炼到Strategy Memory，既节省在线微调算力，又可避免微调带来的效果波动

  - 固定权重的非参数测试时适配方案可复用在电商大促等流量峰值场景的生成式推荐、Query改写实时优化，无额外训练开销，响应延迟更低

  - 记忆的蒸馏-合并-淘汰机制（按重复度、新鲜度排序，淘汰stale条目）可直接用于业务RAG动态知识库更新，提升动态场景下RAG召回准确率，减少旧无效信息干扰'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有测试时训练（TTT）框架可让开源LLM在科学发现任务上超过闭源模型推理-only效果，但需要在线更新模型权重，算力开销极高，难以扩展到大模型场景，亟需更高效的测试时自适应方案。
### 方法关键点
- 提出即插即用的Test-Time Memory Evolution（TTME）方案，全程固定模型权重，仅通过更新外部记忆实现测试时自适应，无需任何权重更新操作
- 双互补记忆模块设计：①Guideline Memory：蒸馏执行、评估反馈得到通用操作指南，按重复出现次数、新鲜度动态更新淘汰，上限存储24条；②Strategy Memory：从能提升任务得分的修改中提炼可复用的算法策略，按语义相似性归为策略族存储
- 候选生成分支：α比例的候选直接基于任务和Guideline Memory生成，剩余比例基于当前父节点适配后的策略指导生成，实验中α取0.5
### 关键实验
在TTT-Discover、ThetaEvolve两个现有科学发现框架，Qwen3-8B、gpt-oss-120B等3个参数量8B~120B的模型，5个数学构造任务上验证，对比TTT基线：所有任务效果均超过TTT，FLOPs降低82.8%~84.6%，运行时间降低47.7%~58.4%。
### 核心结论
在迭代式探索类任务中，用结构化外部记忆沉淀经验替代在线权重更新，完全可以实现更好的效果和更低的算力开销
