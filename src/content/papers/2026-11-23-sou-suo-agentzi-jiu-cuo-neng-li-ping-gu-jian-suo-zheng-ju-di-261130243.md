---
title: Can Search Agents Correct Their Own Errors? Evaluating Retrieval, Evidence
  Delivery, and Answer Completion
title_zh: 搜索Agent自纠错能力评估：检索、证据传递与答案补全故障诊断
authors:
- Venkata Pagadala
- K. Rajasekhara Rao
- Pratyay Ganguly
affiliations:
- KL University
- Indian Institute of Technology Kharagpur
arxiv_id: '2611.30243'
url: https://arxiv.org/abs/2611.30243
pdf_url: https://arxiv.org/pdf/2611.30243
published: '2026-11-23'
collected: '2026-11-24'
category: Agent
direction: 搜索Agent · 故障诊断与效果评估
tags:
- Search Agent
- RAG
- Evaluation
- Error Correction
- Retrieval
one_liner: 设计分层干预评估框架，定位搜索Agent自纠错失败的检索、传递、利用、完成四类故障
practical_value: '- 排查电商导购/客服Agent错误时可复用分层诊断逻辑：先直接给模型注入正确证据，若能答对则是检索/排序问题，若答错则是模型知识冲突/历史记忆影响问题，再针对性优化

  - 做Agent交互设计时，若用户质疑之前的回答，不要保留历史错误答案在上下文，触发强制重搜并直接将高置信证据片段注入上下文，可大幅提升纠错成功率

  - 不要盲目提升搜索召回深度：返回结果从5条涨到20条仅提升8.6pp的gold recall但准确率无变化，优先优化高相关结果的预览信息、强制关键片段自动注入上下文性价比更高

  - 评估搜索Agent效果时，除准确率外还要增加拒答率、超时率、错误答案复用率三个指标，避免只看准确率遗漏输出环节的故障'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
搜索Agent出错后常无法自行修正，现有评估仅能输出最终准确率，无法定位故障出在检索、证据读取、知识冲突处理还是答案输出环节，导致优化缺乏针对性。

### 方法关键点
- 基于BrowseComp-Plus多跳问答数据集，设计分层干预实验：先获取模型的错误闭卷答案作为历史错误hint，再分别在检索排序、上下文注入两个环节做控制变量干预
- 覆盖4款开源大模型（Qwen3.5-35B、Nemotron-30B、Gemma-31B、gpt-oss-120B），709个问题、26665个测试条件，将纠错失败划分为检索失败、证据传递失败、证据利用失败、答案补全失败四类

### 关键结果
- 上下文已包含正确证据时，历史自信错误回答使Nemotron准确率下降16.1pp，若用户坚持错误答案，准确率进一步下降32.9pp；gpt-oss面对用户坚持时更多选择拒答而非重复错误
- 将gold页面放在搜索结果首位时，多数模型仍不会主动点开，直接注入关键证据比gold页前置的准确率高34.7pp（Qwen3.5）、18pp（Nemotron）
- 召回结果从5条增至20条，gold recall提升8.6pp但准确率几乎无变化，Nemotron有37%的场景在已获得正确证据时仍耗尽搜索预算不输出答案

### 核心结论
搜索Agent的纠错能力是端到端属性，仅优化检索/排序单一环节无法解决所有错误，必须通过分层干预定位具体故障环节再针对性优化
