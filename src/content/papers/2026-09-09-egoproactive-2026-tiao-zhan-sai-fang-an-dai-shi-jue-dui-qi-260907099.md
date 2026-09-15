---
title: 'Ambient @ EgoProactive 2026 : Proactive Egocentric Assistance with Visually
  Grounded Supervision'
title_zh: EgoProactive 2026 挑战赛方案：带视觉对齐监督的主动第一视角辅助系统
authors:
- Logesh Kumar Umapathi
affiliations:
- TeamAmbient
arxiv_id: '2609.07099'
url: https://arxiv.org/abs/2609.07099
pdf_url: https://arxiv.org/pdf/2609.07099
published: '2026-09-09'
collected: '2026-09-15'
category: Agent
direction: 主动穿戴Agent 干预决策优化
tags:
- Proactive Agent
- Visual Grounding
- Synthetic Annotation
- Video LLM
- Binary Classification
one_liner: 将主动穿戴辅助的干预决策转为单Token分类，结合视觉对齐标注获EgoProactive挑战赛大模型组第一、2B组第二
practical_value: '- 所有涉及二分类触发的LLM场景（如广告插播、PUSH推送决策）均可复用单Token分类改造思路，相比自由生成能大幅提升分类指标

  - 小样本标注场景优先保障标注与任务模态对齐质量，而非盲目扩大低质量标注规模，可通过工具调用Agent生成匹配模态的监督数据

  - 正负样本不均衡的分类任务内部调优时，可优先用G-mean替代macro-F1做选型指标，能更好平衡两类错误的发生概率'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
ECCV 2026穿戴AI挑战赛EgoProactive赛道要求第一视角穿戴助手每8秒视频段判断是否主动干预，原有自由生成决策方案准确率低，且官方仅提供验证集标注，标注资源稀缺。
### 方法关键点
1. 重构任务范式：将干预决策从生成`interrupt<utterance>`/`silent`的自由生成任务，简化为`yes/no`单Token分类任务，基于两个Token重归一化概率输出最终决策；
2. 标注增强：用工具调用型视频Agent逐片段检查并标注干预时间戳，生成视觉对齐的监督数据，放弃规模更大、成本更低但无视觉对齐的纯 narration 标注。
### 关键结果
单Token分类改造相比自由生成，macro-F1提升0.249，G-mean提升0.30；方案最终获得大模型组第1、≤2B参数组第2，验证了visual grounding质量比标注规模对任务增益更高
