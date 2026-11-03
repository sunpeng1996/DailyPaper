---
title: Multi-Teacher Reasoning Distillation for LLM Recommendation with Self-Exploration
title_zh: 面向大语言模型推荐的多教师推理蒸馏与自探索框架
authors:
- Liangbo Ning
- Siyuan Liang
- Yi Zhou
- Yifeng Zhang
- Qing Li
- Wenqi Fan
- Dacheng Tao
affiliations:
- The Hong Kong Polytechnic University
- Nanyang Technological University
arxiv_id: '2611.02457'
url: https://arxiv.org/abs/2611.02457
pdf_url: https://arxiv.org/pdf/2611.02457
published: '2026-11-02'
collected: '2026-11-03'
category: GenRec
direction: 生成式推荐 · 推理蒸馏优化
tags:
- Knowledge Distillation
- Reasoning Augmented Rec
- LLM4Rec
- Contrastive Learning
- Multi-Teacher Distillation
one_liner: 提出多教师效用引导的推理蒸馏框架MUSE，无需标注即可蒸馏对推荐最优的推理能力
practical_value: '- 推理质量评估可直接复用RGUA方法，无需人工标注推理的通顺性/合理性，直接用真实推荐任务的ground-truth item排序提升作为评分标准，大幅降低标注成本

  - 多教师蒸馏+渐进式自探索范式可迁移到小模型推理能力训练场景，先靠多个大模型产出候选推理池，再逐步增加学生自生成推理的占比，突破单教师的知识天花板

  - 双级对比学习Loss设计可复用：不仅让学生模型学习生成优质推理，还要引导推荐编码器区分优劣推理对用户表征的影响，同时优化推理生成和利用两个环节

  - 工程上可提前离线缓存所有教师生成的推理轨迹，训练阶段无需重复调用大模型，额外计算开销极低，适合工业界落地'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有推理增强推荐的知识蒸馏方案依赖单固定教师，存在三类核心问题：不同大模型的推荐推理能力异质，单教师无法适配所有用户/场景；通用大教师缺乏推荐领域知识，学生能力被教师天花板限制；无差别蒸馏所有教师生成的推理，部分逻辑通顺的推理对推荐效果无增益甚至负向，无法真正提升排序效果。
### 方法关键点
- 构建多源推理候选池：接入多个通用大模型作为教师生成多样化推理轨迹，同时加入渐进式自探索策略，随训练轮次逐步增加学生自生成推理的采样占比，突破教师知识上限
- 提出RGUA无标注效用评估：以无推理输入时ground-truth item的全库排序为基准，计算每条推理带来的排序提升作为效用分，无需人工标注即可自动筛选高/低效用推理作为正负样本
- 设计双级对比学习目标：推理生成端拉通高/低效用推理的生成概率差，推荐编码端引导编码器给高效用推理对应的用户表征更高的目标item匹配度，同时优化推理生成和利用两个环节
### 关键结果
在亚马逊3个公开数据集（CDs、Video Games、Musical Instruments）上对比10+基线，以Qwen2.5-3B为骨干时，对比SOTA推理增强推荐方法R2ec，在CDs数据集N@5提升21.4%，H@10提升7.2%；训练开销与R2ec相当，推理延迟仅增加0.05s以内，落地代价极低。
### 核心结论
推理蒸馏的核心不是模仿教师的通顺推理，而是筛选对下游推荐任务真正有效的推理信号，哪怕是学生自生成的
