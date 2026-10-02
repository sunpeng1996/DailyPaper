---
title: 'CorrGRPO: Correlation-Normalized GRPO for Multi-Reward Learning'
title_zh: CorrGRPO：面向多奖励学习的相关归一化GRPO优化算法
authors:
- Wenbin Hu
- Huihao Jing
- Haochen Shi
- Yuxuan Liu
- Haoran Li
- Yangqiu Song
affiliations:
- Hong Kong University of Science and Technology
arxiv_id: '2609.36820'
url: https://arxiv.org/abs/2609.36820
pdf_url: https://arxiv.org/pdf/2609.36820
published: '2026-09-28'
collected: '2026-10-02'
category: Training
direction: 大模型RL对齐 · 多奖励优化
tags:
- GRPO
- Multi-Reward Learning
- Reinforcement Learning
- LLM Alignment
- Policy Optimization
one_liner: 替换GRPO归一化分母的协方差为皮尔逊相关系数，解决多奖励场景下大尺度奖励主导优化的问题
practical_value: '- 电商推荐多目标优化（点击率、转化率、客单价等）场景可复用CorrGRPO归一化思路，避免大尺度目标压制小尺度目标的优化信号，无需手动调整复杂的目标权重

  - 训练导购/客服类Agent时，用CorrGRPO平衡任务完成率、安全性、合规性、用户体验等多奖励，降低奖励调参成本

  - 现有基于GRPO的LLM对齐流程可零成本替换为CorrGRPO，仅修改优势估计的分母计算逻辑，无需改动其他训练模块，代码修改量小于20行

  - 多目标存在强相关或权衡关系时，CorrGRPO可自动适配奖励相关性调整更新幅度，扩展帕累托前沿，鲁棒性优于手动调参'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
GRPO是当前LLM RL对齐的主流轻量算法，无需单独价值网络。但多奖励场景下，其归一化分母采用总奖励的标准差，本质是所有奖励的协方差和，会被数值尺度大的奖励主导，压制小尺度但高价值的奖励信号：比如代码生成中效率奖励尺度远低于正确性奖励、Agent训练中安全奖励尺度低于效用奖励时，优化会严重偏斜，无法兼顾多目标。

### 方法关键点
- 保留GRPO优势估计的分子（中心化总奖励）不变，不改动预设的奖励权重，保证业务预设的目标优先级不受影响
- 将分母的协方差和替换为所有奖励两两皮尔逊相关系数的和，消除奖励尺度对归一化的影响，各奖励对归一化的贡献仅和相关性有关，和自身数值范围无关
- 零方差奖励对应的相关矩阵行列置0，保证数值稳定性，可直接兼容现有GRPO训练 pipeline

### 关键实验
在0.5B~8B参数模型上覆盖3类典型多奖励场景，对比baseline包括原生GRPO、GDPO等：
- 代码生成任务，在LeetCode、HumanEval等4个数据集上平均Pass@1相对GRPO最高提升4.21个百分点，同时扩展了正确性-效率的帕累托前沿
- 工具调用任务，RLLA-4K全Exact匹配率相对GRPO最高提升4.23个百分点，API-Bank泛化得分最高提升3.94个百分点
- Agent安全任务，联合准确率相对GRPO最高提升16.5个百分点， prompt injection攻击成功率最高下降7.36个百分点

### 核心结论
多奖励GRPO的优化偏差本质是协方差耦合了奖励相关性和尺度，仅修改归一化项就能用极低成本解决问题，无需调整奖励权重或引入额外模块。
