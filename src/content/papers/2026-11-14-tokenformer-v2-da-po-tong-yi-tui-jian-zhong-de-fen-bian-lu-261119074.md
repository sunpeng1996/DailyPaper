---
title: 'TokenFormer V2: Breaking the Resolution-Complexity Dilemma in Unified Recommendation'
title_zh: TokenFormer V2：打破统一推荐中的分辨率与复杂度困境
authors:
- Kaihui Wu
- Guoming Li
- Liang Guo
- Yifeng Zhou
- Yuehong Hu
- Junwei Pan
- Zhixiang Feng
- Chengguo Yin
- Wenqi Fan
- Haijie Gu
affiliations:
- Tencent Inc.
- The Hong Kong Polytechnic University
arxiv_id: '2611.19074'
url: https://arxiv.org/abs/2611.19074
pdf_url: https://arxiv.org/pdf/2611.19074
published: '2026-11-14'
collected: '2026-11-17'
category: RecSys
direction: 统一推荐 · 长行为序列建模
tags:
- Unified Recommendation
- Long Behavior Modeling
- Transformer
- CTR Prediction
- Industrial RecSys
one_liner: 提出基于分组令牌布局的统一推荐架构，在保留全分辨率行为特征同时大幅降本提效
practical_value: '- 长行为序列建模可直接复用「分组令牌+层级合并」范式，无需压缩历史即可将注意力复杂度控制在O(N)级别，比滑动窗口、历史聚合等方案精度损失更小，适配电商/广告的长用户行为建模场景

  - NS Fusion+Global Sync的跨组通信设计可迁移至多域/多模态行为融合场景，仅用少量通信token完成全局信息交互，避免全量自注意力的二次算力开销

  - 全分辨率读入模块可直接复用到现有CTR/CVR模型的预测头改造，预测阶段直接访问所有原始行为token，对稀疏行为用户、小众兴趣用户的排序精度提升明显

  - 工业部署可参考其分层编码策略，给近期行为分配更深的编码深度，远期行为做轻量编码，在不损失业务效果的前提下进一步压减serving算力'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
工业推荐长期面临分辨率-复杂度困境：长用户行为序列的全量自注意力建模复杂度随长度呈二次增长，无法满足严苛的线上serving预算；而压缩历史行为为聚合向量的方案会丢失细粒度行为证据，直接导致预测精度下降，现有统一推荐架构无法同时实现全分辨率行为保留与低算力开销。
### 方法关键点
- 分组令牌布局：将行为序列拆分为连续段，每段绑定非序列（NS）特征token、组中继（G）token，组内仅做局部注意力，随网络深度层级合并相邻组扩大交互范围，全程保留每个行为的独立token，无任何压缩或丢弃
- 轻量跨组通信：NS Fusion模块融合所有组更新后的非序列特征并重新分发到各组，Global Sync模块仅在G token、读入（O）token间做全局注意力，开销仅与少量通信token数相关
- 全分辨率读入：预测阶段用O token做候选感知交叉注意力，直接访问所有编码后的行为token，完整保留细粒度行为证据供预测使用
### 关键结果
- TAAC 2026基准：比SOTA MixFormer AUC高0.10pp，前向FLOPs仅为其19.5%，推理速度快2.6倍；行为长度扩展到3072时仍保持近似线性的算力增长
- 微信视频号广告百亿级参数离线实验：比MixFormer AUC高0.0712pp，同时FLOPs降低67.1%
- 线上A/B测试：相对生产基线GMV提升2.33%，效果统计显著
### 核心结论
将行为表征分辨率与交互密度解耦，是兼顾长行为建模精度与工业部署效率的可落地路径
