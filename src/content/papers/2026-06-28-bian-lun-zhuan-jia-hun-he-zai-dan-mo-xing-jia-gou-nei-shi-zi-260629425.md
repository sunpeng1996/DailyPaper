---
title: 'Mixture of Debaters: Learn to Debate at Architectural Level in Multi-Agent
  Reasoning'
title_zh: 辩论专家混合：在单模型架构内实现动态自辩论推理
authors:
- Dayong Liang
- Kaisong Gong
- Yi Cai
- Changmeng Zheng
- Xiao-Yong Wei
affiliations:
- South China University of Technology
- Tianjin University
- The Hong Kong Polytechnic University
arxiv_id: '2606.29425'
url: https://arxiv.org/abs/2606.29425
pdf_url: https://arxiv.org/pdf/2606.29425
published: '2026-06-28'
collected: '2026-06-30'
category: MultiAgent
direction: 多智能体推理 · MoE 参数高效适配
tags:
- multi-agent
- MoE
- reasoning
- LoRA
- parameter-efficient
one_liner: 基于MoE范式将多智能体辩论内化到单模型，降本同时提升复杂推理精度
practical_value: '- 构建在线Agent服务时，可复用MoD思路将多角色转化为轻量LoRA专家池，无需实例化多份模型，大幅降低推理 latency，适配高并发场景

  - 双路由解耦设计可迁移到电商Agent，将角色分配（搜索/比价/议价）和流程控制（讨论/总结）分离，动态适配不同用户query的推理需求

  - 动量滑动窗口路由平滑策略，可解决MoE token级路由频繁切换专家导致的输出连贯性差问题，适合生成导购文案、对话类生成场景'
score: 8
source: arxiv-cs.MM
depth: full_pdf
---

### 动机
现有多智能体辩论框架依赖设计时固定的静态角色架构，需要实例化多个独立模型副本，不仅带来极高的计算和延迟 overhead，也无法适配动态变化的推理任务需求；通用MoE架构也不适应辩论推理的特性，存在路由抖动不稳定、无法同时优化角色分配和流程控制两个正交目标，因此需要一种高效的单模型内化辩论推理方案。

### 方法关键点
- 架构设计：冻结基础大模型backbone，将辩论的**解释（角色分配）**和**合成（流程控制）**解耦为两个独立的轻量LoRA专家池，支持N×N种组合推理路径，保留辩论的行为多样性；
- 双路由机制：两个独立路由器分别负责角色分配和流程阶段管理，动态决定何时开启辩论、何时直接输出总结，可跳过简单子问题的不必要推理；
- 动量切换平滑：采用滑动窗口对最近W个token的路由输入做因果滑动平均，降低token级路由的抖动，兼容自回归生成，配合专用小缓存适配KV cache推理；
- 训练数据构造：从基础模型采样正确/错误候选回答，构造三类训练样本（一致正确链、纠错视点迁移、抗干扰鲁棒样本）做监督微调。

### 关键实验结果
在MMLU、ScienceQA、MMMU、MMStar等多模态推理基准测试，基于LLaVA-v1.6-13B backbone，MoD多轮推理相比传统多智能体辩论，在ScienceQA-TEST提升0.9个点、MMMU提升2.15个点，同时实现**3.7×更低推理延迟，减少87%的token消耗**，仅增加12M可训练参数；消融实验验证双路由比单路由在MMMU提2.65%精度，滑动窗口比原生token级路由在MMStar提3.2%精度。

最值得记住的结论：把多智能体辩论从多模型外部交互转化为单模型内的动态路由问题，可同时兼顾推理精度和部署效率。
