---
title: 'TACT: Taxonomy-Aligned Post-Training for Pedagogically Adaptive English Tutoring'
title_zh: TACT：面向教学自适应英语辅导的分类体系对齐后训练
authors:
- Dongjie Yang
- Siyan Lin
- Leixian Shen
- Rui Sheng
- Huamin Qu
- Zixin Chen
arxiv_id: '2608.03952'
url: https://arxiv.org/abs/2608.03952
pdf_url: https://arxiv.org/pdf/2608.03952
published: '2026-08-04'
collected: '2026-08-06'
category: Agent
direction: 自适应对话Agent 分类体系对齐训练
tags:
- LLM Fine-tuning
- Conversational Agent
- Policy Optimization
- Adaptive Tutoring
- Taxonomy Alignment
one_liner: 提出对齐教学策略分类体系的ESL辅导Agent后训练框架，性能较基线提升20.3%
practical_value: '- 垂直领域对话Agent（如电商导购、客服Agent）研发可先基于领域沉淀的经验构建行为分类体系，再对齐标注数据训练，效果优于纯模仿参考回复

  - 小参数垂直模型优化可采用「SFT基础对齐 + 领域适配的Group Relative Policy Optimization策略优化」的两阶段流程，兼顾效果与泛化性

  - 垂直场景Agent评估可构建策略均衡的诊断基准集，比通用benchmark更能反映模型在实际业务场景的适配效果'
score: 7
source: arxiv-cs.AI
depth: abstract
---

### 动机
现有LLM面向ESL学习者的对话辅导仅能产出流畅回复，未对齐人类教学的自适应策略，已有教学原则多为任务特异性，未充分融入LLM辅导系统的训练与评估流程。
### 方法关键点
1. 基于领域文献构建两类互补分类体系：含13种回复策略的导师策略分类、从行为类型与状态双维度刻画学习者的学生行为分类；
2. 标注260份真实师生对话的32379条数据，结合质控增强数据构建TACTCorpus；
3. 先对Qwen3.5-4B做SFT对齐，再用分类对齐的Group Relative Policy Optimization优化，优先保障教学脚手架质量而非仅模仿参考回复。
### 关键结果
在78个真实辅导场景构成的策略均衡基准TACTBench上，性能较 backbone 提升20.30%，优于所有评测的专有基线，同时保留原有通用教育基准性能；50名学习者双盲测试中综合评分最高。
