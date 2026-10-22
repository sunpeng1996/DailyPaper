---
title: 'LongZero: Enhancing Long-Context Reasoning in LLMs from Zero Data'
title_zh: LongZero：零外部数据提升大模型长上下文推理能力
authors:
- Zhennan Wan
- Jianfei Chen
affiliations:
- Tsinghua University
arxiv_id: '2610.30132'
url: https://arxiv.org/abs/2610.30132
pdf_url: https://arxiv.org/pdf/2610.30132
published: '2026-10-21'
collected: '2026-10-22'
category: LLM
direction: 大模型长上下文 · 零数据强化学习
tags:
- Long-Context Reasoning
- GRPO
- Zero Data
- Synthetic Data
- Reinforcement Learning
one_liner: 无需外部数据或教师模型，通过LLM自合成结构化训练数据与GRPO训练提升长上下文推理能力
practical_value: '- 电商/推荐场景下，处理用户长历史会话、多商品评论聚合、长文档（如商品详情页合集）理解类任务时，可复用「先确定QA对+支撑证据，再扩展生成带干扰的长上下文」的自合成数据范式，无需人工标注即可低成本扩充长上下文训练数据，同时避免参数记忆干扰

  - 做LLM/Agent的RL训练时，可借鉴「仅保留模型回答不稳定的样本」的过滤策略，既能避免全对/全错样本带来的零梯度浪费计算资源，还能自动适配当前模型的能力阶位，无需人工调整难度

  - 优化RAG、多跳检索、长文档推荐理由生成等任务的模型能力时，可复用2:1的推理+检索双任务混合训练配比，同时提升多跳事实整合能力和长文本中精确定位目标信息的能力'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有长上下文RL训练方案依赖昂贵人工标注、外部语料或更强教师模型，数据获取成本高且容易存在数据泄露、模型依赖参数知识回答而非上下文等问题；已有的零数据RL方法仅支持短上下文任务，无法直接迁移到长上下文场景（先生成长文本再写QA的范式容易出现事实不一致、答案不可靠问题）。
### 方法关键点
- 反转生成顺序：先由待训练LLM生成短结构化的问题、支撑证据、答案规范，再将证据扩展为多文档长上下文，答案由构造保证正确，完全无需外部数据或教师模型
- 合成两类互补训练数据：①多跳推理数据（虚构实体+干扰事实，避免模型用参数知识回答，强制依赖上下文）；②多轮检索数据（模拟MRCR任务，提升长文本中精确定位目标信息的能力）
- 难度过滤：仅保留模型回答既有正确也有错误的不稳定样本，适配GRPO训练的梯度要求，自动匹配当前模型能力
- 采用GRPO算法训练，规则化奖励无需人工或模型评判
### 关键结果
在Qwen3-4B-Thinking、Qwen3-8B两个基座上测试，对比基于外部语料的增强HotpotQA、397B大模型合成QA两个基线，在LongBench、LongBench v2等5个长上下文基准上平均得分最高；其中Qwen3-4B上平均得分达57.42，比基线高0.85~1.43分，训练获得的能力可从虚构训练数据迁移到真实文档、从10k-20k的训练上下文迁移到更长的评测输入。

最值得记住的一句话：长上下文零数据训练的核心是先锁定答案的正确性，再扩展长上下文，而非反过来基于已有的长文本生成QA
