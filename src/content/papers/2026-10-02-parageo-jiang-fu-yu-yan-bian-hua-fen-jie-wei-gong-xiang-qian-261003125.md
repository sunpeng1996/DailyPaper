---
title: 'ParaGeo: Decomposing Paralinguistic Variation into a Shared Latent Geometry'
title_zh: ParaGeo：将副语言变化分解为共享潜在几何结构
authors:
- Yuhan Liu
- Yuxuan Ou
- Ruoxi Su
- Mohamed Ahmed Zaki
- Yunbo Long
affiliations:
- University of Cambridge, Department of Engineering
- University of Oxford, Department of Engineering Science
- University of Washington Bothell, Department of Computing & Software Systems
arxiv_id: '2610.03125'
url: https://arxiv.org/abs/2610.03125
pdf_url: https://arxiv.org/pdf/2610.03125
published: '2026-10-02'
collected: '2026-10-05'
category: LLM
direction: 语音大模型 · 副语言表征潜在几何分解
tags:
- Speech LLM
- Paralinguistic Representation
- KV Cache
- Latent Geometry
- Speech Control
one_liner: 提出ParaGeo框架，在冻结语音大模型中分解副语言变化，构建跨内容的共享副语言表征坐标系
practical_value: '- 可借鉴KV表征投影方法，优化语音类Agent的副语言风格（如语气、语速）控制，适配电商售后安抚、新品介绍等差异化场景

  - 跨内容的共享副语言坐标系统可复用，降低多场景语音风格适配的标注成本，无需为每类话术单独训练风格控制模块

  - 冻结大模型下的特征解耦思路可迁移到文本大模型风格控制场景，实现商品文案、营销话术的语气统一校准'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
语音大模型中副语言（语气、语速、语调等）变化同时受语义内容和属性控制，缺乏跨内容的统一表征体系，难以实现稳定的语音风格控制。
### 方法关键点
1. 基于冻结语音大模型GLM-4-Voice构建ParaGeo框架，采用匹配内容的分解策略：合成音频token用固定监听prompt回放，池化后的KV表征经中心化后投影到共享低维空间
2. 设计两类验证探针：覆盖12个基准族80种控制属性的跨句子探针，以及10场景6风格的一致性探针
### 关键结果数字
内容留出的质心准确率达9.49%，远高于1.25%的排列基准；同标签跨内容余弦相似度0.285，对比基准0.017，两组检验p值均为0.001；10场景探针验证风格对比方向可跨场景复现
