---
title: 'Round-Trip Consistency: Bidirectional Diffusion Models Can Predict Their Own
  Rollout Errors'
title_zh: 往返一致性：双向扩散模型可自预测推理迭代误差
authors:
- Alexander Scheinker
affiliations:
- Los Alamos National Laboratory
arxiv_id: '2608.00675'
url: https://arxiv.org/abs/2608.00675
pdf_url: https://arxiv.org/pdf/2608.00675
published: '2026-08-01'
collected: '2026-08-10'
category: Training
direction: 扩散模型训练 · 推理误差自校准
tags:
- Diffusion Model
- Autoregressive Inference
- Error Estimation
- Self-supervised Calibration
- Bidirectional Learning
one_liner: 训练带方向标记的双向扩散模型，通过往返差异生成无标注推理迭代误差代理信号
practical_value: '- 多步序列生成类任务（如长会话推荐路径规划、Agent多轮决策）可复用往返一致性思路：正向生成k步结果后逆向回推初始状态，用差异度量生成误差无需额外标注

  - 双向模型可通过加方向标记的单模型实现，训练成本低于分别训练正向/逆向专家模型，可迁移到用户行为回溯、搜索query改写这类需双向能力的场景

  - 往返差异可直接作为无监督OOD检测信号，无需额外校准数据，可用于推荐系统冷启动物料、异常用户交互行为的快速识别'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
自回归模型长序列迭代推理时会持续累计误差，部署阶段无真值可用于误差度量，传统方案依赖集成模型、预留标注数据或先验规则，落地成本高。
### 方法关键点
训练单条件隐扩散模型，新增方向标记控制模型执行时间步正向/逆向推理；定义i步正向推理后再执行i步逆向推理的往返差异C_i，作为无监督的推理误差代理信号，仅需额外一次推理开销，无需其他辅助数据。
### 关键结果
- 流体力学MHD数据集上，C_i与真实推理误差的Spearman相关系数达0.91~0.98，分布外样本检测AUROC达0.98，推理深度为10时AUROC达1.0
- 同等精度下，单双向模型训练成本仅为10模型集成方案的1/10，误差削减效率是仅依赖推理深度的基线方案的3倍
