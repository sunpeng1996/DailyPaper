---
title: 'PILOT in the Loop: Live Self-Improvement for Long-Horizon Agents'
title_zh: PILOT：面向长周期Agent的实时自优化监管执行框架
authors:
- Yang Xiao
- Yusong Sun
- Haoyi Wu
- Wenyang Hui
- Wen Da
- Zhaokai Luo
- Mu Chuan
- Yao Hu
- Wenjie Li
- Chengyue Jiang
affiliations:
- AllSpark Team
arxiv_id: '2608.26530'
url: https://arxiv.org/abs/2608.26530
pdf_url: https://arxiv.org/pdf/2608.26530
published: '2026-08-26'
collected: '2026-08-28'
category: Agent
direction: Agent 长周期任务实时自优化
tags:
- Long-Horizon Agent
- Self-Improvement
- Supervisor-Worker
- Skill Library
- Live Steering
one_liner: 提出监管执行分离的Agent架构，无需微调LLM即可实现运行中纠错和经验沉淀
practical_value: '- 电商导购、售后等长周期Agent场景可直接复用监管-执行分离架构：执行者负责具体对话/工具调用，监管者独立监控轨迹偏离，避免单Agent上下文被执行细节占满导致的判断失效

  - 可复用实时技能沉淀机制：将Agent执行中验证有效的用户问题解决套路、流程实时写入技能库，后续同类型任务直接调用，大幅降低token消耗，适合电商高频售后、咨询等场景

  - 长周期推荐/导购Agent迭代无需微调LLM，仅通过更新harness层的技能库和记忆即可实现效果提升，降低迭代成本和风险，适配业务快速迭代需求'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有长周期Agent自优化方法均为执行结束后复盘，既无法挽救当前运行失败的任务，也不能即时验证提取经验的有效性；单Agent自纠错会被执行细节占用上下文导致判断失准，子代理委托架构又无法干预运行中的子代理，存在明显架构缺口。

### 方法关键点
- 采用监管者-执行者分离的双层架构，两者复用同一冻结LLM backbone，无需微调模型权重，仅优化harness层的技能库与记忆
- 实现live steering机制：双工通道支持执行者主动上报进度/问题，监管者可在运行中下发纠正指令或终止无效执行，监管者独立上下文避免被执行细节干扰
- 实现live self-evolution机制：监管者在执行过程中实时将有效流程、失败模式沉淀到可复用技能库，后续新启动的执行者可直接加载更新后的harness

### 关键实验
基于Terminal-Bench 2.0、SWE-bench Multilingual、SWE-bench Pro三个长周期任务基准，对比Pi、OpenCode等同类型harness，冻结GLM-5.1、Kimi-K2.6两个backbone：单轮执行场景下6组配置有5组效果排名第一，Terminal-Bench 2.0上最高超出基线9.8pp；自优化场景下20轮迭代后GLM-5.1效果提升14.6pp、Kimi-K2.6提升12.4pp，平均输出token分别降低42.9%、47.4%，每百万token成功次数分别提升110.3%、134.0%。

最值得记住的结论：长周期Agent的自优化不需要等执行结束，运行中纠错和经验沉淀的闭环能同时提升当前任务成功率和后续任务效率。
