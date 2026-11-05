---
title: 'Persona Perspectives: Adopting Viewpoints Reorganizes Representations in LLMs'
title_zh: 人格视角：采用不同观点会重构大语言模型的内部表征
authors:
- Austin C. Kozlowski
- Avital Mintz
- Madison Lee
affiliations:
- University of Chicago
arxiv_id: '2611.06848'
url: https://arxiv.org/abs/2611.06848
pdf_url: https://arxiv.org/pdf/2611.06848
published: '2026-11-04'
collected: '2026-11-05'
category: LLM
direction: LLM可解释性 · 人格诱导表征重构
tags:
- LLM Interpretability
- Persona
- Linear Probe
- SAE
- Representation Geometry
one_liner: 发现提示LLM采用特定人格会系统性重构隐空间语义结构，导致通用安全监控探针失效
practical_value: '- 构建拟人化电商客服、商家Agent时，不能直接复用通用合规性/话术偏向性探针，需在目标人格场景下单独验证探针准确性，避免误判违规内容或漏检风险。

  - 做人群定向生成式推荐、个性化文案生成时，可针对目标人群的偏好构建对应人格下的专属语义轴，相比全局语义轴能显著提升内容相关性与用户接受度。

  - 基于LLM做商品评价情感分析、用户舆情分类时，若涉及立场偏向类内容（如品牌粉丝/黑粉评价、圈层向商品反馈），需针对对应立场微调分类探针，避免通用分类器准确率大幅下降。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有LLM可解释性方法（Linear Probe、SAE）均默认概念表征在不同上下文下保持稳定，但LLM可通过简单prompt唤起不同人格/观点，是否会改变隐空间几何结构、进而破坏通用监控探针的有效性是未被验证的核心问题，对LLM安全落地、个性化场景应用都有重要实际价值。

### 方法关键点
- 实验覆盖Llama 3.1、Gemma 3、Qwen 3、Ministral 3四个系列共8个模型（4B~70B参数），通过system prompt诱导美国自由派、保守派两种政治人格，对比空prompt、helpful AI assistant两个基线。
- 构建9493个常用词的表征库、33个语义轴，计算不同人格下的词在轴上的投影、轴之间的余弦对齐相似度差异。
- 测试三类通用监控探针（Linear Probe、SAE特征探针、词表征探针）在非争议/政治争议内容上的判定准确率差异。

### 关键结果
- 人格诱导后语义轴对齐关系出现系统性偏移：自由派人格下自由-保守轴与好-坏轴相关系数达0.75，保守派人格下反转至-0.79；8个模型的人格诱导偏移模式一致性达r=0.84，与党派语料训练的word2vec语义差异一致性达r=0.64。
- 通用探针在非争议内容上准确率达94~99%，但在政治争议内容上出现显著偏向：同一争议声明在不同人格下的探针判定结果差异可达60%以上，SAE探针在保守派人格下的准确率从97%降至88%。

**最值得记住的结论**：不要默认LLM的概念表征是上下文无关的，仅一句人格诱导prompt就会系统性重构隐空间几何结构，导致通用探针在特定场景下完全失效。
