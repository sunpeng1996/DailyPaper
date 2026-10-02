---
title: Do Multilingual Encoders Produce Language-Consistent Semantic IDs?
title_zh: 多语言编码器能否生成跨语言一致的Semantic ID
authors:
- Abhinav Bohra
- Anuj Bohra
affiliations:
- Amazon
- Rutgers University
arxiv_id: '2610.01139'
url: https://arxiv.org/abs/2610.01139
pdf_url: https://arxiv.org/pdf/2610.01139
published: '2026-10-01'
collected: '2026-10-02'
category: GenRec
direction: 生成式推荐 · 跨语言Semantic ID对齐
tags:
- Semantic ID
- Residual Quantization
- Multilingual Encoder
- Generative Retrieval
- Cross-lingual RecSys
one_liner: 验证仅靠多语言编码器与均衡量化训练集无法保障跨语言Semantic ID对齐
practical_value: '- 跨语言电商推荐/检索场景切勿默认多语言编码器可自动输出对齐的Semantic ID：E5+英文占比80%的量化器下，日语翻译版商品与英文原版的首码一致率仅7.7%，直接用会导致跨语言召回率暴跌

  - 残差量化器训练无需盲目做多语言数据均衡：均衡语言分布反而会降低跨语言ID前缀一致性，西语首码一致率从28.3%跌到6.6%，反而纯英文训练的量化器西语首码一致率可达67.6%

  - 评估Semantic ID抗扰动能力时，优先选用真实商品向量方向的扰动作为对照组，各向同性扰动会高估量化器对语言偏移等特定方向的敏感度

  - 若要实现跨语言Semantic ID对齐，不能依赖编码器或训练集分布的间接作用，必须新增直接约束，强制同一商品的多语言版本共享ID前缀'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
跨语言电商场景中，同一商品的多语言描述若生成的Semantic ID不一致，会导致跨语言检索/推荐时商品无法被召回。业界长期默认多语言编码器的跨语言对齐能力可自动实现ID一致，但该假设从未被系统验证，残差量化过程对语言偏移的影响也不明确。
### 方法关键点
- 数据集：从Amazon ESCI英文商品库采样2万条，用NLLB、Qwen2.5翻译为西语、日语，生成英文复述作为同语言基准
- 对比2款多语言编码器：multilingual E5、LaBSE；采用3级残差量化生成Semantic ID，测试3种训练配比：纯英文、80%英/10%西/10%日、三等分多语言
- 设计两类距离匹配对照组：各向同性扰动、真实商品方向扰动，排除量化器选择性放大语言偏移的可能
### 关键结果
- 80%英文训练的E5量化器下，英文复述首码一致率89.0%，西语翻译仅28.3%，日语翻译仅7.7%
- 均衡训练数据虽缩小了各语言的码本容量差，但西语首码一致率跌至6.6%，纯英文训练的量化器西语首码一致率反而达67.6%
- 真实商品方向扰动下，翻译带来的全ID mismatch和普通商品偏移无显著差异，无证据证明量化器会特意放大语言方向偏移
### 核心结论
仅靠多语言编码器的跨语言对齐能力、或均衡量化训练集的语言分布，都无法保障跨语言Semantic ID的一致性，必须设计直接的对齐约束
