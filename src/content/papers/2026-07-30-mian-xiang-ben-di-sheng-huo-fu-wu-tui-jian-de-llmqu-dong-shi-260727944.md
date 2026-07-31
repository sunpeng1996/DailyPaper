---
title: Interpretable Representation via LLM-Driven Generative Disentanglement for
  Local-Life Service Recommendation
title_zh: 面向本地生活服务推荐的LLM驱动生成式解耦可解释表示
authors:
- Long Zhang
- Hao Jiang
- Sheng Yu
- Fei Pan
- Peng Jiang
- Kun Gai
affiliations:
- Kuaishou Technology
arxiv_id: '2607.27944'
url: https://arxiv.org/abs/2607.27944
pdf_url: https://arxiv.org/pdf/2607.27944
published: '2026-07-30'
collected: '2026-07-31'
category: GenRec
direction: 生成式推荐 · Semantic ID解耦表示
tags:
- Semantic-ID
- Generative-Recommendation
- Local-Life-Recommendation
- Disentangled-Representation
- LLM4Rec
one_liner: 提出LLM驱动生成式解耦的SID生成框架，解决本地生活推荐语义纠缠与SID碰撞问题
practical_value: '- 本地生活类推荐可直接复用Encode→Disentangle→Align→Quantize的SID生成pipeline，先联合编码保留地理-语义交互再解耦分槽量化，相比独立字段编码MRR最高提升88.5%，还能降低SID碰撞率

  - 结构化解耦块(SD-Block)设计可复用：用业务属性相关prompt初始化锚点slot，搭配结构化注意力掩码强制地理/语义槽独立、地理槽内遵循行政层级自回归，大幅提升属性解码准确性

  - 量化阶段采用双路残差量化，地理和语义槽分开编码进SID，生成的SID可直接与原有稀疏ID embedding拼接，无需修改现有排序模型架构，落地成本极低

  - 构造hard negative可参考三类分层负样本（同粗区域不同细位置、同细位置不同语义、同语义不同粗区域），有效提升SID的细粒度区分度'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有Semantic ID（SID）生成普遍采用单表示后量化范式，在本地生活推荐场景下存在两大核心痛点：一是地理、品牌、品类等异质属性语义纠缠，量化时关键属性丢失导致SID碰撞严重，比如不同城市的同品牌门店SID过于相似；二是表示和量化过程黑盒，SID缺乏明确的属性对应关系，无法适配本地生活「先地理可达、后兴趣匹配」的决策逻辑。独立字段编码虽能避免纠缠，但会丢失地理与语义的交互信息（如商圈属性会影响品类语义判断），效果反而更差。
### 方法关键点
- 提出LGRID框架，遵循**Encode→Disentangle→Align→Quantize**的生成式解耦pipeline，先通过LLM联合编码POI的地理、品类、品牌文本，保留地理-语义依赖
- 结构化解耦块：用业务属性相关prompt初始化slot锚点，搭配结构化注意力掩码，实现地理槽内遵循行政层级自回归、地理与语义槽间完全独立，将纠缠隐状态路由到属性对齐的槽位
- 协同对齐学习：通过渐进式生成解耦任务做属性解码监督，搭配三类分层hard negative做对比学习，加潜变量多样性正则约束槽间无冗余
- 双路残差量化：地理、语义槽分别量化为2层code，拼接成4位SID，可直接接入现有推荐模型
### 关键结果
在快手工业数据集、Foursquare公开数据集上对比主流SID方法，适配10种推荐backbone：快手数据集最高获**5.44%相对AUC提升**，粗粒度地理属性解码准确率超99%，全SID碰撞率从LGSID的97.0%降至39.9%，相比独立字段编码各属性MRR提升31.4%~88.5%。
### 核心洞见
Semantic ID生成无需直接量化融合后的单隐向量，先做属性解耦分槽再分流量化，既能提升推荐效果还能获得可解释性，落地成本极低
