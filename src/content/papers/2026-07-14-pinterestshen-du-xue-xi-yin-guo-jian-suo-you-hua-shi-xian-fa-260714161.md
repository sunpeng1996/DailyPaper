---
title: Deep-learning Causal Retrieval Optimization for Efficient e-commerce Distribution
  in Pinterest
title_zh: Pinterest深度学习因果检索优化实现高效电商内容分发
authors:
- Junpeng Hou
- XianXing Zhang
- Sai Xiao
- Derek Cheng
- Darren Reger
- Olafur Gudmundsson
- Mehdi Ben Ayed
- Zhiqing Rao
- Huizhong Duan
affiliations:
- Pinterest, Inc.
- LinkedIn
arxiv_id: '2607.14161'
url: https://arxiv.org/abs/2607.14161
pdf_url: https://arxiv.org/pdf/2607.14161
published: '2026-07-14'
collected: '2026-07-17'
category: RecSys
direction: 推荐系统 · 早期检索因果触发优化
tags:
- Causal Inference
- Recommender System
- Retrieval Optimization
- Multi-task Learning
- Doubly Robust
one_liner: 在级联推荐早期检索阶段用因果模型触发购物候选生成器，降本同时提升非购物场景用户engagement
practical_value: '- 多垂直召回场景可复用这套因果触发框架：切小流量随机分触发/不触发组，离线用线性时间replay选阈值，大幅降低线上实验成本，避免全量打扰用户

  - 多任务训练复用DCNv2+MMoE架构，叠加Doubly Robust伪标签作为辅助损失，同时用反向PR AUC/反向Precision@K监控误触发，平衡电商转化与整体用户留存等多目标

  - 触发模型和远程召回调用并行执行，无额外端到端延迟，适合高QPS生产场景；还可通过阈值灵活调整不同时期业务优先级，无需重新训练模型

  - 小流量场景无足够随机数据时，可先预训练多任务outcome头，再用小量随机数据微调DR损失，用倾向得分匹配构造准反事实对降低数据需求'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
Pinterest电商内容无差别全量触发，会挤压非购物场景用户的Pin保存、长点击等核心互动，同时大规模调用购物候选生成器带来极高的基础设施成本；静态规则无法平衡电商转化和用户整体体验，且早期检索策略迭代依赖大量线上实验，成本高、周期长，亟需可落地的因果驱动触发方案。
### 方法关键点
- 数据层：切分小流量Shopping Holdout组，50%概率随机触发/不触发购物候选生成器，收集反事实标签，避免倾向得分估计偏差
- 模型层：采用DCNv2做特征交叉+MMoE做多任务学习，同时预测多业务指标的treatment/control组outcome、倾向得分、uplift；总损失融合outcome损失、uplift正则约束、Doubly Robust伪标签MSE损失，对稀疏高优指标加权重提效
- 评估层：设计线性时间离线replay算法，基于Holdout数据模拟不同阈值下的业务表现，直接选定上线阈值，保障离线线上一致性
- 工程层：模型推理与远程召回调用并行执行，无额外端到端延迟，峰值支持10万+QPS
### 关键结果
在Pinterest Closeup场景，用14天随机数据训练、1天数据评估，对比单任务baseline：最优策略最多降低85%购物触发量的同时核心购物会话无显著下降，全站总会话提升0.26%，Pin保存量提升1.10%，单实例节省基础设施成本近50万美元。
**最值得记住的一句话**：早期检索触发决策不要只看相关度，要量化增量收益，因果建模+离线replay可极低实验成本实现业务与成本双赢。
