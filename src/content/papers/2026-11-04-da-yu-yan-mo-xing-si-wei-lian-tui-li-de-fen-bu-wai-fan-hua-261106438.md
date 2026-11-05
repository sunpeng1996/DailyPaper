---
title: Understanding the Out-of-Distribution Generalization of Chain-of-Thought Reasoning
  in LLMs
title_zh: 大语言模型思维链推理的分布外泛化机制研究
authors:
- Nuo-Jing Liang
- Xiao-Tong Yuan
- Pan Zhou
affiliations:
- Nanjing University
- Singapore Management University
arxiv_id: '2611.06438'
url: https://arxiv.org/abs/2611.06438
pdf_url: https://arxiv.org/pdf/2611.06438
published: '2026-11-04'
collected: '2026-11-05'
category: Reasoning
direction: 思维链推理 · 分布外泛化理论分析
tags:
- Chain-of-Thought
- OOD-Generalization
- Generalization-Bound
- LLM-Reasoning
- Rademacher-Complexity
one_liner: 从理论和实验层面揭示CoT复用单步预测器实现组合分布外泛化的机制并给出泛化边界
practical_value: '- 做Agent多步推理（如电商导购、订单全链路规划）时，可优先标注训练单原子步骤能力，无需标注完整长推理轨迹，大幅降低标注成本

  - CoT中间输出必须显式记录完整当前状态（剩余任务、上下文信息等），可直接应用于RAG问答、商品属性推导、多轮推荐理由生成等场景提升准确率

  - 多步推理任务错误率随深度T呈√T级增长而非线性，当推理步长过大时可拆分为多个子链独立执行，控制整体推理误差'
score: 8
source: arxiv-stat.ML
depth: full_pdf
---

### 动机
CoT显著提升LLM数学、逻辑推理能力，但可泛化到训练未见过的复杂多步OOD任务的内在机制缺乏系统理论支撑，现有分析多局限于窄场景或两阶推理，未给出适配自回归Next-Token Prediction（NTP）范式的显式泛化边界。
### 方法关键点
- 将CoT的OOD泛化建模为组合泛化问题：训练仅提供分布内（ID）单步转换数据，目标任务无完整推理轨迹或直接输入输出配对数据
- 理论证明CoT通过复用共享单步预测器组合可复用的ID转换实现泛化，OOD任务风险由ID子任务风险之和乘以与推理深度T无关的O(k)系数控制（k为单步输出token数）
- 基于Rademacher复杂度分析得到泛化误差项为O(√T/n)（n为单步训练样本数），而非线性依赖T，同时适配NTP训练场景给出包含模型参数、维度等的显式边界
### 关键实验
- 自研Atom-Task符号组合基准，对比CoT与无CoT设置：仅单步数据训练的CoT模型9步任务准确率22.27%，无CoT仅0.67%；用3步数据训练的CoT模型9步准确率达79.27%
- 状态跟踪 ablation：去掉CoT中间输出的完整状态记录后，7步任务平均准确率从85.37%降至67.56%；GSM8K实验验证理论结论在真实推理场景成立
### 核心结论
CoT的OOD泛化能力本质来自单步预测器的跨步骤复用，而非直接拟合复杂端到端映射，显式状态跟踪是多步推理有效的核心前提
