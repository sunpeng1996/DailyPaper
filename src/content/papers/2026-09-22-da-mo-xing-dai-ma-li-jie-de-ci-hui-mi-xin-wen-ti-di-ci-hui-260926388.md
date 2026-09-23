---
title: 'On the Lexical Superstition of Large Language Models for Code Comprehension:
  Re-evaluation on Code of Low Lexical Quality'
title_zh: 大模型代码理解的词汇迷信问题：低词汇质量代码下的重评估
authors:
- Xin Shen
- San-Zhuo Xi
- Yali Du
- Ming Li
affiliations:
- Nanjing University, China
arxiv_id: '2609.26388'
url: https://arxiv.org/abs/2609.26388
pdf_url: https://arxiv.org/pdf/2609.26388
published: '2026-09-22'
collected: '2026-09-23'
category: LLM
direction: 大模型鲁棒性 · 代码理解任务
tags:
- LLM
- Code Comprehension
- Model Robustness
- Lexical Cue
- Evaluation
one_liner: 提出语义保留的标识符重命名框架Face/Off，验证大模型代码理解中普遍存在过度依赖词汇线索的系统性漏洞
practical_value: '- 开发Agent代码工具（如运维Agent、报表生成Agent）时需额外增加语义校验模块，避免LLM因标识符歧义输出错误结果

  - 训练垂直领域LLM（如电商业务规则解析模型）时，可加入词汇混淆的扩增样本，降低模型对表层词汇的过度依赖，提升鲁棒性

  - 做结构化规则/代码片段的RAG召回时，需在词汇匹配之外补充结构语义匹配通路，避免因表层词汇差异漏召回相关上下文'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
当前LLM广泛落地于代码理解、生成类任务，天然代码中的标识符词汇信息虽具备统计相关性，但并不完全可靠，现有模型对词汇线索、程序结构的权重分配是否合理尚未被验证。
### 方法关键点
设计语义保持的标识符重命名框架Face/Off，覆盖标识符信息擦除、误导性命名等多组渐进式命名条件，在多个主流LLM、多类代码理解任务上开展评估，同时引入prompt优化、微调等干预手段验证问题的顽固性。
### 关键结果
1. 所有被测模型均存在普遍的词汇过度依赖问题：移除标识符信息或加入误导性命名时性能明显下降，输出常被误导性名称的语义引导
2. 该问题在prompt优化、微调等常规干预手段下依然存在，属于模型的系统性缺陷
3. 仅当答案无需目标标识符即可局部推导时，命名带来的负面影响才会显著缩小
