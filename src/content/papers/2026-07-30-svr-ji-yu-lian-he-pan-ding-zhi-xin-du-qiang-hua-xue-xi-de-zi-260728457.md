---
title: 'SVR: Self-Verifying Refinement via Joint Verdict-Confidence Reinforcement
  Learning for Adaptive Test-Time Compute'
title_zh: SVR：基于联合判定-置信度强化学习的自适应测试时计算自验证框架
authors:
- Hongyu Chen
- Liang Lin
- Guangrun Wang
affiliations:
- Sun Yat-sen University
- Guangdong Key Laboratory of Big Data Analysis and Processing
- X-Era AI Lab
arxiv_id: '2607.28457'
url: https://arxiv.org/abs/2607.28457
pdf_url: https://arxiv.org/pdf/2607.28457
published: '2026-07-30'
collected: '2026-07-31'
category: Reasoning
direction: LLM推理优化 · 自适应测试时计算
tags:
- Self-Verification
- Adaptive Test-Time Compute
- Reinforcement Learning
- GRPO
- Confidence Calibration
one_liner: 提出无外部推理反馈依赖的自验证细化框架，用模型自生成判定与置信度自适应分配测试时计算资源
practical_value: '- 做Agent多轮推理/工具调用时，可复用「判定+置信度双门控停止策略」，在无外部验证器的场景下大幅减少无效推理轮次，降低token成本同时保证输出准确率

  - 多轮RL训练可借鉴固定horizon训练+推理自适应停止的范式：训练阶段强制跑满轮次保证数据覆盖，推理阶段用学习到的置信信号动态停止，无需为不同部署阈值重训模型

  - 生成式推荐/Query生成场景下，可复用联合置信校准+非对称惩罚过置信的奖励设计，减少高置信错误输出，提升模型自我评估的校准度，降低badcase'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
当前LLM测试时计算缩放存在明显资源浪费：固定预算方案给所有输入分配相同推理轮次，易对简单样本过度计算、难样本计算不足；验证器引导的细化方法依赖推理阶段无法获取的外部正确性反馈，同时LLM原生置信度校准度差，无法直接作为可靠的停止控制信号，亟需无外部oracle依赖的自适应计算分配方案。

### 方法关键点
- SVR框架每轮推理同时输出解、离散正确性判定（正确/错误/不确定）、置信度得分，仅当判定为正确且置信度超过阈值时停止推理，否则用自生成的验证信息构造下一轮prompt继续细化，推理全程不需要外部反馈
- 基于GRPO做固定horizon训练，轨迹级奖励融合三类信号：解正确性与跨轮进度奖励、验证信号校准奖励（含Brier风格置信校准、过置信错误惩罚、错误识别奖励、可停止正确状态奖励）、格式合规奖励，仅对最后一轮生成的token做策略梯度更新
- 训练阶段强制跑满预设轮次保证中间状态覆盖，推理阶段可通过调整置信度阈值灵活权衡准确率与计算成本，无需重训模型

### 关键结果
基于Qwen3.5-2B在7个数学推理benchmark测试，SVR宏平均准确率达0.563，平均仅需2.99轮推理，比最优非oracle多轮基线准确率高7.5pp，比固定10轮推理方法token消耗减少50%以上，和10次采样GRPO多数投票准确率相当但token消耗仅为后者的一半。

最值得记住的结论：通过RL让LLM学会可靠的自我验证，比依赖外部验证器或固定计算预算的方案，能获得更优的准确率-计算效率trade-off
