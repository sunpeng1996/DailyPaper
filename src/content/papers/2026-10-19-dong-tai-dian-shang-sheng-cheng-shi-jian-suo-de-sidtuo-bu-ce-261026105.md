---
title: 'Don''t Rewrite the SID Map: Topology Preservation for Generative Retrieval
  in Dynamic E-Commerce Search'
title_zh: 动态电商生成式检索的SID拓扑保持更新策略
authors:
- Jianbo Zhu
- Xing Fang
- Xiaopeng Chu
- Mingmin Jin
- Jing Wang
- Bokang Wang
- Jiaqi Ye
- Xiang Zhang
affiliations:
- Taobao & Tmall Group of Alibaba
- Nankai University
- University of Science and Technology of China
arxiv_id: '2610.26105'
url: https://arxiv.org/abs/2610.26105
pdf_url: https://arxiv.org/pdf/2610.26105
published: '2026-10-19'
collected: '2026-10-20'
category: GenRec
direction: 生成式推荐 · SID动态更新
tags:
- Generative Retrieval
- Semantic ID
- E-commerce Search
- Dynamic Update
- Generative Recommendation
one_liner: 基于大规模电商实验验证SID拓扑保持原则，提出增量更新策略实现GMV+1.16%
practical_value: '- SID更新直接复用旧item的SID，仅给新item分配新SID，完全避免语义漂移，无需做复杂的重映射对齐，落地成本低收益高

  - 生成式检索的离线评估必须覆盖小beam场景，大beam会掩盖真实的漂移损失，避免上线后低延迟窄beam配置下效果暴跌

  - 模型更新优先用前序checkpoint做warm-start，不要做新旧模型权重插值（模型soup），纯新微调checkpoint效果最优，短更新周期可尝试保留10%以内旧权重

  - SID设计可采用混合碰撞方案，头部高价值item分配唯一SID，尾部长尾item共用bucket SID，既能保证头部效果，又能控制SID空间大小'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
动态电商场景下新商品持续上架、业务信号不断变化，需要定期更新SID-商品映射，传统全量重映射会导致SID语义漂移，破坏模型已学习的解码路径，且大beam离线评估会掩盖漂移的真实影响，现有研究未系统量化映射变化与检索效果的关系。

### 方法关键点
- SID采用三层结构：前两层通过加入query-item对比损失的RQ-VAE生成语义前缀，第三层基于点击/加购/成交等业务价值排序分配，头部item配唯一SID、尾部item共享碰撞桶，兼顾语义和业务价值
- 映射更新策略：冻结旧商品的SID不变，新商品仅按语义前缀插入对应聚类的价值排序位置，不修改任何旧映射
- 训练策略：从历史checkpoint做warm-start，仅微调用户+query生成SID的阶段，无需全量重训

### 关键实验结果
基于天猫67天大规模搜索日志实验：全量重映射在beam=1时HitRate下降41.78%~62.05%，beam=1000时仅下降8.33%~10.85%；旧item重映射比例从0%升到72.75%时HitRate单调下降最高42.66%；拓扑保持+warm-start策略相对全量重映射，旧item HitRate提升约10%，新item HitRate提升约109%；线上3周A/B测试实现UCTCVR+0.29%，GMV+1.16%。

### 核心结论
永远不要修改模型已经学习过的SID，插入新item、冻结旧item、尽可能warm-start是生成式检索动态更新的最优原则。
