---
title: 'Translation as a Computationally Efficient Bridge: Feasibility of English
  BERT for Low-Resource Languages'
title_zh: 《翻译作为高效桥梁：英文BERT适配低资源语言的可行性研究》
authors:
- Hielke Muizelaar
- Giulia Rivetti
- Marco Spruit
- Marcel Haas
arxiv_id: '2607.12612'
url: https://arxiv.org/abs/2607.12612
pdf_url: https://arxiv.org/pdf/2607.12612
published: '2026-07-14'
collected: '2026-07-15'
category: LLM
direction: 低资源NLP · 跨语言模型微调
tags:
- BERT
- Cross-lingual NLP
- Low-resource NLP
- Fine-tuning
- Translation
one_liner: 跨6类NLP任务5种语言对比验证翻译后微调英文BERT在低资源场景的可行性
practical_value: '- 跨境电商小语种业务场景优先试用该方案：可将小语种用户评论、query翻译为英文后微调成熟英文BERT，无需从零训练小语种预训练模型，大幅降低算力与标注成本

  - 任务选型适配：意图识别、语义匹配、用户咨询问答这类句法类任务可优先落地，实体抽取、涉敏检测等token级或文化强相关任务需额外做效果验证再上线

  - 语言适配参考：荷兰语、意大利语等与英语亲缘性近的小语种可直接复用该方案，中文、俄语等差异大的语言需补充少量本地化标注做效果校准'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
低资源语言原生BERT训练面临标注数据稀缺、算力成本高的痛点，翻译后微调英文BERT的低成本方案此前缺乏系统性跨任务跨语言效果验证。
### 方法关键点
选取6类NLP任务（情感分析、仇恨言论检测、问答、NER、词性标注、自然语言推理），覆盖保加利亚语、中文、荷兰语、意大利语、俄语5种语言，对比翻译微调英文BERT与原生语言BERT的表现。
### 关键结果
- 53.3%的实验场景下翻译微调方案效果持平或优于原生方案
- 句法/结构类任务（问答、词性标注、自然语言推理）增益最多，token级/文化强相关任务（NER、仇恨言论检测）易出现效果下降
- 与英语语系接近的语言（如荷兰语）效果最优，中文等差异较大的语言适配性较差
