---
title: 'SetMIR: Multi-Interest Retrieval as Set Prediction'
title_zh: SetMIR：将多兴趣检索建模为集合预测问题
authors:
- Xiaodong Liu
- Congfei Zhang
- Hsiang-wei Chao
- Siman Wang
- Xiao Bai
- Tong Zhao
- Jingxiao Ma
- Wen Zhang
- Zhe Liu
- Shantanu Aggarwal
affiliations:
- Snap Inc.
arxiv_id: '2608.30251'
url: https://arxiv.org/abs/2608.30251
pdf_url: https://arxiv.org/pdf/2608.30251
published: '2026-08-31'
collected: '2026-09-01'
category: RecSys
direction: 推荐系统召回 · 多兴趣检索
tags:
- Multi-Interest Retrieval
- Set Prediction
- Hungarian Matching
- ANN Search
- Recommendation System
one_liner: 将集合预测与匈牙利匹配引入多兴趣检索，解决兴趣坍缩与静态调度问题，降低推理开销
practical_value: '- 训练侧可直接替换现有多兴趣模型的argmax目标匹配逻辑，改用匈牙利匹配做一对一分配，从目标层面解决兴趣坍缩，无需额外添加复杂正则项

  - 推理侧新增presence得分门控+query级NMS策略，可在几乎无损召回的前提下减少约30%的ANN查询量，降低检索链路算力成本，适配高并发电商/广告召回场景

  - 用户行为序列编码可复用α-gated事件类型嵌入技巧，α初始值设为0逐步学习，可稳定提升顶部排序的召回效果，尤其对R@1、MRR指标增益明显

  - 部署无需修改现有单向量ANN索引，仅替换用户塔即可，改造成本极低，可快速接入现有推荐/广告召回链路'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
工业推荐召回阶段，单用户embedding无法覆盖用户多元兴趣，现有多兴趣检索方案存在两个核心痛点：一是兴趣坍缩，多embedding容易学到重复表征，有效兴趣数量远低于设定值；二是静态调度，不管用户实际兴趣数量固定发起K次ANN查询，既浪费算力，冗余候选还会干扰下游排序。

### 方法关键点
- 架构：采用Transformer编码器编码用户行为序列，搭配K个全局共享的可学习兴趣query的Transformer解码器，输出每个兴趣的embedding与presence激活得分
- 训练：用匈牙利匹配实现目标item与兴趣query的一对一分配，匹配上的query计算InfoNCE检索损失，未匹配的query计算presence二分类损失，补充轻量多样性损失抑制兴趣重叠
- 推理：先通过presence门控过滤低置信度兴趣，再用query级NMS去重，仅激活的兴趣发起ANN查询，动态分配检索配额，返回结果按最大得分合并

### 关键结果
离线在Snap DPA电商广告数据集上对比MIND、ComiRec、KuaiFormer等4个主流多兴趣基线，所有指标全面领先，同时减少33%的ANN查询量；相比单兴趣检索，R@10提升55%。线上接入生产召回链路后，整体CVR提升3.1%；与同配置的I2I召回源相比，CTR提升44%、CVR提升51%。

### 核心启示
多兴趣检索的核心不是生成更多embedding，而是生成恰好足够的非重叠有效兴趣，同时控制检索成本。
