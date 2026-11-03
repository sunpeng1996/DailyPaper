---
title: 'Strategist: Evolving Reasoning with Agents'
title_zh: Strategist：基于智能体的推理策略自动进化框架
authors:
- Taiming Lu
- Qi Xu
- Zhigang Hua
- Zhuang Liu
affiliations:
- Princeton University
- Meta
arxiv_id: '2611.03618'
url: https://arxiv.org/abs/2611.03618
pdf_url: https://arxiv.org/pdf/2611.03618
published: '2026-11-02'
collected: '2026-11-03'
category: Agent
direction: Agent推理策略自动优化与跨任务迁移
tags:
- Meta-Agent
- Inference Strategy
- Cross-task Transfer
- Reasoning Optimization
- Strategy Library
one_liner: 提出可跨任务复用的推理策略进化框架，降低39%推理成本的同时提升推理精度
practical_value: '- 可参考Strategy Blueprint设计，搭建企业内部Agent推理策略复用库，将推荐理由生成、用户意图识别、广告文案生成等场景的推理流程抽象为通用结构，跨业务复用避免重复开发

  - 多Tier模型路由思路可直接落地电商/推荐场景：简单请求（常见QA、热销品推荐）用小模型，复杂请求（多跳用户偏好推理、定制化导购）用大模型，可实现30%+的推理成本下降

  - 检索/提案/评估/积累的四步迭代框架可套用到业务策略优化：比如广告文案生成策略，每次迭代基于历史高 CTR 策略修改，自动评估效果后入库，越用效果越好

  - 策略与模型解耦的设计可降低底座切换成本：同一个推理策略可直接迁移到不同LLM底座，业务换模型时不需要重新设计推理流程'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
当前AI Agent的推理策略多为人工针对单任务手写，经验无法跨任务复用，策略优化效率低，无法随任务量增长自动迭代提升，成为Agent系统落地的核心瓶颈。

### 方法关键点
- 设计统一接口的Strategy Blueprint：将推理策略抽象为可执行Python代码，采用统一`execute`接口，支持不同策略互相调用、组合，仅保留通用结构剔除任务特定prompt，实现跨任务复用
- 搭建四步迭代优化流程：1）从共享策略库混合检索相关+多样化历史蓝图作为参考；2）每轮生成5个候选策略，覆盖全新设计、旧策略组合、旧策略微调三类，平衡探索与利用；3）采用训练/验证/隐藏/测试四层数据集拆分评估，避免过拟合；4）所有候选策略的结构、效果指标、经验笔记入库，实现知识持续积累
- 内置多Tier模型路由机制：每个推理步骤可选择fast/balanced/complex三档不同规格的模型，按需分配算力，兼顾精度与成本

### 关键实验
- 覆盖数学、代码、常识、多跳QA、推荐等7大类共40个benchmark，30个用于主迭代实验，10个作为跨任务验证集
- 对比18个主流基线（CoT、Self-Consistency、AutoGen、多智能体辩论等）的108种配置
- 主实验：30个benchmark中赢24个，平均精度74.7% vs 最强基线74.0%，推理成本降低39%
- 跨任务零搜验证：10个未见过的benchmark仅从库检索策略，平均精度81.4% vs 基线77.8%，成本降低23%
- 跨模型迁移：Qwen3上搜索得到的策略直接迁移到GPT-5、Gemini-2.5，精度最高提升20.5pp，成本降低35%-40%

### 核心结论
Agent系统的效果不止由模型决定，推理策略层的自动进化与积累，可以在不微调模型的前提下同时实现精度提升与成本下降
