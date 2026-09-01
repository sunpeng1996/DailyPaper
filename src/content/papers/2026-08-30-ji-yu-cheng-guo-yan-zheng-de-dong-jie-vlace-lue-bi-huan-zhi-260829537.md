---
title: 'AGM: Achievement-Grounded Memory for Closed-Loop Agents with Frozen VLA Policies'
title_zh: 基于成果验证的冻结VLA策略闭环智能体记忆框架AGM
authors:
- Hongbo Gao
- Zeyu Ni
- Xin Wen
- Siyu Xu
- Ruifeng Li
affiliations:
- Harbin Institute of Technology
- The University of Sydney
- StellarEdge AI
arxiv_id: '2608.29537'
url: https://arxiv.org/abs/2608.29537
pdf_url: https://arxiv.org/pdf/2608.29537
published: '2026-08-30'
collected: '2026-09-01'
category: Agent
direction: 具身Agent 记忆更新机制优化
tags:
- Agent
- VLA
- Memory Mechanism
- Closed-Loop Control
- Frozen Model
one_liner: 用事件触发的成果校验记忆更新机制，解决冻结VLA智能体的开环执行误差累积问题
practical_value: '- 设计任务型Agent（如电商导购、履约流程Agent）的记忆系统时，不要将动作尝试直接作为完成进度写入，必须加事件触发的结果校验逻辑，避免临时执行错误转化为永久任务状态偏差

  - 采用冻结基座+轻量校验头的架构改造现有大模型驱动的业务系统，仅需训练百万级参数的小头部即可完成特定场景的执行结果校验，大幅降低微调与部署成本

  - 针对可恢复/不可恢复业务操作设置差异化校验阈值：可恢复操作（如加购、收藏）用严格阈值避免无效操作，不可恢复操作（如下单、支付）用宽松阈值降低误拦截率，平衡正确性与用户体验'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
冻结VLA（视觉-语言-动作）策略泛化能力强但执行是开环的，不跟踪任务进度，传统记忆增强方案直接把动作尝试当做完成进度写入，会把临时执行错误变成持久的任务状态误差，甚至比不用记忆效果还差，尤其在重复操作类任务中感知混淆问题突出，错误会随任务长度持续累积。

### 方法关键点
- 把任务拆解成带类型标签的子目标序列，用进度指针作为唯一的动态任务状态，不存储全量交互历史，内存开销极低
- 基于proprioceptive gripper状态机触发校验，只有和当前子目标类型匹配的交互事件才启动验证，避免无效计算
- 抓取成功用冻结CoTracker3点跟踪器做零训练的运动一致性校验，放置成功用冻结SigLIP编码器做语言条件的跨视角前后对比，仅训练2.43M参数的验证头
- 校验通过指针前进，抓取失败指针保留，可恢复的放置失败指针回滚，针对可恢复/不可恢复放置设置差异化的接受阈值

### 关键实验
在RoboMME Counting基准上，对比最强记忆增强基线MemER，AGM平均成功率高7.1个百分点，PickXTimes任务达100%，BinFill任务达84%，仅新增231M冻结参数，训练参数仅2.43M；真实机器人部署下同样保持显著优势，高重复次数任务下成功率远高于无记忆的冻结VLA策略。

### 核心结论
对于长周期任务的智能体，决定性的问题不是它有多少记忆容量，而是有什么证据支撑它写入记忆。
