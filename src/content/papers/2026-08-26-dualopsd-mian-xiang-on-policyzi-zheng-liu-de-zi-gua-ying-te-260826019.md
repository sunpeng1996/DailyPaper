---
title: 'DualOPSD: Adaptive Privileged Teachers for On-Policy Self-Distillation'
title_zh: DualOPSD：面向On-Policy自蒸馏的自适应特权教师框架
authors:
- Yutong Chen
- Guangfu Guo
- Zhichao Xu
- Kunpeng Liu
affiliations:
- Clemson University
- University of Utah
arxiv_id: '2608.26019'
url: https://arxiv.org/abs/2608.26019
pdf_url: https://arxiv.org/pdf/2608.26019
published: '2026-08-26'
collected: '2026-08-27'
category: Training
direction: LLM训练 · 自蒸馏优化
tags:
- Knowledge Distillation
- On-Policy Training
- LoRA
- LLM Reasoning
- Self-Distillation
one_liner: 提出不对称交替更新的双策略On-Policy自蒸馏框架，显著提升中大规模LLM推理性能
practical_value: '- 做垂域LLM微调（如Agent推理、生成式推荐文案生成）时，可复用不对称交替蒸馏架构：学生用带clip的正向KL保证训练稳定，特权教师用反向KL适配学生分布，无需额外采样rollout，训练成本仅增加40%左右

  - 特权上下文设计可复用：训练推荐文案生成模型时，给特权教师输入已验证的高转化文案作为参考，学生仅输入商品属性，既能获得密集监督又能保证推理时仅依赖商品特征

  - 明确规模依赖结论：小于2B的小模型不要使用该方法会掉点，4B及以上规模模型收益显著，可直接应用于中大规模垂类LLM微调

  - 工程实现可复用：学生和教师用两套独立LoRA适配器挂载同一基座模型，无需维护两份全量参数，显存开销增加可控，适合业务落地'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有On-Policy自蒸馏（OPSD）将特权教师固定，训练过程中随着学生分布、输出风格变化，教师提供的监督信号与学生适配性越来越差，clip操作只能拒绝不兼容的风格信号，无法从根源解决监督错位问题，还会浪费训练算力。

### 方法关键点
- 采用不对称交替更新闭环：先基于学生采样的on-policy轨迹，用带点态clip的正向$D_{KL}(p_T||p_S)$更新学生，保证训练稳定不被风格信号干扰
- 复用同一条学生轨迹，用停止梯度的更新后学生分布，以全量反向$D_{KL}(p_S||p_T)$更新特权教师，让教师适配学生的输出分布，后续监督信号更贴合学生当前状态
- 工程上学生和教师用两套独立LoRA适配器挂载同一基座，仅需额外增加一次教师的前向/反向传播，无需额外采样rollout

### 关键实验
在OpenThoughts数学数据集上训练Qwen3-1.7B/4B/8B模型，对比SFT、GRPO、OPSD等基线：
- Qwen3-8B上，DualOPSD相比OPSD在AIME2024、AIME2025、HMMT2025三个benchmark上avg@12分别提升23.61、13.89、10.00个百分点
- 4B规模同样取得显著收益，1.7B小模型上效果反而下降，呈现明确的规模依赖效应
- 全规模下截断率平均降低60%以上，训练成本仅比OPSD高30%-40%

### 核心结论
On-Policy自蒸馏的特权教师无需固定为静态Oracle，自适应学生分布的动态教师可以在不显著增加训练成本的前提下大幅提升中大规模模型的下游性能。
