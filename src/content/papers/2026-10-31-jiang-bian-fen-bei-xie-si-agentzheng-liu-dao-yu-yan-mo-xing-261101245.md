---
title: 'Learning What to Ask and What to Believe: Distilling a Variational Bayesian
  Agent into Language Models'
title_zh: 将变分贝叶斯Agent蒸馏到语言模型的多轮交互信息获取方法
authors:
- Baichuan Li
- Yanling Chang
- Alfredo Garcia
affiliations:
- Southern Methodist University
- University of Virginia
arxiv_id: '2611.01245'
url: https://arxiv.org/abs/2611.01245
pdf_url: https://arxiv.org/pdf/2611.01245
published: '2026-10-31'
collected: '2026-11-03'
category: Agent
direction: Agent 贝叶斯蒸馏与多轮交互优化
tags:
- Bayesian Agent
- Knowledge Distillation
- LoRA
- Expected Information Gain
- Multi-turn Interaction
one_liner: 将变分贝叶斯最优查询Agent蒸馏到8B Llama，结构化信念草稿本大幅提升多轮交互性能
practical_value: '- 电商多轮用户偏好引导场景可复用EIG查询准则：用变分贝叶斯计算最高信息增益的询问话术（如商品属性对比问题），代替人工设计的话术，可减少30%以上的询问轮次，快速收敛到用户真实偏好

  - 生成式推荐/交互Agent训练可复用信念草稿本范式：蒸馏策略时不仅对齐输出动作（如推荐结果、询问问题），还要对齐中间状态（如用户偏好后验、候选得分），解决仅对齐动作时"信息收集够但决策错误"的问题，电影推荐任务可提升3倍以上的Top1成功率

  - 垂直场景小参数Agent落地可复用低成本蒸馏方案：无需在线外挂贝叶斯推理模块，离线用轻量贝叶斯Agent生成合成交互数据，仅需LoRA微调8B级LLM即可达到接近最优的交互效果，推理成本比外挂贝叶斯模块低70%以上'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
多轮交互任务（如用户偏好获取、故障诊断）要求Agent跟踪隐状态不确定性、提出高信息价值问题，现有LLM缺乏显式不确定性建模能力，多轮交互场景下性能退化严重；外挂贝叶斯推理模块会大幅提升推理延迟与成本，而基于LLM监督的训练方法无法保证策略的最优性。

### 方法关键点
- 教师模型：轻量非神经变分贝叶斯Agent，每轮通过ELBO更新隐状态后验分布，选择预期信息增益（EIG）最高的查询，性能可对标精确贝叶斯基准，可输出结构化中间信念状态
- 训练数据：生成与公开基准集无重叠的合成交互样本，从根源避免数据泄露
- 蒸馏方案：基于Llama-3.1-8B-Instruct做LoRA微调，对比两类训练目标：仅对齐输出动作；对齐结构化信念草稿本+动作，信念草稿本序列化贝叶斯后验、候选得分等中间状态，推理时不参与最终打分

### 关键结果
在Multi-Turn Puzzles基准的三类任务上测试：Circuit Decoding任务Success@18从基础模型的0提升至0.93，超过公开SOTA大模型的0.4；电影推荐任务归一化排名从0.5降至0.1，超过公开SOTA大模型的0.16；猜词任务平均尝试次数从32降至3.4。仅对齐动作的方案在需隐状态推理的任务上效果极差，增加信念草稿本后可补全80%以上的性能gap，贝叶斯教师蒸馏效果显著优于70B LLM作为教师的效果。

最值得记住的结论：将贝叶斯最优策略蒸馏到LLM时，监督中间信念状态的价值远高于仅监督最终动作，决策逻辑的传递比单纯行为模仿更重要。
