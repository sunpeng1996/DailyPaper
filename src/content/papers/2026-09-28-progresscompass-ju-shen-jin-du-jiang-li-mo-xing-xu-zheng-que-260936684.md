---
title: 'ProgressCompass: Embodied Progress Reward Models Are Lost Without the Right
  Context'
title_zh: ProgressCompass：具身进度奖励模型需正确上下文才能准确评估
authors:
- Jianshu Zhang
- Keliang Wu
- Chengxuan Qian
- Xiyuan Yang
- Ce Zhang
- Ariel Tian
- Anbang Liu
- Haoran Lu
- Han Liu
affiliations:
- Northwestern
- UCSB
- UIUC
- CMU
arxiv_id: '2609.36684'
url: https://arxiv.org/abs/2609.36684
pdf_url: https://arxiv.org/pdf/2609.36684
published: '2026-09-28'
collected: '2026-10-07'
category: Agent
direction: 具身Agent · 进度奖励模型优化
tags:
- Embodied Agent
- Progress Reward Model
- VLM
- Context Management
- Long-Horizon Task
one_liner: 提出ProgressCompass智能体循环，用通用VLM为冻结PRM提供上下文，大幅降低长任务进度估计误差
practical_value: '- 进度评估类任务（如用户转化路径进度、Agent任务执行进度、用户兴趣进化阶段判断）不要直接喂全量历史数据，先提取当前步骤所需的精准上下文，可大幅降低评估误差，在电商推荐的用户生命周期建模中可直接复用该思路

  - 可复用「大模型拆任务提上下文 + 冻结领域专用模型打分」的架构，无需重新训练已上线的领域模型，仅新增通用大模型的上下文提取能力即可快速提升业务效果，适合推荐排序、广告出价等已有模型迭代成本高的场景

  - 多模型协作的Agent系统可复用跨请求并行调度方案，不同组件处理不同请求的对应任务，消除组件空闲时间，能把多模块组合的端到端延迟降低60%以上，适合生产环境部署多模型协作的智能体系统'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前具身Agent执行长任务时，进度奖励模型（PRM）仅依赖当前帧或原始历史输入的进度估计误差极高：三类上下文依赖场景（状态召回、序列跟踪、重复事件消歧）的关键信息无法从当前输入直接获得，而现有PRM基准多聚焦短任务，未覆盖这类依赖历史信息的进度估计场景。
### 方法关键点
- 构建CONTEXTPROGRESS-BENCH基准，覆盖24个需上下文的机器人操作任务、120个episode，人工标注三类上下文依赖场景的对应需求
- 设计ProgressCompass智能体循环：冻结PRM仅负责单步骤进度打分，用通用VLM分别承担Orienter（拆解任务、输出当前步骤所需上下文）、Verifier（验证当前步骤是否完成）角色，纯文本Navigator调度全流程，无权重更新无需额外训练
- 新增expected transition机制，明确每个步骤完成的可视化判定标准，降低验证误差；跨episode并行调度多模型组件，端到端延迟降低65.6%
### 关键实验
在自建基准上对5个SOTA PRM做配对测试：供给正确上下文后，所有模型MAE降低77%-82%，秩一致性接近1；ProgressCompass基于冻结的RoboMeter-4B实现，进度MAE降低63%，秩一致性提升76%，填补了78%的oracle上下文性能gap，在任务提前终止、额外执行步骤、指令不匹配的鲁棒性测试中远超所有基线模型。
### 核心结论
PRM不是进度估计能力不足，而是缺失正确上下文就会迷失，无需重新训练模型，仅补全当前步骤所需的精准上下文就能获得数倍性能提升
