---
title: LLMs Memorize Their Own Hallucinations During Post-Training
title_zh: 大模型后训练阶段会记忆自身生成的幻觉内容
authors:
- Anirudh Atmakuru
- Tanya Goyal
affiliations:
- Cornell University
arxiv_id: '2611.26863'
url: https://arxiv.org/abs/2611.26863
pdf_url: https://arxiv.org/pdf/2611.26863
published: '2026-11-18'
collected: '2026-11-24'
category: Training
direction: 大模型后训练 · 幻觉记忆机制研究
tags:
- LLM Hallucination
- Post-Training
- Reinforcement Learning
- GRPO
- Outcome-based Reward
one_liner: 验证推理导向后训练配方会让LLM记忆自身生成的幻觉并量化效应
practical_value: '- 电商导购/知识库Agent做RL对齐时，不能仅用最终答案正确性作为奖励，需额外校验中间思考链的事实性，避免商品属性、活动规则等错误幻觉被固化进模型

  - 训练垂直领域知识类LLM时，对难样本不要强行做outcome-based RL优化，难样本的幻觉记忆效应更强，极易引入错误业务信息

  - 用CoT做商品问答、用户咨询响应的模型对齐时，即使模型最终输出正确，也要对中间出现的错误事实做惩罚，否则模型依然会记忆这些错误并在后续输出

  - 常规KL正则无法缓解幻觉记忆问题，需从奖励机制设计层面优化，不能仅依赖最终结果的反馈'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前主流大模型后训练配方（如GRPO、仅基于最终输出的奖励、鼓励思考回溯等）均为数学、代码等推理任务设计，但被广泛迁移到知识类任务（如问答、知识库对齐）中，其可能引入的幻觉风险未被系统性研究，而电商、搜索推荐场景的知识类响应幻觉会直接带来资损、用户投诉等业务问题。
### 方法关键点
- 实验覆盖Qwen、Olmo两个模型家族共6款不同规模、不同架构（稠密/MoE）的开源大模型
- 定义两类幻觉集合：HalluSet-train（训练阶段生成的、对应最终正确答案的幻觉）、HalluSet-heldout（非训练样本生成的幻觉，作为对照组）
- 设计memorization score量化训练前后幻觉召回率的变化，基于GRPO做RL训练，仅给最终正确答案正向奖励
### 关键结果
- 训练中被强化的幻觉平均召回率提升4.83%，对照组仅提升0.17%；即使是模型中途回溯纠正的幻觉，记忆率与未回溯的仅差0.08%，几乎无差异
- 越难的训练样本（正确rollout越少），幻觉记忆效应越强；被强化的幻觉的abstention概率平均下降7.23%，模型更不愿意拒绝回答错误信息
- 加KL正则仅能平均降低0.52的记忆分，无法根本解决问题，幻觉一旦被记忆会在后续训练中长期保留
### 最值得记住的结论
为推理任务设计的后训练配方迁移到知识类任务时，仅基于最终结果的奖励机制必然会固化中间生成的幻觉，哪怕这些幻觉已经被模型主动纠正。
