---
title: 'AILQA: Evaluating AI-Driven Legal Question Answering Systems for the Indian
  Legal System'
title_zh: 面向印度法律体系的AI驱动法律问答系统AILQA评估研究
authors:
- Shubham Kumar Nigam
- Shubham Kumar Mishra
- Noel Shallum
- Kripabandhu Ghosh
- Arnab Bhattacharya
affiliations:
- Indian Institute of Technology Kanpur
- Symbiosis Law School Pune
- Indian Institute of Science Education and Research Kolkata
- University of Birmingham Dubai
arxiv_id: '2607.18825'
url: https://arxiv.org/abs/2607.18825
pdf_url: https://arxiv.org/pdf/2607.18825
published: '2026-07-21'
collected: '2026-07-26'
category: Eval
direction: 垂直领域RAG问答系统评估
tags:
- RAG
- LLM
- DomainQA
- Evaluation
- Hallucination
one_liner: 面向印度法律场景构建AILQA问答系统，验证RAG效果并搭建标准化评估基准
practical_value: '- 垂直领域（如电商合规咨询、商品客服问答）RAG系统落地可复用「量化词汇/语义指标+行业专家人工反馈」的双层评估范式，平衡效率与专业准确性

  - 复杂垂直场景下LLM问答类应用可优先验证RAG范式增益，其关联支撑细节补充能力可显著提升用户满意度

  - 垂直领域LLM系统性能验证可引入行业标准化考试作为benchmark（如电商合规考、品类知识考），量化结果更具业务参考性'
score: 4
source: arxiv-cs.IR
depth: abstract
---

### 动机
印度法律文本结构复杂、规则分散，现有通用问答系统适配性差，缺乏针对本土法律场景的高可靠问答方案与标准化评估体系。
### 方法关键点
构建AILQA法律问答系统，融合多类embedding模型与主流LLM，采用RAG范式召回精准法律文本上下文优化生成质量；评估层设计三层机制：词汇+语义量化指标评估、法律专家人工标注校验、全印度律师资格考试（AIBE）标准化测试。
### 关键结果
RAG范式可显著提升复杂垂直领域问答质量；部分AI生成回答在给定评估规则下评分优于现有参考回答，核心优势为包含更精准的关联支撑细节；明确精准上下文输入、幻觉抑制是垂直领域LLM系统落地的核心瓶颈。
