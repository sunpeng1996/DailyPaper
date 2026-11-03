---
title: Multi-Turn Semantic Caching for Low-Cost LLM Serving
title_zh: 面向低成本LLM服务的多轮语义缓存方案
authors:
- Baran Atalar
- Selly Beyene
- Xutong Liu
- Carlee Joe-Wong
affiliations:
- Carnegie Mellon University
- University of Washington Tacoma
arxiv_id: '2611.01077'
url: https://arxiv.org/abs/2611.01077
pdf_url: https://arxiv.org/pdf/2611.01077
published: '2026-10-31'
collected: '2026-11-03'
category: LLM
direction: LLM服务优化 · 多轮语义缓存
tags:
- Semantic Caching
- LLM Serving
- Multi-turn Conversation
- Online Learning
- Cost Optimization
one_liner: 提出带理论保障的离线/在线多轮语义缓存算法，较基线多省13-16%生成成本，降延迟19-35%
practical_value: '- 电商客服、导购类多轮Agent的语义缓存可复用「实体key硬过滤+上下文加权embedding软匹配」的状态表示，相同实体约束下才做相似匹配，避免跨场景的错误复用

  - 可复用「复用风险+生成成本」的权衡策略，用LLM judge打标训练轻量KRR模型预估复用风险，优先缓存高生成成本、低复用风险的对话状态，比单纯相似度阈值缓存收益高1倍以上

  - 在线场景可借鉴CLCB-LS-MT的低切换设计，会话内冻结缓存策略、仅在会话边界更新，既避免会话内决策相关性问题，又降低缓存更新的工程开销'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有单轮语义缓存无法适配多轮对话场景：相同query在不同上下文下需要不同回复，单纯靠embedding相似度判断缓存复用的AUC仅0.62-0.74，错用率极高，多轮对话下的LLM服务成本、延迟优化空间一直未被充分挖掘。

### 方法关键点
- 状态表示分层：用离散实体key做硬过滤（跨key直接不可复用），再用「0.7权重query embedding + 0.3权重历史embedding」做软匹配，降低历史压缩后的匹配误差
- 引入复用风险：用KRR训练pair级复用风险模型，将缓存决策转化为「生成成本 < 复用风险惩罚」的权衡问题，避免低质量复用
- 两套可落地算法：离线CUCB-SC-MT基于历史日志训练缓存策略，有次优性保障；在线CLCB-LS-MT支持边服务边学习，会话内冻结策略降低相关性干扰，regret为Õ(√N)
- 缓存选择用Reverse Greedy算法，适配非对称、非度量的复用损失，有近似解保障

### 关键实验
在电影订票Taskmaster-3、数学辅导SocraTeach两个多轮数据集上，对比ContextCache、ElastiCache-MT、vCache等7个基线，1000条缓存条目下，CLCB-LS-MT可安全避免35%-41%的生成成本，基线最高仅22%-25%，同时降低服务延迟19%-35%。

最值得记住：多轮语义缓存的核心不是匹配相似度，而是权衡复用的风险成本和重新生成的计算成本，优先在结构化、流程化的多轮场景（客服、订票、辅导）落地收益最高。
