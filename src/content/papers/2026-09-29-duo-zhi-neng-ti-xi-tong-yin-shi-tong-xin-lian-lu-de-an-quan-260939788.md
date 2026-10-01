---
title: Safety of Latent Communication in Multi-Agent Systems
title_zh: 多智能体系统隐式通信链路的安全风险与修复方法
authors:
- Muhammad Huzaifa
- Sina Mavali
- Thorsten Eisenhofer
affiliations:
- CISPA Helmholtz Center for Information Security
arxiv_id: '2609.39788'
url: https://arxiv.org/abs/2609.39788
pdf_url: https://arxiv.org/pdf/2609.39788
published: '2026-09-29'
collected: '2026-10-01'
category: MultiAgent
direction: 多智能体系统 · 隐式通信安全
tags:
- Multi-Agent
- Latent Communication
- Safety Alignment
- Communication Attack
- Link Repair
one_liner: 发现多智能体隐式通信链路的安全漏洞，提出无需更新智能体的攻击与修复方案
practical_value: '- 采用多Agent做电商推荐/客服协作时，若用隐式通信降本，不能默认单个Agent对齐就安全，必须对全链路做安全评测，避免无意中提升有害内容输出概率

  - 业务中使用隐式通信链路时，可借鉴文中奖励引导优化方法，仅更新链路参数即可修复安全问题，无需重新微调冻结大模型，大幅降低迭代成本

  - 链路训练时可加入少量安全对齐负样本，或在生成开头强制注入拒绝前缀，能大幅降低有害合规率，同时基本不影响良性任务性能

  - 多Agent拓扑设计时，重点加固最后一级输入的通信链路，该链路被攻击的危害最大，是安全防护的核心靶点'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
LLM多智能体系统采用隐式通信替代文本交互，可降低30%+的token消耗与推理延迟，但现有研究仅关注效率提升，未考虑通信链路训练带来的安全风险：即使底层Agent已完成安全对齐，链路对隐层表示的变换也可能绕过安全防护，带来严重的合规风险。

### 方法关键点
- 三类攻击方案：① 用有害查询-响应对监督优化通信链路；② 向良性训练数据注入10%有害样本实现数据投毒；③ 基于GRPO的奖励引导攻击，无需有害目标回复，仅通过回复级反馈同时优化有害合规性与良性任务性能
- 修复方案：基于GRPO优化链路参数，对有害查询惩罚合规回复、奖励明确拒绝，对良性查询奖励正确回复，全程不更新底层Agent参数

### 关键实验
在2Agent、Sequential、Mixture三类通信拓扑上验证，安全评测采用HarmBench、StrongREJECT等4个基准，良性任务采用MATH500、GPQA-Diamond：
1. 即使是良性训练的隐式链路，平均有害合规率也比文本通信高8.3~28.5个百分点
2. 奖励引导攻击可将平均有害合规率从27.9提升至76.9，同时MATH500准确率从67.2%提升至71.0%，保留良性性能的同时实现高危害
3. 修复方案可将所有攻击场景下的平均有害合规率从70.3降至4.8，低于原始干净链路的安全水平，良性任务准确率基本与原干净链路持平

### 核心结论
安全对齐不能仅验证单个Agent的性能，必须将多智能体系统包括通信链路作为一个整体进行评测与优化
