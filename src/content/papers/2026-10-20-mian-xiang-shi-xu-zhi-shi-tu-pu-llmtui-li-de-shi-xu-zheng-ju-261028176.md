---
title: Temporal Evidence-Parameter Co-Alignment for LLM Reasoning over Temporal Knowledge
  Graphs
title_zh: 面向时序知识图谱LLM推理的时序证据-参数协同对齐框架
authors:
- Jiapu Wang
affiliations:
- 南京理工大学计算机科学与工程学院
arxiv_id: '2610.28176'
url: https://arxiv.org/abs/2610.28176
pdf_url: https://arxiv.org/pdf/2610.28176
published: '2026-10-20'
collected: '2026-10-21'
category: Reasoning
direction: 时序知识图谱 · LLM推理优化
tags:
- TKG
- LoRA
- RAG
- Temporal Reasoning
- LLM
one_liner: 提出证据与参数双对齐的TEPCA框架，结合时序感知检索与动态门控LoRA提升时序知识图谱LLM推理性能
practical_value: '- 电商/广告的时序类RAG场景（如大促咨询、迭代商品问答、时效型内容推荐）可复用DRGP路径剪枝+MI局部事实筛选的双检索策略，优先召回时序一致的全局事件链+高信息增益的局部事实，减少过时信息干扰

  - 需要适配时序语义漂移的PEFT场景（如按季度/大促周期迭代的推荐Agent、营销文案生成模型微调）可直接替换常规LoRA为DG-LoRA，通过时间戳条件门控动态调整低秩子空间，避免不同周期语义互相混淆，提升微调效果的同时保持参数高效

  - 对动态知识依赖强的电商Agent/推荐场景，可借鉴证据-参数双对齐思路，不要只依赖RAG补动态知识，同时配合轻量的输入感知微调对齐模型语义，双管齐下降低过时知识导致的幻觉'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
LLM静态参数记忆与真实世界知识的动态演化存在天然不匹配，常规RAG仅聚焦语义相关性，忽略时序有效性、事件顺序与演化依赖，易召回时序矛盾的碎片化证据；常规PEFT（如LoRA）采用输入无关的固定低秩更新，无法捕捉实体语义、关系随时间的漂移，最终导致时序推理准确率低、过时知识幻觉严重。
### 方法关键点
- 证据层对齐采用双剪枝策略：动态相关性引导路径（DRGP）剪枝，按反向时序约束、全局路径连贯性筛选符合因果逻辑的长程时序路径；互信息（MI）剪枝，结合语义相似度、时序衰减、背景显著性筛选对查询信息量最高的局部事实，避免高普适性低信息量的事实被过度召回
- 参数层对齐采用动态门控LoRA（DG-LoRA）：将时间戳作为输入的一部分，通过可学习的门控网络动态激活不同的低秩子空间，根据时序上下文自适应调整LoRA的有效秩，在保持参数高效的同时捕捉实体/关系的时序语义漂移
- 框架整体先通过时序随机游走做查询扩展补全历史上下文，再召回对齐后的时序子图，最后用DG-LoRA微调后的LLM生成结果
### 关键结果
在ICEWS14、GDELT两个时序知识图谱基准上取得SOTA：ICEWS14上Hit@1=0.371、Hit@10=0.768，较此前最优基线分别提升0.4pp、4pp；GDELT上Hit@1=0.143、Hit@10=0.363，较此前最优基线分别提升0.4pp、5.9pp。在8个通用常识QA数据集上，DG-LoRA较常规LoRA平均提升1.8~2.0pp，适配所有主流开源LLM backbone。
### 核心结论
动态知识场景下仅靠RAG补充外部知识不足以解决时序幻觉，必须同时从证据检索的时序一致性和模型参数的时序适应性两方面做对齐
