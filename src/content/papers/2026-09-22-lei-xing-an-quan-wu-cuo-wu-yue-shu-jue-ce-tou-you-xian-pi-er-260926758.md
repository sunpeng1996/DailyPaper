---
title: 'Type-Safe Is Not Error-Free: A Constrained Decision Head Follows the Option
  Name, Not the Rubric Bound to It'
title_zh: 类型安全≠无错误：约束决策头优先匹配选项名称而非绑定规则
authors:
- Yu Sun
- Junhao Xu
affiliations:
- National University of Singapore
- Fudan University
arxiv_id: '2609.26758'
url: https://arxiv.org/abs/2609.26758
pdf_url: https://arxiv.org/pdf/2609.26758
published: '2026-09-22'
collected: '2026-09-23'
category: LLM
direction: LLM约束决策头行为分析
tags:
- Constrained-Decision-Head
- Typed-Decision-Model
- LLM-Reliability
- Output-Calibration
- Decision-Ranking
one_liner: 发现带约束决策头的类型化模型优先匹配选项名语义而非绑定规则，存在符合格式的隐性错误
practical_value: '- Agent/LLM工作流决策模块设计时，避免使用带语义极性的选项名（如yes/no），改用无意义随机字符串/中性ID，后端再映射到业务规则，可完全消除选项名语义干扰导致的决策反转

  - 电商审核、商品分类等LLM约束分类任务，可优先采用对全选项span做mean-pooling的决策头架构，比普通决策头的选项名语义干扰降低4.1倍

  - 上线约束输出类LLM服务前，必须增加选项名-规则交换测试，排查是否存在优先响应选项名而非规则的隐性错误，避免符合格式的输出完全不符合业务逻辑'
score: 7
source: arxiv-cs.AI
depth: abstract
---

### 动机
类型化决策模型输出强制符合预定义schema，被广泛用于Agent、工作流自动决策等直接对接软件的场景，但类型安全无法保证模型对选项的理解符合设计预期。
### 方法关键点
针对3款带约束决策头的开源模型，仅交换选项名与绑定的定义规则（输入问题、规则文本、选项名集合完全不变），对比不同选项名语义、决策头架构下的决策变化。
### 关键结果
1. 二元选项名从0/1改为no/yes后交换绑定规则，每百样本70.4个决策反转，AUC从0.94降至0.23，效应是中性对照组的7.4倍以上，且随选项数量增加增强
2. 用无意义随机字符串做选项名时，无该类错误且精度不下降
3. 全选项span mean-pooling架构的决策头受干扰程度比普通架构低4.1倍
4. 所有场景下类型错误率始终为0，错误隐蔽性极强
