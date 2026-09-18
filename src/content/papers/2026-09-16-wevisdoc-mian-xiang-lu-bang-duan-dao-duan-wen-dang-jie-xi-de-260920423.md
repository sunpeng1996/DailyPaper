---
title: 'WeVisDoc: From Coverage to Capability for Robust End-to-End Document Parsing'
title_zh: WeVisDoc：面向鲁棒端到端文档解析的从覆盖到能力提升框架
authors:
- Hao Yu
- Kang Liu
- Linnan Zhao
- Jiabo Zhan
- Chong Sun
- Chen Li
- Jing Lyu
affiliations:
- WeChat Vision, Tencent Inc.
arxiv_id: '2609.20423'
url: https://arxiv.org/abs/2609.20423
pdf_url: https://arxiv.org/pdf/2609.20423
published: '2026-09-16'
collected: '2026-09-18'
category: Multimodal
direction: 多模态文档解析 · 数据驱动鲁棒性优化
tags:
- Document Parsing
- Data-centric
- Multimodal
- OCR
- Robustness
one_liner: 提出两阶段以数据为中心的鲁棒端到端文档解析框架，在四类公开基准上全部排名第一
practical_value: '- 针对训练数据分布偏置问题，可复用两阶段数据优化思路：第一阶段扩覆盖，第二阶段聚类定位残差错误定向补数据，适合提升OCR、商品图文解析等场景鲁棒性

  - 结构保留的退化合成方法可直接迁移到商品小票、资质文件、用户上传图文等低质量输入的解析模型训练，降低真实脏数据采集成本

  - 固定视觉-结构簇的残差诊断方法，可复用在推荐系统多场景效果优化中，定向补充分布外场景训练样本，避免盲目扩数据'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有文档解析训练数据集中在常见文档类型与干净数字页面，单纯扩展数据覆盖度无法针对性解决模型剩余弱点，在多样布局、低质量采集场景下性能鲁棒性不足。

### 方法关键点
提出两阶段以数据为中心的WeVisDoc框架：Stage I通过异构数据融合、结构保留的退化合成，拓宽训练数据在语义、结构、外观三方面的覆盖度；Stage II用留存探测集度量Stage I模型在固定视觉-结构簇内的残差错误，基于诊断结果定向构造数据、重分配目标token预算，针对性补全模型能力短板。

### 关键结果数字
WeVisDoc-4B在OmniDocBench v1.6上整体得分95.38，在PureDocBench三个赛道平均得分75.54，四类测试场景下均为SOTA；Stage II相较于Stage I，2B、4B模型在两个基准上得分均提升，在退化场景增益更显著，4B模型在真实退化赛道提升4.03个百分点。
