---
title: LongCat-DeepResearch Technical Report
title_zh: 美团LongCat-DeepResearch 多智能体深度研究系统技术报告
authors:
- Meituan LongCat Team
- He Zhu
- Yue Xu
- Wanli Wu
- Haolin Ren
- Yuxin Bian
- Jiarui Zhao
- Rongzhi Zhang
- Quanchi Weng
- Jinghao Cui
affiliations:
- Meituan LongCat Team
arxiv_id: '2609.36071'
url: https://arxiv.org/abs/2609.36071
pdf_url: https://arxiv.org/pdf/2609.36071
published: '2026-09-27'
collected: '2026-09-30'
category: MultiAgent
direction: 多智能体协作 · 深度研究报告生成
tags:
- MultiAgent
- AgentWorkflow
- LongFormGeneration
- ResearchAgent
- Benchmark
one_liner: 提出基于ResearchSpec的分层多智能体深度研究工作流，效果优于主流同类型系统
practical_value: '- 可复用「全局规划→并行子任务执行→全局校验+局部修订」的分层工作流架构，适配电商大促调研、商品卖点挖掘、多模块活动文案生成等场景，减少全文重写的计算成本

  - 参考ResearchSpec设计，将复杂Agent任务提前拆解为带唯一ID、明确范围、证据要求的可执行子任务，校验通过后再下发，大幅降低后续执行的冲突率

  - 沿用其按工作流阶段收集轨迹数据的方案，针对规划、执行、修订各环节分别标注训练数据，可低成本优化Agent各模块能力，适配业务定制需求'
score: 9
source: huggingface-daily
depth: full_pdf
---

### 动机
现有深度研究Agent通常耦合推理、检索、起草流程，或依赖迭代的完整报告引导后续步骤，存在上下文资源占用过高、早期结论锚定调研方向、重复全文重写成本高三大痛点，无法兼顾全局研究方向对齐与局部深度调研的需求。
### 方法关键点
- 三阶段分层多智能体工作流：①规划阶段：多规划Agent并行检索探索，经合并、补漏、修订生成固定ResearchSpec，明确各章节的范围、研究问题、证据要求、唯一ID；②执行阶段：各研究Agent仅接收对应章节任务，独立检索取证生成带引用的章节内容，并行执行互不干扰；③修订阶段：先机械拼接全稿，全局编辑标注跨章节冲突、内容归属规则，局部编辑仅修订对应章节，无需重写全文。
- 配套训练数据构建流程：基于独立源材料生成研究任务与评分规则，校验内容可检索性后，收集工作流各阶段执行轨迹，用于LongCat模型的中训与后训。
### 关键结果
在3个公开基准+1个内部基准测试：DeepResearchBench得分55.25，超ChatGPT-DeepResearch 0.3分；DeepResearchBench II得分51.35，超Claude-DeepResearch 3.17分；ResearchRubrics得分79.83，超ChatGPT-DeepResearch 5.62分；内部基准得分76.04，仅比ChatGPT-DeepResearch低0.55分，位列第二。
### 核心结论
复杂长周期Agent任务的优化，优先做架构分层解耦，比单纯提升模型能力的投入产出比更高
