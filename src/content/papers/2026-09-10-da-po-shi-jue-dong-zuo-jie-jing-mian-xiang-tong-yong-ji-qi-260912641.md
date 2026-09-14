---
title: 'Breaking the Vision-Action Shortcut: Latent Interface Training for Generalizable
  Robotics Foundation Models'
title_zh: 打破视觉-动作捷径：面向通用机器人基础模型的隐层接口训练
authors:
- Jianman Lin
- Shailesh Shailesh
- Zhongyi Luo
- Jiafei Duan
arxiv_id: '2609.12641'
url: https://arxiv.org/abs/2609.12641
pdf_url: https://arxiv.org/pdf/2609.12641
published: '2026-09-10'
collected: '2026-09-14'
category: Other
direction: 机器人基础模型·分布外泛化优化
tags:
- Robotics Foundation Model
- Distribution Shift
- Generalization
- Latent Interface
- Vision-Action Model
one_liner: 提出两阶段隐层接口训练策略，缓解机器人基础模型视觉-动作捷径，提升分布外泛化能力
practical_value: '- 分布漂移场景下的虚假关联缓解思路可复用：推荐系统中特征与标签的伪相关问题，可参考两阶段训练逻辑，先学习核心任务决策逻辑再接入易漂移特征

  - 隐层接口监督方法可借鉴：多模态推荐/Agent感知模块可增加下游核心任务目标的监督信号，过滤无关特征噪声，提升跨场景泛化性

  - 框架无关的插件式优化思路可复用：无需重构原有模型架构，仅新增轻量接口层和辅助监督即可提升分布外性能，落地成本低'
score: 4
source: huggingface-daily
depth: abstract
---

### 动机
机器人基础模型分布内表现优异，但遇到视觉分布漂移时性能骤降，核心原因是模型学习到训练分布中与动作关联的无关视觉cue，形成视觉-动作捷径，破坏泛化性。

### 方法关键点
提出两阶段隐层接口训练（LIT）框架，与现有架构完全兼容：
1. 第一阶段不输入图像，仅用语言、机器人状态、示范动作的终端执行器位姿训练动作专家，学习独立于视觉信号的目标导向动作生成先验
2. 第二阶段引入隐层接口，聚合视觉与语义表征作为动作专家的唯一视觉输入通路，用第一阶段的终端位姿作为监督信号训练接口，强制其保留动作生成所需的目标相关空间信息

### 关键结果
在4类主流机器人架构上测试，LIBERO-Plus成功率提升3.87-10.70个百分点；真实场景下，未见过的相机配置、光照变化、干扰物环境中，3类任务综合成功率提升13.30-16.70个百分点。
