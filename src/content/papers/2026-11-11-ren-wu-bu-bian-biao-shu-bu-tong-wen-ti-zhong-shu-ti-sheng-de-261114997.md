---
title: 'Same Task, Different Statement: When and How Reformulation Helps LLM Problem
  Solving'
title_zh: 任务不变表述不同：问题重述提升LLM求解效果的机制与方法
authors:
- Wentao Zhang
- Xiaoyu Zhang
- Chengwei Liu
- Yutao Hu
- Tao Zhang
- Junsheng Wu
- Hongping Gan
- Yang Liu
affiliations:
- Northwestern Polytechnical University
- Nanyang Technological University
- Nankai University
- Huazhong University of Science and Technology
arxiv_id: '2611.14997'
url: https://arxiv.org/abs/2611.14997
pdf_url: https://arxiv.org/pdf/2611.14997
published: '2026-11-11'
collected: '2026-11-13'
category: Reasoning
direction: LLM推理优化 · 提示重述
tags:
- Prompt Engineering
- Chain-of-Thought
- Reasoning
- LLM Optimization
- Task Reformulation
one_liner: 提出三类任务保留型问题重述策略，按任务类型匹配可大幅提升LLM推理求解准确率
practical_value: '- 做Agent推理模块时，对用户query可优先按类型匹配重述策略：搜索/分类类query用Decomposition拆分隐式子目标，解释/因果类query用Concept
  Reduction去除冗余叙事，优化/验证类query用Typed Reformulation切换求解框架，避免盲目改写导致效果下降

  - 生成式推荐场景中，可将用户模糊需求按上述三类规则重述后再输入LLM生成候选item，尤其对小参数开源LLM可获得更大提升（实验显示Llama-3.1-8B改写后对应子集准确率提升31.2%）

  - 业务侧落地时可先基于自有任务标注类型训练简单的重述选择规则，仅对匹配的15%-20%query做改写，既能拿到平均+11.0%的效果收益，又能避免额外推理成本和原正确案例被翻转的负向影响'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
现有LLM推理优化多聚焦于求解策略（如CoT、自修正、工具调用），很少改动问题本身的表述，但人类求解难题时会先重述问题降低认知负荷，很多LLM求解失败并非能力不足，而是问题表述不符合模型的推理习惯，因此需要明确合法重述的边界以及不同重述策略的适用场景。

### 方法关键点
1. 定义合法重述4条约束：保留语义、保留约束与目标、保留答案接口、无答案泄露，确保重述不改变原任务本质；
2. 提出三类重述策略：Decomposition拆分隐式子目标，Typed Reformulation切换适配的求解框架，Concept Reduction逐层抽象去除冗余细节暴露核心结构；
3. 基于训练集的重述效果匹配规律，设计轻量选择规则，仅对适配类型的问题执行重述，其余保留原表述。

### 关键实验
在8个数学、逻辑、代码基准数据集，8款LLM上统一用zero-shot CoT验证：Oracle最优重述选择平均提升准确率+27.6%；基于训练集规律的简单选择规则在测试集被改写的问题上平均提升+11.0%，而盲目改写反而下降5.6%；小参数模型从改写中收益更高，Llama-3.1-8B在改写子集上准确率提升达31.2%。

### 核心结论
对LLM而言，部分看似能力不足的推理失败本质是表述适配问题，适配任务类型的重述可低成本获得大幅收益，盲目改写反而会伤害效果。
