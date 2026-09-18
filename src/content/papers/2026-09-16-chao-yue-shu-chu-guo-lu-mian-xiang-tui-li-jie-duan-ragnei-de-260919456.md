---
title: 'Beyond Private Training: The New Landscape of AI Privacy'
title_zh: 《超越输出过滤：面向推理阶段RAG内存的可外部审计擦除》
authors:
- Sean Culatana
- Kang Li
affiliations:
- Atlassian
arxiv_id: '2609.19456'
url: https://arxiv.org/abs/2609.19456
pdf_url: https://arxiv.org/pdf/2609.19456
published: '2026-09-16'
collected: '2026-09-18'
category: RAG
direction: RAG系统 · 向量索引隐私擦除与审计
tags:
- RAG
- Vector Database
- Privacy
- Erasure Audit
- HNSW
one_liner: 提出TSD-AUDIT框架，实现RAG向量索引的遍历安全删除与第三方可审计验证
practical_value: '- 自建RAG向量索引时需区分输出安全与遍历安全，删除敏感数据不能仅做输出过滤，避免已删除向量仍参与相似度计算泄露隐私

  - 对有GDPR等合规要求的电商/广告RAG场景，可复用TSD-AUDIT的先校验存活再打分、仅用存活节点修复图连通性的实现逻辑

  - 高删除率的定向内容清理场景（如违规商品下架、用户数据擦除），采用TSD-AUDIT可比原生过滤大幅提升Recall@10'
score: 7
source: arxiv-cs.IR
depth: abstract
---

### 动机
现有RAG依赖的图结构向量索引（如HNSW）删除数据时仅做输出过滤，已删除向量仍会在遍历阶段参与相似度计算，存在隐私泄露风险，仅校验返回结果的审计机制无法发现该问题。
### 方法关键点
1. 明确定义输出安全（返回结果无删除项）与遍历安全（遍历阶段不计算已删除向量相似度）两类要求；
2. 提出TSD-AUDIT框架，强制先校验节点存活再打分，仅用存活节点修复索引连通性，同时生成每查询的打分轨迹证书支持第三方校验。
### 关键结果
70%删除率下，原生Faiss HNSW的100次查询全部存在已删除向量参与打分的问题；定向删除场景下，删除率0.5~0.9区间，TSD-AUDIT的Recall@10比原生过滤高4.3~42.2个百分点，随机删除场景下性能与原生方案相当。
