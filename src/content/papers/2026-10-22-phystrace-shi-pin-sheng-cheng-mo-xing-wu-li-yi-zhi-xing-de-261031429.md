---
title: 'PhysTrace: Interpretable Temporal Evaluation of Physical Consistency in Video
  Generative Models'
title_zh: PhysTrace：视频生成模型物理一致性的可解释时序评估
authors:
- Taekoan Yoo
- Wonkyung Jung
- Kyunghun Kim
- Kyeongbo Kong
affiliations:
- Independent Researcher, Korea
- Pusan National University, Korea
arxiv_id: '2610.31429'
url: https://arxiv.org/abs/2610.31429
pdf_url: https://arxiv.org/pdf/2610.31429
published: '2026-10-22'
collected: '2026-10-24'
category: Eval
direction: 视频生成 · 可解释物理一致性评估
tags:
- Video Generation
- Evaluation
- Interpretability
- MLLM
- Temporal Localization
one_liner: 推出免训练的视频物理一致性时序评估框架PhysTrace及带违例区间的测试集IntPhys2-Timing
practical_value: '- 电商生成短视频、商品动态展示等生成内容的合理性检测，可复用「历史上下文对齐+MLLM生成预期+时序匹配定位问题」的免训练框架，无需额外训练分类器，冷启动成本低

  - 多模态生成内容效果评估可借鉴逐时间步细粒度定位问题+输出可解释描述的思路，替代粗粒度整体打分，更易定位生成模型的缺陷点

  - 构建自定义生成效果评测基准时，可参考IntPhys2-Timing的构建思路，给现有基准增加问题区间标注，提升评测细粒度'
score: 6
source: arxiv-cs.AI
depth: abstract
---

### 动机
世界动作模型高度依赖预训练视频模型捕捉物理动力学，但现有物理一致性评估方法仅支持整体合理性打分或表征探测，无法定位时序维度的物理违例区间，也不能输出可解释的冲突原因。
### 方法关键点
1. 免训练框架PhysTrace基于MLLM生成依赖历史上下文的物理预期，再将预期与观测视频窗口做对齐，实现物理违例的时序定位与可解释描述，无需任务特定探针或分类器
2. 新增IntPhys2-Timing数据集，在原有IntPhys2基准上补充物理违例区间标注
### 关键结果
在IntPhys2-Timing上跨物理原则的Hit Rate最高达70.7%，在IntPhys2的可能/不可能视频分类任务上准确率优于所有对比方法；应用于扩散/流基视频生成模型的轨迹重建视频分析时，可定位到与属性、噪声相关的物理违例模式，支持跨时间步的可解释物理一致性分析。
