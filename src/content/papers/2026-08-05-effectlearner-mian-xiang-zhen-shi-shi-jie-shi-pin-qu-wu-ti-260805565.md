---
title: 'EffectLearner: World-Aware Object-Effect Reasoning for Real-World Video Object
  Removal'
title_zh: EffectLearner：面向真实世界视频去物体的世界感知物体效应推理
authors:
- Feier Wu
- Wanke Xia
- Xu He
- Zilang Zhou
- Si Chen
- Dongxia Liu
- Liyang Chen
- Qimeng Wu
- Zhengbo Zhang
- Wenming Yang
affiliations:
- Tsinghua University
- China Agricultural University
- Jiangnan University
- Institute of Automation, Chinese Academy of Science
arxiv_id: '2608.05565'
url: https://arxiv.org/abs/2608.05565
pdf_url: https://arxiv.org/pdf/2608.05565
published: '2026-08-05'
collected: '2026-08-07'
category: Multimodal
direction: 多模态视频编辑 · 物体效应推理
tags:
- Video Object Removal
- VLM
- DiT
- Multimodal Reasoning
- Dataset Construction
- Progressive Training
one_liner: 提出VLM推理器+DiT擦除器的视频去物体框架，可同步去除目标物体及其诱导效应
practical_value: '- 电商短视频素材生产场景可复用该框架，自动去除视频中多余杂物、水印、无关人物，降低人力剪辑成本

  - VLM先做语义推理提取约束、再引导生成模型输出的范式，可迁移到AI生成商品短视频、商修图等任务

  - 通用样本+难例结合的渐进式训练策略，可复用在存在长尾场景的生成类业务模型训练中，提升泛化性'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有视频去物体方法仅隐式学习物体-效应对应关系，受限于预定义效应类别与固定数据分布，泛化性差，无法处理复合效应、空间分离效应、长尾物理现象等复杂真实场景。
### 方法关键点
1. 构建EffectLearner语义推理增强框架，包含VLM驱动的物体效应推理器、DiT-based视频擦除器两个核心模块
2. 推理器通过结构化prompt对高亮目标的视频做跨模态推理，提取效应感知上下文引导擦除，确保物体及其诱导效应被同步去除
3. 加入运动感知mask引导、运动一致性监督，提升物体运动与场景动态变化下的去除覆盖度与时空稳定性
4. 构建EffectWorld复杂物体效应配对视频数据集，采用通用样本+复杂效应样本结合的渐进式训练策略
### 关键结果
在标准ROSE-Bench上多数指标优于现有基线，在EffectWorld-Eval、EffectWorld-Wild测试集上均有显著优势，可实现复杂真实场景的高质量视频去物体
