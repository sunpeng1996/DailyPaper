---
title: 'TransRetrieval: Scaling Up Transformer-Based Retrieval for Industrial Recommendation'
title_zh: TransRetrieval：面向工业推荐的可扩展Transformer检索框架
authors:
- Zhifei Zheng
- Yunfei Liu
- Bin Liu
- Qiren Zhu
- Hanbing Liu
- Ziru Xu
- Han Zhu
- Jian Xu
- Qi Qi
- Bo Zheng
affiliations:
- Renmin University of China
- Taobao & Tmall Group of Alibaba
arxiv_id: '2608.25528'
url: https://arxiv.org/abs/2608.25528
pdf_url: https://arxiv.org/pdf/2608.25528
published: '2026-08-26'
collected: '2026-08-27'
category: RecSys
direction: 工业推荐召回 · Transformer可扩展优化
tags:
- Transformer Retrieval
- Scaling Law
- Multi-domain Recommendation
- Model-based Retrieval
- Recall Optimization
one_liner: 解决推荐检索场景Transformer异质性瓶颈，实现可预测缩放，上线提2.53%营收
practical_value: '- 特征聚合侧可直接替换加权求和为加权平均，无需额外参数即可解决异质特征范数偏差问题，快速提升Transformer在推荐场景的表现

  - 检索侧候选特征用3层轻量MLP压缩为单Token，可降低85%单候选FLOPs，省出的算力可投入Transformer深度/宽度缩放，投入产出比远高于多Token小模型方案

  - 多域场景用Position-style Domain Embedding，通过元素相加注入域信息，无需增加序列长度即可实现跨域数据复用，尤其能提升稀疏域的模型效果

  - 工程上可复用用户侧KV cache、批量打包候选计算、部署GPU端全链路检索流程，可降低89%检索延迟，满足工业级高QPS要求'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
大模型的缩放定律在推荐检索场景难以落地：推荐异质特征（用户属性、行为序列、物品属性）映射为Token后范数偏差严重，直接堆叠Transformer层收益递减；同时检索侧单请求需处理十万级候选、延迟要求严苛、多域数据分布冲突，现有可扩展推荐方案多针对排序阶段，检索侧无成熟落地方案。
### 方法关键点
- 加权平均聚合替换传统加权求和，消除特征基数对Token范数的影响，恢复Transformer依赖的同质Token假设，无额外参数开销
- 候选侧用3层MLP将所有特征压缩为单D维Token，单候选FLOPs降低85%，同时复用单请求用户侧KV cache，进一步压缩推理成本
- 位置式域嵌入：将域ID对应向量逐元素加至所有Token，无额外计算成本即可统一多域训练，实现跨域数据增益，稀疏域也能获益
### 关键结果
在阿里400亿交互工业数据集、公开KuaiRand基准上，单候选算力从0.1MFLOPs升至2MFLOPs时，Recall@2000分别提升19.3、22.2个百分点，呈稳定对数线性缩放；线上A/B测试同延迟约束下，平台营收提升2.53%，RPM提升1.28%，效果优于所有SOTA基线。
### 核心启示
推荐场景缩放Transformer的核心突破不一定来自复杂架构创新，先解决输入特征的范数对齐问题，能以极低成本释放缩放潜力。
