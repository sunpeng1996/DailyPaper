---
title: 'FC-SWE: Failure-Conditioned RL for Long-Horizon Software Engineering Agents'
title_zh: 基于失败条件强化学习的长周期软件工程Agent框架FC-SWE
authors:
- Jia Liufu
- Bin Hu
- Linglin Jing
- Terry Kong
- Yuki Huang
- Ashwath Aithal
- Wenming Yang
- Jun Yang
affiliations:
- NVIDIA
- Tsinghua University
arxiv_id: '2610.07898'
url: https://arxiv.org/abs/2610.07898
pdf_url: https://arxiv.org/pdf/2610.07898
published: '2026-10-05'
collected: '2026-10-19'
category: Agent
direction: Agent 强化学习训练优化
tags:
- Reinforcement Learning
- GRPO
- LLM Agent
- Trajectory Optimization
- Long-Horizon Agent
one_liner: 提出带失败反馈的恢复轨迹RL训练框架，适配GRPO提升长周期SWE Agent问题解决率
practical_value: '- 电商文案/广告生成Agent、商品选品Agent可复用失败条件训练逻辑：将前次badcase的诊断反馈（如低点击率、违规原因）作为下一次生成的上下文，训练时采用轨迹局部奖励，避免后续成功的奖励错误分配给前次失败输出

  - 多轮交互Agent的RL训练可复用active-set优势估计方法：仅将实际执行的轨迹纳入对比组，排除未执行的占位样本，降低训练bias

  - 多轮试错Agent部署时可采用「环境重置+失败上下文注入」模式：无需携带之前交互的脏状态，仅将错误反馈作为输入，降低上下文冗余，提升推理效率'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
长周期多轮交互Agent的现有RL训练范式（如GRPO）仅独立采样单次轨迹，完全不利用失败尝试的验证反馈，而失败反馈中的诊断信息可有效指导后续尝试优化；但恢复轨迹的训练存在两大问题：恢复轨迹仅在前序尝试失败时才会生成，上下文依赖前序失败结果，无法直接套用原有独立采样的RL训练逻辑，需解决奖励分配、对比组选择的适配问题。

### 方法关键点
- 失败触发恢复链：单次尝试失败后，重置环境到初始任务状态，将失败输出+验证诊断反馈作为补充上下文输入，生成恢复轨迹，单条恢复链最多支持R轮尝试
- 轨迹局部奖励：每一次尝试的奖励仅对应自身的验证结果，后续恢复成功的奖励不会分配给前序失败轨迹，避免标签污染
- 主动集优势估计：同一任务的所有实际执行的初始和恢复轨迹组成对比组，排除未执行的占位轨迹，基于该集合计算GRPO的相对优势

### 关键实验结果
在SWE-bench Verified 500个任务上，基于Qwen3.5-4B训练的FC-SWE，Resolved@1达41.7%、Resolved@2达52.8%，较GRPO基线分别提升2.8、4.3个百分点；仅训练2轮尝试的策略，测试时11次尝试下Resolved@11达70.7%，较GRPO高3.4个百分点，相同分辨率下token效率比GRPO高~22%。

### 核心结论
给Agent注入失败反馈做训练增强的收益，远高于无反馈的多次独立重采样，前提是做好奖励分配和对比组逻辑的适配。
