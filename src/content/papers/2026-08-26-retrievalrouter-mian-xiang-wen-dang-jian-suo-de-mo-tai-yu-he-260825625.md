---
title: 'RetrievalRouter: Joint Modality and Architecture Selection for Document Retrieval'
title_zh: RetrievalRouter：面向文档检索的模态与架构联合选择路由
authors:
- Emre Kuru
- Mehmet Onur Keskin
- Reza Farahbakhsh
- Noel Crespi
affiliations:
- Institut Polytechnique de Paris
- Özyeğin University
arxiv_id: '2608.25625'
url: https://arxiv.org/abs/2608.25625
pdf_url: https://arxiv.org/pdf/2608.25625
published: '2026-08-26'
collected: '2026-08-27'
category: RAG
direction: RAG 检索管线动态路由优化
tags:
- Retrieval Routing
- Multimodal Retrieval
- RAG
- Latency Optimization
- nDCG
one_liner: 仅通过query文本选择最优检索管线，较最佳静态基线nDCG@5提升2.5%、速度快12.4倍
practical_value: '- 电商搜索/客服RAG系统可复用query级路由思路，根据query复杂度（短尾关键词用BM25、长尾/多模态需求用dense/多模态检索）平衡精度和时延，无需全量部署成本最高的管线

  - 训练路由模型可复用「融合精度+时延的奖励函数+软目标+KL散度损失」方案，通过λ参数灵活调整精度-时延权重，适配不同业务场景（C端搜索优先低时延、内部知识库优先高精度）

  - 多模态检索场景无需盲目全量上线多模态管线，文本管线在长文本推理场景效果更优，通过路由动态分配可同时降本提效

  - 业务部署late-interaction类检索优先选择rerank版本，可覆盖纯late-interaction管线的绝大多数精度收益，同时时延大幅降低'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
当前文档检索管线存在模态（文本/多模态）、架构（稀疏/dense/late-interaction）的选择矛盾：高精度管线时延过高无法规模化部署，低时延管线在复杂文档/query上召回率不足，业务只能全局选择固定管线，被迫在漏召回和高时延中二选一；而不同query对管线的需求差异极大，固定方案存在严重的资源浪费和效果损失。

### 方法关键点
- 动作空间筛选：从7种候选管线中剔除冗余的纯late-interaction管线，保留BM25、文本dense、文本rerank、多模态dense、多模态rerank5种可选项
- 轻量路由结构：基于Qwen3-0.6B做query编码器，仅对注意力和FFN层加LoRA微调，接单层线性决策头输出选择概率，总训练参数量仅4M，推理 overhead 仅15ms
- 抗噪声训练方案：定义融合nDCG@5和归一化时延的奖励函数，通过λ参数控制精度-时延权重，基于奖励生成软目标，用KL散度作为损失训练，避免硬标签的噪声问题

### 关键结果
在11个跨金融、科研、开放域的检索基准上测试：
- 较最优静态基线（Multimodal-Late）nDCG@5提升2.5%，时延降低12.4倍；较部署常用的多模态rerank基线nDCG@5提升3%，时延降低1.7倍
- 精度优先场景下较现有自适应路由方法nDCG@5显著更高，时延优先场景下效果和时延均优于基线

**最值得记住的一句话**：检索的精度-时延矛盾本质是路由问题，而非架构问题，通过query级动态分配管线可在不损失精度的前提下大幅降低推理成本。
