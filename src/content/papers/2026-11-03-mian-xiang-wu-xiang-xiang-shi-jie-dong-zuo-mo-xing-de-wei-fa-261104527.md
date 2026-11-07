---
title: Future Representation Distillation for Imagination-free World Action Models
title_zh: 面向无想象世界动作模型的未来表示蒸馏方法
authors:
- Jaehyeong Jo
- Sangwon Jang
- Sihyun Yu
- Seonghyeon Ye
- Yekyung Nah
- Hojung Jung
- Kimin Lee
- Sung Ju Hwang
affiliations:
- KAIST
arxiv_id: '2611.04527'
url: https://arxiv.org/abs/2611.04527
pdf_url: https://arxiv.org/pdf/2611.04527
published: '2026-11-03'
collected: '2026-11-07'
category: Other
direction: 世界动作模型 · 视频扩散表征蒸馏
tags:
- Representation Distillation
- Video Diffusion Model
- World Model
- Robot Control
- Knowledge Distillation
one_liner: 通过表征蒸馏复用预训练视频扩散模型先验，无需生成未来视频即可实现高效机器人动作预测
practical_value: '- 大模型预训练先验蒸馏思路可迁移：将生成类大模型（扩散、LLM）的隐层预测知识蒸馏到轻量编码器，无需走完整生成链路即可拿到预测性表征，适合推荐系统实时排序/召回场景降本

  - 无标注数据复用方法可借鉴：仅用视频/序列演示数据即可蒸馏先验，无需下游任务标注，可用于电商推荐冷启动，利用海量无标注用户行为视频/浏览序列训练预编码器

  - 实时性优化思路可复用：用蒸馏后的小编码器替代大模型生成链路，14B backbone下仍能做到11Hz实时推理，可迁移到Agent实时决策、推荐低延迟响应场景优化'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
World Action Models (WAMs) 依赖预训练视频扩散模型生成未来视频支撑机器人控制，但迭代去噪推理成本极高，且视觉预测误差会传导降低动作预测准确率。
### 方法关键点
1. 提出DreamFree框架，将冻结的预训练视频扩散模型的未来表征作为监督，蒸馏训练仅需当前观测输入的预测视觉编码器，无需生成未来视频即可获取预测性知识
2. 单独训练动作模块从蒸馏得到的视觉编码器输出中提取动作相关信息，直接输出控制指令
### 关键结果
- 真实+模拟机器人任务成功率超过SOTA VLA、WAM
- 14B参数量视频扩散backbone下可实现11Hz实时闭环控制
- 可跨形态复用无动作标注的演示视频学习新任务
