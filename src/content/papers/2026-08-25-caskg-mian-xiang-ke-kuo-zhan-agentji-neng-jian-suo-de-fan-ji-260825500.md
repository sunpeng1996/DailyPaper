---
title: 'CaSKG: Counterfactual-Causal Skill Graphs for Scalable Agent Skill Retrieval'
title_zh: CaSKG：面向可扩展Agent技能检索的反事实因果技能图
authors:
- Zhiyuan Li
- Linyuan Gao
- Xuechun Ding
- Hongwei Chen
- Yuan Wu
- Yi Chang
affiliations:
- Jilin University
- Ant Group
arxiv_id: '2608.25500'
url: https://arxiv.org/abs/2608.25500
pdf_url: https://arxiv.org/pdf/2608.25500
published: '2026-08-25'
collected: '2026-08-28'
category: Agent
direction: Agent技能检索 · 反事实因果图优化
tags:
- LLM Agent
- Skill Retrieval
- Causal Graph
- Counterfactual Reasoning
- Graph Retrieval
one_liner: 基于反事实因果探针校准技能图边置信度，在多基准多LLM上均实现最优的Agent技能检索效果
practical_value: '- 电商运营/客服Agent的工具/技能库检索可复用该框架：先通过语义、输入输出匹配、流程角色等多信号召回候选技能关联，再用轻量LLM探针校验依赖，平衡检索覆盖度与噪声

  - 三个反事实探针（移除/替换/重排技能对）的设计可直接迁移到工具链、运营流程的依赖关系自动校验，无需人工标注即可判断流程依赖的必要性和方向性

  - 在线检索阶段的个性化PageRank扩散逻辑可替代纯向量检索，能召回与任务语义不直接匹配但属于流程必备的互补技能，适配多步骤电商任务（如活动搭建、用户全链路运营）的技能需求

  - 技能库规模增长时，该「宽候选+严校验」的图构建架构能有效抑制弱关联的错误传播，比全量未校准图检索的精度更稳定，适合大规模工具/组件库的检索场景'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
LLM Agent的可复用技能库规模持续扩大，全库prompt上下文成本过高，纯向量检索忽略技能间的流程依赖，传统图检索依赖的关联边可靠性不足，容易通过多跳传播引入噪声，导致检索得到的技能束无法支撑完整任务执行，亟需平衡覆盖度与精度的大规模技能检索方案。
### 方法关键点
- 离线多信号构建高召回候选技能图：融合语义相似度、词汇匹配、输入输出兼容性、流程结构角色等信号计算初始关联分，可选LLM judge微调分数，优先覆盖潜在的流程依赖关系
- 预算化反事实边校验：对高优先级候选边做三类探针测试（移除源技能、替换源技能为无关技能、颠倒技能顺序），用LLM评估依赖的必要性、特异性、方向性
- Beta平滑聚合探针结果得到边置信度，按阈值分为四类发布：确认边保留全权重、不确定边降权、拒绝边移除、少量未校验边保留低权重作为兜底
- 在线检索无需修改下游Agent接口：以任务query的语义/词汇匹配结果为种子，在校准后的加权图上做个性化PageRank扩散，输出排序后的技能束
### 关键实验
在ALFWorld ID-140家居任务、ScienceWorld U211科学任务两个基准，覆盖6款不同量级LLM，对比全库prompt、向量检索、GoS技能图基线：相对GoS，6模型平均ScienceWorld得分从72.62提升至80.50，ALFWorld成功率从80.01%提升至86.79，同时两个基准的平均环境交互步数均下降，在200-2000规模的技能库上均稳定优于基线。
### 核心结论
技能图检索的核心瓶颈不是关联覆盖度，而是边的置信度校准，「宽候选召回+选择性校验发布」的架构能同时保障检索的覆盖度与执行效率
