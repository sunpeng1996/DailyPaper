---
title: 'Tables Decoded: DELTA for Structure, TARQA for Understanding'
title_zh: 表格解析：面向结构识别的DELTA与面向理解的TARQA
authors:
- Jahanvi Rajput
- Dhruv Kudale
- Saikiran Kasturi
- Utkarsh Verma
- Ganesh Ramakrishnan
affiliations:
- Indian Institute of Technology Bombay
- BharatGen
arxiv_id: '2609.17458'
url: https://arxiv.org/abs/2609.17458
pdf_url: https://arxiv.org/pdf/2609.17458
published: '2026-09-15'
collected: '2026-09-17'
category: LLM
direction: LLM 表格结构识别与问答优化
tags:
- Table Understanding
- TabVQA
- LLM Fine-tuning
- Table Structure Recognition
- Multilingual NLP
one_liner: 提出基于结构化文本表示的表格解析框架DELTA与微调LLM TARQA，显著提升多场景表格问答精度
practical_value: '- 电商场景可复用DELTA的三模块拆分思路，解析商品参数表、运营报表、订单明细表等非结构化扫描表格，省去VLM部署与推理成本

  - 可借鉴OTSL紧凑结构化格式，将表格类数据转换为LLM友好的输入形式，提升RAG系统中表格内容的召回准确率与问答效果

  - 跨语言电商业务可参考其多语言表格处理思路，无需训练语种专属视觉编码器，大幅降低小语种表格解析的适配成本'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有表格理解方案大多依赖VLM处理表格图像，需适配语言的专属视觉编码器，多语言适配成本高、处理效率低，不适用于大规模跨语言表格解析场景。
### 方法关键点
1. 提出DELTA框架，拆分物理结构识别、逻辑结构识别、OCR三个独立模块，精准提取表格布局与内容，输出紧凑统一的OTSL格式，编码单元格排列与文本信息；
2. 基于OTSL序列微调LLM得到TARQA，直接处理结构化文本完成表格问答，无需接入视觉编码器。
### 关键结果
- TSR任务中DELTA在FinTabNet、PubTabNet、PubTables-1M数据集上TEDS-Structure分数与SOTA持平；
- TabQA任务上TARQA在WTQ数据集相对SOTA提升9.3p.p.，FinTabNetQA数据集提升9.2p.p.；
- 自建印地语表格基准TORQUE上，方案性能位列所有VLM、DELTA+LLM变体第2名。
