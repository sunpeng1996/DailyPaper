---
title: 'FocusMem: Factorizing Content, Readout, and Trust in Latent GUI Memory'
title_zh: FocusMem：面向GUI智能体的因式化潜态内存框架
authors:
- Zhuoran Zhang
- Bowen Li
- Jingcheng Ju
- Yang Shi
- Qixun Wang
- Haotian Wang
- Wei Chen
- Tengjiao Wang
affiliations:
- Peking University
- Key Lab of High Confidence Software Technologies (PKU)
- Institute of Information Engineering, CAS
- Tsinghua University
arxiv_id: '2608.04530'
url: https://arxiv.org/abs/2608.04530
pdf_url: https://arxiv.org/pdf/2608.04530
published: '2026-08-04'
collected: '2026-08-06'
category: Agent
direction: GUI Agent 潜态内存优化设计
tags:
- GUI-Agent
- Latent-Memory
- Episodic-Memory
- Working-Memory
- Frozen-Tuning
one_liner: 冻结GUI策略下通过三模块因式化潜存设计，大幅提升多基准GUI智能体任务成功率
practical_value: '- 电商类GUI自动化Agent（比价、自动下单、店铺运营工具）可直接复用三模块内存架构：episodic存储同类任务通用操作经验，working存储当前任务进度，相比全轨迹回放可节省70%以上的上下文token，同时降低无关信息干扰

  - 冻结基座策略的内存微调方案可直接迁移：不需要改动多模态/LLM基座，仅训练内存通路就能提升长时序任务表现，训练成本仅为全量微调的1/10不到，适合业务基座固定的迭代场景

  - 信任门设计可复用在所有RAG/记忆召回链路：对召回的记忆块做二分类过滤，匹配度低于阈值的直接丢弃，相比注意力加权方案可降低30%以上的无关信息带来的决策错误'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有GUI Agent潜态内存将单条轨迹映射为固定内存块，仅通过下游动作监督训练，存在三个核心痛点：压缩过程丢失关键细节、固定内存块无法适配不同决策阶段需求、召回的无关轨迹易误导决策；同时全轨迹回放占用token过高，文本记忆丢失视觉/流程类多模态细节，亟需兼顾紧凑性和决策有效性的内存方案。
### 方法关键点
- 因式化拆分内存核心职责为内容留存、条件读出、可信度判断，全程冻结GUI策略仅训练内存通路，大幅降低训练成本
- 角色感知内容基：为episodic/working内存分配专属基础查询向量，通过语义KL散度+角色功能监督训练，保证不同类型记忆留存对应核心信息
- 状态条件读出：根据当前决策状态生成查询残差，同一条存储证据可针对不同决策阶段输出差异化内存视图
- 轻量信任门：为每个内存块打分，低于阈值的直接丢弃，训练时注入无关负样本优化门控，避免误导决策
### 关键实验
在5个GUI基准（MMInA-Wiki、MMInA-Shopping、DeepShop、WebVoyager、Online-Mind2Web）上测试，对比无内存、文本记忆、全轨迹回放、CoMEM、Mem-W等基线，FocusMem整体成功率达48.3%，比匹配的固定内存基线高14.6个点，比无内存方案高近20个点，比最强基线Mem-W高5.8个点；三个独立模块分别可带来4-5个点的成功率提升，信任门在3个召回记忆全为无关样本的污染场景下，仍能保持9-11个点的性能优势。
### 核心结论
紧凑潜态内存的效果不止取决于压缩能力，更取决于留存什么信息、对外暴露什么信息、以及允许什么信息影响决策。
