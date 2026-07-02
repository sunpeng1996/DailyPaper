---
title: 'Theoria: Rewrite-Acceptability Verification over Informal Reasoning States'
title_zh: Theoria：面向非形式推理状态的重写可接受性验证架构
authors:
- Ben Slivinski
- Michael Saldivar
affiliations:
- Independent Researchers
arxiv_id: '2607.01223'
url: https://arxiv.org/abs/2607.01223
pdf_url: https://arxiv.org/pdf/2607.01223
published: '2026-07-01'
collected: '2026-07-02'
category: Reasoning
direction: LLM推理验证 · 结构化可溯源
tags:
- LLM Reasoning
- Verification
- LLM-as-Judge
- Adversarial Robustness
- Formal Method
one_liner: 提出介于形式证明与整体LLM judge之间的结构化推理验证架构，兼顾高精度与可审计性
practical_value: '- 高风险Agent场景（如电商客诉自动处置、广告合规审核、金融类推荐决策）可复用其「推理拆分为带类型的状态转换+按justify类型做局部校验」架构，对比整体LLM
  judge对抗漏检率降低11.5pp，尤其擅长识别隐藏假设、伪造引用类错误

  - 业务需要可审计的推理链路（如推荐理由合规溯源、广告投放决策留痕）时，可借鉴「状态diff与变更一一绑定justify」的设计，所有错误可定位到具体步骤，满足合规要求同时降低排查成本

  - 做LLM输出质量评估时可参考其ensemble思路：结构化校验与整体LLM judge的错误重叠度仅0.14~0.36，多数投票组合可将精度提升至93.6%，同时基本维持原有覆盖率'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有LLM推理验证存在两端缺陷：形式证明助手精度极高但仅能覆盖可完全形式化的极小范围场景，整体打分的LLM judge覆盖广但输出不透明、不可审计，对抗场景下对隐藏假设、伪造引用等隐性错误漏检率高，无法满足金融、合规、医疗等高风险场景的可信要求。

### 方法关键点
- 核心设计为**重写见证（rewrite witness）**：将LLM推理过程转换为初始状态+带类型的状态转换序列，每个转换的理由仅分三类：citation（引用定理/规则）、computation（计算）、problem given（问题给定事实）
- 严格遵循**变更完备性不变量**：每一步状态间的所有语义差异必须被对应理由完全覆盖，任何隐藏假设都会以未授权变更形式暴露，无法静默通过
- 架构为「求解→形式化生成见证→分类型并行局部校验→冗余过滤→有限修复」，最终输出二元结果：认证通过/拒绝，拒绝结果直接弃用，不输出低置信度结果

### 关键结果
- 主实验（185道HLE-Verified Gold专家题）：覆盖率56.8%，严格精度91.4%，宽松精度100%，认证结果错误率比拒绝结果低5倍
- 对抗测试（95个注入错误样本）：总检出率94.7%，比整体LLM judge高11.5pp，其中隐藏假设检出率高28pp（90.6% vs 62.5%），伪造引用检出率高10pp（100% vs 90%）
- 跨域实验（GPQA Diamond 65道研究生级科学题）：覆盖率52.3%，精度97.1%；与整体LLM judge错误重叠度仅0.14~0.36，多数投票集成精度达93.6%，覆盖率58.9%

### 核心结论
不同架构的验证方法错误覆盖互补性极强，结构化局部校验+整体打分的组合能在几乎不损失覆盖率的前提下大幅提升高风险场景的推理可靠性。
