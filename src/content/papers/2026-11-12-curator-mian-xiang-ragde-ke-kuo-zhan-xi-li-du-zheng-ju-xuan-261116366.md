---
title: 'CURATOR: Scalable Fine-grained Evidence Selection for Retrieval-Augmented
  Generation using Decision Models'
title_zh: CURATOR：面向RAG的可扩展细粒度证据选择决策框架
authors:
- Shib Dasgupta
- Bandish Parikh
- Rashmi Gangadharaiah
affiliations:
- AWS AI Labs
arxiv_id: '2611.16366'
url: https://arxiv.org/abs/2611.16366
pdf_url: https://arxiv.org/pdf/2611.16366
published: '2026-11-12'
collected: '2026-11-13'
category: RAG
direction: RAG优化 · 细粒度证据选择
tags:
- RAG
- Evidence Selection
- Fine-grained Retrieval
- Decision Model
- LoRA
one_liner: 通过可变规模监督微调多输出决策模型，以低计算成本提升RAG细粒度证据选择效果
practical_value: '- 电商/广告RAG场景（如商品问答、投放文案生成、售后知识库问答）可直接复用该细粒度span选择逻辑，在有限context窗口下塞入更多有效证据，降低LLM推理成本，尤其适配端侧小模型RAG、高并发在线RAG链路

  - 微调多输出联合决策模型时，可复用「可变候选集规模采样+类别平衡损失」的训练策略，解决候选数量上升时决策准确率下降的问题，该方法可迁移到多商品/多内容的联合排序、多候选广告素材择优等场景

  - 垂直领域模型适配时，在LoRA微调的同时加入通用任务的replay+知识蒸馏，可避免模型遗忘原有通用能力，平衡领域定制效果和泛化性，适合小参数模型的轻量微调

  - 工程实现上，多候选联合打分相比逐候选上下文感知打分可降低20倍以上的推理延迟和token消耗，适合高并发的搜索推荐、智能Agent的RAG链路优化'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
RAG系统通常将整段召回文本喂给LLM，大量无关内容挤占context窗口、抬高推理成本，还会降低下游生成质量；细粒度span选择可解决该问题，但现有独立打分方法无法捕捉跨span的依赖（如多跳推理需多个关联证据），逐候选上下文感知打分计算量过高，而预训练联合决策模型在候选数量上升时准确率会显著下降，亟需兼顾效果和效率的细粒度证据选择方案。

### 方法关键点
- 训练数据构造：从QA数据集构造可变规模（8~128个候选）、可变证据密度的训练样本，覆盖稀疏/富证据场景，模拟实际业务中候选数量波动的情况
- 模型微调：基于4.5B参数的预训练多输出决策模型，仅用LoRA微调全注意力层的Q/K/V/O投影和决策输出层，仅更新3.8M参数，微调成本极低
- 损失设计：采用类别平衡的联合监督损失，解决正负样本（有效/无效span）极不均衡的问题；同时加入通用决策任务的重放+知识蒸馏，避免模型遗忘原有能力
- 推理逻辑：所有候选span联合打分，按得分排序后贪心选择直到token预算耗尽，候选过多时分批打分再合并结果

### 关键实验
对比基线包括预训练联合决策模型、Qwen3/BGE系列reranker，跨多跳QA、事实校验、金融/法律领域数据集验证：相比预训练联合决策模型，CURATOR在不同context预算下证据召回平均提升25.8%，推理延迟和token消耗仅为逐候选上下文感知方案的1/21.7；128token预算下，跨未见领域数据集证据召回平均提升17.0%，下游RAG回答质量平均提升17.4%；候选数量从8升至256时，CURATOR的证据区分AUROC几乎无下降，解决了预训练模型的规模退化问题。

**最值得记住的一句话**：对于RAG和Agent的context优化，细粒度证据选择的收益在context预算越紧张的场景下越显著，联合决策+针对性微调是兼顾效果和效率的核心路径。
