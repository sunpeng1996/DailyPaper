---
title: 'IndicTriMix: Developing Language Identification Datasets and Models for Tri-Language
  Code-Mixing'
title_zh: IndicTriMix：面向三语码混的语言识别数据集与模型开发
authors:
- Pruthwik Mishra
- Rudra Trivedi
- Avi Patel
- Ashok Urlana
- Shrikant Malviya
affiliations:
- Sardar Vallabhbhai National Institute of Technology, Surat, India
- TCS Research, Hyderabad, India
arxiv_id: '2609.11851'
url: https://arxiv.org/abs/2609.11851
pdf_url: https://arxiv.org/pdf/2609.11851
published: '2026-09-10'
collected: '2026-09-13'
category: LLM
direction: 多语言处理 · 码混语言识别
tags:
- Code-Mixing
- Language Identification
- XLM-RoBERTa
- MuRIL
- Sequence Labeling
one_liner: 发布印度三语码混标注基准，微调XLM-RoBERTa等实现token级语言识别
practical_value: '- 面向南亚/东南亚多语言电商/内容平台的用户query理解场景，可直接复用其token级码混识别的序列标注范式，提升多语言搜索、推荐的语义匹配准确率

  - 小语种码混标注数据稀缺时，可借鉴其基于平行句的码混语料生成方法，低成本扩充训练集降低标注成本

  - 多语言NLP任务选型时，可优先测试MuRIL/XLM-RoBERTa作为基座，已验证在区域语言码混场景下效果优于传统单语言LID模型'
score: 4
source: arxiv-cs.CL
depth: abstract
---

### 动机
多语言UGC场景中用户频繁混用多种语言，传统针对单语文本设计的句子级语言识别（LID）模型无法适配token级细粒度识别需求，印度区域三语（印地语、古吉拉特语、孟加拉语+英语）码混场景缺少公开基准数据集。
### 方法关键点
1. 将token级码混语言识别建模为序列标注任务，微调适配印度语言的MuRIL、XLM-RoBERTa基座模型
2. 提出两种基于三语平行句的码混语料生成方法，构建包含人工标注测试集的公开基准
3. 在三种语言配置下分别验证模型的token级标签预测效果
### 关键结果
验证了上下文嵌入对多语言社交媒体文本token级码混识别的有效性，所有微调模型、数据集、源代码全量开源可直接复用。
