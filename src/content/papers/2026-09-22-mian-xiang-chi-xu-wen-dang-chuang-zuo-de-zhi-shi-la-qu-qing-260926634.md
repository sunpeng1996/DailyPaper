---
title: Knowledge Pull Requests for Continual Document Authoring
title_zh: 面向持续文档创作的知识拉取请求（KPR）框架
authors:
- Alexander Martin
- Benjamin Van Durme
affiliations:
- Johns Hopkins University
arxiv_id: '2609.26634'
url: https://arxiv.org/abs/2609.26634
pdf_url: https://arxiv.org/pdf/2609.26634
published: '2026-09-22'
collected: '2026-09-24'
category: LLM
direction: LLM 可解释持续文档更新
tags:
- KPR
- Continual Document Authoring
- Interpretability
- Cross-lingual
- Knowledge Update
one_liner: 提出可解释的KPR框架，实现带知识变更溯源的跨源跨语言持续文档更新
practical_value: '- 电商商品详情页、品类规则文档的持续更新可复用KPR的claim提取-冲突校验-变更溯源流程，避免全量重生成导致的信息丢失，减少人工审核成本

  - 多语言站点的内容同步可参考跨语言claim匹配机制，比直接全量翻译再重写的信息密度更高、token消耗更少

  - Agent动态维护用户画像、领域知识库时，可借鉴KPR的ChangeLog设计，分离知识变更逻辑和文本修改逻辑，大幅提升调试效率'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有持续文档更新方案仅记录文本diff无法溯源知识变更，要么无感知修改内容要么全量重生成，跨语言多源知识整合效率低、易丢失原有有效信息。
### 方法关键点
KPR框架核心流程：①从新源中抽取结构化claim；②过滤匹配后路由到对应文档段落，自动标记与现有内容的冲突点；③输出分离知识变更（claim提案）和文本改动（diff）的可审核ChangeLog，全链路变更可解释。
### 关键结果
跨语言维基百科更新任务中，KPR比全量重写方案多整合30%+有效信息，单位生成token携带信息量提升25%；基于KPR更新的文档支撑QA效果优于带搜索的SOTA模型，可覆盖仅其他语言存在的冷门知识。
