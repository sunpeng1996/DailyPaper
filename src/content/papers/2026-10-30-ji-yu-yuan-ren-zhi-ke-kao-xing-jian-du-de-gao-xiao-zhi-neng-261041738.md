---
title: 'Search When Needed, Proceed When Reliable: Metacognitive Reliability Supervision
  for Efficient Agentic Search'
title_zh: 基于元认知可靠性监督的高效智能体搜索决策框架
authors:
- Minhao Sun
- Zhijing Wu
- Xian-Ling Mao
affiliations:
- Beijing Institute of Technology
arxiv_id: '2610.41738'
url: https://arxiv.org/abs/2610.41738
pdf_url: https://arxiv.org/pdf/2610.41738
published: '2026-10-30'
collected: '2026-11-02'
category: Agent
direction: Agent 智能体搜索决策优化
tags:
- Agentic Search
- RAG
- Metacognition
- Reinforcement Learning
- Uncertainty Estimation
one_liner: 通过中间推理状态可靠性细粒度监督优化智能体搜索决策，兼顾精度与效率
practical_value: '- 做Agentic RAG/搜索增强推荐时，可在最终答案对错的RL奖励基础上，叠加中间状态可靠性分作为过程奖励，分别对搜索/不搜索动作做细粒度监督，解决现有奖励信号模糊的问题

  - 可复用序列不确定性到准确率的预校准映射方法，用于电商客服、商品问答的检索触发场景：低不确定性直接用内部知识回答，高不确定性才触发商品/知识库检索，降低检索成本

  - 搜索决策可按任务复杂度动态分配资源：单跳/简单查询减少冗余检索，多跳/复杂推理场景增加检索次数，平衡用户体验和系统开销，适配电商多轮导购、复杂需求识别场景

  - GRPO训练时可将过程奖励与最终答案、格式奖励加权结合，无需额外标注，靠模型自生成探针即可计算，工程落地成本低'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有智能体搜索的监督信号多依赖最终答案对错或轨迹级反馈，无法区分正确答案来自可靠知识还是幸运猜测，也无法评估检索动作对推理可靠性的实际贡献，易导致过检索（无必要检索）或欠检索（应检索未检索），精度和效率的tradeoff难以优化。

### 方法关键点
- 预校准映射函数：离线拟合LLM生成结论的平均负对数似然（序列不确定性）与局部结论准确率的对应关系，作为可靠性评估基准，训练过程固定不变
- 双维度可靠性打分：不搜索动作输出「当前状态可靠性分」，计算当前状态可靠性与校准基准的差值；搜索动作输出「检索收益分」，计算有/无检索结果两种匹配上下文下的可靠性差值
- 可靠性感知过程奖励：将每步打分在轨迹内取平均，与最终答案奖励、格式奖励加权结合用于GRPO策略优化，推理阶段无需探针计算，无额外开销

### 关键实验
在7个QA基准（含单跳、多跳）上对比HiPRAG等SOTA基线，使用Qwen2.5-7B backbone时：平均CEM达69.3，比SOTA基线HiPRAG高2.1个点；整体检索调用量减少6.8%，其中单跳QA检索量降20.9%，多跳QA检索量升6.6%，实现检索资源动态分配。

最值得记住的一句话：智能体搜索决策的监督核心不是最终结果对错，而是每步动作是否匹配当前推理状态的真实可靠性，「该搜则搜、该省则省」才能同时提精度降成本。
