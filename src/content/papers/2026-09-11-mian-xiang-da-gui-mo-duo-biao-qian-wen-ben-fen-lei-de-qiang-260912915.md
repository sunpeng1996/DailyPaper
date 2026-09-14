---
title: LLM-Enhanced Dual-Branch Learning for Large-Scale Multi-Label Text Classification
title_zh: 面向大规模多标签文本分类的LLM增强双分支学习方法
authors:
- Hui Ye
- Jing Zhang
- Xiulong Yang
- Rajshekhar Sunderraman
affiliations:
- Georgia State University
- Amazon
- Central China Normal University
arxiv_id: '2609.12915'
url: https://arxiv.org/abs/2609.12915
pdf_url: https://arxiv.org/pdf/2609.12915
published: '2026-09-11'
collected: '2026-09-14'
category: LLM
direction: 多标签分类 · LLM异质表征融合
tags:
- Multi-label Classification
- Dual-branch Learning
- LLM
- Late Fusion
- Text Representation
one_liner: 提出融合自回归LLM与双向编码器的双分支多标签分类框架，在三类基准任务上达SOTA
practical_value: '- 电商商品类目打标、短视频/内容标签生成场景可直接复用双分支架构，分别用BERT类双向编码器捕捉局部上下文、Decoder-only
  LLM捕捉全局语义，仅在logit层做晚融合，无需改动单模型内部结构，工程改造成本极低

  - 推荐/搜索场景的用户意图分类、query标签召回等万级标签任务，可借鉴异质模型独立打分+晚融合思路，既保留单路模型的推理优化空间，又能通过互补性提升分类准确率

  - 生产环境高吞吐需求下，可将双分支任务并行部署，两路打分互不干扰，可复用现有单模型的KV cache、量化等优化手段，时延增幅可控'
score: 7
source: arxiv-cs.AI
depth: abstract
---

### 动机
大规模多标签文本分类需从数千到数万候选标签中为文本匹配相关子集，现有方案多依赖单一编码器或单排序器融合特征，未充分挖掘异质语言模型的表征互补性，在电商商品打标、内容标签生成、搜索意图分类等场景存在效果瓶颈。
### 方法关键点
提出DualMLC双分支框架：同一份输入文本分别送入两个独立表征通路，一路用Decoder-only自回归LLM提取全局语义，另一路用双向编码器提取上下文细粒度语义，两个分支在共享标签空间独立输出相关性打分，最终通过晚logit融合合并两路结果，强化高相关标签权重的同时，弥补单路模型的表征缺陷。
### 关键结果
在3个公开大规模多标签文本分类基准上达到SOTA，消融实验验证双分支融合的排序效果显著优于任意单分支独立输出。
