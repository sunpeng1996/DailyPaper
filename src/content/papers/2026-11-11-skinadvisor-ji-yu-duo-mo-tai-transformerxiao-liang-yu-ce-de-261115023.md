---
title: 'SkinAdvisor: An AI-Driven Decision Framework for Skin Production Planning
  via Multi-Modal Transformer Sales Forecasting'
title_zh: SkinAdvisor：基于多模态Transformer销量预测的游戏皮肤生产决策框架
authors:
- Ge Fan
- Kai Wang
- Chaoyun Zhang
- Yingjie Li
- Yuze Liu
- Junyang Chen
affiliations:
- Independent Researcher
- Tencent Inc.
- Swinburne University of Technology
- CSSE, Shenzhen University
arxiv_id: '2611.15023'
url: https://arxiv.org/abs/2611.15023
pdf_url: https://arxiv.org/pdf/2611.15023
published: '2026-11-11'
collected: '2026-11-13'
category: Other
direction: 多模态时序预测 · 生产决策框架
tags:
- Multi-modal Transformer
- Time Series Forecasting
- Production Planning
- ROI Optimization
- Informer
one_liner: 提出融合多模态编码器的游戏皮肤销量预测模型及ROI驱动的生产规划Pipeline 已落地验证
practical_value: '- 冷启动商品销量预测可复用「时序偏好编码器+关系图谱嵌入+属性上下文编码器」的多模态融合架构，适配无历史数据的新商品ROI预估场景

  - 非自回归Informer解码结构可大幅提升时序预测推理性能，16核CPU下p99延迟8ms、吞吐量1100rps的参数可作为同类业务基线参考

  - 预训练嵌入易泄露时序信息，训练时需按季节拆分数据集避免数据穿越，业务场景不需要高精度，量级正确即可支撑决策'
score: 7
source: arxiv-cs.LG
depth: abstract
---

### 动机
游戏虚拟皮肤是在线游戏核心营收来源，当前生产规划（选品、发版时间、定价）依赖人工经验与回溯分析，无历史销售数据的新皮肤销量预测难度高，决策准确性差。
### 方法关键点
1. 核心预测模块SkinCast融合4类编码器：预训练Informer玩家偏好时序编码器、预训练Player-Hero-Skin关系图谱嵌入编码器、皮肤属性轻量Transformer、发版上下文轻量Transformer，通过带全局+局部位置编码的共享骨干融合，采用非自回归Informer解码一次性输出180天日销量序列；
2. 上层决策Pipeline按Select→Fill→Infer→Sales→ROI→Ranking逻辑对候选皮肤排序，支持多候选对比。
### 关键结果
- 离线RMSE较最优基线Informer降低~20%，较传统方法降低~60%；
- 16核CPU压测p99延迟<8ms，峰值吞吐量>1100rps，已完整落地一个发版周期。
