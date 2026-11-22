---
title: Backtracking Agent Applications Security Incidents
title_zh: Agent应用安全事件入侵入口点回溯工具Origin
authors:
- Yicheng Cai
- Taegyu Kim
- Peng Liu
affiliations:
- Pennsylvania State University
arxiv_id: '2611.26525'
url: https://arxiv.org/abs/2611.26525
pdf_url: https://arxiv.org/pdf/2611.26525
published: '2026-11-19'
collected: '2026-11-22'
category: Agent
direction: Agent 应用安全事件溯源技术
tags:
- Agent Security
- Backtracking
- Cross-layer Mapping
- CEP Detection
- Taint Propagation
one_liner: 提出基于跨层依赖图的Origin工具，解决语义Gap实现Agent安全事件入侵入口点准确定位
practical_value: '- 自研Agent业务（如电商导购Agent、广告投放Agent）可复用跨层语义映射思路，打通上层功能轨迹日志与底层执行日志的关联，快速排查业务异常

  - 线上Agent故障排查场景可借鉴区域推理算法，缩小根因排查范围，降低人工排查代码的时间成本

  - 带敏感操作权限的Agent系统（如支持下单、预算调整的Agent）可接入类似回溯工具，安全事件发生后快速定位入侵入口，降低资产损失'
score: 4
source: arxiv-cs.AI
depth: abstract
---

### 动机
Agent应用部署规模高速增长，但Agent专属攻击风险凸显，安全事件发生后需定位入侵入口点（CEP）完成止损；现有仅有的轨迹日志属于上层功能抽象层，CEP候选对应底层代码执行层的函数调用，两层语义Gap导致必须人工逐行排查代码，效率极低。

### 方法关键点
1. 设计跨层依赖图（CLDG）作为中间抽象层，关联上层语义维度的区域推断函数与底层污点传播子图的变量，配套专用查询语言降低使用门槛
2. 提出区域推理算法，自动构建功能区域到代码变量的映射关系，支撑跨层关联图的自动化构建

### 关键结果
在5款主流开源Agent应用、8个真实攻击场景的案例测试中，分析师使用Origin工具可100%准确识别所有入侵入口点。
