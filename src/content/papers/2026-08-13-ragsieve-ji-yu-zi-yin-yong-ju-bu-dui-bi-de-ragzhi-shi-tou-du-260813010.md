---
title: 'RAGSieve: Self-Referenced Local Contrast for Knowledge-Poison Detection in
  Retrieval-Augmented Generation'
title_zh: RAGSieve：基于自引用局部对比的RAG知识投毒检测框架
authors:
- Xinlong Xu
- Yoshua Y. Li
affiliations:
- Nanjing University of Information Science and Technology
- Meituan
arxiv_id: '2608.13010'
url: https://arxiv.org/abs/2608.13010
pdf_url: https://arxiv.org/pdf/2608.13010
published: '2026-08-13'
collected: '2026-08-14'
category: RAG
direction: RAG安全 · 知识投毒检测
tags:
- RAG
- Poison Detection
- Local Contrast
- Corpus Audit
- Query Time Filtering
one_liner: 提出无需可信语料与投毒标签的双链路RAG投毒检测框架，覆盖离线审计与在线过滤
practical_value: '- 在线召回场景可复用RSQ的检索尾局部对比思路：召回时多召15-20条作为本地基线，对比top候选与基线的token分布、语义突变等特征，低成本过滤异常召回的商品/话术/文档，无需额外可信语料或标注

  - 离线语料审计可复用RSG的局部图对比逻辑：为每个文档构造语义相似但词汇不同的邻域，对比邻域密度与局部基线检测异常聚集的恶意内容，适配不同密度的语料分区，无需全局阈值

  - 电商RAG客服/商品导购场景可直接复用双链路部署方案：离线先筛商家上传的商品详情、客服话术等UGC内容，在线用户查询时二次过滤召回结果，仅损失不到1%的正常请求F1的前提下可将攻击成功率从67.4%降至14%'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有RAG投毒检测依赖可信参考语料、特定攻击特征或全局阈值，容易被分散式、伪装式投毒绕过，且工业场景很难获取无污点的可信参考语料与投毒标注，落地门槛极高。

### 方法关键点
- 核心设计自引用局部对比机制，参考基线全部从待检测系统本身生成，无需外部标注或可信语料
- 在线检测模块RSQ：取查询召回top5作为候选，6-20名作为检索尾基线，从答案锚点浓度、脚本完整性、多尺度语义突变、查询对齐突变四个维度打分，过滤异常候选
- 离线检测模块RSG：为每个文档构造语义相似但词汇不同的近邻图，对比强近邻密度与该文档的邻域基线，结合跨字符脚本特征打分，在语料摄入阶段标记异常文档
- 双模块可独立或联合部署，检测后可配合重排序补全上下文，最大程度降低正常请求损失

### 关键结果
在NQ、HotpotQA、MS MARCO三个QA数据集，6种投毒攻击、3种稠密检索器上测试，对比GMTP、CleanBase等SOTA方案：RSQ AUROC达95.2%，5%干净文档删除率下投毒检测率82.2%；RSG AUROC达93.3%，同删除率下检测率79.8%；双模块联合部署攻击成功率从67.4%降至14%，正常查询F1仅从42.1%降至41.3%。

最值得记住的结论：无需外部可信参考的自引用局部对比是RAG安全检测的高性价比落地路径，双阶段覆盖可在极低业务损失下实现有效的投毒防护
