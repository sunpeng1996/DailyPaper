---
title: 'Opera: A Verbal Critic Framework for Long-horizon Coding Agents'
title_zh: Opera：面向长时序编码Agent的言语批评反馈框架
authors:
- Kai Mei
- Zhiyuan Hu
- Yutong Dai
- Juntao Tan
- Yifan Zhang
- Dingjie Song
- Dimitris N. Metaxas
- Silvio Savarese
- Ran Xu
- Zeyuan Chen
affiliations:
- Salesforce AI Research
- Rutgers University
- Lehigh University
arxiv_id: '2609.33987'
url: https://arxiv.org/abs/2609.33987
pdf_url: https://arxiv.org/pdf/2609.33987
published: '2026-10-07'
collected: '2026-10-10'
category: Agent
direction: Agent 推理优化与训练数据生成
tags:
- Agent Critic
- Long-horizon Agent
- Test-time Optimization
- Training Data Generation
- Coding Agent
one_liner: 提出基于持久化修正笔记的Critic框架，同时提升编码Agent推理成功率与训练数据质量
practical_value: '- 长时序业务Agent（如电商运营Agent、推荐调优Agent）可复用混合审查触发机制：固定间隔+事件触发（无进展、重复操作、报错等），兼顾反馈及时性与干预效率

  - 业务场景反馈模块可落地审计过滤机制：先校验反馈的证据充分性、非重复性再下发，减少错误反馈导致的业务损失，尤其适配有强规则的电商/广告场景

  - 垂直场景小模型迭代可参考训练范式：用强模型作为Critic引导小模型生成近似on-policy纠错轨迹做SFT，比直接蒸馏强模型轨迹的跨场景泛化性更好

  - Agent反馈可替换自由文本为类型化算子：提前定义业务常见错误类型、修正方向、验收标准，提升Agent对反馈的执行率和问题解决率'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
长时序Agent执行中易出现重复操作、冗余探索、误判任务完成等问题，现有Critic方案仅生成反馈不追踪落地效果，常出现干预时机不合理、反馈误判、问题未实际解决等缺陷，亟需闭环可追踪的反馈机制。

### 方法关键点
- 混合审查调度：采用固定间隔+事件触发（无进展、重复操作、工具调用报错、声称任务完成、提交结果）双模式触发审查，事件触发时重置周期定时器，无问题则不干预
- 类型化算子反馈：定义覆盖任务全流程的9类反馈算子，每类算子绑定适用场景、所需证据、修正方向、验收标准，每次审查仅输出1条反馈避免指令冲突
- 审计+持久化笔记管理：每条反馈作为持久化笔记存储，新增、更新、关闭笔记都需经过审计校验证据充分性，单独追踪Agent对反馈的依从性和问题实际解决状态，仅验证解决后才关闭笔记

### 关键实验
在Terminal-Bench 2.1、SWE-Bench Pro 100任务子集、DeepSWE v1.1三个编码Agent基准上测试，对比SWE-PRM、Agentic Rubrics等4种主流Critic基线：
- 推理阶段：不同基座模型任务成功率最高提升12.4、15.0、8.9个百分点，在所有基准上均取得最优效果，自审查（模型自身作为Critic）也能取得显著收益
- 训练阶段：用Opera引导生成的近似on-policy轨迹微调Qwen3.5-9B，在SWE-Bench Pro hold-out集上成功率提升10.2个百分点，效果对齐强模型蒸馏，且不会出现强模型蒸馏的跨场景性能下降问题

### 核心结论
Critic的价值不仅是给出反馈，更要追踪反馈落地直到问题实际解决，近似on-policy的纠错数据比强模型off-policy轨迹的泛化性更好
