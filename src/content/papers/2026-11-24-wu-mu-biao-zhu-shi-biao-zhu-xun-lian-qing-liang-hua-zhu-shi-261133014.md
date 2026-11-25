---
title: 'Training Lightweight Gaze Models without Target Gaze Annotation: What Makes
  a Good Teacher?'
title_zh: 无目标注视标注训练轻量化注视模型：如何选择优质教师模型
authors:
- Scott J. Lewis
- Di Fu
affiliations:
- School of Computer Science and Electronic Engineering, University of Surrey
- School of Psychology, University of Surrey
- Surrey Institute for People-Centred AI, University of Surrey
arxiv_id: '2611.33014'
url: https://arxiv.org/abs/2611.33014
pdf_url: https://arxiv.org/pdf/2611.33014
published: '2026-11-24'
collected: '2026-11-25'
category: Training
direction: 模型蒸馏 · 轻量化模型训练
tags:
- Model Distillation
- Lightweight Model
- Weak Supervision
- Teacher Selection
- Pseudo Label
one_liner: 通过11组对照实验总结出无需目标标注蒸馏轻量化模型时的教师选择与评估原则
practical_value: '- 做端侧轻量化LLM/多模态模型蒸馏时，可先用少量标注验证集计算教师输出的标签误差，提前筛选优质教师，无需跑完完整蒸馏流程

  - 用大模型生成伪标注做弱监督训练时，要排查大模型的捷径输出（如直接复制prompt内的已知信息），避免伪标注质量虚高

  - 不完美的伪标注也可替代人工标注训练小模型，效果甚至超过人工标注训练的同规模模型，可大幅降低标注成本'
score: 7
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有基于大模型生成伪标注训练轻量化小模型的方案缺乏可落地的教师选择标准，无法预先判断教师质量，实验试错成本高。
### 方法关键点
固定学生模型结构、训练策略、361k训练样本，仅改变注视点标签来源，对比11种监督条件，跨3个视频数据集、2种学生尺寸、3个随机种子，所有学生统一用人脸标注评估。
### 关键结果数字
1. 未在目标数据集标注上训练的Gaze-LLE生成的伪标签训练的ViT-Small，比人工标注训练的精度更高（平均距离误差0.187 vs 0.196），ViT-Tiny学生比教师快32倍；
2. 含prompt坐标泄露时InternVL3等VLM的伪标注93.4%是直接复制坐标，无泄露时性能远低于专用模型；
3. 验证集标签误差和学生测试误差的Spearman相关系数达0.91，仅用10个标注片段就能以95%概率筛选出最优的2个专用教师模型。
