---
title: 'APO: Unsupervised Atomic Policy Optimization for 3D Structure Prediction of
  Atomic Systems'
title_zh: APO：用于原子系统3D结构预测的无监督原子策略优化
authors:
- Shentong Mo
- Yatao Bian
affiliations:
- CMU
- NUS
arxiv_id: '2607.28553'
url: https://arxiv.org/abs/2607.28553
pdf_url: https://arxiv.org/pdf/2607.28553
published: '2026-07-30'
collected: '2026-08-03'
category: Other
direction: 原子系统3D结构预测 · 无监督优化
tags:
- Unsupervised Learning
- Policy Optimization
- 3D Structure Prediction
- Generative Model
- Flow Matching
one_liner: 提出无监督原子策略优化框架APO，无需真实结构标签，在晶体抗体结构预测任务上超监督基线达SOTA
practical_value: 主要是学术贡献，业务可借鉴点有限
score: 3
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有原子系统3D结构预测流匹配模型依赖带真实坐标标签的监督偏好学习，新型晶相、从头蛋白的实验标签获取成本极高，是数据稀缺场景下结构建模的核心瓶颈。

### 方法关键点
适配3D原子环境的组相对策略优化，采用双奖励机制：
1. 光谱一致性得分：通过样本相似度特征分解强化策略主导隐结构模式
2. 晶体熵代理：约束热力学稳定性，支持模型在采样组内识别物理合理配置实现自校正

### 关键结果数字
- 晶体、抗体结构预测基准上持续优于全监督基线，匹配率和结构保真度达SOTA
- 拉直概率路径，推理效率得到显著提升
- 证明内在物理一致性比带噪监督坐标匹配是更优的对齐指导
