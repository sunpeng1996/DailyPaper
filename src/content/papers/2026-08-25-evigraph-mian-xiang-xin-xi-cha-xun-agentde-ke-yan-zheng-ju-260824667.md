---
title: 'EviGraph: Towards Verifiable Evidence Construction for Information-Seeking
  Agents'
title_zh: EviGraph：面向信息查询Agent的可验证证据构建框架
authors:
- Jiashun Chen
- Yirong Mao
- Wenhui Que
affiliations:
- WeChat, Tencent Inc., Beijing, China
arxiv_id: '2608.24667'
url: https://arxiv.org/abs/2608.24667
pdf_url: https://arxiv.org/pdf/2608.24667
published: '2026-08-25'
collected: '2026-08-26'
category: Agent
direction: 信息查询Agent · 可验证证据构建
tags:
- Agentic Search
- Evidence Graph
- Reinforcement Learning
- Grounded Reasoning
- Verifiable AI
one_liner: 提出基于证据图的双角色搜索Agent框架，用结构化过程奖励优化证据构造而非仅最终答案
practical_value: '- 可复用双角色拆分架构：将搜索执行、证据提取、结构校验拆为独立模块，冻结不可训练的证据验证模块减少幻觉，适合电商商品信息核验、用户评论真实性校验类Agent落地

  - 结构化过程奖励设计：用证据图覆盖度、冲突率、任务匹配度作为中间奖励信号，无需海量标注即可通过RL优化搜索Agent，适合多步检索场景如商品规格查询、售后问题溯源

  - 模态无关证据图Schema：将多模态证据统一转成文本锚点存入图结构，无需额外适配即可支持图文混合的商品信息检索、内容真实性核验场景'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有搜索Agent仅以最终答案正确性为优化目标，中间检索内容和答案的证据关系隐式存在于交互轨迹中，无法验证支撑性，易出现正确答案但证据不足、引用不明确、矛盾证据被忽略等问题，无法满足多约束验证的复杂信息查询需求。

### 方法关键点
- 架构拆分：执行器负责生成查询、决定终止时机，冻结的证据验证器从搜索结果提取带极性（支持/冲突）的原文片段，证据提议模块请求更新证据图，确定性结构校验器仅检查图结构合法性，不做语义判断
- 证据图设计：包含文档、原文片段、原子声明、候选答案四类节点，边标注包含/支持/冲突关系，所有声明都可溯源到原文片段，天然支持审计
- 训练优化：执行器和证据提议模块共享同一策略模型，通过GRPO做RL训练，奖励由检索新颖度、证据覆盖度、冲突惩罚、任务匹配度共同构成，避免仅用最终答案奖励导致的捷径行为

### 关键结果
在BrowseComp-Plus数据集上，Qwen3-8B EviGraph在相同交互预算下准确率达35.9%，比无RL的双角色架构高9个百分点，比单块Agent高33.2个百分点；在多模态LiveVQA数据集上，零样本迁移的Qwen3-VL-8B EviGraph准确率达78.0%，超过Gemini-2.5-Pro 2个百分点，和30B参数量的SOTA多模态搜索Agent效果相当。

将Agent搜索从「轨迹记录」转为「结构化证据构造」，用可验证的中间过程信号优化，比仅优化最终答案能大幅提升小模型的搜索表现，同时降低幻觉。
