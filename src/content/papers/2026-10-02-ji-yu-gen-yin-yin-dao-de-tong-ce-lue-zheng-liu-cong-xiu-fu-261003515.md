---
title: 'Learning from Repaired Reasoning: Root-Cause-Guided On-Policy Distillation'
title_zh: 基于根因引导的同策略蒸馏：从修复后的推理中学习
authors:
- Chenglei Shen
- Haoyang Yao
- Weijie Yu
- Song Jin
- Xiao Zhang
- Jun Xu
affiliations:
- Renmin University of China
- Peking University
- University of International Business and Economics
arxiv_id: '2610.03515'
url: https://arxiv.org/abs/2610.03515
pdf_url: https://arxiv.org/pdf/2610.03515
published: '2026-10-02'
collected: '2026-10-05'
category: Training
direction: 大模型推理 · 同策略蒸馏优化
tags:
- On-Policy Distillation
- Knowledge Distillation
- Reasoning Optimization
- LLM Training
- Root Cause Analysis
one_liner: 提出根因引导的同策略蒸馏RC-OPD，解决推理不匹配与蒸馏陷阱问题，提升大模型推理性能
practical_value: '- 做LLM驱动的电商推荐Agent推理优化时，可复用RC-OPD的错误诊断-修复-验证范式，针对用户意图理解、召回排序逻辑等推理错误做局部修正，避免直接用参考方案蒸馏导致的「抄答案不会推理」问题

  - 大模型微调蒸馏时可采用差异化监督策略：对错误片段加根因错误提示做强监督，对正确前缀加锚点COT做弱监督，同时设置2轮修复阈值平衡训练效果和成本，比全轨迹KL蒸馏效果更优

  - 生成式推荐的训练中，可引入迭代反事实验证环节：对模型生成的错误推荐路径做局部修复后让模型继续生成，验证修复有效性后再加入训练集，减少无效监督信号'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有同策略自蒸馏（OPSD）依赖参考方案做全轨迹监督，存在两个核心痛点：一是**推理不匹配**，参考方案未针对学生的具体推理错误给出修正路径，导致模型直接照搬正确结论但底层推理逻辑缺失，答题准确率虚高；二是**蒸馏陷阱**，全轨迹统一施加的参考约束会干扰已经正确的推理步骤，挤占错误修正的有效监督信号，最终模型泛化能力不足。
### 方法关键点
- 诊断模块：定位学生推理轨迹中最早的实质性错误阶段，输出三类指导信号：修复后的锚点阶段（承接正确前缀的修正步骤）、错误原因与修正目标、锚点推导COT
- 迭代反事实验证：保留正确前缀+修复后的锚点，让学生继续生成后续推理，最多2轮迭代，若最终答案正确则用该修复链做监督，否则 fallback 到原参考蒸馏
- 差异化蒸馏：对错误阶段用错误原因与目标做教师条件监督，对正确前缀用锚点COT做弱监督，错误段权重设为1，正确前缀权重设为0.1，平衡错误修正与已有推理保留，训练采用rank-64 LoRA适配
### 关键实验
基于Qwen3-1.7B/4B/8B模型，在OpenThoughts-Math-30K数据集训练，在AIME2024/2025、HMMT2025三个推理基准测试，对比OPSD、ROSD、DASH等7种蒸馏基线，RC-OPD相对OPSD在三个模型上分别取得9.66%、5.78%、5.70%的平均准确率提升，正确前缀分布相对基线偏移降低44.7%。
### 核心结论
同策略蒸馏的核心不是让学生拟合参考答案，而是针对性修正学生自有推理路径上的错误，同时保留已经正确的推理逻辑，才能真正提升泛化推理能力。
