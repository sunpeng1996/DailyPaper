---
title: 'Perception, Layout, and Validation: Calibrated Confidence for Reliable Straight-Through
  Processing of Financial Documents'
title_zh: 感知、布局与校验：面向金融单据可靠直通处理的置信度校准方法
authors:
- Yichao Jin
- Yushuo Wang
- Yuxuan Han
- Kwan Ching Yee Sonia
- Weiyang Song
- Chiu Jin-Chun Kent
- Wong Chong Hwee
- Wong Tiong Kiat
- Kenneth Zhu Ke
- Jingyuan Zhao
arxiv_id: '2609.20110'
url: https://arxiv.org/abs/2609.20110
pdf_url: https://arxiv.org/pdf/2609.20110
published: '2026-09-17'
collected: '2026-09-18'
category: Multimodal
direction: 多模态文档抽取 · 置信度校准
tags:
- VLM
- Confidence Calibration
- Conformal Risk Control
- Document Information Extraction
- Straight-Through Processing
one_liner: 拆解三类可解释置信度通道结合共形风险控制，大幅提升金融单据VLM信息抽取的直通处理可用性
practical_value: '- 可将多维度可解释置信度拆解方法迁移到电商小票、订单、广告投放素材等多模态信息抽取场景，替代大模型原生置信度，提升抽取结果自动通过率

  - 共形风险控制思路可直接复用在广告合规校验、商品资质审核等需严格控错的工业大模型落地场景，在可控错误率下最大化自动处理占比

  - 置信度通道拆分方法论可迁移到LLM/RAG回答正确性预判场景，降低大模型落地的人工复核成本'
score: 6
source: arxiv-cs.AI
depth: abstract
---

### 动机
金融单据直通处理（STP）要求自动审批字段的残差误差有明确边界，现有VLM原生输出的置信度信号可靠性差，无法匹配高可用STP的落地要求。

### 方法关键点
拆解出感知、布局、校验三类可解释置信度通道，输出融合打分后叠加共形风险控制模块，实现可控误差下的字段自动审批。

### 关键结果
在3个公开数据集（真实发票、合成发票、广告采购表单）、2类VLM（Qwen3.6-27B、Gemini-3.1-Flash-Lite）上验证：
1. 抽取结果正误分类的AUROC从原生VLM的0.54-0.74提升至0.90-0.99
2. 目标误差<10%的风险控制要求下，原生VLM仅能自动审批0.1%-7.0%的字段，新方法可自动审批49%-72%的字段，且实际误差不超过目标值，满足工业部署要求
