---
title: 'Merge and Branch: Efficient Tree-Structured Supervised Fine-Tuning of LLMs
  for Recommendation'
title_zh: 面向LLM推荐的树形结构高效监督微调框架Merge and Branch
authors:
- Yunqin Zhu
- Yao Xie
affiliations:
- Georgia Institute of Technology
arxiv_id: '2610.37973'
url: https://arxiv.org/abs/2610.37973
pdf_url: https://arxiv.org/pdf/2610.37973
published: '2026-10-27'
collected: '2026-10-30'
category: GenRec
direction: 生成式推荐 · LLM高效微调
tags:
- GenRec
- LLM4Rec
- SFT
- FlashAttention
- KV cache
- Semantic ID
one_liner: 通过交互token压缩、树形多目标训练与定制Attention同时提升生成式推荐效果与训练推理效率
practical_value: '- 交互压缩trick可直接复用：以商品Semantic ID（SID）为锚点，通过轻量跨注意力将每个商品的SID、标题、属性压缩为1-2个软token，在保留语义的前提下将输入长度缩短80%以上，降低训练推理成本

  - 多目标训练方案可迁移：除下一跳主目标外，额外加入用户后续真实交互目标、传统召回模型（如SASRec）生成的合成目标，采用分组加权平衡不同目标贡献，仅增加少量训练成本即可提升推荐效果2%以上

  - 工程优化方案可落地：Tree FlashAttention支持多目标共享历史前缀计算，训练成本降低90%；共享前缀KV cache在beam search时复用历史KV，2048长序列场景下推理内存降低85%、延迟降低40%

  - 业务优化优先级参考：生成式推荐中给单个商品分配更多输入token的收益远低于从单条用户历史中挖掘更多监督信号，优先做单样本多监督优化而非盲目增加输入长度'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
当前基于LLM的生成式推荐存在严重的输入输出不对称问题：需要处理上千token的用户交互历史+商品文本信息，却仅预测几个token的Semantic ID（SID），单条用户历史仅提供1个监督信号，训练效率极低；同时长输入也导致推理成本过高，难以落地工业级长序列推荐场景。

### 方法关键点
- **Merge模块**：以商品SID嵌入为锚点，通过跨注意力将每个商品的SID、文本、元数据压缩为Nq个软token，保留时序和语义信息的同时大幅缩短历史输入长度
- **Branch模块**：每条用户历史对应多个独立预测分支，包含下一跳主目标、后续真实交互目标、传统推荐模型生成的合成目标，各分支仅能访问共享历史和自身前缀，互不干扰，避免推理时的目标泄露
- **Tree FlashAttention**：定制支持树形注意力结构的前向/后向kernel，无需生成稠密注意力矩阵，共享历史计算的同时累计所有分支梯度，端到端训练模型
- **共享前缀KV cache**：推理时beam search的所有假设共享历史前缀的KV缓存，仅保留各假设的SID分支状态，大幅降低推理内存和延迟

### 关键结果
在Amazon三个公开数据集（Beauty、Sports、Toys）上对比SASRec、TIGER、EAGER-LLM等12个基线，效果相对最优基线提升2.48%~16.19%；训练时相比未压缩输入成本降低90%以上，2048长序列下推理内存降低85.8%、延迟降低40%；1个合并token per item即可达到最优的效率效果平衡。

### 最值得记住的一句话
生成式推荐优化的核心是从每条用户历史中学习更多监督信号，而非单纯增加输入的token数量
