---
title: 'Holo-NN: Holographic Nearest Neighbor Search via Compressive Sensing'
title_zh: 基于压缩感知的隐私保护全息近邻搜索框架Holo-NN
authors:
- Bryant Gipson
affiliations:
- Google
arxiv_id: '2610.33224'
url: https://arxiv.org/abs/2610.33224
pdf_url: https://arxiv.org/pdf/2610.33224
published: '2026-10-23'
collected: '2026-10-27'
category: RecSys
direction: 隐私保护向量检索 · 压缩感知
tags:
- ANN
- Privacy-preserving Retrieval
- Compressive Sensing
- FHE
- Vector Search
one_liner: 将隐私近似近邻搜索重构成单轮线性压缩感知问题，无需FHE引导实现低开销可扩展检索
practical_value: '- 隐私合规场景（用户行为向量检索、个性化推荐不泄露query）可复用单轮线性算子设计，规避FHE bootstrapping的高昂开销，满足单服务器隐私约束

  - 高维语义向量检索场景可借鉴Asymmetric FlyHash trick：数据库侧用极稀疏编码压缩索引、query侧放宽激活阈值，无额外带宽开销解决双量化丢失问题

  - 大库检索架构可参考「离线预计算全息感知矩阵+在线单矩阵乘」范式，大幅降低在线计算复杂度，天然适配GPU并行加速

  - 召回链路可复用「高覆盖率粗筛+轻量重排」思路：用Holo-NN先召回top50候选覆盖98%真实近邻，再做轻量精确重排，平衡性能与精度'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
隐私保护ANN搜索是AI时代合规检索的核心需求，传统HNSW、ScaNN等索引依赖非线性分支操作，在FHE或盲服务器约束下存在内存访问模式泄露风险；现有私有ANN方案要么需要多轮交互、多服务器非共谋假设，要么带宽/延迟开销极高，无法适配生产级大库检索需求。

### 方法关键点
- 重构ANN搜索为稀疏信号恢复问题：利用近邻隶属关系天然稀疏的特性，通过RFF（欧氏空间）或非对称FlyHash（语义超球面）将距离转化为高维空间线性内积，生成稀疏相似性向量
- 离线预计算全息感知矩阵：将数据库嵌入矩阵与伪随机测量矩阵相乘得到压缩的H矩阵，无需存储原始大库嵌入
- 在线查询仅需单轮矩阵乘：服务器对加密的query嵌入做线性运算得到压缩测量向量，无FHE bootstrapping、无多轮交互，客户端本地通过LASSO恢复稀疏相似性向量得到候选集
- 支持精度-带宽-算力灵活调优：可通过调整测量维度M、特征维度B等参数，离线标定数据集专属的帕累托最优工作点

### 关键结果
在SIFT-1M、GloVe-25等标准数据集上测试，对比SANNS、Panther、Compass等SOTA私有ANN方案：基于32位CKKS GPU后端的Holo-NN在SIFT-1M上实现单轮0.26~1.30s延迟，带宽仅2.10~8.65MB，比Panther带宽降低8.3~44.2倍，比SANNS降低159~843倍；1-recall@10最高达98.5%，top50候选覆盖98%真实10近邻。

### 核心结论
Holo-NN本质是高覆盖率的粗召回方案而非精确排序器，搭配下游轻量重排即可在隐私场景下达到生产级可用的精度与性能。
