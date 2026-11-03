---
title: 'CogRSI: Evolving and Auditing Cognitive Reasoning Strategies'
title_zh: CogRSI：认知推理策略的演化与审计框架
authors:
- Yandan zheng
- Haoran Luo
- Xinliang Zhou
- Anhtuan Luu
affiliations:
- Nanyang Technological University
- Stanford University
- VinUniversity
arxiv_id: '2611.01113'
url: https://arxiv.org/abs/2611.01113
pdf_url: https://arxiv.org/pdf/2611.01113
published: '2026-10-31'
collected: '2026-11-03'
category: Agent
direction: Agent自演化 · 心智理论推理审计
tags:
- AgentSelfImprovement
- TheoryOfMind
- RecursiveSelfImprovement
- ReasoningAudit
- CounterfactualValidation
one_liner: 提出认知推理策略演化与审计框架，在心智理论任务上优于基线，同时发现86.7%自演化规则存在逻辑漏洞
practical_value: '- 可复用Agent自演化的准入机制：策略迭代时设置校准后的多桶测试阈值，比如文中3分精度阈值将有害更新占比从31.8%降至16.7%，可直接用到推荐排序、广告投放策略的灰度更新环节，降低负向风险

  - 多视角投票+仲裁的推理框架可迁移：针对用户意图识别、客诉语义理解等复杂场景，先做6路左右的温度采样，结果冲突时用预设业务规则仲裁，同token成本下可提升约4%的准确率

  - 自学习规则的审计方法可落地：生成式推荐的文案规则、用户分群规则不能仅靠线上指标评估，可将自然语言规则转成可执行代码，在构造的边界case集上验证，避免出现类似文中86.7%规则存在逻辑漏洞却无法通过精度发现的问题'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有递归自改进（RSI）Agent仅通过任务精度判断是否保留新策略，无法确认策略是否具备跨场景泛化性、逻辑是否严谨。尤其是心智理论等需要因果推理的任务，模型极易学到仅适配训练数据的表面规则，存在大量隐性漏洞，落地时容易出现边界case错误。
### 方法关键点
- 接地阅读器：给对话/文本的每个片段标注感知到该内容的角色，同时输出4路带标注视角、2路原始文本的采样结果，当结果冲突或票数差距过小时，调用预设原则仲裁
- 反事实引导的策略演化：自动迭代规则库，每轮生成的新规则需要满足多批测试集精度提升≥3个校准阈值，带门控的版本额外要求通过反事实测试对，仅保留符合要求的规则
- 语义审计：将每条学习到的自然语言规则通过两个独立大模型转成可执行代码，在6000个覆盖睡觉、撒谎、偷看等训练未出现的构造场景上验证，存在共同反例的规则判定为无效
### 关键结果
- 带专家规则的CogRSI在同token成本下，比self-consistency（k=9）的平均精度高4.4个百分点（73.1% vs 68.7%），在5个不同大小的模型骨架上均保持优势
- 自演化策略具备跨数据集迁移能力：在未见过的800条BigToM测试集上，所有自学习规则的精度都超过专家规则，最高达96.6%
- 86.7%的自学习规则存在逻辑漏洞，仅靠任务精度和反事实门控无法识别这类问题，精度表现好的规则也可能在边界场景下出错

> 最值得记住：自改进系统不能仅靠任务精度判断策略好坏，必须同时验证策略的实际行为和逻辑正确性
