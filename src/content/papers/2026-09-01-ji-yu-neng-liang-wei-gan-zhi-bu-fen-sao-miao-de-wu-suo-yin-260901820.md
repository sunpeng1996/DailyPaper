---
title: Index-Free Dynamic Edge Retrieval with Energy-Tail-Aware Partial Scans
title_zh: 基于能量尾感知部分扫描的无索引动态边缘检索方法
authors:
- Mohammad Arif Rasyidi
- Omar Alhussein
affiliations:
- Khalifa University
arxiv_id: '2609.01820'
url: https://arxiv.org/abs/2609.01820
pdf_url: https://arxiv.org/pdf/2609.01820
published: '2026-09-01'
collected: '2026-09-03'
category: RecSys
direction: 动态MIPS · 端侧向量检索
tags:
- Dynamic-MIPS
- Index-Free-Retrieval
- Edge-Computing
- Vector-Search
- Quantization
one_liner: 提出无索引ETAR动态MIPS方法，兼顾低更新开销与高检索效率，性能优于全扫描与传统索引
practical_value: '- 端侧个性化推荐/端侧Agent的本地向量检索可直接复用ETAR架构，无索引维护成本，适配用户偏好实时更新场景，比全扫描快4~7倍，资源开销远低于HNSW等索引方案

  - 高更新频率的召回场景（如电商实时上新商品向量召回、实时用户行为检索）可借鉴能量尾感知候选生成逻辑：仅计算query能量占比最高的部分坐标内积，加尾项修正后选Top-R候选重排，可在召回损失可控的前提下大幅降低计算量

  - 存储受限的端侧场景可采用ETAR-LM的双8bit量化存储方案：列存8bit码用于快速候选筛选，行存8bit码用于重排，存储开销仅为全精度的51%，Recall@10损失不到3%

  - 流式向量库场景可直接复用ETAR的更新逻辑：仅需修改向量本身与删除标记，无需重建索引，单条更新延迟低至0.002ms，远低于索引类方案'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
端侧个性化推荐、RAG推理、传感器匹配等场景需要频繁执行向量检索，同时向量库会随用户行为、新数据摄入动态更新。传统全扫描方案更新简单但查询效率低，HNSW、IVF等索引方案查询快但需要维护复杂的索引结构，动态更新时开销极高，甚至需要定期全量重建索引，无法适配端侧受限资源与高动态场景的需求。
### 方法关键点
- 双存储视图设计：每个向量存两份量化表示，列存8bit编码按坐标对齐用于快速候选扫描，行存全精度32bit/8bit编码用于候选重排，更新时仅需编码新向量插入即可，无需全局调整
- 能量感知坐标选择：对每个query，选择平方值之和占总能量比例≥ρ的top-h个坐标，仅用这部分坐标计算候选向量的部分内积，大幅降低计算量
- 尾项修正评分：基于统计的坐标能量分布预估跳过坐标的内积贡献，给部分内积加修正项得到候选评分，避免漏选高相关向量
- 两阶段检索：先用低精度部分内积选Top-R候选，再用全精度向量计算完整内积重排得到最终Top-K结果
### 关键实验
在9个公开静态数据集、5个流式更新工作负载、ARM移动端设备上测试，对比全扫描、Faiss HNSW、IVF、ScaNN等基线：静态场景下ETAR达到99.2% Recall@10，比全扫描快4.5倍，移动端最高快6.9倍；流式更新场景下无需索引重建，全程保持100% Recall@10，单条更新延迟低至0.002ms，端到端事件耗时比HNSW低一个数量级；ETAR-LM版本存储仅为全精度的51%，Recall@10仍达97.2%。
### 核心结论
无索引的轻量动态MIPS方案在高更新、资源受限场景下的性价比远高于传统索引方案，通过「轻量粗筛+精确重排」的两阶段架构可平衡效率、精度与更新开销。
