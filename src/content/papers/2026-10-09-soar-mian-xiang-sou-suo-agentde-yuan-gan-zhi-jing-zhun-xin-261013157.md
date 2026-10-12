---
title: 'SOAR: Source-Aware Reinforcement Learning with Precise Credit Assignment for
  Search Agents'
title_zh: SOAR：面向搜索Agent的源感知精准信用分配强化学习框架
authors:
- Shengze Huang
- Zihao Tang
- Jinluan Yang
- Xin Yu
- Zhenghao Lin
- Xiao Liu
- Zengxuan Wen
- Yeyun Gong
- Haizhen Huang
- Weiwei Deng
affiliations:
- Zhejiang University
- Microsoft
arxiv_id: '2610.13157'
url: https://arxiv.org/abs/2610.13157
pdf_url: https://arxiv.org/pdf/2610.13157
published: '2026-10-09'
collected: '2026-10-12'
category: Agent
direction: 搜索Agent 源感知强化学习优化
tags:
- Search Agent
- Reinforcement Learning
- Hallucination Mitigation
- Credit Assignment
- GRPO
one_liner: 将搜索Agent推理拆为显式内外知识流，结合源一致性奖励大幅降幻觉提性能
practical_value: '- 搜索Agent训练可复用「内外知识显式拆分」工作流：将LLM内部知识作为独立可观测流与外部检索结果并行输入，解决RL信用分配模糊问题，适合电商导购Agent、商品问答Agent训练

  - 奖励设计可复用源一致性约束：在传统答案正确性、格式奖励之外，新增「输出与声明信息源对齐」的轻量规则奖励，无需额外大模型判分即可大幅降幻觉，适合业务端低 overhead
  优化

  - 多跳检索场景优化思路：对于电商多属性商品查询、复杂售后问题等需多步检索的场景，该框架可引导Agent主动触发补充检索，减少依赖内部过时商品知识导致的错误回复'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有基于RL的搜索Agent普遍存在证据捏造问题：推理不依赖检索到的外部信息，而是靠内部知识捷径输出错误结果。传统RL框架的整体推理轨迹不区分信息源，导致奖励无法区分正确结果来自可信检索还是内部幻觉，信用分配失效，知识密集型多步推理场景下幻觉率最高可达16%，严重影响Agent可靠性。
### 方法关键点
- 源感知工作流：将内部知识（Eint）和外部检索信息（Eext）拆为两个并行可观测流，内部知识通过上下文隔离的显式触发获得，避免和当前推理上下文混淆，信息来源完全可追溯
- 源一致性多维度奖励：在答案正确性、格式合规奖励之外，新增源一致性匹配奖励，惩罚输出与声明信息源不一致的行为，实现精准信用分配
- 基于GRPO完成RL训练，源一致性校验仅用规则匹配实现，无需额外大模型判分，开销可控
### 关键结果
在NQ、HotpotQA等7个单/多跳QA基准上测试，对比Search-R1、AutoRefine等SOTA搜索Agent：3B backbone平均EM提升7.3%，7B backbone平均EM提升5.4%，证据捏造率相对降低74.8%，仅比基线增加5.5%的token开销；抗检索噪声能力显著优于基线，噪声训练下幻觉率仅上升0.33%，远低于基线的2%以上。

最值得记住的一句话：搜索Agent的幻觉问题大概率不是模型容量不足，而是RL训练的信用分配模糊导致的，通过显式信息源拆分即可极低代价大幅缓解。
