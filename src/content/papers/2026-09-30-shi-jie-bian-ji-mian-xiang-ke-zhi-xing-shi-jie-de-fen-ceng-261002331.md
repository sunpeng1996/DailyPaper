---
title: 'World Editing: Intervening on Executable Worlds at Increasing Depth'
title_zh: 世界编辑：面向可执行世界的分层深度干预方法与基准
authors:
- Max Ku
- Nok-Kan Law
- Yu-Chien Tang
- Shih-Ying Yeh
- Ping Nie
- Andy Zheng
- Tat Hei Lai
- Fei-Yueh Chen
- Nikko Yu
- Wei-Chieh Sun
affiliations:
- University of Waterloo
- G-G-G
- Comfy Org Research
- University of Illinois Urbana-Champaign
arxiv_id: '2610.02331'
url: https://arxiv.org/abs/2610.02331
pdf_url: https://arxiv.org/pdf/2610.02331
published: '2026-09-30'
collected: '2026-10-07'
category: Agent
direction: Agent 可执行世界编辑能力评估
tags:
- Agent
- World Editing
- Code Agent
- Benchmark
- Game Modding
one_liner: 提出世界编辑分层干预框架与IGMBench基准，量化前沿编码代理的可执行世界修改能力
practical_value: '- 分层干预粒度可复用：业务系统迭代（如推荐规则修改、活动配置更新）可按L1属性/L2实体/L3规则/L4系统的分层逻辑划分修改难度，预估上线风险，分配研发资源

  - 三阶段评估框架可直接迁移到业务Agent验收：先验证可执行性（配置/代码是否正常加载）、再验证功能正确性（规则是否生效）、最后验证体验一致性（是否符合现有业务风格）

  - 失败根因可指导业务Agent优化：当前编码Agent大部分失败是行为不符合预期而非编译错误，做业务代码/配置生成Agent时要重点强化行为校验逻辑，而非仅做语法检查'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前AI与可执行交互世界的研究集中于世界生成、智能体在世界中执行任务两大方向，对已有世界的定向编辑能力（修改指定属性同时保留无关特征）研究缺失，缺乏统一的能力分级框架与可复现的评估基准，无法量化不同智能体的编辑能力差异。
### 方法关键点
- 提出4层干预深度分级体系：L1属性干预（修改现有组件参数/外观）、L2实体干预（新增符合现有规则的内容）、L3规则干预（修改实体交互逻辑）、L4系统干预（修改多耦合子系统）
- 搭建IGMWorld执行环境：支持编辑→构建→运行→观测的全流程迭代，兼容Minecraft、Terraria的原生modding工具链
- 构建IGMBench评估基准：覆盖两款游戏共110个编辑任务、1.1K+可执行评估指标，配套三阶段评估逻辑：可执行性校验→编辑正确性校验→视觉一致性校验
### 关键结果
测试7款前沿编码智能体，核心结论：
1. 最强配置GPT-5.6 Sol的任务级成功率（WSR）达78.2%，单指标通过率（CPR）达94.8%
2. 编辑成功率随干预深度上升显著下降，该规律与任务的评估指标数量无关，耦合度越高的修改难度越大
3. 90%以上的失败任务可正常编译加载，核心瓶颈是行为不符合预期；视觉一致性是独立短板，所有Agent的联合风格+语义通过率均低于50%
### 核心结论
世界编辑是独立于世界生成、世界交互的第三类Agent核心能力，其可靠性由干预的耦合深度而非代码量决定
