---
title: Do We Really Need Multimodal Emotion Language Models Larger Than 1B Parameters?
title_zh: 我们真的需要参数超1B的多模态情感语言模型吗？
authors:
- Kaiwen Zheng
- Junchen Fu
- Wenhao Deng
- Hu Han
- Joemon M. Jose
- Xuri Ge
arxiv_id: '2607.12787'
url: https://arxiv.org/abs/2607.12787
pdf_url: https://arxiv.org/pdf/2607.12787
published: '2026-07-14'
collected: '2026-07-15'
category: Training
direction: 多模态大模型 · 轻量化训练
tags:
- Multimodal-LLM
- Knowledge-Distillation
- Model-Compression
- MER
- Efficient-Inference
one_liner: 提出1B参数内轻量多模态情感识别框架Light-MER，性能达SOTA且推理效率大幅提升
practical_value: '- 电商直播/短视频带货的多模态内容情感分析场景，可直接复用该蒸馏框架，将7B级大模型蒸馏到1B以内，支持端侧/边缘设备部署，大幅降低推理成本

  - 模型蒸馏任务可直接复用两个优化trick：结合Sliced Wasserstein Distance的最优传输损失做隐层对齐，以及GRPO多奖励优化平衡效果与效率，提升小模型知识吸收效率

  - 资源受限的实时情感分析场景（如直播实时舆情监控、对话Agent情绪响应）无需盲目堆叠大参数，可优先尝试1B内小模型+蒸馏的方案'
score: 8
source: arxiv-cs.CL
depth: abstract
---

**动机**
当前多模态大模型（MLLM）做多模态情感识别（MER）普遍需要7B以上参数，计算成本高、推理效率低，无法部署在机器人、移动设备等资源受限平台，行业普遍疑惑是否必须用1B以上大模型才能实现高质量MER。

**方法关键点**
提出轻量MER框架Light-MER，通过知识蒸馏将大参数教师模型的多模态情感推理能力迁移到1B以内的学生模型；新增两个优化策略：一是结合Sliced Wasserstein Distance与隐层对齐的最优传输损失，二是基于GRPO的多奖励优化策略平衡MER效果与效率，强化学生模型知识吸收能力。

**关键结果**
在9个公开基准数据集上达到SOTA性能，参数规模控制在1B以内，推理效率较7B级大模型大幅提升。
