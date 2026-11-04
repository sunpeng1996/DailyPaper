---
title: 'JHiMA-WebRL: A Joint Hierarchical Multi-Agent Reinforcement Learning Framework
  for Long-Horizon Web Tasks'
title_zh: JHiMA-WebRL：面向长周期网页任务的联合分层多智能体强化学习框架
authors:
- Shanka Subhra Mondal
- Jiayun Wang
affiliations:
- Center for Advanced AI, Accenture
arxiv_id: '2611.05263'
url: https://arxiv.org/abs/2611.05263
pdf_url: https://arxiv.org/pdf/2611.05263
published: '2026-11-03'
collected: '2026-11-04'
category: Agent
direction: 多智能体Agent · 分层强化学习
tags:
- Multi-Agent
- Reinforcement Learning
- GRPO
- Web Agent
- Hierarchical Planning
one_liner: 通过分层GRPO联合训练任务分解器与执行器，用更小参数量实现网页长周期任务效果大幅提升
practical_value: '- 架构选择：做电商自动化Agent（自动退单、后台操作、商品巡检等）时，可拆分为任务分解+执行两个小模型，无需盲目堆叠单模型参数量，降低推理和训练成本

  - 算法trick：分层GRPO的角色专属优势计算方式可复用，仅用终端成功/失败的二进制奖励就能联合训练多模块，不需要复杂的过程奖励工程

  - 数据构造：无人工子任务标注时，可用强LLM作为教师从历史操作轨迹中自动生成子任务标注，快速构建规划模块训练数据

  - 工程实现：两个模块分别用LoRA微调，无需全参数更新，训练算力成本低，适合业务侧快速迭代Agent能力'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
单模型Web Agent处理长周期多步任务（如电商多步查询、售后退单、后台配置）时需要同时学习规划、状态跟踪、视觉 grounding、执行，能力上限低；此前模块化多Agent系统的规划器和执行器分开训练，规划器不会根据执行效果迭代，无法适配执行器能力，堆大模型参数量的投入产出比极低。

### 方法关键点
- 框架拆分为两个独立的Qwen2.5-VL-7B模块：任务分解器输入初始任务+首屏截图输出有序子任务序列，执行器输入子任务+当前页面截图+历史操作输出点击、输入等网页动作
- 用GPT-5.2-Codex作为教师模型，从76K公开GUI操作轨迹中自动生成子任务标注，分别完成两个模块的SFT
- 扩展GRPO为分层多智能体版本：每个任务分解器生成K个候选子任务，每个子任务对应执行器M次环境rollout，分别计算执行器优势（同子任务下不同执行结果对比）和分解器优势（不同子任务的平均执行成功率对比），仅用终端二进制奖励即可联合更新两个模块

### 关键结果
在WebArena-Lite-v2的154个长周期网页任务（含电商购物、后台管理等场景）上，14B参数量（7B分解器+7B执行器）的JHiMA-WebRL平均成功率37.2%，比同训练条件下的ScaleCUA-32B RL单模型高13.2个百分点；冻结分解器仅训练执行器效果下降3.8个百分点，移除分解器用单模型效果下降2个百分点以上。

最值得记住的结论：对于长周期交互类Agent任务，角色拆分的小模型联合训练，比盲目堆叠单模型参数量的投入产出比更高。
