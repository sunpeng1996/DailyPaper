---
title: 'OmniConfess: Eliciting Token Confessions to Mitigate Omni-Modal Hallucination'
title_zh: OmniConfess：通过token级证据归因缓解全模态大模型幻觉
authors:
- Huiqiang Rong
- Haoran Luo
- Hui Feng
- Zhonghong Ou
- Kaiwen Xue
- Guoxin Zhang
- Yifan Zhu
affiliations:
- Beijing University of Posts and Telecommunications
- Nanyang Technological University, Singapore
arxiv_id: '2610.02999'
url: https://arxiv.org/abs/2610.02999
pdf_url: https://arxiv.org/pdf/2610.02999
published: '2026-10-04'
collected: '2026-10-06'
category: Multimodal
direction: 全模态大模型 · 幻觉缓解
tags:
- Hallucination Mitigation
- Omni-modal LLM
- Inference-time Optimization
- Token-level Attribution
- Training-free
one_liner: 提出免训练全模态幻觉缓解框架，通过token级通道证据归因指导输出修正
practical_value: '- 电商多模态生成场景（商品图文/短视频详情、直播口播文案生成）可直接复用该免训练框架，通过token级证据归因定位幻觉内容，无需微调即可降低生成内容与商品实际属性不符的问题

  - 多模态RAG问答场景（商品咨询客服Agent、搜索多模态答案生成）可借鉴通道级证据干预思路，区分文本/图像/视频等输入通道对生成token的贡献度，避免过度依赖无关检索片段产生错误回答

  - 生成式推荐的多模态item生成、个性化文案生成场景，可借鉴Commitment Anchoring设计，冻结候选响应后再做证据校验，比全量重新生成成本更低，且能保留语义连贯性的同时修正事实错误

  - 可复用其评测思路，构建业务场景的多模态幻觉评测集，覆盖图文/音视频混合输入的判断、生成类任务，量化现有生成链路的幻觉率'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
全模态大模型（OmniLLM）统一处理文本、图像、音频、视频输入，可实现跨模态推理，但生成时易出现过度依赖无关证据、未充分利用有效证据的幻觉问题，现有推理侧幻觉缓解方法要么需要额外训练或外部资源，要么无法定位每个生成token的证据来源，跨模态贡献纠缠、token级分辨率不足，难以精准修正错误。

### 方法关键点
- 免训练推理侧框架，核心包含三个模块：1. Commitment Anchoring：先生成候选响应并完全冻结，消除不同证据干预下的生成轨迹差异，仅保留token的log概率用于后续计算；2. Evidence Interrogation：逐个移除单通道证据，重新计算冻结候选的token得分，得到每个token对各输入通道的依赖度，生成token×通道的结构化confession，标记token为对齐、依赖不足、过度依赖、完全受控四类状态；3. Confession-Guided Correction：判断类任务直接修正分类得分，自由生成任务定位高风险token span，仅局部重生成错误片段，保留正确内容。

### 关键实验
构建了包含3540个难例的OmniHalluBench基准数据集，覆盖文本/图文/音视频输入的判断、自由生成任务，在Qwen2.5-Omni-7B、Qwen3-Omni-30B、Nemotron-3-Nano-Omni-30B三个骨架模型上测试，对比11种现有推理侧方法，平均F1相对base模型分别提升10.3、6.34、7.5个百分点，其中PHD、CMM数据集F1比最强基线高10.2、9.35个点，RAGTruth数据集Token-F1提升16.84个点，推理开销远低于搜索类幻觉缓解方法。

### 核心结论
全模态幻觉的核心是证据依赖错配，冻结候选后做通道级干预的token归因，可在不损失生成流畅度的前提下，以较低成本大幅降低事实错误。
