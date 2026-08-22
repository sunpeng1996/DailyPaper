---
title: 'SWE-bench Science: Can Coding Agents Resolve Engineering Tasks in Science?'
title_zh: SWE-bench Science：面向科学领域编码Agent的任务评测基准
authors:
- Zhipeng Xu
- Jiahao Lu
- Yining Zheng
- Yuxin Wang
- Xipeng Qiu
affiliations:
- Shanghai Innovation Institute
- Fudan University
arxiv_id: '2608.19799'
url: https://arxiv.org/abs/2608.19799
pdf_url: https://arxiv.org/pdf/2608.19799
published: '2026-08-19'
collected: '2026-08-22'
category: Agent
direction: 垂直领域Agent · 评测基准与失败分析
tags:
- Coding Agent
- Benchmark
- Evaluation
- Vertical Domain
- Failure Analysis
one_liner: 推出跨20个科学领域的代码库级编码Agent评测基准，明确科学编码任务四类典型失败机制
practical_value: '- 垂直领域Agent落地时，可参考本文三类任务范式（问题驱动、专家探索、工程集成）设计评测集，避免仅看整体成功率忽略细分场景缺陷

  - 给Agent注入领域知识需做对齐校验，精准匹配的领域知识可提升token效率与性能，错配知识反而会引发锚定偏差降低效果

  - 分析Agent失败原因时可复用本文四类归因框架（知识缺失、探索偏差、覆盖不全、泛化不足），快速定位优化方向'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有编码Agent评测仅聚焦整体任务成功率，无法解释科学领域代码修复任务的失败根因，而科学代码缺陷会直接影响科研结论可信度，缺乏面向垂直科学场景的专属评测基准。
### 方法关键点
- 发布SWE-bench Science代码库级基准，覆盖20个科学领域98个GitHub仓库的119个软件工程任务，分为Issue-driven、Expert-exploratory、Engineering-integration三类范式
- 开展配对消融实验，对比保留代码工程上下文前提下有无显式科学指导的效果差异
### 关键结果数字
- 最优Claude Code with Opus-5 (max)的pass@1不足50%，科学领域编码任务难度远高于通用场景
- 总结出4类高频失败机制：科学知识/抽象能力缺失、探索方向偏差/表层修复、修复覆盖不全/系统集成失败、科学知识泛化不足
- 精准对齐的科学指导可提升平均性能与token效率，错配的科学指导会引发锚定效应，无法提升修复成功率
