---
title: 'Self Gradient Forcing: Native Long Video Extrapolation'
title_zh: 自梯度强制：原生长视频时序外推方法
authors:
- Junhao Zhuang
- Shiyi Zhang
- Yuxuan Bian
- Yaowei Li
- Yawen Luo
- Yijun Liu
- Weiyang Jin
- Songchun Zhang
- Xianglong He
- Xuying Zhang
affiliations:
- Joy Future Academy, JD
arxiv_id: '2607.20368'
url: https://arxiv.org/abs/2607.20368
pdf_url: https://arxiv.org/pdf/2607.20368
published: '2026-07-21'
collected: '2026-07-23'
category: Other
direction: 长视频自回归生成 · 训练策略优化
tags:
- Autoregressive Generation
- Diffusion Model
- Training Strategy
- KV Cache
- Long Video Generation
one_liner: 提出双阶段自梯度强制训练策略，解决自回归视频扩散的历史上下文梯度缺口，提升长视频生成一致性
practical_value: '- 自回归类生成任务（如商品文案/直播脚本/推荐理由长序列生成）可复用双Pass训练思路，解决KV Cache梯度冻结导致的长序列一致性差问题

  - 无需全序列反向传播的梯度监督方案，可降低长序列自回归生成任务的训练显存开销，适配大参数量LLM/多模态生成场景

  - 短训练窗口生成超长序列的优化思路，可迁移至电商内容生成场景（如30s训练样本生成分钟级带货脚本/直播切片内容）'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
自回归视频扩散的Self Forcing训练虽缓解暴露偏差，但历史KV cache仅作为冻结状态使用，未来损失无法监督早期隐层生成更适配后续推理的KV表征，存在历史上下文梯度缺口，长视频生成一致性差。
### 方法关键点
提出Self Gradient Forcing（SGF）双Pass训练策略：1. Pass 1无梯度执行和推理对齐的自回归滚动生成，在采样的去噪退出步记录自生成上下文与输入噪声隐层；2. Pass 2并行对记录的退出步做上下文梯度重建，将生成上下文作为梯度截断的干净隐层输入，重计算上下文KV表征与未来到上下文的因果注意力，补充缺失的记忆写入监督信号，无需全序列反向传播。
### 关键结果
相比基线Self Forcing，长视频外推在主体一致性、背景布局稳定性、时序连贯性指标上全面占优；仅用5s训练窗口即可外推生成数分钟长度的连贯视频。
