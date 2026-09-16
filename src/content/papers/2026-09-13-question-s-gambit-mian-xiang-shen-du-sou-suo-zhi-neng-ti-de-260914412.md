---
title: 'Question''s Gambit: The First Move Matters in Agentic Deep Search'
title_zh: Question's Gambit：面向深度搜索智能体的首步检索优化方法
authors:
- Radin Hamidi Rad
- Amin Bigdeli
- Negar Arabzadeh
- Sajad Ebrahimi
- Charles L. A. Clarke
- Benjamin C. M. Fung
- Ebrahim Bagheri
affiliations:
- University of Toronto
- Mila – Quebec AI Institute
- University of Waterloo
- University of California, Berkeley
- McGill University
arxiv_id: '2609.14412'
url: https://arxiv.org/abs/2609.14412
pdf_url: https://arxiv.org/pdf/2609.14412
published: '2026-09-13'
collected: '2026-09-16'
category: Agent
direction: Agent 深度搜索首步优化
tags:
- Agentic Search
- RAG
- Query Rewriting
- Retrieval Augmentation
- Multi-hop Reasoning
one_liner: 通过前置多线索拆分检索模块为搜索Agent暖启动，大幅提升复杂问答准确率
practical_value: '- 电商导购/客服Agent可复用多线索拆分检索逻辑，处理用户多约束商品查询（如「2000元内、续航10小时以上的轻薄本」），首步拆分每个约束分别检索再融合，避免单条查询漏召回

  - 搜索query改写模块可借鉴「线索+语料反馈扩展+原query拼接」的检索串构造方法，无需修改现有召回链路即可提升召回覆盖率

  - 多跳RAG系统可前置该首步模块，无需修改后续Agent推理逻辑即可提升回答准确率，工程落地成本极低

  - Agent预算优化可向首步检索倾斜，少量额外成本即可大幅减少后续无效搜索调用，整体ROI更高'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
当前深度搜索Agent处理多约束复杂查询时存在严重冷启动问题：首条查询通常混合多个约束导致召回覆盖不足，极易带偏后续推理轨迹，浪费有限的交互预算。现有优化多聚焦于Agent循环内的工具、推理能力增强，普遍忽略了首步检索对整个任务轨迹的决定性影响。

### 方法关键点
- 前置轻量首步检索模块Question's Gambit，完全不修改后续Agent推理逻辑和底层召回器，落地零侵入
- 线索拆分：用LLM将原query拆分为多个独立可检索的原子线索，每个线索对应一个明确的约束条件
- 线索级检索：每个线索先执行轻量化检索获取语料反馈，扩展为符合语料表述的搜索词，再拼接「线索+扩展词+原query」执行检索，得到每个线索的召回列表
- 融合重排：合并所有线索的召回结果去重，用通用reranker按原query排序，取Top-k作为Agent的暖启动上下文

### 关键实验
在BrowseComp-Plus（830条复杂多线索查询）上对比SOTA基线Pi-Serini：搭配GPT-5.5时回答准确率从83.1%提升至90.5%，绝对涨点7.4pp，校准误差从15.7降至7.58；搭配DeepSeek-v4-pro、GPT-5.4-mini均有稳定涨点，搜索调用量基本不变，仅增加单query约0.05美元的首步成本（占总预算<10%）。迁移到MultiHop-RAG数据集也有稳定小幅收益，无性能退化。

> 最值得记住的结论：Agentic搜索的效果不仅取决于循环内的推理和工具能力，首步检索的质量对整个轨迹走向的影响远大于预期
