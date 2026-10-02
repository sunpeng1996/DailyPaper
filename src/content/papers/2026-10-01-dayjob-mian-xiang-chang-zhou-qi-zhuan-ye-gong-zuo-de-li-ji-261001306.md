---
title: 'DAYJOB: A Benchmark for Long-Horizon Professional Work'
title_zh: DAYJOB：面向长周期专业工作的Agent能力基准测试集
authors:
- Stephanie Finley
- Liudas Panavas
- Thomas Mikkelson
- Cam Hinton
- Stacey Ganss
- Bradley Monton
- Emily Kendall
- Michelle Spradlin
- Lydia Bye
- Michael O'Brien
affiliations:
- Surge AI
arxiv_id: '2610.01306'
url: https://arxiv.org/abs/2610.01306
pdf_url: https://arxiv.org/pdf/2610.01306
published: '2026-10-01'
collected: '2026-10-02'
category: Eval
direction: Agent能力评测 · 长周期专业任务
tags:
- Agent
- Benchmark
- Long-Horizon Task
- Professional Work
- Evaluation
one_liner: 构建含130个医疗/金融长周期专业任务的基准，测试Agent处理真实工作场景的能力
practical_value: '- 可复用「极简请求+多源异构文档池+全符合二进制判据」的测试范式，构建电商/广告业务Agent内部评测集，适配运营需求自动化、投放素材审核等场景的任务验收标准

  - 工程上可借鉴container化运行+agentic judge自动判分的架构，减少业务Agent上线前的人工评测成本，尤其适用于跨多文档校验的场景（如大促活动规则校验、账单核对）

  - 优化长周期任务Agent时，可针对性强化「质疑请求前提、校验输入数据正确性」两个能力，减少业务中基于错误前提输出方案、算错投放ROI等问题

  - 高要求业务场景可参考「全符合严格判据+分阈值弹性判据」的组合评估方式，平衡容错率与核心要求的不可妥协性，比如电商合规审核场景核心规则必须100%符合'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有Agent基准多聚焦短周期、指令明确的任务，缺少真实职场中「指令模糊、依赖多源异构文档、隐含隐性要求、需要独立决策」的长周期专业工作场景，无法有效衡量Agent落地真实业务的能力。
### 方法关键点
- 任务设计：由医疗/金融专业人士构建130个真实工作任务（50个医疗、80个金融），单任务人类完成时长平均13.6/16.6小时，仅提供极简工作请求（平均48.9/80.7字），附带包含大量无关、冲突、多格式（PDF/表格/Word）输入文件的工作区
- 评估范式：每个任务配套几十条二进制判据（中位数47.5/57.5条），Agent必须100%满足所有判据才算通过；采用container化环境限制外网访问，搭载terminal、文件编辑器等通用工具，运行完成后由agentic judge自动校验所有判据，无需人工参与
- 配套资源：开源全部50个医疗任务、50个金融任务、评测框架、排行榜，供社区迭代
### 关键结果
测试13家厂商的30种模型配置，每个任务跑5次：
- 最优模型Claude Opus 5.5（自适应最大推理）仅达到24.7%医疗任务通过率、23.9%金融任务通过率，中位数配置通过率仅0.6%/2.5%，19种配置通过率低于5%
- 放松判据到满足90%即可通过时，最优模型通过率提升到62.4%/58.3%，中位数配置到6.4%/10.4%
- 最优模型单任务平均处理9.8M/17.8M tokens，94%以上为缓存输入，单任务成本7.1/11.47美元
### 核心结论
当前最先进的Agent在真实长周期专业工作中的落地能力仍然极弱，核心短板是不会质疑请求前提、容易基于错误输入输出逻辑自洽但结果错误的方案
