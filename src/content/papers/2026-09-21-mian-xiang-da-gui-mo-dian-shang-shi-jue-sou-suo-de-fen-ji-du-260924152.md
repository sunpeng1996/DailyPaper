---
title: Graded-Relevance Composed Multimodal Retrieval for E-commerce Visual Search
  at Scale
title_zh: 面向大规模电商视觉搜索的分级相关度组合多模态检索方案
authors:
- Anubhav Gupta
- Hrushikesh Mohapatra
- Prijith Chandra
- Asish Mohapatra
- Anuj Garg
- Arvind Maan
- Sudip Datta
- Venkat Bulusu
- Sitesh Kumar Jalan
affiliations:
- Walmart Global Tech
arxiv_id: '2609.24152'
url: https://arxiv.org/abs/2609.24152
pdf_url: https://arxiv.org/pdf/2609.24152
published: '2026-09-21'
collected: '2026-09-23'
category: RecSys
direction: 电商多模态搜索 · 组合图像检索
tags:
- Composed Image Retrieval
- Multimodal Retrieval
- VLM
- Visual Search
- E-commerce
one_liner: 基于VLM无标注分级标签与角损失训练CIR模型，落地沃尔玛电商视觉搜索
practical_value: '- 数据侧可复用：无需人工标注，用VLM自动生成query并做4级相关度标注，配合迭代难负例挖掘，可低成本生成千万级训练集，适配所有多模态检索场景

  - 训练侧可复用：用AngleLoss替代传统二元对比损失适配分级标签，仅修改损失函数即可获得NDCG@10 5%左右的稳定提升，无额外推理成本

  - 工程侧可复用：用Matryoshka表示学习训练多维度embedding，可根据 latency 要求直接截断维度无需重训，配合LoRA微调VLM大幅降低训练成本

  - 架构选择结论：处理带文本修饰的多模态检索场景，优先选择early-fusion VLM，相比late-fusion方案在修饰类query上效果提升更显著'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有组合图像检索（CIR）普遍采用二元相关度标注，不符合真实电商场景中大量部分匹配商品的存在，二元标签会丢失排序所需的细粒度信息，直接影响用户体验，且大规模人工标注成本极高，难以落地生产。

### 方法关键点
1. **数据流水线**：用VLM自动生成两类query（目标检测生成相似类query、修饰词合成生成修改类query），并用VLM judge自动标注4级相关度（Exact/NearExact/PartialMatch/Irrelevant），全程无人工标注
2. **迭代难负例挖掘**：用训练中的模型不断召回新的难负例，补充到训练集直到离线效果收敛，最终生成3.5M高质量训练对
3. **训练目标**：采用层次感知AngleLoss替代传统二元对比损失，充分利用分级标签的序关系，避免信息丢失
4. **模型适配**：基于PaliGemma2 early-fusion VLM做bi-encoder检索适配，添加[QUERY]/[ITEM]角色前缀，用Matryoshka学习多维度embedding，配合LoRA微调降低训练成本

### 关键结果
内部沃尔玛测试集上，相比二元标注方案，4级分级标注带来NDCG@10 4.9%~5.9%的提升；该方案对任意多模态编码器均有效，最多可将early-fusion backbone的NDCG@10提升8.5%；公开FashionIQ数据集上fine-tune后平均Recall达0.6703，超过SOTA基线SPN4CIR；目前已落地沃尔玛生产环境，承载真实用户流量。

最值得记住的结论：电商检索场景中，细粒度分级相关度标注带来的效果增益，远大于单模型结构优化的收益，且VLM自动标注可低成本实现这一方案
