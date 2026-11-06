---
title: Reducing Representational Interference in Retrieval Embeddings with Trainable
  Prefix Tokens
title_zh: 基于可训练前缀Token的检索嵌入表征干扰抑制方法
authors:
- Seongtae Hong
- Youngjoon Jang
- Jungseob Lee
- Chanjun Park
- Heuiseok Lim
affiliations:
- Korea University
- Soongsil University
arxiv_id: '2611.07298'
url: https://arxiv.org/abs/2611.07298
pdf_url: https://arxiv.org/pdf/2611.07298
published: '2026-11-05'
collected: '2026-11-06'
category: RecSys
direction: 检索嵌入优化 · 非语义噪声抑制
tags:
- Dense Retrieval
- Embedding
- Attention Sink
- Contrastive Learning
- Long Context Retrieval
one_liner: 在检索嵌入模型输入前加可训练[DUMP]前缀，无结构修改即可提升检索与长上下文性能
practical_value: '- 电商语义召回/商品检索场景可直接将[DUMP]前缀加入现有Embedding模型训练流程，无需修改架构、损失即可低成本提升长商品描述、长query的匹配准确率

  - 优化Agent/RAG系统的检索模块时，给Query和Chunk输入都加2-4个可训练前缀Token，可减少停用词、位置噪声对嵌入的干扰，提升召回精度

  - 调参时可将[DUMP]数量作为超参数，编码器模型优先试2个，解码器模型优先试4个，根据业务文本长度调整，无需盲目增加Token数量'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有嵌入模型将变长文本压缩为固定维度向量时，注意力沉底（Attention Sink）产生的残差信号、停用词等非语义噪声会与核心语义信息纠缠，降低检索表征的区分度；尤其长上下文场景下压缩瓶颈更突出，常规对比学习微调仅在宏观层面优化Query-Passage对齐，无法显式路由低信息信号，存在明显性能瓶颈。
### 方法关键点
- 向Tokenizer新增K个可训练[DUMP]前缀Token，嵌入参数随模型通过标准InfoNCE对比损失共同更新，无需引入辅助损失
- 训练和推理阶段均将[DUMP]Token拼接在Query、Passage输入最前端，参与全层自注意力计算，承接低信息信号的注意力权重
- 完全保留原有模型架构、池化策略、训练目标，属于零侵入的插件式优化
### 关键实验
在BEIR、MTEB、LongEmbed等标准基准上测试6款不同架构的嵌入模型（含gte、BGE等编码器，MobileLLM等解码器），对比无[DUMP]Token的微调基线，标准检索任务平均nDCG@10相对提升2.46%，长上下文检索任务平均相对提升2.41%，增益跨架构、跨数据集一致。
### 核心结论
无需改动模型结构和训练目标，仅添加少量可训练前缀Token即可低成本提升检索嵌入性能，核心逻辑是为非语义噪声提供专用的注意力承接槽，避免其干扰最终表征的语义纯度。
