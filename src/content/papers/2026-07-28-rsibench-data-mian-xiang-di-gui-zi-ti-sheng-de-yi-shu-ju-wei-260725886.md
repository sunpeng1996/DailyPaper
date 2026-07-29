---
title: 'RSIBench-Data: Benchmarking Data-Centric Research for Recursive Self-Improvement'
title_zh: RSIBench-Data：面向递归自提升的以数据为中心研究基准
authors:
- Fanqing Meng
- Lingxiao Du
- Qiguang Chen
- Ziqi Zhao
- Haocheng Lu
- Mengkang Hu
- Michael Qizhe Shieh
affiliations:
- Evolvent AI
- National University of Singapore
arxiv_id: '2607.25886'
url: https://arxiv.org/abs/2607.25886
pdf_url: https://arxiv.org/pdf/2607.25886
published: '2026-07-28'
collected: '2026-07-29'
category: Agent
direction: Agent 自迭代能力评估基准
tags:
- Agent
- Benchmark
- Recursive Self-Improvement
- Data-Centric
- Post-Training
- LoRA
one_liner: 首个隔离评估LLM Agent数据-centric post-training研究能力的可控基准
practical_value: '- 做推荐/广告模型的Agent驱动迭代优化时，必须固定训练、评估基建，排除环境变量才能准确归因数据策略的效果，避免将基建差异误认为是数据迭代的收益

  - 迭代优化训练数据策略时必须保留历史最优checkpoint，现有Agent在78%的峰值后迭代尝试中会出现性能回落，不要盲目追求迭代次数

  - 优化数据策略可复用4个有效特征：精准的能力缺口假设、基于验证的监督数据、与目标行为对齐的数据集、保留强checkpoint，适配推荐场景的微调数据迭代流程

  - 算力预算有限的场景下，优先用高推理effort做深度数据构造，比多次浅度迭代尝试的性价比更高，适合中小流量的推荐模型快速微调'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有面向递归自提升的自动化post-training基准混杂了优化、部署、评估、系统实现等多个变量，无法隔离评估LLM Agent作为以数据为中心的研究员的核心能力，难以准确衡量Agent自动将模型失败证据转化为更优训练数据策略的真实水平。

### 方法关键点
- 固定全套post-training基建栈：所有Agent共享Tinker提供的LoRA SFT训练服务、Harbor编排的E2B沙箱评估服务、统一的基础模型、资源预算、评估规则，仅放开训练数据策略与白名单内训练配置的修改权限，彻底隔离基建差异对结果的影响。
- 评估完整闭环决策能力：要求Agent迭代完成「能力缺口假设→训练数据策略设计验证→提交训练→根据反馈修订策略」的全流程，记录完整决策轨迹而非仅评估最终模型效果。
- 覆盖6类不同任务：包含3个SWE系列代码任务、Terminal-Bench 2.0终端工具使用、GPQA Diamond科学问答、AIME 2026数学推理，覆盖不同场景的训练数据构造需求。

### 关键结果
在4个前沿Agent（Claude Code系列、Codex系列）的对比实验中，58.33%的场景下Agent可通过迭代数据策略超过首次有效尝试的效果，具备初步的数据-centric研究能力；但在达到观测峰值后继续迭代的场景中，78.26%的最终尝试效果低于已达到的峰值，剩余场景仅能回到原有峰值，无进一步提升。

最值得记住的结论：当前LLM Agent尚无法稳定将反馈转化为持续的模型提升，历史最优checkpoint保留是现阶段Agent自迭代流程的必要组件。
