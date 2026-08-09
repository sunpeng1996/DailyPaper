---
title: 'Clinical Communication Processing with Models Trained on LLM-Generated Synthetic
  Data: A Structured Survey and Novel Application Case Studies'
title_zh: 基于LLM合成数据训练的临床通信处理：结构化综述与新应用案例
authors:
- Alexander Apartsin
- Yehudit Aperstein
affiliations:
- Holon Institute of Technology (HIT), Israel
- Afeka Academic College of Engineering, Israel
arxiv_id: '2608.05993'
url: https://arxiv.org/abs/2608.05993
pdf_url: https://arxiv.org/pdf/2608.05993
published: '2026-08-06'
collected: '2026-08-09'
category: LLM
direction: LLM合成数据生成 · 低资源场景NLP落地
tags:
- Synthetic Data
- LLM
- Low-resource Learning
- Data Augmentation
- Domain Adaptation
one_liner: 系统梳理LLM生成合成临床通信数据的研究体系，附13个无标注场景落地案例
practical_value: '- 低资源业务场景（如小语种电商客服、冷启动类目意图识别）可参考将结构化业务数据（商品属性、工单标签）通过LLM转合成对话/文本，解决标注不足问题

  - 下游小模型微调时可引入带噪声的合成数据提升鲁棒性，比如模拟用户错别字、表述不完整的query，提升搜索意图识别准确率

  - 小样本场景下，基于合成数据微调的encoder模型效果优于zero-shot大模型，低算力业务可优先选择该技术路线'
score: 4
source: arxiv-cs.CL
depth: abstract
---

### 动机
临床通信类非结构化数据隐私性强、标注成本极高，高质量标注语料极度稀缺，制约临床NLP系统落地。
### 方法关键点
按数据来源、通信形式、生成方法、下游任务四个维度构建结构化综述，梳理LLM生成合成临床通信数据的完整技术体系；落地13个无真实标注数据的临床NLP场景，覆盖急救预到报告、现场无线电伤亡记录、护士交接班、患者门户分诊、低资源语言出院通知等。
### 关键结果数字
基于合成数据微调的encoder模型效果显著优于zero-shot基线，引入故意加噪的合成数据可进一步提升模型鲁棒性；当前核心局限是70%以上的验证基于合成测试集，合成训练-真实测试的跨域验证证据仍不足。
