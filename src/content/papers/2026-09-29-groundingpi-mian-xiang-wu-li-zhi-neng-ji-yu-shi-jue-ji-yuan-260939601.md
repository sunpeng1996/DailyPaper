---
title: 'GroundingPI: A Grounding Foundation Model towards Physical Intelligence with
  Visual Primitives'
title_zh: GroundingPI：面向物理智能、基于视觉基元的定位基础模型
authors:
- Qize Yu
- Lianrui Fan
- Boyu Chen
- Jiaqi Liang
- Xini Ding
- Yue Chen
- Zetian Song
- Yuran Wang
- Yi Zou
- Kaixuan Wang
affiliations:
- XPeng Inc.
- Peking University
- The University of Hong Kong
- University of California, Berkeley
- Princeton University
arxiv_id: '2609.39601'
url: https://arxiv.org/abs/2609.39601
pdf_url: https://arxiv.org/pdf/2609.39601
published: '2026-09-29'
collected: '2026-10-13'
category: Multimodal
direction: 多模态感知 · 物理智能定位基础模型
tags:
- Grounding Model
- Multimodal Perception
- Physical Intelligence
- Autonomous Driving
- Robotics
one_liner: 提出4B参数定位基础模型，在多感知基准上超GPT-6 Astra，赋能自动驾驶与机器人任务
practical_value: '- 电商场景下直播商品识别、图搜同款的目标定位任务，可复用其将坐标量化为共享词汇的编码方法，提升杂乱场景小目标定位精度

  - 仓储拣货Agent、线下导购Agent的视觉感知模块，可直接复用GroundingPI预训练权重作为backbone，减少下游任务标注量（50%标注量即可超基线75%标注的效果）

  - 多模态模型训练可借鉴「多模态空间预训练+SFT+GRPO强化学习」三阶段范式，搭配专属数据引擎补充数据，能显著提升下游任务性能'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有通用视觉语言、视频生成骨干在杂乱场景小目标定位精度不足、推理速度慢，无法满足闭环控制需求。
### 方法关键点
提出4B参数的GroundingPI，将点、框坐标量化为共享词汇表中的token，采用多模态空间预训练+监督微调+GRPO强化学习三阶段训练，结合公开数据集与专属数据引擎的标注数据。
### 关键结果数字
在覆盖11种感知能力的34个定位基准上，对比44个基线平均精度达73.68%，超过更大参数的GPT-6 Astra（71.54%）；作为下游视觉骨干，RoboTwin 2.0分布外任务相对最强基线提升最高24.8%，RoboCasa-GR1用50%演示数据性能超基线用75%数据的效果，nuScenes数据集开环L2误差达0.296m。
