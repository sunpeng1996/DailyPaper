---
title: On-Policy Distillation with Negative-Policy Rollouts
title_zh: 基于负策略生成轨迹的同策略蒸馏优化方法
authors:
- Jaehui Hwang
- Dongyoon Han
- Sangdoo Yun
- Byeongho Heo
affiliations:
- NAVER AI Lab
arxiv_id: '2610.07874'
url: https://arxiv.org/abs/2610.07874
pdf_url: https://arxiv.org/pdf/2610.07874
published: '2026-10-05'
collected: '2026-10-08'
category: Training
direction: 大模型后训练 · 同策略蒸馏优化
tags:
- On-Policy Distillation
- Knowledge Distillation
- LLM Post-training
- Negative Sampling
- Policy Optimization
one_liner: 在同策略蒸馏的轨迹生成阶段引入低性能负策略输出，补充负向学习信号，无需修改损失即可提升蒸馏效果
practical_value: '- 做LLM4Rec/Agent模型蒸馏时可直接复用该框架：无需修改现有蒸馏损失，仅额外混入同模型族小参数低性能版本的生成轨迹作为负例，即可提升蒸馏效果，改造成本极低

  - 负策略生成的轨迹可预生成后全训练流程复用，大幅降低蒸馏过程中的实时轨迹生成开销，适合工业界大模型蒸馏的降本需求

  - 电商/广告场景的生成式推荐模型蒸馏，可直接将历史低质量的召回/排序结果作为负策略轨迹混入训练，强化模型对低质量结果的抑制'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有On-Policy Distillation（OPD，同策略蒸馏）仅依赖强教师模型的正向引导，当师生分布重叠度较低时，学习信号不足，难以有效抑制学生模型的低质量输出，限制了蒸馏效果的上限。
### 方法关键点
- 无需修改原有OPD的蒸馏损失函数，仅在轨迹生成阶段混合学生自身生成轨迹和低性能负策略（同模型族更小参数、推理表现更差的版本）的生成轨迹，混合比例由超参数α控制
- 负策略生成的token在OPD损失下的平均收益为负，训练过程中会被自动抑制，实现让学生远离负策略分布的效果，同时完全保留原有正向蒸馏信号的作用
- 负策略生成的轨迹可预生成后在全训练流程复用，无需随学生模型迭代重新生成，大幅降低训练阶段的计算开销
### 关键实验
在数学、科学、代码三大领域共13个推理基准上测试，覆盖Qwen3、Gemma两个模型族，1.7B/4B/8B等不同参数规模的学生模型，同时兼容标准OPD、ExOPD、OPD2等多种现有OPD变体：
- 非思考模式下，Qwen3-1.7B学生模型的数学平均准确率从OPD的48.3提升至56.3，Code平均从27.2提升至31.1，Science平均从37.2提升至41.5
- Qwen3-4B学生模型的数学平均准确率从62.2提升至70.5，Code平均从40.2提升至51.1
- 全量复用预生成负策略轨迹的情况下，Qwen3-1.7B的蒸馏训练时间从9h19m降至3h34m，训练效率提升超60%
### 核心结论
同策略蒸馏的优化无需局限于损失函数修改，通过调整轨迹分布引入低成本负向信号，可实现效果和效率的双重提升
