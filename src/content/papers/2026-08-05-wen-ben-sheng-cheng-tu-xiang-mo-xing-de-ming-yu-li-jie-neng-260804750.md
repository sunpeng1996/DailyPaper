---
title: 'Simile Understanding in Text-to-Image Models: An Evaluation Framework'
title_zh: 文本生成图像模型的明喻理解能力评估框架
authors:
- Luecheng Wang
- Shintaro Ozaki
- Hidetaka Kamigaito
- Katsuhiko Hayashi
- Jingun Kwon
- Manabu Okumura
- Taro Watanabe
affiliations:
- The University of Tokyo
- Nara Institute of Science and Technology
- Chungnam National University
- Institute of Science Tokyo
arxiv_id: '2608.04750'
url: https://arxiv.org/abs/2608.04750
pdf_url: https://arxiv.org/pdf/2608.04750
published: '2026-08-05'
collected: '2026-08-07'
category: Eval
direction: 多模态生成·文本转图像能力评估
tags:
- Text-to-Image
- Simile Understanding
- Diffusion Model
- Evaluation Framework
- Object Detection
one_liner: 构建可扩展的文生图模型明喻理解评估体系，含可控数据集、自动度量与生成过程分析工具
practical_value: '- 电商商品营销文案转商品图场景，可复用该框架的自动评估逻辑，用YOLO检测验证生成图是否符合比喻类文案语义，避免「丝绸一样光滑的面料」生成丝绸布料这类错误

  - 多模态Agent的文生图调用链路可接入该评估逻辑做结果校验，自动过滤不符合修辞语义的低质量生成内容

  - 多模态生成模型微调场景，可复用其可控对比数据集构造方法，针对性优化模型对修辞类prompt的理解能力'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
当前文生图（T2I）模型对包含明喻的prompt普遍存在理解偏差，常把修辞载体误作为生成主体，暴露了比喻类修辞语言与视觉接地之间的能力缺口，缺乏统一可扩展的评估方案。

### 方法关键点
1. 构建可控明喻数据集，修辞载体均来自可检测的物体类别，搭配多样prompt模板；
2. 基于YOLO目标检测设计自动接地度量指标，量化明喻理解准确率；
3. 采用Diffusion Lens分析文本编码器层，追踪修辞载体在生成过程中的特征变化。

### 关键结果
跨不同架构的T2I模型实验均观测到一致的「字面化理解」错误模式，验证了评估框架的通用性，同时给出了针对性的模型优化方向。
