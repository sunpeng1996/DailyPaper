---
title: 'When Local Definitions Are Missing: Stable Errors in Language Models'
title_zh: 大模型缺失局部定义时的稳定错误问题研究
authors:
- Zengqing Wu
- Chuan Xiao
affiliations:
- University of Osaka
- Nagoya University
arxiv_id: '2611.15597'
url: https://arxiv.org/abs/2611.15597
pdf_url: https://arxiv.org/pdf/2611.15597
published: '2026-11-11'
collected: '2026-11-13'
category: LLM
direction: 大模型鲁棒性 · 错误诊断
tags:
- LLM Error Detection
- Hallucination
- Local Definition
- Knowledge Conflict
- Proxy Model
one_liner: 揭示重定义常见词引发的大模型稳定错误现象，提出小模型离线预判高风险问题的方案
practical_value: '- 做垂直场景RAG系统时，必须提前抽取文档/商品/活动的局部专有定义（如电商大促专属术语、社区黑话）存入知识库，不能依赖大模型参数知识，实测仅靠参数知识准确率仅提升1%

  - 大模型输出的置信度、多轮采样一致性对重定义术语导致的错误识别能力接近随机（AUROC仅0.46~0.56），不能用这两个信号作为RAG fallback的触发条件

  - 可使用7B级小模型配合已有标注库离线筛选高风险问答对，用于评测集构建，对大模型错误的排序AUROC可达0.85，大幅降低人工标注成本

  - 电商/广告文案生成时要规避使用被重定义的常见词，否则大模型生成内容易出现稳定常识错误且难以自检'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
当前大模型广泛应用于合同审核、技术手册问答、社区内容理解等场景，这类场景常给常见词赋予特殊局部定义，若RAG召回片段未包含对应定义，大模型会误用通用语义给出看似正确的错误答案，且现有自检信号难以识别这类问题，严重影响垂直场景大模型应用的可靠性。

### 方法关键点
- 构建4类多选题数据集：合成词汇集、商业合同CUAD、35个Reddit社区术语库、去中心化交易所文档，覆盖重定义常见词、生造词、正常含义词三类术语
- 测试3款主流大模型（GPT-5.6-terra、GPT-6-astra、DeepSeek Flash）在有/无局部定义时的回答表现，验证多轮采样一致性、置信度等自检信号的错误识别能力
- 用0.5B~14B参数的小模型作为proxy，基于答案key离线预判大模型的高风险错误问题

### 关键结果
- 无局部定义时，重定义常见词的错误率最高，DeepSeek V4 Flash达44%，是正常含义词的3倍；41%的错误为稳定错误，多次采样返回相同错误答案，多数投票仅能修正38%的错误
- 置信度、采样一致性对重定义词错误的识别AUROC仅0.46~0.56，接近随机水平；输入源定义后，合成数据集准确率从70%提升到97%，但用大模型自身参数知识生成的释义仅提升到71%
- 7B参数Qwen2.5模型对大模型错误的排序AUROC可达0.85，效果远优于词频、稀有度等传统特征（最高AUROC仅0.63）

最值得记住的结论：大模型能很好地遵循给定的局部定义，但缺少定义时几乎无法自检这类错误，垂直场景RAG系统必须优先保障专有定义的召回，不能依赖大模型的参数知识和自校验信号。
