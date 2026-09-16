---
title: StepAudio 3 Music Technical Report
title_zh: StepAudio 3 音乐生成技术报告
authors:
- Chengli Feng
- Zhiyue Wu
- Jiahao Song
- Zheqi Dai
- Boyang Wang
- Ruibin Yuan
- Junming Gong
- Wenxiao Zhao
- Jing Guo
- Gang Yu
affiliations:
- StepFun
- ACE
- The Chinese University of Hong Kong
- University of California San Diego
arxiv_id: '2609.16034'
url: https://arxiv.org/abs/2609.16034
pdf_url: https://arxiv.org/pdf/2609.16034
published: '2026-09-10'
collected: '2026-09-16'
category: Other
direction: 可控长时长音乐生成 · 显式规划
tags:
- Music Generation
- DiT
- MoE
- DPO
- VAE
- Tokenizer
one_liner: 提出支持显式结构规划的长时长音乐生成模型，多项评测指标达行业领先水平
practical_value: '- 生成类任务引入中间规划CoT的思路可复用：比如电商短视频BGM、广告文案生成前先输出结构大纲，大幅提升生成内容的一致性与可控性

  - 单码本Tokenizer结合自监督+多任务训练的方案，可迁移至多模态生成任务的特征离散化步骤，降低后续生成模块的建模难度

  - 离散-连续混合生成架构+DPO偏好优化的组合，可用于提升生成式推荐的用户偏好匹配度，优化推荐物料的用户接受度

  - 渐进式训练课程设计可复用在长序列生成类任务（如长营销文案、长视频推荐物料生成）的训练流程，提升长序列生成质量'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
现有长时长音乐生成缺乏显式结构规划，韵律、和声一致性差，可控性不足难以适配商用需求。
### 方法关键点
1. 设计单码本65536条目的50Hz音频Tokenizer，通过自监督+多任务训练保留音乐结构与重建信息
2. 采用流匹配DiT预测VAE连续隐变量，经VAE解码器输出48kHz高保真音频
3. 引入MoE自回归模型生成ABC notation中间编排计划（ABC-CoT）作为生成前置，显式控制和声、节奏、旋律结构
4. 结合渐进式训练课程、SFT与DPO偏好优化，覆盖多类音乐生成场景
### 关键结果数字
支持最长5分30秒的歌曲/伴奏/翻唱生成，AudioBox三项核心评分、MuQ-MuLan相似度均为参评系统第一，音乐质量Elo得分1105，仅次于Suno V5.5、Mureka，领先Suno V5等主流模型
