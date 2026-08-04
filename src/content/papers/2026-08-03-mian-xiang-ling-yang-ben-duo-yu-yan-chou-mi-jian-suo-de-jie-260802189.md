---
title: Disentangled Contrastive Learning for Zero-Shot Multilingual Dense Retrieval
title_zh: 面向零样本多语言稠密检索的解耦对比学习方法
authors:
- Chao Huang
- Yufeng Chen
- Changhao Guan
- Guang Yang
- Dongze Chen
- Kaiyu Huang
affiliations:
- Key Laboratory of Big Data & Artificial Intelligence in Transportation (Beijing
  Jiaotong University, MOE)
- School of Computer Science and Technology, Beijing Jiaotong University
arxiv_id: '2608.02189'
url: https://arxiv.org/abs/2608.02189
pdf_url: https://arxiv.org/pdf/2608.02189
published: '2026-08-03'
collected: '2026-08-04'
category: RecSys
direction: 跨语言稠密检索 · 解耦对比学习
tags:
- Dense Retrieval
- Contrastive Learning
- Disentangled Representation
- Zero-shot Learning
- Multilingual NLP
one_liner: 将多语言表征解耦为语义与语言子空间，结合分层对比学习提升零样本跨语言检索性能
practical_value: '- 跨境电商多语言搜索场景可直接复用解耦框架，将语义/语言特征分离，降低不同语种语法、词汇差异对召回排序的干扰，零样本迁移到小语种站点

  - 小语种无平行标注语料时，可引入分层语义对齐+非平行语料语义一致性约束，仅需高资源语种标注数据即可实现跨语言迁移，大幅降低标注成本

  - 任意需要跨域/跨场景迁移的检索/推荐模型，均可引入正交约束，让任务相关特征和无关特征（如语言、内容风格）的子空间正交，减少无关特征对匹配效果的干扰'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
当前零样本多语言稠密检索依赖高资源语种（如英文）标注数据迁移到小语种，但多语言预训练模型的表征会纠缠语义与语言特征，导致模型过度依赖语言相关模式而非通用语义匹配，跨语言迁移效果差，无标注小语种场景性能下降明显。

### 方法关键点
- 设计语义-语言解耦模块：通过两个独立投影头，将编码器输出的纠缠表征分别映射到语义子空间（负责检索相关语义匹配）和语言子空间（负责捕获语种特有特征），加入Frobenius正交约束降低两个子空间的相关性
- 分层语义对齐对比学习：有平行语料的语种同时做句子级（加入难负例）和token级的跨语言对齐；无平行语料的小语种加入语义一致性约束，保证同语义不同语种的表征距离一致
- 语言去偏对比学习：让语言子空间中同语种表征聚拢、不同语种表征分散，将语言特有特征从语义子空间剥离
- 联合训练检索损失和解耦损失，平衡检索效果和跨语言迁移能力

### 关键结果
仅用英文检索标注数据训练，在mMARCO（14语种）数据集上平均MRR@10比最强英文监督基线高1.5个点，比多语言监督基线高0.4个点；在MIRACL（18语种）零样本跨域场景下，平均nDCG@10比最强基线XLM-RAGG高2.7个点，无平行语料的小语种提升更显著；消融实验显示仅解耦模块即可提升MRR@10 2.3个点。

最值得记住的一句话：将任务相关和无关特征解耦后针对性优化对应子空间，是提升跨域/跨语言零样本迁移能力的高效路径
