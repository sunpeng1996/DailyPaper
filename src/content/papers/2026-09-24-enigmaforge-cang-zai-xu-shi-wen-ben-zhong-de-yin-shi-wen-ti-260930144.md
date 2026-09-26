---
title: 'EnigmaForge: The Question Is Hidden in the Story'
title_zh: EnigmaForge：藏在叙事文本中的隐式问题发现能力评测基准
authors:
- Daniel Eisner
arxiv_id: '2609.30144'
url: https://arxiv.org/abs/2609.30144
pdf_url: https://arxiv.org/pdf/2609.30144
published: '2026-09-24'
collected: '2026-09-26'
category: Eval
direction: LLM能力评测 · 隐式问题发现
tags:
- LLM Benchmark
- Procedural Generation
- Problem Discovery
- Intuition Evaluation
- SAT Solver
one_liner: 提出无显式问题的程序化生成逻辑谜题基准，量化LLM主动问题发现与解决的直觉能力
practical_value: '- 构建电商/Agent场景的推理能力测试用例时，可复用「SAT solver验证唯一解+全线索必要」的构造方法，避免用例歧义导致评测结果失真

  - 面向电商客服、模糊搜索等场景的LLM选型，可参考intuition指标，优先选择隐式需求识别能力更强的模型

  - 设计推荐系统的用户隐式意图挖掘任务时，可参考该基准的无显式问题任务范式，更贴近真实用户未明确表达需求的场景'
score: 6
source: arxiv-cs.AI
depth: abstract
---

### 动机
现有LLM基准均提供明确问题，无法衡量模型在开放场景下主动发现潜在需求、推理解决问题的真实能力，且固定收集的测试集易过拟合，无法持续复用。
### 方法关键点
1. 程序化生成嵌套在信件、收据等叙事片段中的逻辑谜题，通过SAT solver验证解唯一，消融证明所有线索均为必要；
2. 核心指标为intuition（无显式问题下的任务成功率），辅助指标为世界事实还原率；
3. 支持无限生成测试实例，避免数据泄露。
### 关键结果
25个前沿LLM+4个基线在600个实例上测试：① intuition指标差异达22倍，而事实还原率差异仅1.6倍，两者排序相关性极低；② 多数模型有显式问题时表现提升9-37分，Grok-4.6无差异，GPT-6 Sol无显式问题时表现提升14.2%；③ 部分模型被内容过滤拦截，将拒答判为失败的基准会混入过滤策略的干扰。
