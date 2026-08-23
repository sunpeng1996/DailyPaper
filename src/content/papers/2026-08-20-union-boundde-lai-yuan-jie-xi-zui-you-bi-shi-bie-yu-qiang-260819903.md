---
title: Where Does the Union Bound Go? Best-Arm Identification and Strong FWER Control
title_zh: Union Bound的来源解析：最优臂识别与强FWER控制
authors:
- Rianne de Heide
affiliations:
- Department of Applied Mathematics, University of Twente
- Centrum Wiskunde & Informatica, Amsterdam
arxiv_id: '2608.19903'
url: https://arxiv.org/abs/2608.19903
pdf_url: https://arxiv.org/pdf/2608.19903
published: '2026-08-20'
collected: '2026-08-23'
category: Other
direction: 最优臂识别 · 多重检验误差控制
tags:
- Best-Arm Identification
- FWER
- Union Bound
- Multiple Testing
- Fixed-Confidence BAI
one_liner: 明确固定置信度最优臂识别中K-1倍Bonferroni因子的来源，建立其与强FWER控制的等价性
practical_value: '- 落地多臂老虎机选品/广告最优策略遴选时，可复用本文误差校准逻辑，避免删除K-1校正因子导致置信度不达标

  - 固定置信度BAI算法上线时，可参考两种假设定向视角优化误差分配，在保证强FWER控制前提下降低所需样本量

  - 做多候选召回/排序策略的在线最优筛选时，可借鉴等价性结论设计错误率控制方案，压缩试错成本'
score: 4
source: arxiv-stat.ML
depth: abstract
---

### 动机
固定置信度最优臂识别（BAI）的证明中普遍使用跨臂union bound，带来K-1倍Bonferroni校正因子，但由于最优臂唯一，仅1个「臂i为最优」的假设为真，该校正的合理性长期存在争议。

### 方法关键点
从多重检验视角存在两种假设定向逻辑：① 将BAI视为包含K-1个真实零假设的强族错误率（FWER）控制问题；② 设定仅1个零假设为真，但K-1次两两比较中任意一次假阳性都会导致最终识别错误。

### 关键结果
两种定向下K-1重多重性误差的来源完全等价，解释了union bound在BAI中的必要性，统一了BAI与多重检验领域的术语体系。
