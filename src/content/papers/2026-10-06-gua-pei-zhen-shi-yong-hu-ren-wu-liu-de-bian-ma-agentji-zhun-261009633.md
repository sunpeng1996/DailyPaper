---
title: Coding-Agent Benchmarks Should Match Their Users' Task Flows
title_zh: 适配真实用户任务流的编码Agent基准评估优化框架SWE-TaskFlow
authors:
- Igor Slinko
- Yaroslav Golubev
- Sergey Titov
affiliations:
- JetBrains Research
arxiv_id: '2610.09633'
url: https://arxiv.org/abs/2610.09633
pdf_url: https://arxiv.org/pdf/2610.09633
published: '2026-10-06'
collected: '2026-10-12'
category: Eval
direction: 交互式Agent评估 · 任务流校准
tags:
- Agent Evaluation
- Benchmarking
- Task Flow
- Interactive Agent
- TFAS
one_liner: 基于4782条真实开发会话提出SWE-TaskFlow，校准编码Agent基准匹配真实任务流
practical_value: '- 做垂直场景（如电商导购、客服、运营Agent）评估时，优先采集自家产品真实用户会话的Task Flow（会话长度、意图分布、意图跳转）作为校准目标，避免离线评估结果与线上表现脱节

  - 现有已验证的基准数据集无需完全重构，可通过prompt拆分、插入可验证的领域QA问题的方式改造，大幅降低自定义评估集的构建成本

  - 可复用TFAS（TaskFlow Alignment Score）计算逻辑，量化改造后基准与真实任务流的匹配度，保证评估的真实性和可对比性

  - 多轮交互评估产出的细粒度验证信号，可直接作为RLHF/GRPO类训练的偏好信号，提升Agent的多轮交互能力'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有编码Agent基准大多基于GitHub issue导出，普遍为单轮交互、任务类型集中在bug修复/新功能开发，与真实用户多轮交互、意图频繁切换的使用模式差异极大，评估结果无法反映线上真实表现；且不同产品的用户交互分布差异显著，不存在通用的「真实」基准。

### 方法关键点
1. 定义**Task Flow**为三维分布：会话长度分布、单轮任务意图分布、相邻轮意图跳转分布，作为基准校准的核心目标
2. 提出SWE-TaskFlow框架改造现有issue类基准：
   - 单轮issue拆分为多轮逐步披露需求的prompt，严格保证不丢失原始需求、不引入新需求
   - 插入可验证的仓库QA问题，补充真实会话中高频的explain类意图，问题需通过执行层校验确保答案可复现
   - 提出TFAS分数，基于Jensen–Shannon散度衡量基准与真实任务流的匹配度，优先选择匹配度最高的多轮轨迹
3. 所有改造保留原始基准的仓库、测试用例，保证任务的可验证性和可复现性

### 关键实验
以JetBrains IDE的4782条真实开发者会话（33%为≥3轮的长会话）为校准目标，在700条SWE-Bench Pro任务上验证：
1. 改造后的基准TFAS从纯拆分版本的59.6提升到77.8，与真实任务流匹配度大幅提升
2. 多轮拆分模式下Agent调用成本约翻倍，解决率无稳定升降，说明交互协议本身是评估的核心变量
3. QA问题回答准确率在4个测试模型上介于69.8%~83.0%，提供了除任务解决率之外的第二个可验证信号

### 核心结论
不存在通用的真实交互式Agent基准，所有基准都需要明确目标用例，基于对应场景的真实用户交互数据校准
