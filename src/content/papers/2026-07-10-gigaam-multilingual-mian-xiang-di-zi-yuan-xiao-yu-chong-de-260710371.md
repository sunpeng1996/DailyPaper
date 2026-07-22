---
title: 'GigaAM Multilingual: Foundation Model for Underrepresented Languages'
title_zh: GigaAM Multilingual：面向低资源小语种的多语种ASR基础模型
authors:
- Andrei Kuzmenko
- Alexandr Maximenko
- Aleksandr Kutsakov
- Georgii Gospodinov
- Dmitrii Bolotov
- Oleg Kutuzov
- Pavel Bogomolov
- Fyodor Minkin
affiliations:
- SaluteDevices, Russia
arxiv_id: '2607.10371'
url: https://arxiv.org/abs/2607.10371
pdf_url: https://arxiv.org/pdf/2607.10371
published: '2026-07-10'
collected: '2026-07-22'
category: Other
direction: 低资源多语种ASR 数据平衡预训练策略
tags:
- Multilingual ASR
- Low-resource Language
- Conformer
- Self-supervised Learning
- Data Balancing
one_liner: 提出融合集群级数据平衡、领域感知采样的低资源多语种ASR基础模型，性能优于Whisper Large v3等基线
practical_value: '- 跨境电商多语种语音搜索、语音客服场景可复用集群级数据平衡+领域感知采样的预训练微调策略，缓解高资源语种主导问题，提升小语种ASR效果

  - 需适配低资源小语种语音输入的跨境业务，可直接采用开源的GigaAM Multilingual作为ASR底座，降低自研成本

  - 多模态推荐/Agent涉及低资源语种语音输入的场景，可参考其数据不平衡下的预训练调优思路，避免长尾场景效果过差'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
当前多语种ASR效果在不同语种上分布极不均衡，长尾低资源语种面临严重数据稀缺问题，采用 naive 上采样平衡数据易引发过拟合或高资源语种效果下降。
### 方法关键点
1. 基于HuBERT式预训练目标，在2M小时音频语料上预训练Conformer结构的GigaAM Multilingual编码器
2. 预训练阶段引入集群级数据平衡策略，微调阶段采用领域感知采样方法，缓解头部语种主导的偏置问题
### 关键结果
在哈萨克语、吉尔吉斯语、乌兹别克语等中亚低资源语种上效果优于Whisper Large v3、Omnilingual-1B等开源强基线，自发语音场景提升显著，同时保持推理效率，模型已完全开源
