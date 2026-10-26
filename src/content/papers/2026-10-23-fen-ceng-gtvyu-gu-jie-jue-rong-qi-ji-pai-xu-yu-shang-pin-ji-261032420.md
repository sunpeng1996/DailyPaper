---
title: 'Hierarchical GTV Estimation: Bridging the Gap between Container-Level Ranking
  and Item-Level Conversion'
title_zh: 分层GTV预估：解决容器级排序与商品级转化的粒度错配问题
authors:
- Zerong Lan
- Fan Zhang
- Chuang Chen
- Tianchun Huang
- Teng Zhang
- Xingxing Wang
affiliations:
- Meituan
arxiv_id: '2610.32420'
url: https://arxiv.org/abs/2610.32420
pdf_url: https://arxiv.org/pdf/2610.32420
published: '2026-10-23'
collected: '2026-10-26'
category: RecSys
direction: 电商广告价值预估 · 分层建模
tags:
- GTV-Estimation
- Hierarchical-Modeling
- Sponsored-Search
- O2O-Ecommerce
- Ranking
one_liner: 提出分层GTV预估框架HGE，解决容器级排序与商品级转化的粒度错配，落地美团提1.42% RPS
practical_value: '- 高方差回归任务可借鉴PLL策略，将整体目标拆解为概率、数量、定价多个低方差子任务，大幅降低标签噪声影响

  - 容器类（店铺/直播间）排序场景可复用HSAE模块，在Transformer自注意力后注入用户/容器/query特征，兼顾商品间竞争和上下文关联

  - 冷启动/稀疏样本场景可参考RCEF融合方案，通过可学习门控加权组合细粒度分解预估和通用回归结果，平衡精度与鲁棒性

  - 多任务损失设置可参考：主回归任务用Huber loss降低离群值干扰，分类子任务用BCE，子任务权重按数据量级动态调整'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
直播电商、O2O等场景采用容器（直播间/店铺）级排序、商品级交易的分层范式，天然存在粒度错配：直接把容器当超品做GTV预估会忽略内部商品结构，同时面临容器级标签方差大、商品级转化标签稀疏、容器内商品动态异构三大挑战，现有方法无法兼顾排序准确性和GTV校准度，直接影响平台营收和商家ROI。

### 方法关键点
- Hybrid Set-Aware Encoder（HSAE）：取容器内TopK高频商品加位置编码输入Transformer，自注意力层后拼接用户/容器/上下文/query特征输入FFN，同时建模商品间竞争和上下文关联
- Proxy-Label Learning（PLL）：将GTV拆解为「容器级转化概率×∑(商品级购买概率×购买数量×商品单价）」，对应3个独立预测头，通过总方差定律降低标签方差
- Residual Correction and Ensemble Fusion（RCEF）：先加轻量残差塔修正TopK外商品带来的偏差，再通过可学习门控加权融合分解预估结果和通用DIN+DCN回归塔输出，解决稀疏样本下的鲁棒性问题

### 关键实验
离线数据集为美团712M条广告日志，对比WLR、DLRM、RankMixer、CREAD等SOTA基线，HGE实现XAUC+0.63pp提升，PCOC达0.9858（接近理想值1），MAE降低0.09；在线A/B测试13天，RPS（每搜索营收）提升1.42%，已全量落地美团主流量。

**最值得记住的一句话：高方差的价值预估任务，拆解成低方差子任务的收益远高于单模型结构优化**
