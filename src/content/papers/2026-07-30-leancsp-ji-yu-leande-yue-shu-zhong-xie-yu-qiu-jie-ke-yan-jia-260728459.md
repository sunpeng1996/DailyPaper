---
title: 'LeanCSP: A Framework for Certifying Constraint Reformulation and Solving in
  Lean'
title_zh: LeanCSP：基于Lean的约束重写与求解可验证框架
authors:
- Pablo Manrique
- Stefan Szeider
affiliations:
- TU Wien, Vienna, Austria
- Algorithms and Complexity Group, TU Wien
arxiv_id: '2607.28459'
url: https://arxiv.org/abs/2607.28459
pdf_url: https://arxiv.org/pdf/2607.28459
published: '2026-07-30'
collected: '2026-08-03'
category: Other
direction: 约束求解 · 形式化验证
tags:
- Constraint Satisfaction Problem
- Formal Verification
- Lean Theorem Prover
- Symmetry Breaking
- Solver Certification
one_liner: 基于Lean定理证明器实现约束编程双层可验证框架，大幅降低求解开销，不依赖外部求解器可信度
practical_value: '- 广告库存分配、履约调度、选品组合优化等CSP业务场景，可引入对称破缺验证思路，在保证约束改写语义一致性的同时，大幅降低求解搜索开销。

  - 对核心约束求解模块正确性要求极高的场景（如大促库存分配、预算管控），可参考其端到端验证流程，无需信任外部黑箱求解器结果，避免约束改写错误导致的业务损失。

  - 同问题族参数化证明可跨实例复用的思路可迁移到业务规则验证中，一次验证全量场景生效，降低重复验证成本。'
score: 4
source: arxiv-cs.AI
depth: abstract
---

### 动机
约束编程广泛应用于调度、规划、配置等组合优化场景，现有流程存在两类可信风险：前置约束重写无法保证语义保留，外部求解器黑箱输出缺乏正确性校验，可能生成错误结果且难以被测试发现。

### 方法关键点
基于Lean定理证明器构建双层验证框架：1. 对全问题族做参数化形式化证明，验证约束等价、等可满足性、对称破缺约束的正确性；2. 支持对接MiniZinc、SMT-LIB、OPB等外部求解器格式，校验单实例求解证书的正确性，两层结合实现不依赖外部求解器可信度的端到端CSP验证流程。

### 关键结果
单个问题族的参数化证明可跨所有实例大小复用，最多可降低求解器搜索开销达2×10^7倍，最大实例的Lean端验证耗时仅需数分钟。
