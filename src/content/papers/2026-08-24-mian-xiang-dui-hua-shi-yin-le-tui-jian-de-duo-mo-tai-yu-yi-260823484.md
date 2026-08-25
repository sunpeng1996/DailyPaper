---
title: Multi-Modal Semantic Expansion with Constrained LLM Reranking for Conversational
  Music Recommendation
title_zh: 面向对话式音乐推荐的多模态语义扩展与约束LLM重排序方法
authors:
- Naman Garg
- Sarika Jain
- George Fazekas
affiliations:
- National Institute of Technology Kurukshetra
- Queen Mary University of London
arxiv_id: '2608.23484'
url: https://arxiv.org/abs/2608.23484
pdf_url: https://arxiv.org/pdf/2608.23484
published: '2026-08-24'
collected: '2026-08-25'
category: RecSys
direction: 对话式推荐 · 多模态融合LLM重排
tags:
- ConversationalRecSys
- MultimodalRetrieval
- RRF
- LLM_Reranking
- RAG
one_liner: 提出三阶段多模态融合对话音乐推荐框架，明确LLM重排的窄安全操作边界
practical_value: '- 多模态多路召回融合可采用微分进化优化加权RRF权重，相比均匀权重MRR提升19.5%，该调优方法可直接迁移到电商多信号召回融合场景

  - LLM重排需严格限制干预范围：仅在目标实体（如品牌/艺术家）在Top20中存在1-5个时干预效果最优，全量干预会导致nDCG暴跌18.9%，可直接指导电商搜推广场景的LLM重排边界设定

  - 多目标优化（如推荐精度+生成响应质量）可采用检索、重排、生成三阶段解耦架构，避免单指标优化拉低整体收益，适合对话式导购、内容推荐等需生成解释的场景

  - 生成响应的多样性可通过轮询分配差异化persona+调整temperature/presence penalty实现，Distinct-2可达0.82，可迁移到电商商品推荐话术生成场景'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
对话式推荐需要同时适配多轮对话动态偏好、召回高相关物品、生成符合语境的自然响应，现有方案普遍存在多模态信号融合权重不合理、LLM重排易受位置偏差影响导致效果暴跌、多目标（检索精度/响应质量/多样性）难以协同优化的痛点，在音乐这类元数据、音频、封面等多模态属性强的品类中问题更为突出。

### 方法关键点
- 三阶段解耦架构：① 多模态召回：融合CF-BPR、Qwen3多模态（元数据/歌词/属性）、CLAP音频、SigLIP视觉共7路稠密召回，叠加BM25 lexical召回、艺术家子串匹配信号，采用微分进化算法优化加权RRF的信号权重；② 轻量重排：包含历史推荐去重、流行度平滑、全链路品类多样性惩罚；③ 个性化响应生成：轮询分配10种差异化persona，调用GPT-4o-mini生成符合约束的推荐解释话术。
- 开发期额外验证了专辑续听信号、XGBoost LambdaMART重排、约束LLM艺术家注入等组件，因部署成本和泛化性风险未上线正式版本。

### 关键结果
基于RecSys 2026 TalkPlayData数据集（1.5万训练会话、4.7万首曲目），在500会话验证集上调优RRF权重后MRR相对均匀权重提升19.5%；Blind A验证集上，仅对9个Top20含≤5个目标艺术家的会话做LLM注入nDCG提升0.8%，全量54会话无差别干预导致nDCG暴跌18.9%；正式提交的Blind B版本综合得分0.3213，响应Distinct-2达0.821。

### 核心结论
LLM作为重排组件的增益仅存在于非常窄的「目标实体部分命中」场景，无差别全量干预只会带来灾难性的效果下降。
