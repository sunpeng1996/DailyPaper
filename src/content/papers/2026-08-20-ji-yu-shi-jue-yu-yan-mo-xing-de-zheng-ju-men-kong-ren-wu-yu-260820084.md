---
title: Evidence-Gated Task and Motion Planning with Vision-Language Models
title_zh: 基于视觉语言模型的证据门控任务与运动规划框架
authors:
- Tsunehiko Tanaka
- Matthew Stephenson
- Alistair Macvicar
- Edgar Simo-Serra
affiliations:
- Waseda University
- Flinders University
arxiv_id: '2608.20084'
url: https://arxiv.org/abs/2608.20084
pdf_url: https://arxiv.org/pdf/2608.20084
published: '2026-08-20'
collected: '2026-08-21'
category: Agent
direction: 具身Agent · VLM任务规划优化
tags:
- VLM
- TAMP
- Embodied Agent
- Partial Observability
- Task Planning
one_liner: 提出EAFG框架，规划前主动采集视觉证据，提升部分可观测下VLM+TAMP的任务完成率与异常处理能力
practical_value: '- 导购/线下服务Agent可复用「先探索收集环境证据再执行任务」的流程，避免基于先验假设直接执行导致的用户体验问题，比如找货类Agent先确认商品存在再引导用户

  - 可借鉴可行性门控设计，在Agent执行复杂任务前增加校验环节，判定任务不可行时直接终止，减少无效算力消耗与错误尝试，比如电商售后Agent确认无法满足用户诉求时直接转人工

  - 多模态Agent的状态更新可参考「迭代更新证据状态而非盲目追加历史」的设计，避免冗余上下文干扰大模型推理，降低Prompt长度与推理成本'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
部分可观测场景下，VLM+TAMP的机器人规划方案会依赖先验知识生成无观测支撑的子目标，导致执行失败、无效重试等问题，现有方案默认环境完全可观测，缺乏主动验证未观测对象的机制，长周期任务成功率低。

### 方法关键点
- 证据采集模块：由VLM生成可逆探索子目标（如开柜、移开遮挡物），通过TAMP生成可执行动作序列，执行后更新观测与证据状态，禁止直接执行主任务相关操作
- 可行性门控机制：每轮探索后VLM基于历史证据、观测 collage 输出三种状态：可规划/需更多证据/终止，仅当确认必要条件满足时才进入任务规划阶段，缺失必要对象时直接终止
- 任务规划阶段直接引入采集到的证据状态作为Prompt上下文，保证子目标生成完全基于已验证的观测结果

### 关键实验
在厨房做汤场景下对比基线VLM-TAMP：1）目标明确且对象存在场景，EAFG将GPT-5.5的食谱完成率从20%提升到45%；2）目标不明确场景，GPT-5.5食谱完成率从5%提升到40%，Gemini-3.5-Flash从0提升到20%；3）存在缺失对象场景，EAFG将GPT-5.5的终止准确率从45%提升到90%，缺失对象重试次数从4次降到0.55次，Gemini-3.5-Flash终止准确率达100%，重试次数降为0。

### 核心结论
大模型驱动的Agent执行长周期任务时，先做探索验证再做任务规划，比直接基于先验生成计划的综合效率高得多
