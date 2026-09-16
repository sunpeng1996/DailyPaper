---
title: 'CiteShade: Citation Laundering in Multi-Source Retrieval-Augmented Generation
  and Its Counterfactual Defense'
title_zh: CiteShade：多源RAG的引用洗钱攻击与反事实防御方案
authors:
- Guo Fuzheng
affiliations:
- City University of Hong Kong
arxiv_id: '2609.15660'
url: https://arxiv.org/abs/2609.15660
pdf_url: https://arxiv.org/pdf/2609.15660
published: '2026-09-14'
collected: '2026-09-16'
category: RAG
direction: RAG安全 · 引用归因攻防
tags:
- RAG
- Attack
- Citation
- Counterfactual
- Security
one_liner: 首次提出针对多源RAG的引用洗钱攻击方法及基于反事实删除的防御机制
practical_value: '- 带溯源能力的RAG应用（电商智能客服、商品咨询、内容生成溯源）不能仅校验引用源与声明的匹配度，需额外校验答案的实际驱动源，避免恶意UGC内容通过引用洗钱传递虚假信息

  - RAG引用生成逻辑优化需弱化位置、标签等表面特征的权重，可落地轻量版反事实校验：仅对top2高可疑源做删除重跑，平衡性能与安全性

  - 针对UGC召回源的风险管控，单纯perplexity过滤无法防御自然生成的恶意内容，需结合内容是否诱导单一结论、检索排序特征等做多维度筛查'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有RAG系统将生成答案附带的引用作为用户校验信息可信度的核心审计依据，过往RAG安全研究仅聚焦恶意内容篡改答案的攻击路径，未覆盖引用通道这一全新攻击面；现有引用校验机制仅检查被引用源是否支持对应声明，完全不验证驱动答案生成的实际来源，存在被恶意利用的巨大风险。

### 方法关键点
- 定义引用洗钱攻击范式：攻击者仅控制单条召回源，在保留所有正确证据源、不修改RAG系统任何组件的前提下，诱导RAG输出指定错误答案，且将该答案归因到完全不支持该结论的可信源
- 攻击构造满足三大必要条件：恶意源可被目标query召回、可诱导模型生成目标错误答案、可引导模型引用指定可信源，通过LLM生成符合自然语料统计特征的伪造内容+自验证筛选+引用回声语句植入+利用模型位置偏好四大步骤实现无指令触发攻击
- 反事实防御方案：通过逐一删除召回源重跑生成，计算各源对答案分布的因果影响力，当被引用源不是最高影响力源时触发预警，移除最高影响源后重生成

### 关键实验
在MultiModalQA、HotpotQA两个多源多跳QA数据集上覆盖6款开源生成模型，无攻击时错误答案率为0.01，CiteShade攻击下错误率提升至0.68，对引用生成倾向性最高的模型，引用洗钱率最高可达0.84；反事实防御可将指令类攻击的洗钱率从0.13降至0.03，单query仅需额外3-4次前向推理。

**最值得记住的一句话**：RAG系统的引用质量与引用完整性是完全独立的属性，越容易输出规范引用的模型，越容易被利用实施引用洗钱攻击。
