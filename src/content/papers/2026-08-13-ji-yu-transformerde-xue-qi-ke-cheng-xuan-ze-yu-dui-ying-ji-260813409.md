---
title: Jointly Predicting Courses and Grades Using a Transformer-Based Model
title_zh: 基于Transformer的学期课程选择与对应成绩联合预测模型
authors:
- Paul Savala
affiliations:
- St. Edward’s University
arxiv_id: '2608.13409'
url: https://arxiv.org/abs/2608.13409
pdf_url: https://arxiv.org/pdf/2608.13409
published: '2026-08-13'
collected: '2026-08-16'
category: Other
direction: 教育学习分析 · 多任务序列预测
tags:
- Transformer
- Multi-task Learning
- Sequential Prediction
- Loss Function
- Learning Analytics
one_liner: 提出捕捉课程并发效应的TRACE模型，联合预测学期选课及成绩，MAE较单任务降近50%
practical_value: '- 可复用多任务联合训练思路：电商场景下可将用户下单预测与订单金额/复购周期预测联合建模，设计融合损失函数提升主任务效果

  - 序列建模可引入时间窗口分组编码：推荐系统处理用户行为序列时，可按周/大促周期等窗口分组捕捉同期交互物品的关联效应，优化行为表征

  - 低代价提效技巧：无需修改主模型架构，仅引入轻量辅助预测任务（如排序任务额外加加购/收藏预测分支）即可显著提升主任务性能'
score: 4
source: arxiv-cs.AI
depth: abstract
---

### 动机
现有学习分析领域的预测模型通常将学生学业历史视为简单线性序列，忽略同一学期内多门课程并行修读的并发特性，在学生课程负载高、难度大的场景下预测精度差，单任务成绩预测的性能瓶颈明显。
### 方法关键点
1. 提出TRACE Transformer架构，按学期粒度编码课程序列，捕捉同期修读课程的相互影响；
2. 设计联合损失函数，同时优化「未来学期选课集合预测」「对应课程成绩预测」两个任务，用辅助任务提升主任务表征质量；
3. 天然支持接入学生属性类侧特征，可拓展性强。
### 关键结果
基于10年院校历史数据训练，相比同架构仅做成绩预测的单任务模型，MAE降低近50%；效果优于传统LSTM、GNN等基线方法，可通过重训练/参数校准快速适配新院校。
