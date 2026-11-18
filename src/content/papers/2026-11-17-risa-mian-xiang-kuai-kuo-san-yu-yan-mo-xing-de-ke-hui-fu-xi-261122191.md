---
title: 'RISA: Recoverable Sparse Attention for Block-Diffusion Language Models'
title_zh: RISA：面向块扩散语言模型的可恢复稀疏注意力
authors:
- Xinrui Zhong
- Fanjiang Ye
- Yuke Wang
affiliations:
- Rice University
arxiv_id: '2611.22191'
url: https://arxiv.org/abs/2611.22191
pdf_url: https://arxiv.org/pdf/2611.22191
published: '2026-11-17'
collected: '2026-11-18'
category: LLM
direction: 块扩散大模型 稀疏注意力推理优化
tags:
- Sparse Attention
- KV cache
- Diffusion Language Model
- Long Context Inference
- GPU Optimization
one_liner: 提出可恢复稀疏注意力方案，在不损失效果前提下大幅提升块扩散大模型长上下文推理速度
practical_value: '- 长上下文LLM服务（如Agent长对话、长文档商品分析）可复用RISA的KV分层存储逻辑：HOT/COLD层全量保留在GPU不删除，仅区分访问优先级，避免误删后续需用的KV，效果优于直接KV
  eviction方案

  - 块扩散模型做批量并行生成场景（如批量生成商品文案、推荐理由）可直接复用块内读计划复用逻辑：同一生成块的多步去噪共享一次KV选路结果，不需要改模型结构即可大幅降低注意力计算开销

  - 长上下文召回类任务（如RAG、长文本商品检索）可迁移页级极值打分选KV的方法：用粗粒度页匹配代替逐token匹配，在保持召回准确率的前提下降低计算量'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
块扩散语言模型（DLM）支持并行多token生成，是自回归解码的有力替代，但长上下文推理时每步去噪都要读取全量历史KV cache，内存瓶颈严重；传统稀疏注意力方案存在KV读集合膨胀、选路开销高的问题，永久删除低优先级KV的策略还会导致效果下降，无法兼顾推理质量和速度。
### 方法关键点
- KV分层存储：新生成的KV先进入宽限期，根据多步注意力访问量划分到HOT（高优先级紧凑存储）和COLD（低优先级可恢复存储），全部保留在GPU不删除，避免永久丢失后续可能用到的信息
- 块级共享读计划：每个生成块的第一步种子前向，联合打分选出有界的KV读索引，后续去噪步骤复用该索引，仅更新query和当前块KV，不需要重复选路
- 无侵入设计：不需要修改模型backbone、解码器、提交规则，可直接接入现有块扩散模型
### 关键结果
在DreamReasoner-8B、SDAR-8B-Chat、LLaDA2.2-mini三个模型上测试，对比dense attention、MAGE、QUEST、LoSA等baseline；效果上，在GSM8K、MATH-500、HotpotQA等任务上与dense效果持平甚至略优；速度上，H200 GPU 128K上下文时注意力提速5.53×，32K上下文时整请求提速1.36×，所有8个测试配置下相同KL时解码速度都超过对比方案。
> 最值得记住的一句话：长上下文稀疏注意力优化的核心是区分存储优先级和读优先级，不要把临时的读选择变成永久的KV删除，通过跨步骤复用读计划可以大幅摊薄选路开销
