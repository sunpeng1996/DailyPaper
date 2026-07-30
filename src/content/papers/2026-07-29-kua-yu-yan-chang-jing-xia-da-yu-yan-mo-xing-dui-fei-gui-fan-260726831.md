---
title: Language Models are not Equally Robust to Non-Canonical Tokenization across
  Languages
title_zh: 跨语言场景下大语言模型对非规范分词的鲁棒性存在显著差异
authors:
- Poulami Ghosh
- Preethi Jyothi
affiliations:
- IIT Bombay, India
arxiv_id: '2607.26831'
url: https://arxiv.org/abs/2607.26831
pdf_url: https://arxiv.org/pdf/2607.26831
published: '2026-07-29'
collected: '2026-07-30'
category: LLM
direction: 大语言模型 · 跨语言鲁棒性优化
tags:
- Tokenizer
- Multilingual LLM
- Robustness
- LoRA
- Data Augmentation
one_liner: 系统评估27种语言下LLM非规范分词鲁棒性，提出多分词LoRA微调优化方案
practical_value: '- 多语言跨境电商/推荐场景下，使用多分词数据做LoRA微调，可显著提升小语种用户Query理解、多语言RAG检索的鲁棒性

  - 做用户Query改写、语义匹配任务时，可加入非规范分词样本做数据增强，无需额外标注成本即可提升模型泛化性

  - 选择多语言LLM底座时优先测试非规范分词性能：Qwen3的跨语言分词鲁棒性优于同量级Llama3.1和Gemma3

  - 低资源小语种场景下，仅用英语数据做非规范分词增强的LoRA微调，即可跨语言迁移鲁棒性，降低小语种标注成本'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
英文场景下的研究显示LLM对表示相同文本的非规范分词鲁棒性较强，但该结论未在跨语言场景验证；多语言Tokenizer对不同语言的词表分配不均，低资源语言分词碎片化严重，而Tokenizer裁剪、跨语种适配等实际场景都会产生非规范分词输入，现有模型的鲁棒性尚不明确。

### 方法关键点
- 覆盖27种语言、6类下游任务（QA、数学推理、多选、跨语言检索等），测试Llama3.1-8B、Qwen3-8B、Gemma3-12B三个主流指令微调模型
- 定义三类分词输入：标准规范分词、均匀采样非规范分词、字符级分词，控制解码后文本完全一致，隔离分词结构本身的影响
- 提出多分词数据增强的LoRA微调方案，对比单样本单分词、单样本多分词变体、按分词长度分桶采样等训练策略

### 关键结果
- 英文分词鲁棒性不具备通用性：非规范分词下Llama3.1-8B平均相对性能下降23.7%，Qwen3-8B下降11.4%，Gemma3-12B下降9.9%
- 分词碎片化程度越高的语言，对非规范分词的敏感性越强，性能下降与分词长度正相关，排除了序列长度增加的干扰
- 仅用英文数据做LR-Bucketed多分词LoRA微调，全语言的非规范分词性能最多提升2.1%，鲁棒性损失降低0.9个百分点

**最值得记住的一句话**：LLM的分词鲁棒性不是通用属性，高度依赖语言本身的分词特性和训练数据覆盖度，多分词数据增强是低成本提升跨语言鲁棒性的有效方案
