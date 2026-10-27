---
title: How Much Fresh Data Should CTR Recalibration Use? A Temporal Evaluation of
  Post-hoc Calibration
title_zh: CTR 校准需要多少新鲜数据？事后校准的时序特性评估
authors:
- Rui Liu
affiliations:
- Independent Researcher
arxiv_id: '2610.33168'
url: https://arxiv.org/abs/2610.33168
pdf_url: https://arxiv.org/pdf/2610.33168
published: '2026-10-23'
collected: '2026-10-27'
category: RecSys
direction: 广告CTR模型 · 事后校准优化
tags:
- CTR-prediction
- model-calibration
- temporal-evaluation
- post-hoc-calibration
- offline-evaluation
one_liner: 通过时序对照实验明确CTR事后校准最优新鲜数据窗口，揭示随机评估对校准效果的高估问题
practical_value: '- 离线评估CTR模型校准效果必须使用时间分割而非随机分割，且要覆盖多个训练起点和随机种子，避免得到过于乐观的无效结果

  - 事后校准的新鲜数据窗口优先选择12小时而非更短的6小时，可将校准劣化的概率从1/3降到不到1/6，进一步拉长到24小时劣化概率反而回升

  - 12小时窗口的校准数据可稀疏采样到原规模的5%，仅损失12%的校准收益，拟合速度提升20-25倍，大幅降低计算开销

  - 基于拟合切片ECE的前置门控无法有效规避校准劣化风险，不建议上线使用，校准波动主要来自流量分布的时段错配'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
当前CTR模型离线评估默认采用随机分割，事后校准普遍默认使用最新几小时数据，二者都没有经过时序生产场景的严格验证；而CTR校准精度直接影响竞价、预算调控等下游链路的业务效果，校准误差的业务影响远高于排序指标的小幅波动。

### 方法关键点
- 采用Avazu 40.4M曝光公开数据集，训练LR、DeepFM、DCN-v2三类主流CTR模型，设置2个滚动时序训练起点+随机分割对照组，每个实验组跑3个随机种子消除随机性影响
- 校准方法选用行业通用的Platt缩放、保序回归，校准拟合窗口覆盖1/3/6/12/24小时多组对照，严格保证无时间泄露
- 评估指标除AUC、LogLoss外，核心采用ECE（期望校准误差）衡量校准效果，同时通过模拟二价拍卖量化校准对最终利润的影响

### 关键结果数字
- 随机分割会低估LR模型的ECE达38-45%，深度模型的低估幅度最高达45%，且校准误差不会随训练与测试的时间差单调增长
- 6小时拟合窗口的事后校准约1/3场景会升高ECE，12小时窗口劣化率降至1/10以内，24小时窗口劣化率回升至1/4；12小时窗口采样到5%规模即可保留88%的校准收益
- 校准带来的利润波动在-0.21%~+0.26%之间，即使是基于测试日数据的理想校准器，利润提升也仅为每千次曝光0.147元

### 核心结论
CTR事后校准的效果核心取决于拟合数据覆盖的时段分布，而非单纯的数据量，盲目使用最新短窗口数据做校准反而会劣化效果。
