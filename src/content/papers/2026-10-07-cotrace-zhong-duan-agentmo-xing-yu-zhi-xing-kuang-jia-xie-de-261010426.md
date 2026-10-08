---
title: 'CoTrace: Data Recipes for Training Terminal Agents with Harness-Model Co-Evolution'
title_zh: CoTrace：终端Agent模型与执行框架协同进化的数据规范
authors:
- Jixuan Chen
- Jiaxin Zhang
- Qinyuan Ye
- Yada Pruksachatkun
- Haoxiang Zhang
- Jingming Zhuo
- Yifan Zhang
- Yutong Dai
- Juntao Tan
- Xiangyu Peng
affiliations:
- University of California, San Diego
- Salesforce AI Research
- University of Washington
arxiv_id: '2610.10426'
url: https://arxiv.org/abs/2610.10426
pdf_url: https://arxiv.org/pdf/2610.10426
published: '2026-10-07'
collected: '2026-10-08'
category: Agent
direction: Agent协同进化 · 数据规范设计
tags:
- Agent
- Co-Evolution
- SFT
- RL
- Data Selection
one_liner: 提出感知harness的Agent协同进化数据规范，用更少轨迹实现更高性能与跨域迁移能力
practical_value: '- 做Agent/大模型推荐系统迭代时，无需盲目积累大量训练轨迹，仅筛选与当前部署的prompt模板、工具绑定、上下文处理逻辑完全匹配的成功轨迹做SFT，30-50条匹配轨迹即可实现比数百条混杂轨迹更稳定的收益，同时降低训练算力成本

  - 模型与业务配套逻辑（如推荐Agent的召回规则、prompt模板、错误处理流程）协同迭代时，执行组件级晋升校验：更新业务逻辑时固定模型权重，更新模型时固定业务逻辑，可明确收益归因，避免回归

  - 跨场景迁移Agent/大模型推荐能力时，不要仅迁移模型权重，需将配套的业务执行逻辑一同迁移，可大幅减少执行故障，释放模型在OOD场景下的潜在能力，例如电商跨类目迁移选品Agent时同步迁移类目适配的prompt与工具链'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有终端Agent的模型与执行框架（harness，负责prompt格式化、工具绑定、错误恢复）协同进化方案，通常把迭代中产生的所有轨迹扔进无差别回放缓冲区，忽略了轨迹的训练价值和生成它的harness强绑定，容易出现训练数据与部署runtime不匹配、模型更新无收益甚至负向的问题。

### 方法关键点
- 交替协同进化框架：先固定模型权重更新harness，再固定harness更新模型，用固定的promotion split做组件级晋升校验，仅当新组件净解决任务数大于退化数时才落地，避免回归
- 核心三机制：Route机制将失败轨迹导去做harness优化，仅与当前harness匹配的成功轨迹可用于模型训练，不足时补充同harness下的新生成轨迹；Ratchet机制做组件级独立归因，确保每个收益明确来自模型或harness；Refresh机制动态淘汰已掌握任务，将迭代资源集中在未解决的前沿任务上
- 两种训练变体：CoTrace-SFT用匹配轨迹做LoRA微调，CoTrace-RL用同harness下的在线交互奖励做强化学习

### 关键实验
在Tmax的102任务promotion split上，Qwen3.5-9B基线解决78个任务，CoTrace-SFT提升到88个，CoTrace-RL提升到90个；对比基线用149-308条混杂harness的轨迹训练无模型增益，CoTrace-SFT仅用30-50条匹配轨迹就实现+6的模型收益，单迭代算力消耗降低13%。跨域测试中，SWE-bench Lite上同harness部署比用第三方框架的无patch失败数最多降低59%，性能最高提升10.3pp。

最值得记住的一句话：Agent的能力是模型和执行框架的共同产物，轨迹与部署runtime的匹配度比轨迹数量对训练增益的影响大得多。
