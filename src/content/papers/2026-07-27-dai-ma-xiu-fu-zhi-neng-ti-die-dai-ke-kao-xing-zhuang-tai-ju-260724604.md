---
title: 'Looping Is Not Reliability: State-Bound Evidence and Typed Revision Contracts
  for Agentic Code Repair'
title_zh: 代码修复智能体迭代可靠性：状态绑定证据与类型化修订合约
authors:
- Xueping Gao
- Jianwei Yang
- Qiang Yang
affiliations:
- Alibaba Cloud
arxiv_id: '2607.24604'
url: https://arxiv.org/abs/2607.24604
pdf_url: https://arxiv.org/pdf/2607.24604
published: '2026-07-27'
collected: '2026-07-28'
category: Agent
direction: 智能体代码修复 · 迭代可靠性机制
tags:
- AgentReliability
- CodeRepair
- LLM
- IterativeRefinement
- Verification
one_liner: 提出状态绑定证据与类型化修订合约，解决代码修复Agent迭代中正确状态易丢失的问题
practical_value: '- 做业务侧迭代式Agent（如广告文案生成、推荐策略调优、规则自动迭代Agent）时，需对反馈加状态绑定校验：只有反馈对应的状态哈希与当前状态一致时才允许用于修订，避免旧的错误反馈将已生成的正确结果改坏

  - 迭代过程中强制保留last-known-good checkpoint，只要未通过外部校验就回滚到最近的正确状态，可应用于A/B实验参数迭代、商品文案批量生成等场景，避免错误结果流出

  - 迭代停止策略不要依赖LLM自评估，需引入独立的外部可执行校验门，同时校验不同评估器的错误相关性，避免同系列模型的共通错误导致错误放行'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
生成-测试-修订的迭代循环是当前编码Agent的通用范式，但现有方案仅关注迭代过程中是否出现过正确结果，忽略了迭代中正确状态易被后续修改破坏、过期反馈误导等问题，导致最终提交结果的可靠性远低于过程最优水平：测试中迭代1次后正确率达82%，强制迭代2次反而降至67.3%，16%的轨迹出现过正确结果后又丢失。
### 方法关键点
- 设计轨迹级可靠性分解指标，同时度量正确结果发现率、保留率、正误状态转移率、校验器风险覆盖率与错误依赖度
- 开展共同状态干预实验，固定初始代码状态后对比不同证据的影响，消除后处理风险集偏差
- 提出状态绑定证据+类型化修订合约：反馈必须绑定对应代码状态哈希，不匹配则禁止用于修订；修订动作限定为保留/提交补丁/升级三类；自动保留最近通过校验的 checkpoint；基于校验器实际风险校准停止策略
### 关键结果
基于30个HumanEval修复任务、24个真实仓库bug测试：14B模型下使用过期反馈的正确状态损毁率达25.2%，比使用当前反馈高22.2个百分点；状态绑定机制可拦截100%过期反馈导致的正确状态损毁，配合类型化动作可将总损毁率从69降至33；引入可执行挑战校验门可将错误接受风险从29.5%降至0，覆盖率保持77.8%。
> 最值得记住的结论：迭代只能提供更多候选，本身不能保证可靠性，迭代收益与风险由反馈有效性、状态管理、校验机制共同决定，而非迭代次数。
