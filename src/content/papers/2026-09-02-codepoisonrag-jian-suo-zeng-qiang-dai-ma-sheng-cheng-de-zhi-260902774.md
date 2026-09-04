---
title: 'CodePoisonRAG: Knowledge Poisoning Attacks on Retrieval-Augmented Code Generation'
title_zh: CodePoisonRAG：检索增强代码生成的知识投毒攻击
authors:
- Varun Gadey
- Ziad Marey
- Alexandra Dmitrienko
affiliations:
- University of Duisburg-Essen, Germany
arxiv_id: '2609.02774'
url: https://arxiv.org/abs/2609.02774
pdf_url: https://arxiv.org/pdf/2609.02774
published: '2026-09-02'
collected: '2026-09-04'
category: RAG
direction: RAG安全 · 知识投毒攻击研究
tags:
- RAG
- Knowledge Poisoning
- Code Generation
- LLM Security
- Retrieval Augmented Generation
one_liner: 提出黑盒场景下RAG代码生成定向投毒框架，0.7%投毒比例即可实现80%+攻击成功率
practical_value: '- 自建业务RAG知识库时需增加外部来源语料的安全校验，重点排查带虚假合规/安全标注的低占比恶意语料

  - 对召回Top-K的RAG片段做交叉一致性校验，避免单条恶意语料主导生成结果，可大幅降低投毒攻击风险

  - 代码生成、商品文案生成、活动规则生成等强合规RAG场景，需额外增加生成结果的规则校验层'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
检索增强代码生成（RACG）依赖外部知识库降本提效，但现有研究仅关注利用已有漏洞样本泛化投毒，未覆盖黑盒场景下攻击者构造单条任务匹配语料实现定向弱点注入的攻击路径，RAG的外部知识信任边界风险被低估。
### 方法关键点
提出CodePoisonRAG定向上游知识投毒框架，攻击链包含两个核心模块：1）CWE特定漏洞注入：在保留任务对齐性的前提下嵌入指定的源到汇漏洞流；2）语义错标：添加虚假安全声明但不修复漏洞。攻击者无需获取受害方知识库、召回排序逻辑、prompt等任何信息，单任务仅需注入1条恶意语料即可实现攻击。
### 关键结果数字
构造覆盖Java、C共10类CWE的85条恶意语料，语料投毒占比仅0.7%，所有恶意语料均进入对应查询Top3召回结果，攻击成功率达0.8~0.93；对抗注入安全知识的CodeGuarder防御机制时，攻击成功率仍可达0.4~0.71。
