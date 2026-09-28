---
title: 'Towards Mitigating Fabricated Consensus: The Active Provenance Gate for Multi-Agent
  Debate Synthesis'
title_zh: 主动来源门：缓解多智能体辩论合成中的虚构共识问题
authors:
- Jakub Masłowski
- Jarosław A. Chudziak
affiliations:
- Warsaw University of Technology
arxiv_id: '2609.31422'
url: https://arxiv.org/abs/2609.31422
pdf_url: https://arxiv.org/pdf/2609.31422
published: '2026-09-25'
collected: '2026-09-28'
category: MultiAgent
direction: 多智体辩论 · 共识合成校验
tags:
- Multi-Agent Debate
- Hallucination Mitigation
- Natural Language Inference
- Provenance Fidelity
- Consensus Synthesis
one_liner: 为多智能体辩论增设主动来源验证层，阻断虚构共识，输出可溯源结果或明确分歧报告
practical_value: '- 多Agent业务决策链路（如广告投放策略生成、大促资源分配讨论）可新增APG式后置校验层，用NLI逐句校验输出结果是否匹配前置讨论、RAG/KB业务数据，从流程上阻断无依据的幻觉输出

  - 校验层可复用不对称架构：生成侧用低成本轻量LLM，校验侧用强推理LLM，对比同模型自校验可降低60%+的错误通过率，兼顾成本与可靠性

  - 高风险业务场景（如客诉处理方案生成、商品合规审核）可复用「校验不通过则输出结构化分歧报告」的设计，不需要强行生成流畅结果，实测用户对明确失败的信任度远高于虚假共识

  - 可直接复用Provenance Fidelity（PF）指标量化生成结果与输入证据的匹配度，替代模糊的人工一致性校验，提升评估效率'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
多智能体辩论（MAD）系统已被广泛用于复杂决策链路，但最终合成阶段存在结构性缺陷：为了输出流畅的共识结论，合成模型会刻意抹平未解决的冲突，生成完全无辩论历史支撑的虚构共识，现有溯源框架仅做被动日志留痕，无法实时阻断这类幻觉，高风险场景下会严重误导使用者，引发决策失误。
### 方法关键点
- 提出**Active Provenance Gate (APG)** 作为辩论结束后的独立校验层，将所有辩论日志、KG/RAG证据整合为封闭证据集，要求生成结果的所有主张必须可溯源到该证据集。
- 采用不对称Proposer-Auditor架构：轻量LLM负责生成候选共识，强推理LLM作为NLI审计器逐句校验，计算**Provenance Fidelity (PF)** 指标（即被证据支撑的语句占总输出的比例）。
- 设置硬校验阈值`PF≥0.95`，未达阈值则触发最多3轮定向自修复，仍不通过则强制输出结构化`Divergence Report`，明确列示未解决冲突和对应来源。
### 关键实验
在90条带知识标注的危机模拟辩论轨迹上测试：基线合成方案高冲突场景下PF仅0.288，加APG自修复后PF提升至0.617，75%的高冲突未达标样本会触发分歧报告；用户调研显示75.8%的参与者在高冲突场景下更偏好APG的明确分歧输出，尽管基线结果流畅度评分高66.7%；不对称校验架构比同模型自校验的错误通过率降低63.3%。
### 核心结论
高风险决策场景下，用户对明确的系统失败的信任度远高于流畅但无依据的虚构共识，溯源不能只做被动日志，要作为主动控制层前置到结果发布前。
