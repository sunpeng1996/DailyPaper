---
title: 'Reading Beyond OCR Noise: Robust Cross-Lingual RAG for Legislative Archives'
title_zh: 适配OCR噪声的多语言立法档案鲁棒跨语言RAG系统
authors:
- Radha Krishna Deshpande
- Ajoy Mondal
- Akash Manna
- C V Jawahar
affiliations:
- International Institute of Information Technology, Hyderabad
arxiv_id: '2610.35240'
url: https://arxiv.org/abs/2610.35240
pdf_url: https://arxiv.org/pdf/2610.35240
published: '2026-10-26'
collected: '2026-10-27'
category: RAG
direction: 跨语言RAG · 抗OCR噪声优化
tags:
- RAG
- Agentic RAG
- Cross-lingual
- OCR
- Document Retrieval
one_liner: 融合布局感知OCR与Agentic RAG实现多语言历史档案抗噪声跨语言问答
practical_value: '- 处理多语言、OCR噪声强的UGC内容、历史商品评论、老旧合同等非结构化文本时，可复用Agentic RAG的「上下文充分性校验+迭代查询改写」逻辑，降低文本噪声对检索准确性的负面影响；

  - 跨语言检索场景优先选用BGE-M3这类原生多语言嵌入模型，省略中间翻译步骤，既减少语义偏差又降低链路复杂度；

  - 存在印刷/识别噪声的语料检索任务可配置最多3轮的查询重写迭代，在可控 latency 下可实现Answer F1近2倍提升，平衡效果与性能'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
历史多语言立法档案普遍存在印刷退化、多列复杂布局、多脚本混合等问题，OCR识别误差会直接传播到下游检索、问答环节，传统单步RAG、纯文本检索方案在这类噪声语料上表现极差，亟需端到端的抗噪声跨语言检索生成框架。

### 方法关键点
- 离线处理：融合微调YOLO布局分割模型+CRNN多语言OCR完成档案文本提取，采用BGE-M3生成原生多语言文本嵌入存入向量数据库，无中间翻译步骤，避免语义损失；
- 在线Agentic检索流：先召回Top-k相关上下文，用LLM校验上下文充分性，不满足阈值则结合OCR噪声先验改写查询后重检索，最多迭代3轮；
- 生成阶段：严格基于校验后的上下文输出用户原生语言回答，最大化事实 grounding 减少幻觉。

### 关键结果
在20万页旁遮普立法档案数据集（覆盖1950-2024年，包含印地语、旁遮普语、英语混合脚本）上测试：
- 对比标准BGE-M3基线，MRR@1从0.775提升至0.810，Hit@3从0.900提升至0.925；
- 3轮迭代Agentic Loop对比单步无改写检索，Answer F1从0.18提升至0.35，实现近2倍提升。

### 核心结论
OCR噪声等上游文本提取误差对RAG效果的影响远大于嵌入模型的差异，通过轻量Agentic迭代查询重写可低成本大幅提升噪声语料下的RAG表现
