---
title: 'Switch-SWE: Do Coding Agents Hold Focus When Switching Between Unfinished
  Tasks?'
title_zh: Switch-SWE：编码Agent在未完成任务切换场景下的注意力保持评测
authors:
- Shuochen Chang
- Qianli Ma
- Yibo Miao
- Qingyang Liu
- Bingjie Gao
- Haonan Zhao
- Siyu Sun
- Yulin Sun
- Han Zhao
- Jiangtong Li
affiliations:
- Shanghai Jiao Tong University
- Tongji University
arxiv_id: '2611.02017'
url: https://arxiv.org/abs/2611.02017
pdf_url: https://arxiv.org/pdf/2611.02017
published: '2026-10-31'
collected: '2026-11-04'
category: Agent
direction: Agent 任务切换能力评测与优化
tags:
- Coding Agent
- Benchmark
- Context Management
- Task Switching
- Long-horizon Task
one_liner: 提出同仓库任务切换评测基准Switch-SWE及上下文管理模块缓解任务恢复性能损失
practical_value: '- 多任务切换类Agent（如电商多店铺运营Agent、推荐系统多目标调优Agent）可复用RCM的设计，拆分「任务历史路由+任务状态记忆」两个模块，大幅降低跨任务上下文干扰

  - 做多Agent/单Agent多任务场景评测时，可借鉴Switch-SWE的配对实验设计：相同任务在连续执行和插入干扰任务两种场景下对比，精准量化任务切换的性能损失

  - 电商/推荐业务的用户会话中断恢复场景（如用户浏览中途退出再返回、跨端续看推荐），可参考任务locality分析逻辑，优先召回关联度高的历史上下文，降低续看场景的推荐偏差'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有编码Agent评测基准大多针对单任务端到端执行，未覆盖真实开发中频繁切换同仓库多个未完成任务的场景，无法衡量Agent从干扰中恢复原任务的能力，而这是Agent落地复杂长会话场景的核心痛点。
### 方法关键点
- 配对评测设计：每个目标任务分别在无中断连续执行、插入4个同仓库未完成干扰任务两种场景下评测，两种场景的目标任务需求、可执行验证器完全一致，仅统计目标任务最终完成率，排除代码冲突等无关变量
- Switch-SWE基准构造：从19个Python仓库的Issue、PR、评审历史中构建200个多阶段目标任务，生成400组配对会话，按干扰任务与目标任务的代码目录关联度分为近邻/远邻两组，可量化关联度对任务恢复的影响
- 可插拔恢复上下文管理器（RCM）：包含任务历史路由器（筛选当前任务相关会话历史）、任务状态记忆（增量记录当前任务的目标、进度、待办）两个模块，不修改Agent原生执行逻辑即可集成
### 关键结果
- 7款主流编码Agent在任务切换场景下平均完成率下降11.5个百分点，远邻干扰的性能损失（14.9pp）是近邻干扰（8.1pp）的近2倍，同时任务切换会使会话Token消耗提升4.5~11.1倍
- 集成RCM后，DeepSeek-V4.1-Flash的任务切换完成率提升15.5pp，GLM-5.3提升5.5pp，几乎抹平任务切换带来的性能损失
### 核心结论
单靠持久化任务工作区不足以解决多任务切换的性能下降，任务级的上下文过滤+状态显式记忆是更有效的优化路径
