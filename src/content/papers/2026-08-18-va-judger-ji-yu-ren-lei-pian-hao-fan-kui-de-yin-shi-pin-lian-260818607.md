---
title: 'VA-Judger: Reward Modeling from Human Preference Feedback for Joint Video-Audio
  Generation'
title_zh: VA-Judger：基于人类偏好反馈的音视频联合生成奖励建模
authors:
- Yinming Huang
- Shuyuan Tu
- Xi Yan
- Zihan Yang
- Jianhua Han
- Xu Hang
- Yu-Gang Jiang
- Zuxuan Wu
affiliations:
- Fudan University
- Shanghai Innovation Institution
- Yinwang Intelligent Technology Co., Ltd
arxiv_id: '2608.18607'
url: https://arxiv.org/abs/2608.18607
pdf_url: https://arxiv.org/pdf/2608.18607
published: '2026-08-18'
collected: '2026-08-21'
category: Multimodal
direction: 多模态生成 · 人类偏好对齐奖励建模
tags:
- Reward Modeling
- Human Preference Alignment
- Multimodal Generation
- RLHF
- Chain-of-Thought
one_liner: 构建音视频人类偏好数据集与评测基准，提出分维度思维链奖励模型，提升生成质量与人类偏好对齐度
practical_value: '- 分维度拆解人类偏好做奖励建模的思路可迁移到生成式推荐、广告文案/多模态素材生成的RLHF流程，解决单一偏好标签信号稀疏问题

  - 先易后难的奖励模型训练范式（先学差距大的样本、再蒸馏难样本偏好解释）可复用在各类对齐人类偏好的奖励模型训练中

  - 构建域内+跨域偏好评测基准的方法，可用于验证生成类任务奖励模型的泛化性，避免过拟合离线指标'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有音视频联合生成的奖励信号拆分单维度指标计算，无法捕捉prompt、视频、音频间的整体语义与时序一致性，易触发奖励黑客，生成内容对齐人类偏好程度低。
### 方法关键点
1. 构建VAPref-10K大规模人类偏好数据集，包含9K条prompt、10.3K细粒度成对对比标注；同步推出VA-Judger-Bench基准，覆盖域内/跨域评测场景。
2. 提出思维链全模态奖励模型VA-Judger，三阶段训练：先学习质量差距大的样本对建立结构化输出与粗粒度判别能力，再通过拒识采样蒸馏难样本的偏好解释，最后将人类反馈拆解为多维度信号做强化学习，获得比二元标签更稠密的奖励。
### 关键结果
域内/跨域评测中人类偏好预测准确率优于所有指标基线，用其输出奖励微调音视频生成模型，生成质量获显著提升
