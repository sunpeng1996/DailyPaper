---
title: 'UniSwap: Streaming Audio-Visual Identity Swapping for Talking Videos'
title_zh: UniSwap：面向口播视频的流式音视频身份替换框架
authors:
- Yuxuan Zhang
- Haozhong Xiong
- Jiayi Song
- Jinpeng Yu
- Yang Shi
- Jiaming Liu
- Ruihua Huang
- Liwei Wang
affiliations:
- The Chinese University of Hong Kong
- Qwen Applications Business Group of Alibaba
arxiv_id: '2608.11752'
url: https://arxiv.org/abs/2608.11752
pdf_url: https://arxiv.org/pdf/2608.11752
published: '2026-08-12'
collected: '2026-08-14'
category: Multimodal
direction: 多模态音视频生成 · 流式推理优化
tags:
- Multimodal Generation
- Diffusion Transformer
- LoRA
- KV Cache
- Streaming Inference
one_liner: 首个单架构联合流式音视频身份替换框架，实现低延迟高一致性长视频生成
practical_value: '- Multi-LoRA Switching共享冻结主干的方案可复用在电商多场景多模态生成任务部署，大幅降低显存占用与部署成本

  - swap-and-reconstruct无对齐标注训练对构造方法，可迁移到数字人定制等缺少跨身份对齐标注的多模态生成场景

  - Feature-RoPE分解解决长序列推理位置超出训练范围的思路，可用于长视频/长文本生成类Agent的稳定推理优化

  - DMD将扩散采样步从30压缩到3的trick，可复用在直播实时数字人换脸、实时互动等低延迟多模态生成场景'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有口播视频身份替换方案对音视觉模态单独优化，一致性难保障，同时面临跨身份对齐训练样本稀缺、推理延迟高、长序列生成不稳定等问题。
### 方法关键点
- 单架构音视频扩散Transformer，联合完成人脸外观+音色迁移，保留原视频动作、内容与时序
- 自研swap-and-reconstruct训练流水线，消除原始clip身份信息后以原片为重构目标，解决标注不足问题
- 三阶段渐进适配：上下文预训练练联合替换能力，条件流式适配支持块因果KV cache生成，自激励DMD将每块去噪步从30压缩到3
- Multi-LoRA Switching实现多任务共享冻结主干，Feature-RoPE分解保证长序列推理位置在训练范围内
### 关键结果
单H100上3步采样推理速度达13.6FPS，支持小时级长视频稳定生成，音视频同步性、身份保留效果达SOTA。
