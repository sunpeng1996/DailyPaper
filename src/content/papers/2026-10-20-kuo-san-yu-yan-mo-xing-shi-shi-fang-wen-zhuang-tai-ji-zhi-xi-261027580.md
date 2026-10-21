---
title: 'Factual Access States in Diffusion Language Models: From Mechanism to Knowledge
  Editing and Retrieval'
title_zh: 扩散语言模型事实访问状态：机制解析、知识编辑与检索应用
authors:
- Yuchen Guo
- Zhuoyuan Mao
- Yiwen Guo
affiliations:
- The University of Tokyo
- LIGHTSPEED Tencent
- Independent Researcher
arxiv_id: '2610.27580'
url: https://arxiv.org/abs/2610.27580
pdf_url: https://arxiv.org/pdf/2610.27580
published: '2026-10-20'
collected: '2026-10-21'
category: LLM
direction: 扩散LLM · 知识编辑与检索
tags:
- DiffusionLM
- KnowledgeEditing
- Retrieval
- CausalTracing
- FactualAccess
one_liner: 揭示扩散LM事实访问的实体-关系融合机制，提出多视图知识编辑与零训练实体检索方案
practical_value: '- 电商Agent商品知识实时更新场景可借鉴多视图编辑思路：对单条知识构造正向、反向、关系掩码、上下文变体等多视图训练，大幅提升不同用户问法（含反向问法）的回答准确率，解决“反转诅咒”问题。

  - 多实体多关系Query理解/检索场景可直接抽取LLM早期层的实体位置隐藏态作为关系感知检索向量，无需额外训练检索模型，就能将双实体查询召回率提升10倍以上，且早期层读出入参仅2ms/query，时延远低于普通深度检索器。

  - LLM知识校验场景可基于事实访问状态的触发强度阈值，快速判断用户Query是否命中已编辑知识，避免无关查询触发错误更新，保障知识编辑的局部性。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有自回归（AR）模型的知识编辑方法迁移到扩散语言模型（DLM）时，存在 paraphrase 泛化差、反向查询完全不生效的问题，核心原因是DLM的事实访问机制与AR模型差异显著，尚未被明确解析，导致上层编辑、检索方案无法匹配底层计算逻辑。

### 方法关键点
- 用适配掩码范式的因果追踪方法定位DLM事实访问机制：Layer0注意力将关系表述路由到可见实体位置，1-8层MLP基于融合后的实体-关系状态做事实查询，该状态同时依赖实体、关系表层形式、查询方向，构成状态空间区域而非单点。
- 提出MULTI-VIEWEDIT编辑方法：对单条事实构造正向、反向、部分关系掩码、上下文变体等多视图，为每个方向拟合共享值写入早期MLP层，无需修改注意力结构。
- 检索侧直接提取每个实体位置的事实访问状态作为关系感知检索向量，无需训练或Query分解，交替融合各实体的检索排序结果。

### 关键结果
- 知识编辑实验在CounterFact、BAKE、QAEdit数据集上验证：BAKE数据集上，反向QA准确率在LLaDA-8B上从22.4%提升到63.2%，Dream-7B上从20.3%提升到83.6%，而AR编辑器提升不足3个点；QAEdit上44.6%的原错误自由式回答变为至少部分正确。
- 检索实验在自研多实体查询数据集上验证：双实体查询的All@2准确率，单向量基线最高仅3.06%，本方法可达41.94%。

最值得记住的结论：扩散LM的事实访问核心是实体与关系的早期融合状态，所有知识操作的泛化性本质取决于对该状态空间的覆盖度。
