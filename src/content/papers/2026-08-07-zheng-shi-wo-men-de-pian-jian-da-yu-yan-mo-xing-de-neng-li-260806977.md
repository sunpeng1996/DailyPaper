---
title: Confirming Our Biases? Evaluating the Capabilities, Risks, and Societal Impact
  of Large Language Models
title_zh: 证实我们的偏见？大语言模型的能力、风险与社会影响评估
authors:
- Mudar Adas
- Polina Tsvilodub
- Michael Franke
- Martin V. Butz
affiliations:
- University of Tübingen, Neuro-Cognitive Modeling Group
- University of Tübingen, Department of Linguistics
arxiv_id: '2608.06977'
url: https://arxiv.org/abs/2608.06977
pdf_url: https://arxiv.org/pdf/2608.06977
published: '2026-08-07'
collected: '2026-08-10'
category: Eval
direction: 大语言模型风险与社会影响评估
tags:
- LLM Bias
- Prompt Framing
- Factual Consistency
- Model Manipulability
- Societal Impact
one_liner: 通过10个领域160条prompt测试6款LLM，揭示其即使在事实场景下也会依从prompt框架强化用户偏见
practical_value: '- 搭建LLM驱动的电商导购/咨询Agent时，新增prompt框架校验模块，拦截用户输入的引导性话术，避免Agent输出错误商品信息、强化用户不当认知

  - 做生成式推荐的prompt工程时，可反向利用prompt框架效应，通过正向引导话术强化用户对商品优势的感知，提升下单转化

  - 评估LLM在业务场景的可靠性时，需覆盖事实类、观点类多维度引导性prompt测试，提前规避模型可操纵性带来的合规风险'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有研究已证实LLM对prompt框架高度敏感，但尚未明确其强化用户prompt中隐含偏见的程度，以及隐式框架效应与显式prompt操纵的边界，直接影响LLM落地的可靠性与合规性。
### 方法关键点
选取6款LLM，覆盖观点类、事实类共10个主题，构造160条差异化prompt，系统控制prompt策略、支持/挑战指令、prompt极性、用户表达信念、主题域5个变量开展对照测试。
### 关键结果
LLM会系统性调整输出匹配prompt框架，该效应即使在事实场景下也成立，prompt框架对输出的影响权重可超过事实一致性，明确了LLM可操纵性的范围与边界。
