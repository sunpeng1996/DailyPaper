---
title: 'Option-GRPO: Hierarchical RL Against AI Slop in Code Generation for Unseen
  SDKs'
title_zh: Option-GRPO：分层RL解决未知SDK代码生成的AI冗余问题
authors:
- Prashank Kadam
affiliations:
- Cerby Inc., USA
arxiv_id: '2611.23633'
url: https://arxiv.org/abs/2611.23633
pdf_url: https://arxiv.org/pdf/2611.23633
published: '2026-11-17'
collected: '2026-11-19'
category: Training
direction: 分层RL · LLM代码生成训练优化
tags:
- GRPO
- Hierarchical RL
- Code Generation
- SDK Adaptation
- Reward Engineering
one_liner: 基于分层RL与GRPO的未知SDK代码生成框架，无标注同时优化正确性与代码质量
practical_value: '- 分层option+课程式GRPO训练可迁移到生成式推荐的语义ID、商品文案生成场景，将高频可复用的文案/ID模式作为option，既降低长序列生成的奖励稀疏问题，还能减少生成冗余、提升输出合规性

  - 从结构化数据（如电商类目体系、Agent工具接口定义）自动挖掘可复用option的方法，可落地到电商Agent的工具调用优化，无需大量人工标注的工具调用样本，仅从接口结构就能挖掘常用组合模式，降低训练成本

  - Option级别的信用分配方案可复用在推荐系统多步转化的RL优化场景，把曝光→点击→加购→下单每个转化节点作为option，相比token级/单步的奖励分配，梯度信噪比提升可达√(T/K)倍（T为总步长，K为option数量）'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
代码LLM面对训练截断后发布的未知SDK时，易生成冗余、非惯用的AI垃圾代码，现有方案仅优化功能正确性，且依赖人工标注的使用示例或测试用例，落地成本高，无法同时兼顾生成质量与效率。

### 方法关键点
- 从SDK源码的参数流图挖掘分层代码option：分为单API调用的Level 0 option和多API组合的Level 1 option，option预定义类型触发条件、允许调用的函数集与终止条件，同时保留原生token生成作为fallback
- 课程式分层训练：三个阶段依次训练原子API调用、组合模式调用、完整程序生成，每阶段训练后筛选出准确率≥70%、出现≥5次的可复用option加入下一阶段动作空间
- 改进GRPO优化：在原序列级组归一化奖励基础上，新增option级信用分配，对比包含/排除对应option的样本组奖励差，梯度信噪比相比flat GRPO提升Θ(√(T/K))倍
- 无人工标注奖励体系：基于SDK类型注解自动生成分层执行奖励，额外增加代码简洁度、API调用效率、自一致性的多目标奖励项

### 关键结果
在12个未知SDK构成的UnseenSDK-Bench上，基于Qwen3-32B基础模型：
1. pass@1达61.4%，比flat GRPO高8.7个点，比ReCode高6.3个点，性能超过GPT-4o、Claude 3.5 Sonnet等通用前沿模型在未知SDK上的表现
2. 生成代码长度比flat GRPO短27%，API调用数少34.7%，代码中惯用模式覆盖率从41%提升至74%，有效解决AI冗余问题

### 核心结论
将分层RL的option框架与课程训练阶段强绑定，把前一阶段验证有效的可复用模式作为下一阶段的动作原子，既大幅缩小长序列生成的探索空间，又能完全基于结构化数据自动挖掘模式，无需人工标注样本
