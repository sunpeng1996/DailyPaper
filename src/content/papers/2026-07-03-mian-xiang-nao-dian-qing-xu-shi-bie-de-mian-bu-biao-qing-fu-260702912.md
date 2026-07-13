---
title: 'See the Emotion: A Facial Emoji Proxy Modeling for EEG Emotion Recognition'
title_zh: 面向脑电情绪识别的面部表情符号代理建模方法
authors:
- Jingjing Hu
- Guo Dan
- Haofan Cheng
- Ying Zeng
- Zhan Si
- Jinxing Zhou
- Meng Wang
affiliations:
- Hefei University of Technology
- Institute of Artificial Intelligence, Hefei Comprehensive National Science Center
- PLA Information Engineering University
- University of Science and Technology of China
- MBZUAI
arxiv_id: '2607.02912'
url: https://arxiv.org/abs/2607.02912
pdf_url: https://arxiv.org/pdf/2607.02912
published: '2026-07-03'
collected: '2026-07-13'
category: Other
direction: 脑电情绪识别 · 跨模态可解释性生成
tags:
- EEG
- Emotion Recognition
- Cross-Modal Generation
- Explainable AI
- Regularization
one_liner: 提出将EEG信号转换为匿名面部表情符号的框架，兼顾脑电情绪识别SOTA精度与可解释性
practical_value: '- 可解释性范式可迁移：将黑盒模型的可解释性需求从特征归因转化为跨模态生成任务，比如推荐系统可解释性可以生成用户可感知的场景/符号替代抽象特征重要性说明

  - 多任务正则技巧可复用：引入和主任务语义关联的代理重建任务作为结构化正则项，在不损失主任务精度的前提下提升可解释性，可用于推荐系统多目标优化时补充弱监督信号

  - 隐私友好输出设计可参考：用匿名化的代理输出替代原始敏感信息，适用于电商用户情绪感知、广告效果归因等涉及用户敏感数据的场景'
score: 4
source: arxiv-cs.MM
depth: abstract
---

### 动机
现有基于EEG的情绪识别模型精度较高，但普遍为黑盒结构，抽象神经特征与人类可理解的情绪状态之间缺乏语义映射，可解释性差。
### 方法关键点
1. 重构EEG可解释性为跨模态生成任务，将范式从传统特征归因转向行为可视化；
2. 面部表情符号代理建模框架基于神经-面部关联的神经科学先验，将高维EEG信号转换为身份匿名的面部表情符号；
3. 框架包含两大核心模块：FMENet骨干建模表情相关的空间协同特征，FELB分支将表情符号重建作为结构化语义正则项约束主任务训练。
### 关键结果
在EAV、MMER基准数据集上取得纯EEG模型的SOTA识别精度，同时生成语义保真的面部动画，可提供透明、隐私保护的大脑情绪演化可视化能力。
