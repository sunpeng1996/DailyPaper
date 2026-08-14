---
title: When Can You Trust Offline Evaluation of Equal-Cost Top-k Allocation? A Controlled,
  Reproducible Benchmark and Practitioner's Guide
title_zh: 等成本Top-k分配的离线评估可靠性基准与从业者指南
authors:
- Binshuang Li
affiliations:
- Independent Researcher
arxiv_id: '2608.12489'
url: https://arxiv.org/abs/2608.12489
pdf_url: https://arxiv.org/pdf/2608.12489
published: '2026-08-12'
collected: '2026-08-14'
category: Eval
direction: Top-k定向策略离线评估基准
tags:
- Offline-Evaluation
- OPE
- IPS
- Doubly-Robust
- Top-k-Allocation
- Benchmark
one_liner: 针对等成本Top-k分配场景，基准测试6种离线评估器并给出可落地操作指导
practical_value: '- 做Top-k定向/广告投放策略的离线OPE时，优先选用doubly robust类estimator，对propensity估计误差的鲁棒性远高于IPS

  - 不要仅用cross-fitting处理结果nuisance来解决optimizer诅咒，必须做策略级诚实数据拆分，避免训练评估数据复用带来的bias

  - 评估不同日志环境的OPE可靠性可采用有效样本量排名，但单一日志下的候选策略排序不要依赖该指标，且其阈值不可跨场景迁移

  - 日志propensity兜底设为0.02可限制IPS权重爆炸，还能简化混合estimator选型，减少不必要的调参成本'
score: 7
source: arxiv-stat.ML
depth: abstract
---

### 动机
电商/广告等场景的确定性Top-k定向策略上线前依赖离线OPE验证效果，但现有OPE方法的可靠性边界不清晰，从业者缺乏可落地的选型指导。
### 方法关键点
基于5个公开数据集、2组已知效应扫描，对6种主流OPE estimator做受控基准测试，同时引入非模拟配对参考验证机制。
### 关键结果
1. 弱重叠由日志策略与目标策略的动作对齐度决定，仅调整日志策略sharpness几乎不影响重叠度，动作级不一致会直接导致重叠崩溃；
2. 仅对结果nuisance做cross-fitting无法解决optimizer诅咒，甚至会加重bias，策略级诚实拆分可彻底避免数据复用bias；
3. 倾向估计误差对IPS的伤害大于所有其他测试压力，对doubly robust estimator几乎无影响；propensity兜底设为0.02时，2种调优混合estimator会退化为基础版本，仅需保留4种核心estimator即可覆盖业务需求。
