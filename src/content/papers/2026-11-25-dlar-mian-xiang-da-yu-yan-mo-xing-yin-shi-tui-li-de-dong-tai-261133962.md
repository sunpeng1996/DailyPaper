---
title: 'DLaR: Dynamic Stochasticity Control for Latent Reasoning in Large Language
  Models'
title_zh: DLaR：面向大语言模型隐式推理的动态随机性控制框架
authors:
- Xiaocheng Luo
- Peng Xu
- Zaifu Zhan
- Xiangyu Duan
affiliations:
- Soochow University
- University of Minnesota
arxiv_id: '2611.33962'
url: https://arxiv.org/abs/2611.33962
pdf_url: https://arxiv.org/pdf/2611.33962
published: '2026-11-25'
collected: '2026-11-26'
category: Reasoning
direction: 大模型隐式推理动态优化
tags:
- Latent Reasoning
- Stochasticity Control
- GRPO
- Mathematical Reasoning
- LLM
one_liner: 双粒度动态调节隐式推理扰动强度，提升大模型多场景推理性能
practical_value: '- 做Agent多步推理（如电商导购路径规划、复杂query理解多步拆解）时，可复用ASM的置信度-熵融合信号动态调整采样随机性，避免固定温度导致的语义漂移或探索不足。

  - RL训练LLM用于推荐/广告生成类任务（如个性化文案生成、query推荐）时，可复用TAST的课程式随机性衰减策略，前期广探索、后期收敛，效果优于固定噪声方案。

  - 隐式推理技术可直接迁移至多步推理类Agent业务：无需暴露中间推理token，仅增加置信度、熵计算逻辑，无额外前向传播，推理延迟几乎无提升。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有隐式推理方法通过注入随机性提升探索能力，但存在两个核心缺陷：所有推理步统一使用相同扰动强度，高置信度步骤易被噪声干扰、低置信度步骤探索不足；无约束扰动易引发语义漂移，破坏推理连贯性，大幅降低复杂多步推理任务的准确率。
### 方法关键点
- 基于GRPO强化学习框架设计双粒度动态扰动调节机制：token级ASM模块通过置信度（预测分布最大概率）与归一化熵加权融合得到调制信号，动态调整每步扰动强度，模型不确定时提升探索、高置信时保障稳定性；
- 训练级TAST模块支持线性、余弦、阶梯三种课程式衰减调度策略，训练前期基扰动强度较高侧重广探索，训练后期逐步降低基强度侧重收敛；
- 最终扰动强度为TAST输出的基强度乘以ASM调制系数，通过上下限裁剪避免极端值，全程复用已有logit计算结果，无额外前向传播开销。
### 关键结果
在4个分布内数学推理基准（GSM8K、MATH500等）、3个分布外推理基准（ARC-C、MMLU-STEM等）上对比GRPO、LEPO等7种基线方案：Llama-3.2-1B上平均Pass@1/ Pass@8达27.9%/50.6%，Qwen2.5-1.5B上达46.8%/68.2%，均为当前最优；训练仅增加8.9%耗时、7%显存开销，推理无额外延迟。
### 核心结论
隐式推理的随机性调节不能采用统一固定策略，基于推理状态的动态适配+训练阶段的课程式衰减，是兼顾探索能力与推理连贯性的核心。
