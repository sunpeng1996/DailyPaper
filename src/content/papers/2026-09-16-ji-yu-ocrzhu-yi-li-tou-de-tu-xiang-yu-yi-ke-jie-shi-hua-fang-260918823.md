---
title: Using OCR Heads to Verbalize Image Semantics
title_zh: 基于OCR注意力头的图像语义可解释化方法
authors:
- Sheridan Feucht
- Benno Krojer
- Sarah Wang
- Henry Abrahamsen
- Byron C. Wallace
- David Bau
affiliations:
- Northeastern University
- Independent
arxiv_id: '2609.18823'
url: https://arxiv.org/abs/2609.18823
pdf_url: https://arxiv.org/pdf/2609.18823
published: '2026-09-16'
collected: '2026-09-17'
category: Multimodal
direction: 多模态大模型 · 语义可解释性
tags:
- VLM
- Interpretability
- Attention Head
- OCR
- Semantic Alignment
one_liner: 识别VLM中通用OCR注意力头，构建语义透镜实现图像语义标注与概念编辑
practical_value: '- 电商多模态搜索/推荐场景可复用OCR头提取的通用语义特征，优化商品图文语义对齐，减少图文不匹配的召回错误

  - 商品营销素材生成场景可复用逆语义透镜变换，低成本实现商品属性替换（如款式、背景），降低素材制作成本

  - 多模态Agent的图像理解模块可提取早期层语义特征，减少推理层数，降低KV cache占用，提升端到端响应速度'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有VLM像素到语义的映射为黑盒机制，可解释性不足限制多模态场景的可控应用，研究以OCR能力为切入点破解VLM语义对齐逻辑。
### 方法关键点
1. 在4款VLM中定位到对OCR任务起因果作用的注意力头，验证其为通用语义头，可输出所有图像token的可解释语义特征；
2. 聚合这些头的注意力权重得到统一的语义透镜变换，可提取全隐层的可解释语义特征，结合词表投影可直接输出语义标签；
3. 逆语义透镜变换可实现图像概念的可控编辑。
### 关键结果
Qwen3-VL-8B等模型从第0层即可输出可解释语义标签，证明VLM早期层已完成图文语义对齐；逆变换可实现自然图像的概念替换（如拖拉机改左轮手枪），验证语义子空间的通用性。
