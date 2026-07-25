---
title: 'ReferTrack: Referring Then Tracking for Embodied Visual Tracking'
title_zh: ReferTrack：面向具身视觉跟踪的先指代后跟踪范式
authors:
- Hanjing Ye
- Tianle Zeng
- Jiazhao Zhang
- Shaoan Wang
- Zibo Zhang
- Weisi Situ
- Yuchen Zhou
- Yonggen Ling
- Hong Zhang
affiliations:
- RCV Laboratory, SUSTech
- Tencent Robotics X
- Peking University
- Futian Laboratory
arxiv_id: '2607.20061'
url: https://arxiv.org/abs/2607.20061
pdf_url: https://arxiv.org/pdf/2607.20061
published: '2026-07-21'
collected: '2026-07-25'
category: Agent
direction: 具身Agent · 视觉目标跟踪
tags:
- Embodied Agent
- Visual Tracking
- Vision-Language-Action
- CoT
- Sim2Real
one_liner: 提出先指代后跟踪的具身视觉跟踪范式，单目摄像头性能匹配甚至超过多相机基线
practical_value: '- 多模态指代+跟踪的两阶段范式可直接迁移到电商直播商品跟随Agent、线下导购机器人的目标用户/商品识别跟踪场景，降低端到端VLA模型的对齐难度

  - 滑动窗口缓存历史目标特征+时序指示token注入的方法，可复用在推荐系统长短期用户行为序列建模、实时兴趣捕捉模块，提升序列特征的时序一致性

  - 针对核心识别任务定制小样本QA数据集做联合训练的思路，可用于提升业务场景中LLM对特定领域目标（如小众商品、指定用户群体）的识别准确率

  - 单摄像头低成本实现SOTA跟踪的方案，可复用在电商线下门店、智能货柜的客流/商品跟踪Agent落地，大幅降低硬件部署成本'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
具身视觉跟踪（EVT）要求移动Agent仅靠机载视觉跟随自然语言描述的目标，现有VLA策略的CoT推理在抽象空间隐变量中运行，难监督且与图像空间检测对齐度低。
### 方法关键点
1. 采用先指代后跟踪范式，先从索引的边界框集合中筛选目标，再基于该图像域决策解码跟踪航点；
2. 维护历史选中框的滑动窗口队列，通过TVBI token将几何特征注入视觉历史，保留目标长时运动线索；
3. 基于自定义Refer-QA数据集联合训练，强化目标识别准确率。
### 关键结果
在EVT-Bench上单视图性能达SOTA，单目标、干扰项、歧义跟踪分块成功率分别为89.4%、73.3%、74.1%，匹配甚至超过多个多相机基线，足式、人形机器人真实部署验证了优秀的sim-to-real迁移能力。
