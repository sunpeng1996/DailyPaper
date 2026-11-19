---
title: 'X-split Argus: Learning Reusable History Tokens for Efficient CTR Prediction'
title_zh: X-split Argus：学习可复用历史Token实现高效CTR预估
authors:
- Alexander Ploshkin
- Nikita Stepanov
- Alexey Pismenny
- Viacheslav Ovchinnikov
- Nikolay Savushkin
arxiv_id: '2611.24283'
url: https://arxiv.org/abs/2611.24283
pdf_url: https://arxiv.org/pdf/2611.24283
published: '2026-11-18'
collected: '2026-11-19'
category: RecSys
direction: 推荐系统 · 高效长序列用户建模
tags:
- CTR-Prediction
- Sequential-Modeling
- Knowledge-Distillation
- Long-User-History
- Ranking
one_liner: 提出端到端训练的可复用历史Token CTR预估框架，低延迟下保留70%+全量历史模型收益
practical_value: '- 架构上可直接复用「离线预计算长历史压缩Token + 在线处理近M条行为 + 候选侧Cross-Attention」的范式，平衡长序列建模收益与线上延迟，适合广告/商品排序场景

  - 训练策略可借鉴「蒸馏全量历史大模型logit + 负样本不对称标签平滑」的组合监督，无需改动线上推理逻辑即可提升小模型效果，可保留70%+大模型收益

  - 工程侧可参考调优策略：压缩Token数K≥8、近历史长度M≥256、每日微调模型权重，该配置下仅增加15%GPU成本即可拿到4.65%的业务价值提升'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
CTR预估高度依赖长序列用户行为建模，但在线请求时实时编码全量历史会带来极高的计算与延迟压力，现有离线预计算用户表征的方案难以保留候选感知的精准性，无法在生产约束下拿到全量长序列的全部收益。

### 方法关键点
- 三模块拆分架构：离线历史压缩机将全量长历史编码为K个与候选无关的Token，可跨请求复用；在线Runtime编码器处理近M条行为，可跨候选复用；解码器通过Cross-Attention将候选表征与两类历史Token融合打分
- 端到端联合训练：结合真实点击的交叉熵损失，以及全量历史教师模型logit的L1蒸馏损失，监督压缩Token的信息保留度，同时引入负样本不对称标签平滑缓解曝光误差
- 可灵活配置K（压缩Token数）、M（近历史长度）适配不同的延迟与算力预算

### 关键结果
离线基于内部365天RTB日志、最大8192条行为历史的数据集测试，相对生产基线Context-aware ARGUS的NE相对下降0.81%，保留了71.6%的全量历史教师模型收益；上线十万QPS的RTB系统A/B测试，ACV（广告转化价值）相对提升4.65%，点击量提升2.96%，仅增加15%的在线GPU成本即可满足原延迟预算。

可复用历史压缩+候选感知Cross-Attention+大模型蒸馏的组合，能在工业级生产约束下拿到绝大多数长序列用户建模的业务收益。
