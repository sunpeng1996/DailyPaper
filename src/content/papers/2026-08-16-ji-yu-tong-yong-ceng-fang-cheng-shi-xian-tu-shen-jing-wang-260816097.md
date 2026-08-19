---
title: Unifying Graph Neural Networks Through a Common Layer Equation
title_zh: 基于通用层方程实现图神经网络架构统一
authors:
- Sai Karthik Navuluru
- Siddhartha Shankar Das
- Bo Ni
- Hongjie Chen
- Yu Wang
- Baris Coskunuzer
- Nesreen K. Ahmed
- Franck Dernoncourt
- Mahantesh Halappanavar
- Tyler Derr
affiliations:
- University of Texas at Dallas
- Pacific Northwest National Laboratory
- Vanderbilt University
- Dolby Laboratories
- University of Georgia
arxiv_id: '2608.16097'
url: https://arxiv.org/abs/2608.16097
pdf_url: https://arxiv.org/pdf/2608.16097
published: '2026-08-16'
collected: '2026-08-19'
category: Other
direction: GNN架构统一 · 组件化设计框架
tags:
- Graph Neural Networks
- Unified Framework
- Message Passing
- GNN Architecture
- Graph Learning
one_liner: 提出7组件通用层方程，统一200+GNN架构，构建可对比可生成的GNN设计空间
practical_value: '- 做电商用户社交/物品关联图召回/排序的GNN选型时，可复用该框架的7组件维度对比不同GNN结构差异，降低选型试错成本

  - 自研业务定制GNN时，可基于插槽式设计按场景（异构图/长程依赖需求）灵活替换7类组件，降低架构设计复杂度

  - 排查GNN过平滑/过压缩问题时，可对应到传播bank/消息映射等具体组件定位根因，提升调优效率'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有GNN各架构族采用独立层方程表述，掩盖了底层共享计算逻辑与结构差异，无法支持跨架构统一对比、问题根因定位与系统化新架构设计。

### 方法关键点
提出包含更新域、通道集、传播bank、单通道消息映射、通道融合算子、自环/残差映射、更新映射7个组件的通用层方程，核心解耦信息流动路径（传播bank编码）与信息内容（消息映射编码），通过固定插槽规则覆盖消息传递、注意力、谱滤波等7类非互斥GNN架构族。

### 关键结果
可统一归类200+现有GNN架构，支持组件级架构对比与结构一致的新架构生成，同时建立了传播组件选择与过平滑、过压缩、异质性适配、表达能力的理论关联。
