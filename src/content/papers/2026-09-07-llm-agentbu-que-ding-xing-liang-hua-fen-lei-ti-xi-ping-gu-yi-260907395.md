---
title: 'Uncertainty Quantification for LLM Agents: A Taxonomy, an Evaluation Protocol,
  and an Empirical Study'
title_zh: LLM Agent不确定性量化：分类体系、评估协议与实证研究
authors:
- Moule Lin
- Qizhen Lan
- Shuhao Guan
- Weipeng Jing
- Jiexin Fan
- David Gregg
- Goetz Botterweck
affiliations:
- Trinity College Dublin
- University of Texas Health Science Center at Houston
- University College Dublin
- Northeast Forestry University
arxiv_id: '2609.07395'
url: https://arxiv.org/abs/2609.07395
pdf_url: https://arxiv.org/pdf/2609.07395
published: '2026-09-07'
collected: '2026-09-09'
category: Agent
direction: LLM Agent · 不确定性量化
tags:
- Uncertainty_Quantification
- LLM_Agent
- Calibration
- Trajectory_Evaluation
- Tool_Use
- Hallucination_Detection
one_liner: 覆盖LLM Agent全流程的不确定性三轴向分类体系、轨迹级校准度量TC-ECE与评估框架
practical_value: '- 电商导购/客服Agent场景下，不要仅依赖单步置信度做容错判断，多轮查品、调用库存/物流工具的场景需按轨迹阶段拆分校准，避免早期错误传播导致的整体置信度误判

  - TC-ECE度量可直接复用到业务Agent评测流程，分checkpoint统计校准误差，能发现长对话后期的过置信问题，比传统单步ECE更贴合多轮交互场景

  - 5类不确定性来源框架（随机/认知/工具/累积/多智体）可直接套用到业务Agent异常归因，快速定位是prompt问题、工具接口不稳还是多步推理误差累积

  - 3步以内的短路径Agent（查券、查物流）可直接用步置信度乘积近似估计可靠性，长路径复杂任务（定制化多轮导购）必须加误差相关性建模，不能直接相乘步置信度'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有LLM不确定性量化方法几乎都针对单轮QA场景，但Agent多轮交互、调用工具、长轨迹执行的模式下，错误会跨步骤累积传播，单步校准结果无法代表整体轨迹可靠性，同时领域缺乏统一的分类体系和适配Agent特性的评估方法，无法支撑Agent的安全落地。

### 方法关键点
- 三轴向分类体系：按不确定性来源（随机/认知/工具/累积/多智体5类）、估计方法（口头置信/采样一致性/Token概率/共形预测等8类）、管道阶段（规划/工具调用/检索/记忆/多步推理/多智体6类）划分，覆盖120篇相关领域论文
- 形式化证明单步校准无法推导轨迹级校准，误差由步间错误相关性决定，给出边际乘积近似的误差上界
- 轨迹-检查点预期校准误差TC-ECE，针对不同轨迹长度的checkpoint单独统计校准误差，避免数据pooling隐藏轨迹后期的过置信问题

### 关键结果
在4种模型、3类任务、最长50步的真实Agent轨迹上测试：Agent自报告的置信度表现没有稳定超过简单的步索引基线；pooling所有checkpoint的统计结果会掩盖轨迹后期的过置信问题，分阶段统计才会显现；工具调用/规划阶段的误差相关性远高于单轮推理，步置信度乘积会低估真实轨迹可靠性15%以上。

### 核心结论
不要用单步置信度的乘积直接作为长轨迹Agent的可靠性估计，不确定性会跨步骤累积传播，必须针对轨迹全流程做分阶段校准。
