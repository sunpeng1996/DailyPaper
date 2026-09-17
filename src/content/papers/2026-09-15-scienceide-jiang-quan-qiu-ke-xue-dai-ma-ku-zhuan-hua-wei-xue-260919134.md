---
title: 'ScienceIDE: Turning World''s Scientific Codebase into Agent Learnable Environments'
title_zh: ScienceIDE：将全球科学代码库转化为Agent可学习的训练环境
authors:
- Hejia Geng
- Zesen Huang
- Haoyang Li
- Wenbin Li
- Koutian Wu
- Zihan Zhou
- Yuanbo Pang
- Weihao Liu
- Zigong Xu
- Zhiping Li
affiliations:
- AItonomy Foundation
- PhAI-Labs
- Qwen
arxiv_id: '2609.19134'
url: https://arxiv.org/abs/2609.19134
pdf_url: https://arxiv.org/pdf/2609.19134
published: '2026-09-15'
collected: '2026-09-17'
category: Agent
direction: 科学Agent训练环境基础设施构建
tags:
- Agent
- Code Agent
- Training Environment
- SFT
- Reinforcement Learning
one_liner: 开源了可将科学代码库批量转换为Agent训练/评测环境的基础设施ScienceIDE
practical_value: '- 垂直领域Agent训练可复用「专家定验收规则+Agent自动批量生成任务+可执行校验」的流水线，替代人工标注任务，大幅降低领域Agent的训练数据生产成本，可直接迁移到电商运营/客服代码Agent、导购多轮Agent的训练场景

  - 长路径Agent RL训练可复用截断轨迹处理技巧：预算不足被截断的轨迹仅用于计算组奖励基线，不参与梯度更新，避免Agent投机输出短内容应付任务，解决电商多轮导购、复杂搜索Query理解等长路径任务的奖励偏置问题

  - 领域LLM微调可引入垂直场景的可执行交互轨迹做SFT，不仅能提升领域任务表现，还能正向迁移到通用能力，比如用电商后台代码修复、活动规则校验的交互轨迹微调LLM，可同时提升代码能力和规则推理能力'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
全球科学代码库沉淀了数十年的人类知识，但碎片化工具链、隐性领域规则、特殊正确性校验标准，导致这些知识无法直接转化为Agent的可训练经验，形成科学经验瓶颈；现有科学Agent基准多为人工构造的固定任务，没有可扩展的基础设施支撑批量生成可训练的环境与任务。

### 方法关键点
- 环境构建流水线：先由Agent自动解析代码库的依赖、测试、运行逻辑，再由领域专家定义模块边界、科学等价性规则、数值校验容忍度，打包为可复用的执行环境，每个环境自带私有校验器和标准化检查项
- 自动任务工厂：针对每个环境自动生成修复、实现、加速等7类任务，任务必须通过可执行验证：已知正确解可通过、错误基线无法通过才会被纳入任务库，避免标注噪音
- 统一训练接口：所有环境对外提供统一的交互接口，Agent交互轨迹可直接用于SFT、RL训练、模型评测，校验结果直接作为奖励信号，无需额外适配
- RL训练优化：针对长路径任务的预算截断问题，截断轨迹仅用于计算组奖励基线，不参与梯度更新，避免Agent学会缩短轨迹投机取巧

### 关键实验结果
- 累计构建27个科学代码库、64个环境、2812个验证任务，构造85个难例组成的评测集ScienceIDE-Hard
- 15款主流模型评测中，Claude Fable 5.1准确率最高为67.1%，GPT-6 Astra为63.1%，其余模型均低于40%，科学任务仍有较大优化空间
- 基于ScienceIDE交互轨迹SFT的Qwen系列模型，在科学代码修复任务上最高提升33pp，同时在通用代码、推理、知识基准上获得3-33pp的正向迁移提升
- 基于环境原生奖励RL训练的Qwen-4B，在两个科学环境的域外任务上奖励分别提升2.4倍、2.0倍

### 核心结论
垂直领域的可执行交互经验，是兼具领域针对性和通用迁移性的高质量训练数据，可同时提升Agent的领域能力和通用能力。
