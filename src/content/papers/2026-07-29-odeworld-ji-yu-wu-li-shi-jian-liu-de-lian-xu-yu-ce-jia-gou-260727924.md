---
title: 'ODEWorld: A Continuous Predictive Architecture via Physical-Time Flow'
title_zh: ODEWorld：基于物理时间流的连续预测架构
authors:
- Dongxiu Liu
- Haoyi Niu
- Peng Cheng
- Yuan Gao
- Xirui Kang
- Sangli Teng
- Koushil Sreenath
- Xianyuan Zhan
affiliations:
- Institute for AI Industry Research (AIR), Tsinghua University
- Berkeley Artificial Intelligence Research (BAIR), University of California, Berkeley
arxiv_id: '2607.27924'
url: https://arxiv.org/abs/2607.27924
pdf_url: https://arxiv.org/pdf/2607.27924
published: '2026-07-29'
collected: '2026-08-04'
category: Agent
direction: Agent 世界建模 · 连续时序预测
tags:
- World Model
- ODE
- Continuous Prediction
- Latent Representation
- Sequential Modeling
one_liner: 提出基于物理时间流的连续时间潜空间世界模型ODEWorld，解决离散时序预测低效、表征崩塌问题
practical_value: '- 电商用户行为长序列预测、长时序召回场景可借鉴PT-Flow的连续潜空间ODE参数化思路，替代传统离散步长时序建模，降低长序列预测的误差累积

  - 生成式推荐的Semantic ID压缩、用户兴趣嵌入建模等存在表征崩塌风险的任务，可复用「在表征空间和潜速度场同时约束ODE属性」的trick，缓解长周期建模的表征退化

  - 需多时间粒度预测的业务（如大促流量预估、广告动态出价时序预测）可借鉴连续时间预测范式，无需为不同时间粒度单独训练模型'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有世界建模范式多局限于离散时间预测，捕捉物理世界动力学效率低，且潜空间世界模型长期存在表征崩塌问题，无法支持长时序、任意分辨率的预测需求。
### 方法关键点
1. 提出Physical-Time Flow（PT-Flow）范式，在结构化表征空间中嵌入ODE参数化序列数据底层动力学，将未来预测转化为压缩潜空间中ODE求解器的时序积分
2. 基于PT-Flow构建ODEWorld连续时间潜空间世界模型，在动力学表征空间和潜速度场同时约束ODE属性，提取时变特征
### 关键结果
在视频生成、机器人控制任务上性能优于现有离散时间模型，支持任意时间分辨率、反向预测，长时序预测后仍可实现高质量图像重建，输出的规划导向信息可有效降低下游策略学习成本
