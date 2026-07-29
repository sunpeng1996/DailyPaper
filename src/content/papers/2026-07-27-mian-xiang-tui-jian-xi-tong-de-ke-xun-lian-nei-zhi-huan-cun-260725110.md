---
title: 'Memory Layer: Train the In-Model Cache for Recommendation Models'
title_zh: 面向推荐系统的可训练内置缓存记忆层
authors:
- Liangyuan Na
- Gufan Yin
- Yixin Bao
- Xianjie Chen
- Justin Lin
- Ziheng huang
- Xinyuan Zhang
- Wen Zhang
- Hao Lin
- Xiaoheng Mao
affiliations:
- Meta
arxiv_id: '2607.25110'
url: https://arxiv.org/abs/2607.25110
pdf_url: https://arxiv.org/pdf/2607.25110
published: '2026-07-27'
collected: '2026-07-29'
category: RecSys
direction: 推荐系统 · 训推一致性与冷启动优化
tags:
- Recommendation System
- Training-Serving Consistency
- Cold Start
- Embedding Cache
- Early Ranking
one_liner: 将推荐系统serving只读缓存改造为训推共享的可训练记忆层，消除训推差异，提升冷启动效果与运行效率
practical_value: '- 可直接复用Writeback机制：用η=1的EXACT_SGD实现embedding缓存的精确写入，无需额外损失调参，即可将item
  embedding缓存纳入训练链路，消除表征层面的训推差异，减少多链路运维成本

  - 冷启动优化可复用always-on embedding设计：拆分商品特征为缓存储存的独有特征和小体量通用特征（如商家ID、类目ID），缓存miss时自动兜底为通用特征embedding，训练阶段就融合两种表征，避免缓存miss直接给低分的问题，大幅提升新品冷启动效果

  - 实时embedding更新可参考Raw Embedding Streaming设计：在训练侧embedding预取阶段异步捕获更新值，批量推送到serving节点，无需额外的流更新集群，即可将embedding更新延迟降到20s级别，适配热点商品、大促等实时性要求高的场景

  - 可借鉴Multi-Table Training思路：训练时同时加载训练样本流和全候选池流，合并过item tower批量写入缓存，省去独立的离线全量embedding预计算任务，可降低30%左右的训练发布计算成本'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
工业级推荐系统早期排序阶段需在十毫秒级延迟下完成千级候选打分，普遍采用离线预计算item embedding、serving内置缓存查询的架构，但缓存仅在serving侧存在、完全脱离训练链路，导致三大结构性训推差异：item tower参数陈旧、特征源不一致、缓存miss逻辑训练时从未见过，最终带来5-12%的Normalized Entropy(NE)训推gap，同时冷启动内容缓存命中率低、embedding更新延迟达5分钟级别，运维三套独立的参数/embedding更新链路复杂度极高。
### 方法关键点
- 模型层：引入训推共享的KV记忆层作为item表征唯一来源，训练时通过Writeback机制（设置SGD学习率为1，将梯度设为缓存值减item tower输出，实现缓存值的精确赋值）写入embedding，训练与serving均从该表读取表征，从根源消除表征差异；新增always-on embedding模块，拆分item特征为缓存特征和小体量通用特征，缓存miss时用通用特征embedding兜底，实现100%预测覆盖
- 工程层：采用MPZCH零冲突哈希作为存储后端，支持LRU淘汰和GPU加速读写；新增Multi-Table Training机制，训练时同时加载训练样本流和全候选池流，合并过item tower批量写入缓存，无需单独的离线全量embedding预计算任务；设计Raw Embedding Streaming，训练侧异步捕获更新的embedding推送到serving节点，15s推送一次，实现20秒级的embedding更新延迟
### 关键结果
在Instagram Reels早期排序阶段线上A/B测试，对比原有SilverTorch缓存架构：预测覆盖率从96%提升到100%，embedding更新延迟从O(5min)降到O(20s)；训推NE gap最高缩小86%，冷启动内容（创建<5min）召回提升超2倍，冷启动互动率提升5-6%；训练发布计算成本降低30%，serving计算成本与基线持平。
> 最值得记住的话：将训练和serving链路联合设计获得的质量、可靠性、效率收益，远高于单独优化任意一条链路能达到的效果
