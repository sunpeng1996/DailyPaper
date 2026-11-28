---
title: 'DexEngine: Scaling Human Demonstrations into Physically Executable Whole-Robot
  Data'
title_zh: DexEngine：将人类操作演示转化为可物理执行的全机器人训练数据
authors:
- Wongyun Yu
- Honggeun Kim
- Donguk Lee
- Minchan Kim
- Kyoung Whan Choe
- Minsu Cho
affiliations:
- POSTECH
- RLWRLD
arxiv_id: '2611.33579'
url: https://arxiv.org/abs/2611.33579
pdf_url: https://arxiv.org/pdf/2611.33579
published: '2026-11-24'
collected: '2026-11-28'
category: Other
direction: 机器人操作 · 人类演示数据转译流水线
tags:
- Robotics
- Demonstration Retargeting
- Reinforcement Learning
- Simulation Pipeline
- Data Augmentation
one_liner: 提出仿真流水线DexEngine，可批量将人类操作演示转化为物理可执行的全臂-机械手训练数据
practical_value: '- 数据生产流水线可参考「前置约束校验→初步拟合→残差修正→批量扩增」的架构，兼顾生成效率和质量，适合推荐/广告领域大物料库、大用户行为数据的预处理场景

  - 训练数据增加符合物理/业务规则的修正环节，可比直接使用原始标注数据大幅提升下游模型性能，该结论可复用在需符合业务约束的推荐排序、文案生成等任务

  - 批量数据生成时先做可行性过滤再进入重计算环节，可显著降低无效计算开销，适合大语料、大样本量的预处理流程'
score: 4
source: huggingface-daily
depth: abstract
---

### 动机
现有将人类手部操作演示转译为机器人训练数据的方案，无法批量生成运动学可行、物理可执行的全臂+手整机器人策略训练数据，纯RL类方法生成效率极低。
### 方法关键点
1. 先将人类手部-物体交互片段定位到机械臂可达范围，求解跟随人类手部动作的机械臂基础运动轨迹
2. 采用残差RL在物理仿真环境中修正轨迹，保证输出结果的物理可执行性
3. 支持多类灵巧手适配，内置数据增强流程可快速扩容训练样本量
### 关键结果数字
基于9个人类手部操作数据集，为4款灵巧手各生成约5200条原始片段，扩增后共得到6.5万条轨迹（116h）、32.5万条训练片段（578h）；目标跟踪精度优于现有浮动手方法，生成速度比RL类方案快10倍以上；用其生成数据训练的机器人策略，性能显著优于无物理修正的基线，同等微调预算下做训练中增量微调可同时提升仿真和真机效果
