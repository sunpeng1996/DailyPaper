---
title: 'Failure-Transparent Agents: Benchmarking Post-Failure Reporting in Tool-Using
  Language Models'
title_zh: 故障透明Agent：工具调用大模型故障后报告能力评测基准
authors:
- Junru Zhu
- Shiming Xie
- Aime Lu Fan Chen
- Xiaoqing Ding
- Chunxin Tang
- Ruoyu Qi
- Yulang Fei
affiliations:
- Independent Researcher
- Ant Group
- Tsinghua University
- University of Chicago
- University of Waterloo
arxiv_id: '2609.35732'
url: https://arxiv.org/abs/2609.35732
pdf_url: https://arxiv.org/pdf/2609.35732
published: '2026-09-28'
collected: '2026-09-30'
category: Agent
direction: Agent 工具调用故障透明性评测
tags:
- LLM Agent
- Tool Use
- Benchmark
- Failure Transparency
- Hallucination
one_liner: 提出隔离工具执行故障的可控基准FTA，验证结构化证据契约可大幅降低虚假报告率
practical_value: '- 电商导购/客服Agent工具调用（库存/物流/优惠券查询等）失败后，可强制输出STATUS/EVIDENCE/LIMITATION/NEXT
  ACTION四字段结构化结果，可将虚假报告率从22.8%降至0.8%，同时有用响应率提升至98.8%，避免错误信息引发客诉

  - 若暂不改动输出结构，可在系统提示词中添加通用透明度指令，仅需少量改动即可将虚假成功率降至9.3%，有用响应率提升至89.2%，投入产出比高

  - 内部做Agent可靠性评估时，可参考FTA的隔离评测思路，固定故障输入单独验证报告准确性，避免和工具选择、重试逻辑等其他环节的问题混淆，快速定位故障根因'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
现有Agent基准多混合工具选择、故障恢复、环境动态等干扰因素，无法单独隔离评测工具执行失败后Agent输出的真实性；而电商客服、导购等落地场景中，Agent工具调用失败后谎报成功（如查不到库存谎称有货、物流接口超时谎称已发货）会直接引发客诉和资损，亟需可控的专项评测基准。
### 方法关键点
- 设计固定故障后证据状态的评测框架：每个任务仅向模型输入用户请求+确定的工具失败trace，评测侧留存合法完成所需证据、可行恢复方案、可提供的部分帮助信息，直接审计输出与观测证据的一致性
- 构造100个合成任务，覆盖检索不可用、附件缺失、执行失败、权限拒绝、数据过期5类常见故障，同时包含中性、预期答案、紧急、强制选择、要求隐瞒故障5类用户压力场景
- 定义虚假成功、捏造细节两类违规指标，同时加入限制披露、可行恢复、有用响应、过度拒绝等辅助指标，避免将一律无响应误判为高可靠性表现
- 采用元数据盲评的人工标注规则，标注者看不到模型身份、响应策略等信息，仅按固定规则打分
### 关键实验
覆盖6款主流大模型，对比3种响应策略，共产出3600条人工标注样本：基线策略虚假成功率22.8%、捏造细节率28.3%、有用响应率74.9%；添加通用透明度指令后三个指标分别为9.3%、14.3%、89.2%；采用结构化证据契约策略后三个指标分别为0.8%、0.8%、98.8%，效果跨模型稳定一致。
### 核心结论
工具故障和故障后报告是Agent两类独立的可靠性维度，可靠的Agent不仅要能完成任务，还要保证向用户传递的所有声明都与实际获取的证据完全一致。
