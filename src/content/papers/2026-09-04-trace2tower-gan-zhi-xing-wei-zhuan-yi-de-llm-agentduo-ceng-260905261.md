---
title: 'Trace2Tower: Transition-Aware EigenTrace Induction of Multi-Level Skills for
  LLM Agents'
title_zh: Trace2Tower：感知行为转移的LLM Agent多层级技能归纳框架
authors:
- Jiazheng Sun
- Boyu Yang
- Binhao Yuan
- Mingxuan Li
- Xin Peng
affiliations:
- Fudan University
arxiv_id: '2609.05261'
url: https://arxiv.org/abs/2609.05261
pdf_url: https://arxiv.org/pdf/2609.05261
published: '2026-09-04'
collected: '2026-09-07'
category: Agent
direction: Agent 经验复用与技能库构建
tags:
- LLM Agent
- Skill Induction
- Trajectory Reuse
- Spectral Decomposition
- Hierarchical Skill
one_liner: 从LLM Agent执行轨迹提炼融合行为转移与成败信号的结构化多层级技能塔
practical_value: '- 电商导购Agent、搜索交互Agent的历史交互轨迹可复用该框架的事件抽象+成败关联转移图方法，提炼可复用的查询、选品、下单标准化流程，减少无效交互步骤

  - 技能分层构建思路可直接迁移到推荐系统的用户行为模式挖掘：把用户点击/加购/下单轨迹抽象为事件序列，聚类出操作层、流程层、策略层不同粒度的行为模式，用于冷启动用户引导或流程优化

  - 对比谱分解的成败信号加权方法可复用：对同时存在成功/失败的行为转移路径，用(A_success²)/(A_success+A_failure)的加权方式抑制高失败率捷径，不需要手动调权重，适合规则难覆盖的复杂交互场景

  - 分层技能的成本-效果权衡策略可借鉴：可根据业务算力预算选择仅用高层策略（低token消耗、高通用性）或叠加中层流程技能（高准确率、中等消耗），平衡推理成本和效果'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
现有LLM Agent的轨迹复用和技能提取方法多依赖浅层语义匹配或扁平技能总结，忽略了行为的时序依赖、转移关系和成败关联，既无法区分有效路径和易失败捷径，也不能支撑局部技能到全局策略的组合，导致经验复用效率低、泛化性差。

### 方法关键点
- 先把原始轨迹分段抽象为标准化事件，替换任务特定实体为类型化参数，消除实例级语言差异，保留执行时序
- 构建融合三类信号的转移感知EigenTrace图：语义兼容性（事件嵌入余弦相似度）、转移依赖（成败轨迹中事件的相邻出现频率）、成败相关性（事件的历史成功率平滑值），几何加权不需要手动调参
- 用无参对比谱分解抑制失败关联模式，通过最大特征间隔自动聚类得到行为模式，分层构建动作模板、执行流程、全局策略三级技能塔
- 部署时可根据token预算选择仅检索高层策略，或叠加中层流程技能，后续通过验证器反馈动态调整技能权重，无需重新训练

### 关键实验
在ALFWorld household操作、WebShop电商导购两个基准测试，对比ExpeL、SkillX、Trace2Skill等基线：ALFWorld上成功率达87.31%，比ExpeL高5.72个百分点，仅需10.35步、0.26次无效操作；WebShop上精确成功率达50.67%，比SkillX高1.34个百分点，无效操作从0.68降到0.27；消融实验显示去掉转移依赖信号成功率下降17.16个百分点，验证了时序关系的核心价值。

### 核心结论
Agent经验复用的核心不是简单存储历史轨迹，而是挖掘与成功绑定的、可组合的结构化行为依赖关系。
