---
title: Evidence-Based Credit Assignment for Search-Augmented Language Models
title_zh: 面向搜索增强大模型的基于证据的信用分配机制
authors:
- Wen Wang
- Jindong Wang
- Jiahua Bao
- Tu Yongsiqi
- Yihao Liu
- Junwei He
- Wenkui Fan
affiliations:
- University of the Chinese Academy of Sciences
- Tencent
- Harbin Institute of Technology
- Renmin University of China
- Peking University
arxiv_id: '2611.23824'
url: https://arxiv.org/abs/2611.23824
pdf_url: https://arxiv.org/pdf/2611.23824
published: '2026-11-17'
collected: '2026-11-19'
category: Agent
direction: Agent 搜索增强LLM信用分配优化
tags:
- Search-Augmented-LLM
- Credit-Assignment
- GRPO
- Reinforcement-Learning
- RAG
- Agent-Training
one_liner: 提出基于证据的信用分配ECA框架，无需外部标注即可优化搜索增强LLM的RL训练效果
practical_value: '- 电商搜索/导购Agent的RL训练可复用ECA的证据-only奖励思路，仅用用户Query+召回的商品/内容计算辅助奖励，排除中间思考、Query措辞的干扰，无需额外标注即可提升搜索动作的信用分配精度

  - 多轮召回场景的全失败轨迹（如多轮搜索均未命中用户需求）可复用cross-fold归一化+新奇度门控方案，给召回了有效信息的动作分配正向梯度，避免全失败组梯度消失，同时抑制冗余重复召回

  - 多步信用分配优先选用ECA-Horizon方案，通过终态证据势能与步前势能的差值计算回报，增益随模型容量提升更显著，3B/7B规模下相对GRPO基线EM分别涨1.03pp/4.80pp'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前搜索增强LLM基于终端结果奖励的RL训练存在严重信用分配偏差：所有搜索动作共享同一个轨迹级奖励，召回有效证据的搜索可能因最终回答错误被惩罚，冗余搜索也可能因最终答对被奖励；尤其当同一问题的所有采样轨迹都回答错误时，组归一化后的优势会全部归零，即使部分轨迹已经召回了关键证据，也无法提供有效梯度信号。
### 方法关键点
- 训练阶段引入仅用于计算辅助信号的证据势能：用当前策略的冻结合副本，仅基于问题+去重后的召回文档计算参考答案的长度归一化对数似然，完全排除中间思考、搜索Query措辞的干扰，推理阶段无额外开销
- 设计两种回报计算范式：ECA-Step对每步势能增量做clip后累加，ECA-Horizon直接用终态势能减去当前步前势能的telescoping差值，保留完整多步证据增益
- 配套cross-fold归一化（每个轨迹用另一半组的统计量做归一化，避免自身高增益拉高基线导致信号抵消）、新奇度门控（召回重复文档的搜索无法获得正向辅助奖励），辅助奖励仅施加到对应搜索的思考+Query token，最终回答token仍只用终端结果奖励
### 关键结果
在7个搜索QA数据集共5.17万测试样本上，对比GRPO、RLOO、GiGPO等主流基线，ECA-Horizon在Qwen2.5-3B上相对GRPO提升macro EM 1.03pp，7B上提升4.80pp；零样本迁移到MultiHop-RAG数据集上7B模型EM达89.22%，比GRPO高6.38pp，同时可降低3B模型重复搜索率17.6pp。
> 最值得记住的结论：搜索动作的信用分配只应和召回的有效证据挂钩，与中间思考的措辞、Query的表述无关
