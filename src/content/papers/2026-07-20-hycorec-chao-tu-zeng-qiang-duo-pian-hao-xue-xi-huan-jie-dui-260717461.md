---
title: 'HyCoRec: Hypergraph-Enhanced Multi-Preference Learning for Alleviating Matthew
  Effect in Conversational Recommendation'
title_zh: HyCoRec：超图增强多偏好学习缓解对话推荐马太效应
authors:
- Yongsen Zheng
- Ruilin Xu
- Ziliang Chen
- Guohua Wang
- Mingjie Qian
- Jinghui Qin
- Liang Lin
affiliations:
- Sun Yat-sen University
- Peng Cheng Laboratory
- South China Agricultural University
- Guangdong University of Technology
- Jinan University
arxiv_id: '2607.17461'
url: https://arxiv.org/abs/2607.17461
pdf_url: https://arxiv.org/pdf/2607.17461
published: '2026-07-20'
collected: '2026-07-21'
category: RecSys
direction: 对话推荐 · 马太效应缓解 · 超图建模
tags:
- Conversational Recommendation
- Hypergraph
- Matthew Effect
- Multi-preference Learning
- Diversity Optimization
one_liner: 通过多维度超图建模5类用户偏好，同时提升对话推荐性能与多样性缓解马太效应
practical_value: '- 多维度偏好建模思路可复用：可参考其5类（商品/实体/关键词/评论/上下文）偏好融合方案，解决对话式导购的推荐同质化问题

  - 超图建模落地技巧：针对电商多属性商品，可直接复用其基于同会话商品、实体k-hop邻居、关键词共现构建超图的方法，挖掘用户隐含偏好

  - 马太效应评估指标可直接复用：Coverage@k、Iso-Index组合可作为业务端衡量推荐多样性、缓解头部商品过度曝光的核心评估指标'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
对话推荐系统（CRS）在电商导购、内容推荐场景广泛应用，但传统方法多在静态场景优化马太效应，忽略用户与系统动态交互的反馈循环会持续放大马太效应，导致头部商品过度曝光、长尾商品得不到曝光、用户陷入信息茧房；同时传统知识图谱仅能建模两两关联，无法捕捉用户多维度复杂偏好（如用户选衣服同时关注品牌、颜色、材质等多个属性），是当前CRS落地的核心痛点。

### 方法关键点
- 构建三类超图：基于会话内商品构建商品超图、基于DBpedia的实体k-hop邻居构建实体超图、基于ConceptNet的关键词k-hop邻居构建词超图，捕捉多维度高阶关联
- 学习5类用户偏好：基于三类超图分别学习商品、实体、词维度偏好，结合Transformer编码的评论偏好、RGCN编码的对话上下文知识偏好，覆盖用户显隐性需求
- 双任务联合优化：融合多维度偏好同时优化推荐任务（召回多样化商品）与对话生成任务（生成符合用户偏好的回复），从交互层面缓解马太效应的动态放大

### 关键实验
在REDIAL、TG-REDIAL两个公开对话推荐数据集上，对比KBRD、KGSF、MHIM等10+SOTA基线，推荐任务R@10最高提升13.5%、NDCG@10提升9.3%，对话任务Dist-2/3/4指标平均提升6%；马太效应评估维度，REDIAL数据集上Coverage@20达0.2071（相对基线提升4.7%）、Iso-Index低至0.0617（相对基线下降33%），显著提升推荐多样性。

### 核心结论
缓解对话推荐马太效应的核心不是强行打散推荐结果，而是通过更精细的多维度偏好建模挖掘用户未被满足的隐性需求，在不损失推荐准确度的前提下提升多样性。
