---
title: Doc2LoRA Provides Decodable Representations of Scientific Ideas
title_zh: Doc2LoRA：支持检索与生成的科学文献可解码表示框架
authors:
- Chand Sahil Mansuri
- Joel Zachariah
- Sadamori Kojaku
affiliations:
- Binghamton University
arxiv_id: '2609.38374'
url: https://arxiv.org/abs/2609.38374
pdf_url: https://arxiv.org/pdf/2609.38374
published: '2026-09-29'
collected: '2026-10-01'
category: LLM
direction: LLM文档表示 · LoRA嵌入
tags:
- LoRA
- Document Embedding
- Hypernetwork
- Retrieval
- Generative Representation
one_liner: 以Doc2LoRA生成的LoRA作为文档嵌入，同时支持语义检索、向量运算与自然语言查询
practical_value: '- 可迁移到电商商品/内容的可解释表示场景：将商品详情、用户历史等文档编码为可解码LoRA嵌入，聚类后直接查询簇的主题，替代传统聚类后人工打标流程，大幅降低运营成本

  - 可复用「生成式嵌入+可逆线性变换对齐」的架构：针对生成任务训练的嵌入，仅需少量标注数据训练轻量可逆线性层，即可同时达到接近SOTA的检索效果，兼顾生成与检索需求，避免多套嵌入的维护成本

  - 支持向量运算后的可解释性：对用户兴趣、商品标签的嵌入做插值、平均等操作后，可直接解码为自然语言描述，为推荐理由生成、跨品类商品组合推荐、兴趣探索类推荐提供可解释支撑'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
传统文档嵌入仅适配检索场景，无法对向量运算得到的合成点（如聚类中心、插值点）做精准语义解释，依赖近邻标签、向量转文本等启发式方法，受限于预定义词表或重建精度，无法支撑组合创新类的语义探索需求。
### 方法关键点
- 复用开源Doc2LoRA超网络，将文档编码为固定尺寸的LoRA隐张量作为嵌入，利用其线性等价性，保证向量插值、平均等运算等价于直接操作LoRA参数
- 针对原始D2L嵌入检索效果差的问题，训练仅262k参数的可逆线性变换层，在不损失LoRA解码能力的前提下对齐检索空间
- 解码时将任意嵌入点（含合成点）映射回LoRA适配器，加载到冻结基座LLM即可通过自然语言查询对应语义
### 关键结果
- 聚类标签解码任务上，模糊token重叠度达0.64，较最优基线高12%，LLM评委偏好度领先所有对比方案
- 经可逆变换后的检索效果与SPECTER2、EmbeddingGemma持平，接近SBERT，在14个检索基准上平均排名位列第三
- 文档插值任务上，解码内容可随插值权重平滑过渡，verbatim copy率仅0.56，接近in-context prompting效果

最值得记住的一句话：生成式训练的嵌入隐空间本身隐含可挖掘的检索语义结构，仅需轻量可逆变换即可同时实现检索、生成、可解释三大能力，无需分别训练多套嵌入体系。
