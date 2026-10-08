---
title: Training Advisors for LLM Agents from Task Outcomes
title_zh: 基于任务最终结果训练 LLM Agent 的自然语言反馈顾问模型
authors:
- Sergei Polezhaev
- Barys Liskavets
- Ori Press
- Alexander Golubev
affiliations:
- Nebius AI
arxiv_id: '2610.09858'
url: https://arxiv.org/abs/2610.09858
pdf_url: https://arxiv.org/pdf/2610.09858
published: '2026-10-07'
collected: '2026-10-08'
category: Agent
direction: Agent 反馈顾问训练 · 跨模型跨域迁移
tags:
- LLM Agent
- Reinforcement Learning
- Critic Training
- Transfer Learning
- DAPO
one_liner: 提出无需步骤级标注、仅用任务最终结果训练可跨模型跨域迁移的LLM Agent反馈顾问Caddie
practical_value: '- 电商客服、导购类多步Agent可直接复用Caddie训练范式，无需标注每步反馈，仅用会话最终成交/问题解决率作为奖励训练小型顾问模型，大幅降低标注成本

  - 可直接复用self-call反馈触发机制，给业务Agent新增call_advisor工具，让Agent自主判断何时请求反馈，避免固定干预时机的效果波动，适配多步商品检索、退换货流程处理等场景

  - 利用跨模型迁移特性，用小基座（如4B）训练的顾问模型可直接对接大基座业务Agent，无需针对每个大基座单独训练顾问，节省训练资源

  - 若业务主Agent已通过RL完成优化，可叠加训练Caddie顾问进一步提升效果，两者能力互补，可用于下单引导、售后处理等已经完成基础优化的场景'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有LLM Agent执行多步任务时容易陷入无效循环、偏离初始目标，传统过程奖励模型依赖昂贵的步骤级标注，已有的批评反馈模型要么需要参考批评样本，要么难以跨模型跨域迁移，无法直接通过任务最终效果对齐反馈价值。

### 方法关键点
- 全程冻结基座Agent，仅在轨迹中间随机采样节点让批评模型生成自然语言分析和建议，以基座Agent接收反馈后的任务最终成功率作为奖励，用DAPO算法更新批评模型参数，无需任何步骤标注或参考批评样本
- 推理支持三种干预模式：固定窗口干预、概率干预、Agent自主调用（self-call），最优模式为Agent通过`call_critic`工具自主判断何时请求反馈，无需外部调整干预时机
- 奖励计算直接取接收反馈后N次轨迹rollout的平均最终成功率，组内归一化后作为优势更新批评模型，实现反馈效果的直接对齐

### 关键结果
- 在MuSiQue多跳问答数据集上，用Qwen3-4B训练的Caddie相比无批评基线，将同基座Agent成功率提升25.31个百分点，效果超过无批评的Kimi K3
- 训练好的4B批评模型无需微调直接适配3个未见过的基座（Qwen3-30B、Qwen3.8-27B、Kimi K3），成功率最高提升13.19个百分点；跨域迁移到𝜏3零售、航空客服、DeepDive搜索任务上，成功率最高提升7.81个百分点
- 已通过DAPO优化过的基座Agent，叠加Caddie后还能再提升13.88个百分点，两者能力互补

最值得记住的结论：仅用任务最终结果训练的小型反馈顾问，可跨不同基座、不同业务域为Agent带来稳定效果提升，大幅降低多步Agent的优化成本
