---
title: 'UI-Mate: Advancing Open-Weight Foundation GUI Agents with In-Context Demonstrations'
title_zh: UI-Mate：基于上下文演示的开源权重基础GUI Agent框架
authors:
- Zihan Ding
- Longxu Dou
- Qi Gao
- Xiangwu Guo
- Shengchao Hu
- Zilong Huang
- Zihang Jiang
- Lei Ke
- Mengcheng Lan
- Weixian Lei
affiliations:
- Tencent Hy Frontier Team
arxiv_id: '2608.15930'
url: https://arxiv.org/abs/2608.15930
pdf_url: https://arxiv.org/pdf/2608.15930
published: '2026-08-15'
collected: '2026-08-18'
category: Agent
direction: GUI Agent · 上下文演示学习 · 自动化任务执行
tags:
- GUI Agent
- In-Context Learning
- Reinforcement Learning
- SFT
- Benchmark
one_liner: 提出环境锚定训练栈与上下文演示学习机制，开源GUI Agent达SOTA，配套长周期办公任务评测基准
practical_value: '- 上下文演示转子任务工作流的思路可迁移到电商运营自动化Agent：比如店铺装修、订单批量处理等固定流程，无需完整重放轨迹，允许异常重排，提升流程执行稳定性

  - 环境锚定的闭环数据引擎+能力树均衡采样方案可复用：解决业务Agent训练数据分布偏置、长尾能力缺失问题，自动补全弱能力的训练样本

  - 轨迹到token的信用分配+异步GRPO训练范式可直接用到Agent的RL优化环节：降低长序列任务训练的偏置，提升异构任务的训练效率，适配推荐/广告系统的Agent优化需求'
score: 9
source: huggingface-daily
depth: full_pdf
---

### 动机
当前GUI基础Agent落地面临两大瓶颈：训练端数据稀缺、分布偏置，交互端prompt模糊、执行不可靠，长流程跨应用任务执行一致性差，难以满足办公、电商运营等场景的自动化需求。

### 方法关键点
- 可扩展环境锚定训练栈：闭环数据引擎自动完成任务生成、环境构建、轨迹回滚过滤、层级能力均衡，并行输出SFT与在线RL的训练数据，配套统一任务-验证器绑定逻辑
- 上下文演示学习（DemoCUA）：将多模态演示转化为子任务级柔性工作流，而非刚性轨迹重放，执行时以实时界面像素为权威，匹配演示步骤的同时支持自主重规划
- OSWorkerBench基准：覆盖41个应用的100个长周期办公任务，支持纯指令与演示引导两种评测模式，拆分同任务自演示、跨任务变体演示两类评测子集

### 关键实验
UI-Mate-27B在OSWorld-Verified基准上得分77.0%，WindowsAgentArena上得分66.2%，成为开源权重SOTA；在OSWorkerBench上严格成功率41.0%、进度完成率76.9%，比Qwen3.6-27B基线分别提升17.7、24.5个百分点；同任务演示加持下，OSWorkerBench自演示子集严格成功率从17.2%提升至35.4%，进度完成率从67.9%提升至81.1%，长流程执行可靠性大幅提升。

### 核心结论
演示提升的不仅是任务平均完成率，更是Agent对未明确用户意图执行的一致性，而可靠性是Agent能力落地的核心前提。
