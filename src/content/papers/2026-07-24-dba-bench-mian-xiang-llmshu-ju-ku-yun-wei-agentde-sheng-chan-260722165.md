---
title: 'DBA-Bench: A Production-Fidelity Benchmark for LLM-Based Database Operations
  Agents'
title_zh: DBA-Bench：面向LLM数据库运维Agent的生产级保真评测基准
authors:
- Junming Chen
- Junyang Jiang
- Xu Chen
- Zibo Liang
- Kai Zheng
affiliations:
- University of Electronic Science and Technology of China
arxiv_id: '2607.22165'
url: https://arxiv.org/abs/2607.22165
pdf_url: https://arxiv.org/pdf/2607.22165
published: '2026-07-24'
collected: '2026-07-27'
category: Agent
direction: Agent 垂直领域运维评测基准
tags:
- LLM Agent
- Benchmark
- Database Operation
- Fault Diagnosis
- Evaluation
one_liner: 构建覆盖106个真实场景的数据库运维Agent评测基准，补齐现有评测与生产环境的4类差距
practical_value: '- 垂直领域Agent评测可复用「生产环境保真+结果优先+可复现快照」框架，解决实验室与上线效果脱节问题

  - 多源观测（时序/日志/并发状态）+安全约束下的结果判定逻辑，可直接迁移到电商搜推系统故障排查Agent评测

  - 按诊断深度/环境复杂度划分场景难度的策略，可用来构建阶梯式测试集，支撑内部Agent迭代优化'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有LLM数据库运维Agent评测标准不统一，和真实生产存在4类差距：缺少运行库多轮读写交互、观测空间复杂度不足、解空间未覆盖多方案权衡、场景未覆盖跨域级联故障，导致方案无法公平对比。

### 方法关键点
提出DBA-Bench，基于带真实工作负载的instrumented PostgreSQL环境，支持多源观测、状态持久化；采用结果优先评测逻辑，以安全约束下的故障消除/恢复为成功标准；每次运行前恢复场景快照保证可复现，覆盖7类任务域共106个场景，按诊断深度、环境复杂度划分易/难两个等级。

### 关键结果数字
9组基线（6个基础模型、2个GPT-5.5驱动的数据库Agent、人类DBA）共848次自动化运行的平均诊断通过率32.7%、结果通过率19.6%、安全通过率12.4%；最优自动化基线安全通过率17.9%，远低于人类DBA的93.4%；难场景下自动化安全通过率降至7.6%。
