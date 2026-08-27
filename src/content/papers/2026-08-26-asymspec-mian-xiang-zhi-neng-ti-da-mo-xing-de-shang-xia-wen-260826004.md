---
title: 'AsymSpec: Context-Asymmetric Speculative Decoding for Agentic LLMs'
title_zh: AsymSpec：面向智能体大模型的上下文非对称投机解码框架
authors:
- Sheng Liang
- Yongyue Zhang
- Nathanael Brian
- Hang Lv
- Hao Wang
- Chen Zhang
- Yong Liu
affiliations:
- Huawei Technologies Co., Ltd.
- University of Science and Technology of China
arxiv_id: '2608.26004'
url: https://arxiv.org/abs/2608.26004
pdf_url: https://arxiv.org/pdf/2608.26004
published: '2026-08-26'
collected: '2026-08-27'
category: LLM
direction: 大模型推理优化 · 投机解码
tags:
- Speculative Decoding
- LLM Inference
- Context Compression
- Agentic LLM
- Logit Fusion
one_liner: 打破投机解码上下文对称约束，轻量全上下文草稿模型引导压缩上下文大模型推理，兼顾精度与效率
practical_value: '- 电商智能客服、导购Agent、RAG问答机器人等长上下文场景可直接复用该框架：小模型读全量会话/检索上下文，大模型跑压缩后上下文，可降低30%~80%推理成本，同时保留约90%全量上下文精度

  - 对比δ-fusion的思路可迁移：同一小模型分别跑全量和压缩上下文得到的logit差作为上下文增益信号，注入大模型logit的trick，可复用在所有需要补全压缩上下文信息的场景

  - 无参数CDA门无需逐场景调参，可直接替换现有投机解码的固定接受阈值，在上下文压缩场景下提升草稿接受率，工程改造成本极低

  - 跨模态扩展思路可复用：电商多模态导购Agent可用小多模态模型读原图，大文本模型跑图片摘要，无需改造大模型即可低成本支撑多模态推理需求'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
当前Agent LLM在多轮交互、RAG检索、工具调用流程中会持续累积上下文，推理延迟随上下文长度呈超线性增长，成为业务落地的核心瓶颈。常规上下文压缩方案会丢失关键细节导致精度下降，而传统Speculative Decoding要求草稿模型与验证模型读取完全相同的上下文，无法打破「全上下文高成本、压缩上下文低精度」的刚性trade-off。

### 方法关键点
- 非对称上下文访问：轻量草稿模型读取全量上下文xfull，大参数量验证模型仅读取压缩后的上下文xcomp，核心计算开销由大模型侧转移到轻量模型侧
- 对比δ-fusion机制：同一草稿模型分别运行在全量和压缩上下文上，将两组输出logits相减得到纯上下文增益信号δ，注入验证模型的logit空间，引导输出向全上下文结果对齐
- 无参数CDA接受门：基于全量与压缩上下文输出分布的Jensen–Shannon散度动态调整草稿接受阈值，上下文差异越大阈值越宽松，无需逐场景调参即可保证高接受率
- 天然跨模态兼容：草稿模型可替换为多模态模型读取原始图像等输入，验证模型仍为纯文本模型，无需改造大模型即可支撑多模态推理需求

### 关键实验结果
在长上下文多跳QA、多轮指令遵循、工具使用、多模态推理4类Agent能力，以及GAIA、SimpleQA 2个端到端Agent基准上测试，对比全上下文大模型、压缩上下文大模型、传统Speculative Decoding等基线：平均恢复90%的全上下文精度，文本任务仅需0.2~0.3倍全上下文计算量，吞吐量提升1.3~1.7倍，压缩程度越高精度恢复效果越显著。

### 核心洞见
上下文压缩损失无需通过大模型重读全量上下文修复，仅需轻量模型提取全上下文增益信号引导大模型输出，即可在极低额外成本下大幅抵消精度损失。
