---
title: 'Twin: Playing an Unknown Game with a Test-Time Digital Twin'
title_zh: Twin：面向未知交互任务的测试时可执行数字孪生Agent系统
authors:
- Alexy Skoutnev
- Kirill Acharya
- Gaston Longhitano
- Madeleine Udell
- Kevin Ellis
- Iddo Drori
affiliations:
- Stanford University
- Cornell University
- University of Southern California
- Yeshiva University
arxiv_id: '2608.14490'
url: https://arxiv.org/abs/2608.14490
pdf_url: https://arxiv.org/pdf/2608.14490
published: '2026-08-14'
collected: '2026-08-17'
category: Agent
direction: Agent · 测试时世界模型构建
tags:
- World Model
- Code Agent
- Test-Time Adaptation
- ARC-AGI
- Goal Inference
one_liner: 通过测试时生成代码形式的可验证世界模型，在ARC-AGI-3基准上达到接近人类的行动效率
practical_value: '- 可复用「全量历史重放校验」硬约束机制：在电商直播话术优化、广告投放策略迭代场景，决策前强制策略仿真匹配所有历史行为数据，大幅减少真实流量试错成本

  - 可借鉴「预奖励目标假设」设计：在推荐/广告冷启动场景，无需等待真实转化反馈，先基于交互特征生成候选目标假设，小流量验证后再放量，缩短冷启动周期

  - 可落地「反例驱动自动修复」流程：当推荐/搜索策略的线上表现与离线仿真不一致时，自动将错例作为迭代信号修复模型，降低人工排查与迭代成本'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
现有Agent处理规则与目标均未知的交互任务时，要么依赖手工定制世界模型泛化性差，要么盲目试错行动效率极低，在黑盒交互场景下表现远逊于人类，亟需低试错成本、可自动构建环境认知的Agent架构。
### 方法关键点
- 调用代码Agent生成Python形式的可执行数字孪生，包含环境转移函数`step`和目标判断函数`goal_reached`两个核心模块
- 强制硬约束：所有对外交互的动作提交前，必须通过全量历史交互日志的重放校验，只要存在1条转移预测不匹配就触发模型修复
- 分两类阻塞场景处理：动态墙（模型不匹配历史）优先修复转移规则，目标墙（模型匹配历史但无可行路径）基于状态变化特征生成候选目标假设，校验通过后作为临时目标规划路径
- 执行阶段每一步都对比模型预测与真实交互结果，不匹配立即终止当前计划，将错例加入日志触发模型迭代
### 关键结果
基于ARC-AGI-3基准的25个公开游戏共183个关卡测试，对比直接调用基座模型、普通Codex harness、OPINE-World等竞品：
- Twin得分93.3/100，通关23/25个游戏、179/183个关卡，88.3%的通关关卡行动次数少于首次接触游戏的人类
- 87.2%的关卡在获得首次奖励前就推断出了正确目标，基座模型直接调用得分仅7.8%，普通Codex harness得分61.1%
> 值得记住：构建可验证的世界模型远比想象中简单，真正的难点在于推断出正确的目标
