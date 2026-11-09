---
title: 'Exploring Weight-Space Programming: Capabilities, Generalization, and Limitations'
title_zh: 权重空间编程（WSP）的能力、泛化性与局限性探究
authors:
- Junru Hu
- Cheng Tang
- Wei Li
- Hongze Zhu
- Chun-Mei Feng
- Qi Zhang
- Yirong Chen
- Ming Hu
affiliations:
- Shanghai Artificial Intelligence Laboratory
- Tongji University
- Fudan University
arxiv_id: '2611.09382'
url: https://arxiv.org/abs/2611.09382
pdf_url: https://arxiv.org/pdf/2611.09382
published: '2026-11-05'
collected: '2026-11-09'
category: LLM
direction: 大模型适配 · 权重空间编程
tags:
- Weight-Space-Programming
- Model-Editing
- LLM-Adaptation
- Gradient-Free
- Parameter-Efficiency
one_liner: 系统评估权重空间编程（WSP）的适配效果、跨任务迁移规律与实际应用限制
practical_value: '- 垂域小参数LLM（如电商客服、推荐理由生成模型）可优先尝试WSP做定向适配，仅修改千级参数即可实现任务效果大幅提升，存储 overhead
  远低于LoRA

  - 跨多下游任务的模型适配可复用WSP编辑后的checkpoint，如数学推理编辑后的模型可直接提升指令遵循、科学QA效果，降低重复适配成本

  - 业务落地优先选择小参数模型做WSP编辑，大模型baseline准确率高，提升空间有限，且干预效果不稳定，投入产出比远低于小模型

  - WSP编辑不要以修改参数量为核心指标，优先针对Transformer的特定组件（单个MLP列、Attention头）做定向修改，效果远优于盲目做大范围秩一更新'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
传统大模型适配依赖梯度驱动的微调（如LoRA），需大量任务标注数据，Weight-Space Programming（WSP）允许推理Agent直接无梯度修改模型参数实现适配，但其能力边界、跨任务泛化规律、落地限制尚未被系统验证，无法指导工业场景落地。
### 方法关键点
- 以GPT-6 Astra为编辑Agent，针对Qwen3.5-0.8B、Qwen3.5-9B两个尺度模型做权重干预，支持稀疏MLP列修改、秩一更新、注意力头重缩放三类操作，全程无梯度参与
- 编辑流程仅分配50次前向工具请求预算，Agent基于开发集反馈选择最优checkpoint，最终效果在完全未见过的held-out测试集上评估
- 覆盖7类基准测试：数学推理（MATH-500）、通用知识（MMLU-Pro）、指令遵循（IFEval）、科学QA（GPQA Diamond）、医疗QA、科学推理、科学编码
### 关键结果
- 0.8B小模型上WSP效果突出：仅修改1023个参数，MATH-500准确率提升29.45pp，IFEval提升36.72pp，SciBench提升17.11pp
- 跨任务泛化性可观：数学编辑后的checkpoint无需额外修改，GPQA提升3.03pp，IFEval提升12.18pp，SciBench提升20.10pp
- 局限性显著：16条编辑轨迹中6条最终保留原权重，9B大模型效果提升普遍小于1pp，修改参数量与效果无正相关，不同编辑轨迹结果差异极大

WSP对小参数模型的极稀疏定向适配性价比远高于大模型，其效果核心取决于干预结构而非修改参数量
