---
title: 'When Models Edit Too Much: On the Fidelity of Minimal Code Edits'
title_zh: 模型过度编辑问题：代码最小修改的保真度研究
authors:
- Tongyao Zhu
- Wei Hern Lim
- Min-Yen Kan
affiliations:
- National University of Singapore
arxiv_id: '2609.04061'
url: https://arxiv.org/abs/2609.04061
pdf_url: https://arxiv.org/pdf/2609.04061
published: '2026-09-03'
collected: '2026-09-05'
category: LLM
direction: LLM代码编辑 · 保真度优化
tags:
- LLM
- Code Editing
- Evaluation
- Reinforcement Learning
- Supervised Fine-Tuning
one_liner: 提出代码编辑保真度评估框架，验证提示指令与RL训练可降低LLM代码修复过度编辑问题
practical_value: '- 做LLM辅助代码修复/改写场景时，可在prompt中加入「尽可能保留原逻辑，仅做最小必要修改」的指令，能同时提升准确率和可读性

  - 针对最小修改类生成任务（如推荐文案微调、Query改写），后训练优先选RL而非SFT，避免过拟合到见过的修改模式，提升跨域泛化性

  - 评估LLM改写类任务效果时，除准确率外可新增超额编辑距离、新增认知复杂度两个指标，衡量输出的实际可用性'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
当前LLM代码修复仅关注正确性，普遍存在过度编辑问题，额外修改会提升代码review成本、破坏原有逻辑，现有评估体系缺少对编辑保真度的衡量。
### 方法关键点
1. 基于400个BigCodeBench问题，在参考代码中注入可控AST级错误，构建带已知最小补丁的评估数据集；
2. 测试prompt中加入保留原代码指令的优化效果；
3. 对比SFT和RL两种后训练方式对最小编辑能力的提升效果。
### 关键结果数字
1. 即使GPT-5.5这类强模型也普遍存在过度编辑，高Pass@1可同时伴随大量不必要修改；
2. 加入保留指令后，平均超额Levenshtein距离从0.195降至0.131，新增认知复杂度降26.6%，Pass@1提升2.3个点；
3. SFT易过拟合到见过的错误模式，RL的跨域编辑保真度和性能保留的权衡最优。
