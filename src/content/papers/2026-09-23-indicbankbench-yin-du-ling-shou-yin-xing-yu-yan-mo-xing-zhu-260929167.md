---
title: 'IndicBankBench: Evaluating Safety and Reliability of Language Model Assistants
  in Indian Retail Banking'
title_zh: IndicBankBench：印度零售银行语言模型助手安全与可靠性评测基准
authors:
- Suvradip Paul
- Chandra Bhushan
- Harsh Sharma
- Nitin Kukreja
- Yatharth Dedhia
- Keyur Doshi
- Prashant Devadiga
affiliations:
- National Payments Corporation of India
arxiv_id: '2609.29167'
url: https://arxiv.org/abs/2609.29167
pdf_url: https://arxiv.org/pdf/2609.29167
published: '2026-09-23'
collected: '2026-09-28'
category: Eval
direction: 银行垂直领域 LLM 安全可靠性评测
tags:
- LLM-Evaluation
- Banking-Assistant
- Safety-Benchmark
- Tool-Use-Evaluation
- Reliability-Metric
one_liner: 推出含799个用例的印度零售银行评测基准，分四阶段评估LLM银行助手的安全与可靠性
practical_value: '- 高可靠性垂直Agent（如电商交易助手、客服）可复用分阶段评测框架：先做安全、工具调用的确定性检查，仅歧义场景用窄逻辑消解，语义层面用LLM
  judge评估，降低评测成本

  - 涉及资损的交互场景（如电商退款、改绑操作）可采用strict pass^3 指标（多次测试全通过）替代单次/至少一次成功指标，避免高估系统稳定性，降低线上故障风险

  - 构建垂直领域评测集时，可覆盖重复索要已有信息、上下文过期、实体匹配错误等易被忽略的细粒度错误场景，提升评测全面性'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有银行LLM助手评测仅关注最终响应，会遗漏重复索要已有信息、依赖过期上下文、选错账号、正确声明后输出非法值等隐性错误，缺乏零售银行场景下的多维度可靠度评测基准。
### 方法关键点
构建共799个用例的IndicBankBench，覆盖5个业务操作域、1个能力/拒答域、20个核心评测维度；分四阶段评测：安全检查、工具调用与动作正确性、响应充足性、建议质量，其中工具调用与大部分安全检查为确定性逻辑，仅写操作前确认的歧义场景用窄范围消解器，语义响应充足性由独立LLM judge评估；提出strict pass^3 指标，要求同一用例3次测试全通过才算成功。
### 关键结果
11个参评模型的strict reliability区间为43.7%~58.2%，而至少一次成功的指标区间为60%~74%，证明后者会显著高估系统的实际可靠表现。
