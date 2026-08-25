---
title: 'Apodex 1.1: Scaling Agentic Intelligence for Complex Work'
title_zh: Apodex 1.1：面向复杂长周期任务的Agent智能规模化系统
authors:
- Apodex Team
- B. An
- B. Li
- B. Wang
- B. Zhang
- B. L. Wang
- C. Feng
- C. Wei
- C. Xue
- C. Zhang
affiliations:
- Apodex AI
arxiv_id: '2608.23283'
url: https://arxiv.org/abs/2608.23283
pdf_url: https://arxiv.org/pdf/2608.23283
published: '2026-08-23'
collected: '2026-08-25'
category: Agent
direction: Agent 长周期复杂任务执行优化
tags:
- Agentic Workflow
- Multi-Agent Coordination
- Long-Horizon Task
- Environment Scaling
- AgentOS
one_liner: 通过环境扩展+Agent协作扩展双路径，用小参数量实现SOTA级复杂任务处理能力
practical_value: '- 可复用Agent Team协作架构：将任务分解、异步子任务调度、定向不对称验证、证据落地合成的流水线套用到电商大促策划、用户画像分析、选品策略制定这类长周期运营任务，减少人工对齐成本

  - 工程上可直接落地AgentOS的持久化工作空间、状态维护、上下文分级压缩方案，解决电商/推荐场景下Agent跨多轮会话处理用户需求时的状态丢失、上下文溢出问题

  - 训练思路可迁移：围绕业务常见的工具调用失败、信息冲突、用户需求变更等Failure Case构造多样化训练环境，提升Agent在真实业务场景的鲁棒性，无需仅堆SFT对话数据

  - 不对称验证设计可复用在生成式推荐的内容审核环节，无需让大模型重复生成全量内容，只针对高风险的促销规则、价格、权益点做定向校验，兼顾效率和准确性'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
通用大模型的推理、知识、编程能力已达到较高水平，但处理长周期复杂任务时，需要持续和文件、工具、信息源交互，还要维护状态、故障恢复、交付可验证结果，现有Agent方案多把工具调用当附加能力，或仅靠简单多Agent对话协作，无法稳定落地真实工作流，小模型也很难达到前沿大模型的任务处理效果。

### 方法关键点
- 双扩展路径：①环境扩展：覆盖文件、搜索、代码三类可执行环境，统一任务契约定义状态、动作、转移、验证规则，覆盖33个领域、318个职业场景的训练环境；②Agent协作扩展：训练模型自带任务分解、子任务委派、异步结果整合、动态重规划能力，配套自组织Agent Team架构，支持显式任务看板、异步人工干预、不对称定向验证、自适应算力分配、证据落地合成5项新增能力。
- 统一执行底座AgentOS：维护持久化工作空间、依赖溯源图、任务状态，支持上下文分级压缩、预算友好的优雅终止、可中断续跑，对齐训练和推理的执行契约。
- 训练流程：统一SFT混合训练覆盖推理、工具调用、故障恢复、多Agent协作能力，再用Agentic RL基于环境轨迹和协作Trace优化长周期决策，围绕实际Failure Case迭代训练集分布。

### 关键结果
35B参数的Apodex 1.1 Mini在多类任务上达到前沿大模型性能区间，全量Agent Team版本在APEX-Agents专业任务集得分42.3，远超GPT-5.6 Sol的35.6、Claude Opus 5的39.9；在FrontierFinance金融任务集得分89.4，超出第二名10.1分；在FrontierScience-Research科研任务集得分63.3，是第二名的1.15倍。

### 最值得记住的一句话
Agent智能的核心评价单元不是孤立的回答质量，而是可验证的完成工作，环境和协作是比单纯堆模型参数更有效的规模化路径。
