---
title: Are Dense Rewards Worth Their Tokens in GRPO?
title_zh: GRPO训练中密集奖励是否值得其消耗的Token成本
authors:
- Vikash Singh
- Weicong Chen
- Debargha Ganguly
- Yanyan Zhang
- Mohsen Hariri
- Sreehari Sankar
- Wang Yang
- Chaoda Song
- Alexander Nemecek
- Osama Zafar
affiliations:
- Case Western Reserve University
arxiv_id: '2611.13560'
url: https://arxiv.org/abs/2611.13560
pdf_url: https://arxiv.org/pdf/2611.13560
published: '2026-11-09'
collected: '2026-11-11'
category: Training
direction: 大模型RL训练 · GRPO效率优化
tags:
- GRPO
- RLVR
- Dense Reward
- Training Efficiency
- Prompt Selection
one_liner: 提出匹配算力的RL训练评估协议，证明GRPO下密集奖励性价比远低于基线与prompt选择策略
practical_value: '- 做GRPO训练（如电商Agent推理、推荐文案生成微调）时不要盲目上密集/过程奖励：先核算生成token与GPU时间成本，同等算力下普通GRPO效果大概率更好，省出的算力可用于扩充训练数据或调优学习率

  - 训练样本筛选可低成本提效：优先选择模型预测成功率接近50%的样本训练，无需额外生成token，小模型上可提1~2个点准确率，适合低算力预算场景

  - 梯度测试仅可做排名参考不能作为上线依据：不要因梯度对齐度高就直接上线新奖励机制，必须做等算力AB测试，避免踩成本高估的坑

  - RL训练前先固定奖励验证规则：比如电商场景下转化、点击率的判定标准要严格，避免训练漂移浪费算力'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
GRPO是当前大语言模型推理RL训练（RLVR）的主流算法，现有研究普遍认为密集过程奖励能通过对中间步骤赋值提升训练效果，但传统评估仅对比相同更新步数下的效果，完全忽略了密集奖励采样中间续写带来的巨额token与算力成本，导致大量方法的实际收益被严重高估。

### 方法关键点
- 设计匹配算力的评估协议：所有对比方法分配等额的生成token预算（含续写、丢弃样本的所有消耗）与GPU训练时长，排除成本差异对结果的干扰
- 对比两类训练干预：4种密集奖励变种（蒙特卡洛续写奖励、在线拟合critic奖励等）、prompt选择策略（筛选模型预测成功率接近1/2的prompt训练，避免全对/全错的无梯度批次）
- 实验严格控制：覆盖6款Qwen、Llama小模型，累计1668次运行，所有研究提前预注册，控制随机种子、验证规则、基线调优的干扰

### 关键结果
- 同等token预算下，蒙特卡洛密集奖励准确率比普通GRPO低14.3pp，同等GPU时间下低7.8pp，4种密集奖励变种均无法超过普通GRPO
- 梯度测试仅能对奖励效果排序，但会高估实际增益1~2pp，与实测的有效增益幅度相当，无法作为上线依据
- 筛选近50%成功率的prompt训练，同等token下Qwen3-0.6B准确率提升1.7pp，Qwen2.5-1.5B提升0.8pp，收益可复现到未见过的测试集，仅需将基线学习率翻倍即可达到相近效果

### 最值得记住的一句话
任何训练干预的效果宣称都必须标注token、GPU算力预算、验证规则、基线调优方式，脱离成本谈收益毫无意义
