---
title: Leveraging Psychophysical Attentional Distribution for Gaze-Augmented Reward
  Modeling
title_zh: 基于心理物理注意力分布的眼动增强奖励建模方法
authors:
- Chaeho Lee
- Junyup Kim
- Wansoo Kim
- Young Min Jung
- Sang Ho Lee
affiliations:
- KAIST School of Digital Humanities and Computational Social Sciences
- KAIST Department of Brain & Cognitive Sciences
- KAIST Graduate School of Data Science
arxiv_id: '2611.13477'
url: https://arxiv.org/abs/2611.13477
pdf_url: https://arxiv.org/pdf/2611.13477
published: '2026-11-10'
collected: '2026-11-11'
category: Training
direction: LLM对齐训练 · 眼动特征增强奖励建模
tags:
- Reward Modeling
- RLHF
- Gaze Feature
- Attention Distribution
- LLM Alignment
one_liner: 引入阅读注意力非对称高斯分布重构眼动特征，提升RLHF奖励模型偏好预测准确率
practical_value: '- 做用户兴趣建模时，可将离散交互特征（点击、停留时长）按非对称高斯分布平滑分配给相邻内容/商品，模拟用户感知范围，提升建模准确率

  - 对于噪声较高的离散行为特征，可通过空间平滑方式降噪，减少单个异常点的影响，提升模型训练稳定性

  - 做Agent或生成式推荐的人类偏好对齐时，可挖掘用户交互过程中的隐式信号（滑动速度、停留时长），通过分布重构增强信号价值，降低对齐标注成本'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
标准RLHF的奖励模型仅依赖最终偏好标签，忽略人类判断过程中的认知信号；现有眼动增强奖励模型仅将眼动特征绑定到单个注视token，不符合人类阅读时注意力覆盖周边区域的认知规律，无法充分挖掘眼动信号价值。

### 方法关键点
- 在GazeReward框架的眼动特征生成与投影之间新增重分布模块，选择总阅读时长（TRT）作为核心眼动特征
- 用可学习非对称高斯核将每个token的TRT权重分配到相邻token，左侧、右侧σ参数独立学习，分别控制注视点左右的注意力扩散范围，权重归一化保证TRT总量不变
- 重分布后的TRT特征与文本特征通过拼接或相加融合，不修改原奖励模型的训练目标与主干结构

### 关键实验
在OASST1、HelpSteer2、UltraFeedback三个公开偏好数据集上，以原GazeReward为基线，采用Llama-3-8B系列作为主干。结果显示：OASST1数据集GazeConcat配置下相对精度提升最高达9.29%，UltraFeedback数据集上相对提升13.02%；同时模型输出的标准差更低，训练稳定性更优；学习到的σ_right普遍大于σ_left，与人类左到右阅读的感知跨度规律一致。

将认知科学的成熟结论引入大模型训练，不仅能直接提升性能，还能同时提升模型的可解释性与训练稳定性。
