---
title: 'SLCA-GRPO: Resolving Cross-Segment Credit Misattribution in Tool-Calling RL'
title_zh: SLCA-GRPO：解决工具调用强化学习中的跨段信用错配问题
authors:
- Yan Zhan
- Shaobo Liu
- Qiunan Liu
- Yuanjun Shi
- Siqi Xu
- WeiYi Hou
- Xiang Xu
- Zekang Li
- Weizhou Pan
- Jiahong Yan
affiliations:
- Peking University
- Shenzhen University
- Tencent PCG QQ Team
arxiv_id: '2609.29050'
url: https://arxiv.org/abs/2609.29050
pdf_url: https://arxiv.org/pdf/2609.29050
published: '2026-09-23'
collected: '2026-09-28'
category: Agent
direction: Agent 工具调用强化学习优化
tags:
- Tool Calling
- GRPO
- Reinforcement Learning
- Credit Assignment
- Agent Training
one_liner: 提出段锁定信用分配的SLCA-GRPO框架，解决工具调用RL的跨段信用错配问题
practical_value: '- 工具调用Agent训练时可复用SLCA机制，将工具调用段与回复摘要段的优势估计解耦，分别用执行奖励和偏好奖励更新对应token，避免梯度污染，直接提升电商客服、导购类Agent的工具调用准确率

  - 大规模工具调用Agent训练可采用SGLS替代真实API，既降低API调用成本，又能保证返回的工具响应符合Schema约束，大幅提升训练稳定性

  - 混合结构生成的RL优化（如生成式推荐同时输出推荐商品与推荐理由、广告同时输出创意文案与定向规则）可复用该思路，先按语义拆分输出段，再匹配对应目标单独做优势估计，避免多目标梯度冲突'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前工具调用Agent输出由结构化工具调用段与用户侧自然语言摘要段混合组成，标准GRPO等on-policy RL算法将统一轨迹级优势广播给所有token，导致摘要生成的梯度噪声泄露到工具决策token，出现跨段信用错配：错误工具调用搭配正确摘要会被奖励，正确工具调用搭配错误摘要会被惩罚，训练不稳定、工具调用准确率低。
### 方法关键点
- 设计HierR分层奖励：拆分为面向工具段的dense执行奖励（评估工具调用正确性、效率）与面向摘要段的终端偏好奖励（评估回复质量）
- 核心SLCA机制：基于token掩码自动拆分工具段与摘要段，两类奖励分别在rollout组内归一化得到独立优势，仅路由到对应语义段的token，无需额外rollout、不拆分模型
- 配套SGLS模拟器：通过Schema校验+冻结LLM模拟工具响应，无需调用真实API即可实现大规模稳定训练
### 关键实验
基于3B/7B/8B Qwen backbone测试，对比基线包括原生GRPO、ToolPO、RLTR等，覆盖3个基准：7B backbone下，域内Toucan测试集Success率比GRPO高2.53pp，跨域BFCL工具调用榜单准确率比GRPO高1.36pp，鲁棒性τ2-Bench Pass1率比GRPO高9.15pp，同时工具调用轮次更少、冗余度更低。
### 核心结论
异构输出的RL训练中，按语义结构拆分优势分配比统一广播的效果更稳定、准确率更高，该思路可拓展到所有混合结构生成的RL优化场景
