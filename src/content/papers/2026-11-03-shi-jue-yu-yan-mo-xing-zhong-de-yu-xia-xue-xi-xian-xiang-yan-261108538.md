---
title: Subliminal Learning in Vision-Language Models
title_zh: 视觉语言模型中的阈下学习现象研究
authors:
- Arman Hatami
- Romina Aalishah
- Ilya E. Monosov
affiliations:
- Johns Hopkins University
arxiv_id: '2611.08538'
url: https://arxiv.org/abs/2611.08538
pdf_url: https://arxiv.org/pdf/2611.08538
published: '2026-11-03'
collected: '2026-11-14'
category: Training
direction: 多模态大模型 · 训练特性研究
tags:
- VLM
- Subliminal Learning
- Knowledge Distillation
- Synthetic Data
- Model Bias
one_liner: 验证视觉语言模型存在阈下学习效应，无关任务训练数据可隐式传递偏好与表达习惯
practical_value: '- 做VLM蒸馏/合成数据训练时，需排查教师模型隐藏偏好，避免无关任务数据引入业务侧隐性偏见，比如商品图分类、多模态召回、推荐理由生成的偏好偏移

  - 多模态生成式推荐场景下，可利用阈下学习特性，通过少量无关任务的定制化训练数据，隐式注入目标品牌/品类偏好，降低显性prompt engineering与全量微调成本

  - 做VLM可解释性优化时，可参考该研究的偏好传递路径，对齐师生模型的解释话术风格，提升电商推荐理由、智能客服答复的一致性与用户信任度'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
当前VLM训练广泛依赖模型生成的合成数据与知识蒸馏数据，LLM中已被证实的阈下学习（隐藏偏好通过无关任务数据隐式传递）效应是否存在于VLM中尚不明确，直接影响多模态模型训练的可控性。
### 方法关键点
1. 微调同基座教师VLM注入特定动物/人脸属性偏好，设置无偏好对照教师；
2. 两类教师在完全无关的几何形状计数视觉任务上生成标注，用相同图像分别训练两个同基座学生VLM；
3. 覆盖2B-7B参数规模的多类VLM开展对照实验。
### 关键结果数字
- 偏好传递效应稳定存在，动物偏好任务中偏置组学生选择目标的概率比对照组最高高10个百分点；
- 训练数据量越大，偏好传递效果越强，强度随偏好类型、模型规模、标注生成方式存在差异；
- 即便输出决策完全一致，偏置组学生的解释话术与偏置教师的重合度显著高于对照组。
