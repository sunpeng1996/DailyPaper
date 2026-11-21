---
title: 'Xing-Audio-NVVASR: Scaling and Refining Supervision for Joint Recognition
  of Speech and Non-Verbal Vocalizations'
title_zh: Xing-Audio-NVVASR：面向语音与非言语发声联合识别的监督优化方法
authors:
- Pengyu Xu
- Gang Liu
- Genliang Zhao
- Hongjie Chen
- Jian Kang
- Jie Lian
- Jie Li
- Yongxiang Li
affiliations:
- Xingchen AGI Lab, China Telecom Artificial Intelligence Technology Co. Ltd
arxiv_id: '2611.26000'
url: https://arxiv.org/abs/2611.26000
pdf_url: https://arxiv.org/pdf/2611.26000
published: '2026-11-19'
collected: '2026-11-21'
category: Other
direction: 多模态语音识别 · 非言语发声事件识别
tags:
- ASR
- Multi-modal
- Label Refinement
- Data Mining
- Speech Recognition
one_liner: 提出迭代标注优化的端到端语音非言语发声联合识别模型，性能大幅超越现有SOTA
practical_value: '- 双异构模型交叉校验+专属检测器查漏的弱标注迭代优化框架，可直接迁移到电商用户行为数据、商品评论数据的标签清洗场景，降低人工标注成本

  - 渐进式数据挖掘+累积保留人工确认标注的思路，可用于推荐系统长尾样本、冷启动类目的标注扩量，解决小样本训练数据不足问题

  - 单大模型做多模态多任务联合识别的方案，可迁移到电商语音客服场景的用户情绪、意图、语音指令联合识别任务，提升客服ASR系统的语义理解能力'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
语音与非言语发声（NVV，含笑声、咳嗽、呼吸等）联合识别面临训练数据稀缺、标签不准/缺失的核心瓶颈，现有公开语料对自发NVV的场景覆盖严重不足。
### 方法核心
- 采用渐进式数据挖掘+迭代监督优化的训练范式：双异构模型基于统一声学准则交叉校验标注，分歧样本送人工重标
- 新增补充呼吸检测器全量遍历语料，挖掘模型一致误判的漏检样本送人工审核，多轮迭代中累积的人工确认标注全程保留不覆盖
### 关键结果
5轮迭代后构建80万量级高质量标注语料，训练的1.7B参数端到端模型支持6类NVV inline标签识别；4个人工标注基准上，综合得分64.46，超SOTA模型StepAudio 3 Chat Preview 6.03分，6类Macro-F1位列9个参比模型第一，呼吸类F1超专业标注师14.4~31.57个百分点。
