---
title: 'UniEvo-VL: An On-policy Self-Distillation Training Recipe for Multimodal Model
  Self-improvement'
title_zh: UniEvo-VL：面向多模态模型自进化的同策略自蒸馏训练方案
authors:
- Fang Wu
- Da Xing
- Yanjie Huang
- Junxi Wang
- Ji Wang
- Hejia Geng
- Guancheng Wan
- Bowen Zuo
- Xiaomin Li
- Shixiang Tang
affiliations:
- Stanford University
- Johns Hopkins University
- University of Toronto
- University of Oxford
- UC Riverside
arxiv_id: '2609.38721'
url: https://arxiv.org/abs/2609.38721
pdf_url: https://arxiv.org/pdf/2609.38721
published: '2026-09-29'
collected: '2026-10-01'
category: Training
direction: 多模态模型 · 自进化训练方案
tags:
- Multimodal
- Self-Distillation
- On-Policy
- LoRA
- Self-Evolution
one_liner: 无需外部大模型教师，通过单模型分饰师生的同策略自蒸馏实现多模态生成能力迭代提升
practical_value: '- 电商商品图、营销海报生成场景可直接复用该自蒸馏框架：无需人工标注训练数据，仅通过模型自批判反馈即可迭代提升生成内容和原始需求的对齐度，比如商品属性、宣传文案的准确率

  - 生成式推荐场景可迁移该逻辑：对生成的推荐文案、商品卖点做自批判→生成修正prompt→蒸馏进生成模型，可提升原生生成的用户意图匹配度，无需推理时额外加修正步骤，降低线上延迟

  - 工程上可复用其post-revision验证过滤逻辑：仅保留修正后生成结果能通过原始需求校验的样本进入训练，可降低60%以上无效训练开销，同时避免模型学习到错误修正逻辑'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有多模态模型自进化方案要么依赖参数更大的外部教师模型，要么仅通过偏好优化、监督微调利用自生成数据，无法将生成过程中的修正反馈直接内化到原生生成策略，推理时往往需要额外的反射修正步骤才能获得符合要求的输出，训练效率和落地便利性不足。
### 方法关键点
- 单模型分饰师生角色：学生策略仅接收原始用户prompt，EMA权重的教师策略接收融合了自批判反馈的修正后prompt作为特权信息，无需额外引入外部教师模型
- 同策略自蒸馏训练：在学生自身采样的扩散去噪轨迹上逐状态对齐师生的预测分布，无需标注目标图像或标量奖励信号，训练时仅更新生成器的LoRA参数，成本极低
- 新增修正后验证环节：只有基于修正prompt生成的图像能通过原始prompt的对齐校验时，才将该样本纳入训练集，过滤无效、错误的反馈样本
### 关键实验结果
基于开源Qwen-Image-2512底座验证：原生生成能力在GenEval基准从0.747提升到0.808，GenEval2 Soft-TIFA得分从32.97提升到35.53；搭配外部强批评家GPT5.6-Luna时GenEval得分进一步提升到0.882；训练后模型推理时搭配反射修正步骤性能还能进一步提升，两者收益互补。
### 最值得记住的结论
「验证比生成更容易」的假设在多模态生成场景成立，基于自批判的同策略自蒸馏可以在无需外部标注和教师模型的前提下，持续提升模型原生生成能力。
