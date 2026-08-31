---
title: 'HubMixer: Progressive Latent Hub Mixing for Parameter-Efficient Feature Interaction
  in Recommendation'
title_zh: HubMixer：推荐系统参数高效特征交互的渐进式潜中心混合架构
authors:
- Jie Zhou
- Zixian Gong
- Wenhao Li
- Chang Liu
- Enzhao Shen
- Bo Liu
- Xu Guo
- Fei Pan
- Peng Jiang
affiliations:
- Kuaishou Technology
- Tsinghua University
arxiv_id: '2608.27991'
url: https://arxiv.org/abs/2608.27991
pdf_url: https://arxiv.org/pdf/2608.27991
published: '2026-08-28'
collected: '2026-08-31'
category: RecSys
direction: 推荐排序 · 特征交互建模
tags:
- Feature Interaction
- Ranking Model
- Token Mixing
- Parameter Efficient
- Industrial RecSys
one_liner: 提出基于可学习潜中心的诱导-交互-读出范式，实现参数高效的异构推荐特征交互，已落地快手招聘业务
practical_value: '- 可直接替换现有CTR/CVR排序模型中的特征交互模块（如DCN、TokenMixer），在异构特征多的电商、内容推荐场景下，用更少参数获得更好的多目标效果

  - 工程调优可参考H=16的性价比配置，H远小于token数T时复杂度为O(TH)，远低于标准自注意力的O(T²)，适配线上低延迟推理要求，可根据算力预算灵活调整H的大小

  - 多目标排序场景可复用token-conditioned readout设计，避免全局池化丢失特征域特异性，下游多任务头可更灵活抽取不同目标（如点击、加购、成交）所需的特征信号

  - 落地改造代价低，可作为共享特征交互层直接接入现有MTL训练推理pipeline，不需要大幅重构即可获得业务指标提升，参考快手5.48%的转化增益'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
工业推荐/广告排序的输入特征（用户画像、行为序列、物品属性、上下文、统计信号）高度异构，有效交互稀疏且样本依赖，现有token-mixing类架构直接在原始token空间做全量混合，参数效率极低，大量算力浪费在无意义的特征配对上，亟需适配异构特征的高效交互范式。
### 方法关键点
- 堆叠HubMixer块，每块遵循**诱导-交互-读出**三阶段范式，用远小于token数T的可学习潜中心H作为交互中介，复杂度从O(T²)降至O(TH)
- 潜中心融合静态可学习原型与输入全局均值生成的动态残差，适配样本级上下文
- 诱导阶段：潜中心作为query通过cross-attention选择性聚合异构特征token的信息
- 交互阶段：在紧凑的潜中心空间做self-attention建模高阶交互，计算成本可忽略
- 读出阶段：每个原始特征token作为query从交互后的潜中心拉取定制化信息，通过LayerScale残差写回原token，保留特征域独立性
- 输出增强后的token直接接入下游多任务头，无需全局池化
### 关键实验
在快手短视频招聘业务10亿+样本多任务数据集上测试，对比DCN、DCNv2、AutoInt、RankMixer、TokenMixer等基线：离线平均AUC比最强基线TokenMixer高0.15pp，参数量减少14.5M；线上A/B测试覆盖7.2%流量，简历提交转化率提升5.48%，已全量部署。
### 核心结论
面向异构特征的交互建模，先通过可学习潜中心聚合再交互再定制化分发的范式，能同时提升效果和参数效率，工业落地性价比极高
