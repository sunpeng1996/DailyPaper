---
title: 'Marimba: A System One Model for Speech'
title_zh: Marimba：面向语音场景的一体化决策模型
authors:
- Solano Amadori
affiliations:
- charcot.ai
arxiv_id: '2611.18330'
url: https://arxiv.org/abs/2611.18330
pdf_url: https://arxiv.org/pdf/2611.18330
published: '2026-11-13'
collected: '2026-11-16'
category: Other
direction: 语音多任务统一决策 · 大模型特征复用
tags:
- ASR
- Multi-task Learning
- Frozen LLM
- Speech Processing
- Feature Reuse
one_liner: 基于冻结Qwen3-ASR 0.6B特征构建多场景语音决策统一接口，性能优于多个主流基线
practical_value: '- 电商语音导购、智能客服类Agent开发可参考该框架思路：复用冻结ASR大模型不同层特征做下游多任务，无需全量微调，大幅降低训练和部署成本

  - 多目标优化场景可迁移其统一接口设计：同一个基座特征上挂载不同任务头，同时支持语音搜索query敏感词检测、轮次结束判断、语种识别多类需求

  - 词相关/非词相关任务分流处理的trick可复用：词级任务直接用ASR转录做零样本打分，非词级任务用特定层读出头，兼顾精度和效率'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
语音应用需在同一段音频窗口完成术语存在判断、轮次结束检测、语种识别等多类决策，现有单任务工具接口不统一，直接取ASR 1-best转录会丢失识别不确定性，多prompt生成模式成本高、输出概率未校准。
### 方法关键点
基于冻结的Qwen3-ASR 0.6B特征构建统一决策接口：lexical类任务直接对ASR转录做零样本打分；非lexical类任务用问题条件头+第18层专属轮次结束读出头；语种识别直接复用ASR自身的语言得分，不同任务从基座不同层提取特征做预测。
### 关键结果数字
- 私有对话测试集decoder AUROC 0.80-0.92，公开朗读语音AUROC 0.92-0.97
- 语音命令四分类准确率0.93，PII检测合成巴西葡语语音F1达0.904
- 说话人转换检测AUROC 0.966-0.980，优于ECAPA基线，说话人计数准确率高于pyannote 3.1
