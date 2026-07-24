---
title: 'One More Turn, Less Regret: A Regret-Based Multi-Turn Benchmark for LLMs''
  Clarification Policies'
title_zh: 基于后悔值的大语言模型多轮澄清决策基准RegretBench
authors:
- Minh Ngoc Ta
- My Anh Tran Nguyen
- Duong D. Nguyen
- Yuxia Wang
- Preslav Nakov
affiliations:
- MBZUAI
- BKAI Research Center, Hanoi University of Science and Technology
- INSAIT, Sofia University "St. Kliment Ohridski"
arxiv_id: '2607.21143'
url: https://arxiv.org/abs/2607.21143
pdf_url: https://arxiv.org/pdf/2607.21143
published: '2026-07-23'
collected: '2026-07-24'
category: Eval
direction: Agent 多轮澄清决策评测
tags:
- Clarification Policy
- Multi-turn Dialogue
- Benchmark
- Regret Metric
- Conversational Agent
one_liner: 提出政策级评估LLM多轮澄清行为的RegretBench基准，引入后悔值衡量决策性价比
practical_value: '- 电商会话式导购/搜索的澄清策略可复用其 reward 设计：结合意图匹配准确率、交互轮次成本、无效提问惩罚，平衡推荐准确性和用户体验

  - 多轮澄清prompt优化可参考文中方案：Explanation类引导prompt能同时提升意图识别准确率和交互效率，One-shot提示适合需压缩轮次的场景

  - 澄清策略的评测可直接复用其后悔值指标：对比最优参考策略的性能gap，替代仅看最终准确率的单一评估逻辑，避免过度澄清或过早应答的问题

  - 产品推荐场景的歧义意图建模可借鉴CIG（澄清交互图）结构：预先定义候选意图集、歧义维度、有效澄清动作，提升离线策略迭代效率'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有LLM澄清行为评测多聚焦单轮提问质量或固定轮次后的准确率，无法衡量多轮决策的合理性：过早应答容易误解用户意图，过度提问会增加用户交互成本，相似准确率的模型在交互效率、鲁棒性上可能存在巨大差异，亟需政策级的全链路评测框架。
### 方法关键点
- 定义澄清交互图（CIG）数据结构：对每个歧义用户请求，定义隐藏候选意图集、区分意图的语义维度、支持的澄清动作集，实现自由交互和语义状态追踪的解耦
- 设计全对话reward函数：整合最终意图匹配效用、交互token成本、无效/冗余提问惩罚，综合衡量澄清策略的整体价值
- 引入后悔值（Regret）指标：将待评测策略和语义参考规划器的最优表现对比，量化当前策略的相对性能损失，避免不同实例歧义程度不同导致的评测偏差
- 覆盖开放域QA、电商产品推荐两类场景，内置cooperative、vague、contradictory三类用户persona模拟不同交互行为，支持鲁棒性评测
### 关键结果
在6664条CIG实例（4836条开放域QA、1451条条件QA、377条产品推荐）上测试10余款主流LLM：① 最终准确率相近的模型reward差异可达4.89，如K2Think V2准确率0.74但因过度提问和惩罚奖励为-4.23，而DeepSeek V4 Flash准确率0.73、奖励达0.61；② 简单prompt优化可提升3.5%的reward，Explanation提示同时提升准确率和效率，One-shot提示可降低11.3%的平均交互轮次；③ 模糊/矛盾用户persona下，模型reward最高下降29.2%，鲁棒性差异明显。

最值得记住的一句话：多轮澄清的核心不是问出合理的问题，而是在正确的时间问正确的问题，在意图明确时立刻停止。
