---
title: 'RiLM: Parameter-Efficient Language Modeling via Geodesic Decoding'
title_zh: RiLM：基于测地线解码的参数高效语言建模
authors:
- Fang Li
affiliations:
- Oklahoma Christian University
arxiv_id: '2609.10305'
url: https://arxiv.org/abs/2609.10305
pdf_url: https://arxiv.org/pdf/2609.10305
published: '2026-09-09'
collected: '2026-09-10'
category: LLM
direction: 小参数语言模型 · 几何解码参数高效
tags:
- Geodesic Decoding
- Hyperbolic Neural Network
- Parameter Efficient LM
- Riemannian Geometry
- Small LM
one_liner: 移除语言模型输出层，用黎曼流形测地线距离解码，小参数下性能远超各类基线
practical_value: '- 端侧/边缘部署的生成式推荐、Query推荐场景可复用测地线解码思路，去掉W_out层节省约30%参数，将预算倾斜给核心表征模块，适配资源受限场景

  - 商品/内容类目有强层级结构的推荐场景，可尝试将用户兴趣序列建模为庞加莱球上的测地线轨迹，用Möbius变换解决双曲空间边界坍塌问题，提升小参数下兴趣表征精度

  - 电商垂域小对话Agent、搜索Query改写等场景，可复用tied embedding+度量学习解码思路，耦合输入输出表征减少冗余参数，降低垂域适配成本'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
小参数LM（<1M参）是端侧部署、垂域适配的核心选项，但传统架构中输出矩阵W_out会占用近1/3参数预算，压缩隐层维度会直接削弱核心建模能力；tied embedding仅能减少参数冗余，未解决解码与表征脱节的问题；同时语言天然的层级结构在欧氏空间表征会产生失真，双曲空间的指数体积特性未被有效用于序列建模。

### 方法关键点
- 完全移除W_out层，将上下文状态、词向量都映射到同一黎曼流形，下一token概率由当前状态与词向量的测地线距离平方的负指数计算，输入输出共享同一嵌入表
- 实现两个版本：欧氏空间的Flat RiLM、庞加莱球的HypRiLM；针对双曲递归的边界坍塌问题，提出Möbius稳定更新，在原点计算增量再通过Möbius加法迁移到当前状态，避免状态漂移到球边界导致logit平坦
- 共享单MLP作为序列合成函数φ，用截断BPTT训练，核心版本总参数量仅~290k（d=128，词表2k）

### 关键结果
WikiText-2（2k词表）上HypRiLM验证困惑度达54.2±0.2，比同参Flat RiLM低38%，比同参tied SSM基线低52%，比参数量2.7倍的untied LSTM低64%；Penn Treebank（2k词表）上Flat RiLM困惑度40.9±0.6，优于HypRiLM和所有基线；词表扩展到10k时，RiLM系列仍比tied SSM基线低50%以上，Flat RiLM稳定性更优。

参数受限场景下，将表征与解码通过流形几何耦合，比单纯压缩模型、复用嵌入能带来更大的性能增益。
