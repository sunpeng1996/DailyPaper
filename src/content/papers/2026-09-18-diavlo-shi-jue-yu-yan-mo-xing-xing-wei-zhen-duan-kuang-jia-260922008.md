---
title: 'DiaVLo: Diagnosing Behaviours of Vision-Language Models'
title_zh: DiaVLo：视觉语言模型行为诊断框架
authors:
- Lorenzo Corti
- Jie Yang
affiliations:
- Delft University of Technology
arxiv_id: '2609.22008'
url: https://arxiv.org/abs/2609.22008
pdf_url: https://arxiv.org/pdf/2609.22008
published: '2026-09-18'
collected: '2026-09-21'
category: Multimodal
direction: 多模态模型 · 行为对齐诊断
tags:
- VLM
- Alignment Diagnosis
- Causal Inference
- Model Evaluation
- Multimodal
one_liner: 提出结合人工标注与因果分析的VLM行为诊断框架DiaVLo，可识别对齐偏差与核心影响概念
practical_value: '- 多模态商品搜索/理解场景可复用DiaVLo的行为对齐检测逻辑，快速定位VLM商品识别、文案生成的错漏行为

  - 可借鉴其因果概念归因方法，定位影响多模态推荐效果的核心特征，大幅降低badcase排查成本

  - 多模态Agent感知模块校验可复用「预期行为-观测行为对齐校验」框架，保障Agent推理链路可靠性'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
当前VLM在多模态任务落地中存在视觉感知盲区、行为不可预测等问题，缺乏系统化的行为诊断与对齐校验方法，严重影响部署可靠性。
### 方法关键点
1. 提出DiaVLo诊断框架，结合人工标注与VLM生成能力，分别构建预期行为、观测行为的规范描述，通过二者比对快速识别对齐偏差；
2. 引入因果估计模块，可定位影响VLM决策逻辑的核心概念。
### 关键结果
在多个开源VLM的分类、生成任务上验证，DiaVLo生成的行为标签与模型性能强相关，可明确识别对齐/错位行为，同时能挖掘VLM感知、概念排序的内在规律。
