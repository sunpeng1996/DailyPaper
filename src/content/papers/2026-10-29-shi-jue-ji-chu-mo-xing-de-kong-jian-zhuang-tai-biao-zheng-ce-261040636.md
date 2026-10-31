---
title: Probing Spatial State Representations in Visual Foundation Models
title_zh: 视觉基础模型的空间状态表征探测研究
authors:
- Baiqiao Yin
- Zhongang Cai
- Ruisi Wang
- Qiwei Liang
- Lei Yang
- Ziwei Liu
affiliations:
- New York University
- Nanyang Technological University
- The Hong Kong University of Science and Technology
- The Chinese University of Hong Kong
arxiv_id: '2610.40636'
url: https://arxiv.org/abs/2610.40636
pdf_url: https://arxiv.org/pdf/2610.40636
published: '2026-10-29'
collected: '2026-10-31'
category: Multimodal
direction: 多模态基础模型 · 空间表征能力探测
tags:
- Visual Foundation Model
- Spatial Representation
- Probing
- Object Persistence
- Actionability
one_liner: 通过四层能力体系探测视觉基础模型的空间状态表征特性并提出新评估标准
practical_value: '- 做AR导购、虚拟直播间等多模态Agent时，可复用四层空间能力框架评估VFM的空间感知可用性

  - 冻结特征探针的评估方法可低成本验证预训练视觉特征的下游适配性，无需全量微调

  - 空间相关任务需同时校验可见解码、非可见信息留存、预测更新、动作导向四个维度，避免单指标高估特征价值'
score: 6
source: arxiv-cs.AI
depth: abstract
---

### 动机
现有视觉基础模型(VFM)的表征是否支持可随自身运动更新、可指导动作的持久空间状态尚不明确，单一可见场景解码指标无法全面衡量空间感知能力。
### 方法关键点
1. 定义空间结构、物体持久性、预测性空间更新、可执行性四层递进的空间能力评估维度
2. 针对静态室内环境流式第一人称观测数据，采用冻结特征探针测试10种VFM表征的空间能力表现
3. 设置匹配对照实验，分离表征解码精度对视觉历史、运动信息的依赖
### 关键结果
强可见场景解码能力不保证准确的物体持久性或未来特征检索效果；在真实特征上训练的空间读取器无法直接迁移到预测特征；物体持久性与可执行性依赖相机位姿解码，特征预测依赖可见场景读取能力。
