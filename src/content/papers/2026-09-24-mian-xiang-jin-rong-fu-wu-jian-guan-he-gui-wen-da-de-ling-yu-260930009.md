---
title: Automated Regulatory Compliance Question Answering in Financial Services with
  Domain-Adapted Retrieval-Augmented Generation
title_zh: 面向金融服务监管合规问答的领域适配RAG方案
authors:
- Tobias Deußer
- Abhishek Pillai
- Aurelio F. Bariviera
- Dhananjay Bhardwaj
- Lorenz Sparrenberg
- David Berghaus
- Christian Bauckhage
- Rafet Sifa
affiliations:
- University of Bonn
- Lamarr-Institute for Machine Learning and Artificial Intelligence
- Universitat Rovira i Virgili
- Fraunhofer IAIS
arxiv_id: '2609.30009'
url: https://arxiv.org/abs/2609.30009
pdf_url: https://arxiv.org/pdf/2609.30009
published: '2026-09-24'
collected: '2026-09-25'
category: RAG
direction: 垂直领域RAG 金融合规问答优化
tags:
- RAG
- Domain Adaptation
- LoRA
- Hybrid Retrieval
- LegalNLP
one_liner: 提出三阶段适配检索器+RAFT-LoRA微调小模型的RAG pipeline，提升金融合规问答效果
practical_value: '- 垂直领域RAG的检索器优化可复用三阶段方案：先基于领域预训练模型做蕴含调优，再用batch内负例对比学习，最后和BM25做分数融合，可大幅提升召回率

  - 本地/端侧部署小模型的RAG场景，可采用4-bit量化+RAFT-LoRA微调方案，低算力开销下提升生成质量，弱模型增益更明显

  - 垂直领域RAG的评估不能只看综合得分，需单独设计溯源性/事实准确性评估指标，避免得分高但幻觉严重的问题

  - 跨领域RAG系统需额外做领域适配微调，直接复用同套微调参数效果会大幅下降'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
金融机构监管合规问答要求结果可溯源到权威文本，可本地部署的小参数LLM幻觉问题突出，通用RAG在垂直监管领域召回准确率不足。
### 方法关键点
检索器基于LegalBERT做三阶段训练：1. 蕴含调优，将问题-段落匹配转化为前提-假设重构任务；2. 批次内负例对比调优；3. 与BM25做分数级融合。生成器采用2B-12B参数小模型4-bit量化部署，通过LoRA做检索感知微调（RAFT）适配。
### 关键结果
在ObliQA金融监管问答基准上，三阶段检索器Recall@10达0.774，优于BM25（0.678）和E5-large-v2（0.758）；RAFT-LoRA可提升所有适配模型的RePASs得分，弱模型增益最显著；微调模型无法跨领域迁移到澳大利亚判例法问答，无检索的闭卷模型RePASs得分仅比全pipeline低0.011，但无引用、幻觉严重，说明现有综合指标无法衡量事实溯源能力。
