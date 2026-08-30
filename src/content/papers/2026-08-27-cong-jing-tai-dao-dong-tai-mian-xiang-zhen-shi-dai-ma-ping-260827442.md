---
title: 'From Static to Dynamic: Benchmarking Real-World Code Review with MCR-Bench'
title_zh: 《从静态到动态：面向真实代码评审的MCR-Bench基准测试集》
authors:
- Dewu Zheng
- Yanlin Wang
- Xiwen Wang
- Kefeng Duan
- Hongyu Zhang
- Xilin Liu
- Yuchi Ma
- Zibin Zheng
affiliations:
- Sun Yat-sen University
- Chongqing University
- Huawei Cloud Computing Technologies Co., Ltd.
arxiv_id: '2608.27442'
url: https://arxiv.org/abs/2608.27442
pdf_url: https://arxiv.org/pdf/2608.27442
published: '2026-08-27'
collected: '2026-08-30'
category: Eval
direction: 多轮交互场景 · LLM评测基准构建
tags:
- LLM Evaluation
- Multi-round Interaction
- Defect Detection
- Benchmark Construction
one_liner: 推出首个缺陷状态感知的真实多轮代码评审基准MCR-Bench，给出主流LLM在该场景的实测结论
practical_value: '- 构建多轮交互类Agent（如电商多轮客服、售后工单处理）评测集时，可借鉴分轮次状态标注、缺陷全链路轨迹追踪的标注方法

  - 优化多轮LLM应用性能时，可针对本文发现的核心问题，重点优化跨轮次时序对齐、长上下文记忆衰减问题

  - 做缺陷/负样本敏感的业务（如广告违规检测、电商商品合规审核）评估时，可参考按缺陷类型、严重度分级测试的方案，针对性补全低显著性样本的训练数据'
score: 5
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有LLM自动代码评审方案普遍将任务简化为单轮静态决策，无法匹配真实场景多轮交互、缺陷动态演化的核心特性，缺少适配该场景的标准化评测基准。

### 方法关键点
推出MCR-Bench，是首个缺陷状态感知的多轮代码评审基准，覆盖5种常用编程语言，包含2269个真实多轮评审任务，每个任务标注细粒度缺陷元数据（类型、严重程度等）、跨轮状态标签，完整还原缺陷在多轮交互中的全链路演化轨迹。

### 关键结果
- 主流LLM在缺陷检测、缺陷生命周期状态追踪任务上整体表现有限，性能随交互轮次增加显著下降
- LLM性能对缺陷特征高度敏感，语义复杂、低显著性缺陷漏检率远高于其他类型
- 错误根源主要为跨轮时序对齐偏差、长程记忆不足两类
