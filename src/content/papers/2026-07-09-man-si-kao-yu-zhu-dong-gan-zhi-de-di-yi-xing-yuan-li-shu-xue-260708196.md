---
title: A First-Principles Theory of Slow Thinking and Active Perception
title_zh: 慢思考与主动感知的第一性原理数学理论框架
authors:
- Hongkang Yang
- Zhi-Qin John Xu
- Feiyu Xiong
- Weinan E
affiliations:
- MemTensor (Shanghai) Technology Co., Ltd.
- Institute for Advanced Algorithms Research, Shanghai
- Shanghai JiaoTong University
- Peking University
arxiv_id: '2607.08196'
url: https://arxiv.org/abs/2607.08196
pdf_url: https://arxiv.org/pdf/2607.08196
published: '2026-07-09'
collected: '2026-07-10'
category: Reasoning
direction: 大模型慢思考 · 第一性原理理论
tags:
- SlowThinking
- ActivePerception
- FirstPrinciples
- LLMTheory
- Reasoning
one_liner: 从第一性原理推导慢思考的数学形式，给出大模型慢思考能力的三阶优化路径
practical_value: '- 落地Agent推理模块时可复用其三阶优化路径，优先升级采样效率再优化表达能力，最后放开思维链格式约束，降低迭代试错成本

  - 解决慢思考RL训练的policy collapse问题，可同时拟合后验采样器与好奇采样器，平衡隐空间的探索与利用，避免推理能力退化

  - 做多模态内容/商品特征提取时，可借鉴主动感知的不确定性最大化降低目标，优先抽取高区分度特征，提升特征编码效率'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有AI领域主要靠工程试错迭代，缺乏第一性原理指导，容易走弯路、浪费资源；慢思考（系统2）、主动感知等认知能力没有统一的数学建模框架，大模型推理能力的优化方向模糊。
### 方法关键点
- 提出「主动提升（active lifting）」理论，通过将观测空间的复杂概率分布映射到隐空间，实现用神经网络等简单函数族拟合复杂分布
- 构建表示层级、采样器层级两个优化轴，现有慢思考模型可通过攀爬两个层级持续升级能力
- 明确慢思考模型的三阶优化路径：阶段一提升采样效率，阶段二增强近似表达能力、天然平衡快慢思考，阶段三实现无预设格式的自由慢思考
- 给出统一训练目标：最大化不确定性降低速率，可自然导出全部静态理论结论
### 关键实验
仅开展初步原理验证实验，暂未披露公开数据集上的量化对比结果
### 核心结论
慢思考的本质是模型自主构造内部「思维语言」拆解复杂任务，其能力上限由表达能力与采样效率共同决定
