---
title: 'Spruce: Scalable Private Outsourced Retrieval Using Compact Embeddings'
title_zh: Spruce：基于紧凑嵌入的可扩展隐私外包检索系统
authors:
- Peichun Hua
- Yunming Xiao
affiliations:
- The Chinese University of Hong Kong, Shenzhen
- State Key Laboratory of Internet Architecture, Tsinghua University
arxiv_id: '2609.03376'
url: https://arxiv.org/abs/2609.03376
pdf_url: https://arxiv.org/pdf/2609.03376
published: '2026-09-03'
collected: '2026-09-04'
category: RAG
direction: RAG隐私检索 · 双服务器MPC+深度哈希
tags:
- RAG
- Secure Retrieval
- MPC
- Deep Hashing
- Privacy Preserving
one_liner: 联合设计紧凑二进制哈希与双服务器MPC协议，大幅降低隐私检索的延迟与通信开销
practical_value: '- 做合规隐私RAG检索（电商用户查询、商品知识库保护等）可直接复用「紧凑哈希隐私粗过滤+本地全精度重排」的两级架构，平衡隐私、性能与检索效果

  - 深度哈希训练trick可迁移：LoRA微调双编码器加哈希头，搭配InfoNCE+列表式margin损失+教师锚定蒸馏，无需额外码平衡正则即可生成高质量短哈希码，适合端侧/隐私场景向量压缩

  - 离线预校准固定阈值替代在线多轮Top-K选择的思路，可迁移到所有隐私排序场景（如隐私广告出价、隐私推荐排序），大幅降低MPC交互开销

  - 对延迟要求高、可接受微小精度损失的业务，可复用私有聚类剪枝优化，实测提效13~22倍，NDCG损失不到3%，性价比极高'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
当前企业普遍将RAG向量索引外包给公有云，云服务商可获取企业私有知识库与用户查询向量，通过向量逆推攻击可还原明文内容，存在严重隐私泄露风险。传统全精度MPC隐私检索方案开销极高，百万级文档单查询延迟达数分钟、通信量超80GB，完全无法满足业务可用性要求。

### 方法关键点
- 联合设计哈希表示与MPC协议：用LoRA微调预训练双编码器，新增轻量哈希头生成128位二进制哈希码，将全向量余弦计算替换为MPC友好的汉明距离计算
- 离线校准固定半径候选选择：提前用小批量校准集确定最小汉明距离阈值，保证重排后NDCG达到目标保留率，避免在线多轮Top-K选择开销
- 部署优化：私有聚类剪枝仅检索最近的p个桶，用微小精度损失换大幅性能提升；企业侧轻量可信节点生成Beaver三元组，消除云侧OT预处理瓶颈

### 关键结果
在4个BEIR数据集（38万~542万文档）上测试：全扫描模式延迟0.21~2.97秒，比SOTA快4.8~6.7倍，NDCG保留全精度检索的95.2%~97.8%；开启剪枝后延迟0.06~1.09秒，比SOTA快13.1~22.9倍，NDCG保留原精度的93.9%~97.3%，搭配可信节点后吞吐量提升31.5倍。

**最值得记住的一句话**：隐私检索场景下，表示层压缩优化的投入产出比远高于单纯优化密码学协议。
