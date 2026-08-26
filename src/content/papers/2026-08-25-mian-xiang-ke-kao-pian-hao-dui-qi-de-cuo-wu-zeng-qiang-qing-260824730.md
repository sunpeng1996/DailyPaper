---
title: 'Learning to Prefer Reliably: Error-Augmented Emotion Preference Optimization
  with Calibrated Fusion'
title_zh: 面向可靠偏好对齐的错误增强情感偏好优化与校准融合框架
authors:
- Zilong Huang
- Junyi Peng
- Junjie Li
- Kai Li
- Wenze Ren
- Kong Aik Lee
- Man-Wai Mak
- Tatsuya Kawahara
affiliations:
- 香港理工大学
- 布尔诺理工大学
- 清华大学
- 台湾大学
- 京都大学
arxiv_id: '2608.24730'
url: https://arxiv.org/abs/2608.24730
pdf_url: https://arxiv.org/pdf/2608.24730
published: '2026-08-25'
collected: '2026-08-26'
category: Training
direction: 多模态大模型 · 偏好优化训练
tags:
- Preference Learning
- DPO
- LoRA
- Multimodal LLM
- Model Fusion
one_liner: 提出错误增强偏好优化EAPO框架，从数据和模型层面提升MLLM情感偏好判断可靠性
practical_value: '- 做LLM对齐/偏好训练时，可复用错误增强负样本构造方法：针对业务场景预设核心错误类型（如推荐文案的情绪反转、信息造假、证据遗漏等），通过局部编辑+校验生成可控负样本，提升模型鲁棒性

  - 多模型集成打分时，可复用margin校准融合方法：先将不同模型的偏好得分标准化到同一尺度再加权融合，比硬投票/直接平均效果更优，适合广告/推荐多打分器融合场景

  - 偏好训练流水线可复用LoRA SFT→DPO两阶段适配方案，搭配样本顺序翻转消除位置bias，低计算成本即可提升模型偏好匹配精度'
score: 8
source: arxiv-cs.MM
depth: full_pdf
---

### 动机
当前情感偏好学习依赖稀疏的人工成对标注，仅为每个正样本匹配单个天然负样本，对情绪反转、强度错配、证据矛盾、模态遗漏等多样错误模式覆盖不足，易导致MLLM偏好判断对语义通顺但情感不符的样本鲁棒性差；同时单模型判断受自身固有偏差影响，在细粒度、模糊情感场景下可靠性不足。
### 方法关键点
- 数据层：构造错误增强数据集，在原生负样本之外，基于偏好正样本通过局部定点编辑生成4类可控错误负样本，经过规则校验+语义验证后入库，同时随机翻转正负样本顺序消除位置bias
- 训练层：采用LoRA SFT→DPO两阶段独立适配多个MLLM偏好judge，低计算成本下让模型学习区分不同错误类型的样本
- 融合层：提出margin校准软融合方法，先将不同judge输出的偏好margin标准化到同一尺度，再等权融合得到最终偏好结果，保留偏好强度信息，避免硬投票的信息损失
### 关键实验
在MER2026-EmoPrefer挑战赛数据集上验证，对比官方基线、零样本MLLM、单模型训练方案，EAPO在官方两阶段测试集的Macro WAF达80.23%，比最优单judge提升0.83个百分点，比硬投票方案提升1.76个百分点；同时在4类受控错误样本集上平均WAF达85.35%，样本顺序交换一致性达76.38%，鲁棒性显著优于原生训练方案。
### 核心结论
仅在原生分布上做偏好训练可能提升分布内精度，但会降低对合理错误样本的鲁棒性，错误增强数据+多judge校准融合是兼顾精度和鲁棒性的有效路径
