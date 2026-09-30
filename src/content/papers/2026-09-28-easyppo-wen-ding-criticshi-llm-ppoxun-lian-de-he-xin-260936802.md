---
title: 'EasyPPO: Stabilizing the Critic Is Key'
title_zh: EasyPPO：稳定Critic是LLM-PPO训练的核心
authors:
- Xuanyi Zhou
- Qiuyang Mang
- Huanzhi Mao
- Dacheng Li
- Wenhao Chai
- Mayank Mishra
- Yichuan Wang
- Karthik Narasimhan
- Alvin Cheung
- Joseph E. Gonzalez
affiliations:
- UC Berkeley
- Princeton University
arxiv_id: '2609.36802'
url: https://arxiv.org/abs/2609.36802
pdf_url: https://arxiv.org/pdf/2609.36802
published: '2026-09-28'
collected: '2026-09-30'
category: Training
direction: LLM 强化学习训练优化
tags:
- PPO
- RLHF
- Critic
- LLM Training
- Policy Optimization
one_liner: 针对LLM-PPO的Critic不稳定问题提出3项极简改进，全任务无训练崩溃效果优于基线
practical_value: '- 做LLM Agent的RL对齐时，截断样本仅过滤actor侧、保留给critic训练，避免策略过度偏向短回复、忽略回复完整性，适合电商客服/导购Agent的多轮对话优化

  - Critic损失按同prompt下采样回复的回报标准差倒数加权，平衡不同难度query的梯度贡献，可迁移到生成式推荐的RLHF训练，避免高方差query主导更新

  - Critic mini-batch设置为每轮rollout批的1/4（默认K=4），平衡梯度噪声抑制和梯度裁剪的离群点限制效果，降低LLM-RL训练崩溃概率，无需额外修改PPO主逻辑，工程改造成本极低'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
PPO是LLM RLHF/RLVR训练的主流算法，但现有实现常出现后期训练崩溃，核心根源未被明确。本文发现critic是PPO不稳定的核心来源，存在两种失效模式：一是同时为actor和critic过滤截断样本，会让策略目标偏移为「已完成样本的条件回报」，导致截断率持续升高、整体回报不升反降；二是同批次不同prompt的回报噪声异质性强，高方差prompt的梯度会主导critic更新，放大预测偏差。

### 方法关键点
- 仅actor侧过滤截断样本，critic训练保留所有完整+截断样本，保证critic学习全样本期望回报，间接鼓励策略生成完整回复
- 噪声归一化critic回归：每个prompt的critic损失按同组采样回报的标准差倒数加权，平衡不同方差prompt的梯度贡献，消除噪声异质性影响
- 适度缩小critic mini-batch：默认将每轮rollout批拆为4个mini-batch更新，既通过梯度裁剪限制离群点影响范围，又保留足够样本量抵消噪声

### 关键实验
在3类任务上验证：连续回报的FrontierCS编码任务、二分类回报的AIME24数学推理任务、多轮搜索的Search-R1任务，对比基线包括vanilla PPO、VAPO、HL-Gauss PPO。EasyPPO全程无训练崩溃，最优验证分相对PPO分别提升14.89%、2.28%、9.47%，是唯一在三类任务上均稳定且效果最优的方法。

**最值得记住的一句话**：LLM-PPO训练不稳定的核心根源是critic不稳定，仅需3项无额外开销的极简改进，即可大幅提升训练稳定性与最终效果
