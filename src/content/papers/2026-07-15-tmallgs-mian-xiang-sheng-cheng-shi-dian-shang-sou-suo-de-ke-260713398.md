---
title: 'TMallGS: Scaling Unified Feature and Sequence Modeling for Generative E-commerce
  Search'
title_zh: TMallGS：面向生成式电商搜索的可扩展统一特征与序列建模架构
authors:
- Zhentao Song
- Yufeng Gao
- Xing Fang
- Jing Wang
- Guangxin Song
- Bokang Wang
- Yipin Dai
- He Guo
affiliations:
- Southeast University
- Taobao & Tmall Group of Alibaba
- Peking University
arxiv_id: '2607.13398'
url: https://arxiv.org/abs/2607.13398
pdf_url: https://arxiv.org/pdf/2607.13398
published: '2026-07-15'
collected: '2026-07-16'
category: RecSys
direction: 推荐系统 · 可扩展Transformer精排架构
tags:
- CTR Prediction
- Ranking Model
- Transformer
- Scaling Law
- E-commerce Search
one_liner: 适配电商搜索精排的可扩展Transformer架构，离线GAUC+1.26%，线上GMV+1.52%
practical_value: '- 特征处理可复用分层分布校准Tokenization方案：先通过FSR做域级重要性重加权，再用DCP完成特征投影，比SwiGLU-FFN节省33%投影FLOPs，同时缓解异构特征梯度冲突

  - 精排Transformer改造可直接复用3个设计：域专属QKV投影、上下文主导注意力掩码（避免候选间信息泄露）、噪声自适应门控，适配长序列建模和搜索强匹配约束

  - 硬信号保留可采用Decoupled FiLM晚融合方案：在输出层用Query-Item匹配分这类高频硬信号调制语义表征，避免深层Transformer低通滤波导致的信号稀释，实测可提0.32%+GAUC

  - 存量模型迁移可复用两阶段预热方案：先冻结现有稀疏embedding训练稠密骨干，再联合微调，解决流形错位问题，比直接加载旧embedding多提1%左右GAUC'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
传统DLRM类精排模型为内存绑定架构，GPU MFU极低，参数量scaling边际收益递减；直接套用LLM全token化Transformer架构，会面临异构特征梯度冲突、高频硬匹配信号被深层注意力稀释、CTR稀疏监督下深层训练不稳定三大问题，无法适配电商搜索精排的强Query约束需求。

### 方法关键点
- 分层分布校准Tokenization：先做域级显著性重加权（FSR）抑制全局噪声，再用分布校准投影（DCP）将异构特征映射到对齐子空间，比SwiGLU省33% FLOPs
- 域自适应门控Transformer骨干：分域做QKV投影，搭配上下文主导掩码（候选间不可见）和噪声自适应门控，过滤长行为序列噪声
- 解耦FiLM晚融合：在输出层用Query-Item交叉特征动态调制语义表征，保留高频匹配信号
- 上下文感知偏置解耦：用全局锚点token的表征单独建模位置、分页等系统偏置，pairwise loss训练时偏置项自动抵消，专注优化相对相关性
- 错误感知渐进训练：每层加辅助头，用前一层的预测误差动态加权后一层损失，实现自适应难样本挖掘

### 关键结果
基于天猫31天5亿+搜索样本（平均行为序列长1500），对比DIN、DCNv2、OneTrans、RankMixer等SOTA：离线GAUC相对DIN提升1.26%、AUC+1.12%；线上30天AB测UCTCVR+1.38%、GMV+1.52%，仅增加6ms延迟，符合生产SLA；模型符合scaling law，增加计算量性能单调增长。

最值得记住的结论：电商搜索精排从内存绑定DLRM转向计算绑定Transformer架构的核心是「语义交互解耦」，而非直接套用LLM的全token化范式。
