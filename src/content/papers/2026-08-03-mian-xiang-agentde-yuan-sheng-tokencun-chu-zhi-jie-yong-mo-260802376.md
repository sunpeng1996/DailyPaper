---
title: 'Token-Native Storage: Read and Write in your Agent''s Language'
title_zh: 面向Agent的原生Token存储：直接用模型原生Token ID读写文本
authors:
- Kumar Shivendu
affiliations:
- Qdrant
arxiv_id: '2608.02376'
url: https://arxiv.org/abs/2608.02376
pdf_url: https://arxiv.org/pdf/2608.02376
published: '2026-08-03'
collected: '2026-08-04'
category: Agent
direction: Agent系统 · 原生Token存储优化
tags:
- Token-Native Storage
- BPE
- RAG
- Agent Infrastructure
- Text Compression
one_liner: 提出以BPE Token ID为原生存储格式，大幅降低Agent/RAG系统的文本存储成本与读写延迟
practical_value: '- RAG/Agent系统可直接落地原生Token存储：将召回的商品详情、用户对话、知识库文本预先以业务常用LLM的Token
  ID存储，读取时跳过重复Token化，单512Token chunk读延迟从~235μs降到0.4~25μs，大幅降低RAG链路耗时。

  - 低延迟场景优先用+freq压缩方案：将BPE Token ID按业务语料频率重排后用streamvbyte编码，仅损失20%压缩率即可获得比ANS熵编码快7倍的解码速度，适合电商搜索推荐、实时Agent对话等低延迟场景。

  - 大规模文本存储成本优化：电商大促话术、商品评论、检索知识库等大体积文本场景，采用原生Token存储+ANS编码可获得3.3x以上的压缩比，大幅降低SSD存储与跨节点传输成本。

  - 全链路Token化优化：统一Embedder、Reranker、Agent LLM的Tokenizer，全链路直接传递Token ID，避免多环节重复Token化计算，端到端链路延迟可降低一个数量级。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

## 动机
当前数据库/搜索引擎默认以UTF-8格式存储文本，但Agent、Embedder、Reranker等AI组件的原生处理单元是BPE Token ID，每次读写都要重复做字符与Token ID的转换，不仅存储效率低，还带来极高的Token化开销——RAG场景下单查询往往需要处理上百个文本Chunk，Token化耗时占比极高，成为链路瓶颈。

## 方法关键点
- 原生存储设计：直接以业务常用LLM的BPE Token ID为文本的原生存储格式，仅在人机交互边界做一次Token化/反Token化，AI组件读写直接传递Token ID，跳过重复转换。
- 分级压缩方案：可选两种压缩模式，ANS熵编码压缩比最高；Token ID按语料频率重排后用streamvbyte编码（+freq方案），解码速度比ANS快7倍，是低延迟场景首选。
- 兼容接口：存储层新增Token类型字段，同时支持字符串、Token ID写入，读取可指定返回文本或Token ID，不影响原有业务逻辑。

## 关键实验
基于C4英文、Python代码、印地语维基百科三个数据集，对比LZ4、gzip、zstd等字节级压缩方案：
- 压缩比：r50k Tokenizer无压缩就比UTF-8小2.25x，+ANS编码可达3.3x，+freq方案也可达2.6x，均超过普通zstd压缩效果。
- 延迟：单512Token Chunk读延迟，UTF-8存储需~235μs（解压+Token化），原生Token存储最低0.4μs，+freq方案仅4μs，最快提速600x。
- 成本：10亿条1000词文档用r50k+ANS存储，比UTF-8节省4.2TB SSD空间，每月节省约336美元存储成本。

> 最值得记住的话：当AI成为存储系统的主要读写主体时，存储格式应适配AI原生数据结构，而非人类的文本格式，转换成本仅需在人机交互边界发生。
