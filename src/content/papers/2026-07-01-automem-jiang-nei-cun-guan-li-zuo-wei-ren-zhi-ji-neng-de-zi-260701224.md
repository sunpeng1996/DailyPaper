---
title: 'AutoMem: Automated Learning of Memory as a Cognitive Skill'
title_zh: 《AutoMem：将内存管理作为认知技能的自动化学习框架》
authors:
- Shengguang Wu
- Hao Zhu
- Yuhui Zhang
- Xiaohan Wang
- Serena Yeung-Levy
affiliations:
- Stanford University
arxiv_id: '2607.01224'
url: https://arxiv.org/abs/2607.01224
pdf_url: https://arxiv.org/pdf/2607.01224
published: '2026-07-01'
collected: '2026-07-02'
category: Agent
direction: Agent 内存管理自动化优化
tags:
- Agent
- Memory Management
- LoRA
- LLM
- Long-horizon Task
one_liner: 通过双自动化优化框架让LLM Agent自主掌握内存管理技能，长序列任务性能提升2~4倍
practical_value: '- 做电商长会话导购Agent、用户长周期行为建模时，可将文件读写操作加入Agent动作空间，让模型自主决策用户偏好、商品信息的存储/检索规则，替代人工硬编码的召回逻辑

  - 双循环优化范式可直接复用：外层用强LLM review全业务链路日志，自动迭代prompt、内存schema等脚手架；内层用LoRA微调专属内存子模型，完全冻结主任务模型，避免迭代影响原有推荐/广告效果

  - 资源受限场景下优先优化内存管理策略ROI远高于堆参数量，32B模型经内存优化即可追平72B甚至闭源前沿模型效果，适合低延迟推荐、端侧Agent部署'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有LLM Agent的外部内存多为人工设计的固定架构，长horizon任务中内存决策的影响滞后，错误往往经过上千步才会暴露，全轨迹人工review成本极高，内存管理作为类人元认知技能缺乏端到端自动化优化方案，盲目堆参数量的ROI极低。
### 方法关键点
- 将文件系统操作（read/write/search/append/create）提升为与任务动作平级的一等动作，所有内存决策可追踪，模型完全自主控制存储、检索、结构组织规则
- 双自动化优化循环：外层循环用Meta-LLM review完整episode轨迹，诊断内存使用缺陷，自动迭代内存脚手架（prompt、文件schema、动作词汇），迭代通过效果gating才保留
- 内层循环用Meta-LLM从海量轨迹中筛选优质内存决策作为训练数据，仅用LoRA微调专属内存专家模型，主任务模型完全冻结，避免破坏原有任务能力
### 关键结果
在Crafter、MiniHack、NetHack三个长序列游戏基准上测试，base模型为Qwen2.5-32B-Instruct，对比滑动窗口、CoT等基线，以及同系列72B模型、Claude Opus 4.5等前沿模型：仅优化内存就带来2~4倍性能提升，优化后的32B模型性能超过Qwen2.5-72B，追平Claude Opus 4.5、Gemini 3.1 Pro Thinking等闭源前沿模型，内存训练额外带来9%~18%相对提升，无效动作率下降32%~65%，冗余写操作下降68%~83%。
> 最值得记住：长序列任务中，内存管理是可独立训练的高杠杆优化目标，ROI远高于盲目提升模型参数量。
