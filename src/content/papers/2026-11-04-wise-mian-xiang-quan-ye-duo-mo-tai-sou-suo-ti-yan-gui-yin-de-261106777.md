---
title: 'WISE: An Agentic Framework for Whole-page Multimodal Search Experience Attribution'
title_zh: WISE：面向全页多模态搜索体验归因的智能体框架
authors:
- Wenyi Xu
- Renzhe Zhou
- Songyang Li
- Feiran Zhu
- Ruoqi Zhao
- Chenglei Dai
- Xuanping Li
- Kaiqiao Zhan
- Jingwei Zhuo
affiliations:
- Kuaishou Technology
- Independent Researcher
arxiv_id: '2611.06777'
url: https://arxiv.org/abs/2611.06777
pdf_url: https://arxiv.org/pdf/2611.06777
published: '2026-11-04'
collected: '2026-11-05'
category: Agent
direction: 智能体 · 搜索系统质量诊断
tags:
- LLM Agent
- System Quality Diagnosis
- Search Quality Evaluation
- Agent Optimization
- Benchmark
one_liner: 提出系统质量诊断任务、WISE智能体框架与基准，实现搜索质量问题端到端归因
practical_value: '- 可复用ReTrace轨迹修复方法：仅用专家标注的最终结果即可修复智能体执行轨迹，低成本生成高质量SFT数据，无需标注全链路执行步骤，解决业务场景Agent训练缺标注的痛点

  - 可借鉴AHPO自适应调优策略：将智能体错误分为harness（工具/上下文/schema层面）和policy（模型决策层面）两类分别优化，无需修改模型权重即可先通过harness优化提效，大幅降低落地调优成本

  - 可直接复用闭环迭代路径：先通过该框架实现全链路badcase自动归因，再将归因得到的定向badcase补充到召回、排序模型训练集，实现搜索/推荐系统的自迭代，实测可带来CTR、长看占比等业务指标提升

  - 多模态搜索/推荐质量标注可参考WISE-Bench的两阶段范式：先标注用户侧体验问题，再关联内部pipeline做根因标注，降低标注成本，提升标注一致性'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
当前搜索、推荐、广告系统的部署后监控仅覆盖运行可靠性（延迟、可用性、错误率），但运行状态正常的系统仍可能返回不符合用户意图的低质量结果，现有评估体系只能识别坏结果，无法定位问题根因对应的链路模块，也缺少统一的任务定义和公开基准。
### 方法关键点
- 定义System Quality Diagnosis（SQD）任务，要求同时完成用户侧质量问题发现、坏商品定位、内部pipeline根因归因
- WISE采用分层多Agent架构，分为问题发现组、归因组、报告生成组，harness负责上下文管理、工具调用权限控制、状态校验，LLM policy负责推理决策
- ReTrace轨迹修复方案：保留原始执行轨迹的正确前缀，仅修复错误后缀生成符合专家标注的证据一致轨迹，用于SFT，比全量重新生成降低36%的token成本
- AHPO自适应优化策略：将错误分为harness缺陷（证据不足、工具不支持、schema不匹配）和policy决策错误两类，分别优化harness或用GRPO微调policy
- 构建WISE-Bench，包含12k真实多模态搜索case，配套用户体验标注、pipeline全链路数据、专家归因标注
### 关键实验
在WISE-Bench 2k测试集上验证：Qwen3.5-35B-A3B作为backbone时，端到端Exact Match从基线的35.25%提升至75.20%；仅优化harness不改模型权重时，GPT-5.6-Terra的E2E EM从65.85%提升至69.75%；落地快手生产后，诊断成本比人工降低99.55%，用归因badcase优化相关性模型，线上CTR提升0.15%，长看占比提升0.20%。
### 核心结论
工业级Agent落地的收益，很大一部分来自harness层的优化，而非单纯依赖大模型能力或参数微调。
