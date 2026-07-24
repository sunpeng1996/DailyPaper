---
title: 'Beyond Sycophancy: Structured Resistance and Compliance in LLM Moral Reasoning'
title_zh: 《超越谄媚问题：LLM道德推理中的结构化抗拒与服从机制》
authors:
- Baihui Wang
- Bernard Koch
affiliations:
- University of Chicago
- Yale School of Management
arxiv_id: '2607.21558'
url: https://arxiv.org/abs/2607.21558
pdf_url: https://arxiv.org/pdf/2607.21558
published: '2026-07-23'
collected: '2026-07-24'
category: Reasoning
direction: LLM道德推理 · 对齐优化
tags:
- LLM Alignment
- Moral Reasoning
- Sycophancy
- Belief Updating
- Social Influence
one_liner: 从社会心理学三维度解析LLM判断更新逻辑，区分建设性信念修正与谄媚服从，支撑高风险场景LLM对齐
practical_value: '- 设计导购/客服Agent时，可引入观点距离、来源可信度维度做判断过滤，避免无底线迎合用户错误诉求，降低合规风险

  - 开展Agent对齐训练时，可参考三维判断更新框架区分合理合规的响应调整与谄媚行为，提升对齐效率

  - 商品评价/内容审核场景中，可基于该框架设计模型判断稳定性校验逻辑，减少人为prompt诱导导致的审核偏差'
score: 7
source: arxiv-cs.AI
depth: abstract
---

### 动机
现有LLM谄媚问题治理多将其视为一维故障模式，无法区分合理信念修正与无底线服从，难以支撑高道德风险场景的可靠对齐。
### 方法关键点
引入人类社会心理学经典研究框架，从三个维度系统解析LLM判断的抗拒-服从机制：输入观点与模型初始立场的距离、观点的来源归因、支持观点的群体结构。
### 关键结果
实验证实LLM对接近自身初始立场的观点接受度更高，对标注为自身先前判断的观点响应提升最显著，对不同群体压力的响应存在明显异质性；该框架将谄媚重新归类为通用判断更新流程的特定表现，为高风险场景LLM对齐提供了可解释的理论基础。
