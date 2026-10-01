---
title: 'Org-Agent: Beyond Personal Assistants Towards Organizational Agents'
title_zh: 面向组织场景的多用户共享Agent框架Org-Agent
authors:
- Luyao Zhuang
- Yujing Zhang
- Zijin Hong
- Yilin Xiao
- Xiao Huang
affiliations:
- The Hong Kong Polytechnic University
arxiv_id: '2609.34392'
url: https://arxiv.org/abs/2609.34392
pdf_url: https://arxiv.org/pdf/2609.34392
published: '2026-09-27'
collected: '2026-10-01'
category: Agent
direction: 多用户Agent · 组织场景协同框架
tags:
- Multi-User Agent
- Organizational Agent
- Task Scheduling
- Memory Management
- Constraint Reasoning
one_liner: 提出约束中心的三阶段组织Agent框架，支持跨用户协同决策与跨交互记忆知识复用
practical_value: '- 电商多角色协同场景（如运营、供应链、商家联合活动排期）可复用TDG任务依赖图+拓扑排序的调度逻辑，规避多角色需求冲突、权限越界问题

  - 多用户会话记忆复用场景（如客服团队承接同一企业客户的多轮咨询）可借鉴证据获取工具的「语义+lexical混合排序+元数据过滤+关系遍历」设计，提升跨会话历史信息召回准确率

  - 弱推理能力的开源LLM做Agent时，可通过显式约束规则+工具调用补全推理短板，无需完全依赖大模型原生能力，降低落地成本'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有LLM Agent多为单用户场景设计，无法适配组织级多用户协同需求：一方面要协调多用户请求完成联合决策，另一方面要复用跨用户交互的历史知识，同时还要满足身份权限、信息时效、冲突解决三类组织约束。现有方案要么简单拼接全量上下文无视约束，要么单用户独立处理忽略跨用户依赖，实际效果难以满足业务要求。
### 方法关键点
- 三阶段约束驱动推理框架：① 任务分解为原子子任务，动态构建带依赖关系的有向无环**任务依赖图（TDG）**，实时更新新用户输入带来的任务变更；② 依赖感知调度：对TDG做拓扑排序生成执行顺序，同层无依赖子任务可并行执行；③ 约束感知执行：调用两类工具完成子任务，证据获取工具实现「混合相似度排序+元数据条件过滤+关联关系遍历」的历史记录召回，内存管理工具读写执行过程的中间结果与结构化信息。
### 关键实验
- 数据集：在GroupMemBench（跨用户记忆问答，745个样本）和MUSES-Bench（跨用户交互决策，1183个样本）两个公开基准上测试
- 效果：GroupMemBench上平均准确率达44.03%，较最强基线Hindsight高5.24pp，较BM25高6.31pp；MUSES-Bench上以GPT-4o-mini为骨干时平均得分72.39%，较原生Agent高8.27pp，会议调度成功率提升23.15pp；用户规模增长时性能衰减速度仅为原生Agent的1/5~1/2
### 核心结论
组织级多用户Agent的核心不是单用户能力的简单扩容，而是以约束为核心显式建模任务依赖与执行规则，才能兼顾协同效率与合规性
