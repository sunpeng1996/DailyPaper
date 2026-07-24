---
title: Streaming Multi-Agent Autoregressive Diffusion Model with World State Registers
title_zh: 带世界状态寄存器的流式多智能体自回归扩散模型
authors:
- Sicheng Mo
- Yuheng Li
- Ziyang Leng
- Krishna Kumar Singh
- Bolei Zhou
affiliations:
- University of California, Los Angeles
- Adobe Research
arxiv_id: '2607.21594'
url: https://arxiv.org/abs/2607.21594
pdf_url: https://arxiv.org/pdf/2607.21594
published: '2026-07-22'
collected: '2026-07-24'
category: MultiAgent
direction: 多智能体世界建模 · 共享状态寄存器
tags:
- MultiAgent
- WorldModel
- DiffusionModel
- StateToken
- AutoregressiveGeneration
one_liner: 提出带跨智能体共享世界状态寄存器的流式多智能体视频扩散框架WorldWeaver，提升生成一致性
practical_value: '- 多智能体协同场景（电商多客服Agent、导购Agent集群）可复用共享状态寄存器设计，统一维护全局会话/商品/用户状态，避免各Agent状态冲突

  - Mixture-of-Transformers拆分状态建模与业务输出建模权重的思路，可迁移到生成式推荐场景，分别建模用户全局长期状态和单次推荐内容生成，提升推荐一致性

  - 给共享状态引入多维度监督信号（个体状态、全局视图、文本描述）的方法，可用于优化RAG系统全局记忆模块训练，减少记忆漂移'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有自回归扩散pipeline仅将历史观测作为条件上下文，多智能体、多视角场景下难以维护全局共享状态，易出现逻辑不一致、状态冲突问题。
### 方法关键点
1. 提出WorldWeaver（W²）流式多智能体扩散框架，新增跨智能体世界状态寄存器：用可学习token存储全局共享信息、追踪单智能体状态，每生成一段内容后动态更新；
2. 引入三类监督信号对齐寄存器表示：覆盖单智能体状态、鸟瞰全局视图、场景文本，确保状态寄存器的准确性与可解释性；
3. 采用Mixture-of-Transformers架构，拆分世界状态建模和视觉帧建模的独立权重，降低两类任务的耦合度，提升训练效率。
### 关键结果
双智能体Minecraft视频生成实验验证，显式世界状态建模可显著提升生成逻辑一致性与整体质量，优于现有无全局状态的自回归扩散基线。
