---
title: 'SentAttack: A Sentence-Level Black-Box Adversarial Attack Method for Dense
  Retrieval Models'
title_zh: SentAttack：面向稠密检索模型的句子级黑盒对抗攻击方法
authors:
- Luping Wei
- Yamin Hu
- Sihan Shang
- Shiyin Wang
- Wenjian Luo
affiliations:
- 哈尔滨工业大学（深圳）计算机科学与技术学院
arxiv_id: '2607.03456'
url: https://arxiv.org/abs/2607.03456
pdf_url: https://arxiv.org/pdf/2607.03456
published: '2026-07-03'
collected: '2026-07-07'
category: RAG
direction: RAG鲁棒性 · 稠密检索对抗攻击
tags:
- Adversarial Attack
- Dense Retrieval
- RAG
- Black-box Attack
- Sentence-level Perturbation
one_liner: 提出两阶段句子级黑盒攻击方法，可有效提升低排序无关文档在稠密检索中的排名
practical_value: '- 电商搜索风控场景可参考该攻击逻辑，挖掘恶意商家篡改商品描述刷排名的潜在风险，提前设计防御规则

  - 自研RAG/语义搜索系统做鲁棒性评测时，可复用该方法构造对抗样本，验证稠密检索模块的抗干扰能力

  - 黑盒场景下需要对齐目标模型行为时，可借鉴迭代收集排序数据训练代理模型的方案，降低对齐成本'
score: 7
source: arxiv-cs.IR
depth: abstract
---

### 动机
现有RAG系统鲁棒性研究多聚焦重排序模块，针对稠密检索（DR）模型的对抗攻击仅支持词级别扰动，无法有效误导DR将低排名的无关文档提升到前排，难以充分验证DR模块的安全隐患。
### 方法关键点
提出两阶段黑盒攻击框架SentAttack：
1. 迭代访问黑盒RAG系统获取返回的排序文档与排名信息，训练代理DR模型对齐目标黑盒DR的行为；
2. 用代理DR编码目标query的相关文档做聚类得到多个质心，将质心对应语义在句子层面拼接到目标无关文档生成初始对抗候选，再通过query+质心引导的目标函数结合梯度引导束搜索优化候选。
### 关键结果
实验显示SentAttack效果全面优于现有DR对抗攻击基线，对低排名无关文档的攻击提升幅度远高于词级别攻击方法。
