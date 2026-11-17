---
title: 'When the Bill Falls: Reusing the Old Index Defers,Never Avoids, Re-encoding
  in Complete Embedding-Model Migration'
title_zh: 嵌入模型全量迁移场景下：复用旧索引仅推迟而非避免重编码
authors:
- Nannan Zhao
- Jiameng Zhang
- Taoyu Zhong
- Hao Wang
- Bo Wang
affiliations:
- Northwestern Polytechnical University
arxiv_id: '2611.20702'
url: https://arxiv.org/abs/2611.20702
pdf_url: https://arxiv.org/pdf/2611.20702
published: '2026-11-16'
collected: '2026-11-17'
category: Other
direction: 向量检索 · 嵌入模型迁移优化
tags:
- Vector Search
- Embedding Model
- Index Migration
- Model Upgrade
- Cost Optimization
one_liner: 通过多数据集实验验证嵌入模型迁移时旧索引复用效果，给出3条预迁移决策规则
practical_value: '- 嵌入模型升级无需迷信adapter方案，仅同家族LLM嵌入器的bridge adapter略优于旧模型，收益可忽略，优先评估重编码+过渡方案的ROI

  - window重排序的成本可直接基于旧索引计算，结合业务流量的Zipf倾斜特征提前预估过渡阶段的资源消耗与质量损失

  - 全量迁移前先在服务索引上实测新老模型效果差、窗口重排质量损失，再决策是否采用旧索引复用策略，避免盲目复用带来的长期成本浪费'
score: 7
source: arxiv-cs.IR
depth: abstract
---

### 动机
向量检索系统升级嵌入模型时需全量重编码语料，现有方案试图通过adapter、窗口重排复用旧索引降低迁移成本，但真实收益缺乏系统性验证。
### 方法关键点
在passage、代码、NQ共27组模型配对场景下测试旧索引复用策略效果，覆盖5种adapter变体、不同深度窗口重排，结合Zipf流量倾斜做预注册回放验证。
### 关键结果数字
1. 旧索引复用完全无法避免重编码，仅能推迟重编码时间、改变过渡阶段服务质量
2. 仅同家族LLM嵌入器的bridge adapter略优于旧模型，提升幅度可忽略
3. 窗口重排成本预测误差低于4e-5，NQ数据集上11组配对中10组的策略选择完全符合预设计规则
