---
title: Self-Evaluating Recursive Agents
title_zh: 自评估递归智能体（SERA）：共享权重的递归Agent训练框架
authors:
- TianYi Lyu
- Xiaozhe Li
- Yang Li
- Yongkang Chen
- Kefei Tian
- Junbo Niu
- Zican Hu
- Hongbo Liu
- Mingliang Xiong
- Qingwen Liu
affiliations:
- Tongji University
- Shanghai Artificial Intelligence Laboratory
- Shanghai Jiao Tong University
- Peking University
- Nanjing University
arxiv_id: '2610.04902'
url: https://arxiv.org/abs/2610.04902
pdf_url: https://arxiv.org/pdf/2610.04902
published: '2026-10-03'
collected: '2026-10-20'
category: Agent
direction: 递归Agent · 自评估训练优化
tags:
- Recursive Agent
- Self-Evaluation
- Rubric Reward
- Reinforcement Learning
- Multi-Agent
one_liner: 通过共享权重同步学习任务分解、执行、自评估能力，显著提升递归Agent表现并降低外部监督成本
practical_value: '- 电商导购/复杂咨询类递归Agent落地时，可复用叶子覆盖率奖励优化任务拆分逻辑，避免生成无意义子任务，降低无效调用成本

  - 业务中依赖外部LLM Judge做中间结果打分的场景，可借鉴rubric自评估机制，仅用少量外部标注训练rubric生成能力，后续自生成连续打分可替代90%以上外部Judge调用，实测降本4-5倍

  - 推理阶段可复用训练好的rubric打分做候选分支排序，比如多商品组合推荐、大促活动方案生成的结果筛选，无需额外训练即可提升最终效果'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
递归Agent通过拆分复杂任务下发给同策略子实例并行处理，是当前长程任务Agent的主流架构，但训练存在核心痛点：仅最终任务结果有可验证标注，中间自生成子任务无ground truth；现有用外部Judge给每个节点打分的方法成本高、信号粗（仅二元）、无法评估任务拆分质量，制约递归Agent的落地性价比。
### 方法关键点
- 将递归Agent的核心能力拆分为任务分解、子任务执行、结果评估三个耦合模块，全部共享同一套权重，通过三个独立奖励信号交替训练避免参数干扰
- 父Agent下发子任务前提前生成冻结的加权rubric评分标准，子任务完成后用同策略无梯度调用rubric生成连续得分，作为子任务执行的奖励
- 新增叶子覆盖率奖励：仅整棵任务树成功时，按子任务树覆盖的原子任务叶子节点占比给拆分动作发放奖励，直接优化任务拆分合理性
- rubric生成能力用排序损失训练：对同一子任务的多个反事实rollout，要求rubric将外部Judge判定成功的结果打分高于失败结果，仅该阶段使用外部监督
### 关键结果
在TextCraft-Synth、TextWorld-Sync两个基准上，SERA比最优递归Agent基线RAO平均提升5.38、13.14个百分点；外部LLM Judge调用量降低4.1倍，输入token消耗降低5.1倍；推理阶段用rubric引导树搜索可在TextWorld-Sync上额外提升2.43个百分点。
> 最值得记住的结论：让执行任务的同一套权重学会自我评估，评估能力的提升会反向强化执行能力，是递归Agent性能提升的核心来源。
