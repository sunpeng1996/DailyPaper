---
title: 'Never the Number: Structural Abstention for AI Systems Whose Answers Are Consumed
  as Fact'
title_zh: 面向事实消费场景的AI系统结构性弃权架构：规避不可信输出
authors:
- Zhelun
- Wu
affiliations:
- Apple Inc.
arxiv_id: '2608.13926'
url: https://arxiv.org/abs/2608.13926
pdf_url: https://arxiv.org/pdf/2608.13926
published: '2026-08-14'
collected: '2026-08-17'
category: Agent
direction: Agent系统可靠性 · 结构性弃权设计
tags:
- Hallucination
- Structural Abstention
- Agent Safety
- Text-to-SQL
- Reliable AI
one_liner: 提出生成外壳+确定性内核架构，通过结构性弃权避免事实类场景的AI幻觉输出
practical_value: '- 电商/广告业务的自助数据分析Agent可直接复用该架构：LLM仅负责语义理解、澄清引导、回复润色，所有指标查询走预定义模板的确定性编译路径，彻底消除指标幻觉，避免错误数据影响运营决策

  - 高风险Agent工具调用场景（如发券、改库存、投放预算调整）可扩展该架构：LLM仅负责生成动作提议，用户确认后才走预定义的确定性工具调用路径，不符合规则的请求直接拒绝，不做近似执行

  - 搜索/自助分析的Query推荐/Autocomplete场景，可仅从预定义可回答模板池召回候选，避免推荐系统无法回答的query，降低用户挫败感'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
LLM驱动的text-to-SQL、自助数据分析、Agent工具调用等「事实消费」场景下，模型生成的错误结果（如幻觉列、错误聚合）和正确结果无明显差异，若用户无法审计中间执行过程，错误会直接流入业务决策。依靠置信度校准的统计性弃权效果有限，尤其在企业级复杂schema场景下，通用text-to-SQL准确率暴跌至个位数，完全无法满足生产要求。

### 方法关键点
- 核心遵循「周界不变性」：可生成的组件仅能影响系统回答什么问题，绝对不能影响返回的数值/执行的动作
- 架构拆为两层：生成Shell负责语义理解、澄清话术生成、回复润色，错误仅增加一轮对话成本；确定性Kernel无任何生成组件，负责匹配预定义可回答模板、确定性编译查询/动作
- 采用结构性弃权：Kernel无法匹配的请求直接拒绝，无需置信度估计，从结构上让不可回答的请求无法被表示
- 增加用户确认环节：Kernel将待执行请求转化为用户可理解的自然语言描述，确认后才执行后续计算/调用

### 关键结果
该架构在Apple内部零售渠道数据分析场景落地2年，完全消除了不可感知的事实错误。对比基准：通用Code Agent在面向企业场景的Spider 2.0数据集上准确率仅21.3%（原Spider数据集上为91.2%）；在BEAVER企业私有仓库数据集上，通用模型端到端准确率接近0，即使提供黄金表和列映射也仅能达到个位数准确率，远达不到生产可用标准。

### 最值得记住的一句话
当AI输出的数值/动作会被直接用于决策且无法被用户审计时，宁可不回答，也不能输出错误结果，结构性弃权比优化模型准确率、做置信度校准更能保障生产可靠性。
