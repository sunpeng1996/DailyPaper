---
title: 'The Maskability Index: Predicting Task-Objective Alignment in Pretrained Language
  Models'
title_zh: 可掩码性指数：预测预训练语言模型的任务-目标对齐度
authors:
- Ahmad Pouramini
- Mahsa Afsharzadeh
affiliations:
- Department of Computer Engineering, Sirjan University of Technology
arxiv_id: '2607.20265'
url: https://arxiv.org/abs/2607.20265
pdf_url: https://arxiv.org/pdf/2607.20265
published: '2026-07-22'
collected: '2026-07-23'
category: LLM
direction: LLM任务-预训练目标对齐度量
tags:
- Prompt Engineering
- Pre-trained Language Model
- Knowledge Extraction
- Low-resource Learning
- Metric
one_liner: 提出可掩码性指数MI，量化知识关系适配掩码/前缀提示的程度，辅助低资源场景prompt选择
practical_value: '- 电商搜索/推荐场景做prompt工程时，可参考MI思路选择适配PLM预训练目标的提示模板，降低小样本场景调优成本

  - 低资源业务场景（如新品类知识抽取、小众用户意图识别）可借鉴MI的度量逻辑，快速筛选适配的prompt范式，无需大量标注数据验证

  - 基于PLM搭建Agent工具链时，可引入类似对齐度度量预筛选prompt模板，提升知识抽取、意图理解等模块的稳定性'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
PLM（如BERT、T5）生成结构化知识的性能高度依赖prompt策略与预训练目标的匹配度，现有prompt调优缺乏可量化的对齐评估指标，小样本/低资源场景下试错成本极高。
### 方法关键点
提出Maskability Index (MI)定量度量指标，通过计算掩码模板与非掩码模板的DepthRank得分差值，直接判断特定知识关系更适配掩码式提示（适配BERT类掩码预训练目标）还是前缀式提示（适配自回归生成目标），为prompt与预训练目标的对齐度提供可解释的量化依据。
### 关键结果
在ATOMIC2020知识库补全基准的多类关系上验证，MI与下游生成性能显著正相关，可直接指导低资源场景下的prompt模板选择、模型适配策略制定，无需大量标注数据即可降低prompt调优成本
