---
title: 'How Feedback-Free Self-Evolution Reshapes Agent Skills: A Systematic Study'
title_zh: 无反馈自进化重塑Agent技能的系统研究
authors:
- Litao Guo
- Man Chen
- Xinli Xu
- Jinsong Zhou
- Zixin Zhang
- Ying-Cong Chen
affiliations:
- The Hong Kong University of Science and Technology (Guangzhou)
- The Hong Kong University of Science and Technology
- Knowin
arxiv_id: '2611.25534'
url: https://arxiv.org/abs/2611.25534
pdf_url: https://arxiv.org/pdf/2611.25534
published: '2026-11-18'
collected: '2026-11-24'
category: Agent
direction: Agent自进化 · 技能优化
tags:
- Agent Self-Evolution
- Skill Optimization
- LLM Agent
- Feedback-Free
- SkillDiff
one_liner: 系统揭示无反馈Agent技能重写的性能衰减机制，提出无改动提效方法SkillDiff
practical_value: '- 业务Agent技能库迭代时严禁无反馈递归重写，30轮重写平均降低15pp任务通过率，电商下单、客服流程等核心技能必须保留专家原始内容

  - 可复用SkillDiff思路：对专家录入的业务技能，先让模型仅基于主题生成10份自写技能，对比筛选出模型不会主动生成的核心规则（如优惠叠加规则、违禁回复要求），加高亮标签提示Agent优先执行，实测平均提升4.8pp通过率

  - 做技能压缩、跨模型适配时优先保护不属于模型先验的独有知识，该部分内容丢失是性能下降的核心原因，恢复该部分可找回80%以上的性能损失'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前LLM Agent普遍依赖专家撰写的技能文档支撑复杂任务执行，技能适配、压缩、迭代场景常采用无反馈重写，但该操作对技能价值的影响无系统研究，存在「适配模型提效」或「侵蚀专家知识掉效」两种可能性，亟需明确演化机制。

### 方法关键点
- 实验设计：选择6款主流LLM对专家技能递归重写30轮，全程无任务反馈、执行结果或外部校验，同一模型使用重写后的技能执行任务测试性能
- 先验度量：让模型仅基于技能主题生成10份自写技能作为该主题的模型先验，将原技能拆分为独立条目，对比标注哪些条目属于先验外知识
- 因果验证：对30轮重写后的技能，分别恢复先验外条目、先验内条目、全部丢失条目，对比性能恢复幅度验证衰减原因
- 优化方法SkillDiff：无需改动技能原文，仅对先验外条目标注[FOCUS]标签，提示Agent严格执行

### 关键结果
在SkillsBench（87个跨域任务）、LogicBench（760道逻辑题）、MedCalc-Bench（1100道医疗计算题）上测试：30轮无反馈重写后，技能平均通过率分别下降14.6pp、14.7pp、11.1pp，LogicBench上重写后效果与无技能相当；先验外条目30轮后仅23.1%留存，先验内条目留存率达84.2%；恢复先验外条目可找回80%以上的性能损失，SkillDiff在原技能基础上平均提升4.8pp通过率。

**最值得记住的一句话**：专家技能的核心价值是模型不会主动生成的先验外知识，无反馈重写会优先丢失这部分知识。
