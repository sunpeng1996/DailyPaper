---
title: Latent Reasoning in Continuous Space for Unified Multimodal Models
title_zh: 面向统一多模态模型的连续空间隐式推理框架
authors:
- Byungwoo Jeon
- Yoonwoo Jeong
- Hyunseok Lee
- Minsu Cho
- Jinwoo Shin
affiliations:
- KAIST
- POSTECH
- RLWRLD
arxiv_id: '2610.42149'
url: https://arxiv.org/abs/2610.42149
pdf_url: https://arxiv.org/pdf/2610.42149
published: '2026-10-29'
collected: '2026-11-02'
category: Multimodal
direction: 统一多模态 · 连续空间隐式推理
tags:
- Unified Multimodal Model
- Latent Reasoning
- Text-to-Image
- Chain-of-Thought
- Reinforcement Learning
- SFT
one_liner: 提出连续空间隐式推理框架LARC，解决统一多模态模型推理模态不匹配问题，大幅提升文生图性能
practical_value: '- 电商商品文生图场景可复用两阶段训练策略：先用课程式SFT迁移离散CoT推理能力，再用信息增益RL无标注迭代优化，降低生成任务标注成本

  - 做多模态商品生成/商品素材文案匹配时，可借鉴连续空间推理思路，避免离散token转连续像素的模态gap，提升prompt遵循度

  - 测试时推理步长扩容策略可直接复用，在不重新训练模型的前提下，通过增加推理步数提升生成质量，适配不同算力资源的业务场景'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
统一多模态模型（UMM）无法有效复用LLM的CoT推理能力优化文生图效果，根源是离散token推理范式与连续像素生成模态存在本质不匹配，现有推理增强UMM缺失LLM具备的测试时缩放能力与细粒度可控性。
### 方法关键点
提出连续空间隐式推理框架LARC，采用两阶段训练流程：1）课程式SFT，逐步将token级推理转换为隐空间连续状态推理；2）信息增益RL，无需真值监督即可自我迭代优化隐式推理能力。
### 关键结果
各文生图基准上生成质量、prompt遵循度、组合保真度均稳定提升，GenEval基准较SOTA方案BAGEL提升7个百分点，测试时推理步数扩容效果显著优于token式生成方案。
