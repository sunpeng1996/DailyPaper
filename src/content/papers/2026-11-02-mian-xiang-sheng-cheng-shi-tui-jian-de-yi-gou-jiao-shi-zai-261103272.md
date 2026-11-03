---
title: Diverse-Teacher On-Policy Distillation for Generative Recommendation
title_zh: 面向生成式推荐的异构教师在策略蒸馏框架HERO
authors:
- Zhipeng Yi
- Xinyu Lin
- Minxuan Shan
- Zipeng Chen
- Yujiao Zhao
- Chuanyu Xu
- Wenjie Wang
affiliations:
- University of Science and Technology of China
- National University of Singapore
- Alibaba Group
arxiv_id: '2611.03272'
url: https://arxiv.org/abs/2611.03272
pdf_url: https://arxiv.org/pdf/2611.03272
published: '2026-11-02'
collected: '2026-11-03'
category: GenRec
direction: 生成式推荐 · 流行度去偏 蒸馏优化
tags:
- Generative Recommendation
- On-Policy Distillation
- Popularity Debias
- Semantic ID
- Knowledge Distillation
one_liner: 提出异构教师加多样性采样的在策略蒸馏框架，缓解生成式推荐流行度偏差，1688线上GMV提升3.412%
practical_value: '- 生成式推荐使用On-Policy Distillation (OPD)训练时，可直接复用异构教师设计：按item流行度划分头/尾群，分别训练专精教师，训练时按样本真实item所属群路由对应教师做蒸馏，无需修改推理逻辑，无额外推理开销。

  - 针对尾item Semantic ID (SID)路径训练覆盖不足的问题，可直接新增尾item真实SID路径的蒸馏损失，无需修改rollout逻辑即可提升尾item召回率，线上尾item
  CTR、曝光收益明确。

  - 无需单纯通过调整尾样本loss权重平衡头/尾效果（该方法易导致头群效果下降），异构教师+尾路径蒸馏的方案可同时提升头/尾推荐精度，无明显精度损失。

  - 线上部署仅保留蒸馏后的学生模型，无额外推理延迟，适配高并发的首页推荐场景，可直接接入现有生成式推荐训练流水线。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
生成式推荐通过生成Semantic ID (SID)完成召回，On-Policy Distillation (OPD)可提供更稠密的token级监督提升训练效率，但现有OPD会严重放大流行度偏差：教师天然偏好头item，学生rollout时生成的头item占比更高，尾item的SID路径几乎得不到训练，二者形成恶性循环，最终降低推荐多样性，限制业务长期增长。

### 方法关键点
- 异构教师蒸馏：将训练样本按item流行度分为头/尾两个群，分别训练两个专精教师，头教师在头样本加10%尾样本上训练，尾教师在尾样本加10%头样本上训练，训练时按样本真实item的群路由对应教师，学生匹配路由后教师的token分布做KL损失优化。
- 多样性感知item rollout：除了学生自生成的SID路径外，额外将尾item的真实SID路径加入蒸馏训练，补充尾路径的监督信号，避免学生训练路径过度集中在头item。
- 推理时仅保留学生模型，无额外开销。

### 关键实验结果
离线在1688工业数据集、Amazon Beauty、Pet、MovieLens-1M三个公开数据集上对比SFT、GKD、Ghost-AUO等10+基线，整体Hit@20最高提升2.9%，尾Hit@20最高提升108%，DTR最接近1（曝光与需求匹配度最高）；线上在1688首页「猜你喜欢」模块做15天A/B测试，相对原有生成式推荐基线GMV提升3.412%，尾item曝光+0.8%、尾点击+3.53%、尾CTR+2.71%，无推理延迟上升。

### 核心结论
生成式推荐的OPD训练中，仅靠稠密token监督提升精度的同时必然伴随流行度偏差放大，从教师分群和尾路径覆盖两个维度优化可以在不增加推理开销的前提下同时提升精度和多样性。
