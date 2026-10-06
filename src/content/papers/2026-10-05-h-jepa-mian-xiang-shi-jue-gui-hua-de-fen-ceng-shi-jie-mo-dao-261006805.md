---
title: 'H-JEPA: End-to-End Learning of Hierarchical World Models for Visual Planning'
title_zh: H-JEPA：面向视觉规划的分层世界模型端到端学习框架
authors:
- Wancong Zhang
- Basile Terver
- Michael Rabbat
- Yann LeCun
- Randall Balestriero
affiliations:
- NYU
- Advanced Machine Intelligence
- INRIA Paris
- Brown University
arxiv_id: '2610.06805'
url: https://arxiv.org/abs/2610.06805
pdf_url: https://arxiv.org/pdf/2610.06805
published: '2026-10-05'
collected: '2026-10-06'
category: Agent
direction: Agent世界模型 · 分层JEPA视觉规划
tags:
- JEPA
- World Model
- Hierarchical Planning
- Visual Planning
- Latent Representation
one_liner: 提出分层JEPA架构，每层独立潜空间匹配不同时间尺度，大幅提升长程视觉规划效率与成功率
practical_value: '- 分层抽象思路可迁移到长序列用户行为建模：上层建模长期兴趣（慢特征）、下层建模短期点击（快特征），既降低长序列预测误差累积，又能减少推理算力消耗

  - 分层规划的子目标拆解逻辑可用于LLM Agent复杂任务执行：比如电商导购Agent先定上层「完成商品转化」子目标，下层拆解为咨询应答、需求匹配、优惠引导等细粒度动作，提升任务成功率

  - 当场景存在多时间尺度特征差异时，可参考SIGReg+逆动力学损失的组合：避免潜空间坍缩到仅保留慢不变特征（比如推荐场景仅保留用户性别年龄，丢失实时行为信号）

  - 目标匹配可换用更抽象的上层潜空间度量：比如召回排序中不用原始点击序列的距离匹配，改用上层长期兴趣潜空间的距离，提升长周期兴趣匹配效果'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有单尺度JEPA世界模型仅在单一潜空间做预测规划，长程场景下预测误差累积严重、动作搜索空间爆炸，且单一潜空间无法同时适配低阶动力学建模与高阶抽象目标匹配，限制长程任务表现。

### 方法关键点
- 构建多层JEPA分层架构，每层拥有独立的状态编码器、动作编码器与潜态预测器，层级越高时间步长越粗、潜空间抽象度越高
- 端到端训练策略：每层单独用JEPA预测损失+SIGReg正则防止潜空间坍缩，上层训练梯度可回传更新下层编码器
- 自上而下分层规划逻辑：上层先规划到最终目标的粗路径，输出的每步预测作为下层的子目标，逐层拆解到原始动作输出
- 跨域适配：针对场景多变的真实环境新增逆动力学损失项，避免潜空间坍缩到仅保留慢变静态特征

### 关键实验
在4个模拟导航/操控环境测试，对比平层LeWM基线，3层H-JEPA在Visual AntMaze任务上将成功率从18%提升到73%，同时规划算力更低；在真实机器人DROID数据集上，2层H-JEPA比平层基线Fréchet保真度提升5%，算力需求降低一个数量级。

### 核心结论
当数据特征存在时间尺度差异时，分层独立潜空间建模+自顶向下子目标拆解，可同时实现长程任务成功率提升与推理算力下降。
