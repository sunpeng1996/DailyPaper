---
title: 'ContextPilot: Teaching Agents for Proactive Context Management via Fine-grained
  RL'
title_zh: ContextPilot：基于细粒度RL的Agent主动上下文管理框架
authors:
- Zhuoshi Pan
- Qizhi Pei
- Junru Lu
- Honglin Lin
- H. Vicky Zhao
- Di Yin
- Xing Sun
affiliations:
- Tsinghua University
- Tencent Youtu Lab
- Shanghai AI Lab
arxiv_id: '2608.28476'
url: https://arxiv.org/abs/2608.28476
pdf_url: https://arxiv.org/pdf/2608.28476
published: '2026-08-27'
collected: '2026-08-31'
category: Agent
direction: Agent 主动上下文管理优化
tags:
- Context Management
- Reinforcement Learning
- Long-Horizon Agent
- LLM Agent
- Credit Assignment
one_liner: 扩展Agent上下文管理工具集，结合细粒度RL训练，在长任务下实现更高性能与更紧凑上下文
practical_value: '- 可复用扩展后的上下文管理工具集，在电商搜索导购、长对话推荐Agent中引入规划、长期记忆、软上下文卸载三类工具，大幅降低多轮交互下的上下文膨胀，减少KV
  cache占用

  - 借鉴细粒度RL训练范式，针对上下文编辑这类高影响操作，用上下文变化+熵变化识别关键决策点分配更多探索预算，避免传统轨迹级奖励导致的信用分配错位，适合多轮推荐、深度搜索类Agent的微调

  - 可直接落地快照级奖励计算逻辑，将同一前缀的所有分支轨迹的最终奖励平均作为中间快照的奖励，显著提升RL训练稳定性，减少错误奖励信号对上下文管理策略的干扰'
score: 9
source: huggingface-daily
depth: full_pdf
---

### 动机
长horizon Agent任务（如深度搜索、长上下文QA）需要LLM跨多轮交互检索整合信息，现有主动上下文管理方法存在三个核心缺陷：工具集仅支持搜索、删除、总结，缺少全局规划、长期记忆等能力；RL探索效率低，未区分不同上下文操作对结果的异质性影响；信用分配粗粒度，直接将轨迹级奖励赋给所有中间上下文编辑动作，导致训练信号偏差。

### 方法关键点
- 工具层：扩展上下文管理工具集，新增规划、长期记忆、软上下文卸载三类工具，支持结构化信息存储、跨片段关联、动态压缩/折叠历史等操作
- 训练层：提出适配上下文管理的RL方法，用上下文长度变化+生成熵变化计算操作敏感度，给高影响操作分配更多探索预算做分支采样
- 信用分配层：对每个中间轨迹快照，聚合所有以其为前缀的终端轨迹的奖励，计算快照级优势，实现细粒度奖励信号分配

### 关键实验
在长上下文QA（NovelQA、∞Bench等4个基准）、深度搜索（BrowseComp、GAIA等4个基准）上测试，跨Qwen3、Gemma4、WebSailor等多个底座均获得稳定收益：32K上下文窗口的ContextPilot-14B-RL比128K窗口的同底座无工具版平均高18.94个百分点，比同规格StateLM-14B-RL高2.09个百分点；深度搜索任务比SOTA SUPO平均高1.51个百分点，同时上下文长度稳定在8K-10K，远低于基线的30K。

### 核心结论
上下文管理操作对长任务结果的影响差异极大，针对高敏感操作做定向探索和细粒度信用分配，是用小上下文窗口实现大窗口性能的核心路径。
