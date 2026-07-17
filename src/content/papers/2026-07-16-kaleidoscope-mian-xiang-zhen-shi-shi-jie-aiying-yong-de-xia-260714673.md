---
title: 'Project Kaleidoscope: Contextual, Human-Aligned Evaluation for Real-World
  AI Applications'
title_zh: Kaleidoscope：面向真实世界AI应用的上下文感知人类对齐评估框架
authors:
- Leanne Tan
- Rohan Jaggi
- Shaun Khoo
- Roy Ka-Wei Lee
affiliations:
- GovTech Singapore
- National University of Singapore
- University of British Columbia
arxiv_id: '2607.14673'
url: https://arxiv.org/abs/2607.14673
pdf_url: https://arxiv.org/pdf/2607.14673
published: '2026-07-16'
collected: '2026-07-17'
category: Eval
direction: AI应用评估 · 人类对齐自动化评估
tags:
- LLM Evaluation
- Human Alignment
- Automated Scoring
- Context-aware Eval
- LLM-as-Judge
one_liner: 提出融合persona测试生成、上下文评分规则、阈值门控LLM打分的可落地AI应用评估工作流
practical_value: '- 评估Agent/LLM导购应用时，可复用该框架的persona测试用例生成逻辑，匹配平台不同用户分层的需求

  - 可引入「LLM打分阈值门控」机制：LLM评委和人工标注一致性达预设阈值时才启用自动评分，平衡效率和准确性

  - 业务侧可基于自身合规、体验要求定制评估维度和打分规则，替代通用benchmark，更贴合实际业务场景'
score: 7
source: arxiv-cs.HC
depth: abstract
---

### 动机
真实场景AI应用落地的核心瓶颈是评估：公开benchmark无法匹配业务特定的用户、上下文、合规要求，纯人工标注规模大、成本高，尤其是需要满足本地政策、治理要求的场景缺少适配的评估方案。
### 方法关键点
提出Kaleidoscope集成评估工作流，三大核心模块：1）基于persona生成场景化测试用例；2）配置应用专属的上下文打分规则；3）设计可靠性门控的自动打分机制，仅当LLM评委和人工标注的一致性达到预设阈值时才启用LLM自动评分，其余场景走人工审核，流程可追溯、可迭代。
### 关键结果数字
在4个组织用例的3周试点、覆盖4个领域14个评估维度的108条标注Q&A对的实验中，验证了该端到端可靠自动评分方案的实用性。
