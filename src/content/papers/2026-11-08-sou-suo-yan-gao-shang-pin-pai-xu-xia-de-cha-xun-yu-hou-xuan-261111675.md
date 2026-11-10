---
title: Query- and Candidate-Aware Long User Sequence Modeling for Sponsored Product
  Ranking in Search
title_zh: 搜索广告商品排序下的查询与候选感知长用户序列建模
authors:
- Dongyue Xie
- Sergey Kolbin
- Manavender Malgireddy
- Iurii Shcherbak
- Weixing Tang
- Arushi Jain
- Wanchen Shao
- Kurt Zimmer
- Raja Hafiz Affandi
- Matt Lindsay
affiliations:
- Wayfair LLC, USA
arxiv_id: '2611.11675'
url: https://arxiv.org/abs/2611.11675
pdf_url: https://arxiv.org/pdf/2611.11675
published: '2026-11-08'
collected: '2026-11-10'
category: RecSys
direction: 搜索广告排序 · 长用户序列建模
tags:
- Sponsored Search
- User Sequence Modeling
- Ranking
- Long Sequence
- E-commerce
one_liner: 在电商搜索广告排序场景引入双路长序列检索+早融合架构，显著提升CTR、CVR等核心业务指标
practical_value: '- 长序列处理可复用「近期行为+候选NN检索+查询NN检索」的双路召回架构，两种检索结果互补，相比单路检索可多获得约20%的AUC增益，同时可通过控制各段序列长度严格适配
  latency 预算

  - 工程落地可直接复用现有语义模型产出的SKU、query embedding做ANN检索，无需重新训练检索表示，32维低维emb即可满足检索需求，大幅降低存储和lookup耗时

  - 排序侧序列建模必须优先加candidate-aware早融合：将候选emb直接拼入每个历史行为token的输入，该改造的增益远高于全局context token、辅助loss等策略，去掉早
  fusion 会比基线掉点超4%

  - 线上部署可参考100条近期+50条候选检索+50条query检索的序列长度配置，2层小Transformer即可满足性能要求，latency增幅仅12%，适合工业级快速落地'
score: 10
source: arxiv-stat.ML
depth: full_pdf
---

### 动机
工业搜索广告排序通常仅使用短窗口近期用户行为建模，长历史中存储的用户稳定偏好、语义相关行为无法被有效利用；直接处理全量长序列会超出竞价阶段 latency 预算，且大部分历史行为与当前 query、候选商品无关，现有单路候选感知检索会遗漏与 query 高度相关但和候选间接关联的历史行为，无法匹配搜索场景的显式意图建模需求。
### 方法关键点
- 长序列采用三段式构造：100条近期行为 + 50条与候选SKU语义最相似的历史行为（候选NN检索） + 50条与当前query语义最相关的历史行为（查询NN检索），总长度控制在200以内适配 latency 要求
- 序列输入加入独立的query、候选context token，同时将候选SKU embedding直接拼入每个历史行为token的输入层，实现candidate-aware早融合
- 训练采用多任务排序损失+next-action辅助损失，Transformer前层用混合注意力掩码避免标签泄露，后层全双向注意力学习全局交互
### 关键实验
离线基于Wayfair内部1个月测试集，以生产环境仅用近期行为的排序模型为基线，双路检索版本相比基线Click AUC提升1.37%，Order-7d AUC提升2.19%；在线5周A/B测试中，CTR提升6.0%，归因CVR提升5.2%，千次曝光订单量提升11.5%，整体 serving latency 仅增加12%，所有指标均统计显著。
### 核心结论
搜索场景的长用户序列建模必须同时感知当前query和候选商品的双路上下文，token级的候选早融合是比全局context token、辅助loss优先级高得多的优化点。
