---
title: 'Athanor: An Agent-Native System for Autonomous Post-Training Research'
title_zh: Athanor：面向自主大模型后训练研究的Agent原生系统
authors:
- Yufa Zhou
- Yichen Wang
- Jiakun Fan
- Ziqi Shu
- Zhichao Liu
- Anru R. Zhang
- Neiwen Ling
- Zijun Wei
affiliations:
- ByteDance
- Duke University
- The University of Chicago
- Virginia Tech
arxiv_id: '2610.21055'
url: https://arxiv.org/abs/2610.21055
pdf_url: https://arxiv.org/pdf/2610.21055
published: '2026-10-14'
collected: '2026-10-16'
category: Agent
direction: Agent 自主大模型后训练系统优化
tags:
- Agent System
- Post-Training
- Autonomous Research
- LLM Fine-Tuning
- Multi-Agent Collaboration
one_liner: 4个Claude Opus 5.5 Agent组成的团队104小时将Qwen3-4B-Base后训练至官方Instruct版本水平
practical_value: '- 多Agent协作任务可复用「决策与执行分离+状态外部化」架构：Agent仅负责策略决策，底层工程执行、资源调度由统一系统封装，大幅降低Agent工具调用复杂度，适合推荐系统自动调优、广告素材自动迭代这类长周期迭代场景

  - 可借鉴多Agent无预设角色的协作机制：设置统一的结果沉淀、checkpoint共享、笔记互通模块，仅靠公开可验证的评估反馈就能驱动多Agent自发复用其他成员的有效方案，适合大模型推荐prompt调优、召回策略迭代这类多思路试错场景

  - 长周期模型迭代任务可参考全链路可回溯设计：记录每一次实验的代码、数据、参数、效果，方便复现和归因，减少垂域大模型SFT、推荐排序模型调优等场景的重复实验成本'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
大模型后训练是塑造指令遵循、推理、编码、对齐能力的核心环节，现有后训练研究依赖人力开展数据配比、算法迭代、超参调优，迭代成本高且全流程难以复现；已有的Agent辅助训练方案多限定单任务、允许调用教师模型，无法实现完全自主的通用模型后训练。

### 方法关键点
- 核心架构遵循三大设计原则：决策与执行分离，Agent仅负责研究决策（数据选择、算法修改、超参调整等），底层训练、评估、资源调度由系统自动封装完成；研究状态全外部化，所有请求、结果、checkpoint谱系、交互记录持久化存储，支持跨Agent共享和全链路实验回溯；研究循环异步高效，支持多实验并行执行，结果实时推送减少空闲等待。
- 给Agent完全研究自主权，仅提供基础starter代码、去污染的公开数据集、冻结的开发集评估接口，禁止调用外部教师模型，设置Agent无感知的held-out测试集保证结果无泄露。
- 天然支持多Agent协作，Agent可自由读取队友的实验记录、checkpoint、笔记，自发复用经评估验证有效的方案，无需预设协作规则。

### 关键实验
4个Claude Opus 5.5 Agent组成团队，基于Qwen3-4B-Base开展104小时自主后训练，总花费约1.2万美元；最终模型在开发集得分67.3（官方Qwen3-4B-Instruct-2507为66.5），在Agent无感知的held-out测试集得分48.2（官方Instruct版本为47.9），效果追平甚至超过官方发布的通用Instruct模型。分析显示Agent会自发组合SFT、GRPO、权重合并、自蒸馏等已知方法，21小时后所有最优模型均融合了多个Agent的训练成果。

### 最值得记住的一句话
当前前沿Agent已经具备足够的工程与研究能力，消除执行层摩擦后即可自主完成复杂的大模型后训练任务，达到人类专业团队的产出水平。
