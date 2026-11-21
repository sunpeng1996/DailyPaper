---
title: 'CodeReel: Accelerating Code-to-Video Agents with Exact Frame Reuse and Blocking-Aware
  Scheduling'
title_zh: CodeReel：基于帧复用与阻塞感知调度的代码生成视频Agent加速框架
authors:
- Junyi Shen
- Yao Lu
affiliations:
- National University of Singapore
arxiv_id: '2611.22967'
url: https://arxiv.org/abs/2611.22967
pdf_url: https://arxiv.org/pdf/2611.22967
published: '2026-11-17'
collected: '2026-11-21'
category: Agent
direction: Agent执行层效率优化
tags:
- CodeAgent
- ExecutionOptimization
- FrameReuse
- Scheduling
- AgentEfficiency
one_liner: 提出无训练执行层CodeReel，通过帧复用和调度优化大幅降低代码生成视频Agent等待耗时
practical_value: '- 循环迭代类Agent（如电商内容生成、推荐策略调优Agent）可复用「按执行指令生成唯一键缓存中间结果」的思路，避免重复计算

  - 阻塞型任务调度可参考先跑校验任务、后台低优先级启动主任务的策略，在不多耗算力的前提下降低等待时延

  - 迭代类任务的失败分支中间结果可缓存复用给后续成功分支，无需完全丢弃失败任务产出，提升资源利用率'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
代码生成视频Agent工作在build-inspect-edit循环中，中位耗时11分钟、成本2.85美元，超1/3时间浪费在阻塞Agent的构建环节；其中37.5%的后续视频帧已被渲染过，50%的构建会在校验环节终止但无法提前预判。
### 方法关键点
1. 无训练执行层CodeReel，完全兼容现有Agent指令；2. 精确帧复用：按帧的绘制指令生成唯一键，无论时序位置直接复用匹配的已渲染帧；3. 阻塞感知调度：优先跑校验任务，同时以低优先级启动渲染，若近期构建通过率低则延后渲染。
### 关键结果
EditLoop基准上，相比并行渲染的Rebuild pipeline等待时间降36.3%，相比串行pipeline降57.9%；实Agent场景下，Claude Code中位构建耗时为Rebuild的0.62倍，Codex CLI为0.67倍，增益跨5个模型、2个框架生效。
