---
title: Adaptive Memory and Reflection Multi-Agent System for Medical Question Answering
title_zh: 面向医疗问答的自适应记忆与反思多智能体系统
authors:
- Pradeep Murugesan
- Luoxiao Yang
- Xueli Chen
- Xinqi Fan
affiliations:
- Manchester Metropolitan University
- Technion – Israel Institute of Technology
- Hong Kong Metropolitan University
arxiv_id: '2608.19029'
url: https://arxiv.org/abs/2608.19029
pdf_url: https://arxiv.org/pdf/2608.19029
published: '2026-08-19'
collected: '2026-08-20'
category: MultiAgent
direction: 多智能体协作 · 记忆与反思机制优化
tags:
- MultiAgent
- Medical QA
- Adaptive Memory
- Reflection Mechanism
- RAG
one_liner: 提出带角色专属记忆、反思反馈、复杂度路由的多智能体医疗QA框架，性能追平人类基准
practical_value: '- 可复用复杂度路由逻辑：根据任务难度自动分配单智能体/多智能体协作/高级专家处理链路，平衡推理效果与算力成本，适配电商客服、复杂query推荐等场景

  - 角色专属记忆设计：不同角色agent独立维护记忆库而非共享存储，按角色属性检索对应历史经验，可迁移到电商分垂类客服、定向推荐agent的记忆模块

  - 无参数反思反馈机制：推理错误时仅更新对应角色记忆条目而非微调模型，可低成本实现agent效果迭代，适合电商高频场景的快速badcase修复

  - 独立输出审核模块：将答案生成与合规审核拆分，可复用在广告文案、商品推荐理由生成的合规筛查环节，降低违规风险'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
医疗QA要求精准可溯源，但现有单智能体/静态RAG架构缺乏持久记忆、反思能力与伦理管控，无法从历史错误中迭代，输出可靠性不足，难以适配不同复杂度的临床推理需求。

### 方法关键点
- 基于LangGraph搭建模块化多智能体链路，由Moderator先评估问题复杂度，Recruiter自动路由到三类处理链路：低复杂度由单全科医生处理，中复杂度走多专家协作共识，高复杂度走多轮迭代+高级决策人审核，平衡效果与效率。
- 每个角色agent维护独立记忆库，存储历史问答、推理过程、角色元数据；推理错误时触发反思反馈，将纠错信息写入对应角色记忆，无需微调模型即可实现经验复用。
- 新增独立Ethical Overseer模块，最终输出前筛查不安全内容，审核逻辑与推理过程解耦，便于政策迭代。

### 关键实验
在MedQA（美国医师执照考试数据集）、MedMCQA（印度医学考试数据集）上测试，对比GPT-4、MDAgents、MedAgents等基线：全量AMR（记忆+反思+RAG）在MedQA准确率达93.2%，比GPT-4高7.1pct，比人类基准高6.2pct；在MedMCQA准确率达90%，与人类基准持平。消融实验显示仅加反思比基线高2pct，仅加角色记忆比基线高4-6pct，记忆+反思+RAG组合增益最大。

### 核心结论
多智能体系统的效果提升不依赖模型参数微调，通过复杂度路由、角色专属记忆、反思反馈的架构设计即可实现显著增益，同时兼顾可控性与迭代效率。
