---
title: Understanding the limits of latent world models
title_zh: 潜层世界模型的局限分析：任务成功不等于动力学建模准确
authors:
- Rodrigo Gonzalez Laiz
- Steffen Schneider
affiliations:
- Helmholtz Munich
- Munich Center for Machine Learning (MCML)
arxiv_id: '2610.37588'
url: https://arxiv.org/abs/2610.37588
pdf_url: https://arxiv.org/pdf/2610.37588
published: '2026-10-27'
collected: '2026-10-28'
category: Agent
direction: Agent 世界模型可靠性评估
tags:
- WorldModel
- ModelBasedRL
- Probing
- LatentDynamics
- RepresentationLearning
one_liner: 提出忠实性度量LRC，验证现有SOTA潜层世界模型高奖励下仍未准确建模环境真实动力学
practical_value: '- 做Agent决策/规划系统（如多步营销序列优化、客服Agent应答规划）时，不能仅靠业务Reward评估世界模型性能，需补充类LRC的隐空间多步预测一致性指标和关键状态探针，避免高Reward下的建模失效

  - 从非结构化数据（如用户行为序列、商品内容图像）学习用户/商品状态表征时，需显式加入动态属性（如用户兴趣变化速率、商品热度变化率）的建模约束，降低非线性观测带来的关键动态信息丢失

  - 做生成式推荐的长序列规划（如用户全生命周期运营、多触点触达优化）时，不要仅用单步预测损失训练动力学模型，需验证多步隐层预测的一致性，避免长horizon规划完全偏离真实用户反馈'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
当前潜层世界模型是通用Agent长时序决策的核心组件，但行业普遍仅通过任务Reward评估模型性能，无法判断其是否真的学到了符合环境真实结构的隐层动力学，易出现高任务表现下的跨场景、长horizon泛化失效。
### 方法关键点
- 定义**忠实潜层世界模型**：需满足两个核心条件：① 隐层动力学与真实环境状态变换满足等变性；② 隐层表示可完整还原真实环境状态
- 提出 **Latent Rollout Consistency (LRC)** 度量：对比自回归预测的隐状态序列与真实观测编码得到的隐状态序列的加权R²，100%代表预测完全一致
- 配套后验非线性状态解码探针：量化隐层表示中可还原的真实环境状态信息量，排除隐空间坍缩导致的伪高LRC
### 关键实验
在3个低维连续控制环境（Pendulum、CartPole、Reacher）上测试3类SOTA潜层世界模型（DreamerV3、TD-MPC2、LeWM），核心结果：
1. 像素输入模型即使任务Reward接近满值，30步LRC可低至0%，远低于状态输入模型的80%+水平
2. 像素输入模型的速度类属性解码误差比位置类高3~10倍，显式注入真实速度后LRC最高可提升70个百分点
3. 即使输入包含完整状态信息，经过3层可逆非线性变换后，模型LRC可降至0，任务Reward完全失效
### 核心结论
任务成功不代表世界模型学到了真实的环境动力学，高Reward下的隐层建模缺陷会直接导致长horizon决策的泛化失效
