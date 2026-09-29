---
title: 'TimeEvo: Failure-Driven Self-Evolution of a Time Series Agent'
title_zh: TimeEvo：失败驱动的时序智能体自进化框架
authors:
- Jie Yang
- Yan Zheng
- Jiarui Sun
- Xiran Fan
- Junpeng Wang
- Liang Wang
- Zelin Xu
- Qinghua Liu
- Zhengyu Fang
- Yiwei Cai
affiliations:
- University of Illinois at Chicago
- Visa Research
- University of Florida
- The Ohio State University
- Case Western Reserve University
arxiv_id: '2609.27277'
url: https://arxiv.org/abs/2609.27277
pdf_url: https://arxiv.org/pdf/2609.27277
published: '2026-09-22'
collected: '2026-09-29'
category: Agent
direction: Agent 自进化 · 工具库动态优化
tags:
- LLM Agent
- Self-Evolution
- Time Series
- Tool Learning
- Validation Mechanism
one_liner: 提出失败驱动的时序Agent自进化框架，解决工具错配与自修订静默伤害问题
practical_value: '- 业务Agent工具库优化可借鉴失败聚类反推所需工具的思路，比人工预判更贴合Agent实际运行需求，避免盲目堆专家工具带来的效果下降

  - Agent自更新时需加配对验证机制，统计更新的「修复样本数」和「误杀原有正确样本数」，设置净增益阈值，避免总指标不动但大量正确结果被破坏的静默伤害

  - 工具库可跨模型迁移，用小参数模型跑进化生成的工具库，放到大模型上能拿到更高增益，大幅降低自进化的计算成本，适合业务大规模落地

  - 工具设计为仅输出数值证据不直接给结论，同时加scope范围匹配，非适用范围的请求直接走原有逻辑，避免工具滥用带来的负向效果'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前基于工具的时序Agent依赖人工预先配置工具库，存在两个核心痛点：一是**人-Agent工具错配**，21个专家整理的工具会导致异常检测任务准确率下降5.8~8.8个点，部分任务收益为负；二是**静默伤害**，一次通用自修订会修改147个答案，修复49个错误的同时破坏56个原本正确的答案，总指标波动不足1个点，问题被完全掩盖。
### 方法关键点
- 失败聚类分析：将Agent的运行错误按缺失能力聚类为失败桶，每个桶生成测量合约，明确所需证据类型、适用范围与反适用范围
- 证据型工具合成：每个合约最多尝试3次生成纯数值输出的工具（不直接输出结论），支持嵌入训练集校准的轻量决策树，预筛选要求至少可修复1个对应桶的错误
- 双验证准入机制：单工具筛选后，全工具库做配对验证，要求修复样本数大于误杀样本数，净增益为正且误杀率≤10%，不通过则剪枝有害工具后重测一次，仍不通过直接回滚
- 残差推理：仅对工具适用范围内的请求用证据辅助决策，其余请求直接走原有逻辑，避免非适用场景的负向影响
### 关键结果
在10个时序QA任务、3个LLM backbone上测试，对比专家工具库、Self-Refine、少样本ICL等baseline：
- TimeEvo是唯一在所有任务、所有backbone上都取得正向增益的方法，平均准确率提升7.21~8.79个点，异常检测任务最多提升16.25个点
- 用低成本小模型进化得到的工具库，迁移到更强的大模型上，平均准确率可再提升8.27~10.65个点，70%的任务增益超过原模型的进化收益
### 核心结论
Agent自身的运行失败，比人工预判更适合作为工具库的需求来源
