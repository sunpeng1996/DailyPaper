---
title: 'Skill Self-Play: Pushing the Frontier of LLM Capability with Co-Evolving Skills'
title_zh: 技能自博弈：通过协同进化技能拓展大语言模型能力边界
authors:
- Siyuan Huang
- Pengyu Cheng
- Haotian Liu
- Tao Chen
- Yihao Liu
- Jingwei Ni
- Shijie Zhou
- Ziyi Yang
- Gangwei Jiang
- Mengyu Zhou
affiliations:
- 阿里巴巴通义千问大模型应用团队
- 香港中文大学
- 中国人民大学
- 中山大学
- 北京大学
arxiv_id: '2607.22529'
url: https://arxiv.org/abs/2607.22529
pdf_url: https://arxiv.org/pdf/2607.22529
published: '2026-07-23'
collected: '2026-07-27'
category: Training
direction: LLM自进化 · 技能协同自博弈
tags:
- Self-Play
- LLM Training
- Reinforcement Learning
- Skill Library
- Agent Capability
one_liner: 提出基于动态进化技能库的自博弈框架，平衡LLM自进化的任务多样性与验证可靠性
practical_value: '- 电商服务/导购Agent可直接复用动态技能库架构，将咨询应答、营销推荐、订单处理等场景封装为带验证器的技能模块，结合自博弈自动生成训练数据，无需大量人工标注即可快速迭代场景能力

  - 训练推荐/搜索场景的工具调用Agent时，可采用「技能引导生成+开放探索」双数据流混合方案，既保证训练任务的有效性，又能自动挖掘新的用户需求场景，避免训练数据模式坍塌

  - 自训练阶段可复用其难度匹配奖励机制，生成刚好位于当前模型能力边界的任务，避免过难/过易导致的训练低效，小模型场景下可大幅提升能力迭代效率'
score: 9
source: huggingface-daily
depth: full_pdf
---

### 动机
现有LLM自进化方法存在核心矛盾：绑定外部环境的自博弈可获得精准验证反馈，但任务域狭窄扩展性差；无引导的开放任务生成覆盖范围广，但缺乏可靠校验机制，容易积累错误导致训练数据崩塌，始终无法平衡任务多样性与验证可靠性，严重限制了无监督自进化的落地效果。

### 方法关键点
- 核心框架由Proposer、Solver、动态技能控制器三部分组成，三者通过RL循环协同进化：Proposer基于采样的技能生成匹配当前模型能力的挑战任务，Solver求解任务提升自身能力，控制器根据执行反馈迭代技能库
- 技能被定义为包含路由元数据、生成规则、可执行验证器、使用统计的模块化单元，技能库支持自动精炼现有技能、裁剪过时技能、从开放探索流中归纳全新技能的完整进化逻辑
- 采用双数据流混合设计：技能流生成结构化高可靠任务，开放探索流扩展任务边界，按比例混合构建梯度课程，用GRPO算法分别优化Proposer和Solver的策略

### 关键结果
实验覆盖工具调用（API-Bank、BFCL数据集）和逻辑推理（ZebraLogic数据集）两大域，测试5个3B-14B的开源LLM backbone，对比无引导自博弈基线：工具调用任务上，基础能力较强的Qwen、Granite模型获得2.8~6.5的绝对提升，初始对齐较差的Ministral-3-8B获得最高42.9的绝对提升；逻辑推理任务上，Ministral-3-14B获得最高12.0的整体准确率提升，小难度拼图提升超35个点，所有指标均显著优于基线。

> 值得记住：技能作为连接结构化验证和开放探索的中间层，是实现LLM可持续、无监督自进化的核心载体。
