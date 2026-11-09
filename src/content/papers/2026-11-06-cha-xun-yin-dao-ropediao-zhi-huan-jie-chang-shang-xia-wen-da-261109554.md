---
title: Query-Guided RoPE Modulation for Lost-in-the-Middle Mitigation in Long-Context
  LLMs
title_zh: 查询引导RoPE调制缓解长上下文大模型中间信息丢失问题
authors:
- Peiyu Zhang
- Heng Ping
- Shinibali Bhattacharyya
- Anwesan Pal
- Nikos Kanakaris
- Kevin Cheang
- Shixuan Li
- Wei Yang
- Paul Bogdan
affiliations:
- University of Southern California
- Amazon Web Services
arxiv_id: '2611.09554'
url: https://arxiv.org/abs/2611.09554
pdf_url: https://arxiv.org/pdf/2611.09554
published: '2026-11-06'
collected: '2026-11-09'
category: LLM
direction: 长上下文LLM · RoPE优化
tags:
- RoPE
- Long-Context-LLM
- Lost-in-the-Middle
- Inference-Optimization
- RAG
one_liner: 无需训练无需删改输入的RoPE调制方法，缓解长上下文LLM中间信息丢失
practical_value: '- 电商RAG场景（商品详情问答、售后知识库检索、用户评价汇总）可直接复用QGPM逻辑，无需微调模型，仅在推理侧调整RoPE位置编码，就能提升长上下文里相关商品/规则的召回准确率，避免中间信息丢失。

  - 长上下文Agent任务可复用分层相关性映射设计：低层用宽相关性映射保留多候选信息，高层用窄映射聚焦目标，既无需暴力截断/重排上下文损失信息，又能提升目标内容检索精度。

  - 可复用「从模型自身注意力头提取查询相关性」的trick，无需引入外部重排器，减少额外组件的latency开销，适配高并发的搜索/推荐在线场景。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
长上下文LLM普遍存在「lost-in-the-middle」问题，输入中间段信息容易被忽略，现有方案要么删除低重要度token损失信息，要么RoPE修改是查询无关的泛用映射，无法适配不同查询的相关性需求；同时RoPE自身的长距离衰减特性会弱化远距离token的位置信号，进一步加剧中间信息丢失。

### 方法关键点
- 完全训练免方案，无需修改模型权重、无需删改输入token，两次预填充完成推理：第一次预填充从模型预筛选的注意力头提取查询与上下文句子的相关性，生成宽、窄两个相关性映射
- 频率感知调制：仅在RoPE快旋转平面压缩低相关性token的位置步长，拉近高相关性内容与查询的距离，慢旋转平面保留原位置不变，保证文档整体结构不被破坏
- 分层调度：低层网络用宽相关性映射保留多候选信息，高层网络用窄相关性映射聚焦高相关内容，适配不同层的信息处理需求

### 关键实验
在NoLiMa、RULER两个长上下文基准上测试4个主流开源长上下文LLM（Qwen2.5、Qwen3、Ministral、Granite），对比原生模型、LLMLingua-2、STRING等基线：整体准确率平均提升2.4~8.9个百分点，其中NoLiMa低语义重叠检索任务提升最大，平均增益9~17.6个百分点，96个测试场景下赢过原生模型的场景占比超74%。

### 核心结论
无需删上下文、无需微调，仅利用模型自身的注意力信号调整RoPE位置编码，就能以极低代价大幅提升长上下文检索性能，是RAG、长上下文Agent场景性价比极高的优化方案。
