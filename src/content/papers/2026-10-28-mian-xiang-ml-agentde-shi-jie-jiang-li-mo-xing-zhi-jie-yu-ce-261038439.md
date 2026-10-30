---
title: 'Predict the Reward, Not the World: World Reward Models for ML Agents'
title_zh: 面向ML Agent的世界奖励模型：直接预测奖励而非模拟执行
authors:
- Yuxiao Lee
- Zherui Yang
- Fan Liu
- Hao Liu
affiliations:
- The Hong Kong University of Science and Technology (Guangzhou)
arxiv_id: '2610.38439'
url: https://arxiv.org/abs/2610.38439
pdf_url: https://arxiv.org/pdf/2610.38439
published: '2026-10-28'
collected: '2026-10-30'
category: Agent
direction: ML Agent 执行效率优化 · 奖励模型
tags:
- Agent
- Reward Model
- World Model
- LLM4Agent
- Efficiency Optimization
one_liner: 提出直接预测候选程序胜率的世界奖励模型 使三类ML Agent提速4.4-7.5倍且性能持平或提升
practical_value: '- 做高成本试错类Agent（如推荐策略优化、广告投放策略生成Agent）时，可放弃模拟中间执行的思路，直接基于历史真实执行的优胜样本训练偏好判断模型，大幅降低推理成本和误差累积

  - 多候选对比的偏好任务可采用Typed Decision Model + LoRA的轻量化微调方案，仅用几千对标注样本就能获得远超通用LLM Judge的准确率，且输出概率校准度高，可直接用于阈值截断

  - Agent搜索流程中可引入「模型预筛+仅执行最优候选」的架构，用校准后的预筛模型置信度做门控，高置信样本直接淘汰劣势候选，低置信样本保留走真实执行，兼顾效率和准确率'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有基于搜索的ML Agent需要执行每一个生成的候选程序来获取反馈，单轮执行耗时可达数小时，90%以上的执行资源都浪费在被淘汰的候选上；而用LLM作为世界模型预测执行结果的方案准确率仅53%-62%，预测误差会误导搜索方向，反而降低最终性能。

### 方法关键点
- 提出World Reward Model（WRM）：跳过中间执行过程的模拟，直接输入任务上下文和候选程序，输出每个候选的真实执行胜率，无需生成任何中间推理文本
- 训练方案：基于历史真实执行的程序对优胜标注，用交叉熵损失微调9B参数的Typed Decision Model，仅更新LoRA adapter和指针头，训练数据仅需5k对标注样本
- 集成方案：WRM嵌入Agent搜索流程时，替代候选执行的评分环节，仅对最终选中的最优候选执行验证，高置信度对比直接淘汰劣势候选，低置信度对比可保留走真实执行

### 关键实验
测试集为12438对标注的ML程序对，对比基线包括DeepSeek-V3.2、GPT-5.1等通用LLM Judge，WRM的成对选择准确率达79.4%，比通用LLM高出17-26个百分点；嵌入AIDE、ML-Master、ForeAgent三类ML Agent后，平均任务耗时降低4.4-7.5倍，其中ForeAgent的平均性能反而从0.527提升到0.607，其余两类Agent性能下降不超过0.01。

### 最值得记住的一句话
对于只需要判断候选优劣的决策场景，模拟中间执行过程不会带来任何额外信息，反而会引入累积误差，直接基于真实执行结果训练端到端的偏好模型是更高效的方案。
