---
title: Scaling Discovery Requires Forgetting
title_zh: 规模化智能体探索能力提升需要引入遗忘机制
authors:
- Shangyin Tan
- Ben Zhou
- Lakshya A Agrawal
- Jialin Zhang
- Yilin Chen
- Qiuyang Mang
- Donghyun Lee
- Dennis Jacob
- Koushik Sen
- Alex Dimakis
affiliations:
- UC Berkeley
- Stanford University
- Bespoke Labs
arxiv_id: '2610.20563'
url: https://arxiv.org/abs/2610.20563
pdf_url: https://arxiv.org/pdf/2610.20563
published: '2026-10-14'
collected: '2026-10-15'
category: Agent
direction: Agent 自动探索遗忘机制优化
tags:
- LLM Agent
- Multi-Agent System
- Auto-Research
- Forgetting Mechanism
- Optimization
one_liner: 为长周期自动探索多智能体引入周期性遗忘机制，突破性能平台期，同预算下最高提效39%
practical_value: '- 做推荐/广告策略迭代、prompt优化、A/B测试的多Agent自动化系统时，可接入遗忘机制：当效果进入平台期后，清空所有Agent会话与历史候选，仅保留当前最优策略重启探索，无需额外算力预算即可获得效果提升

  - 多Agent协作无需设计复杂的点对点通讯逻辑，采用异步共享所有Agent的历史候选+对应分数的极简模式即可，无中心化调度器，工程落地成本极低

  - 长周期Agent任务（如爆款选品策略迭代、广告出价优化）可将Agent的提案修改幅度、单轮推理token数作为遗忘触发信号，替代固定周期遗忘，适配不同任务的收敛节奏

  - 遗忘机制可大幅降低长会话的KV cache开销，同预算下可支持更多轮探索，兼顾效果与成本'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
当前LLM驱动的自动探索Agent有三类规模化方案：单智能体长周期迭代、多智能体并行探索、带通讯的多智能体协作，但三类方案最终都会进入性能平台期：随着历史会话与尝试记录积累，Agent会被过去的失败尝试锚定，提案越来越保守，额外算力预算几乎带不来效果提升，亟需低成本的破局方案。
### 方法关键点
- 提出周期性遗忘机制：将探索拆分为多个轮次，每轮结束后清空所有Agent的会话上下文、历史候选与尝试记录，仅保留全局最优候选作为下一轮的唯一启动点
- 多智能体采用极简异步通讯：无中心化调度器，Agent之间无需直接对话，每次提案前仅可查看其他所有Agent的历史候选与对应评分
- 新轮次的所有Agent均为空白上下文，从当前最优候选重新启动探索，无历史负担
### 关键结果
在4类不同的优化任务（启发式编程竞赛、VLIW内核优化、组合优化、小语言模型训练脚本优化）上，同token预算下：
- 带遗忘的4智能体团队平均优于并行智能体基线10%，优于单智能体基线22%，最高在AHC014任务上比单智能体提升39%
- 遗忘后Agent的单轮代码编辑行数提升6倍，推理token数提升2倍，同增益下的算力成本仅为长会话持续迭代的50%
- 32/36次遗忘操作后均能产生新的全局最优候选

> 对于开放探索类任务，Agent被允许记住的内容和分配给它的计算资源同等重要
