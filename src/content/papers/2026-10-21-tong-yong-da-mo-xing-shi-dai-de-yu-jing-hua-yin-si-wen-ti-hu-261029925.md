---
title: Privacy in Context Is Being Overlooked in the Age of General-Purpose LLMs
title_zh: 通用大模型时代的语境化隐私问题被严重忽视
authors:
- Prakhar Ganesh
- Yash More
- Marco Romanelli
- Ferdinando Fioretto
- Golnoosh Farnadi
affiliations:
- McGill University
- Mila - Quebec AI Institute
- Hofstra University
- University of Virginia
arxiv_id: '2610.29925'
url: https://arxiv.org/abs/2610.29925
pdf_url: https://arxiv.org/pdf/2610.29925
published: '2026-10-21'
collected: '2026-10-23'
category: LLM
direction: 大模型隐私 · 语境适配落地路径
tags:
- LLM Privacy
- Contextual Privacy
- Prompt Privacy
- Privacy Evaluation
- LLM Deployment
one_liner: 指出通用大模型统一隐私框架的认知误区，给出3条语境适配的隐私落地路径
practical_value: '- 业务侧LLM应用（如电商导购Agent、生成式推荐）不要盲目采用通用隐私方案，需针对消费数据、订单信息、浏览行为等场景敏感点定制隐私规则

  - 隐私效果评估不使用通用benchmark，针对当前业务场景做专项测试，如推荐系统用户敏感标签泄露、导购对话支付/地址信息泄露测试

  - 结合场景做用户隐私引导，如电商导购Agent界面明确提示哪些信息会被用于推荐优化，降低合规风险'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
当前通用LLM跨多场景部署成为趋势，业界普遍追求一刀切的统一隐私解决方案，完全忽略隐私天然的语境依赖属性，易催生虚假安全感知，带来实际隐私泄露风险。

### 方法关键点
论证统一prompt隐私框架的根本不合理性，明确不同隐私技术（差分隐私、匿名化、密码学方案）在性能、效率、防护能力、域适配性等核心维度存在固有矛盾，不存在通用最优解。

### 核心结论
提出三条落地路径：1）LLM按具体应用场景独立部署，避免跨场景混用；2）针对业务语境做隐私框架专项评估；3）强化用户场景化隐私素养教育
