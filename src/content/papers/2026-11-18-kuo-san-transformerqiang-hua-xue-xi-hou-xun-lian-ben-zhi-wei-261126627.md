---
title: RL Post-Training in Diffusion Transformers Is Activation Steering
title_zh: 扩散Transformer强化学习后训练本质为激活调控
authors:
- Tuna Han Salih Meral
- Kaan Oktay
- Alec Helbling
- Atakan Kara
- Duen Horng Chau
- Pinar Yanardag
affiliations:
- Virginia Tech
- fal
- Georgia Tech
- IBM Research
arxiv_id: '2611.26627'
url: https://arxiv.org/abs/2611.26627
pdf_url: https://arxiv.org/pdf/2611.26627
published: '2026-11-18'
collected: '2026-11-21'
category: Training
direction: 大模型训练 · RL后训练机制
tags:
- RL
- Diffusion Model
- Activation Steering
- LoRA
- Post-Training
one_liner: 发现扩散Transformer RL后训练90%+收益可由参数量仅为LoRA 1/65的固定激活偏移向量实现
practical_value: '- 电商营销素材（商品图、海报文案）生成的RL对齐场景，可优先用固定激活偏移向量替代LoRA，参数量降65倍，大幅降低训练推理开销

  - 生成式推荐/Agent的RLHF对齐阶段，可先试固定激活steering方案快速验证业务收益（比如内容转化率、用户偏好匹配度），再迭代更重的微调方案

  - 扩散类生成模型的业务优化无需盲目上复杂输入依赖变换，固定偏移即可覆盖90%+的RL后训练收益，可快速落地对齐业务规则'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
扩散Transformer的RL后训练可显著提升视觉质量、文本渲染与组合精度，但此前普遍认为该收益依赖复杂输入依赖变换，底层机制未被明确。

### 方法关键点
在冻结的基础扩散Transformer块输出上加入与prompt、token、采样种子完全无关的固定激活调控向量，仅拟合RL微调后checkpoint的速度预测，目标无奖励项；SD3.5-M场景下向量参数量仅0.29M，是RL微调LoRA参数量的1/65。

### 关键结果
- 固定向量可覆盖6个图像RL模型90.0%~96.3%的奖励收益，2个视频RL模型收益恢复率分别达89.8%、111.9%
- 从零初始化在线训练该向量，在SD3.5-M的文本渲染（OCR）、人类偏好（PickScore）指标上收益超过基于权重的RL方案
