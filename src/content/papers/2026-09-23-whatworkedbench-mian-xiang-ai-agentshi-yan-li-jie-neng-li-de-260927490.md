---
title: 'WhatWorkedBench: Benchmarking Experimental Understanding in AI Agents'
title_zh: WhatWorkedBench：面向AI Agent实验理解能力的基准测试框架
authors:
- Jingjie Ning
- Xueqi Li
- Yibo Kong
- Dongting Li
affiliations:
- Carnegie Mellon University
- Tsinghua University
arxiv_id: '2609.27490'
url: https://arxiv.org/abs/2609.27490
pdf_url: https://arxiv.org/pdf/2609.27490
published: '2026-09-23'
collected: '2026-09-24'
category: Agent
direction: Agent 实验理解能力评估基准
tags:
- Agent Benchmark
- Experimental Design
- Response Surface Estimation
- Gaussian Process
- Causal Intervention
one_liner: 构建覆盖8类工作流的可执行基准，量化评估AI Agent通过有限实验预测组件干预效果的能力
practical_value: '- 调优推荐/广告多参数组合时，可复用「有限预算采样+高斯过程（GP）拟合补全未测配置效果」的方案，相同观测下比Agent自主预测的效果恢复度最高提升10.6%，大幅降低全量AB测试成本

  - 做算法消融实验自动化的Agent时，可引入代码等价性约束（如某开关关闭时对应参数失效），相同预算下能把GP的效果恢复度从0.248提升到0.462，减少无效采样

  - 评估自动调优Agent能力时，不要只看最优配置的选准率，还要评估对所有组件干预效果的预测准确率，避免选到最优配置但完全不懂参数间的交互效应，无法迁移到其他场景'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
当前AI Agent已能自主规划、执行计算实验，但缺乏对「实验理解能力」的量化评估标准——即Agent在有限实验预算下，能否准确预测不同组件改动对最终效果的影响。现有相关基准多关注最终任务性能，不关注对组件交互效应的理解，无法支撑自动实验Agent的迭代。

### 方法关键点
- 覆盖8类计算工作流（分类、回归、检索、时序预测等）、36个任务、30个数据源，共1248条全量配置的真实运行结果作为ground truth
- 评估范式：Agent可读取工作流代码、在预算内选择有限配置运行，最终提交所有配置的效果预测表（响应面）
- 评估指标包括条件效应MAE、效果恢复度、最优配置选择regret、严格重建率，明确区分「选对最优配置」和「真正理解组件效应」两个目标
- 设计固定观测下的对比范式，可单独拆分采样策略和拟合算法的贡献

### 关键结果
在4因子任务、8次测量预算下，pair效应岭回归恢复度达0.612，效应方差GP恢复度达0.701；相同观测下用GP回溯拟合，DeepSeek V4 Flash的恢复度从0.632提升到0.698，额外测试队列从0.621提升到0.720；在节拍检测、图链接预测任务上，GP拟合将Agent提交结果的恢复度从0.303提升到0.455；引入代码等价性约束后，6因子任务20次测量预算下GP恢复度从0.248提升到0.462。

**最值得记住的一句话**：选对最优配置不代表真正理解实验，35/36的任务中都存在组件效应的符号反转，仅靠平均效应或单点最优结论无法泛化到其他配置场景。
