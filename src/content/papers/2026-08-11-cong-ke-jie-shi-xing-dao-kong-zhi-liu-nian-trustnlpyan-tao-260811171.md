---
title: 'From Interpretability to Control: Insights from Six Years of the TrustNLP
  Workshop'
title_zh: 《从可解释性到控制：六年TrustNLP研讨会研究趋势洞见》
authors:
- Rahul Gupta
- Abhinav Mohanty
- Anaelia Ovalle
- Anil Ramakrishna
- Anubrata Das
- Apurv Verma
- Jwala Dhamala
- Ninareh Mehrabi
- Tharindu Kumarage
- Yada Pruksachatkun
affiliations:
- Amazon AGI
- Meta
- Autodesk
- New Jersey Institute of Technology
- Salesforce
arxiv_id: '2608.11171'
url: https://arxiv.org/abs/2608.11171
pdf_url: https://arxiv.org/pdf/2608.11171
published: '2026-08-11'
collected: '2026-08-12'
category: LLM
direction: 可信大语言模型 研究趋势梳理
tags:
- Trustworthy NLP
- LLM Alignment
- Interpretability
- Safety Control
- Fairness
one_liner: 梳理6届TrustNLP共144篇论文，总结可信NLP从后验解释到生成系统主动可控的演进趋势
practical_value: '- 落地LLM驱动的推荐/Agent系统时，可优先对齐truthfulness维度，匹配当前行业优先级，降低幻觉导致的业务负向收益

  - 搭建生成式推荐/Agent的可信评估体系时，可直接复用TrustLLM、DecodingTrust的六大维度框架，减少自研成本

  - 迭代模型可解释性方案时，可同步布局mechanistic interpretability方向，避免技术选型落后于行业趋势'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
LLM在搜索推荐、Agent等业务场景加速落地，可信性已成为核心落地瓶颈，亟需明确可信NLP领域的演进路径与优先级方向

### 方法
汇总6届TrustNLP研讨会共144篇录用论文，基于TrustLLM、DecodingTrust成熟框架划分为六大可信维度做分类统计，同时对比同期ACL/NAACL/EACL/EMNLP的2000余篇同领域论文，交叉验证趋势普适性

### 关键结果
- 可信NLP领域整体从静态模型后验可解释性研究，转向生成系统机制理解与主动控制
- truthfulness是增长最快的维度，2021-2022年无相关研究，2025-2026年占比达37%
- fairness是最稳定的研究主题，explainability呈U型发展，随机制可解释性兴起于2026年反弹
- TrustNLP主题分布与行业整体趋势高度一致，参考性强
