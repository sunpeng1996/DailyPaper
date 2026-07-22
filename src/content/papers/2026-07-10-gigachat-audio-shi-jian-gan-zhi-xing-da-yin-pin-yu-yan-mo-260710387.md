---
title: 'GigaChat Audio: Time-aware Large Audio Language Model'
title_zh: GigaChat Audio：时间感知型大音频语言模型
authors:
- Aleksandr Kutsakov
- Mariia Sadovina
- Georgii Gospodinov
- Alexandr Maximenko
- Oleg Kutuzov
- Pavel Bogomolov
- Fyodor Minkin
affiliations:
- SaluteDevices, Russia
arxiv_id: '2607.10387'
url: https://arxiv.org/abs/2607.10387
pdf_url: https://arxiv.org/pdf/2607.10387
published: '2026-07-10'
collected: '2026-07-22'
category: LLM
direction: 大音频语言模型 · 长音频时序理解
tags:
- Large Audio Language Model
- Temporal Grounding
- Long-form Speech Processing
- Audio Question Answering
- Time-aware LLM
one_liner: 通过在音频token中插入周期性时间标记，实现最长120分钟音频的带精准时间戳的问答与摘要
practical_value: '- 处理长音频类业务内容（直播回放、客服通话、带货短视频）结构化时，可借鉴插入周期性时间标记的方案，让大模型输出对应内容的精准时间戳，方便用户快速定位片段

  - 长上下文时序信息建模可复用该方案：无需修改模型架构，仅通过输入侧插入时序标记+合成监督数据微调，即可大幅提升时序定位准确率，落地成本低

  - 可直接复用其时间标记频率、tokenization的 ablation 结论，根据业务场景的音频时长（15分钟带货视频/2小时直播）平衡准确率与计算成本'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
长音频（会议、客服通话、直播回放等）交互问答场景中，现有音频LLM时序定位能力差，常输出错误或粗粒度时间戳，无法支持用户跳转定位对应片段的需求。
### 方法关键点
1. 输入侧将周期性时间标记与连续音频token交叉拼接，无需修改模型底层架构；
2. 基于级联pipeline生成大规模合成监督数据，训练模型输出带明确时间戳的结果；
3. 训练时混合不同时长样本，最长支持120分钟音频输入。
### 关键结果
在长短音频基准测试集上时序定位准确率表现优异，支持时间锚定的片段描述、摘要功能；ablation验证时间表示方式、标记频率、tokenization、时长混合设计均会显著影响准确率与计算成本，已开源10B参数模型权重与数据集。
