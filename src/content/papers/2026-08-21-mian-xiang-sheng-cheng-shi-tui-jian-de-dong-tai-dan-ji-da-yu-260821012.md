---
title: From a Static Multi-Level Small Semantic Codebook to a Dynamic Single-Level
  Large Semantic Codebook for Generative Recommendation
title_zh: 面向生成式推荐的动态单级大语义码本设计与优化
authors:
- Tianlu Xie
- Xin Ku
- Mingjie Sun
- Yunhao Sha
- Lixiang Wang
- Peng Wang
- Yiyu Wang
- Wenjin Wu
- Zhaojie Liu
- Peng Jiang
affiliations:
- Kuaishou Technology
arxiv_id: '2608.21012'
url: https://arxiv.org/abs/2608.21012
pdf_url: https://arxiv.org/pdf/2608.21012
published: '2026-08-21'
collected: '2026-08-24'
category: GenRec
direction: 生成式推荐 · Semantic ID 码本优化
tags:
- Generative Recommendation
- Semantic ID
- Codebook
- Dynamic Update
- Efficient Inference
one_liner: 将生成式推荐3级Semantic ID简化为2级，结合曝光感知动态更新，同时提升效果与推理效率
practical_value: '- Semantic ID 设计可直接复用「单级大语义码本+独立消歧token」架构，减少自回归解码步数，避免多级码本的条件稀疏问题，降本提效

  - 动态码本更新可照搬3个可落地trick：时序衰减曝光权重、EMA中心更新、高曝光item的SID变更惩罚，平衡适配性与稳定性

  - 可复用论文提出的离线码本评估框架，从5个维度快速筛选候选码本，无需每次重训下游推荐模型，大幅降低迭代成本

  - 工业流量验证短SID收益明确，QPS最高提升47%，核心业务指标提升0.792%，可直接接入现有生成式推荐管线'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有生成式推荐采用的多级残差量化Semantic ID存在三类痛点：一是多1级语义编码就多1步自回归解码，且工业数据显示一级码下二级语义码的平均利用率仅2.48%，空间严重浪费且推理效率低；二是静态码本无法适配线上item新增、流量分布漂移的场景，长期运行效果下降；三是码本迭代需重训下游推荐模型，成本极高，缺乏快速评估维度。

### 方法关键点
- 架构简化：将原2级语义残差编码合并为1个大语义码本，保留基于item稳定Key哈希的独立消歧token，把3级SID缩短为2级，减少1步自回归解码
- 曝光感知动态更新：采用时序衰减的曝光权重做加权聚类，EMA更新码本中心，给高曝光item加SID切换惩罚，既适配流量变化又避免下游模型训练波动
- 离线码本评估框架：从重建质量、码本利用率、集群负载、SID碰撞率、时序稳定性5个维度快速评估码本质量，无需重训下游模型

### 关键结果
在Amazon Beauty、KuaiRec公开数据集上，2级静态SID相比3级baseline，使OneRec-V1的Recall@10提升5.0%~8.8%、NDCG@10提升4.1%~5.1%，动态更新进一步使Recall@10提升1.4%~2.7%；工业5天A/B测试显示，核心消费指标提升0.792%，推理FLOPs降低47.93%~48.70%，单卡QPS提升28.57%~47.0%。

### 最值得记住的一句话
生成式推荐的Semantic ID设计优先做「宽度扩容」而非「深度堆叠」，既能提升效果又能显著降低推理成本。
