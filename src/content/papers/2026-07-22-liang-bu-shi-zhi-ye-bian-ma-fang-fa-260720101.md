---
title: Two-Step Occupation Coding
title_zh: 两步式职业编码方法
authors:
- Alexander M. Esser
- Jens Dörpinghaus
affiliations:
- University of Koblenz
- Federal Institute for Vocational Education and Training (BIBB)
- Linnaeus University (LNU)
arxiv_id: '2607.20101'
url: https://arxiv.org/abs/2607.20101
pdf_url: https://arxiv.org/pdf/2607.20101
published: '2026-07-22'
collected: '2026-07-25'
category: Other
direction: 职业编码 · 两步式文本分类
tags:
- NER
- Text Classification
- Two-Stage Framework
- Confidence Calibration
one_liner: 将职业编码拆分为职位实体抽取和分类映射两步，结合边际置信度准则提升效果与可解释性
practical_value: '- 两步拆分复杂多目标任务的思路可直接复用在电商类目映射、SPU标准化场景：先抽核心实体再做分类映射，抗噪性、可解释性远高于端到端方案

  - 基于边际的置信度准则可替换推荐/搜索系统中常用的绝对阈值过滤逻辑，解决不同类别下得分分布不均导致的一刀切问题

  - 噪声文本下的领域NER优化方案可迁移到电商OCR商品标题识别、用户UGC评论实体抽取等业务场景'
score: 4
source: arxiv-cs.IR
depth: abstract
---

### 动机
现有职业编码采用端到端单步方案，同时完成职位实体识别与分类编码映射，在OCR错误等噪声场景下效果差，结果可解释性弱。
### 方法关键点
1 拆分任务为独立两步：第一步用领域专属NER模型从含噪自由文本中抽取职位名称实体，第二步单独将抽取结果映射到职业分类体系，分类器仅需聚焦映射任务
2 提出基于边际的置信度判断准则，替代传统绝对阈值，适配不同类别的得分分布差异
### 关键结果
相比单步端到端方案，准确率、鲁棒性、可解释性均显著提升；德语场景验证有效，可迁移到其他语言，完整源代码与评估脚本已开源。
