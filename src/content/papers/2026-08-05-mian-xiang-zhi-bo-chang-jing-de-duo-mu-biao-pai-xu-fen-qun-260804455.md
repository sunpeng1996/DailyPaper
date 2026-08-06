---
title: 'Multi-Objective Ranking for Live-Streaming: Balancing Fresh and Delayed Signals
  with Segment-Aware Targeting'
title_zh: 面向直播场景的多目标排序：分群感知策略平衡实时与延迟信号
authors:
- Xiaoyi Gu
- Julia Tavares
- Eder Santana
- Carlos Mendoza-Cardenas
- Nikita Mishra
- Saad Ali
affiliations:
- Twitch Interactive
- Amazon Prime Video
arxiv_id: '2608.04455'
url: https://arxiv.org/abs/2608.04455
pdf_url: https://arxiv.org/pdf/2608.04455
published: '2026-08-05'
collected: '2026-08-06'
category: RecSys
direction: 多目标推荐 · 直播场景信号平衡与用户分群
tags:
- Multi-Objective Optimization
- Ranking
- MMoE
- Delayed Feedback
- Live-Streaming Recommendation
one_liner: 针对直播延迟反馈、用户分群偏差问题提出FSM-MMoE-VST多目标排序架构 兼顾多业务指标与效率
practical_value: '- 信号拆分思路：对稀疏高价值目标（如关注、付费）设长周期延迟窗口采集标签，密集即时目标（短时长观看/点击）单独建模，避免梯度压制，可直接迁移到电商加购、复购等延迟目标建模场景

  - 用户分群调优技巧：无需训练分群专用模型，仅在推理阶段对不同生命周期用户（新客/老客/低活）给各目标预测值分配差异化权重，低成本解决训练数据中高活用户占比过高的偏差问题，适合电商新客扶持、低活用户促活场景

  - 多任务结构选型：把即时密集的浅层目标单独建模，深层目标（长观看、互动、付费）用MMoE联合建模，比全目标统一多任务模型效果更好，还可降低41.9%参数，降低训练和推理成本，适合多目标排序场景快速落地

  - 延迟窗口选型经验：平衡标签密度、信号新鲜度、计算成本，直播场景最优为14天，电商场景可参考按转化周期（7/14/30天）做AB测试选最优窗口'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
直播场景推荐存在三大核心痛点：一是高价值行为（关注、付费）稀疏，发生率仅为点击的1/90，建模难度大；二是反馈延迟，用户可能在曝光后数天甚至数周才产生高价值行为，过早标负引入噪声，等待过久则数据过时；三是用户分群偏差，高活用户贡献80%以上训练样本，模型天然向高活用户倾斜，忽略新客/低活用户的长期增长价值，现有通用多目标方案未针对性解决这些问题。

### 方法关键点
- 延迟窗口框架：对关注、聊天、付费等稀疏高价值目标设14天延迟采集窗口，将正样本密度提升12倍，同时解决样本稀疏和延迟反馈问题
- 多模型架构拆分：即时密集目标（短时长观看SMP）单独训练Fresh Signal Model（FSM），长观看、关注、付费等深层/延迟目标用MMoE联合建模，避免密集信号梯度压制稀疏信号
- 分群感知（VST）模块：将用户分为新客/低活、高活两类，推理阶段给不同分群的目标预测值分配差异化权重，新客侧侧重即时观看，高活侧侧重互动与付费，无额外训练成本即可解决分群偏差
- 结构参数优化：独立FSM加4专家MMoE的架构，相比多独立延迟信号模型参数减少41.9%，降低训练与推理成本

### 关键实验结果
在Twitch千万级用户的生产环境做分阶段A/B测试，基线为单目标短观看排序模型：
1. 多模型+延迟窗口：整体DAV（日活观众）+0.09%，高活用户ARPU+0.56%
2. 叠加VST模块：新客/低活用户DAV额外+0.15%
3. 叠加MMoE优化：整体DAV额外+0.08%，新增关注+0.27%，p99排序 latency 保持110ms以下，该架构还在移动feed场景验证获得+1.12%正向交互（点击/关注/点赞）提升

### 核心结论
当多目标的信号密度、延迟属性差异较大时，信号层面的架构拆分收益远大于多任务 backbone 的选型优化
