---
title: Inverting Multi-Vector Visual Document Indices
title_zh: 多向量视觉文档索引的逆向还原攻击研究
authors:
- Zhuchenyang Liu
- Yao Zhang
- Yu Xiao
affiliations:
- Aalto University
arxiv_id: '2610.09920'
url: https://arxiv.org/abs/2610.09920
pdf_url: https://arxiv.org/pdf/2610.09920
published: '2026-10-07'
collected: '2026-10-10'
category: RAG
direction: RAG 多向量检索安全防护
tags:
- Multi-Vector Retrieval
- Vector Database
- Security
- RAG
- Vision-Language Model
one_liner: 证明多向量视觉文档索引可被逆向还原，验证两类低成本防护方案效果
practical_value: '- 业务中使用第三方向量数据库存储多向量检索索引时，需将索引与原始文档做同等安全等级防护，避免敏感信息泄露

  - 针对多向量检索的隐私防护需求，可优先落地token pooling、向量打乱两种低成本方案，实测可将文字还原召回率降至8%

  - 若采用向量打乱防护，需额外防范向量顺序复原攻击，避免攻击者通过还原向量顺序绕过防护机制'
score: 6
source: arxiv-cs.IR
depth: abstract
---

### 动机
现有多向量视觉文档检索器将单页文档拆分为上千个patch向量存储在第三方向量库，业界普遍认为向量无敏感信息、防护等级低于原始文档，存在安全隐患。
### 方法关键点
将索引逆向问题转化为条件文档图像生成任务，验证攻击者仅需编码器、页面形状、向量顺序三类信息即可还原完整页面；测试token pooling、向量打乱两种低成本防护方案，以及针对向量打乱的顺序还原攻击效果。
### 关键结果数字
- ViDoRe v3基准上，原始索引逆向页面可还原47%文字、45%敏感token，作为查询检索时源页Top1准确率达98.4%
- 两种防护方案均可将文字召回率降至8%左右，向量打乱防护被顺序还原攻击破解后，源页Top1准确率从3.8%回升至93.5%
- 攻击方案泛化到其他多向量检索器时，源页Top1准确率仍达70.2%
