---
title: 'MoTE: Mixture of Task Experts for Multi-Task Video Understanding'
title_zh: MoTE：面向多任务多模态理解的任务专家混合解码器架构
authors:
- Muhammad Asad Ali
- Umar Khan
- Nadia Robertini
- Didier Stricker
affiliations:
- University of Kaiserslautern-Landau (RPTU)
- German Research Center for Artificial Intelligence (DFKI)
arxiv_id: '2608.24763'
url: https://arxiv.org/abs/2608.24763
pdf_url: https://arxiv.org/pdf/2608.24763
published: '2026-08-25'
collected: '2026-08-26'
category: LLM
direction: 多模态LLM · 任务级MoE路由
tags:
- MoE
- Multi-Task Learning
- LLM
- Decoder Architecture
- Multimodal
one_liner: 将LLM解码器FFN替换为任务级路由专家，共享骨干，兼顾多任务效果、推理效率与可扩展性
practical_value: '- 多任务LLM服务可复用MoTE架构：将LLM解码器FFN拆分为共享专家+任务专属专家，每个请求仅激活单个任务专家，既避免多任务负迁移，又降低推理算力成本，适合电商多场景文案生成、商品理解等多任务并行的业务场景

  - 新增任务时仅初始化新任务专家，冻结原有骨干与已上线专家参数单独训练，旧任务效果无劣化，无需全量重训，大幅降低新场景迭代成本，可用于快速上线新的推荐/广告生成任务

  - 推理无显式任务标识时，可通过prompt与预注册的专家描述做语义匹配自动选路由，轻量实现意图识别，无需额外训练分类模型，适合Agent的多工具路由场景

  - 多模态理解任务（如商品短视频理解、直播内容审核、小票信息抽取）可复用该设计，共享骨干处理通用模态编码，任务专家适配不同场景的输出要求，兼顾效果与扩展性'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
多任务多模态LLM采用全共享解码器时，差异较大的任务目标（如动作识别、步骤预测、结构化信息抽取）会互相干扰，产生负迁移；传统token级稀疏MoE路由粒度和用户侧任务边界不匹配，可解释性差，新增任务扩展困难，无法满足模块化部署需求。

### 方法关键点
- 改造LLM解码器FFN层：每层替换为1个共享FFN专家+N个任务专属FFN专家，注意力层、模态编码器、投影层全量共享，每个样本仅激活对应任务的1个专属专家+共享专家，单请求计算量不随专家数量增长
- 路由设计：训练时用任务标签做显式路由监督，仅激活的专家回传梯度；推理时支持直接传入任务ID，或通过prompt与预注册的专家描述做语义匹配自动选择路由
- 模块化扩展：新增任务仅需初始化新的任务专家单独训练，无需修改原有参数；不需要的任务可直接移除对应专家，满足合规性要求

### 关键结果
- COIN视频理解5个任务上，1B参数的VideoLLM-MoTE平均top-1准确率达62.9%，超过8B参数VideoLLM基线的61.8%；单样本仅激活2B参数，推理 latency 较8B基线降低35.7%，解码 throughput 提升35.6%
- 新增任务时原有任务准确率无下降，跨领域迁移到文档OCR+KIE任务，CORD数据集KIE Micro-F1从基线的20.07%提升到95.79%，同时完全保留原OCR效果

### 核心结论
对于边界清晰的多任务场景，显式任务级路由比隐式token级MoE或全参数共享的效果更优，同时兼顾可解释性、扩展灵活性与推理效率。
