---
title: 'VAD: Attributing Visual Evidence for Target Reconstruction in Multimodal On-Policy
  Distillation'
title_zh: VAD：多模态在线策略蒸馏中面向目标重建的视觉证据归因
authors:
- Kangning Zhang
- Yixing Li
- Shuai Shao
- Qingyao Li
- Zhengxi Lu
- Zhiyuan Yao
- Jianghao Lin
- Wenxiang Jiao
- Yuan Lu
- Weiwen Liu
affiliations:
- Shanghai Jiao Tong University
- Xiaohongshu Inc.
- The Chinese University of Hong Kong
- Zhejiang University
- Southeast University
arxiv_id: '2607.28590'
url: https://arxiv.org/abs/2607.28590
pdf_url: https://arxiv.org/pdf/2607.28590
published: '2026-07-30'
collected: '2026-07-31'
category: Training
direction: 多模态大模型 · 知识蒸馏训练
tags:
- Multimodal LLM
- Knowledge Distillation
- On-Policy Distillation
- Counterfactual Inference
- Visual Attribution
one_liner: 提出基于反事实目标重建的视觉归因蒸馏方法，解决多模态在线策略蒸馏的源混合监督问题
practical_value: '- 多模态生成式推荐/商品文案生成蒸馏时，可借鉴反事实擦除视觉证据的方法，过滤和商品视觉特征无关的语言先验干扰，提升生成内容与商品图匹配度

  - 带特权教师的蒸馏场景下，可复用「教师修正投影到视觉证据方向仅保留对齐分量做监督+教师信号做弱正则」的训练范式，避免过度拟合教师无关偏差

  - 多模态Agent视觉理解模块蒸馏训练时，可借鉴$u_t$指标量化视觉证据对候选token的支持/反驳程度，优化细粒度视觉知识迁移效率'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
多模态在线策略蒸馏（OPD）采用特权视角教师监督学生生成轨迹，但next-token修正存在源混合问题，同时包含视觉信号、语言先验和教师专属偏差，无法区分哪些修正来自真实视觉证据。
### 方法关键点
1. 提出视觉归因蒸馏（VAD），采用反事实目标重建思路，对同一固定教师分别输入带/不带目标视觉证据的样本，计算中心化对数概率差得到视觉证据方向代理$u_t$，量化视觉证据对候选token的支持/反驳程度。
2. 将原始教师修正投影到$u_t$，仅保留干预对齐分量重构学生锚定的训练目标，主监督用重构目标，特权教师信号仅做弱正则。
### 关键结果
在4B、9B参数规模的6个细粒度视觉基准上，VAD效果超过直接特权视角蒸馏和视觉优势加权方法；token级分析显示对齐分量富含任务相关视觉修正，尤其在证据反驳错误答案时效果提升更显著。
