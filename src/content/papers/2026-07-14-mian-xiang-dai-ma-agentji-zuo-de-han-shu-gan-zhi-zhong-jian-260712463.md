---
title: Function-Aware Fill-in-the-Middle as Mid-Training for Coding Agent Foundation
  Models
title_zh: 面向代码Agent基座的函数感知中间补全中期训练方法
authors:
- Yubo Wang
- Jiarong Liang
- Yuxuan Zhang
- Xuye Liu
- Cong Wei
- Yuyu Zhang
- Ping Nie
- Wenhu Chen
arxiv_id: '2607.12463'
url: https://arxiv.org/abs/2607.12463
pdf_url: https://arxiv.org/pdf/2607.12463
published: '2026-07-14'
collected: '2026-07-15'
category: Agent
direction: 代码Agent 基座训练优化
tags:
- Coding Agent
- Fill-in-the-Middle
- Mid-Training
- Self-Supervised Learning
- Foundation Model
one_liner: 利用代码函数调用与Agent推理环的同构性设计自监督中期训练目标，提升代码Agent性能并缓解能力侵蚀
practical_value: '- 可借鉴FIM中期训练思路，针对电商/搜索Agent的工具调用场景，用业务日志中天然的请求-调用-返回链路构造自监督训练目标，无需额外标注

  - 可复用「结构同构+复杂度筛选」的掩码构造逻辑，针对推荐Agent的API调用、召回结果拼接等环节，仅筛选符合依赖逻辑、难度适中的样本做掩码训练，提升训练效率

  - 中期训练+下游对齐的两阶段范式可直接迁移，能有效缓解Agent对齐过程中基座通用能力掉点的问题，适配多场景Agent快速迭代'
score: 9
source: arxiv-cs.CL
depth: abstract
---

### 动机
标准左到右代码预训练仅覆盖前向推理逻辑，无法适配代码Agent整合外部工具返回、完成行动-观察-推理闭环的需求，常规Agent对齐流程还易导致基座通用能力侵蚀。

### 方法关键点
发现代码Agent的行动-观察-延续环路与函数调用结构完全同构，提出函数感知FIM中期训练自监督目标：基于程序依赖图分析、复杂度-可推断性双重标准筛选待掩码的函数，在2.6B token去重GitHub代码语料上完成中期训练后，再接入现有Agent后训练管线。

### 关键结果
- 7B/14B Qwen2.5-Coder-Instruct的SWE-Bench-Verified分别提升2.8/3.0，Qwen3-8B提升3.2；SWE-Bench-Lite分别提升3.7/4.0/5.4
- 跨2种后训练管线、不同基座均生效，同时缓解Agent对齐带来的非Agent代码能力、非代码工具使用能力掉点，仅用Python语料训练也可获得跨任务增益
