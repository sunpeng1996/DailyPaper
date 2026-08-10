---
title: 'TEPA: Revoking Stale Memories for Conflict-Robust Language Agents'
title_zh: 《TEPA：支持过期记忆撤销的高鲁棒性语言Agent记忆机制》
authors:
- Yan Zhou
- Yue Ouyang
- Kaiyang Zheng
- Suncheng Xiang
affiliations:
- 长沙理工大学数学与统计学院
- 上海交通大学生物医学工程学院
arxiv_id: '2608.07429'
url: https://arxiv.org/abs/2608.07429
pdf_url: https://arxiv.org/pdf/2608.07429
published: '2026-08-07'
collected: '2026-08-10'
category: Agent
direction: Agent 记忆有效性管理与过期撤销
tags:
- AgentMemory
- MemoryPollution
- StaleMemory
- LifecycleManagement
- RAG
one_liner: 为语言Agent记忆引入显式有效性状态，通过冲突键匹配撤销过期记忆解决记忆污染
practical_value: '- 电商用户偏好记忆系统可借鉴冲突键设计：将用户品类偏好、价格敏感度、收货地址等作为固定冲突键，新交互反馈覆盖时自动撤销旧偏好记忆，避免推荐过时、不符合当前需求的商品

  - Agent工具调用记忆可复用生命周期状态管理：对工具返回结果按「任务类型+入参维度」做冲突键，新返回结果冲突时自动标记旧结果为过期，避免调用失效的工具模式

  - RAG系统的实体类知识更新可借鉴有效性标记逻辑：对商品价格、库存、活动规则等易变属性做冲突键匹配，过期知识仅归档不参与召回，同时保留全量历史支持审计回溯'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
当前语言Agent依赖长期记忆复用过往事实、偏好、任务经验，但记忆持久化会导致已被新证据覆盖的过期冲突信息仍可被召回，污染Prompt，极端情况下带记忆的Agent表现甚至不如无记忆基线，现有记忆系统缺乏显式的有效性状态管理与过期撤销机制。

### 方法关键点
- 将观测转换为带冲突键的记忆先例，每个先例分配Hypothesis/Active/Revoked三种生命周期状态，仅Active状态记忆可被召回，Revoked状态记忆保留归档用于审计
- 新证据进入时匹配相同冲突键的活跃记忆，若冲突则更新旧记忆的支持/冲突计数，通过Beta-Bernoulli模型估算有效性后验，低于阈值时标记为Revoked移出活跃集
- 进阶版TEPA-Full新增候选记忆试跑验证，通过3个小流量测试（支持/反事实/无影响校验）确认后再激活记忆，降低错误记忆上线风险

### 关键实验结果
在控制变量漂移、真实文件执行漂移、用户偏好更新流、MemoryAgentBench SH-6k四个场景测试，对比无记忆、Append-only、Last-write-wins（LWW）等基线：全反转阶段控制漂移场景Append-only和LWW成功率仅0.210，低于无记忆的0.309，TEPA达0.950；偏好更新场景Append-only成功率0.138，TEPA-Full达0.872；MemoryAgentBench SH-6k单跳事实更新任务上TEPA与强基线LWW持平，均为0.890。

### 核心结论
记忆的相关性和新鲜度不能替代有效性，长期记忆必须显式跟踪有效性状态，冲突键粒度的过期撤销是解决单跳事实类记忆污染的核心手段
