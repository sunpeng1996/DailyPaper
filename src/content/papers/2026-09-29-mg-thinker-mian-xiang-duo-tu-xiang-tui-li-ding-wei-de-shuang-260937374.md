---
title: 'MG-Thinker: Bi-Axial Self-Reflection for Multi-Image Reasoning Grounding'
title_zh: MG-Thinker：面向多图像推理定位的双轴自反思框架
authors:
- Heyu Huang
- Chi Chen
- Zonghao Guo
- Yuhua Li
- Maosong Sun
- Ruixuan Li
affiliations:
- Huazhong University of Science and Technology
- Tsinghua University
arxiv_id: '2609.37374'
url: https://arxiv.org/abs/2609.37374
pdf_url: https://arxiv.org/pdf/2609.37374
published: '2026-09-29'
collected: '2026-10-04'
category: Multimodal
direction: 多模态大模型 · 多图像推理定位
tags:
- MLLM
- Reinforcement Learning
- Chain-of-Thought
- Multimodal Reasoning
- Grounding
one_liner: 设计双轴优势分解RL的多图像推理定位框架，配套25K任务自适应CoT标注数据集，性能达SOTA
practical_value: '- 双轴优势分解的RL优化思路可复用在多模态搜推的样本难度异构场景，比如多商品图理解、跨模态召回的后训练调优

  - 任务自适应CoT标注方法可迁移至多模态Item理解的标注流程，降低细粒度视觉定位类任务的标注成本

  - 粗到细的分层推理范式可用于电商多图商品属性识别、像素级商品定位业务（如以图搜商品的精准匹配）'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
现有RL驱动的多图像推理定位（MRG）方法忽略两个核心特性：从粗到细的分层推理模式、任务-样本难度异构分布，难以实现跨多图上下文的像素级精准定位。
### 方法关键点
1. MG-Thinker后训练RL框架，配套25K规模、带任务自适应CoT标注的MRG数据集，支撑分层推理范式，引导模型输出结论前先收集多视角证据；
2. 配套BiA-DAPO算法，沿组内信号轴、组间能力轴分解rollout优势，基于预定义候选池实现稳定的组级统计，解决样本难度异构问题。
### 关键结果
在多图像推理定位任务上达到SOTA性能，在多图像理解、各类多模态基准测试上的泛化能力均获得一致提升。
