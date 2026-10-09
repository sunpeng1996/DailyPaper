---
title: 'OnTrack: Real-Time Monitoring and Intervention in LLM Agent Trajectories via
  Streaming Structure-Aware Optimal Transport'
title_zh: OnTrack：基于流式结构感知最优传输的LLM Agent轨迹实时监控与干预
authors:
- Babak Barazandeh
- Connor Swanson
- Chinmay Kulkarni
- Nikhil Mungel
affiliations:
- Cribl AI Research Lab
arxiv_id: '2610.12375'
url: https://arxiv.org/abs/2610.12375
pdf_url: https://arxiv.org/pdf/2610.12375
published: '2026-10-08'
collected: '2026-10-09'
category: Agent
direction: Agent 轨迹实时监控与干预
tags:
- LLM Agent
- Trajectory Monitoring
- Optimal Transport
- Streaming System
- Anomaly Detection
one_liner: 提出毫秒级延迟的LLM Agent流式轨迹监控方案，可提前终止失败任务节省算力成本
practical_value: '- 电商导购Agent、客服Agent、售后履约Agent可直接复用L1层无参考的异常检测逻辑，无需额外LLM调用即可毫秒级识别死循环、无意义重复工具调用、停滞等问题，不影响用户交互体验

  - 对于有标准化执行流程的Agent任务（如订单退款、优惠券发放、商品上下架），可先沉淀历史成功执行的DAG作为参考样本，用最优传输对齐方法做实时合规校验，提前拦截错误操作避免资损

  - 工程实现可直接复用两级计算策略：常规路径每步仅跑1次暖启动迭代，只有触发异常预警时才执行全量收敛求解，兼顾线上高吞吐需求与异常检测准确率

  - 阈值设计可复用文中经验：放弃固定全局得分阈值，改用滚动窗口内的异常信号密度触发干预，同时给新执行步骤预留3步左右的grace window，大幅降低合法探索行为的误拦截率'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
当前LLM Agent在电商导购、运维、交易等场景自主执行时，主流监控方案存在明显缺陷：在线 safeguard 依赖额外LLM调用，大幅增加延迟与成本；事后日志评估无法及时止损，Token消耗与业务损失已发生；且现有方案普遍忽略执行步骤间的依赖结构，难以识别死循环、工具乱序调用、无意义重复调用等常见异常。

### 方法关键点
- 轨迹建模为动态增长的依赖DAG，支持三级能力降级：有历史成功参考+工具schema时可检测全类型偏差；仅schema时可拦截前置条件缺失的不可逆操作、检测循环/停滞；无任何先验时仍可识别死循环等高频异常
- 针对流式场景四大痛点做专项优化：加frontier mask仅匹配当前阶段应完成的参考步骤，不惩罚提前执行的合法步骤；新节点结构权重随时间线性增长，减少依赖边延迟发现带来的误报；每步仅执行1次暖启动最优传输迭代，仅触发预警时才跑全量收敛求解，单步延迟控制在1ms内；放弃全局固定得分阈值，改用单步异常信号+滚动窗口异常密度触发干预，适配不同执行长度的轨迹
- 三层解耦架构：L1参考无关的基础异常检测、L2依赖参考的最优传输对齐偏差检测、L3依赖schema的不可逆操作前置校验，仅不可逆操作需同步校验，不影响常规步骤延迟

### 关键实验
在SWE-bench共2288条真实Agent轨迹上测试，前8步时轨迹成败分类AUROC比传统内容相似度方法高0.057；部署基于异常密度的终止策略后，可节省约18%的失败任务算力，被拦截的任务中83%确实会最终失败，单步平均延迟仅0.85ms。

### 最值得记住的一句话
Agent监控的核心价值是用远低于工具调用的成本提前止损，分层降级+暖启动增量计算是平衡线上可用性、准确性、成本的最优路径。
