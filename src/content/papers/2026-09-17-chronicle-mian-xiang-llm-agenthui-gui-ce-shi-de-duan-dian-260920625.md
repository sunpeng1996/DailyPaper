---
title: 'Chronicle: Cut-Point Replay for Regression Testing of LLM Agents'
title_zh: Chronicle：面向LLM Agent回归测试的断点重放框架
authors:
- Tisha Chawla
- Susheem Koul
affiliations:
- Microsoft
arxiv_id: '2609.20625'
url: https://arxiv.org/abs/2609.20625
pdf_url: https://arxiv.org/pdf/2609.20625
published: '2026-09-17'
collected: '2026-09-18'
category: Agent
direction: LLM Agent 回归测试与故障复现
tags:
- LLM Agent
- Regression Testing
- Record & Replay
- CI-CD
- Fault Reproduction
one_liner: 提出可选择指定边界运行新代码的断点重放机制，实现LLM Agent故障的可复现回归测试
practical_value: '- 业务侧上线电商导购Agent、售后工单Agent这类调用工具的LLM Agent时，可复用该框架的边界埋点方案，记录生产故障的调用轨迹，快速生成回归用例加入CI流程，避免同类故障重复上线

  - 不需要手写全量mock数据，直接基于真实生产的trace重放，仅把待验证的工具/逻辑模块设为live，既能保证测试场景真实性，又能避免重放时重复调用LLM产生的成本

  - 边界埋点的overhead仅23μs，几乎不影响生产运行性能，可直接在生产环境埋点记录全量调用轨迹，不需要额外部署压测环境采集故障场景'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
LLM Agent的输出存在非确定性，且依赖外部工具状态、多步调用轨迹，生产故障很难复现；现有tracing工具仅能记录运行过程，无法基于故障轨迹直接生成回归测试用例，每次验证代码修复都要重新构造场景，成本高且无法保证一致性。

### 方法关键点
- 对Agent的非确定性边界（LLM调用、工具调用、路由决策）添加`@boundary`注解埋点，每次调用生成不可变envelope存储输入、输出、元数据，支持敏感字段自动脱敏
- 支持两种重放模式：全量重放直接返回所有边界的记录结果，零LLM调用且完全可复现；断点重放可自由选择部分边界运行新代码（live），其余边界返回记录值，同时通过调用次数校验避免轨迹漂移
- 内置结构断言和可选LLM-as-judge，可直接将故障轨迹+断言转化为CI可执行的回归测试用例

### 关键实验
基于6个真实Agent故障场景（退款超发、货币错配、误删文件等）测试，对比全量mock基线：
1. 埋点overhead仅23μs/次，占单次300ms LLM调用耗时的0.008%，对生产性能无感知；
2. 全量重放20次完全一致，零LLM调用，单轮测试仅耗时3.5ms；断点重放在6个故障场景下100%检测到未加防护的故障代码，同时100%通过修复后代码和30个良性代码修改；
3. 突变测试中，断点重放测试能100%拦截所有会导致原有风险动作的代码突变，全量mock基线则完全无法检测工具代码修改带来的风险。

**最值得记住的一句话**：生产环境的真实故障trace是最有价值的测试用例，通过选择性重放可以零额外成本将其转化为持续集成的回归防护。
