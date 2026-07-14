---
title: 'Letting the Data Speak: Extracting Keywords from Crowdsourced Collections
  with AI'
title_zh: AI驱动的众包馆藏关键词自动化提取方法对比评估
authors:
- Miguel Arana-Catania
- Catherine Conisbee
- Matthew Kidd
affiliations:
- University of Oxford, UK
arxiv_id: '2607.09324'
url: https://arxiv.org/abs/2607.09324
pdf_url: https://arxiv.org/pdf/2607.09324
published: '2026-07-10'
collected: '2026-07-14'
category: NLP
direction: NLP关键词提取 · 众包UGC内容处理
tags:
- Keyword Extraction
- NER
- Topic Modelling
- Crowdsourced Data
- NLP
one_liner: 对比三类NLP关键词提取方案效果，给出众包场景下负责任的模型选型建议
practical_value: '- 电商UGC内容（用户评价、晒单、社群内容）的关键词标注场景，优先选型开源抽取式模型而非生成式大模型，降低内容合规、版权相关的问责风险

  - 做关键词自动化标注技术选型时，需同时测试NER、传统统计抽取、大模型生成三类方案，结合业务场景选最优，不要单押单一技术路径

  - UGC类内容的关键词提取pipeline需加入轻量人工审核环节，平衡自动化效率和内容管理责任，避免错误标签影响搜索/推荐效果'
score: 4
source: arxiv-cs.IR
depth: abstract
---

### 动机
众包数字馆藏的规模化关键词标注存在技术、实操、伦理三重挑战，人工标注成本高、效率低，亟需可落地的自动化方案，同时需平衡标注效果与内容管理责任。
### 方法关键点
以牛津大学二战众包数字馆藏为测试案例，覆盖三类NLP关键词提取范式：命名实体识别（NER）、抽取式关键词提取、主题建模，技术栈横跨传统统计方法到现代生成式大模型，同时开展量化+定性双维度评估。
### 关键结果
NLP方法均具备规模化关键词提取的落地潜力，但无单一方法可覆盖全场景需求，模型选型对最终结果影响极大；开源抽取式模型是负责任部署的最优选择，生成式AI虽具备抽象生成优势，但存在较高的问责风险，UGC场景需谨慎选用。
