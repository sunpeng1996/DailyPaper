---
title: 'From Alignment to Access Control: A Framework for GenAI Policy Enforcement'
title_zh: 从对齐到访问控制：生成式AI政策执行落地框架
authors:
- Nathalie Baracaldo
affiliations:
- IBM Research
arxiv_id: '2609.26682'
url: https://arxiv.org/abs/2609.26682
pdf_url: https://arxiv.org/pdf/2609.26682
published: '2026-09-22'
collected: '2026-09-23'
category: LLM
direction: LLM安全 · 政策合规执行体系建设
tags:
- GenAI Compliance
- Policy Enforcement
- LLM Security
- Access Control
- Alignment
one_liner: 系统化分析GenAI现有政策执行方案，提出统一落地方法论与行业改进建议
practical_value: '- 落地LLM驱动的推荐/Agent业务时，可复用本文的政策执行分析框架，统一对齐合规、模型对齐、访问控制三类约束，避免零散规则导致的合规风险

  - 梳理现有GenAI相关业务策略时，可参考本文的方法论拆解现有规则的覆盖盲区，比如电商Agent调用用户隐私数据、执行下单/退款操作的权限管控

  - 搭建LLM业务安全体系时，可借鉴本文的分类思路统一不同团队的政策定义口径，避免烟囱式规则带来的执行冲突与安全漏洞'
score: 6
source: arxiv-cs.AI
depth: abstract
---

### 动机
GenAI及衍生Agent业务落地速度远超安全合规机制建设速度，已发生多起生产事故（如AI编码Agent误删生产数据库）；不同从业者对「政策」的定义口径差异大，零散烟囱式的规则方案无法满足统一合规要求，存在大量安全盲区。
### 方法关键点
系统性梳理当前工业界、学术界GenAI政策执行方案的优劣，提出标准化的政策定义、执行路径拆解方法论，覆盖从预训练对齐、推理侧内容审核到资源访问控制的全链路政策约束场景。
### 关键结果
完成了现有GenAI政策执行方案的体系化分类，明确了不同方案的适用边界与盲区，输出了行业可落地的政策执行体系建设建议，是USENIX Security 2026 Enigma同名议题的延伸成果。
