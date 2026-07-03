---
title: Embedding Inference Attack
title_zh: 嵌入模型推理攻击
authors:
- Cedric Fitiavana Raelijohn
- Sébastien Gambs
- Jean-Francois Rajotte
affiliations:
- Université du Québec à Montréal, Canada
arxiv_id: '2607.01276'
url: https://arxiv.org/abs/2607.01276
pdf_url: https://arxiv.org/pdf/2607.01276
published: '2026-07-01'
collected: '2026-07-03'
category: RAG
direction: RAG系统安全 · 嵌入模型隐私攻击
tags:
- Embedding Inference Attack
- Black-box IR
- RAG Security
- Privacy Protection
- Model Fingerprinting
one_liner: 黑盒场景下仅通过无排序返回文档集识别IR/RAG系统所用嵌入模型，验证攻击路径与防御方案
practical_value: '- 搭建电商商品语义检索、客服RAG系统时，可叠加相似性阈值过滤+轻量reranker的组合策略，大幅提升嵌入模型被恶意识别的门槛，降低后续隐私泄露风险

  - 对外提供向量检索类API服务时，需隐藏返回结果的排序、相似度得分等冗余信息，避免攻击者构造查询反推底层嵌入模型

  - 涉及用户隐私的行为/商品嵌入部署时，可定期轮换底层嵌入模型版本，进一步提升攻击的匹配成本'
score: 6
source: arxiv-cs.IR
depth: abstract
---

### 动机
现有语义IR、RAG系统的嵌入模型多以黑盒API形式对外暴露，传统嵌入 inversion攻击需提前获知目标嵌入模型才可实施，此前无仅靠无排序返回文档集识别底层嵌入模型的黑盒攻击路径研究。
### 方法关键点
1. 构造高区分度定制查询，仅通过目标系统返回的无排序文档集合，在候选模型池中匹配识别实际使用的嵌入模型，即嵌入推理攻击（EIA）；
2. 验证了添加reranker、LLM非合规输入过滤等常规防御下，部分定制查询仍保留模型区分能力；
3. 提出相似性阈值过滤等缓解策略。
### 关键结果
在真实RAG系统上验证EIA攻击可成功绕过LLM的非法输入拒答机制，所提相似性阈值策略可将攻击成功率降至极低水平。
