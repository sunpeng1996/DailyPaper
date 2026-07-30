---
title: 'Enhancing Generative Information Extraction with Two-step Validation: A Product
  Attribute Use Case'
title_zh: 两步验证增强生成式信息抽取：产品属性抽取应用实践
authors:
- Yi-Sheng Hsu
- Nermeen Abou Baker
- Uwe Handmann
affiliations:
- Ruhr West University of Applied Sciences
arxiv_id: '2607.26780'
url: https://arxiv.org/abs/2607.26780
pdf_url: https://arxiv.org/pdf/2607.26780
published: '2026-07-29'
collected: '2026-07-30'
category: LLM
direction: 生成式信息抽取 · 电商产品属性
tags:
- Information Extraction
- Product Attribute Extraction
- LLM
- PLM
- Two-step Validation
- Local Deployment
one_liner: 提出PLM预抽取+LLM校验的两步生成式IE框架，提升产品低显著度属性抽取效果，支持本地部署
practical_value: '- 电商商品属性抽取可采用分策略架构：尺寸/重量/货号等显式属性直接用LLM抽取，组件/材质/生产商等弱显著度属性用"小PLM预抽取+LLM校验修正"的两步流程，整体F1最高可提升7%

  - 若有本地部署/数据隐私需求，优先选用7B及以上开源LLM做校验模块，3B及以下小模型在长prompt校验场景下会出现性能下降，仅适合硬件极度受限场景

  - 实体抽取评估时可先对预测值和标签做去空格、去特殊字符、实体去重等预处理，再做实体级精确匹配，避免格式差异导致的误判

  - 低资源垂直领域信息抽取任务都可复用该"小模型预标+大模型校验"的混合架构，平衡效果、成本和数据隐私要求'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
欧洲数字产品护照（DPP）政策要求结构化披露产品全生命周期属性，但电商/工业场景下产品标注数据稀缺、数据隐私要求高，直接用PLM微调泛化性差，直接用LLM抽取对弱显著度实体（如材质、组件）召回率低，且大模型本地部署成本高。

### 方法关键点
- 重构生成式IE任务为两步验证流程：第一步用微调后的RoBERTa/DeBERTa等小PLM做预抽取输出结构化结果，第二步将PLM输出与原文一起输入LLM，让LLM校验修正预抽取结果而非从零抽取
- 对属性做分群适配：尺寸/重量/货号等显式属性直接用LLM抽取，组件/材质/生产商等弱表达属性走两步验证流程
- 全流程采用开源模型，支持本地部署，避免数据泄露风险

### 关键结果
- 实验基于亚马逊商品描述、电商文本分类两个公开标注数据集，覆盖6类产品属性，对比基线为LLM直接抽取方案
- 7B及以上开源LLM采用两步法后，整体F1最高提升7.6个百分点；Gemma-3 27B在亚马逊数据集上F1可达72.64%，Llama-3.3 70B可达72.94%
- 两步法对弱显著度实体提升最明显，可让8B规模LLM的弱属性抽取效果接近24B模型的直接抽取效果；3B及以下小模型因长prompt理解能力不足，性能会出现下降

**最值得记住的一句话：** 垂直领域低资源信息抽取任务中，"小模型预抽取+大模型校验"的混合架构可在不增加模型规模的前提下，大幅提升低显著度实体的抽取效果，同时满足本地部署的隐私要求
