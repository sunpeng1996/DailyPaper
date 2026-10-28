---
title: Rethinking Verification in Agent Harnesses
title_zh: Agent执行框架的验证机制设计与效果对比研究
authors:
- Zhengxin Zhang
- Erkang Zhu
- Yin Lin
- Claire Cardie
- Bolin Ding
- Jingren Zhou
affiliations:
- Cornell University
- Alibaba Group
arxiv_id: '2610.34577'
url: https://arxiv.org/abs/2610.34577
pdf_url: https://arxiv.org/pdf/2610.34577
published: '2026-10-24'
collected: '2026-10-28'
category: Agent
direction: Agent执行框架 · 验证机制优化
tags:
- Agent Harness
- Verification
- LLM Agent
- Critic
- Test-time Scaling
one_liner: 系统对比4层17种Agent执行框架验证方案，验证独立critic审核具备最优准确率-成本比
practical_value: '- 搭建业务Agent（如电商文案生成、商品信息抽取、推荐策略调优Agent）时优先采用L3独立critic验证机制：选用低成本小模型作为critic，仅输入任务要求+Agent产出变更内容，可在仅增加13%-25%成本的前提下提升5.9-9.5pp准确率，远优于让主Agent自检的方案

  - 若预算有限可搭配轻量前置验证策略：将校验要求写入系统prompt而非用户prompt，同时在Agent每次输出修改后推送系统校验提醒，可在不显著增加成本的前提下获得3-5pp的准确率提升

  - 需规避高成本低收益的自检方案：不要在Agent完成任务后强制其自检，该类方案成本提升48%-76%但收益仅与轻量前置策略相当，性价比极低

  - 对交互类/生成类Agent任务（如电商活动页搭建、商品短视频脚本生成）可叠加多轮critic或多critic并行校验，额外提升最高3.5pp准确率'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前Agent执行框架（harness）的验证机制多依赖工程经验启发式设计，缺乏系统性的效果、成本对比指导，现有自检、校验方案的收益是否匹配额外算力投入没有实证支撑，无法适配不同模型、任务的优化需求。

### 方法关键点
- 按照Agent生命周期将验证机制划分为4层：L0初始指令校验引导、L1执行过程校验提醒、L2完成后自我检查门控、L3独立critic审核
- 共设计17种验证变体，覆盖干预时机、校验主体、反馈方式三个核心维度，其中L3层进一步对比是否传入Agent执行轨迹、是否加入可视化校验等设计

### 关键实验结果
- 实验覆盖3类数据集：Terminal-Bench、SWE-bench Verified代码任务，以及自建18个视觉交互任务的VisualBench
- 对比7个前沿代码大模型，以无验证的原生Agent为baseline
- 核心量化结果：L0/L1方案仅提升1.2-5.4pp准确率，成本为baseline的0.75-1.08倍；L2自检方案提升0.5-6.2pp准确率，成本高达1.48-1.76倍；L3独立critic方案提升3.9-9.5pp准确率，成本仅为baseline的1.00-1.25倍，在VisualBench上净偏好比baseline高13.2-23.8pp；多轮/多critic可额外提升最高3.5pp准确率。

### 最值得记住的结论
让主Agent自检的性价比远低于引入独立低成本critic做校验，是Agent测试时算力扩容的最优路径。
