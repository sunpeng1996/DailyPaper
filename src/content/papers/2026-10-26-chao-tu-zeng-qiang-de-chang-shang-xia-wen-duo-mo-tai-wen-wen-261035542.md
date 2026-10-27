---
title: Hypergraph-Enhanced Evidence Selection for Long-Context Multimodal Document
  QA
title_zh: 超图增强的长上下文多模态文档问答证据选择框架
authors:
- Wenxin Zhao
- Jiachuan Wang
- Xinyi Zhu
- Jiake Ge
- Haoyang Li
- Yongqi Zhang
- Shuangyin Li
- Lei Chen
affiliations:
- The Hong Kong University of Science and Technology (Guangzhou)
- University of Tsukuba
- Tianjin University
- The Hong Kong Polytechnic University
- South China Normal University
arxiv_id: '2610.35542'
url: https://arxiv.org/abs/2610.35542
pdf_url: https://arxiv.org/pdf/2610.35542
published: '2026-10-26'
collected: '2026-10-27'
category: RAG
direction: 多模态RAG · 超图证据选择
tags:
- Multimodal RAG
- Hypergraph
- Long Context
- Evidence Selection
- Document QA
one_liner: 提出超图建模多模态文档结构关联，结合意图感知成本优先选择，提升长上下文多模态文档QA效果
practical_value: '- 多模态内容（商品详情页、广告素材、商家手册）的RAG系统可借鉴超图建模方法，将图片/表格/关联文本绑定为超边作为检索单元，避免跨模态信息断裂，提升召回准确性

  - 检索阶段放弃固定top-K cutoff，改用成本感知的贪心选择策略，根据查询意图动态调整召回量：定位类query只召回最小必要单元，统计类query召回全量匹配单元，在控制token成本的同时提升召回覆盖

  - 离线构建多粒度结构化索引（页面/区块/跨模态关联组），在线根据query意图触发不同检索工具，可直接迁移到电商客服Agent、商品文档问答、广告素材合规校验等场景的多模态RAG系统'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
长上下文多模态文档QA需要跨页、跨模态关联推理，但现有多模态RAG依赖固定粒度（页面/区块）+静态top-K召回，易丢失结构关联、召回冗余或缺失证据，同时受VLM上下文窗口预算限制，难以平衡召回覆盖和推理成本。
### 方法关键点
- 离线构建文档超图：节点为多粒度文档单元（页面、文本/标题/图表/标题区块），超边分两类：①视觉中心上下文超边，绑定图表/表格等视觉锚点与对应标题、说明文本；②结构超边，绑定页面、章节下的所有关联单元，保留层级和跨页关联
- 在线查询流程：①意图解析，识别5类意图（定位/统计/枚举/对比/跨源推理），拆分硬约束（页码/章节/ID）和软约束（语义关键词）；②意图引导候选召回，根据约束触发对应检索工具生成候选超边池；③成本感知贪心选择，优先满足硬约束，再按单位成本的边际覆盖增益排序选择超边，达到阈值自动停止，规避固定top-K缺陷
- 选中超边经重排序和区块级剪枝后线性化为VLM输入，平衡覆盖度和token成本
### 关键结果
在MMLongBench-Doc、LongDocURL、DocBench三个长文档多模态QA基准测试，对比M3DocRAG、MDocAgent、MoLoRAG等SOTA基线：使用Qwen3-VL-32B时，三个基准ACC分别达54.7%、66.2%、78.2%，较最优基线最高提升5.6pp；检索召回率对比ColPali最高提升27pp，端到端 latency 较MDocAgent降低30%以上
### 核心结论
多模态RAG的核心不是召回更多内容，而是用结构化建模保留证据关联，结合查询意图和预算动态选择最匹配的证据组，在控制成本的同时提升推理效果
