---
title: 'Think Harder Where It Matters: Item-Level Adaptive Recursion for Sequential
  Recommendation'
title_zh: 面向序列推荐的物品级自适应递归计算框架LoopRec
authors:
- Zhanshuo Cao
- Jiakai Tang
- Yuqi Zhou
- Sunhao Dai
- Jun Xu
affiliations:
- Renmin University of China
arxiv_id: '2610.30128'
url: https://arxiv.org/abs/2610.30128
pdf_url: https://arxiv.org/pdf/2610.30128
published: '2026-10-20'
collected: '2026-10-22'
category: RecSys
direction: 序列推荐 · 自适应计算优化
tags:
- Sequential Recommendation
- Adaptive Depth
- Looped Transformer
- Early Exit
- Computation Efficiency
one_liner: 提出物品级自适应递归序列推荐框架LoopRec，适配多骨干、效果更优且降低计算冗余
practical_value: '- 可直接复用自适应递归+轻量门控的设计，对现有序列推荐骨干（SASRec/BSARec/LRURec等）做改造，无需重构全量架构即可获得效果+计算效率双重收益

  - 深度分配先验规则可直接落地：给交互序列中最近的物品、低频长尾物品分配更多计算资源，符合用户行为和业务场景普遍规律

  - 训练trick可复用：路由模块先做N轮全深度warm-up，搭配负载均衡正则和z-loss防止门控过早饱和，解决自适应路由训练不稳定问题

  - 稀疏业务场景优先尝试：在交互稀疏、长尾商品多的电商类目/新用户冷启动场景下，该方案效果提升幅度远高于稠密场景'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有序列推荐对用户所有历史交互物品分配固定计算预算，忽略不同物品的预测贡献差异。诊断实验显示76.14%的物品经过1层处理后表征已收敛，仅6.72%的物品需要全3层处理；固定深度分配仅在4.6%的序列上是最优的，灵活分配可带来最高8.8%的HR提升，说明固定计算既浪费资源又限制效果。
### 方法关键点
- 采用权重共享的递归骨干，不同深度退出的物品表征天然落在同一特征空间，解决跨深度表征对齐问题
- 每层递归边界加轻量二元门控，根据物品当前表征和递归索引独立判断是否提前退出，无需额外深度标注
- 训练时加入负载均衡正则防止深度坍缩，加z-loss防止门控过早饱和，同时设置路由warm-up阶段，先全深度训练N轮再开启自适应路由
### 关键实验
在Amazon的Software、Office、Patio三个公开数据集上，针对SASRec、BSARec、NextItNet、LRURec四大主流序列推荐骨干做适配，48组对比中44组取得统计显著提升，相对提升幅度0.69%~49.07%；交互最稀疏的Patio数据集上平均NDCG@20提升11.14%，计算量仅为固定深度方案的0.407~0.755倍。
### 核心结论
序列推荐的计算资源应该向近期交互、低频长尾物品倾斜，而不是对所有历史物品平均分配
