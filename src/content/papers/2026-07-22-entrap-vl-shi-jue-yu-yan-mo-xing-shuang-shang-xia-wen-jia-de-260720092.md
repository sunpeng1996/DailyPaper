---
title: 'ENTRAP-VL: A Taxonomic Probe for Dual Contextual Entrainment in Vision-Language
  Models'
title_zh: ENTRAP-VL：视觉语言模型双上下文夹带效应的分类探测工具
authors:
- Karan Goyal
- Afreen Hossain
- Debojyoti Das
- Vishal Bhutani
affiliations:
- IIIT Delhi, India
- Dr. Ambedkar Institute of Technology, India
- Heritage Institute of Technology, India
- PwC, India
arxiv_id: '2607.20092'
url: https://arxiv.org/abs/2607.20092
pdf_url: https://arxiv.org/pdf/2607.20092
published: '2026-07-22'
collected: '2026-07-23'
category: Eval
direction: 多模态大模型可靠性评估
tags:
- VLM
- Contextual Entrainment
- Probing Dataset
- Trustworthy AI
- Multimodal Evaluation
one_liner: 推出面向VLM的双上下文夹带效应分类探测工具ENTRAP-VL及配套评估协议
practical_value: '- 多模态搜索/商品理解场景下，可复用该探测方法检测VLM受无关图文上下文干扰的程度，降低商品推荐/搜索结果错配风险

  - 多模态Agent处理商品图文query时，可参考双上下文分类体系优化prompt结构，规避无关图文上下文对输出结果的误导

  - VLM上线前的可靠性校验环节，可直接接入ENTRAP-VL数据集做抗干扰测试，减少幻觉导致的业务损失'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
单模态LLM的上下文夹带效应（输出被无关/错误/无意义辅助上下文带偏）已有明确机制研究，但VLM中该效应的表现尚未被系统探索，且缺失适配多模态特性的专用探测工具，直接迁移文本基准无法覆盖双上下文干扰、场景真实性差异等多模态特有问题。

### 方法关键点
构建双轴分类体系，从「上下文与目标项的关联度」「上下文真实性」两个维度划分测试场景，拆分文本夹带（8种上下文条件）、视觉夹带（3种上下文条件）两个独立测试流，手动标注覆盖8个类别的样本。

### 关键结果
产出包含1500条标注样本的ENTRAP-VL公开数据集，配套完整分类框架与评估协议，支持社区对VLM双上下文夹带效应开展严谨研究。
