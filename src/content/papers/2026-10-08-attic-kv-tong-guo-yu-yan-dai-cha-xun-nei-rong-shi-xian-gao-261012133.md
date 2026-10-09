---
title: 'Rehearse Everything, Remember Nothing: Attic-KV Rehearses What Will Be Read'
title_zh: Attic-KV：通过预演待查询内容实现高效无训练KV缓存压缩
authors:
- Zhiyun Shi
affiliations:
- Nanyang Technological University
arxiv_id: '2610.12133'
url: https://arxiv.org/abs/2610.12133
pdf_url: https://arxiv.org/pdf/2610.12133
published: '2026-10-08'
collected: '2026-10-09'
category: LLM
direction: LLM推理优化 · KV cache压缩
tags:
- KV_cache
- query_agnostic
- training_free
- long_context_LLM
- compression
one_liner: 提出无训练Attic-KV，通过自生成QA+自适应预演实现极低保留率下的高效KV缓存压缩
practical_value: '- RAG场景下的商品/文档KV预压缩可直接复用Attic-KV方案，3-5%的低保留率能让相同内存存储20倍的文档缓存，大幅降低电商搜索、客服Agent的RAG推理延迟和存储成本

  - 自生成QA预演的思路可迁移到电商商品语义关联建设，提前生成用户对商品的常见问题并关联到对应属性KV，提升搜索、问答场景下的召回准确率

  - 内容自适应的缓存分配逻辑可复用给推荐/广告系统的热点内容缓存，对高信息密度的内容（如商品参数、优惠规则）分配更多缓存资源，比固定比例缓存策略的命中率提升明显

  - Agent长对话上下文压缩可直接接入Attic-KV，无需训练就能在极低保留率下保留关键对话信息，降低多轮对话、规划推理的计算开销'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
RAG、共享prompt前缀、长对话等场景需要提前对KV缓存做查询无关的一次性压缩，现有全上下文预演的压缩方案在3-5%的高收益保留率区间效果极差，预算被大量无用的流畅文本占用，关键事实的KV条目留存率接近随机，无法兼顾压缩收益和推理效果。

### 方法关键点
- 遵循两个核心原则：预演未来会被读取的内容而非全上下文；预演长度随内容密度自适应调整而非固定比例
- 实现步骤：首先提取KeyDiff得分最高的锚点token，扩展到其所在句子作为基础预演内容；其次让模型自生成6个用户可能提出的QA对（答案强制引用原文）作为补充预演；最后按预演阶段的注意力得分保留Top r%的KV条目
- 无训练设计，可直接作为插件接入KVgrad、RestoreKV+等现有KV压缩框架，无需修改原有打分逻辑

### 关键结果
在RULER、LongBench、LooGLE三个长上下文基准上测试，对比KVzip+、KV2等主流方案：3%保留率下在RULER-4K得分73.4，超出KVzip+ 41.9分；5%保留率下接入RestoreKV+后，LooGLE短依赖问题ROUGE-L达40.9，比原生RestoreKV+高1.9；压缩速度比KVzip+快18%以上，优势随保留率降低持续扩大。

### 核心结论
KV缓存保留的内容由预演内容决定，而非评分方式，在存储预算紧张时，针对性预演关键事实比全量重读的效率高得多
