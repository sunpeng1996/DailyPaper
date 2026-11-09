---
title: 'AgentBaton: Efficient Model Collaboration in Agentic Tasks'
title_zh: AgentBaton：长周期Agent任务的高效异构模型协作框架
authors:
- Junlong Li
- Jindong Jiang
- Yonggan Fu
- Jiarui Yao
- Hanrong Ye
- Wonmin Byeon
- Peter Belcak
- Hao Zhang
- Pavlo Molchanov
affiliations:
- The Hong Kong University of Science and Technology
- University of Illinois Urbana-Champaign
- NVIDIA
arxiv_id: '2610.35959'
url: https://arxiv.org/abs/2610.35959
pdf_url: https://arxiv.org/pdf/2610.35959
published: '2026-10-24'
collected: '2026-11-09'
category: Agent
direction: Agent 多模型协作成本优化
tags:
- LLM Agent
- Model Collaboration
- Cost Optimization
- Handoff Detection
- Inference Efficiency
one_liner: 提出轻量切换检测器与强到弱模型接力策略，平均降低Agent任务65.9% API成本且保精度
practical_value: '- 长周期Agent业务（电商智能客服、商品文案生成Agent、售后问题处理Agent）优先采用强→弱模型接力架构，放弃弱→强的思路，后者普遍精度低于纯强模型且成本下降空间极小

  - 上下文传递可直接复用结论：强→弱接力优先用in-context方式传递历史，仅当强模型不暴露思维链时改用logfile方案；弱→强场景（若必须使用）优先用logfile传递，可同时提精度降成本

  - 切换时机判断逻辑可直接落地：当任务产出可运行原型/物料、已经拿到真实用户/系统反馈、剩余工作为局部优化（如文案润色、规则调优、结果校验）时即可切换到小模型，可基于该规则训练2B级轻量检测器，单H100上p95延迟仅1.11s，完全满足线上要求

  - 线上模型路由避免踩坑：不要用query级静态路由（几乎无成本收益），也不要用每轮动态路由（成本高且精度波动大），单次切换的方案成本收益比最优，比MTRouter等每轮路由方案最多降本86.6%'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
长周期Agent任务（如复杂编程、系统运维、电商多轮咨询等）依赖高成本大模型多轮调用，API开支极高；现有query级静态路由、每轮动态路由方案未考虑任务进度的动态变化，要么无法有效降本，要么显著损失精度，异构模型在单任务内的协作策略缺少系统性研究。
### 方法关键点
- 通过控制变量实验验证两种接力方向的效果：弱→强接力普遍精度低于纯强模型，成本下降空间有限；强→弱接力在合适时机切换可同时保精度、大幅降本，因此采用单次强→弱接力架构，切换后无需切回强模型
- 上下文传递提供两种方案：in-context直接传递完整历史对话，logfile将历史写入环境文件供模型按需读取；强→弱场景优先用in-context（仅当强模型不暴露思维链时用logfile），弱→强场景优先用logfile
- 训练2B级轻量检测器AgentBaton，基于「是否产出可运行原型/物料、是否拿到真实反馈、剩余工作是否为局部优化」三个特征判断切换时机，每轮执行后检测一次，触发切换后弱模型接棒直到任务结束
### 关键实验
在Terminal-Bench 2.1、DeepSWE v1.1两个长周期Agent基准，11组模型对测试：平均降低65.9% API成本，精度最高比纯强模型高8.8个百分点；对比每轮路由基线MTRouter，降本46.7%~86.6%且精度持平甚至更高，大幅拓展了精度-成本帕累托前沿。
### 核心结论
长周期Agent任务中，单次强到弱的模型接力，比静态路由、每轮动态路由的成本收益比都高，是兼顾精度和成本的最优选择。
