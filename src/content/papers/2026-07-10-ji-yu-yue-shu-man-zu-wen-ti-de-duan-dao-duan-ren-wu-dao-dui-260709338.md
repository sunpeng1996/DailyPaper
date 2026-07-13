---
title: Towards Detecting Inconsistencies in End-to-end Generated TODs
title_zh: 基于约束满足问题的端到端任务导向对话不一致性检测
authors:
- Tiziano Labruna
- Giovanni Bonetta
- Bernardo Magnini
affiliations:
- Fondazione Bruno Kessler
arxiv_id: '2607.09338'
url: https://arxiv.org/abs/2607.09338
pdf_url: https://arxiv.org/pdf/2607.09338
published: '2026-07-10'
collected: '2026-07-13'
category: Agent
direction: 对话Agent 知识库一致性校验
tags:
- Task-Oriented Dialogue
- Constraint Satisfaction Problem
- Hallucination Detection
- Knowledge Alignment
- LLM Evaluation
one_liner: 将任务导向对话一致性建模为约束满足问题，实现高准确率的对话幻觉检测
practical_value: '- 电商客服、导购类对话Agent可复用这套CSP约束框架，把商品库作为KB，定义槽值匹配、上下文一致性、商品属性匹配三类约束，快速检测LLM生成回复的幻觉

  - 变量提取可用轻量级LLM+结构化输出prompt实现，配合开源CSP求解器（如Chuffed）做一致性校验，工程落地成本低，准确率高于LLM自检

  - 生成式推荐场景下，可将用户历史行为、推荐商品属性作为约束，用CSP校验生成的推荐话术、商品列表是否符合用户需求和商品实际属性，降低推荐幻觉'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
端到端生成的任务导向对话（TOD）是电商客服、智能导购等场景的核心技术，但LLM生成回复容易出现与领域知识库不符、上下文逻辑矛盾的幻觉问题，比如给用户推荐不存在的商品、前后回复属性冲突，直接导致任务失败，传统对话评估方法难以系统性检测这类全局一致性问题。

### 方法关键点
- 将TOD一致性建模为约束满足问题（CSP）：把对话中提到的槽值、实体数量作为变量，定义三类共6条通用约束：语言学约束（槽值与语义类型匹配）、对话约束（上下文同槽值一致、同句同类型槽值不重复）、领域约束（知识库实体存在性、数量匹配）
- 检测pipeline分四步：用GPT-4o提取对话中的变量→根据通用约束模板实例化当前对话的约束集→用CSP求解器计算所有合法变量赋值→将原对话的变量赋值与合法解对比，判断是否一致，同时给出最小修改方案

### 关键实验
数据集基于MultiWOZ 2.3构建108组平衡的对话-KB对，另用950组对话测试LLM生成一致性；对比baseline包括随机baseline、基于标注的局部/全局CSP、基于GPT-4o变量提取的端到端CSP。关键结果：基于全局标注的CSP准确率达91.6%，端到端全自动pipeline准确率75.9%；测试主流LLM生成TOD的全局一致性准确率最高仅14%（GPT-4o/GPT-o1），其中领域数量匹配约束是最易出错的点。

### 核心结论
仅靠LLM自身能力很难保证TOD的知识库一致性，结合CSP的显式约束校验是低成本提升对话可靠性的有效方案。
