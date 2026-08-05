---
title: 'Knowledge-Geometry Decoupling: Refreshable Pretrained Transfer for Streaming
  Recommendation'
title_zh: 知识-几何解耦：面向流推荐的可刷新预训练迁移框架
authors:
- Zixuan Wang
- Yuhong Chen
- Yuxuan Zhu
- Guidong Lei
- Zhiluohan Guo
- Yu Zhao
- Kun Wang
- Bangyang Hong
- Kangle Wu
- Yabo Ni
affiliations:
- Xiamen University
- Shopee Pte. Ltd.
arxiv_id: '2608.02738'
url: https://arxiv.org/abs/2608.02738
pdf_url: https://arxiv.org/pdf/2608.02738
published: '2026-08-02'
collected: '2026-08-05'
category: RecSys
direction: 流推荐 · 可刷新预训练迁移
tags:
- Streaming Recommendation
- Pretrain-Transfer
- Sequential Recommendation
- CTR Prediction
- Domain Adaptation
one_liner: 通过知识与几何参数解耦，解决流推荐预训练持续刷新与下游迁移的梯度冲突问题
practical_value: '- 预训练目标可直接复用BMTP思路：无需LLM逐序列推理，离线缓存item的协同/语义相似度阈值过滤监督样本，剔除跨会话虚假依赖，计算成本低可直接落地亿级行为日志场景

  - 迁移架构可借鉴知识-几何解耦设计：预训练编码器冻结仅作只读输出，下游通过正交低秩残差ACR+只读交叉Attention引入任务专属几何，避免预训练刷新与任务梯度冲突，无需重训下游适配层

  - 流迭代流程可直接复用：每日先刷新预训练编码器，再固定编码器更新下游任务模块，训练成本仅增约1倍，无线上推理延迟上涨，适配电商每日流量漂移场景

  - 工业落地收益明确：Shopee首页搜索全流量部署后，单用户GMV提升1.75%，广告收入提升1.53%，无无关推荐率上涨，投入产出比可观'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
工业流推荐已广泛采用预训练-迁移范式，但存在两个核心痛点：1）传统next-token预训练将序列相邻视为行为依赖，会编码跨无关会话的虚假转移噪声，学到的知识可迁移性差；2）预训练知识与下游任务几何对共享参数的优化目标冲突，预训练需随流量漂移持续刷新时，要么任务梯度覆盖预训练知识，要么冻结预训练无法适配新分布。
### 方法关键点
- 预训练优化：提出**BMTP**目标，离线预计算item的协同相似度（共现图）、语义相似度（文本embedding），仅保留相似度超过阈值的未来item作为监督，过滤跨会话噪声，无额外推理成本
- 迁移架构解耦：预训练编码器独立持有行为知识，仅提供只读输出；下游任务通过两个单向接口适配：① **ACR**：在预训练embedding上叠加正交低秩残差，写入任务专属几何且不破坏预训练结构；② 只读交叉Attention：任务Transformer读取编码器上下文表示，梯度不回传编码器
- 流更新流程：每日先刷新预训练编码器，再固定编码器更新下游任务模块，两者迭代互不干扰
### 关键结果
8个Amazon公开数据集上，KGD相比最优基线提升4~12%；Shopee 90天工业流测试中，其余基线均出现性能衰减，KGD效果稳定；线上A/B测试单用户GMV提升1.75%，广告收入提升1.53%，已全量部署。
> 最值得记住的结论：流推荐预训练迁移的核心矛盾是可刷新通用行为知识与任务专属几何结构的参数所有权冲突，解耦而非共享参数是最优解法
