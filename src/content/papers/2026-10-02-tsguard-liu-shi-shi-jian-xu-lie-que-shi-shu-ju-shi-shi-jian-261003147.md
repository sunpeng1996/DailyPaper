---
title: 'TSGuard: A Real-Time Framework for Detecting and Imputing Missing Data in
  Streaming Time Series'
title_zh: TSGuard：流式时间序列缺失数据实时检测与补全框架
authors:
- Imane Hocine
- Asma Abboura
- Soror Sahri
- Abhijith Senthilkumar
- Yacine Hakimi
- Grégoire Danoy
affiliations:
- University of Luxembourg
- Hassiba Benbouali University of Chlef
- Université Paris Cité
- École Supérieure d’Informatique
arxiv_id: '2610.03147'
url: https://arxiv.org/abs/2610.03147
pdf_url: https://arxiv.org/pdf/2610.03147
published: '2026-10-02'
collected: '2026-10-05'
category: Other
direction: 流式时序处理 · 实时缺失值补全
tags:
- Time-series Imputation
- Streaming Data
- Data Quality
- Spatiotemporal GNN
- Real-time System
one_liner: 提出结合轻量时空补全、领域约束校验的流式时序缺失值实时处理框架
practical_value: '- 推荐系统实时用户行为时序特征丢数场景，可复用「轻量图感知时序补全+业务约束校验」逻辑，替换传统均值/前值填充方案，提升特征可靠性

  - 实时特征pipeline可直接套用「检测-补全-校验-留用/替换」闭环架构，避免补出不符合常识的特征值（如异常客单价、负点击量）

  - 需人工运营的特征异常排查场景，可借鉴其可解释输出+人在回路设计，降低运营排查成本'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
流式时序数据（传感器、用户行为流等）普遍存在观测延迟、缺失问题，现有补全方法要么需要离线访问未来数据，要么仅追求吞吐不保障结果符合领域约束，无法适配实时业务需求。
### 方法关键点
1. 设计全链路数据质量闭环：先检测异常/缺失观测，再用轻量graph-aware时序模型补全，之后基于物理/空间领域约束校验结果，不符合约束的触发fallback estimation，符合约束的则判断保留原异常值或替换
2. 配套可交互解释能力，支持用户实时查看数据状态、对比不同补全模型效果、自定义约束、校验标记值
### 关键结果
作为演示系统在环境传感场景验证了端到端实时处理能力，补全结果的领域合理性远高于无约束通用时序补全方案，人在回路交互可大幅降低运营排查工作量
