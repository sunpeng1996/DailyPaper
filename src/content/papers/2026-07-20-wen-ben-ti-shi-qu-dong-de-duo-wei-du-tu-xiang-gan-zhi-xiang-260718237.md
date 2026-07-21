---
title: 'The Many Senses of Visual Similarity: A Text-Prompted Image Perceptual Metric'
title_zh: 文本提示驱动的多维度图像感知相似度度量
authors:
- Sheng-Yu Wang
- Yotam Nitzan
- Aaron Hertzmann
- Jun-Yan Zhu
- Eli Shechtman
- Alexei A. Efros
- Richard Zhang
affiliations:
- Carnegie Mellon University
- Adobe Research
- UC Berkeley
arxiv_id: '2607.18237'
url: https://arxiv.org/abs/2607.18237
pdf_url: https://arxiv.org/pdf/2607.18237
published: '2026-07-20'
collected: '2026-07-21'
category: Multimodal
direction: 多模态 · 文本可控视觉相似度度量
tags:
- VLM
- Perceptual Similarity
- Image Retrieval
- Metric Learning
- Text-guided Search
one_liner: 构建多语义维度标注的图像相似度数据集，微调VLM得到文本可控的感知相似度度量TPIPS
practical_value: '- 电商相似款召回场景可接入TPIPS，实现按自定义维度（版型/颜色/面料等）的精细化召回，满足用户多粒度选品需求

  - 生成式商品图评估环节可复用TPIPS做细粒度校验，验证生成结果与参考样例在指定维度的相似度，降低bad case率

  - 多模态语义搜索场景可借鉴其微调思路，用少量业务场景下的三元组标注适配自有VLM，提升多条件检索准确率'
score: 7
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有图像感知相似度度量仅输出单一标量结果，无法匹配人类上下文依赖的多维度（颜色、形状、风格、语义等）相似度判断需求，主流前沿VLM在该任务上与人类标注共识存在显著差距。
### 方法关键点
1. 构建大规模图像三元组标注数据集，每个三元组覆盖多自由形式语义维度的人工相似度标注
2. 基于标注数据微调VLM得到TPIPS度量，支持通过输入文本提示指定相似度判断的具体维度
### 关键结果
TPIPS与人类感知的对齐度显著优于现有基线方法，跨分布泛化性稳定；可直接支撑文本引导检索、组合搜索、生成模型细粒度评估三类下游任务
