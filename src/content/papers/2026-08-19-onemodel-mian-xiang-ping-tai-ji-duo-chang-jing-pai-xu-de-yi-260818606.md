---
title: 'OneModel: A Unified Foundation for Platform-Scale Multi-Scenario Ranking'
title_zh: OneModel：面向平台级多场景排序的统一框架
authors:
- Yinqi Zhang
- Peiyu Hu
- Yuntian Tang
- Siying Gu
- Jiahao Liang
- Longxin Kou
- Haiqing Hu
- Shuman Zhuang
- Yubin Xu
- Chenggen Sun
affiliations:
- Xiaohongshu
arxiv_id: '2608.18606'
url: https://arxiv.org/abs/2608.18606
pdf_url: https://arxiv.org/pdf/2608.18606
published: '2026-08-19'
collected: '2026-08-20'
category: RecSys
direction: 多场景统一排序 工业级落地实践
tags:
- Multi-scenario Ranking
- Long-context User Modeling
- Industrial RecSys
- Multi-objective Training
- Serving Optimization
one_liner: 面向平台多业务流排序提出统一框架，兼顾跨流迁移与场景定制，全业务线获显著线上收益
practical_value: '- 多场景统一建模思路可直接复用：主场景（自然流）的大量用户行为信号可迁移到低流量的广告、商服场景，几乎无负迁移，还能减少多套排序模型的运维成本

  - 场景适配轻量trick落地成本低：SAIM门控仅在Transformer FFN层插入场景相关的通道调制，梯度隔离在训练早期冻结backbone梯度先训场景头，两个改动小、收益明确，可直接复用到现有多场景排序模型

  - 长序列推理优化方案可直接落地：用户状态增量预计算缓存、用户塔计算共享、特征分解等工程优化，可在模型参数上涨30%的前提下将推理延迟降低60%+，解决大排序模型上线的延迟瓶颈

  - 多目标训练调参经验可复用：跨流batch采样避免高流量场景主导训练，loss权重按单任务验证AUC反比分配，训练过程动态调整自监督与监督任务的loss权重，这些调参策略可直接用到多任务多场景训练中'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
平台级推荐系统通常覆盖自然流、广告、商服等多业务线，传统分场景独立维护排序模型的方案既割裂用户连续行为轨迹造成信号浪费，也大幅提升训练、迭代、运维的工程成本；而多场景统一建模又面临异构特征适配、目标冲突负迁移、长序列推理延迟高等落地难题，亟需兼顾效果、效率的工业级可落地方案。
### 方法关键点
- 异构特征统一：各场景原始特征先经场景专属线性投影映射到共享空间，再叠加场景、动作类型、时间间隔、位置的结构上下文embedding，生成统一可比对的事件token
- 序列建模优化：基于动作导向的GenRank式因果Transformer降低有效序列长度；插入SAIM场景感知门控到FFN层，实现共享参数下的场景专属特征通道调制；结合全局注意力池化与末次序列状态输出分层用户表征
- 训练策略：混合自监督下一跳预测、多场景监督任务的统一loss，动态调整各loss权重；采用跨流batch采样、训练早期梯度隔离、选择性反向传播提升训练稳定性与效率
- 推理优化：用户长序列表征预计算并增量缓存，与请求时候选打分解耦；搭配特征分解、用户特征预取、用户塔共享计算、图级推理优化降低延迟
### 关键结果
在小红书10%流量切片上对比单场景HSTU、GenRank等基线，统一训练后广告、商服的点击AUC均提升3‰，自然流无明显负迁移；线上A/B测试实现自然流停留时长+0.33%、互动+1.25%，广告价值+3.43%、CTR+8.18%，商服DGMV+1.19%、GPM+2.16%；模型参数提升32.9%的情况下，推理latency从270ms降至90ms，下降66.7%。
> 最值得记住：多业务流统一排序可同时实现跨场景信号复用提效、工程资源集约降本，是平台级推荐的可行演进方向。
