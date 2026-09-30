---
title: 'Marathoner: Ultra-Long-Horizon Autonomous Intelligence'
title_zh: Marathoner：具备超长时间执行能力的自主智能体训练框架
authors:
- Zhang Ruiyang
- Ou Jinpeng
- Xie Yifan
- Zhou Jingang
- Pan Lirui
- Guo Qingpei
- Zheng Zhedong
affiliations:
- University of Macau
- Peking University
- Ant Group
arxiv_id: '2609.34378'
url: https://arxiv.org/abs/2609.34378
pdf_url: https://arxiv.org/pdf/2609.34378
published: '2026-09-27'
collected: '2026-09-30'
category: Agent
direction: Agent 超长时间跨度任务执行优化
tags:
- Autonomous Agent
- Long Horizon Task
- Reinforcement Learning
- RFT
- Task Synthesis
one_liner: 通过三阶段后训练 pipeline 让开源Agent获得10+小时连续执行、千次工具调用的超长周期任务能力
practical_value: '- 训练长周期执行Agent时，可复用Multi-Task Chaining方法，把业务场景下的多步原子任务（比如用户全生命周期运营、跨链路搜索推荐优化）串联为更复杂的训练任务，提升Agent处理长流程业务的能力

  - 可借鉴Later Stage Bonus Reward设计，针对推荐/广告Agent的长链路转化任务（比如从曝光到复购的全路径优化），给后期有效操作额外奖励，避免Agent只关注短期目标、后期放弃探索

  - 工程上可复用多harness轨迹生成+拒绝采样微调的范式，用强老师模型在业务场景生成成功轨迹，再做SFT冷启动，大幅降低长周期Agent的训练成本'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前头部闭源模型已具备数天级连续执行复杂任务的能力，但训练方案未公开，开源Agent普遍缺乏超长时间跨度（数小时到数天）的持续执行能力，无法处理跨多子任务、需要上千次工具调用的复杂场景，亟需可复现的训练框架。

### 方法关键点
- 超长时间跨度任务合成：基于1万个GitHub仓库的10万条大版本PR生成Easy/Medium/Hard三类难度任务，新增Multi-Task Chaining机制将5个原子任务串联为难度更高的Frontier任务，覆盖从短到长的任务跨度
- 拒绝采样微调（RFT）：用Kimi K3作为教师模型，搭配Claude Code/Codex/OpenClaw 3种不同harness生成任务执行轨迹，仅保留奖励为1的成功轨迹，对256k上下文的基座做SFT，获得冷启动长周期执行能力
- 强化学习优化：采用GRPO算法做RL训练，新增Later Stage Bonus Reward，对轨迹后半段的有效操作额外加0.5分奖励，避免Agent在长任务后期放弃有效探索

### 关键实验
在5个长周期任务基准上测试，对比基座Qwen3.5-9B，Marathoner-9B在FrontierSWE上提升158.8%（从10.2到26.4），SWE-Marathon从0提升到8.2，甚至超过Gemini-3.1-Pro在多个基准的表现，可连续执行10+小时、完成1000+次工具调用。

> 最值得记住的一句话：持续扩大RL训练的真实环境任务规模，是提升Agent长周期执行能力上限的核心路径
