---
title: 'Conservative Meta-Agent Search: Architecture Adaptation under Non-Stationarity'
title_zh: 保守元代理搜索：非平稳环境下的智能体架构自适应框架
authors:
- Ali Atiah Alzahrani
arxiv_id: '2610.31436'
url: https://arxiv.org/abs/2610.31436
pdf_url: https://arxiv.org/pdf/2610.31436
published: '2026-10-22'
collected: '2026-10-23'
category: Agent
direction: Agent 元代理架构自适应优化
tags:
- MetaAgent
- ArchitectureSearch
- NonStationary
- ConservativeLearning
- Benchmark
one_liner: 提出带风险约束的CMAS框架与METAINVEST-BENCH基准，实现非平稳场景低风险架构自适应
practical_value: '- 推荐/广告系统的版本迭代可复用「候选版本-在位版本配对影子回放+方差惩罚校准门控」机制，严格控制新版本上线的负向风险，降低错误更新导致的业务损失

  - 多智能体系统（如用户建模、内容生成、审核链路）优化可借鉴Shapley式干预性信用分配方法，精准定位各组件的真实贡献，避免无用组件堆积导致的推理成本膨胀

  - 非平稳业务场景（如大促、热点事件、用户兴趣突变）的系统适配可参考「历史架构归档+基于场景特征相似度的候选检索」设计，大幅提升架构适配效率，降低切换成本'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
当前智能体架构自动搜索方案多基于静态任务集、即时标量奖励评估，而实际部署系统普遍面临环境持续漂移、反馈延迟依赖、组件关联故障、架构切换成本高、错误更新风险大等痛点，既缺乏低风险的连续自适应机制，也没有可量化衡量元代理泛化能力的可控基准。
### 方法关键点
- 将元代理架构搜索形式化为带切换成本和硬风险约束的连续在位架构替换问题，元代理覆盖候选提议、编译、评估、门控、回滚全外循环链路
- 候选生成基于历史架构归档检索，仅允许可审计的固定类型图编辑，规避无限制代码生成带来的校准偏差
- 采用同随机种子下候选与在位架构的配对影子回放评估，结合Shapley式干预性组件信用分配，大幅降低评估方差，精准定位组件贡献
- 升级需先通过经验校准的方差惩罚同步得分校验，再进入模拟金丝雀阶段，支持预设触发条件自动回滚
### 关键实验
在自研METAINVEST-BENCH的96条 regime 切换模拟流上测试，对比MaAS/AutoMaAS等7种同预算基线：归一化动态Oracle regret从0.116降至0.104，OOD效用从0.44提升至0.48，部署推理成本低6%，单轮更新虚假升级率仅3.4%（低于预设5%的风险目标）；在额外智能体无价值场景下可自动收缩到接近单智能体规模，避免架构膨胀。
### 核心启示
智能体架构迭代的核心不是追求单次最优，而是在非平稳环境下通过保守校准机制控制错误更新风险，兼顾效用、成本与鲁棒性
