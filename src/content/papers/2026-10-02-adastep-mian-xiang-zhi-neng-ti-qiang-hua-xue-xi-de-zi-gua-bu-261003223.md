---
title: 'AdaStep: Adaptive Step Credit Weighting for Agentic Reinforcement Learning'
title_zh: AdaStep：面向智能体强化学习的自适应步级信用加权方法
authors:
- Xin Wang
- Wenhao Wu
- Menghao Zhang
- Zhi Wang
- Kun Shao
- Jian Luan
affiliations:
- Tsinghua University
- Nanjing University
- Xiaomi Inc.
arxiv_id: '2610.03223'
url: https://arxiv.org/abs/2610.03223
pdf_url: https://arxiv.org/pdf/2610.03223
published: '2026-10-02'
collected: '2026-10-05'
category: Agent
direction: Agent 强化学习步级信用分配优化
tags:
- LLM Agent
- Reinforcement Learning
- Credit Assignment
- GRPO
- Long Horizon
one_liner: 为长 horizon LLM Agent 的 group RL 训练提供无额外开销的自适应步级信用分配权重
practical_value: '- 电商导购Agent、多步搜索任务的RL训练可直接替换GiGPO的固定加权系数为AdaStep的自适应权重，仅增加1%计算开销即可稳定提升任务成功率，无需额外调参

  - 长序列决策任务的信用分配可借鉴信号-总方差的权重构造思路，步级优势估计噪声大时自动压低权重，避免错误惩罚正确动作（如电商场景下不会误罚加购后跳转其他页面最终下单的加购动作）

  - 数据量不足的步级组可直接复用论文fallback策略：组内样本不够时权重设为1，无需额外设计规则，性能优于均值和0权重方案'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
长 horizon LLM Agent 训练通常使用稀疏最终奖励，GRPO这类轨迹级信用分配粒度太粗，无法区分单步动作的贡献；GiGPO加入固定权重的步级优势修正，但步级估计受下游随机行为、环境跃迁影响噪声大，固定权重要么放大噪声要么压制有效信号，严重影响训练效果。

### 方法关键点
- 将步级优势加权建模为潜步优势的MSE估计问题，在条件采样假设下推导最优的每状态收缩系数，系数本质是信号-总方差比：当回报波动主要由动作质量决定时保留局部信号，由下游随机量主导时压制噪声
- 无需额外critic、额外rollout或模型推理，仅用现有rollout的统计量计算权重，计算开销极低
- 不满足权重估计条件的小组采用fallback策略：组内回报相同则步级优势为0，否则权重设为1

### 关键实验
在ALFWorld、WebShop（模拟电商购物场景）、ScienceWorld三个基准上，采用Qwen3-1.7B/4B、Qwen2.5-7B三个骨干模型对比GRPO、GiGPO、HGPO等baseline，AdaStep全面领先，相比GiGPO最高提升9.36个百分点，仅增加约1%的信用计算时间。

**最值得记住的一句话**：步级信用修正的核心不是越密越好，而是要根据估计可信度动态加权，在压制噪声和保留有效信号之间做最优平衡。
