---
title: 'ASI-Bench: At the Dawn of Artificial Superintelligence'
title_zh: ASI-Bench：面向超人工智能的自主科研能力评估基准
authors:
- Junwei Zhou
- Zhen Sun
- Binyu Li
- Jiangyu Zhou
- Yuexi Pan
- Hengyu Wang
- Honghe Ren
- Xiaohan Jia
- Xueyang Zhou
- Xiaoyu Cao
affiliations:
- Tsinghua University
- Massachusetts Institute of Technology
- Harvard University
- Carnegie Mellon University
- University of Michigan
arxiv_id: '2608.17271'
url: https://arxiv.org/abs/2608.17271
pdf_url: https://arxiv.org/pdf/2608.17271
published: '2026-08-17'
collected: '2026-08-19'
category: Agent
direction: Agent 自主科研能力评估基准
tags:
- Benchmark
- Autonomous Research
- Agent Evaluation
- ASI
- Scientific Agent
one_liner: 推出首个梯度撤去人类方法指导的跨领域项目级科研Agent能力评估基准
practical_value: '- 做Agent能力评估时可复用「梯度减少人工指导」的分级评估范式，清晰拆解Agent在任务理解、方法选择、落地执行各环节的能力短板，可直接用于评估电商选品、营销方案生成等业务Agent的自主决策能力

  - 复杂长周期Agent任务的评测设计可参考其多轮专家审核+沙箱执行验证的流程，确保评测结果稳定无漏洞，避免Agent走捷径刷分，适合大促智能运营Agent等核心业务Agent的上线前评测

  - 业务Agent选型时可参考其结论：同一底座模型搭配不同Agent Harness（执行框架）性能差异可达40%以上，不需要盲目追更大底座，优化Agent执行框架的投入产出比更高'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有AI基准多聚焦知识记忆或固定流程下的任务执行能力测试，无法衡量AI在无明确人工指导下自主完成开放、复杂项目级科研任务的真实能力，难以支撑超人工智能（ASI）发展路径上的能力进展量化评估。
### 方法关键点
- 采用分级指导设计：同一科研任务设置4档输入梯度，B1提供完整方法步骤，B2仅给出方法类别，B3仅提供研究目标与数据，B4在B3基础上增加无关干扰信息，精准拆解Agent不同环节的自主能力
- 覆盖11个科学领域共60个项目级科研任务，单任务平均需要2600+交互轮次、2400+执行步骤，要求Agent完成从问题理解到结果输出的全流程科研工作
- 构建流程经过5轮专家交叉审核、AI辅助校验、沙箱全流程执行验证，累计投入3.1万+人时，严格规避信息泄露、评估逻辑偏差、Agent捷径刷分等问题
### 关键实验
测试18种SOTA Agent框架+大模型底座组合：平均得分从B1的50.91骤降到B2的29.10，B3仅为26.62，证明当前Agent极度依赖人类详细步骤指导；同一底座搭配不同Agent框架性能差距最高可达44%；最强配置（Codex+GPT-5.6 Sol ultra）B3得分仅51.60，远未达到可靠自主科研水平。
### 核心结论
当前AI自主科研的核心瓶颈不是方法选型能力，而是把方法转化为完整可执行流程的落地能力，盲目提升大底座推理规格的投入产出比远低于优化Agent执行框架。
