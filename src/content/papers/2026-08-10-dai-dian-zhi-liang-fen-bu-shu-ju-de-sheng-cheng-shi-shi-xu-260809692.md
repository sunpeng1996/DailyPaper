---
title: Evaluating Generative Time-Series Models on Data with Point Masses
title_zh: 带点质量分布数据的生成式时序模型评估
authors:
- Jian Xu
arxiv_id: '2608.09692'
url: https://arxiv.org/abs/2608.09692
pdf_url: https://arxiv.org/pdf/2608.09692
published: '2026-08-10'
collected: '2026-08-11'
category: Eval
direction: 生成式时序模型 · 评估方法优化
tags:
- Time-Series
- Generative Model
- Evaluation
- CRPS
- Benchmark
- Zero-Inflated Data
one_liner: 指出含大量零值的时序数据现有评估偏差，给出校准方案与7类模型基准测试结论
practical_value: '- 评估零膨胀时序（如商品销量、用户点击、骑手订单请求）生成模型时，需先校验评估窗口零值占比与原数据集分布一致性，避免结论失真

  - 做零占比高的时序预测（如库存规划、冷门商品销量预估）时，优先测试自回归hurdle模型，效果远优于conditional flow模型

  - 多指标对比模型时需注意不同发生统计量的排序一致性，避免单指标带来的选型偏差'
score: 6
source: arxiv-cs.LG
depth: abstract
---

**动机**：当前生成式时序模型的常用基准数据集普遍存在单点概率质量（即大量零值，对应无订单、无点击、无请求等业务场景），现有评估协议存在严重分布错配问题，易得出完全错误的模型性能结论。
**方法关键点**：1. 量化标准滚动原点评估协议的分布错配缺陷；2. 提出构造CRPS不变、时序耦合破坏的对照组，可精准量化时序耦合对统计量的贡献；3. 对齐评估协议、固定5个随机种子，对7类主流生成式时序模型完成基准测试。
**关键结果**：① 2个公开基准中原数据集零占比分别为42%、47%，对应评估窗口零占比仅13%、5%，该错配可直接反转模型性能排序；② 自回归hurdle模型在6个数据集中的5个上优于conditional flow，最高领先153倍；③ conditional flow的发生统计量在不同训练种子下波动高达62%，5种发生统计量的模型排序无一致性
