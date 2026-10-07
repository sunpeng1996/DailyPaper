---
title: Capability-Driven Self-Evolution of Agent Memory
title_zh: 基于能力维度引导的Agent记忆自进化框架PRISMEM
authors:
- Yaoqi Chen
- Yuru Feng
- Qianxi Zhang
- Baotong Lu
- Jianan Lu
- Zhirui Wang
- Shusen Xu
- Zewen Jin
- Zengzhong Li
- Cheng Li
affiliations:
- University of Science and Technology of China
- Microsoft
- University of California, San Diego
arxiv_id: '2610.06361'
url: https://arxiv.org/abs/2610.06361
pdf_url: https://arxiv.org/pdf/2610.06361
published: '2026-10-04'
collected: '2026-10-07'
category: Agent
direction: Agent 记忆系统自进化架构优化
tags:
- AgentMemory
- SelfEvolution
- LongContext
- MemoryOptimization
- LLMAgent
one_liner: 提出PRISMEM框架沿记忆能力维度迭代优化再整合，显著提升长上下文Agent记忆效果
practical_value: '- 做用户长期兴趣建模、电商个性化对话Agent时，可将记忆能力拆分为事实召回、时序追踪、偏好提取等独立维度分别迭代，避免全局优化时的能力跷跷板问题，不会因单版本整体得分不高就废弃某维度的有效优化

  - 迭代优先级评估可复用依赖感知的能力调度逻辑，优先优化对其他能力溢出收益最高的瓶颈模块，比如电商场景下时序追踪能力差会同时影响偏好更新和跨会话行为合成，优先迭代该模块ROI更高

  - 多版本策略整合时可采用配对差分案例法，筛选两个版本效果差距最大的样本对比行为差异，精准合并增益，无需全量AB即可快速定位可复用的优化点，降低迭代成本

  - 可复用细粒度记忆模块拆分（提取/索引/规划/召回/回答）的设计，在迭代时能精准定位问题模块，无需每次修改全链路，降低调试成本'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有Agent记忆自进化方法基于整体任务性能做全局优化，混合反馈会导致优化方向模糊，单能力增益可能被其他能力的下降抵消。统计显示80.5%的未带来整体收益的迭代版本实际上至少提升了一项记忆能力，大量有效优化方向被浪费，在性能平台期该问题尤为突出。
### 方法关键点
- 将记忆能力拆分为事实召回、时序追踪、偏好提取、跨会话合成、对抗鲁棒性5个独立维度，每个维度单独跟踪最优专家版本，避免全局得分掩盖单能力增益
- 依赖感知的能力选择机制：计算每个能力的直接缺陷和对其他能力的溢出瓶颈效应，优先迭代优先级最高的能力，避免资源浪费在已plateau的方向
- 历史引导的诊断逻辑：筛选有历史优化参照的退化案例、降低重复案例权重，每次选5个最有信息量的失败样本优化，提升诊断效率
- 轨迹引导的整合：用配对差分案例对比全局最优版本和各维度专家版本的行为差异，将各维度增益合并到统一记忆程序中，同时规避能力退化
- 效率优化：压缩诊断上下文减少token消耗，仅重新执行修改后的记忆模块，单诊断案例token消耗平均降低44%
### 关键实验
在BEAM-1M和LongMemEval-M两个百万token级长上下文记忆基准上测试，对比Mem0、A-MEM、M⋆、EvolveMem等7个主流基线，PRISMEM比最优基线分别高10.54、7.83个百分点，进化总token消耗比M⋆降低4%-30%。
### 核心结论
将整体优化的一维搜索空间拆分为多能力维度的并行搜索，再定向合并增益，是突破自进化系统性能天花板的有效路径
