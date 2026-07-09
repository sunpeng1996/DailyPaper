---
title: 'Co-LMLM: Continuous-Query Limited Memory Language Models'
title_zh: 连续查询有限内存语言模型Co-LMLM：低开销可编辑知识外部化框架
authors:
- Yair Feldman
- Linxi Zhao
- Nathan Godey
- Dongyoung Go
- Yilun Hua
- Kilian Q. Weinberger
- Jennifer J. Sun
- Yoav Artzi
affiliations:
- Cornell University
arxiv_id: '2607.07707'
url: https://arxiv.org/abs/2607.07707
pdf_url: https://arxiv.org/pdf/2607.07707
published: '2026-07-08'
collected: '2026-07-09'
category: LLM
direction: LLM知识外部化 · 有限内存模型优化
tags:
- LLM
- Knowledge-Externalization
- Contrastive-Learning
- Dense-Retrieval
- Limited-Memory
one_liner: 用模型隐状态生成连续向量查询，实现比结构化LMLM与原生LLM更高的事实精度与更低推理开销
practical_value: '- 高QPS的电商搜索/推荐场景可复用连续查询设计：直接从模型隐状态生成检索向量，无需解码文本查询，单检索开销从平均28ms降至2.2ms，同时规避文本查询的语义偏差问题

  - 大规模领域知识库标注可复用其蒸馏流水线：先用大模型标注小批量种子数据，再蒸馏轻量事实span标注器+问题生成器，低成本标注海量商品/用户/运营知识，降低人工标注成本

  - 电商合规场景可直接复用其可控知识编辑方案：无需重训模型，仅通过删除外部知识库对应条目即可实现下架商品、敏感信息等特定知识的完全遗忘，无模型效用损失'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有有限内存语言模型（LMLM）依赖关系型知识库，仅支持Wikipedia等结构化实体数据，检索需解码文本查询带来额外推理开销，无法适配通用大规模语料，知识表达灵活性与检索效率均存在瓶颈，难以满足高可控、低开销的事实性生成需求。

### 方法关键点
- 知识库采用向量key+自由文本事实span的键值对存储，替代原有的关系三元组，支持任意非结构化语料的知识外部化
- 推理时模型输出<FACT>特殊token后，直接取最后一层隐状态作为连续检索向量，无需解码文本查询，仅需1次前向传播即可完成查询生成
- 训练时联合优化next-token prediction损失与双向InfoNCE对比损失，事实span内的token不参与NTP损失计算，强制模型将知识存储到外部KB而非参数中
- 标注流水线先用前沿大模型标注小样本种子数据，蒸馏出轻量事实span标注器与问题生成器，可低成本处理数百亿tokens的通用语料

### 关键实验
在Wikipedia+FineWeb-Edu语料上训练135M、360M两个尺度模型，对比基线包括原生LLM、结构化REL-LMLM、开源SMOLLM2系列：360M尺度下困惑度比用40倍数据预训练的SMOLLM2-360M更低，SimpleQA得分达21.7，与gpt-4o-mini持平，高于Claude Sonnet 4.5；事实精度相比同尺度原生LLM平均提升20个百分点以上，检索开销相比文本查询LMLM降低13倍；知识遗忘仅需删除KB对应条目，无模型效用下降，显著优于训练式遗忘方案。

### 核心结论
在预训练阶段明确定义参数知识与外部知识的边界，用极低开销的连续向量检索替代文本查询，是平衡小模型事实性、可控性、推理效率的可行路径。
