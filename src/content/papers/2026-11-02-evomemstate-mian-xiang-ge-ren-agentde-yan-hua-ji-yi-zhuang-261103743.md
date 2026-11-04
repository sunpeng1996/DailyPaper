---
title: 'EvoMemState: Evolving Memory State for Personal Agents'
title_zh: EvoMemState：面向个人Agent的演化记忆状态框架
authors:
- Zhishang Xiang
- Yunbo Tang
- Zhongqiao Liu
- Junkai Chen
- Zerui Chen
- Qingguo Hu
- Yuxuan Zhang
- William Grant
- Qinggang Zhang
- Jinsong Su
affiliations:
- Xiamen University
- Nanyang Technological University
- University of British Columbia
- University of Waterloo
- Jilin University
arxiv_id: '2611.03743'
url: https://arxiv.org/abs/2611.03743
pdf_url: https://arxiv.org/pdf/2611.03743
published: '2026-11-02'
collected: '2026-11-04'
category: Agent
direction: Agent 长期记忆状态优化
tags:
- LLM Agent
- Long-term Memory
- Reinforcement Learning
- Ontology
- Memory State
one_liner: 提出状态中心的记忆框架，通过关系状态与RL生成的推理状态提升Agent记忆利用准确性
practical_value: '- 可借鉴本体引导的记忆状态归纳方法，对用户行为/偏好事实分层组织，显式标记偏好的新旧更替、冲突关系，解决电商推荐中用户偏好冲突识别难的问题

  - 可复用RL-based记忆使用策略学习思路：用GRPO训练轻量的记忆优先级/适用性判断策略，无需改动主模型即可提升个性化生成效果，适合电商导购Agent场景

  - 记忆检索可参考关系遍历思路：召回种子事实后遍历关联的更新、冲突事实，提升检索完整性，解决现有RAG召回相关信息遗漏的问题

  - 推理状态可跨记忆系统迁移的结论可直接复用，现有业务的记忆/用户画像系统可接入训练好的推理状态生成模块，低成本提升效果'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有LLM Agent长期记忆普遍采用事实中心范式，独立存储碎片化记忆，忽略了事实间的更新、约束、冲突关系，且无法根据当前请求动态判断记忆的适用性、角色与优先级，即便召回全部相关记忆，也容易出现误用旧偏好、冲突处理错误等问题，导致个性化服务准确性不足。

### 方法关键点
- 本体引导的记忆状态归纳：从交互历史提取原子持久事实，增量构建个人记忆本体，用PARENT_OF/CONTAINS/SUPERSEDES/CONFLICTS_WITH等类型边标记事实层级、更新、冲突关系，生成持久化关系状态，保留原始事实的同时显式记录其有效性、作用范围
- RL驱动的状态演化：基于GRPO训练轻量记忆状态演化策略，以候选推理状态带来的回答效果增益为奖励，将记忆使用经验内化到策略中，为每个请求生成专属推理状态，明确相关记忆的适用性、角色、优先级
- 状态感知推理：召回语义相似的种子记忆后，遍历关系边扩展关联事实，结合关系状态与推理状态引导Agent生成回答

### 关键实验
在MemSyco-Bench、MemTrapBench、LoCoMo等4个长期记忆基准测试，对比MemGPT、MemoryBank、Mem0等9个SOTA记忆系统；搭载Qwen3-8B时，整体平均准确率达59.9%，较最优基线高6.3pp，完整检索率达85.6%，完整检索下的准确率较最优基线高31.2pp；推理状态可迁移到其他记忆系统，带来0.2~4.9pp的效果提升。

### 核心结论
可靠的个性化记忆既需要连贯的状态构建，也需要基于使用经验的状态演化
