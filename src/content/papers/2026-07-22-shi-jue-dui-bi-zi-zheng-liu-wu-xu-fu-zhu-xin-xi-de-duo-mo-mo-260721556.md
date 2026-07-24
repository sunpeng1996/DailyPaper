---
title: Visual Contrastive Self-Distillation
title_zh: 视觉对比自蒸馏：无需辅助信息的多模态模型自训练方法
authors:
- Yijun Liang
- Yunjie Tian
- Yijiang Li
- Yuqi Jia
- Furong Huang
- Tianyi Zhou
- Di Fu
affiliations:
- University of Maryland, College Park
- University of California, San Diego
- Duke University
- MBZUAI
arxiv_id: '2607.21556'
url: https://arxiv.org/abs/2607.21556
pdf_url: https://arxiv.org/pdf/2607.21556
published: '2026-07-22'
collected: '2026-07-24'
category: Training
direction: 多模态大模型 · 无监督自蒸馏
tags:
- Self-Distillation
- VLM
- On-Policy Training
- Contrastive Learning
- Multi-modal
one_liner: 通过对比原图与内容擦除控制图的EMA教师预测，实现无辅助信息的多模态模型高效自蒸馏
practical_value: '- 电商多模态商品理解场景可复用VCSD自蒸馏思路，无需标注特权答案、视觉证据，仅用商品原图+黑/高斯噪声图做对比即可提升VLM细粒度识别、计数准确率，大幅降低标注成本

  - 自蒸馏训练可直接复用「plausibility support阈值过滤+对比加权调整分布+正向KL蒸馏」的组合trick，有效避免训练漂移，稳定提升模型性能，适配商品属性识别、图文匹配等下游任务

  - 轻量多模态Agent/搜推场景的小模型蒸馏可直接采用VCSD架构，无需依赖外部大教师模型，仅靠EMA教师即可完成自训练，降低训练与推理部署成本'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有On-policy自蒸馏（OPSD）需构造师生信息不对称才能生成有效训练信号，普遍依赖特权答案、视觉证据等辅助标注或额外处理管道，标注成本高、任务适配性差；如何仅通过输入条件构造不对称性，实现无辅助信息的高效自蒸馏是多模态模型训练的核心痛点。
### 方法关键点
- 构造内容擦除的控制图（如全黑图、噪声图），让EMA教师分别预测原图与控制图下的下一词分布，计算token级对数概率差Δt(v)，度量token对实例视觉内容的依赖度
- 仅对原图预测下概率高于阈值β的候选token，用Δt(v)加权调整得到蒸馏目标分布，限制修正范围避免训练漂移
- 用正向KL将目标分布蒸馏到学生模型，EMA教师随学生迭代更新，推理时仅保留学生无额外开销
### 关键结果
在ViRL39K数据集上训练Qwen3-VL、Qwen3.5两个系列2B~9B参数模型，对比Base基线、带答案提示的OPSD基线：Qwen3-VL系列7个视觉语言基准平均准确率分别提升4.77%（2B）、1.86%（4B）、3.75%（8B），Qwen3.5系列提升2.83%~4.27%，全面优于两类基线。
**最值得记住的一句话**：模型自身在输入扰动下的预测差异本身就是高质量自监督信号，无需额外标注即可实现性能稳定提升
