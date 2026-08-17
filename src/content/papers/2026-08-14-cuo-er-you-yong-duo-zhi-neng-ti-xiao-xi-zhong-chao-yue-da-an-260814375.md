---
title: 'Wrong but Useful: Trajectory Value Beyond Answer Correctness in Multi-Agent
  Messages'
title_zh: 错而有用：多智能体消息中超越答案正确性的轨迹价值
authors:
- Chih-Hsuan Yang
- Anjir Ahmed Chowdhury
- Cheng-Hau Yang
- Weijian Zheng
- Fernando Llorente
- Xiaolong Ma
- Xinyang Li
- Eliu A. Huerta
- Ian T. Foster
- Rajeev Thakur
affiliations:
- Argonne National Laboratory
- University of Houston
- Brookhaven National Laboratory
- University of Chicago
arxiv_id: '2608.14375'
url: https://arxiv.org/abs/2608.14375
pdf_url: https://arxiv.org/pdf/2608.14375
published: '2026-08-14'
collected: '2026-08-17'
category: MultiAgent
direction: 多智能体协作 · 消息价值评估
tags:
- MultiAgent
- TrajectoryValue
- DHDProtocol
- MessageSelection
- Reasoning
- LLM
one_liner: 提出DHD测量协议，证明答案错误的多智能体消息仍可为下游推理提供有效价值
practical_value: '- 多智能体导购/营销内容生成场景中，不要直接过滤答案错误的Agent输出，可提取其推理过程中的用户需求拆解、场景约束、品类规则等复用，减少有效信息浪费

  - 借鉴DHD留一法重放机制，离线评估不同Agent角色、不同输入信息对最终推荐/投放效果的边际贡献，仅控制消息可见性即可完成归因，无需重构上游生成逻辑

  - 构建多Agent消息过滤/排序模型时，除答案置信度特征外，新增推理内容与当前用户需求、业务约束的语义匹配特征，可提升消息筛选的准确性

  - 多Agent生成候选推荐方案的场景下，可先缓存所有候选消息，通过少量重放测试识别高价值消息，即使其最终答案错误，也可用于下游方案融合'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
当前多智能体推理系统普遍基于答案正确性、置信度、共识度过滤消息，默认输出错误答案的消息无价值，但实际错误答案可能附带有用的问题拆解、约束条件、领域规则，现有筛选逻辑会浪费这部分价值，也无法准确评估单条消息对下游推理的真实贡献。

### 方法关键点
- 设计DHD（Diverse Hypothesis Deliberation）测量协议：为每个问题动态分配5个互补角色，各角色独立生成包含推理过程和答案的结构化消息并缓存，全程不做预过滤
- 采用留一法（LOO）重放对比：固定其他消息不变，仅控制单条目标消息是否对下游整合器可见，对比两次结果的正确性差异，定义为该消息的**trajectory value**
- 配套组件掩码测试：分别隐藏消息的推理部分和答案部分，定位价值来源

### 关键结果
实验覆盖Omni-MATH-2、JEEBench等5个数学/科学推理基准，测试gpt-oss-120b和gemma-4-31B-it两个开源大模型：
1. 所有基准+模型组合中均存在错而有用的消息，错误答案的消息触发最终结果翻转时，41.9%（OSS）、45.3%（Gemma）的翻转是正向提升
2. 控制重放随机性后，该效应统计显著（p=0.0002）
3. 错误有用消息的价值主要来自推理过程：保留推理的成功率为64%，仅保留答案的成功率为44%
4. 基于trajectory value的消息选择比仅基于答案正确性的选择多带来1.68pp（OSS）~2.61pp（Gemma）的准确率提升

### 核心结论
答案正确性是消息有用性的有效参考，但绝非决定因素，错误答案附带的推理过程往往能带来超出预期的价值
