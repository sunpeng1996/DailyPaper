---
title: 'AdviSD: Learning to Advise Frontier LLMs via Targeted Multi-Turn Self-Distillation'
title_zh: AdviSD：基于定向多轮自蒸馏的前沿大模型指导训练方法
authors:
- Rishabh Agrawal
- Hejie Cui
- Shasha Li
- Shanchan Wu
- Sercan Ö. Arık
affiliations:
- Google
- University of Southern California
arxiv_id: '2609.38142'
url: https://arxiv.org/abs/2609.38142
pdf_url: https://arxiv.org/pdf/2609.38142
published: '2026-09-29'
collected: '2026-09-30'
category: Agent
direction: Agent 黑盒大模型外接指导训练
tags:
- Self-Distillation
- LLM Agent
- GRPO
- Transfer Learning
- Black-box LLM
one_liner: 提出定向自蒸馏方法训练小尺寸advisor，无需改动冻结大模型权重即可提升其多轮任务表现
practical_value: '- 电商/客服Agent场景可直接复用架构：无需微调API调用的商用大模型，仅训练小尺寸advisor即可提升其工具调用、多轮任务完成率，大幅降低适配成本

  - 自蒸馏数据筛选trick可复用：通过对比有无目标干预下的模型响应得分差筛选训练样本，过滤冗余无影响的修正，避免共享参数被无效样本干扰，适配所有小模型蒸馏场景

  - 跨LLM部署场景可参考迁移结论：AdviSD训练的advisor无需重训即可跨大模型版本、跨家族迁移，适合业务多LLM服务并存的场景，减少重复训练开销'
score: 9
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
前沿大模型多以API形式提供，无法微调权重，外接小尺寸advisor可指导冻结大模型（executor）执行任务，但现有训练方案会学习所有反馈修正，其中大量冗余修正（executor本身无需指导即可正确执行的步骤修改）会通过共享参数干扰有用知识的学习，限制最终效果上限。
### 方法关键点
- 结合GRPO强化学习与定向自蒸馏，将修正提案与学习样本选择解耦，仅保留对执行结果有实际影响的修正做监督
- 用预更新advisor分别计算**有/无 issued advice**时executor已记录响应的平均对数得分差，差值大于预校准阈值的修正才进入蒸馏训练，无需额外调用executor获取新响应
- 反馈增强的预更新advisor作为teacher（可见全量交互反馈），仅可见原始上下文的训练advisor作为student，蒸馏损失作为GRPO损失的补充项优化
### 关键结果
- 以Qwen3-8B为advisor，分别指导Gemini 3.7 Flash、Claude Sonnet 4.6，在BFCL-v3、EnvScaler基准测试上，AdviSD比纯GRPO训练的advisor高4.2-6.4个百分点（BFCL-v3）、3.9-5.1分（EnvScaler）
- 无重训跨域迁移时，比纯executor执行高2.7-3.6分，跨大模型家族迁移时比迁移的GRPO高3.1个百分点
### 核心结论
训练外接指导模型时，仅学习能实际改变冻结大模型执行行为的修正，效果远好于学习全量修正
