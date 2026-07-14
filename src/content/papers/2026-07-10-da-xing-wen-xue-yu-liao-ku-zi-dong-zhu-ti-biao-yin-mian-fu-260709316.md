---
title: 'Automatic Thematic Indexing of Large Literary Corpora: A Machine Learning
  Approach to Voltaire''s Complete Works'
title_zh: 大型文学语料库自动主题标引：面向伏尔泰全集的机器学习方法
authors:
- Miguel Arana-Catania
- Gillian Pink
- Glenn Roe
affiliations:
- University of Oxford, UK
arxiv_id: '2607.09316'
url: https://arxiv.org/abs/2607.09316
pdf_url: https://arxiv.org/pdf/2607.09316
published: '2026-07-10'
collected: '2026-07-14'
category: LLM
direction: 大语言模型多标签文本分类
tags:
- multi-label-classification
- LoRA
- quantized-LLM
- Mistral
- automatic-indexing
one_liner: 对比多类模型实现文学语料自动主题标引，4-bit量化Mistral效果最优
practical_value: '- 多标签分类打标场景可直接复用「4-bit量化+LoRA微调Mistral」的配置，平衡效果与推理成本，适配电商商品/内容大规模打标需求

  - 人工标注存在主观不一致性时，可将语义有效的非匹配模型预测作为补充标引结果，降低人工审核工作量

  - 跨语料泛化评估框架可复用在电商跨类目/跨场景打标任务中，验证模型鲁棒性'
score: 4
source: arxiv-cs.IR
depth: abstract
---

### 动机
大规模文学、历史语料的主题标引目前高度依赖人工，劳动密集、效率低下，无法适配海量语料的结构化检索需求。
### 方法关键点
将主题标引建模为多标签分类任务，覆盖3B~120B参数区间对比两类方案：带分类头的Encoder类模型、经LoRA微调的生成式LLM；引入4-bit量化降低大模型推理开销，测试数据为伏尔泰全集中的两个子语料库。
### 关键结果
最优方案为4-bit量化的Mistral系列模型，F1最高达0.67；因人工标引存在固有主观性，大量与标注不一致的模型预测语义实际有效，该F1为效果下界；完成跨语料泛化评估，定性明确了文学修辞类样本的模型处理边界。
