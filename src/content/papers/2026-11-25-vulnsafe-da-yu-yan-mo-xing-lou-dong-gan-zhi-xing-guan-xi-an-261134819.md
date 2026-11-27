---
title: 'VulnSafe: Measuring Vulnerability-Aware Relational Safety in Large Language
  Models'
title_zh: VulnSafe：大语言模型漏洞感知型关系安全能力度量
authors:
- Jiaming Luo
- Jiacheng Ji
- Haoan Jin
- Xiaoning Sun
- Qiuzhi Xiong
- Yuxin Zhang
- Hanhui Xu
- Mengyue Wu
affiliations:
- Shanghai Jiao Tong University
- Fudan University
- Ant Group
- Shanghai Mental Health Center
- Chang'an University
arxiv_id: '2611.34819'
url: https://arxiv.org/abs/2611.34819
pdf_url: https://arxiv.org/pdf/2611.34819
published: '2026-11-25'
collected: '2026-11-27'
category: Eval
direction: 大语言模型安全 · 多维度能力评估
tags:
- LLM Safety
- Benchmark
- Evaluation
- Relational Safety
- Vulnerability Detection
one_liner: 中文LLM漏洞感知响应能力评估基准VulnSafe，从5个维度度量关系安全性
practical_value: '- 搭建电商客服、内容推荐等用户-facing Agent的安全体系时，不能仅校验违禁内容，需新增风险感知、用户自主权保护、边界管理等隐性安全维度的检测规则，避免合规之外的体验或舆情风险

  - 评估业务场景下Agent的安全能力时，可参考VulnSafe的证据中心设计思路，构建分场景的测试prompt库和场景化评分规则，拆分「禁止做」和「应该做」两类要求，更精准定位能力短板

  - 开发面向情绪安抚、健康科普等敏感场景的LLM应用时，可复用VulnSafe的5维能力框架做对齐训练，降低隐性安全风险'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有LLM安全基准仅检测孤立的违规内容，无法衡量面向脆弱场景（如情绪支持、健康咨询）的关系安全能力，难以识别看似无问题但会损伤用户自主权、强化错误认知、造成隐性伤害的回复。

### 方法
中文评估基准VulnSafe围绕漏洞感知响应能力（VARC）拆解为5个互补维度：风险感知、安全留存、自主权保护、支持性回复、边界管理；基于证据中心设计覆盖41个场景、2050条平衡prompt，配套场景化评分规则，同时区分主动「应做」行为和「禁做」行为。

### 关键结果
8个主流LLM测试结果显示，不同模型的VARC能力分布差异显著，且该维度的能力差距远大于传统违禁内容拒答的能力差距，证明关系安全是独立于合规拒答的多维度能力。
