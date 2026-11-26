---
title: What Is a Theory Worth to an LLM Solver? Measuring, Inducing, and Merging Theories
  in Context
title_zh: LLM求解器中上下文理论的价值度量、诱导与合并方法
authors:
- Jun Gao
- Shuchao Bi
affiliations:
- Meta Platforms, Inc.
arxiv_id: '2611.34751'
url: https://arxiv.org/abs/2611.34751
pdf_url: https://arxiv.org/pdf/2611.34751
published: '2026-11-25'
collected: '2026-11-26'
category: Reasoning
direction: LLM推理 · 上下文知识利用
tags:
- LLM Reasoning
- In-Context Learning
- Theory Induction
- Knowledge Merging
- Controlled Evaluation
one_liner: 通过长度匹配受控实验量化上下文理论的价值，验证LLM可诱导合并未知数学理论
practical_value: '- 搭建Agent推理系统时，相同长度的上下文优先放领域通用规则而非案例，规则的准确率增益、推理成本节约远优于样例，可降低KV
  cache占用、缩短推理耗时，适合电商搜索query理解、推荐品类匹配等固定规则场景

  - 诱导领域私有规则时，强制模型先在小样本上做代码/数据探索再输出通用规则，可大幅提升规则有效性，比如大促满减计算、库存分配规则的自动生成

  - 零散运营规则/领域知识可通过强LLM合并为统一规则库，效果优于单条规则或机械规则选择，适合整合多来源的推荐选品、流量调控规则

  - 验证规则有效性时以下游任务的准确率/成本增益为核心标准，不要依赖人工评判规则表述的合理性，避免出现形式正确但无法落地的问题'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
LLM执行复杂推理任务时推理链长、token消耗高，现有方案无法量化上下文内的通用理论（规则）能带来多少准确率提升与成本节约，也无法区分模型生成规则是诱导出新知识还是回忆训练数据内容，缺少受控的理论价值度量方法。

### 方法关键点
- 设计长度匹配对照协议，所有上下文输入token数完全一致，对比无理论、oracle人工理论、无关文本、通用提示、同方法样例等不同条件的效果，排除长度干扰
- 提出recovery ratio R指标，衡量诱导理论覆盖oracle理论增益的比例
- 构造3个未公开发表的自定义概率问题家族（planted theorem），验证模型预训练时无相关知识，彻底区分规则诱导与训练数据回忆
- 设计「探索-诱导-合并」流程：诱导模型需至少完成3次代码探索验证后才能输出理论，再用强LLM合并多份零散的局部理论，输出统一规则

### 关键结果
- 实验覆盖2类经典概率问题+3类自定义planted问题，对比基线包括无理论、无关文本、样例、通用提示
- Qwen3-14B在模式等待时间问题上，加入oracle理论后pass@1从0.37升至0.83，正确解的中位token从10.2k降至6.3k，相同长度的样例无任何增益
- 强诱导模型在F1 planted问题上恢复60%的oracle增益，合并多份局部理论后恢复率从单条最高47%升至61%
- 长token预算下，理论的增益几乎全部来自节约推理token，所有条件下完成的样本准确率均达98%以上

最值得记住的一句话：理论的价值在于它能节约的推理量，而非它本身的表述合理性。
