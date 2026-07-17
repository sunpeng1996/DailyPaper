---
title: Long-History User Transformers for Real-Time Ad Ranking
title_zh: 面向实时广告排序的长历史用户Transformer架构
authors:
- Viacheslav Ovchinnikov
- Georgii Smirnov
- Nikolai Savushkin
- Veronika Ivanova
- Maksim Kuzin
affiliations:
- Yandex
- Yandex Applied AI Institute
arxiv_id: '2607.14331'
url: https://arxiv.org/abs/2607.14331
pdf_url: https://arxiv.org/pdf/2607.14331
published: '2026-07-15'
collected: '2026-07-17'
category: RecSys
direction: 广告CTR排序 · 长序列用户建模
tags:
- CTR Prediction
- Sequential Recommendation
- Transformer
- Ad Ranking
- Real-time Serving
one_liner: 提出离线在线拆分的长历史用户Transformer架构，在无延迟增加前提下大幅提升广告排序效果
practical_value: '- 长序列建模的离线在线拆分范式可直接复用：大模型离线预训练编码全量长历史（最长支持8192个事件）存特征库，轻量小模型在线仅编码最近几十到上百条事件，兼顾长序列信号和实时延迟要求，适配广告、电商推荐等强延迟约束场景

  - 训练-推理分布对齐的设计值得落地：训练阶段给离线编码器的历史故意加2天截断，匹配线上实际缓存的滞后分布，避免分布差导致的效果损失，该思路可推广到所有带预计算特征的排序场景

  - 缓存更新策略可直接参考：采用「用户点击触发重算」的事件驱动更新+周级全量批量更新的混合策略，实测5天缓存滞后仅损失0.38pp的NLL增益，在效果损失可接受的前提下大幅降低离线计算成本

  - 跨场景预训练双目标可复用：联合CTR预测+下一个事件检索的双目标自回归预训练，统一建模广告、搜索、有机点击等多源行为数据，可显著提升用户表征的泛用性，适配多业务线的排序需求'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
长用户交互历史是CTR预测的核心强信号，但广告排序场景有严格的百毫秒级延迟约束，实时运行大参数量长序列Transformer完全不可行，现有方案仅能使用短窗口历史，丢失大量长周期行为信号，亟需兼顾长序列建模效果和实时性能的落地方案。
### 方法关键点
- 架构拆分：10层大参数量离线Transformer异步编码用户跨场景全量8192条历史行为，输出固定长度表征缓存至特征库；5层轻量在线Transformer仅编码最近100条事件，结合离线缓存表征、请求上下文完成CTR预测
- 预训练设计：采用双目标自回归预训练，联合优化CTR预测损失和下一个事件检索损失，融入搜索、有机点击、广告等跨场景行为数据，提升用户表征泛化性
- 分布对齐：训练时故意给离线编码器的历史加2天截断，模拟线上缓存的实际滞后，避免训练线上分布不一致导致的效果损失
### 关键结果
离线在Yandex搜索广告、YAN广告网络两个场景验证，拆分架构可恢复72%~80%的不可部署全量8k长序列在线Transformer的效果；线上A/B测试搜索广告主排序指标+2.77%、收入+2.26%，YAN主指标+2.1%、收入+0.43%，无任何线上延迟增加。
### 核心结论
长序列Transformer落地的核心瓶颈不是效果，而是推理成本，通过离线在线拆分的设计可以在完全不增加线上延迟的前提下拿到绝大部分长序列建模的收益。
