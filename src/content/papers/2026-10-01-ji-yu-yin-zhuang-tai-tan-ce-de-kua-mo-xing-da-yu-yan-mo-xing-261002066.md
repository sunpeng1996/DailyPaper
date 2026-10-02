---
title: 'External Observers May See More Clearly: Cross-Model Span-Level Hallucination
  Detection in Large Language Models via Hidden State Probing'
title_zh: 基于隐状态探测的跨模型大语言模型跨度级幻觉检测方法
authors:
- Kingshuk Gupta
- Davide Buscaldi
affiliations:
- École Polytechnique
- Sorbonne Paris Nord
- Nanyang Technological University
arxiv_id: '2610.02066'
url: https://arxiv.org/abs/2610.02066
pdf_url: https://arxiv.org/pdf/2610.02066
published: '2026-10-01'
collected: '2026-10-02'
category: LLM
direction: 大模型鲁棒性 · 幻觉检测
tags:
- Hallucination Detection
- Hidden State Probing
- Cross-Model
- Sequence Labeling
- LLM Safety
one_liner: 提出跨模型隐状态探测的跨度级幻觉检测框架，小观测模型可超越生成模型自检测效果
practical_value: '- 业务侧使用LLM生成商品文案、用户咨询回复时，可复用临界层筛选+NAS特征提取+CRF序列标注的低开销方案，无需额外RAG即可实时定位幻觉跨度，适配低延迟、本地化部署场景

  - 当自研生成大模型自检测效果不佳时，可部署参数更小的外部观测模型做幻觉检测，精度甚至高于生成模型自检测，大幅降低推理成本

  - 针对极端不平衡的序列标注任务（如幻觉起始token识别），可引入类加权交叉熵辅助损失+CRF标签约束，有效提升小众类别的检测精度'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
现有LLM幻觉检测方案普遍依赖RAG带来高延迟，或是仅支持token级二分类、句子级判断，无法精准定位幻觉的起止跨度，不适用于无检索的本地化隐私部署场景。

### 方法关键点
- 将幻觉检测定义为BIO三分类序列标注任务，分别对应事实token、幻觉起始token、幻觉延续token，可精准锚定语义漂移的边界
- 离线计算事实与幻觉样本隐向量的余弦相似度，筛选对语义漂移最敏感的临界层，仅提取这些层的Neuron Activation Score (NAS)作为特征，降低计算开销
- 支持自检测、跨模型检测两种模式，分类器可选MLP、BiLSTM-CRF、BiLSTM-Attn-CRF、BERT-CRF架构，CRF层用于约束标签序列合法性，提升幻觉起始token的检测精度

### 关键结果
在PsiloQA、RAGTruth数据集上测试SmolLM2(1.7B)、TinyLlama(1.1B)、Mistral-7B三个模型：跨模型检测场景下，Gemma2(2B)检测SmolLM2生成内容的幻觉起始token Precision达0.63，较自检测的0.54提升16.7%；1.7B的SmolLM2作为观测模型检测7B Mistral的幻觉，PR-AUC达0.242，超过Mistral自检测的0.221；幻觉起始token检测PR-AUC最高较随机基线提升15倍。

### 核心结论
大模型自检测性能不是幻觉定位的上限，更小的外部观测模型可捕捉到生成模型自身未显性表达的幻觉信号。
