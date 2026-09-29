---
title: 'FactorEngram: Factorized N-gram Memory with Basis-Level Gating for Language
  Models'
title_zh: FactorEngram：面向大语言模型的带基级门控的分解式N-gram记忆
authors:
- Bowen Yang
- Jingbo Zhou
- Qinghong Miao
- Hua Wu
affiliations:
- Baidu Inc.
- Nanyang Technological University
arxiv_id: '2609.35578'
url: https://arxiv.org/abs/2609.35578
pdf_url: https://arxiv.org/pdf/2609.35578
published: '2026-09-27'
collected: '2026-09-29'
category: LLM
direction: LLM lookup式记忆架构优化
tags:
- LLM
- Lookup Memory
- Engram
- N-gram
- Contextual Gating
- Sparse Coding
one_liner: 提出FactorEngram分解式N-gram记忆架构，解决lookup记忆的多义适配与语义参数共享问题
practical_value: '- 电商/推荐场景的小LLM优化可复用该架构：将高频用户行为pattern、商品词组、搜索query对存为lookup记忆，替代部分LLM推理逻辑，降低推理延迟的同时提升高频场景效果

  - 多义内容/query适配可参考基级门控设计：用共享语义基+动态系数的方案，替代传统单scalar门控，让同一个pattern（如多义搜索词、多类目商品词）在不同用户上下文下激活不同语义分量

  - 记忆模块接入可直接复用实验结论：插在Transformer中间层attention前的效果最优，尤其适配长会话推荐、长用户序列理解等长上下文场景，无需额外遍历测试插入位置

  - 边缘/端侧部署的LLM可采用共享字典+系数的存储方案：相比每个n-gram单独存embedding的方式，存储开销可降低30%以上，同时保证语义共享性'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有基于lookup的LLM记忆架构（如Engram）将每个检索到的n-gram embedding作为整体，仅通过单个标量门控调制，存在两大核心缺陷：一是多义pattern无法根据上下文选择对应语义分量，例如搜索词“苹果”在数码、生鲜场景下无法自适应匹配语义；二是参数共享仅依赖哈希碰撞，语义相似的pattern无法复用表征，既浪费存储又限制效果提升。
### 方法关键点
- 分解式记忆表征：用全pattern共享的字典基+稀疏正则化的系数表示每个n-gram，语义相关的pattern可复用相同基向量，加L1正则约束系数稀疏性，降低计算开销
- 基级上下文门控：复用同一个字典计算当前backbone隐藏态与每个基向量的相似度作为门控，单独调整每个基的系数权重，实现细粒度的上下文自适应记忆读取
- 架构优化：同时覆盖unigram、bigram、trigram三类pattern，记忆模块以残差方式接入，不修改原有backbone结构，系统验证最优插入位置为Transformer中间层attention之前
### 关键实验结果
基于340M、1B参数量的Transformer backbone训练，对比原生Transformer、原版Engram基线：340M规模下，WikiText PPL较Transformer降1.9、较Engram降1，LAMBADA PPL较Transformer降3.21、较Engram降2.25；长上下文检索NIAH-3准确率较Engram提升43.3个百分点；1B规模下NIAH-3准确率仍较Engram高27.6个百分点。
> 最值得记住的结论：Lookup式记忆的优化核心是解决语义共享与上下文适配问题，分解式表征+细粒度门控的收益远高于整体式记忆的简单堆叠
