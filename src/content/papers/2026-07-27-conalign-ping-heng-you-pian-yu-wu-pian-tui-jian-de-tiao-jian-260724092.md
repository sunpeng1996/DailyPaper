---
title: 'ConAlign: Conditional Alignment Framework for Balancing Biased and Unbiased
  Recommendation'
title_zh: ConAlign：平衡有偏与无偏推荐的条件对齐框架
authors:
- Jingcheng Zhang
- Yihan Wang
- Qi Song
- Liyin Hong
affiliations:
- Kuaishou Technology
arxiv_id: '2607.24092'
url: https://arxiv.org/abs/2607.24092
pdf_url: https://arxiv.org/pdf/2607.24092
published: '2026-07-27'
collected: '2026-07-28'
category: RecSys
direction: 推荐系统去偏 · 双塔式知识对齐
tags:
- Recommendation Debias
- Dual-tower
- Knowledge Distillation
- Conditional Alignment
- Industrial Deployment
one_liner: 双塔式条件对齐的工业级去偏推荐框架，兼顾有偏场景性能与无偏去偏效果，支持流式部署
practical_value: '- 工程上可复用低侵入无偏流量采集方案：以小概率随机插入全库采样item到推荐流，不影响短期体验的同时持续积累无偏标注数据

  - 架构上可基于现有双塔排序模型低改造升级：新增轻量无偏塔复用有偏塔隐层特征，仅增加极微推理开销即可上线

  - 训练trick可直接复用：基于单样本有偏/无偏塔预测loss的离散门控选择对齐策略，避免负迁移，平衡去偏效果与当前业务指标

  - 调优经验：对齐权重λ可动态调整长短期收益，λ越高有偏环境性能越好、去偏效果越弱，可根据业务阶段灵活配置'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有推荐系统基于有偏观测数据训练会产生过滤气泡，压缩用户兴趣广度、损害长期留存；仅用无偏数据训练的去偏方法往往会降低现有有偏环境下的推荐精度，且普遍存在计算开销大、无法适配工业流式训练的问题，落地难度高。

### 方法关键点
- 双塔式架构：有偏塔在全量有偏交互数据上训练，无偏塔复用有偏塔最后一层隐层特征+通用属性特征作为输入，仅在小流量无偏交互数据上训练，推理直接输出无偏塔结果
- 条件对齐机制：仅当有偏塔在单样本上的预测loss低于无偏塔时，激活两塔隐层特征的对齐损失（用`stop-gradient`切断梯度回传至有偏塔），选择性迁移有偏塔的有效知识，避免负迁移
- 流式训练支持：并行消费有偏/无偏双数据流构造训练batch，无需笛卡尔乘积计算或多阶段蒸馏，训练开销极低

### 关键实验
离线在Coat、Yahoo! R3、KuaiRand-Pure三个公开数据集上对比AutoDebias、InterD等SOTA去偏方法，无偏场景下UAUC最高比SOTA高0.8pct，有偏场景下性能与SOTA持平，训练速度比InterD快86倍；快手线上A/B测试10%流量，LT7提升0.029%，用户有效兴趣数VIN提升0.097%，类别集中度下降0.083%，排序CPU开销无显著变化，短期观看等指标无负向。

**最值得记住的一句话**：小流量长期无偏数据结合选择性知识对齐，是平衡推荐系统短期业务指标与长期生态健康的可落地方案。
