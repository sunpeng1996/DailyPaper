---
title: 'STEB: Style Text Embedding Benchmark'
title_zh: STEB：风格文本嵌入评测基准
authors:
- Rafael Rivera Soto
- Anna Wegmann
- Cristina Aggazzotti
affiliations:
- Johns Hopkins University
- Utrecht University
arxiv_id: '2606.31741'
url: https://arxiv.org/abs/2606.31741
pdf_url: https://arxiv.org/pdf/2606.31741
published: '2026-06-30'
collected: '2026-07-02'
category: Eval
direction: 文本风格嵌入 · 标准化评测基准
tags:
- Text Embedding
- Style Embedding
- Evaluation Benchmark
- Open Dataset
- NLP
one_liner: 推出覆盖7语言96个数据集的开源风格文本嵌入基准STEB，标准化风格嵌入评测体系
practical_value: '- 电商文案风格匹配、达人内容风格召回场景不要直接用通用语义嵌入，需单独选型/训练风格嵌入模型

  - 自研风格嵌入模型时可直接复用STEB的数据集与评测流程，避免自建测试集的碎片化问题

  - 做AI生成电商文案风格校验、虚假AI评论识别场景时，可参考STEB覆盖的任务与评测指标'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
通用语义嵌入已有MTEB作为统一评测标准，但风格嵌入领域长期缺少统一评测体系，不同工作的任务、数据集、预处理规则差异极大，评测结果难以横向对比。
### 方法关键点
推出开源STEB基准，覆盖7种语言共96个数据集，包含作者身份验证、作者检索、AI文本检测、语言特征探测等多类风格相关任务，统一了评测预处理、编码规则等全流程协议。
### 关键结果
1. 通用语义嵌入在风格类任务上表现普遍极差，即使是MTEB排名Top5的Qwen3-Embedding-8B，在STEB上排名也很低
2. 暂未发现能在所有风格任务上取得全局最优的风格嵌入模型，需根据业务场景选型
