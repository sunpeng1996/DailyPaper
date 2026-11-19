---
title: 'PGPO: Prototype-Guided Progressive Obfuscation for Privacy-Preserving LLM-Enhanced
  Recommendation'
title_zh: PGPO：原型引导渐进式混淆实现隐私保护的LLM增强推荐
authors:
- Shengxiang Lin
- Jiajie Su
- Pengyang Zhou
- Xiang Chen
- Xiaolin Zheng
- Feng Tian
- Chaochao Chen
affiliations:
- Zhejiang University
- Xi'an Jiaotong University
arxiv_id: '2611.23236'
url: https://arxiv.org/abs/2611.23236
pdf_url: https://arxiv.org/pdf/2611.23236
published: '2026-08-25'
collected: '2026-11-19'
category: RecSys
direction: LLM增强推荐 · 隐私保护
tags:
- Privacy-Preserving
- LLM4Rec
- Obfuscation
- GRPO
- Topology-Aware
one_liner: 提出原型引导的渐进式混淆框架，在LLM增强推荐场景同时实现强隐私防护与近上限推荐精度
practical_value: '- 做推荐侧信息隐私防护时可放弃字面语义保真要求，仅保留item间相对语义拓扑（关系保真）即可维持推荐精度，比传统同义词替换、加噪声方案掉点低至少30%

  - 可直接复用GRPO三奖励设计：个体语义偏移奖励拉远原/混淆词相似度、结构一致性奖励保item相对关系、语义约束奖励防生成结果偏出品类，快速平衡隐私与效用

  - 大规模词表混淆无需全表同时优化，先筛选高影响力原型词作为锚点再向外传播，可降低70%以上计算开销，适合电商百万级SPU侧信息批量预处理

  - 调用第三方LLM生成item语义embedding时，可离线用PGPO预处理侧信息再传接口，避免价格带、小众品类标签等敏感属性被embedding inversion攻击泄露'
score: 9
source: huggingface-daily
depth: full_pdf
---

### 动机
LLM增强推荐通过item侧信息生成语义embedding，有效缓解冷启动、数据稀疏问题，但公开的embedding易被embedding inversion攻击还原出原始敏感文本属性（如商品小众分类、用户敏感标签）。现有输入侧防御要么依赖可信数据采集方，要么做局部token扰动，会破坏item间的语义拓扑，导致推荐精度大幅下降，无法平衡隐私与效用。

### 方法关键点
- 提出**关系保真**核心原则：混淆时仅需保证item间的相对语义关系不变，无需保留字面语义，大幅降低约束难度
- 三级渐进式混淆流程：1）基于词的全局语义影响力筛选高价值原型词，构建静态语义邻接图；2）用GRPO微调LLM生成原型词的混淆锚点，优化目标为三个奖励加权和：个体差异奖励最大化原/混淆词embedding距离、结构一致性奖励保持局部语义相似性排序、语义约束奖励限定混淆结果在原品类语义空间内；3）基于静态图将原型锚点的混淆规则传播到全词表，降低全表优化开销
- 两级缓存机制：单词缓存存最高奖励的混淆结果，全局队列存已生成的混淆对用于上下文prompt组装，提升生成一致性

### 关键实验
在MovieLens-1M、Amazon-Book两个公开推荐数据集上，和InferDPT、SanText+等6种基线对比：1）相同embedding偏移量下，语义拓扑保持的Spearman相关性比基线最高高117%；2）下游推荐性能接近原始侧信息的上限，掉点小于2%，优于所有基线；3）embedding inversion攻击成功率比原始侧信息低50%以上，与基线防护能力相当。

> 最值得记住的结论：LLM增强推荐的隐私防护不需要保持侧信息的字面语义保真，仅维持item间的相对语义拓扑关系，就能在强隐私防护下实现接近上限的推荐效用。
