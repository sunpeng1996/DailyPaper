---
title: 'Super Library Agent: Joint Generation and Maintenance of Multiple Applications
  Beyond the Single Codebase'
title_zh: Super Library Agent：跨单代码库的多应用联合生成与维护
authors:
- Daegyu Sung
- Yukyeong Lee
- Geon Park
- Yumin Choi
- Sung Ju Hwang
affiliations:
- KAIST
- DeepAuto.ai
arxiv_id: '2608.29310'
url: https://arxiv.org/abs/2608.29310
pdf_url: https://arxiv.org/pdf/2608.29310
published: '2026-08-28'
collected: '2026-09-01'
category: Agent
direction: Agent 多关联应用代码库共享维护
tags:
- Coding Agent
- Code Reuse
- Shared Library
- Code Generation
- Dependency Migration
one_liner: 提出Super Library Agent框架，通过共享可复用组件库生成多关联应用，降低冗余避免结构侵蚀
practical_value: '- 电商/广告后台多相似业务系统开发可复用该思路，沉淀跨业务通用组件库，避免重复开发，降低后续维护成本

  - 可借鉴候选引导提取、调用图辅助依赖迁移的思路，优化内部低代码Agent的组件生成与复用逻辑，减少生成冗余

  - 做LLM驱动的代码生成业务时，可参考预提取代码库合并的trick，提升公共逻辑提取的召回率，降低token消耗'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
现有LLM编码Agent逐应用生成维护多关联代码库时，会重复实现共享逻辑，长期维护易积累冗余代码、死代码，出现结构侵蚀，基础顺序提取框架存在公共逻辑召回率低、依赖迁移鲁棒性差的缺陷。

### 方法关键点
1. 基于代码块摘要的候选引导公共组件提取；2. 提取前先做代码库合并预处理；3. 结合提取痕迹与调用图信息做上下文感知的依赖迁移，同步维护跨应用共享的Super Library可复用组件库。

### 关键结果
在WebGen-Bench和PaperBench上可完整保留应用功能，相比零-shot方案冗余度、token footprint显著降低，避免朴素库构建的结构侵蚀问题，LOC与MDL均有额外下降。
