---
title: Forensic Trajectory Signatures for Agent Memory Poisoning Detection
title_zh: 用于Agent内存投毒检测的法医式行为轨迹签名方法
authors:
- Jun Wen Leong
arxiv_id: '2606.30566'
url: https://arxiv.org/abs/2606.30566
pdf_url: https://arxiv.org/pdf/2606.30566
published: '2026-06-29'
collected: '2026-06-30'
category: Agent
direction: Agent安全 · 内存投毒检测
tags:
- Agent Security
- Memory Poisoning
- Trajectory Analysis
- Behavioral Detection
- LLM Agent
one_liner: 发现LLM Agent内存投毒的行为不变量，仅靠工具调用日志实现高准确率检测
practical_value: '- 生产环境带工具调用的Agent可直接复用该思路：仅需工具调用日志即可做异常检测，无需修改Agent架构、访问内存/模型权重，接入成本极低

  - 机制驱动的特征设计更鲁棒：抓住攻击本身的信息依赖约束（必须先召回再执行恶意操作），比纯数据驱动的异常检测更稳定

  - 支持双阶段部署适配不同业务场景：前缀级实时检测（AUC=0.934）做前置拦截，全会话级检测（AUC=0.990）做事后安全审计

  - 可基于轨迹特征区分不同攻击向量，仅靠日志即可完成攻击归因，方便安全应急响应'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有LLM Agent内存投毒防御要么需要访问内存存储、要么依赖白盒模型权限，对大多数业务部署来说门槛太高；当前没有仅靠可观测工具调用日志就能检测内存投毒攻击的低侵入方案，无法满足生产Agent的安全审计需求。

### 方法关键点
- 核心发现：成功的持久化内存投毒存在机制强制的行为不变量：攻击者把漏出地址存在持久化内存，必须调用`memory recall fact`取出地址后才能调用`send email`完成漏出，`recall before send`的顺序是攻击的固有特征，正常会话极少出现
- 特征工程：仅从触发会话的工具日志提取19个轨迹特征，包括调用计数、结构标记、转移bigram、入口特征，全部只用到工具名称和顺序，不涉及任何请求/响应内容
- 部署模式：支持前缀-only实时检测（仅用发送前的轨迹特征）和全会话事后审计两种模式，简单树模型/逻辑回归即可达到最优效果，分类器架构本身不影响性能

### 关键实验结果
基于2520个标注会话（覆盖9个7B-120B参数模型、7种防御条件）验证：
1. 单条`recall before send`规则就达到AUC=0.9563，全特征Random Forest达到AUC=0.9904，召回率98.38%
2. 移除所有召回相关特征后AUC仍保持0.9904，证明攻击会留下多维度行为痕迹，签名是过定的，无法轻易规避
3. 跨模型留一验证中9个模型有6个达到AUC=1.000，无需微调就能泛化到GPT-4.1等前沿模型
4. 提示注入攻击的平均检测得分仅0.541，可清晰区分不同攻击向量

### 最值得记住的一句话
机制强制的行为不变量本身就无法被规避：攻击者要隐藏不变量就必须破坏攻击本身。
