---
title: 'Code Skill Server: A Large-Scale Search Engine for Code Generation Skills'
title_zh: Code Skill Server：面向代码生成技能的大规模搜索引擎
authors:
- Xiaoyong Li
- Haolong Li
- Dongliang Xu
- Haoyu Li
- Yifan Wang
- Jingyuan Shi
- Yanghua Wang
- Yanbin Sun
- Shidong Pan
- Yue Yao
affiliations:
- Shandong University
- Guangzhou University
- Independent Researcher
arxiv_id: '2610.23186'
url: https://arxiv.org/abs/2610.23186
pdf_url: https://arxiv.org/pdf/2610.23186
published: '2026-10-16'
collected: '2026-10-19'
category: Agent
direction: Agent 技能检索与服务框架
tags:
- Agent Skill
- Skill Retrieval
- Code Generation
- LLM Agent
- Search Engine
one_liner: 提出统一的代码生成技能搜索服务框架，跨模型提升代码生成任务的Pass@1效果
practical_value: '- 可复用技能库分层分类组织方法：电商/营销Agent的运营、客服、投放等技能可按业务域打标分池，检索时限定候选池减少无关结果，提升召回准确率

  - 服务端-端侧解耦架构可直接复用：服务端统一维护、迭代全量公共技能库，业务侧Agent仅需调用检索接口，无需各自重复维护技能数据，大幅降低迭代成本

  - 技能库构建流程可落地：从内部沉淀/公开资源采集技能后做归一化、去重、质量过滤，相比同规模随机选择的技能库，任务效果提升更显著

  - 跨模型适配逻辑可复用：同一技能服务可支持不同基座的业务Agent，无需针对每个基座单独优化技能库，降低多模型部署的适配成本'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
随着可复用Agent技能的数量和来源快速增长，跨异构源手动查找适配任务的技能难以规模化落地，现有技能检索方案大多局限于固定自建库，缺乏统一的技能收集、组织、检索、服务全链路框架，无法支撑不同Agent的通用技能需求。
### 方法关键点
- 服务端架构：从GitHub、Skills.sh等公开源采集代码生成技能，经过滤、归一化、SHA-256去重后，按7类能力标签分池构建索引，支持BM25、Graph-of-Skills、SkillTrace等可插拔检索算法
- 客户端交互：FASTADAPT模块自动从任务中抽取检索约束（能力标签、返回数量、token预算、相关性阈值等），向服务端发起结构化查询
- 权责分离设计：服务端仅负责返回相关度排序的技能，端侧Agent自主决定是否使用、如何组合技能，适配不同基座和业务逻辑
### 关键实验结果
在BigCodeBench、CoderEval-Python两个代码生成基准测试，对比无技能基线：最优配置下Pass@1在BigCodeBench从53.42%提升至60.88%，在CoderEval从33.04%提升至46.96%；跨5款不同代码基座测试，所有模型Pass@1至少提升4.21%，最高提升13.91%；993条经过规整的技能库比同规模随机采集的技能库Pass@1高出7.15pct，技能库规模越大效果增益越高。
### 最值得记住的结论
**规模化的Agent能力提升，核心不在于每个Agent单独积累技能，而在于统一公共技能服务层的建设与复用**
