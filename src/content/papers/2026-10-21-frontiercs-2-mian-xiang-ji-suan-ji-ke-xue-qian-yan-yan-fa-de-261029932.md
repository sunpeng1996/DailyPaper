---
title: 'FrontierCS 2: A Benchmark for Computer Science R&D'
title_zh: FrontierCS 2：面向计算机科学前沿研发的LLM Agent基准
authors:
- Qiuyang Mang
- Wenhao Chai
- Runyuan He
- Dongruixuan Li
- Zihan Zheng
- Yujun He
- Xuanyi Zhou
- Hao Wang
- Siddhant Ray
- Bo Peng
affiliations:
- UC Berkeley
- Princeton University
- University of Waterloo
- New York University
- Georgia Institute of Technology
arxiv_id: '2610.29932'
url: https://arxiv.org/abs/2610.29932
pdf_url: https://arxiv.org/pdf/2610.29932
published: '2026-10-21'
collected: '2026-10-22'
category: Agent
direction: Agent 前沿科研能力基准测评
tags:
- Agent Benchmark
- LLM Agent
- Code Agent
- R&D Benchmark
- Capability Evaluation
one_liner: 构建覆盖13个CS领域的代码级Agent研发基准，测评12款主流Agent的科研复现与优化能力
practical_value: '- 可复用「删减已知最优实现+黑盒反馈」的评测范式，构建推荐/广告系统的算法优化Agent评测集，比如KV cache优化、召回算子优化类任务

  - FCI能力指数的构建方法可迁移到业务Agent的能力分层，按任务难度匹配不同成本的模型，平衡效果与推理成本

  - 多轮迭代+阶段反馈的Agent研发流程可复用在业务系统性能优化场景，比如让Agent基于线上压测分迭代优化推荐引擎的耗时指标'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有开放任务基准多为单次写代码打分模式，或仅覆盖单一细分领域，无法衡量LLM Agent在真实科研场景下继承已有代码库、迭代优化核心组件、超越人类已有实现的能力，缺乏对标原作者代码的客观、跨领域评测标准。

### 方法关键点
- 任务构造采用减法范式：选取已发表CS论文的官方代码库，删除核心贡献代码部分，保留其余运行依赖，要求Agent生成补丁补全并超越原实现
- 黑盒评测机制：Agent仅能拿到开发集的反馈分数，测试集、原作者参考实现、评测逻辑全部对Agent隐藏，最终提交需在所有指标上超过原实现才算通过
- 设计FCI（FrontierCS Capabilities Index）统一度量Agent能力与任务难度，可跨任务横向对比不同Agent的研发能力

### 关键结果
共48个公开任务覆盖13个CS领域（MLSys、数据库、安全等），另有100+私有任务待发布，测评12款主流Agent：最优Claude Opus 5.5的通过率仅58%，其余Agent通过率均低于50%，16个任务无任何Agent通过；任务难度中位数恰好等于当前最强Agent的FCI分值，说明基准难度匹配当前最先进Agent的能力边界；不同成本下最优Agent不同，低预算场景下DeepSeek V4.1 Flash表现最优，高预算场景下Claude Opus 5.5领先。

**最值得记住的一句话**：当前最先进的LLM Agent仅能完成一半左右的前沿CS研发优化任务，任务的整体通过率比综合得分更能反映Agent的真实落地能力。
