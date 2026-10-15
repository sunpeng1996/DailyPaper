---
title: 'MMLA-RSI: Recursive Self-Improvement through RTT and RTMA'
title_zh: MMLA-RSI：基于推理时训练与记忆适配的可控递归自改进框架
authors:
- Junyi Zou
- Avrova Donz
affiliations:
- MMLA-org
- Communication University of China
arxiv_id: '2610.20294'
url: https://arxiv.org/abs/2610.20294
pdf_url: https://arxiv.org/pdf/2610.20294
published: '2026-10-14'
collected: '2026-10-15'
category: Agent
direction: Agent 可控递归自优化框架设计
tags:
- Agent
- Self-Improvement
- LoRA
- Memory Adaptation
- Recursive Learning
one_liner: 提出双路径可控递归自改进方案，分别更新策略状态与权威记忆，支持安全迭代优化
practical_value: '- 可复用双路径优化思路：业务Agent迭代中拆分「策略参数微调（如LoRA更新）」和「权威记忆库更新（如RAG知识库）」两个独立路径，避免参数与记忆更新的耦合冲突

  - RTT落地参考：借鉴其带约束的梯度裁剪、动量更新规则，在搜索推荐实时微调场景中限制参数更新范围，避免模型分布偏移

  - RTMA工程实现：其基于显式特征的内存淘汰、写前验证规则可复用在RAG系统的记忆更新模块，降低脏数据写入风险

  - 实验设计参考：反馈绑定对照实验（真实/虚假反馈+保留/重置状态）可直接用于业务A/B实验，准确度量优化路径的真实收益，排除随机波动干扰'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有Agent自改进方案多未拆分参数与记忆的优化链路，缺乏可解释的约束机制，迭代过程不可控、收益难追溯，无法直接落地到风险敏感的工业场景。
### 方法关键点
- 双独立优化路径：RTT（推理时训练）路径通过LoRA结构更新低秩策略状态Φ，RTMA（推理时记忆适配）路径更新带权限校验的权威记忆库M，支持单独或联合优化
- 递归迭代机制：当前代的策略更新器、记忆管理器会参与下一代候选规则的生成，候选规则需经过独立任务审计通过后才会正式替换上代规则
- 严格因果约束：明确「尝试结束→反馈到达→更新提交→下次推理」的事件顺序，所有状态带版本标记，优化链路可完整溯源
- 边界安全控制：固定解释器、可信提交器、独立审计器三层校验，限制参数更新范围、内存写入规则，避免无约束自修改
### 关键结果
四候选程序选择任务中，保留LARC反馈更新相对无适配baseline，两种初始化方案的预期错误分别下降24.65、36.65个百分点；时序持续集成回放场景下反馈绑定效果为正，但记忆保留会升高损失。
**值得记住的一句话**：自改进系统的功能生效与任务收益是两个独立指标，有效更新不一定带来正向收益，必须通过独立审计和对照实验验证真实价值。
