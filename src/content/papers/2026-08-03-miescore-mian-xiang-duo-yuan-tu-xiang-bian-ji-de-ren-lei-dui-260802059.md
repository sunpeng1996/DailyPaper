---
title: 'MIEScore: Human-Aligned Evaluation for Multi-Source Image Editing'
title_zh: MIEScore：面向多源图像编辑的人类对齐评估方法
authors:
- Zitong Xu
- Huiyu Duan
- Xinyun Zhang
- Weifei Xiong
- Tianyi Zheng
- Xiongkuo Min
- Qiang Hu
- Zhengxue Cheng
- Bo Li
- Guangtao Zhai
affiliations:
- Shanghai Jiao Tong University
- Vivo Mobile Communication Co., Ltd
- University of Electronic and Science Technology of China
arxiv_id: '2608.02059'
url: https://arxiv.org/abs/2608.02059
pdf_url: https://arxiv.org/pdf/2608.02059
published: '2026-08-03'
collected: '2026-08-07'
category: Eval
direction: 多模态图像编辑 · 人类对齐评估
tags:
- Multimodal Evaluation
- Image Editing
- Human Alignment
- MLLM
- Benchmark
one_liner: 提出首个大规模多源图像编辑基准MIE-Bench及人类对齐的MLLM评估模型MIEScore
practical_value: '- 电商场景中商品图合成、风格融合、人物背景拼接等AI修图效果的自动化评估可直接复用MIEScore的多维度打分框架，大幅减少人工审核成本

  - 构建生成内容类评估基准时，可参考MIE-Bench的细粒度标注方法，覆盖指令遵循度、属性保留度、视觉质量三个核心维度，提升评估结果的人类对齐度

  - 基于MLLM搭建生成内容评估模型时，可复用技能优化+多维度SFT的训练范式，仅需微调少量参数即可实现特定生成任务的评估效果提升，降低训练成本'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
当前多源图像编辑（MIE）技术快速发展，可实现物体合成、跨图风格融合、人景拼接等复杂任务，但现有图像编辑评估基准与方法仅针对单图编辑场景，缺乏符合人类偏好的大规模MIE专用评估体系。
### 方法关键点
1. 构建MIE-Bench：覆盖16类任务共3000个编辑实例，每个实例含≥2张源图与编辑Prompt，收集12个SOTA编辑模型生成的36K编辑结果，标注超108K MOS分，覆盖视觉质量、指令遵循、属性保留三个核心维度。
2. 提出MIEScore：基于MLLM结合技能优化、多维度SFT训练，实现MIE效果的人类对齐自动化评估。
### 关键结果
MIEScore在人类偏好对齐指标上达到SOTA，且在其他通用图像编辑评估数据集上表现出优异的跨域泛化性。
