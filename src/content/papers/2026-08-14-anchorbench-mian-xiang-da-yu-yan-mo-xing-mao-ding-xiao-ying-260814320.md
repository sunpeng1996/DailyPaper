---
title: 'AnchorBench: A Multi-Pathway Benchmark for the Anchoring Effect in LLMs'
title_zh: AnchorBench：面向大语言模型锚定效应的多通路评估基准
authors:
- Yiderigun Borjigin
- Alexander Hermann
- Christian Cyron
- Roland Aydin
affiliations:
- Saarland University
- Hamburg University of Technology
- Helmholtz-Zentrum Hereon
- German Research Centre for Artificial Intelligence (DFKI)
arxiv_id: '2608.14320'
url: https://arxiv.org/abs/2608.14320
pdf_url: https://arxiv.org/pdf/2608.14320
published: '2026-08-14'
collected: '2026-08-17'
category: Eval
direction: 大语言模型认知偏差 · 鲁棒性评估
tags:
- LLM
- Anchoring Effect
- Benchmark
- Robustness
- Evaluation
one_liner: 构建区分锚点相关性、覆盖多通路的LLM锚定效应基准，完成14款模型的系统评估
practical_value: '- 做RAG增强电商导购、决策类Agent时，需校验检索返回的参考数值锚点，避免错误数值引导模型输出偏离事实的决策

  - 评估LLM在推荐文案生成、价格预测、用户需求判断类任务的鲁棒性时，可复用该基准的多通路锚点测试设计，补充现有评估维度

  - 面向定价、优惠发放等高敏感LLM应用，可引入锚点距离校验逻辑，锚点超出合理区间阈值时触发二次校验，降低业务损失'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有LLM锚定效应研究仅覆盖窄范围锚点注入通路，未区分锚点合理性，无法全面评估LLM在决策类场景下的锚定偏差风险，难以支撑高可靠LLM应用的选型与优化。
### 方法关键点
提出AnchorBench基准，覆盖多类常见锚点注入通路，设置锚点相关性、锚点与证据支持答案的距离两个核心控制变量，对14款模型（10款开源模型、4款前沿闭源API模型）开展大规模受控prompt测试。
### 关键结果
1. 锚定效应强度高度依赖注入通路；
2. 强通路下合理锚点比无关锚点带来的判断偏移幅度更大；
3. 锚点与合理答案距离越远，影响越弱，该规律在External、RAG场景下最明显；
4. 无锚点控制条件下准确率超过95%的前沿API模型，依然易受合理锚点影响出现判断偏差。
