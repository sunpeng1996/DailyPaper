---
title: 'RECAP: Training Long-horizon LLM Agents with Context Compaction'
title_zh: RECAP：面向长时序LLM Agent的上下文压缩训练框架
authors:
- Yulun Jiang
- Maria Brbic
- Michael Moor
affiliations:
- EPFL
- ETH Zurich
arxiv_id: '2611.31258'
url: https://arxiv.org/abs/2611.31258
pdf_url: https://arxiv.org/pdf/2611.31258
published: '2026-10-18'
collected: '2026-11-25'
category: Agent
direction: 长时序Agent · 上下文压缩RL训练
tags:
- LLM-Agent
- Context-Compaction
- Reinforcement-Learning
- Self-Distillation
- Long-Horizon
one_liner: 提出基于行为失真的RL框架，联合优化上下文压缩与Agent策略，提升长时序任务性能
practical_value: '- 电商多轮导购、搜索类Agent的上下文压缩训练可直接复用行为失真监督信号，替代仅依赖最终转化/回答准确率的稀疏奖励，解决长轨迹下压缩动作信用分配难的问题

  - 无需额外标注的自蒸馏trick可无缝嵌入现有GRPO/PPO等RL训练流程，用全上下文策略作为自老师监督压缩后动作，不增加额外推理开销

  - 小模型Agent部署场景可借鉴该方法，用短上下文窗口逼近长窗口效果（如4B模型32K窗口性能接近128K窗口），降低KV cache占用、提升高并发场景吞吐量'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
长时序LLM Agent的交互历史随任务推进快速增长，易触发上下文窗口溢出；现有上下文压缩与Agent策略联合RL训练方案仅依赖最终任务奖励作为监督，长轨迹下压缩动作的影响会随后续多轮交互扩散，信用分配噪声大，压缩策略优化效率低。
### 方法关键点
- 提出行为失真目标，通过压缩上下文与原始全量上下文下Agent后续动作的token级KL散度，量化压缩对Agent决策的影响
- 目标梯度拆解为两个互补无监督信号：①失真奖励分配给摘要生成步骤，对诱导行为偏差更小的压缩结果给予更高权重；②自蒸馏信号分配给压缩后的动作，以全上下文下的策略作为自老师，监督压缩上下文下的输出分布
- 两类信号与任务奖励直接融合进统一RL优化框架，无需额外轨迹采样或环境交互，训练开销与仅用任务奖励的基线持平
### 关键结果
基于Qwen3.5-4B测试：32K上下文窗口下，对比仅用任务奖励的GRPO基线，在BrowseComp-plus、SWE-bench Verified两个长时序基准上精度分别绝对提升4.6%、4.3%，工具调用数、总token消耗均显著降低；16K短上下文窗口下增益更突出，32K窗口下的精度仅比128K无压缩GRPO低1%，大幅缩小长短窗口性能gap。
> 最值得记住：上下文压缩的核心目标是保留原始历史诱导的Agent行为，而非单纯的信息留存，行为偏差信号可大幅降低长时序Agent的训练难度
