---
title: Selective Credibility-Limited Belief Update
title_zh: 选择性可信度受限信念更新
authors:
- Theofanis Aravanis
- Costas D. Koutras
affiliations:
- University of the Peloponnese
- American University of the Middle East
arxiv_id: '2607.28523'
url: https://arxiv.org/abs/2607.28523
pdf_url: https://arxiv.org/pdf/2607.28523
published: '2026-07-30'
collected: '2026-08-02'
category: Agent
direction: Agent 信念更新逻辑优化
tags:
- Belief Update
- Agent Reasoning
- Knowledge Representation
- Non-Prioritized Belief Change
- Selective Acceptance
one_liner: 提出支持源依赖选择性接受的可信度受限信念更新框架，兼容两类经典信念更新范式
practical_value: '- 多Agent导购、智能客服的信念更新模块可借鉴选择性接受思路，对用户多轮输入、第三方上下文按源可信度做部分采信，而非全接受/全拒绝

  - Agent侧用户偏好更新逻辑可参考最大一致性保持算子设计，在输入存在冲突时优先保留最大信息量的可信片段，避免偏好模型频繁震荡

  - 跨域推荐的异源知识融合场景可复用源依赖转换逻辑，对异域输入做适配裁剪后再融入本地偏好模型，降低无效信息干扰'
score: 4
source: arxiv-cs.AI
depth: abstract
---

### 动机
现有可信度受限信念更新将认知输入视为不可分割整体，无法适配仅复合输入的部分内容可被采信的场景，经典Katsuno-Mendelzon（KM）更新也未考虑可信度约束的适配需求。
### 方法关键点
1. 选择性可信度受限信念更新框架针对每个源世界，先将原始认知输入转换为更弱的可信代理输入，再执行可信度受限的状态迁移；
2. 框架包含该类更新算子的语义与公理刻画，定义两类良构子类：一致性保持算子（原始输入一致时转换后输入对源世界可信）、最大一致性保持算子（额外要求代理输入是原始输入可信推论中信息量最大的）。
### 关键结果
该框架是现有信念更新范式的超集：原有可信度受限更新是其特例，移除可信度约束且转换函数为恒等映射时可退化为经典KM更新，表达能力严格优于现有方案。
