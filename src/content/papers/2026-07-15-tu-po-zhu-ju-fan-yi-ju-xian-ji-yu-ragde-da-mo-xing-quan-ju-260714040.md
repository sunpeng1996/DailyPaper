---
title: Can an Old Dog Be Taught New Tricks? Taking LLMs Beyond Sentence Level Translation
title_zh: 突破逐句翻译局限：基于RAG的大模型全局文档翻译方案
authors:
- Alaina Brandt
arxiv_id: '2607.14040'
url: https://arxiv.org/abs/2607.14040
pdf_url: https://arxiv.org/pdf/2607.14040
published: '2026-07-15'
collected: '2026-07-16'
category: LLM
direction: 大模型长文档跨语言翻译优化
tags:
- RAG
- LLM
- Document Translation
- MQM
- Corpus Informed
one_liner: 提出RAG驱动的PAT翻译系统，实现融合多粒度上下文的整文档语料感知翻译
practical_value: '- 跨境电商多语种商品详情页、海外站营销文案生成可复用多粒度上下文RAG架构，融合段落、篇章级参考样例提升译文风格与目标市场适配性

  - 定制化生成任务可参考「用户可配置规则+领域语料召回」双路输入范式，降低Prompt调优成本同时对齐业务合规、风格要求

  - 生成效果评估可借鉴自定义MQM指标体系思路，针对特定业务场景（如小语种广告文案）设计贴合业务目标的多维度评估标准'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有自动翻译系统普遍采用逐句翻译范式，忽略篇章层级的语用规范、修辞风格与话语组织差异，生成的译文难以适配目标语言本土语境，仅能实现字面意思对齐，无法满足专业翻译要求。
### 方法关键点
提出RAG驱动的PAT（Pragmatic Auto-Translator）系统，支持用户自定义翻译规范，同时从美式英语-拉美西班牙语对照长文本语料库中召回段落、章节、文档级的多粒度参考上下文，输入LLM完成整文档翻译生成，输出供专业人员校验的翻译草稿。
### 关键结果
针对生成式AI主题的6篇译文，由2名专业译员基于自定义MQM指标评估显示：普通Prompt生成的译文无有效风格适配，融合配置规范+语料上下文的方案可实现显著的篇章级重构，但当前重构有效性仍待进一步优化。
