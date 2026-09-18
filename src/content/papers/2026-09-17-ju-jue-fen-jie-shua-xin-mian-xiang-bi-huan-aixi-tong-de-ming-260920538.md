---
title: 'Refuse, Decompose, Refresh: A Claim-Safe Protocol for Closed-Loop AI Evaluation'
title_zh: 拒绝、分解、刷新：面向闭环AI系统的声明安全评估协议
authors:
- Peiying Zhu
- Sidi Chang
affiliations:
- Blossom AI, San Francisco, CA, USA
arxiv_id: '2609.20538'
url: https://arxiv.org/abs/2609.20538
pdf_url: https://arxiv.org/pdf/2609.20538
published: '2026-09-17'
collected: '2026-09-18'
category: Eval
direction: 闭环AI评估 · 结论有效性校准
tags:
- Closed-Loop-Evaluation
- Claim-Safety
- Distribution-Shift
- Selective-Prediction
- Agent-Evaluation
one_liner: 提出包含拒绝、分解、刷新三步的闭环AI评估协议，构建可支撑明确有效结论的可执行评估契约
practical_value: '- 线上A/B实验可引入Refuse逻辑，无干净基准流或匹配runtime对照组时直接弃权，避免基于无效数据得出错误迭代结论

  - 评估输出避免只用单一涨跌标签，可拆解为协议执行情况、误纳率、结构假设验证三部分，大幅降低结论误导性

  - 分布漂移告警不要直接判定为策略故障，可触发基准映射重算，适配电商/推荐场景常见的流量分布波动问题'
score: 6
source: arxiv-cs.AI
depth: abstract
---

### 动机
闭环AI系统（如推荐、Agent）的评估即使可完全复现，也容易因策略决定访问状态、故障可观测性差异等问题导出错误结论，现有评估框架普遍缺乏明确的结论有效性边界。
### 方法关键点
提出三步声明安全评估协议：1. Refuse：无干净参考流或匹配运行时对照时直接弃权；2. Decompose：拆分输出协议执行情况、操作误纳率、结构假设验证结果，替代单一PASS/FAIL标签；3. Refresh：将分布漂移告警作为基准映射失效重算的触发信号，而非直接作为故障证据。
### 关键结果
在含24个策略组件、3种需求模式的模拟器上验证，预注册留存集共1440个测试用例，仅55/72的模式-组件单元通过参考准入，其中54/55通过运行时准入；稳定误纳率为0/20，95%单侧上界0.1391；准入单元内干净流量预测效果优于标称故障单元，负对数似然差达0.1264 nats/行。
