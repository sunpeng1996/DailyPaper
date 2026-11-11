---
title: 'ARE-bench: Benchmarking Agents'' Research Ability in Real-World Researcher
  Sessions and Workspaces'
title_zh: ARE-bench：面向真实研究会话与工作空间的研究Agent能力基准
authors:
- Jiahang Lin
- Wanying Ren
- Wanghan Xu
- Huayu Sha
- Yang Shu
- Zhonghang Lu
- Chengjun Pan
- Yi Dong
- Shichun Liu
- Yuyang Hu
affiliations:
- Shanghai Artificial Intelligence Laboratory
- Fudan University
- East China Normal University
- Shanghai Jiao Tong University
- Renmin University of China
arxiv_id: '2611.14364'
url: https://arxiv.org/abs/2611.14364
pdf_url: https://arxiv.org/pdf/2611.14364
published: '2026-11-10'
collected: '2026-11-11'
category: Agent
direction: 研究Agent · 真实场景能力评测基准
tags:
- Agent-Benchmark
- Research-Agent
- Context-Aware
- Workspace-Evaluation
- Session-Context
one_liner: 基于真实研究者会话和未清理工作空间，构建75任务基准评测研究Agent的在研项目推进能力
practical_value: '- 设计电商/推荐领域业务Agent（如运营Agent、策略迭代Agent）评测体系时，可复用「保留历史生效上下文+未清理工作空间」的任务设计思路，避免用干净独立任务高估Agent实际落地能力

  - Agent任务验收checklist可参考分层校验设计：先校验交付契约与通用规范，再补充历史决策约束、工作空间适配要求，覆盖隐性业务规则，减少漏判

  - 业务Agent选型时，不能仅看编码、写作等单维度能力，需重点校验方案设计、执行落地两个高难度阶段的表现，避免局部能力强但整体交付成功率低'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有研究Agent基准多聚焦独立任务、干净人工构造的工作空间，无法反映真实在研项目中Agent需承接历史决策、适配含未完成文件/过时版本/失败尝试的工作空间的实际表现，会严重高估Agent能力，也无法区分不同模型的真实交付能力差距。

### 方法关键点
- 从真实研究者的项目会话中筛选75个任务，覆盖调研、设计、数据&环境、编码、执行、分析、写作7个研究阶段，共1173项二元校验项
- 任务保留会话边界前的所有未清理工作空间（平均每个任务41.1个文件，65.3%包含历史Agent生成文件），同时摘要仍生效的历史请求作为背景信息
- 用Instance Success Rate（ISR，需所有校验项通过才算任务成功）和Checklist Item Success Rate（CSR，分项通过率）作为核心评估指标

### 关键结果数字
- 7款前沿模型中，最强的GPT-6.1-Sol整体ISR仅为66.2%，其余5款模型ISR均低于40%
- 仅校验交付契约与通用规范时，3款模型ISR约为69%，加入历史与工作空间约束后ISR降至28.4%~40.0%，模型间能力差距被放大10个量级
- 设计、执行是所有模型的最薄弱阶段，两类任务的最优与最差模型ISR差距最高达37.4个百分点

**最值得记住的一句话：脱离项目历史上下文和真实工作空间的Agent评测结果会严重高估其实际落地交付能力，且掩盖模型间的真实能力差距
