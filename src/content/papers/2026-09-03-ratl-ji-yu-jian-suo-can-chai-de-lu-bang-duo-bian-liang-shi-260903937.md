---
title: 'RATL: Learning from Retrieved Residuals for Robust Multivariate Time-Series
  Forecasting'
title_zh: RATL：基于检索残差的鲁棒多变量时间序列预测方法
authors:
- Yuchen He
- Yueyang Cang
- Zhiyuan Ning
- Ningyu Wang
- Li Shi
affiliations:
- Department of Automation, Tsinghua University
- State Key Laboratory of Hydroscience and Engineering, Tsinghua University
arxiv_id: '2609.03937'
url: https://arxiv.org/abs/2609.03937
pdf_url: https://arxiv.org/pdf/2609.03937
published: '2026-09-03'
collected: '2026-09-05'
category: Other
direction: 时序预测 · 检索增强残差校正
tags:
- Time-Series Forecasting
- RAG
- Residual Learning
- Plug-in Module
- Robust Prediction
one_liner: 提出即插即用的残差检索校正框架RATL，无需改动基模型即可提升时序预测性能
practical_value: '- 电商销量、流量、库存等时序预测场景可直接复用RATL即插即用架构，无需改动现有基预测模型即可通过残差检索校正提升精度

  - 可借鉴「检索基模型历史残差而非原始目标值」的思路，解决RAG用于回归任务时不同样本数值尺度、动态性差异导致的鲁棒性问题

  - 时序类预测上线时可引入验证集驱动的校正强度自适应选择机制，避免残差注入过多导致的预测偏差'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
RAG思路迁移到连续输出回归任务时，直接检索历史目标值易受样本输出量级、数值尺度、局部动态性差异影响，鲁棒性差；传统时序预测流程仅将残差用于训练优化和错误诊断，未将历史残差作为推理阶段可访问的记忆资源。
### 方法关键点
1. 冻结基预测器构造检索键，将其历史预测残差构建为基模型专属的训练态记忆库
2. 推理时在因果可用性约束下检索相似历史上下文的残差轨迹，通过集合感知路由模块选择融合多段残差
3. 引入验证集驱动的校正强度选择机制，避免残差过度注入导致的预测偏差
### 关键结果
以iTransformer为核心冻结基预测器的实验中，RATL在90%以上的时序预测基准场景下性能优于现有强基线，且可跨不同基预测器架构迁移，无精度下降情况。
