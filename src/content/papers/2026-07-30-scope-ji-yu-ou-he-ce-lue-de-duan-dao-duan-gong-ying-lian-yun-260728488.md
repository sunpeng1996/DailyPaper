---
title: 'SCOPE: Supply-Chain Operations through Coupled Policies for End-to-End Coordination'
title_zh: SCOPE：基于耦合策略的端到端供应链运营协调框架
authors:
- Yunhao Liang
- Xianqi Cao
- Pujun Zhang
- Yuan Qu
- Yongzhi Qi
- Ningxuan Kang
- Max Z. J. Shen
affiliations:
- The University of Hong Kong
- OptiMax AI
- JD.com
arxiv_id: '2607.28488'
url: https://arxiv.org/abs/2607.28488
pdf_url: https://arxiv.org/pdf/2607.28488
published: '2026-07-30'
collected: '2026-08-01'
category: Other
direction: 供应链运营 · 端到端耦合决策优化
tags:
- Supply-Chain-Optimization
- End-to-End-Coordination
- Composite-Policy
- Operational-Planning
- Retail-Operations
one_liner: 提出端到端耦合的供应链决策框架SCOPE，在叮咚、京东场景优于分阶段优化基线
practical_value: '- 电商生鲜零售补货场景可直接复用耦合决策思路，替代现有分部门独立优化的模式，降低缺货率、库存积压与运输冗余

  - 可借鉴将供应链各类实体映射为token、基于共享全局效用评估完整计划的设计，降低跨模块决策冲突，提升全局收益

  - 现有供应链系统迭代可优先试点嵌入跨阶段决策依赖关系建模，无需全量重构，降低落地成本'
score: 7
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有供应链的选品、货源分配、补货频率、配送路由等决策由不同部门独立优化，忽略模块间的耦合依赖，易引发缺货、库存积压、无效运输等问题，整体运营效率低。

### 方法关键点
1. 提出SCOPE复合策略框架，将供应链各类实体抽象为token，基于共享运营表征做上下文关联，不同token映射对应决策接口；
2. 各阶段决策基于前置决策生成的局部计划输出，最终完整计划采用全局系统效用做统一评估，实现跨模块决策协同。

### 关键结果
在叮咚买菜、京东两个不同补货层级的大型生鲜零售供应链真实运营数据上测试，SCOPE性能持续优于分阶段独立优化方法，以及供应链运营常用的行业基线。
