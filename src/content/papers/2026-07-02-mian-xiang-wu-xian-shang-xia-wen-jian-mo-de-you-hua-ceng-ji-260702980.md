---
title: 'Hierarchical Sparse Attention Done Right: Toward Infinite Context Modeling'
title_zh: 面向无限上下文建模的优化层级稀疏注意力机制HiLS-Attention
authors:
- Xiang Hu
- Xinyu Wei
- Hao Gu
- Minshen Zhang
- Tian Liang
- Huayang Li
- Lei Zhu
- Yan Wang
- Sirui Han
- Yushi Bai
affiliations:
- Tencent HY Team
- ShanghaiTech University
- Hong Kong University of Science and Technology
- University of California, San Diego
arxiv_id: '2607.02980'
url: https://arxiv.org/abs/2607.02980
pdf_url: https://arxiv.org/pdf/2607.02980
published: '2026-07-02'
collected: '2026-07-08'
category: LLM
direction: 大语言模型 · 长上下文稀疏注意力优化
tags:
- Sparse Attention
- Long Context LLM
- Inference Acceleration
- KV Cache
- Length Extrapolation
one_liner: 提出端到端可训练的层级稀疏注意力HiLS-Attention，兼顾短上下文性能、超长上下文外推与推理效率
practical_value: '- 长上下文Agent应用可直接复用HiLS的chunk检索+层级注意力架构，大幅降低超长用户行为序列、多轮对话历史的处理成本，同时保证信息召回准确性

  - 长文档RAG场景可借鉴其Landmark Token+低秩Query校准的trick，提升大段商品评价、售后工单等长文本的语义检索精度，避免均值池化丢失关键信息

  - 大模型推理引擎优化可参考其相邻查询chunk打包复用的kernel设计，在推荐系统批量生成个性化文案、商品解说等场景下提升推理吞吐量

  - 现有全注意力模型可通过仅训练<1%参数（Landmark Token+低秩投影）的低成本方式，快速升级为长上下文能力模型，适配电商大促全量用户行为建模需求'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前大语言模型长上下文能力受全注意力的二次复杂度、外推能力差、KV缓存开销随长度线性增长的限制，现有分块稀疏注意力方法因分块选择不准确，性能始终低于全注意力，无法满足长周期Agent任务、大规模用户行为建模等场景需求。

### 方法关键点
- 引入Landmark Token为每个分块生成可学习的压缩摘要，通过LogSumExp一阶泰勒展开拟合全注意力下的分块质量，解决均值池化摘要表达能力不足的问题
- 采用层级注意力分解架构：先通过分块间softmax分配注意力权重到top-K选中分块，再在分块内计算token级注意力，分块选择与LM损失端到端联合优化
- 工程优化：相邻查询的选中分块打包复用，提升Tensor Core利用率，无需依赖大GQA分组即可实现高效推理；支持轻量增量训练，现有全注意力模型仅需训练<1%参数即可迁移

### 关键结果
- 仅8K上下文预训练的345M模型，外推到4M上下文时NIAH检索准确率仍保持90%+，外推倍数达512倍
- 512K上下文下，预填充速度比全注意力快13.5倍，解码速度快15.7倍，短上下文通用任务性能与全注意力持平
- 7B全注意力模型仅需50B token继续训练，即可保持短上下文能力不变，LongBench整体得分比YaRN增强的基线高1.5个百分点

最值得记住的一句话：稀疏注意力不再是精度妥协的折衷方案，HiLS证明其可同时实现比全注意力更强的长上下文能力、更高的推理效率与相当的短上下文性能
