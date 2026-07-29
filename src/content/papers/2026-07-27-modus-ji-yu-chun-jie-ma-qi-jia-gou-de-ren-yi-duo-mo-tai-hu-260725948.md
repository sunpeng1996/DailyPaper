---
title: 'MODUS: Decoder-Only Any-to-Any Modeling of Diverse Modalities'
title_zh: MODUS：基于纯解码器架构的任意多模态互建模框架
authors:
- Mingqiao Ye
- Zhaochong An
- Zhitong Gao
- Xian Liu
- François Fleuret
- Chuan Li
- Amir Zadeh
- Serge Belongie
- Afshin Dehghan
- Jesse Allardice
affiliations:
- EPFL
- Apple
- University of Copenhagen
- CUHK
- University of Geneva
arxiv_id: '2607.25948'
url: https://arxiv.org/abs/2607.25948
pdf_url: https://arxiv.org/pdf/2607.25948
published: '2026-07-27'
collected: '2026-07-29'
category: Multimodal
direction: 多模态大模型 · 纯解码器任意模态互转
tags:
- Multimodal-LLM
- Decoder-Only
- Any-to-Any-Modality
- Autoregressive
- Unified-Modeling
one_liner: 提出纯解码器架构的任意模态互建模框架MODUS，无需模态专属头即可支持多模态任意输入输出
practical_value: '- 电商多模态商品内容处理可复用无模态专属头的统一建模思路，替换现有文本/图像/视频分模块处理pipeline，降低多模态召回/排序链路复杂度

  - 电商导购Agent可借鉴链式模态生成+跨模态自校验机制：比如用户实拍商品图→生成描述文本→生成检索query→再生成相似图反向校验query准确性，提升多轮交互准确率

  - 多模态推荐系统可直接复用该框架的统一自回归模态编码逻辑，降低不同模态语义对齐的训练成本，适配商品搜推的多模态输入输出场景'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
现有任意多模态互转模型多基于编码器-解码器或扩散架构从零训练，无法复用成熟预训练纯解码器大模型的能力，性能受限；且需要模态专属头、定制损失和独立任务流水线，灵活性差，适配新模态成本高。

### 方法关键点
MODUS采用纯解码器架构，对所有模态做对称处理，将不同模态统一转换为自回归token序列输入单个Transformer解码器处理，无需模态专属头、定制损失或独立任务流水线，支持任意模态组合作为输入输出，天然支持链式跨模态生成、跨模态自校验等扩展能力。

### 关键结果
单模型在视觉任务（RGB转深度/法向量/边缘特征）、视觉语言任务（VQA、视觉定位）等多类基准上性能对标专用模型和多任务基线，开箱即用性能优异，全代码开源。
