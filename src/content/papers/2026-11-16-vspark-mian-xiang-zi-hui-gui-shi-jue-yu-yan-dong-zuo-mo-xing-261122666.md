---
title: 'VSpark: Speculative Decoding for Autoregressive Vision-Language-Action Models'
title_zh: VSpark：面向自回归视觉-语言-动作模型的推测解码
authors:
- Suho Yoo
- Youngjoon Jang
- Hyebin Cho
- Taeyeop Lee
- Jaewook Jeong
- Joon Son Chung
affiliations:
- KAIST
- VGG, University of Oxford
arxiv_id: '2611.22666'
url: https://arxiv.org/abs/2611.22666
pdf_url: https://arxiv.org/pdf/2611.22666
published: '2026-11-16'
collected: '2026-11-20'
category: LLM
direction: 多模态大模型 · 推测解码推理加速
tags:
- Speculative Decoding
- VLA
- Inference Acceleration
- Autoregressive Model
- Lossless Decoding
one_liner: 提出三项优化改进推测解码，实现自回归VLA模型无损失解码最高2.1倍加速
practical_value: '- 生成式推荐/Agent推理加速场景可借鉴特征对齐思路训练draft小模型，对齐大模型隐层特征而非仅输出token，大幅提升推测解码的token命中率，降低推理
  latency

  - 可复用延续复用机制，被拒绝draft分支上大模型已计算的结果不直接丢弃，作为下一轮验证候选，减少重复计算，适配KV cache优化链路

  - 训练draft小模型时可引入校准噪声扩充训练样本，提升小模型对电商场景多变的用户query、物品特征分布的泛化性，进一步提升加速效果'
score: 7
source: huggingface-daily
depth: abstract
---

## 动机
自回归视觉-语言-动作模型（VLA）逐token生成动作的推理模式延迟高，传统推测解码在动作生成场景下命中率极低：大量语义接近的动作token因与大模型输出不完全匹配被直接拒绝，加速效果受限。

## 方法关键点
核心设计三点：1）用校准后的动作噪声采集轨迹数据，扩充draft小模型的训练状态覆盖范围；2）采用特征对齐训练，让draft模型拟合大VLA模型的隐层特征而非仅对齐输出token，提升draft准确率；3）新增延续复用机制，被拒绝draft路径上大模型已计算的预测结果不丢弃，直接作为下一轮验证的候选集。

## 关键结果
在4种搭载不同动作分词器的VLA、4个机器人操作基准测试上，实现1.28x~2.10x的无损失解码加速，无精度损失。
