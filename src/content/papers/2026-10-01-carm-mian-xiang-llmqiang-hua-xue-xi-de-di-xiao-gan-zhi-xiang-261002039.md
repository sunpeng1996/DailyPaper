---
title: 'CARM: Cancellation-Aware Response Masking for LLM Reinforcement Learning'
title_zh: CARM：面向LLM强化学习的抵消感知响应掩码算法
authors:
- Yafei Zhang
- Songshuo Lu
- Sicong Liao
- Zhi Chen
- Yaohua Tang
affiliations:
- Moore Threads AI
arxiv_id: '2610.02039'
url: https://arxiv.org/abs/2610.02039
pdf_url: https://arxiv.org/pdf/2610.02039
published: '2026-10-01'
collected: '2026-10-02'
category: Training
direction: LLM强化训练 · 离策略响应掩码优化
tags:
- RLHF
- GRPO
- PPO
- Off-Policy Learning
- Sequence Masking
one_liner: 通过对token对数比率取绝对值平均的序列级掩码，避免正负漂移抵消，提升LLM RL训练效果
practical_value: '- 业务中若用RL对齐LLM（如Agent工具调用、推荐话术偏好对齐），可直接将现有GeoMean序列掩码替换为CARM，仅需修改掩码统计逻辑，改造成本极低，可稳定提升对齐效果

  - LLM RL训练时无需仅过滤负优势响应，实验显示CARM全量掩码相比仅负优势过滤，在数学推理、代码生成任务上提分可达10个点以上，该结论可直接复用

  - 序列过滤率与模型效果非单调正相关，无需盲目调高过滤阈值，可通过CARM的token违规比例理论bound快速校准阈值，减少调参成本'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
LLM RL（PPO/GRPO）训练中，策略更新、rollout与训练引擎差异会导致采样响应离策略，常用的GeoMean序列掩码对token对数比率取带符号平均，正负漂移会互相抵消，明明单token漂移幅度大却被判定为合规，引入大量训练噪声。

### 方法关键点
- 提出CARM序列掩码：计算每个token当前策略与rollout策略的对数比率的绝对值，做长度归一化平均后指数化得到判定指标，从根源避免正负漂移抵消
- 理论证明CARM接受的响应满足token比率违规比例、违规严重程度的联合bound，阈值具备明确的token级可解释性
- 掩码判定为常量不参与反向传播，完全兼容现有PPO/GRPO的token级损失逻辑，改造无需改动核心训练流程

### 关键结果
- 数学推理：Qwen3.5-4B/9B训练后，AIME 2024/2025/2026+BeyondAIME的mean@16较GeoMean最高提升3.13个百分点
- 代码生成：Qwen3.5-9B训练后，4个代码基准的平均pass@1较最强基线IcePop高2.88个百分点，LiveCodeBench上提分达6.7个点
- 相同过滤率下CARM效果显著优于GeoMean、TRM等基线，过滤率与效果非单调相关

### 核心结论
LLM RL训练中序列级掩码的核心是衡量双向漂移幅度而非净漂移，避免正负抵消才能真正控制离策略误差
