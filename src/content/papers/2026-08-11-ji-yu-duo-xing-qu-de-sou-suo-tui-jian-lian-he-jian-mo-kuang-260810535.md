---
title: Multi Interests for Joint Search-Recommendation Modeling
title_zh: 基于多兴趣的搜索-推荐联合建模框架MIJSR
authors:
- Xiangchen Pan
- Wei Wei
- Huakang Niu
- Zhicong Cheng
affiliations:
- Huazhong University of Science and Technology
arxiv_id: '2608.10535'
url: https://arxiv.org/abs/2608.10535
pdf_url: https://arxiv.org/pdf/2608.10535
published: '2026-08-11'
collected: '2026-08-12'
category: RecSys
direction: 搜索-推荐联合建模 · 多兴趣挖掘
tags:
- Multi-Interest
- Joint Search-Recommendation
- Contrastive Learning
- Multi-Task Learning
- Sequential Modeling
one_liner: 从结构与语义双维度挖掘搜索推荐混合序列多兴趣，同时提升两类任务效果
practical_value: '- 可直接复用双维度多兴趣拆分方案：结构侧拆分搜索/推荐/跨域兴趣，语义侧基于query聚类拆分语义兴趣，解决混合行为序列的兴趣耦合问题

  - 搜索推荐联合建模时，可先用对比学习做query和item的表征对齐，再用序列级对齐损失将item映射到query语义空间，降低跨域特征差异

  - 多任务预测模块直接复用PLE结构，缓解搜索和推荐任务的负迁移，对比普通MLP有稳定提升

  - 语义聚类的簇数k建议设为10左右，太小兴趣粒度太粗，太大容易出现稀疏噪声导致效果下降'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有搜索推荐联合建模方案多直接混合异构行为序列，忽略了不同场景下的多兴趣表达，容易出现长短兴趣耦合、query语义信息利用不充分的问题，导致两个任务的效果无法同时提升。

### 方法关键点
- 跨域行为融合：用对比学习对齐query和对应点击item的表征，统一跨域特征空间
- 多兴趣挖掘：结构侧拆分搜索/推荐/跨域三类兴趣，其中跨域兴趣通过掩码自注意力仅建模不同类型行为的转换；语义侧先对所有query做K-Means聚类，用序列级对齐损失将item映射到query语义空间，再按聚类标签拆分混合序列得到语义多兴趣，新增正交损失降低不同语义兴趣的冗余度
- 多任务预测：采用PLE分层专家结构，分别设置搜索、推荐专属专家和共享专家，自适应融合多兴趣后完成双任务预测

### 关键实验
在KuaiSAR、Amazon两个公开数据集上，对比15个SOTA基线（包含单场景顺序推荐、个性化搜索、联合建模三类）；搜索任务上KuaiSAR数据集HR@5提升4.48%、NDCG@5提升3.4%，Amazon数据集NDCG@5提升4.14%；推荐任务上Amazon数据集HR@5提升4.39%、NDCG@5提升4.85%，KuaiSAR数据集效果与SOTA持平，双任务整体效果最优。

**最值得记住的一句话**：搜索推荐联合建模中，结构+语义双维度的多兴趣拆分，能有效解决异构行为序列的兴趣耦合问题，实现双任务的协同提升。
