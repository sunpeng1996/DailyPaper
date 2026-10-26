---
title: 'DirCast: Live Esports Directing and Commentary with a Single Streaming Video-Language
  Model'
title_zh: DirCast：基于单流视频语言模型的电竞赛事实时导播与解说
authors:
- Zixian Gao
- Lixin Xiu
- Penghao Luo
- Xiangcheng Cao
- Ziqi Cai
- Zhen Li
- Erwin Wu
- Kaipeng Zhang
affiliations:
- Alaya Lab
- The University of Tokyo
- Georgia Institute of Technology
- Peking University
- Institute of Science Tokyo
arxiv_id: '2610.31734'
url: https://arxiv.org/abs/2610.31734
pdf_url: https://arxiv.org/pdf/2610.31734
published: '2026-10-21'
collected: '2026-10-26'
category: Multimodal
direction: 多模态视频大模型·实时流内容生产
tags:
- Video-LLM
- Streaming Processing
- Multimodal
- Real-time Generation
- Multi-task Learning
one_liner: 提出单流视频语言模型DirCast，同时实现电竞赛事实时导播与解说双任务
practical_value: '- 多分辨率分层处理流输入技巧可复用：低分辨率快速扫描全量候选（如推荐召回池、直播多路流），高分辨率精细处理选中目标，平衡推理性能与耗时，适配实时推荐、直播实时文案生成场景

  - 滑动上下文过期机制可借鉴：仅保留核心有效历史（如用户近期交互、已播出内容），丢弃冗余信息，可控KV cache开销，适配长时会话Agent、无限流推荐场景

  - 单模型多任务协同范式可迁移：用同一个多模态模型同时完成决策（如推荐排序、流选择）+ 生成（如推荐理由、商品解说文案）任务，降低多模块链路的延迟与一致性问题'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有流视频语言模型仅能基于人工预导播的赛事流做解说，无法覆盖「多路摄像头选流导播+实时解说」的全链路直播生产需求，且长时流处理的上下文存储开销不可控，无法支撑无限时长直播。
### 方法关键点
1. 单模型协同完成导播+解说双任务：每秒先低分辨率扫描全量选手摄像头，通过hold-or-switch模块决策是否切流、切向哪路；选中流用高分辨率读取后生成对应解说
2. 上下文仅保留已播出内容与对应解说，其余视角信息自动过期，可支撑任意长度流处理且推理成本可控
3. 构建包含27场专业Dota2赛事的数据集，覆盖每英雄独立摄像头、人工导播决策、专业解说文本三类标注
### 关键结果
导播效果优于规则基线及包括GPT-5在内的零-shot导播方案；解说在Proact-VL评测中对比GPT-4o的胜率达29.2%，远高于仅观看人工导播流的最强基线模型的19.4%胜率
