---
title: 'When Coding Agents Get Arms: Safety Risks Across the Digital-Physical Boundary'
title_zh: 具身编码Agent跨数字-物理边界的安全风险研究
authors:
- Yiming Sun
- Mi Zhang
affiliations:
- Fudan University
- JADE AI(Whitzard AI) Team
arxiv_id: '2611.11438'
url: https://arxiv.org/abs/2611.11438
pdf_url: https://arxiv.org/pdf/2611.11438
published: '2026-11-08'
collected: '2026-11-14'
category: Agent
direction: 具身Agent 跨域安全风险评估
tags:
- Embodied Agent
- Safety Benchmark
- Prompt Injection
- Zero-shot Control
- Coding Agent
one_liner: 提出首个ArmedAgent基准，系统评估零样本控制机械臂的编码Agent跨数字物理域安全风险
practical_value: '- 电商仓储具身拣货Agent可复用该基准的风险检测框架，提前识别恶意指令、间接prompt injection导致的误操作风险

  - 多模态Agent跨数字-物理域部署时，可参考该研究的5类36项任务场景设计前置安全校验模块，拦截有害执行逻辑

  - 零样本Agent上线前的安全审计流程，可复用该基准的「模拟验证+实体校验」两阶段评估方案，降低落地安全隐患'
score: 7
source: arxiv-cs.MM
depth: abstract
---

## 动机
编码Agent已实现零样本端到端控制实体机械臂，无需任务特定演示或重训，但存在两类未被覆盖的跨数字-物理域安全风险：大模型泛化能力带来的能力滥用，数字侧prompt injection等威胁传导至物理世界。
## 方法关键点
推出ArmedAgent基准，覆盖5类场景共36项测试任务，包含鲁棒性、恶意使用、间接注入三类测试维度，采用「模拟环境评估+实体机械臂验证」双重范式，专门覆盖传统VLA范式无法实现的有害行为测试集。
## 关键结果
对GPT-6-Astra等前沿大模型在主流Agent框架下测试，验证当前系统普遍存在显著的跨域安全风险。
