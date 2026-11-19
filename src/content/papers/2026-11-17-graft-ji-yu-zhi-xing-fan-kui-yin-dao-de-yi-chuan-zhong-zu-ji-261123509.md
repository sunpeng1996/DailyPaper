---
title: 'GRAFT: Execution-Guided Genetic Recombination for Agent Design'
title_zh: GRAFT：基于执行反馈引导的遗传重组Agent自动设计框架
authors:
- Sevda Ebrahimi
- Mohammed Saidul Islam
- Xiaodan Zhu
- Elham Dolatabadi
affiliations:
- York University
- Vector Institute
- Queen’s University
arxiv_id: '2611.23509'
url: https://arxiv.org/abs/2611.23509
pdf_url: https://arxiv.org/pdf/2611.23509
published: '2026-11-17'
collected: '2026-11-19'
category: Agent
direction: Agent架构自动搜索 · 进化算法
tags:
- AgentDesign
- EvolutionaryAlgorithm
- GeneticCrossover
- LLM
- AutomatedOptimization
one_liner: 将父Agent的执行成败样本引入遗传交叉算子，显著提升Agent架构自动搜索性能
practical_value: '- 业务Agent迭代时可复用历史请求的成功/失败样例作为优化反馈，无需额外标注或推理成本，即可让LLM快速定位到输出格式、参数解析等共性缺陷，大幅降低人工调优成本

  - 做Agent架构自动搜索时可复用现有成熟Agent作为初始种群，采用小种群（如5个）+每代少量后代（如2个）的进化策略，算力开销低，适合电商推荐、客服等场景快速迭代

  - 进化搜索过程中可缓存每个Agent的执行记录与fitness，做精英种群替换时直接复用缓存数据，无需重复执行验证任务，进一步降低工程落地的算力成本'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有基于进化算法的LLM Agent架构搜索仅依赖整体fitness分数引导交叉变异，无法感知分数背后的样本级成败原因，优化方向盲目，难以定位输出格式错误、参数传递错误等易修复的架构缺陷，导致搜索效率低、最终性能上限不足。
### 方法关键点
- 沿用轻量遗传算法框架：以人工设计的成熟Agent（如CoT、Self-Refine）作为初始种群，用整体fitness做父本选择和种群淘汰，固定每代生成2个后代，迭代15代左右，算力开销可控
- 新增执行反馈harness：复用验证阶段生成的每个Agent的成功/失败执行样本（各最多3/6条，不泄露参考答案），和父本代码、fitness一起输入交叉LLM，精准定位父本的具体缺陷
- 交叉变异一体化：LLM同时完成父本优秀机制融合与缺陷修复，生成的后代经过可执行性校验，避免无效代码
### 关键结果
在6个推理/编程基准上测试，采用Qwen3.5-35B同时作为优化器和执行器时，平均测试准确率达82.0%，较最强基线SwarmAgentic高9.8个百分点；在SuperGPQA-Hard-Calc任务上准确率96.5%，较次优基线高29.3个百分点；仅移除执行反馈的对照组在MGSM任务上准确率仅56.7%，加反馈后提升至91.6%，涨幅达34.9个百分点。
### 核心结论
Agent架构优化的反馈粒度越细，LLM输出的优化方案越精准，复用已有的执行日志做引导，无需额外标注即可获得大幅性能收益。
