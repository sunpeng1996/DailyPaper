---
title: Memory-Centric Continual Learning for AI Agents
title_zh: 面向AI Agent的以记忆为核心的持续学习框架
authors:
- Dongfang Li
- Zhuoen Chen
- Bonian Jia
- Zixuan Liu
- Zhengxuan Lu
- Can Deng
- Yukun Shi
- Yuhang Meng
- Xin Zhang
- Jiahe Huang
arxiv_id: '2610.29357'
url: https://arxiv.org/abs/2610.29357
pdf_url: https://arxiv.org/pdf/2610.29357
published: '2026-10-20'
collected: '2026-10-22'
category: Agent
direction: Agent 记忆驱动持续学习架构与评估
tags:
- Continual Learning
- Agent Memory
- LLM Agent
- Scaling Law
- Evaluation Protocol
one_liner: 提出以记忆为核心的Agent持续学习框架，重构记忆从被动检索到主动学习的完整体系
practical_value: '- 可直接复用三轴记忆分类法梳理电商导购Agent、个性化推荐系统的记忆模块，明确当前短板（如是否缺失用户偏好的来源、时效标签）

  - 记忆五阶段生命周期可迁移到用户长期兴趣建模：对交互历史分层存储（episodic存交互明细、semantic存长期偏好、procedural存决策规则），缓解兴趣漂移和记忆污染

  - 评估协议可优化RAG-based推荐系统：从仅看召回准确率，升级为评估记忆对最终转化率、跨场景偏好迁移的提升，解决检索信息不被模型利用的问题

  - 记忆缩放定律可指导资源分配：当Agent交互数据增长时，按量化关系匹配非参数化存储容量和计算资源，平衡成本和性能'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有LLM Agent的记忆系统多作为被动RAG缓存，仅评估事实召回能力，无法支撑长期部署下的行为持续优化；常规持续微调存在灾难性遗忘、算力成本高的问题，扩展上下文窗口又存在注意力衰减、长度限制的瓶颈，无法实现真正的持续学习。
### 方法关键点
- 三轴记忆架构分类：按存储介质（上下文/激活层/外部可寻址/自适应参数）、知识形态（情景/语义/过程）、管理策略（预设规则/ deliberative/ learned）三个维度解耦记忆系统设计，明确各维度的trade-off
- 双循环记忆生命周期：内循环更新记忆内容，覆盖写入、整合、检索、修正、遗忘五个核心阶段；外循环根据任务反馈迭代记忆管理策略，实现记忆管控的自优化
- 专用评估协议：从干扰下的保留率、变化适配能力、跨任务迁移能力三个维度评估，区分单纯上下文扩展和真实行为提升，避免伪持续学习
- 记忆缩放定律：量化Agent性能与经验量、存储容量、计算预算的对应关系，覆盖非参数化和参数化两类记忆，给出资源最优分配路径
### 关键结果
理论推导与合成实验验证：非参数化记忆按最优比例分配存储和读取资源时，超额任务误差随总资源提升最多下降2个数量级；参数化记忆采用专用适配器（如LoRA）相比骨干直接微调，抗干扰能力提升1-2个数量级，相同经验量下所需存储容量低3个数量级。
### 核心结论
Agent记忆的核心价值不是召回多少历史信息，而是能否通过记忆持续提升未来的决策表现
