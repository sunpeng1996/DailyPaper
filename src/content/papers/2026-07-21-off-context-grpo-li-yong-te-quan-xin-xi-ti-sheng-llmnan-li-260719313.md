---
title: 'Off-Context GRPO: Learning to Reason on Hard Problems using Privileged Information'
title_zh: Off-Context GRPO：利用特权信息提升LLM难例推理能力的训练方法
authors:
- Priyank Agrawal
- Ankur Samanta
- Shervin Ghasemlou
- Jalaj Bhandari
- Kavosh Asadi
- Daniel Jiang
- Aditya Modi
affiliations:
- Meta AI
- Columbia University
arxiv_id: '2607.19313'
url: https://arxiv.org/abs/2607.19313
pdf_url: https://arxiv.org/pdf/2607.19313
published: '2026-07-21'
collected: '2026-07-22'
category: Training
direction: LLM训练 · GRPO优化与难例推理
tags:
- GRPO
- RLVR
- Importance Sampling
- Privileged Information
- LLM Reasoning
one_liner: 对GRPO做最小修改，通过重要性重加权修正引导采样的上下文偏移，解决难例下的学习悬崖问题
practical_value: '- 业务中做Agent/推荐系统的RLHF流程时，遇到难case（比如复杂用户query理解、多步工具调用零成功率），可引入最短特权引导（如正确路径前缀）配合OC-GRPO的重要性修正，既突破学习悬崖，又避免直接SFT引导破坏模型原生行为

  - 小参数模型做端侧推荐/推理的RL训练时，优先用OC-GRPO替代原生带引导的GRPO，避免小模型无法吸收上下文偏移导致的效果退化，实测小模型规模下OC-GRPO增益更显著

  - 工程落地优先选择OC-GRPO-Fixed变体，仅需在训练前预筛选难case的最短有效引导前缀，无需训练中动态调整，额外开销可忽略，性价比远高于自适应引导方案'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有基于GRPO的RLVR（带可验证奖励的强化学习）方法在难例场景下存在致命的学习悬崖问题：当一个批次内所有采样输出全错时，组内奖励方差为0，无梯度信号无法学习；现有引入特权引导（如解题前缀、提示）的方法存在上下文偏移缺陷，训练时用带引导的prompt采样，却按无引导的目标更新，导致优化目标和部署目标不一致，小模型下甚至出现效果退化。
### 方法关键点
- 仅对GRPO做最小修改，引入重要性比值（无引导prompt下的输出概率 / 带引导prompt下的输出概率）对每token的优势重加权，保证优化目标和部署的无引导目标完全对齐
- 重要性修正天然实现行为感知的credit分配：高度依赖引导的正确轨迹权重被压低，带引导仍然失败的轨迹惩罚被放大，避免模型学习到依赖引导的伪推理能力
- 提供两种落地变体：OC-GRPO-Fixed提前预筛选每个难例的最短有效引导前缀，训练额外开销极低；OC-GRPO-Adaptive训练中动态调整引导层级，效果接近但训练成本更高
### 关键实验
在Qwen2.5 7B/3B/1.5B三个规模模型上，针对MATH数据集的难例训练，对比原生GRPO、POPE、PrefixRL、BREAD等基线方法，OC-GRPO-Fixed在7B模型上平均Pass@1相对提升13.8%，3B模型提升7.2%，1.5B模型提升10.2%，且小模型下基线方法普遍出现效果退化时，OC-GRPO仍能保持稳定增益。

最值得记住的一句话：特权信息可以用来引导探索，但参数更新必须修正其带来的分布偏移，才能保证优化目标和部署目标完全一致。
