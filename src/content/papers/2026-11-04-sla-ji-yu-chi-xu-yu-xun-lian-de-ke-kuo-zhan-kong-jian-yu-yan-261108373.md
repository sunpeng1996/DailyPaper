---
title: 'SLA: Scaling Spatial-Language-Action Model via Continual Pre-training'
title_zh: SLA：基于持续预训练的可扩展空间-语言-动作模型
authors:
- Fuhao Li
- Wenxuan Song
- Qizhou Huang
- Ziyang Zhou
- Jingbo Wang
- Junwu E
- Pengwei Wang
- Yan Wang
- Shunbo Zhou
- Haoang Li
affiliations:
- The Hong Kong University of Science and Technology (Guangzhou)
- OLA Dimensions
- Beijing Academy of Artificial Intelligence
- Tsinghua University
arxiv_id: '2611.08373'
url: https://arxiv.org/abs/2611.08373
pdf_url: https://arxiv.org/pdf/2611.08373
published: '2026-11-04'
collected: '2026-11-07'
category: Agent
direction: 具身Agent · 空间-语言-动作预训练
tags:
- Continual Pre-training
- Vision-Language-Action
- Embodied Agent
- Spatial Alignment
- Robotics
one_liner: 提出持续预训练阶段注入空间对齐能力的具身VLA模型SLA，真实场景成功率较基线提升24pct
practical_value: '- 持续预训练阶段引入冻结专家模型做特征对齐的思路，可迁移到多模态推荐的跨模态（文本/图像/3D商品）表征对齐任务，无需改动推理架构

  - 特征依赖门自适应聚合多中间层特征做监督的方法，可复用在异构行为数据融合的用户建模、多源召回结果融合场景，提升异质数据利用率

  - 概率状态Dropout缓解演示轨迹过拟合的trick，可用于Agent仿真训练、推荐系统模拟环境预训练阶段，提升模型泛化性'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有VLA基础模型的视觉表征多继承自2D视觉-语言预训练，空间监督仅在下游任务适配阶段引入，空间理解泛化能力不足，无法支撑跨场景机器人操控需求。
### 方法关键点
1. 基于预训练pi0.5策略初始化SLA，联合优化动作预测、中间视觉embedding与冻结3D感知模型空间表征的对齐双任务；
2. 统一异构机器人数据集支撑跨形态/任务/场景的空间学习，引入特征依赖门自适应聚合多层VLA视觉embedding做空间监督，结合深度、相机标定信息复用异构几何标注；
3. 采用概率状态Dropout缓解演示轨迹过拟合，所有辅助组件仅训练阶段启用，无需改动原有推理架构。
### 关键结果
在RoboDojo-Real、RoboTwin 2.0等4个基准测试集达SOTA，8种真实部署场景下平均成功率较pi0.5基线提升24.0个百分点
