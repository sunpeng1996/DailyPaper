---
title: 'RULER: Instance-aware Rubric Rewards for SVG Generation'
title_zh: RULER：面向SVG生成的实例感知评分规则奖励机制
authors:
- Hangyu Ran
- Yuhao Zheng
- Yingying Zhang
- Kevin Qinghong Lin
- Han Peng
affiliations:
- Ant Group
- The Hong Kong University of Science and Technology (Guangzhou)
- Independent Researcher
- University of Oxford
arxiv_id: '2609.25270'
url: https://arxiv.org/abs/2609.25270
pdf_url: https://arxiv.org/pdf/2609.25270
published: '2026-09-20'
collected: '2026-09-23'
category: Training
direction: 生成任务训练优化 · 多维度奖励设计
tags:
- Reward Modeling
- Reinforcement Learning
- VLM
- Text-to-SVG
- RL Optimization
one_liner: 提出基于实例感知多维度评分规则的RL奖励框架，无需标注即可优化文本到SVG生成效果
practical_value: '- 电商营销矢量素材（图标、商品插画、活动装饰元素）生成场景，可复用多维度评分规则思路替代单一CLIP/美学指标，减少奖励黑客问题，提升生成内容和需求的匹配度

  - 生成类任务RL优化阶段，可借鉴实例感知评分逻辑，无需配对标注/人类偏好数据即可生成细粒度奖励信号，大幅降低标注成本

  - 开放域生成任务的离线评估环节，可引入VLM分维度打分机制，和人工判断的相关性远高于scalar指标，提升评估结果置信度'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
文本生成SVG为无绝对视觉真值的开放任务，现有CLIP、美学等适配自然图像的标量指标迁移到矢量内容效果差，作为RL奖励易触发奖励黑客，缺乏可靠的评估与策略优化信号。
### 方法关键点
1. 验证带多维度评分规则的VLM裁判与人工判断的相关性远高于标量指标；
2. 提出RULER框架，将每条指令转换为覆盖语义、视觉、风格3大维度的6项实例感知评分规则；
3. 用VLM对生成结果逐维度打分，加权得到细粒度奖励，通过Group Relative Policy Optimization优化策略，无需配对SVG真值或人类偏好标注。
### 关键结果
在MMSVG-Illustration、MMSVG-Icon数据集上，评分分别从0.432/0.395提升至0.693/0.683，效果超过专用SVG生成模型，追平参数量大得多的DeepSeek-V3，消融实验证明评分规则设计是核心优化杠杆。
