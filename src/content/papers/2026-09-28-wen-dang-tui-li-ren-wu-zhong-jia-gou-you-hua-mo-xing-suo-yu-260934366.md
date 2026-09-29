---
title: When Harness Beats Scale, and When Reading Beats Both
title_zh: 文档推理任务中架构优化、模型缩放与输入质量的效果对比研究
authors:
- Ivan Bondarenko
- Nikolay O. Nikitin
affiliations:
- Novosibirsk State University
- ITMO University
arxiv_id: '2609.34366'
url: https://arxiv.org/abs/2609.34366
pdf_url: https://arxiv.org/pdf/2609.34366
published: '2026-09-28'
collected: '2026-09-29'
category: LLM
direction: LLM应用架构 · 性能优化实践
tags:
- PoT
- RAG
- Structured Output
- Model Scaling
- Document Reasoning
- OCR
one_liner: 验证工具链加持的中小模型可追平大模型性能，输入质量决定系统最终性能上限
practical_value: '- 中小模型经过结构化输出训练（JSON、格式约束）后搭配PoT、工具链，可在垂直任务上追平2-3倍参数的大模型，大幅降低推理成本，适合电商属性抽取、订单对账、客服问答等场景

  - 上线RAG/Agent系统前必须做输入分布校验：比如电商用户上传图片OCR质量、爬虫脏数据、商品详情页格式等，输入质量波动带来的性能损失远大于架构优化收益，避免验证集效果好线上崩的问题

  - GraphRAG不要盲目注入全量图谱上下文，仅取和query最相关的top-k实体注入prompt性价比最高，全量图谱反而会降低小模型性能，可复用在商品知识图谱增强推荐/搜索prompt的场景

  - 需严格格式输出的场景（推荐理由结构化生成、广告文案打标、工单自动分类）优先选经过结构化输出训练的小模型，格式准确率远高于未训练的大模型，降低后处理成本'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
当前LLM落地普遍依赖堆大参数提升效果，忽略架构优化的性价比，且训练/验证与真实场景的输入分布偏移常导致线上性能雪崩，亟需明确模型缩放、架构设计、输入质量三者的贡献优先级，为垂直场景降本增效提供指引。

### 方法关键点
- 推理pipeline：混合块检索（稠密+稀疏向量RRF融合，重排序取top3）→ 块级知识蒸馏取top3相关实体增强prompt → PoT生成代码沙箱执行得结果 → 自一致性采样k=5投票
- 控制变量实验：对比7B/27B/72B不同规模模型、有无结构化输出训练、有无工具链加持的效果差异
- 输入退化校验：人工生成带水印的低分辨率扫描PDF，模拟测试集输入偏移，定位性能退化根因

### 关键结果数字
- 干净标注集上，结构化训练的7B模型加PoT后联合准确率提升0.282；27B模型加完整工具链效果追平72B（0.884 vs 0.873），参数仅为1/2.7，碳排放降75%
- 测试集为带水印扫描件时，系统性能从验证集的0.853骤降至13.58%，输入质量导致超80%的性能损失
- 结构化训练的7B模型JSON格式准确率达98.1%，远高于原生7B的30.2%，是工具链生效的核心前提

### 最值得记住的一句话
输入质量的优先级高于架构优化，架构优化的优先级高于模型参数缩放
