---
title: 'SIT-Eval: Situation-Based Interactive Turn-by-Turn Evaluation of Conversational
  Agents'
title_zh: SIT-Eval：面向会话Agent的基于场景的逐轮交互式评估框架
authors:
- Ravil Mussabayev
- Saveliy Zavertyaev
- Dmitriy Parpulov
- Andrey Savchenko
affiliations:
- Satbayev University
- Sber AI Lab
arxiv_id: '2610.23612'
url: https://arxiv.org/abs/2610.23612
pdf_url: https://arxiv.org/pdf/2610.23612
published: '2026-10-16'
collected: '2026-10-19'
category: Eval
direction: 会话Agent评估 · LLM-as-Judge
tags:
- LLM-as-Judge
- Conversational-Agent
- Evaluation-Framework
- Situation-Aware
- Multi-turn-Dialogue
one_liner: 通过均匀采样场景+预定义规则+校验后LLM Judge实现会话Agent细粒度鲁棒评估
practical_value: '- 评估电商客服/导购会话Agent时，可复用「规则拆解+Golden对话校准LLM Judge」的流程：先把业务要求拆成可观测原子规则（如不得主动提竞品、售后先致歉再引导），再用少量人工标注的Golden对话校准Judge，评估效率远高于纯人工评估

  - 做Agent抗压测试时，可采用均匀采样触发场景的方案，给低概率高风险边缘场景（如用户恶意投诉、索要大额赔偿）分配同等采样权重，避免上线后小概率事件演变为大规模故障

  - 编写Agent系统提示词时，将抽象行为要求拆解为明确的条件规则写入，实验证明可平均提升7%的规则符合率，适用于导购、内容推荐等各类会话Agent'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有会话Agent评估依赖静态自然对话，天然存在分布偏置，低概率风险场景样本极少，但生产环境百万级流量会让这类小概率故障高频发生；同时现有评估多为对话整体打分，会掩盖逐轮行为违规问题，且通用LLM Judge普遍缺乏校准，评估结果可靠性不足。

### 方法关键点
- 把Agent预期行为定义为「若触发场景P，则必须满足规则Q」的可观测原子规则，所有规则均可仅通过对话上下文判断合规性
- 用LLM交互者均匀采样预定义的场景动作，确保常见和罕见场景获得同等统计权重，最大化边缘场景覆盖度
- 先在人工校验的Golden对话集上验证LLM Judge的准确率，达标后才用于实际评估，输出逐轮规则合规性结果而非模糊的整体得分

### 关键实验
在数学家教场景下构建12条专家定义的教学规则，基于GSM8K数据集生成500条Golden对话，3名专家标注的噪声率仅0.85%；LLM Judge整体准确率达84.4%，比随机基线高34.4个百分点；对8款主流LLM的1292轮对话评测发现，整体得分相近的模型在单条规则的符合率上差异极大，所有模型在歧义澄清、苏格拉底提问两类规则上表现最差，平均符合率仅11%。

### 值得记住的一句话
把抽象的行为要求拆解为可观测的原子规则，并用均匀采样覆盖边缘场景，是解决会话Agent生产环境风险的核心评估思路。
