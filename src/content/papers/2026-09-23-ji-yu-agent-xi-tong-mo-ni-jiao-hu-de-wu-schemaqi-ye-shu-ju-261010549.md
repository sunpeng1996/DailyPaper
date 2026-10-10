---
title: 'Synthesis Through Simulation: Generating Coherent Enterprise Data via Scalable
  Agent-System Interaction'
title_zh: 基于Agent-系统模拟交互的无Schema企业数据合成框架
authors:
- Yipeng Li
- Ashutosh Hathidara
- Jane Lo
- Harshavardhan Abichandani
- Gunraj Singh
- Atin Ghosh
affiliations:
- SAP Labs
arxiv_id: '2610.10549'
url: https://arxiv.org/abs/2610.10549
pdf_url: https://arxiv.org/pdf/2610.10549
published: '2026-09-23'
collected: '2026-10-10'
category: Agent
direction: Agent 企业工具调用训练数据合成
tags:
- Agent
- Data Synthesis
- Tool Calling
- LLM
- Enterprise AI
one_liner: 提出无Schema的STS数据合成范式和通用填充Agent GP，保证100%结构有效性同时兼顾分布保真度
practical_value: '- 电商/广告场景训练工具调用Agent缺合规数据时，可复用STS范式：搭建模拟业务API层（内置业务规则校验），让Agent调用API生成合规训练数据，避开用户隐私/数据权限问题，无需依赖数据库Schema

  - 通用填充Agent GP的三阶段（EXPLORE/PLAN/EXECUTE）+ 跨轨迹共享的ExplorationManifest记忆机制可直接迁移到多轮工具调用Agent流程设计，仅需3次探索即可拿到最优效果，落地成本低

  - Agent生成训练数据时，新增PLAN阶段做任务多样性控制，相比无规划批量生成可提升分布保真度6%以上，避免数据分布偏斜，适合生成推荐/广告场景的用户行为模拟数据

  - 下游工具调用Agent做SFT时，使用多样性更高的STS合成数据训练，相比有限种子数据训练版本pass@k可提升0.12+，适合优化电商客服/运营Agent的工具调用能力'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
企业工具调用Agent的训练/评估依赖真实业务数据，但受隐私合规、Schema权限限制无法直接获取；传统表格合成方法要么无法保证动态业务规则有效性，要么需要逐域手工配置规则，冷启动难度高。

### 方法关键点
- 提出STS范式：将数据合成的结构有效性完全交给模拟企业环境的API层校验，Agent所有写操作都经过API预校验，从构造上保证100%符合业务规则，无需访问底层数据库Schema
- 通用填充Agent GP采用三阶段流程：EXPLORE阶段仅调用读接口推断实体依赖关系、工具分类，仅需3次探索即可完成；PLAN阶段基于探索结果生成多样化任务，保证数据分布覆盖；EXECUTE阶段执行任务，跨轨迹共享ExplorationManifest记忆沉淀成功heuristic，减少重复试错
- 解耦有效性校验和分布拟合两个目标，两者可独立优化，无需逐域手工编写业务规则

### 关键实验
在10个覆盖电商、HR、航空、银行等的企业环境测试，对比CTGAN/SDV等统计合成器、Schema特权的EnvScaler基线：
1. GP在所有环境达到100%约束满足率，平均边际保真度0.88，7个无种子数据的冷启动场景下统计合成器完全不可用
2. 航空场景下Schema特权的EnvScaler有82%的轨迹失败，GP的边际保真度0.973、联合保真度0.9、跨表保真度0.949全面领先
3. 用STS生成的数据训练Qwen2.5-7B工具调用Agent，在τ2-bench航空数据集上pass@k达0.5，比种子数据训练版本高0.125，比base模型高0.214

### 核心结论
将业务规则校验下沉到API层、通过Agent交互生成数据的范式，既能解决企业数据合规问题，又能比传统合成方法拿到更优的分布保真度和结构有效性
