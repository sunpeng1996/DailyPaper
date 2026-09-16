---
title: 'Context-Aware Emotionally Adaptive Voice Assistants: A Multimodal Framework
  for Empathetic Human-Agent Interaction'
title_zh: 上下文感知情绪自适应语音助手：共情人机交互多模态框架
authors:
- Tapon Kumer Ray
- Rajkumar Yesuraj
affiliations:
- Vellore Institute of Technology, Amaravati, India
arxiv_id: '2609.16417'
url: https://arxiv.org/abs/2609.16417
pdf_url: https://arxiv.org/pdf/2609.16417
published: '2026-09-14'
collected: '2026-09-16'
category: Agent
direction: 语音Agent 多模态情绪感知交互优化
tags:
- Voice Agent
- Multimodal Fusion
- Reinforcement Learning
- Emotion Recognition
- Human-Agent Interaction
one_liner: 提出融合多模态情绪识别与Double DQN中断策略的EmpathicVA框架，降低语音助手主动打断的侵入性
practical_value: '- 电商语音导购/客服Agent可复用「情绪概率+上下文+交互历史」的状态设计，将用户情绪软标签而非硬分类结果输入交互策略，针对烦躁/压力状态用户先做情绪共情再传递商品信息，或延迟非紧急营销通知的推送时机，降低用户反感

  - 多模态用户建模可借鉴分层融合设计：先做单模态时序编码（生理信号用Conv1D+LSTM、语音用Conv2D+BiLSTM），再用交叉注意力动态加权各模态贡献，该方案比直接融合性能提升6个百分点以上

  - 推送/触达类RL策略可复用奖励拆分逻辑：按4:3:2:1加权满意度、时机质量、共情匹配度，同时增加侵入性惩罚项，动作集拆分响应时机+响应类型两个维度，既保证核心服务可用性，又避免过度打扰

  - 交互类系统评估不要仅看模型分类准确率，需结合业务体验指标（满意度、信任度）、行为指标（交互放弃率、会话时长）、生理指标（压力反应）交叉验证，更贴近真实用户体验'
score: 8
source: arxiv-cs.HC
depth: full_pdf
---

### 动机
现有语音助手的主动交互/打断完全不考虑用户情绪、认知负荷和场景上下文，侵入性极强，容易导致用户反感、信任度下降；过往研究分别探索了主动时机优化、多模态情绪识别、RL对话策略，但三者未打通，无法同时兼顾响应效率和用户情绪体验。

### 方法关键点
- 闭环感知-决策-行动架构，分为多模态情绪识别模块、Double DQN决策模块、响应执行层三层，可直接对接现有语音助手后端，无需重训LLM
- 多模态情绪识别：融合生理特征（HRV、EDA、呼吸）、语音特征（MFCC、基频、BERT embedding）、12维上下文特征（时间、位置、应用活跃状态、会议密度等），先做单模态独立编码，再通过8头交叉注意力加权融合，输出5类情绪的概率分布
- RL策略设计：状态输入为情绪概率向量+上下文特征+最近10次交互反馈，动作集包含立即响应、短延迟、长延迟、共情响应、静默5类，奖励按40%满意度+30%时机质量+20%共情匹配-10%侵入性惩罚加权计算

### 关键结果
多模态情绪识别在包含48名用户的测试集上准确率达92.3%，macro F1 0.922，比最优单模态模型高6.0个百分点；6周被试内田野实验显示，对比基线语音助手，EmpathicVA的用户满意度从3.24提升到4.51，打断相关压力事件减少86.5%，SUS可用性得分从68.4提升到82.7，所有指标提升均在p<0.001水平显著。

### 核心结论
共情交互不仅要调整回复话术，更要管控响应时机，甚至在用户高压力状态下选择不打断，体验远好于强行输出共情话术。
