---
title: 'HF-SID: High-Fidelity Semantic IDs for Generative Retrieval in Location-Based
  Services'
title_zh: HF-SID：面向位置服务生成式检索的高保真语义ID
authors:
- Haowen Lin
- Jing Li
- Zhibin Hao
- Fangye Wang
- Lihui Su
- Song Yang
- Xiaojiang Zhou
- Pengjie Wang
affiliations:
- AMAP, Alibaba Group
- University of Science and Technology of China
- Tsinghua University
- Peking University
arxiv_id: '2608.30479'
url: https://arxiv.org/abs/2608.30479
pdf_url: https://arxiv.org/pdf/2608.30479
published: '2026-08-31'
collected: '2026-09-01'
category: GenRec
direction: 生成式推荐 · POI Semantic ID 生成
tags:
- Semantic ID
- Generative Retrieval
- POI Recommendation
- LBS
- LLM4Rec
one_liner: 通过预训练数值编码器与分层对比学习生成短序列高保真POI语义ID，提升LBS生成式检索效果
practical_value: '- 数值属性编码可直接复用：将经纬度转换为3D笛卡尔坐标，所有多尺度数值属性（价格、评分、销量等）统一做极分解+预训练数值编码器，避免分词破坏数值连续性，适合带地理位置/多维度数值属性的商品、POI推荐场景

  - Semantic ID分层优化范式可迁移：前两层量化保留全局核心语义，仅在最后一层残差上添加结构化对比学习，不破坏粗粒度语义的同时解决细粒度区分问题，平衡全局一致性与局部区分度

  - 小样本持续预训练方法低成本：用简单的数值推理任务（距离计算、属性对比）做增量预训练对齐LLM对结构化属性的感知，不需要大规模标注数据，适合工业界快速迭代

  - 短ID设计适配线上低延迟要求：3-token短ID即可实现优于更长ID的效果，无额外解码成本，可直接落地到对延迟要求高的生成式检索/推荐链路'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
生成式检索中Semantic ID（SID）是物品信息输入LLM的唯一通道，编码阶段丢失的信息在解码阶段完全无法恢复；LBS场景下现有POI SID方案存在三大痛点：LLM分词破坏经纬度连续性，硬编码网格导致相邻POI编码无关；多尺度数值属性（评分、访问量等）序列化后丢失尺度感知；仅靠文本无法区分同粗标签、同区域的细粒度POI，且现有方案普遍通过延长SID长度提效，大幅增加解码成本。
### 方法关键点
- 坐标转换：将经纬度从球面坐标转为3D笛卡尔坐标，欧氏距离与真实地理距离单调正相关，消除网格边界割裂问题
- 数值统一编码：所有数值属性做极分解（符号+整数位+三角函数编码小数位），预训练MLP数值编码器生成单token连续嵌入，搭配Type Embedding区分数值属性类型，避免不同尺度属性混淆
- 两阶段持续预训练：Geo-CPT用距离计算、最近邻识别任务对齐LLM空间感知，Num-CPT用跨属性对比任务强化数值尺度感知
- 分层量化+残差对比学习：前两层RQ量化保留地理/数值全局语义，仅在最后一层残差上添加需两层标签全匹配的对比学习，分离同区域同粗标签的细粒度POI，最终生成3-token SID无额外解码开销
### 关键结果
在高德工业数据集AMAP-L（4810万POI）上对比7个SID基线，平均组内地理距离降低95.9%，Hit@200相对最强基线提升3.66个百分点；线上A/B测试平均PV_CVR提升6.74%、UV_CVR提升6.03%，旅游景点场景PV_CVR涨幅达11.51%。
### 核心结论
Semantic ID的性能上限由编码阶段的信息保真度决定，而非后期的量化或码本优化。
