---
title: 'HNR-DAC: Hard-Negative Reranking and Distribution-Aligned Classification for
  Scientific Claim Verification'
title_zh: HNR-DAC：面向科学主张验证的难负例重排序与分布对齐分类
authors:
- Zhenchao Wang
- Xin Chen
- Luoxi Zhang
- Min Yang
- Shiwen Ni
affiliations:
- Southern University of Science and Technology
- Institute of Artificial Intelligence, Shenzhen University of Advanced Technology
- Shenzhen Institutes of Advanced Technology, Chinese Academy of Sciences
arxiv_id: '2608.07204'
url: https://arxiv.org/abs/2608.07204
pdf_url: https://arxiv.org/pdf/2608.07204
published: '2026-08-07'
collected: '2026-08-10'
category: RAG
direction: RAG 证据验证 · 难负例重排序
tags:
- Hard-Negative Mining
- Reranking
- Distribution Alignment
- Claim Verification
- RAG
one_liner: 提出两阶段HNR-DAC框架解决科学主张验证的证据混淆、训练推理分布不一致问题
practical_value: '- 召回/重排序模块可复用HNR难负例构造思路，用基础排序器打分筛选和正例最相似的难负例做对比学习，提升排序区分度

  - 多阶段pipeline可借鉴DAC分布对齐思路，训练下游分类器时直接用上游模块的输出作为输入，消除训练推理分布差，提升端到端效果

  - 电商商品内容真实性校验、Agent工具调用结果可信度验证场景，可直接复用两阶段「难负例排序+分布对齐分类」架构'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
科学主张验证任务存在两大核心痛点：一是论文内部干扰段落与真实证据相似度高，重排序阶段易混淆；二是分类器训练阶段使用标注的黄金证据，推理阶段使用检索得到的证据，存在训练推理分布差，导致效果受损。
### 方法关键点
提出两阶段HNR-DAC框架：1）HNR难负例重排序：基于基础重排序器对非黄金段落的打分，筛选混淆度最高的难负例与黄金证据做对比学习，提升证据区分度；2）DAC分布对齐分类：冻结训练好的HNR模块，用其输出的Top1段落作为分类器训练输入，保证训练推理分布一致，最终取HNR输出Top3作为证据结果。
### 关键结果
在NLPCC 2026 Task10 Track2数据集上，Hit@3达97.21%，Macro-F1达95.79%，Joint@3达94.47%，平均得分95.13%；官方榜单排名第三，同时拿下全赛道最高Macro-F1 93.05%
