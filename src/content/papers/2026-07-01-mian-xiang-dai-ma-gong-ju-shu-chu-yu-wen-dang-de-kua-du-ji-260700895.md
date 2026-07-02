---
title: 'Beyond Document Grounding: Span-Level Hallucination Detection over Code, Tool
  Output, and Documents'
title_zh: 面向代码、工具输出与文档的跨度级幻觉检测
authors:
- Ádám Kovács
- Bowei He
- Xue Liu
- István Boros
- Szilveszter Tóth
- Gábor Recski
affiliations:
- KR Labs
- MBZUAI
- McGill University
- TU Wien
arxiv_id: '2607.00895'
url: https://arxiv.org/abs/2607.00895
pdf_url: https://arxiv.org/pdf/2607.00895
published: '2026-07-01'
collected: '2026-07-02'
category: RAG
direction: RAG幻觉检测 · 跨结构化输入
tags:
- Hallucination Detection
- RAG
- Span-level Detection
- Code Agent
- Benchmark
- Structured Data
one_liner: 构建覆盖代码/工具输出/文档的统一跨度级幻觉检测基准，微调2B Qwen实现跨场景SOTA检测效果
practical_value: '- 业务RAG系统的幻觉校验可复用编辑式幻觉注入方法，自动生成带精准字符级标注的训练样本，大幅降低人工标注成本

  - 跨异构输入（商品参数、营销文案、工具调用结果等）的幻觉检测可参考统一训练框架，2B级小模型SFT效果比零样本大模型高3倍以上，推理成本更低

  - 代码/结构化数据类Agent的输出校验可直接复用开源的LettuceDetect-Qwen-2B模型，或基于其范式微调适配电商文案、商品参数校验等业务场景

  - 跨度级幻觉输出可直接定位错误内容并替换，适合接入业务RAG的自动纠错链路，减少人工审核成本'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有RAG幻觉检测方案大多仅适配自然语言文档场景，但实际落地的RAG/Agent系统常需处理代码、工具输出、结构化表格、Markdown文档等异构输入，缺乏统一的跨度级检测基准和适配模型，零样本大模型在结构化场景下检测准确率极低，无法满足业务校验需求。

### 方法关键点
- 数据集采用编辑式注入构建：从正确的接地答案出发，仅做局部小范围修改注入幻觉，自动获取精准字符级标注，覆盖代码、工具输出、ACL论文、README、维基百科5类结构化/非结构化场景，新增74285个样本，同时兼容RAGTruth、PsiloQA等现有基准。
- 针对代码场景补充reference grounding：自动补全截断上下文缺失的依赖定义、第三方API签名，避免误判合法引用为幻觉。
- 分别微调Qwen3.5-2B生成式检测器和mmBERT-base编码器，统一适配所有场景，生成式检测器直接输出带分类的幻觉跨度JSON，无需额外后处理。

### 关键结果
- 统一测试集上，LettuceDetect-Qwen-2B达到0.689 span-F1，其中代码Agent场景span-F1达0.60，远超原有LettuceDetect-large（0.17）和最强零样本LLM法官（最高0.22）。
- 自然语言RAG基准上表现依然具备竞争力：RAGTruth example-F1达81.8，PsiloQA英文IoU达0.724，接近甚至超过专用检测模型。

最值得记住的一句话：针对异构结构化输入的幻觉检测，专用小模型微调的效果和成本表现远优于通用大模型零样本判断。
