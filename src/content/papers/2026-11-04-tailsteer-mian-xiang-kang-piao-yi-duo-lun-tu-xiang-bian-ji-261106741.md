---
title: 'TailSteer: Trajectory-Tail Steering for Drift-Resistant Multi-turn Image Editing'
title_zh: TailSteer：面向抗漂移多轮图像编辑的轨迹尾部调控方法
authors:
- Ruikang Li
- Zixuan Chen
- Jiarui Wu
- Mingde Yao
- Yiyuan Zhang
- Yujin Wang
- Hanming Deng
- Lewei Lu
- Tianfan Xue
affiliations:
- MMLab, CUHK
- SenseTime Research
- Shanghai Artificial Intelligence Laboratory
arxiv_id: '2611.06741'
url: https://arxiv.org/abs/2611.06741
pdf_url: https://arxiv.org/pdf/2611.06741
published: '2026-11-04'
collected: '2026-11-05'
category: Multimodal
direction: 多模态生成 · 多轮编辑抗漂移
tags:
- Multi-turn Editing
- Diffusion Model
- Visual Drift Mitigation
- Efficient Fine-tuning
- Multimodal Generation
one_liner: 提出仅微调扩散去噪轨迹尾部的训练框架，大幅降低多轮图像编辑的累积漂移且保留基模型能力
practical_value: '- 电商主图多轮改稿、Agent多轮内容生成等场景可复用「仅微调生成轨迹尾部、保留基模型前期预训练能力」的微调思路，避免全量微调破坏原有预训练先验

  - 多轮交互生成任务可借鉴无需人工标注多轮真值对、用原始未修改内容作为保留参考的自监督训练方式，大幅降低标注成本

  - 多轮生成的累积误差漂移问题，可参考将修正逻辑集中在生成最终阶段的设计，平衡抗漂移效果和推理性能开销'
score: 7
source: arxiv-cs.AI
depth: abstract
---

### 动机
现有单轮图像编辑模型多轮交互时，微小非预期修改会累积为严重视觉漂移；现有优化方案要么改动预训练先验导致基模型能力受损，要么推理端定制优化难以扩展到大模型。
### 方法关键点
提出TailSteer终态训练框架，核心遵循两个原则：1. 保持去噪前期动态与基模型完全一致，避免破坏预训练能力；2. 仅在去噪轨迹尾部集中施加保留修正，抑制细粒度偏差。校正信号从模型自身on-policy去噪滚动输出中学习，用未修改的源内容作为保留参考，无需人工标注多轮真值编辑对。
### 关键结果
在FLUX、SenseNova、Qwen系列模型上验证，15-20轮编辑后累积漂移大幅降低，同时基模型的文生图、单轮图像编辑性能几乎无损失
