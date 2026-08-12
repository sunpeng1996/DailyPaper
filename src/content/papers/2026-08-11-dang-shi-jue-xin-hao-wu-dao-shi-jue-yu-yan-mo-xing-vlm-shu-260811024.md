---
title: 'When Visual Signals Mislead: A Mechanistic Study of Attribute Hallucination
  in Vision-Language Models'
title_zh: 当视觉信号误导：视觉语言模型（VLM）属性幻觉的机制研究
authors:
- Yufei Zhang
- Chenlu Zhan
- Hongwei Wang
affiliations:
- Zhejiang University
arxiv_id: '2608.11024'
url: https://arxiv.org/abs/2608.11024
pdf_url: https://arxiv.org/pdf/2608.11024
published: '2026-08-11'
collected: '2026-08-12'
category: Multimodal
direction: 多模态大模型 · VLM属性幻觉修复
tags:
- VLM
- Hallucination
- Attribute Correction
- VISOR
- Multimodal Model
one_liner: VISOR框架可拆解VLM属性幻觉成因，分故障模式路由修复，无需依赖语言先验主导假设
practical_value: '- 电商多模态商品理解场景可复用VISOR的信号拆解方法，区分视觉信号/语言先验对属性预测的贡献，减少商品属性标注错误

  - 不同属性的故障模式差异可直接复用：颜色/状态类属性用校准调优即可，材质类错误需针对性做视觉适配，降低改造成本

  - 无需修改VLM主干的轻量化修复思路（校准/弃权/定向适配路由）可直接落地，避免全量微调的高成本'
score: 7
source: arxiv-cs.CV
depth: abstract
---

### 动机
VLM属性幻觉（正确识别物体但错判属性）问题普遍，过往归因于语言先验主导，该假设未在属性层面验证，对应抑制先验的方法效果受限。
### 方法关键点
1. VISOR统一框架先通过VSNR诊断模块将预测拆解为视觉logit信号、语言先验信号两类；
2. 基于诊断结果划分两类故障模式：颜色/状态属性对应低边际但方向正确的视觉信号，材质属性对应低SNR或对齐错误的视觉信号；
3. 路由到对应修复算子：阈值误差用校准、低SNR免训练直接弃权、材质错误用定向视觉适配，全程不依赖先验主导假设。
### 关键结果
在Qwen、InternVL、LLaVA三类主流VLM的10791个负真值样本上，VISOR可有效降低属性预测假阳性，语言先验信号对假阳性的预测能力接近随机水平。
