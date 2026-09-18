---
title: 'DocAttriBench: Benchmarking Answer Grounding in Document Visual Question Answering'
title_zh: DocAttriBench：面向文档视觉问答的答案溯源基准
authors:
- Luca De Grandis
- Silvia Cappelletti
- William Raccagni
- Marcella Cornia
- Lorenzo Baraldi
- Rita Cucchiara
affiliations:
- University of Modena and Reggio Emilia
- University of Pisa
arxiv_id: '2609.20574'
url: https://arxiv.org/abs/2609.20574
pdf_url: https://arxiv.org/pdf/2609.20574
published: '2026-09-17'
collected: '2026-09-18'
category: Eval
direction: 多模态大模型 · 答案溯源评测
tags:
- Multimodal-LLM
- Document-VQA
- Answer-Grounding
- Benchmark
- Automatic-Annotation
one_liner: MAPPET自动标注方法实现低成本溯源标注，构建含29.6万问答对的文档VQA溯源基准DAB
practical_value: '- 做电商文档类RAG（商品详情页问答、订单票据问答）时，可复用MAPPET方法自动标注答案对应的证据片段，大幅降低人工标注成本

  - 做多模态RAG系统可解释性评测时，可参考DAB的评测框架，同时评估答案准确率和证据溯源准确率

  - 对Agent的文档工具调用结果校验场景，可借鉴基于mask的perplexity变化方法，自动定位答案依赖的关键信息块'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有文档VQA领域的答案溯源基准普遍缺乏标注或标签质量不佳，人工标注溯源数据集成本极高，无法支撑可信赖、可验证多模态大模型的研发需求。
### 方法关键点
1. MAPPET自动标注方法结合文档布局信息与LLM能力，通过mask候选元素后计算perplexity增幅，定位对答案置信度贡献最大的布局元素（文本块、表格、图片等）
2. 基于MAPPET批量处理多个现有公开文档VQA数据集，构建DAB基准，包含23.7万份文档、29.6万带元素级溯源标注的问答对
3. 配套多维度评测框架，可同时评估模型的答案准确率、溯源准确率、整体答案质量
### 关键结果
测试显示大模型答案准确率随参数量提升，但即使是当前最优模型的证据定位能力仍存在明显缺陷，答案正确时溯源准确率普遍偏低。
