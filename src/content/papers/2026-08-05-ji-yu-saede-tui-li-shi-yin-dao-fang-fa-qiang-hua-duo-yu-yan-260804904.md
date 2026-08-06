---
title: 'Strengthening Target-Language Features: SAE-Based Steering for Multilingual
  Inference'
title_zh: 基于SAE的推理时引导方法强化多语言大模型目标语言特征
authors:
- Hongsheng Wang
- Phlipp Koehn
affiliations:
- Johns Hopkins University
arxiv_id: '2608.04904'
url: https://arxiv.org/abs/2608.04904
pdf_url: https://arxiv.org/pdf/2608.04904
published: '2026-08-05'
collected: '2026-08-06'
category: LLM
direction: LLM推理优化 · SAE多语言特征引导
tags:
- Sparse-Autoencoder
- Multilingual-LLM
- Inference-Steering
- Parameter-Free
- Cross-Lingual
one_liner: 推理时无需更新参数，通过SAE识别目标语言特征并注入隐层，提升多语言大模型下游任务效果
practical_value: '- 跨境电商多语言场景（客服、商品文案生成、小语种query理解）可直接复用该方案，仅需几百条平行语料即可在不微调模型的前提下提升小语种任务效果，大幅降低适配成本

  - 多语言Agent开发中，可借鉴「平行语料对比提取任务专属SAE特征→生成引导向量注入隐层」的流程，无需修改模型参数即可快速适配特定语言、特定领域的需求

  - 大模型推理优化场景可参考其工程实现：选择Transformer靠后层（如输出前一层）注入引导向量，引导系数α可先在0.2-1.4区间快速验证效果，无需逐语言调优即可获得稳定收益'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
多语言大模型性能在不同语言间差异极大，高资源语言（如英语）效果远好于低资源语言，现有适配方法需要更新模型参数、依赖大量多语言训练数据，小语种场景落地成本高，亟需轻量的推理时优化方案。

### 方法关键点
- 采用预训练的层专属SAE对Transformer各层隐状态编码，得到可解释的稀疏特征表示
- 基于少量多语言平行语料，对比目标语言与参考表示（多语言质心/英语）的SAE激活差异，每层选top-k差异最大的特征作为目标语言专属特征
- 将选中的特征差异编码为稀疏向量，通过SAE解码器映射回隐层空间作为引导向量，推理时以系数α加权注入到Transformer指定层的最后一个prompt位置隐状态，全程无需更新模型参数

### 关键实验
基于Gemma-3-12B-it模型验证，仅需500条平行语料完成特征识别：在XCOPA（常识推理）、XNLI（自然语言推理）、MGSM（数学推理）三个多语言基准上，对比无引导基线平均准确率分别提升10.9、5.3、1.9个百分点；采用全局通用系数α=0.6无需逐语言调优，即可实现三个数据集平均4.75、1.61、2.13个百分点的稳定提升。

**最值得记住的一句话**：基于SAE的稀疏特征引导是无需微调即可定向增强大模型特定能力的轻量方案，可快速适配资源受限的小语种、垂直领域场景。
